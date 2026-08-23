#!/usr/bin/env python3
"""
Zero-dependency Pure Python QR Code Generator (ISO/IEC 18004).
Generates QR Code matrices and PIL Images matching standard JS QRCode with Level H & center logo embedding.
"""

import os
from typing import List, Tuple, Optional
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

# Galois Field GF(256) tables with primitive polynomial 0x11D (285)
GF_EXP = [0] * 512
GF_LOG = [0] * 256
_x = 1
for _i in range(255):
    GF_EXP[_i] = _x
    GF_LOG[_x] = _i
    _x <<= 1
    if _x >= 256:
        _x ^= 0x11D
for _i in range(255, 512):
    GF_EXP[_i] = GF_EXP[_i - 255]

def gf_mul(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return GF_EXP[GF_LOG[a] + GF_LOG[b]]

def poly_mul(p1: List[int], p2: List[int]) -> List[int]:
    result = [0] * (len(p1) + len(p2) - 1)
    for i, c1 in enumerate(p1):
        for j, c2 in enumerate(p2):
            result[i + j] ^= gf_mul(c1, c2)
    return result

def rs_generator_poly(num_ec: int) -> List[int]:
    g = [1]
    for i in range(num_ec):
        g = poly_mul(g, [1, GF_EXP[i]])
    return g

def rs_encode(data: List[int], num_ec: int) -> List[int]:
    gen = rs_generator_poly(num_ec)
    padded = data + [0] * num_ec
    msg = list(padded)
    for i in range(len(data)):
        lead = msg[i]
        if lead != 0:
            for j in range(len(gen)):
                msg[i + j] ^= gf_mul(gen[j], lead)
    return msg[len(data):]

# QR Code Specifications for Error Correction Level H:
# Table format: (total_codewords, ec_codewords_per_block, num_blocks_g1, data_per_block_g1, num_blocks_g2, data_per_block_g2)
EC_TABLE_H = {
    1:  (26,   17, 1, 9,   0, 0),
    2:  (44,   28, 1, 16,  0, 0),
    3:  (70,   22, 2, 13,  0, 0),
    4:  (100,  16, 4, 9,   0, 0),
    5:  (134,  22, 2, 11,  2, 12),
    6:  (172,  28, 4, 15,  0, 0),
    7:  (196,  26, 4, 13,  1, 14),
    8:  (242,  26, 4, 14,  2, 15),
    9:  (292,  24, 4, 12,  4, 13),
    10: (346,  28, 6, 15,  2, 16),
    11: (404,  24, 4, 12,  6, 13),
    12: (466,  28, 7, 14,  4, 15),
    13: (532,  22, 12, 11, 4, 12),
    14: (581,  24, 11, 12, 5, 13),
}

ALIGNMENT_LOCATIONS = {
    2: [6, 18],
    3: [6, 22],
    4: [6, 26],
    5: [6, 30],
    6: [6, 34],
    7: [6, 22, 38],
    8: [6, 24, 42],
    9: [6, 26, 46],
    10: [6, 28, 50],
    11: [6, 30, 54],
    12: [6, 32, 58],
    13: [6, 34, 62],
    14: [6, 26, 46, 66],
}

# Format bits for Error Correction Level H (0b10) with BCH(15, 5) error correction & mask 0x5412
G15 = 0x537
MASK15 = 0x5412

def get_format_bits_h(mask_pattern: int) -> int:
    data = (2 << 3) | mask_pattern
    bch = data << 10
    for i in range(14, 9, -1):
        if (bch >> i) & 1:
            bch ^= (G15 << (i - 10))
    return ((data << 10) | bch) ^ MASK15

class BitBuffer:
    def __init__(self):
        self.bits: List[int] = []

    def put(self, val: int, length: int):
        for i in range(length - 1, -1, -1):
            self.bits.append((val >> i) & 1)

    def to_bytes(self) -> List[int]:
        res = []
        for i in range(0, len(self.bits), 8):
            chunk = self.bits[i:i+8]
            byte_val = 0
            for b in chunk:
                byte_val = (byte_val << 1) | b
            if len(chunk) < 8:
                byte_val <<= (8 - len(chunk))
            res.append(byte_val)
        return res

def encode_data(text: str, version: int) -> List[int]:
    data_bytes = text.encode("utf-8")
    bb = BitBuffer()
    # 8-bit byte mode indicator: 0100
    bb.put(0b0100, 4)
    # Character count indicator
    count_bits = 8 if version < 10 else 16
    bb.put(len(data_bytes), count_bits)
    # Data bytes
    for b in data_bytes:
        bb.put(b, 8)

    spec = EC_TABLE_H[version]
    total_data_codewords = spec[2] * spec[3] + spec[4] * spec[5]
    total_data_bits = total_data_codewords * 8

    # Terminator
    rem = total_data_bits - len(bb.bits)
    if rem > 0:
        bb.put(0, min(4, rem))

    # Pad to 8-bit boundary
    while len(bb.bits) % 8 != 0:
        bb.bits.append(0)

    # Pad codewords (0xEC, 0x11)
    raw = bb.to_bytes()
    pad = [0xEC, 0x11]
    p_idx = 0
    while len(raw) < total_data_codewords:
        raw.append(pad[p_idx])
        p_idx = (p_idx + 1) % 2

    # Split into blocks and calculate EC
    blocks_data = []
    blocks_ec = []
    idx = 0
    num_ec = spec[1]

    # Group 1
    for _ in range(spec[2]):
        cnt = spec[3]
        blk = raw[idx:idx+cnt]
        idx += cnt
        blocks_data.append(blk)
        blocks_ec.append(rs_encode(blk, num_ec))

    # Group 2
    for _ in range(spec[4]):
        cnt = spec[5]
        blk = raw[idx:idx+cnt]
        idx += cnt
        blocks_data.append(blk)
        blocks_ec.append(rs_encode(blk, num_ec))

    # Interleave data codewords
    final_codewords = []
    max_data_len = max(len(b) for b in blocks_data)
    for i in range(max_data_len):
        for b in blocks_data:
            if i < len(b):
                final_codewords.append(b[i])

    # Interleave EC codewords
    for i in range(num_ec):
        for ec in blocks_ec:
            final_codewords.append(ec[i])

    return final_codewords

def find_version(text: str) -> int:
    data_len = len(text.encode("utf-8"))
    for ver in range(1, 15):
        spec = EC_TABLE_H[ver]
        count_bits = 8 if ver < 10 else 16
        cap = (spec[2] * spec[3] + spec[4] * spec[5]) * 8
        needed = 4 + count_bits + data_len * 8
        if needed <= cap:
            return ver
    raise ValueError(f"Payload too large for QR generator: {len(text)} bytes")

class QRCodeMatrix:
    def __init__(self, version: int):
        self.version = version
        self.size = 17 + version * 4
        self.grid: List[List[Optional[int]]] = [[None] * self.size for _ in range(self.size)]
        self.is_reserved: List[List[bool]] = [[False] * self.size for _ in range(self.size)]

    def set_module(self, r: int, c: int, val: int, reserved: bool = True):
        if 0 <= r < self.size and 0 <= c < self.size:
            self.grid[r][c] = val
            if reserved:
                self.is_reserved[r][c] = True

    def add_finder(self, row: int, col: int):
        for r in range(-1, 8):
            for c in range(-1, 8):
                gr, gc = row + r, col + c
                if 0 <= gr < self.size and 0 <= gc < self.size:
                    if 0 <= r <= 6 and 0 <= c <= 6:
                        val = 1 if (r in (0, 6) or c in (0, 6) or (2 <= r <= 4 and 2 <= c <= 4)) else 0
                    else:
                        val = 0
                    self.set_module(gr, gc, val, True)

    def add_alignment(self, row: int, col: int):
        if self.is_reserved[row][col]:
            return
        for r in range(-2, 3):
            for c in range(-2, 3):
                val = 1 if (abs(r) == 2 or abs(c) == 2 or (r == 0 and c == 0)) else 0
                self.set_module(row + r, col + c, val, True)

    def setup_structure(self):
        # Finders
        self.add_finder(0, 0)
        self.add_finder(0, self.size - 7)
        self.add_finder(self.size - 7, 0)

        # Alignment
        if self.version >= 2:
            coords = ALIGNMENT_LOCATIONS[self.version]
            for r in coords:
                for c in coords:
                    self.add_alignment(r, c)

        # Timing
        for i in range(8, self.size - 8):
            val = 1 if (i % 2 == 0) else 0
            if not self.is_reserved[6][i]:
                self.set_module(6, i, val, True)
            if not self.is_reserved[i][6]:
                self.set_module(i, 6, val, True)

        # Dark module
        self.set_module(4 * self.version + 9, 8, 1, True)

        # Format info space reservation
        for i in range(9):
            if not self.is_reserved[8][i]:
                self.set_module(8, i, 0, True)
            if not self.is_reserved[i][8]:
                self.set_module(i, 8, 0, True)
        for i in range(self.size - 8, self.size):
            if not self.is_reserved[8][i]:
                self.set_module(8, i, 0, True)
        for i in range(self.size - 7, self.size):
            if not self.is_reserved[i][8]:
                self.set_module(i, 8, 0, True)

    def place_data(self, codewords: List[int], mask_pattern: int):
        bits = []
        for cw in codewords:
            for b in range(7, -1, -1):
                bits.append((cw >> b) & 1)

        spec = EC_TABLE_H[self.version]
        total_data_bits = spec[0] * 8
        bits = bits[:total_data_bits]

        bit_idx = 0
        right = self.size - 1
        upward = True

        while right > 0:
            if right == 6:
                right -= 1

            rows = range(self.size - 1, -1, -1) if upward else range(self.size)
            for r in rows:
                for col in (right, right - 1):
                    if not self.is_reserved[r][col]:
                        val = bits[bit_idx] if bit_idx < len(bits) else 0
                        bit_idx += 1

                        # Standard mask 0: (r + col) % 2 == 0
                        mask = (r + col) % 2 == 0
                        self.grid[r][col] = val ^ (1 if mask else 0)

            upward = not upward
            right -= 2

    def apply_format_info(self, mask_pattern: int):
        fmt = get_format_bits_h(mask_pattern)
        bits = [(fmt >> (14 - i)) & 1 for i in range(15)]

        # Top-left horizontal & vertical
        coords_top = [
            (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 7), (8, 8),
            (7, 8), (5, 8), (4, 8), (3, 8), (2, 8), (1, 8), (0, 8)
        ]
        for i, (r, c) in enumerate(coords_top):
            self.grid[r][c] = bits[i]

        # Bottom-left and Top-right
        for i in range(7):
            self.grid[self.size - 1 - i][8] = bits[i]
        for i in range(8):
            self.grid[8][self.size - 8 + i] = bits[7 + i]

def generate_qr_matrix(text: str) -> List[List[int]]:
    version = find_version(text)
    codewords = encode_data(text, version)
    qr = QRCodeMatrix(version)
    qr.setup_structure()
    qr.place_data(codewords, 0)
    qr.apply_format_info(0)
    return [[1 if cell == 1 else 0 for cell in row] for row in qr.grid]

def generate_qr_image(
    text: str,
    box_size: int = 4,
    border: int = 2,
    fg_color: Tuple[int, int, int, int] = (17, 24, 39, 255),
    bg_color: Tuple[int, int, int, int] = (255, 255, 255, 255),
    logo_path: Optional[str] = None,
    logo_size_ratio: float = 0.24
) -> Image.Image:
    matrix = generate_qr_matrix(text)
    size = len(matrix)
    img_size = (size + border * 2) * box_size
    img = Image.new("RGBA", (img_size, img_size), bg_color)
    pixels = img.load()

    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 1:
                x_start = (c + border) * box_size
                y_start = (r + border) * box_size
                for dy in range(box_size):
                    for dx in range(box_size):
                        pixels[x_start + dx, y_start + dy] = fg_color

    # Embed center logo/favicon if provided
    if logo_path and Path(logo_path).exists():
        try:
            logo = Image.open(logo_path).convert("RGBA")
            l_size = int(img_size * logo_size_ratio)
            lx = (img_size - l_size) // 2
            ly = (img_size - l_size) // 2
            pad = max(3, int(l_size * 0.12))
            
            # White rounded badge behind logo
            badge = Image.new("RGBA", (img_size, img_size), (0, 0, 0, 0))
            b_draw = ImageDraw.Draw(badge)
            b_draw.rounded_rectangle(
                [(lx - pad, ly - pad), (lx + l_size + pad, ly + l_size + pad)],
                radius=int(pad * 1.5),
                fill=(255, 255, 255, 255),
                outline=(226, 232, 240, 255),
                width=1
            )
            
            # Soft badge shadow
            b_shadow = Image.new("RGBA", (img_size, img_size), (0, 0, 0, 0))
            bs_draw = ImageDraw.Draw(b_shadow)
            bs_draw.rounded_rectangle(
                [(lx - pad + 1, ly - pad + 2), (lx + l_size + pad + 1, ly + l_size + pad + 3)],
                radius=int(pad * 1.5),
                fill=(0, 0, 0, 45)
            )
            b_shadow = b_shadow.filter(ImageFilter.GaussianBlur(radius=3))
            
            img = Image.alpha_composite(img, b_shadow)
            img = Image.alpha_composite(img, badge)
            
            resized_logo = logo.resize((l_size, l_size), Image.Resampling.LANCZOS)
            img.paste(resized_logo, (lx, ly), resized_logo)
        except Exception as e:
            print(f"Warning: could not embed logo into QR code: {e}")

    return img

if __name__ == "__main__":
    test_url = "https://jochen.kirstaetter.name/sql-server-on-gcp"
    logo_file = "posts/favicon.png"
    img = generate_qr_image(test_url, box_size=4, border=2, logo_path=logo_file)
    print(f"Level H QR Code with logo generated. Size: {img.size}")
