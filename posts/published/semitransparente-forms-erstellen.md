---
uid: semitransparente-forms-erstellen
title: Semitransparente 'Forms' erstellen
slug: semitransparente-forms-erstellen
date: 2006-10-29
status: published
type: post
description: Semitransparente 'Forms' erstellen Ausgehend von meinem letzten Beitrag zu Projekt Sunshine möchte ich heute ein paar Tipps & Tricks darüber geben.
tags:
- Development
keywords: Development
metaTitle: Semitransparente 'Forms' erstellen
metaDescription: Semitransparente 'Forms' erstellen Ausgehend von meinem letzten Beitrag zu Projekt Sunshine möchte ich heute ein paar Tipps & Tricks darüber geben.
image: ''
ogTitle: Semitransparente 'Forms' erstellen
ogDescription: Ausgehend von meinem letzten Beitrag zu Projekt Sunshine möchte ich heute ein paar Tipps & Tricks darüber geben, wie man den Semitransparenz-Effekt selbst produzieren kann. Gleich vorab möchte ich...
layout: post
bodyClass: post-template tag-development
postClass: post tag-development
isPost: true
isPage: false
isDraft: false
isScheduled: false
isTagPage: false
isTagsIndexPage: false
isAuthorPage: false
isHome: false
author: Jochen Kirstätter
authorTwitter: '@jkirstaetter'
authorFacebook: https://facebook.com/jochen.kirstaetter
website: ''
location: ''
authorImage: content/images/2018/10/JoKi_StAubin_100px.webp
authorSlug: joki
canonicalUrl: https://jochen.kirstaetter.name/semitransparente-forms-erstellen/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-10-29T00:00:00Z
updatedAt: 2018-04-02T08:39:03Z
excerpt: Ausgehend von meinem letzten Beitrag zu Projekt Sunshine möchte ich heute ein paar Tipps & Tricks darüber geben, wie man den Semitransparenz-Effekt selbst produzieren kann. Gleich vorab möchte ich...
twitterTitle: Semitransparente 'Forms' erstellen
twitterDescription: Ausgehend von meinem letzten Beitrag zu Projekt Sunshine möchte ich heute ein paar Tipps & Tricks darüber geben, wie man den Semitransparenz-Effekt selbst produzieren kann. Gleich vorab möchte ich...
twitterImage: 
facebookTitle: Semitransparente 'Forms' erstellen
facebookDescription: Ausgehend von meinem letzten Beitrag zu Projekt Sunshine möchte ich heute ein paar Tipps & Tricks darüber geben, wie man den Semitransparenz-Effekt selbst produzieren kann. Gleich vorab möchte ich...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Ausgehend von meinem letzten Beitrag zu Projekt Sunshine möchte ich heute ein paar Tipps & Tricks darüber geben, wie man den Semitransparenz-Effekt selbst produzieren kann. Gleich vorab möchte ich sagen, dass diverse Lösungsansätze nicht von mir stammen, sondern aus diversen Blogs der VFP-Community entlehnt sind. Ich habe lediglich die verschiedenen Teillösungen ein wenig zusammengeschrieben und daraus generische Komponenten erzeugt. Oder zumindest versucht... 😁

Als Programmierbasis verwende ich VFP 9.0 SP1 und unsere Komponentenbibliothek Acodey, welche in diesem Zusammenhang lediglich einige Helfermethoden zur Verfügung stellt, welche kein Hindernis zur Verwendung ohne Acodey darstellen.

## Transparenz in VFP-Forms realisieren
Die Erzeugung von Transparenz, oder besser gesagt Opacity, bei einer VFP-Form geht mittels der Windows 32 API relativ einfach. Man braucht dazu lediglich zwei API-Funktionen und schreibt die folgenden Zeilen etwa in die Init-Methode einer Form:  

```foxpro
#Define GWL_EXSTYLE -20
#Define WS_EX_LAYERED 0x80000

Declare SetWindowLong In WIN32API ;
  Integer, Integer, Integer

Declare SetLayeredWindowAttributes In WIN32API ;
  Integer, String, Integer, Integer

Local lnOpacity
m.lnOpacity = 255 * This.nOpacity / 100 && This.nOpacity = 75 (%)
SetWindowLong(This.HWnd, GWL_EXSTYLE, WS_EX_LAYERED)
SetLayeredWindowAttributes(This.HWnd, 0, m.lnOpacity, 2)
```
  
Sieht ja schon mal recht einfach und effektiv aus. Nur gibt's dabei leider ein Problem. Erstens funktioniert es nur bei Top-Level-Formularen (ShowWindow = 2) und es werden sämtliche Controls auf dem Formular gleichermaßen transparent angezeigt. Sobald die Form In-Screen verwendet wird, haben die Codeanweisungen keine Wirkung. Well, zumindest kann man damit stylische Popups oder Tooltipps schreiben. Insbesondere wenn man den Opacity-Grad mittels Timer verändert. Anbei mal ein Screenshot mit dem Ergebnis:

![Opacity-Effektiv bei VFP-Form mit Thisform.ShowWindow = 2](https://jochen.kirstaetter.name/files/TransparentForm.png)  
*Opacity-Effektiv bei VFP-Form mit Thisform.ShowWindow = 2*

In den mitgelieferten Solution Samples in VFP ist übrigens ein entsprechendes Beispiel zu finden.  
`Do Home(2) + "solutionsolution.app"`  
Dort dann unter *Forms :: Transparent forms* schauen.

## Formulare vor der Kamera
Der zweite Ansatz besteht in der Anwendung des Blue-/Green-Screen Verfahrens wie man es bei der Filmproduktion kennt. Die Grundlage des Verhahrens ist, dass man diverse Regionen eines Formulars mit einem bestimmten Farbwert - etwa Rgb(0,0,255) oder Rgb(0,255,0) - maskiert und diese Regionen wiederum mittels Win32 API Funktionen aus dem Formular rausschneidet und damit Platz für den Hintergrund schaffen kann. Diesen Lösungsansatz habe ich zuerst bei [VFPSkin](https://www.vfpskin.com.ar/) entdecken können. Aber auch andere VFP-Coder in der Community, namentlich [Craig Boyd](https://www.sweetpotatosoftware.com/SPSBlog/PermaLink,guid,9a91dea3-6413-42e9-aeff-f0097937474d.aspx) und [Bernard Bout](https://weblogs.foxite.com/bernardbout/archive/2006/10/28/2765.aspx), haben bereits damit experimentiert. In den mitgelieferten Solution Samples von Visual FoxPro findet man ebenfalls einen Verweis auf diese Technik. Unter *New in Visual FoxPro 8.0 :: Creating Irregularly shaped windows* findet sich de entsprechende Quellcode für die Umsetzung. Die Lösungen von VFPSkin und Craig Boyd funktionieren jedoch auch für In-Screen-Formulare.

Soweit sieht das ja schon ganz gut aus, aber... der eigentliche Effekt der Semitransparenz haben wir bisher noch nicht erreichen können. Und das größte Problem ist, dass die transparenten Stellen des Formulars immer transparent, also auch Controls 'verschwinden'. Bernard Bout beschreibt in seinem Artikel [Visual Foxpro shows its Glass!](https://weblogs.foxite.com/bernardbout/archive/2006/10/28/2765.aspx) zwar die Vorgehensweise unter Verwendung von zwei überlagerten Formularen, aber ich halte das für zu aufwendig. Letztendlich ist es Ansichtssache.

## Controls mit BackStyle = 0
VFP bietet von Haus aus bereits Transparenz für einige Controls an, leider befindet die Form-Klasse nicht darunter. Es wäre ja auch zu einfach... 🤪 Wenn man jedoch bedenkt, dass eine Form lediglich ein visueller Container mit ein paar netten Eigenschaften wie Titlebar samt Buttons, Datenumgebung, Beweglichkeit und Größenveränderung ist, dann kommt man doch recht schnell auf die Idee einen 'Form-Container' zu erstellen. Die Vorteile liegen meines Erachtens klar auf der Hand. Man erstellt sich eine generische Basisklasse für diesen Container und simuliert die Funktionsweise eines Formulars. Diesem verpasst man eine eigene Titlebar - hier einfach ein Shape -, ein Icon und die ControlButtons (Minimize, Maximize und Close).

![Generische Basisklasse für Container-basierte 'Form'](https://jochen.kirstaetter.name/files/TransparentContainer.png)  
*Generische Basisklasse für Container-basierte 'Form'*

Weiterhin stattet man dann den Container mit einigen Eigenschaften, wie ein Formular aus: Caption (mit Assign), Icon (mit Assign), Movable, nXCoord und nYCoord (wird für MouseMove gebraucht). Dazu kommen noch ein paar Methoden wie Show, Hide, EventClick und EventMouseMove und fertig ist die Basisklasse.

Warum der ganze Aufwand eigentlich? Nun, der Trick hierbei liegt in der Möglichkeit, dass man auf diese Art und Weise sowohl vollständige Freiheit in der optischen Gestaltung von 'Formularen' besitzt und absolut problemlos mit Opacity in diversen Teilbereichen des Containers arbeiten kann.

## Den Container mit den Formfähigkeiten ausstatten
Damit unser Container das Look & Feel einer Form erhält, müssen wir noch ein paar Zeilen Code in die Basisklasse schreiben. Fangen wir mit den einfachen Dingen, wie etwa Caption und Icon an:  

```foxpro
Procedure This.Caption_Assign
  *===================================================
  * Weitergabe des Parameters an das zuständige Control.
  *===================================================
  Lparameters vNewVal

  This.lblCaption.Caption = m.vNewVal
  This.Caption = m.vNewVal
EndProc

Procedure This.Icon_Assign
  *===================================================
  * Weitergabe des Parameters an das zuständige Control.
  *===================================================
  Lparameters vNewVal

  This.imgIcon.Picture = m.vNewVal
  This.imgIcon.Visible = .T.
  This.Icon = m.vNewVal
EndProc
```
  
Dies ermöglicht sowohl im Init wie auch zu späteren Zeitpunkten die einfache Veränderung dieser beiden Eigenschaften. Als nächstes wollen wir sicherstellen, dass unser Container verschiebbar wird.

Dazu implementieren wir die verschiedenen Mouse-Methoden des Shapes, welches unsere Titlebar simulieren wird:  

```foxpro
Procedure This.shpTitlebar.MouseDown
  LPARAMETERS nButton, nShift, nXCoord, nYCoord

  This.Parent.nXCoord = m.nXCoord - Objtoclient(This.Parent, OBJTOCLIENT_LEFT)
  This.Parent.nYCoord = m.nYCoord - Objtoclient(This.Parent, OBJTOCLIENT_TOP)
EndProc

Procedure This.shpTitlebar.MouseUp
  LPARAMETERS nButton, nShift, nXCoord, nYCoord

  This.Parent.nXCoord = 0
  This.Parent.nYCoord = 0
EndProc

Procedure This.shpTitlebar.MouseLeave
  LPARAMETERS nButton, nShift, nXCoord, nYCoord

  This.Parent.nXCoord = 0
  This.Parent.nYCoord = 0
EndProc

Procedure This.shpTitlebar.MouseMove
  LPARAMETERS nButton, nShift, nXCoord, nYCoord

  This.Parent.EventMouseMove(nButton, nShift, nXCoord, nYCoord)
EndProc
```
  
Selbstverständlich kann dies auch per BindEvent()-Funktion gelöst werden. Dabei jedoch an den fünften Parameter (nFlags = 1) denken. Die eigentliche Umsetzung der Bewegung findet dann wieder im Container statt:  

```foxpro
Procedure This.EventMouseMove
  *===================================================
  * Bewegung des Containers als Reaktion der Mausschubserei umsetzen
  *===================================================
  Lparameters tnButton, tnShift, tnXCoord, tnYCoord

  With This
    If .Movable
      If Bittest(m.tnButton, 0) .And. ;
          Not (.nXCoord == 0 .Or. .nYCoord == 0)
        This.Move( ;
          m.tnXCoord - .nXCoord, ;
          m.tnYCoord - .nYCoord, ;
          .Width, .Height ;
          )
      EndIf
    EndIf
  Endwith
EndProc
```
  
Sofern der Container als beweglich konfiguriert ist, führen wir die entsprechende Aktion auch durch. Warum die Verlagerung auf den Container? Ganz einfach, es könnten ja noch weitere Controls das Moven auslösen, oder die Titlebar setzt sich aus mehreren Controls (Images oder so... ) zusammen. Für unseren Basiscotainer gehen wir von einer rechteckigen Titlebar aus und arbeiten jetzt noch ein wenig mit der ZOrder des Shapes. Das Shape sollte auf alle Fälle über dem Caption-Label und dem Icon-Image liegen, jedoch unter dem Controlbox-Image, da die Buttons ja noch klickbar sein sollen. Apropos Controlbox... dieser wenden wir uns jetzt zu.

In seinem Artikel [Using the Alpha Channel in Visual Foxpro Images](https://weblogs.foxite.com/bernardbout/archive/2006/09/11/2436.aspx) verwendet Bernard Bout unsichtbare Commandbuttons (übrigens Style = 1 und nicht Visible = .F.) für die Realisierung des gewünschten Effekts. Das erscheint mir ehrlich gesagt überflüssig, da das Image-Control über eine Click-Methode verfügt und man mittels der Funktion ObjToClient() rausfinden kann, wo auf dem Image geklickt wurde. Das Konzept ähnelt dabei einer ImageMap aus HTML; Regionen können unterschiedliche Aktionen auslösen. In VFP-Code sieht das Ganze dann so aus:  

```foxpro
Procedure This.imgControlBox.Click
  *===================================================
  * Click-Ereignisse auf die Grafik 'simulieren'.
  * Wir verwenden eine Fallunterscheidung auf Basis der Position des
  * Mausklicks, und entscheiden damit, welches 'Ereignis' ausgelöst wird.
  * Zur Orientierung bestimmen wir die linke Ecke der VistaButtons.
  *===================================================

  With This
    Local lnLeftMin, lnLeftMax, lnLeftClose, lnPosition

    m.lnLeftMin = ObjToClient(This, OBJTOCLIENT_LEFT)
    m.lnLeftMax = m.lnLeftMin + 25 && Breite des MinButton
    m.lnLeftClose = m.lnLeftMax + 25 && Breite des MaxButton
    m.lnPosition = Mcol(0, 3)

    Do Case
      Case Between(m.lnPosition, m.lnLeftMin, m.lnLeftMax)
        This.Parent.EventClick("Minimize")
      Case Between(m.lnPosition, m.lnLeftMax, m.lnLeftClose)
        This.Parent.EventClick("Maximize")
      Otherwise
        This.Parent.EventClick("Close")
    EndCase
  EndWith
EndProc
```
  
Auch hier wieder die Ursache warum ich das so mache. Erstens, braucht man weniger Controls, die zwei bzw. drei CommandButtons sind schlichtweg überflüssig und man kann auf diese Weise auch wiederum irregulare Shapes verwenden. Selbst bei Nutzung von einzelnen Grafiken zur Darstellung der Buttons braucht es lediglich deren Click-Methode. Man denke hierbei an zusätzliche Form-Funktionalitäten wie etwa Menü, Stick und Shade (Linux-Kenner wissen Bescheid). Die Reaktion auf die Buttons wird wiederum im Container in der Methode EventClick implementiert:  

```foxpro
Procedure This.EventClick
  *===================================================
  * Reaktion auf die Click-Ereignisse der VistaButtons.
  *===================================================
  Lparameters tcSource

  With This
    Local lcSource
    m.lcSource = Lower(Alltrim(Evl(m.tcSource, "")))

    *-------------------------------------------------------------
    * Fallunterscheidung nach Click-Quelle
    * kann in Ableitungen überlagert und erweitert werden
    *-------------------------------------------------------------
    Do Case
      Case m.lcSource == "ok"
        .Hide()
      Case m.lcSource == "cancel"
        .Hide()
      Case m.lcSource == "minimize"
      Case m.lcSource == "maximize"
      Case m.lcSource == "close"
        .Hide()
      Case m.lcSource == "menu"
      Case m.lcSource == "stick"
      Case m.lcSource == "shade"
      Otherwise
    EndCase
  EndWith
```
  
Selbstverständlich können auch andere Controls mit Click oder MouseDown-Ereignis auf diese Verarbeitungsmethode des Containers umgeleitet werden. Damit kann man auch die Synchronisierung gleichen Verhalten erreichen. Im OK- bzw. Abbrechen-Button ruft man lediglich parametrisiert This.EventClick auf und das war's. Somit haben wir die Grundfunktionalität des Containers erzeugt. Werfen wir noch einen Blick in die Init-Methode, in der einiges zusammengesteckt wird:  

```foxpro
Procedure This.Init
  *===================================================
  * Initialisierung der Container-Form auslösen.
  *===================================================
  Lparameters toForm

  With This
    Local llOk
    m.llOk = .T.

    *------------------------------------------------------------------
    * Assertions und defensive Programmierung
    *------------------------------------------------------------------
    Assert Inlist(Vartype(m.toForm), T_OBJECT, T_OPTIONAL)
    If Vartype(m.toForm) == T_OBJECT
      This.oForm = m.toForm
    Endif

    m.llOk = DoDefault()

    If m.llOk
      .Caption = .Caption
      .Icon = .Icon
      .shpTitleBar.BorderStyle = 0
      If Not .lCustomTitlebar
        .shpTitleBar.Move(0,0,.Width,.shpTitleBar.Height)
      EndIf
      .shpTitleBar.Anchor = 11
      .imgControlBox.Left = .Width - .imgControlBox.Width - 7
      .imgControlBox.Anchor = 9
    EndIf

    If m.llOk
      Bindevent(This.lblCaption, "MouseMove", This, "EventMouseMove", 1)
      Bindevent(This.shpTitleBar, "Click", This, "Show")
      Bindevent(This.lblCaption, "Click", This, "Show")
    EndIf

    If m.llOk
      m.llOk = This.CreateBackground()
    EndIf
  EndWith

  Return m.llOk
EndProc
```
  
Durch das Anchoring von VFP 9.0 werden noch ein paar Positionierungen korrigiert. Somit braucht man sich zur Designzeit nicht um solche Kleinigkeiten kümmern. Über die Eigenschaft This.lCustomTitlebar haben wir die oben bereits genannte Flexibilität, dass wir die Titlebar auch an beliebiger Stelle auf dem Form platzieren können, etwa wenn man einen Offset nach rechts oder unten braucht. Gut, der bisherige Code war erst die Pflicht, kommen wir nun zur Kür und zum eigentlich Ziel des Artikels; der Erstellung von semitransparenten Formularen.



## GDIPlusX aus VFPX hilft für die optische Darstellung
Da die bisherigen Ansätze über die Win32 API nicht zum gewünschten Ergebnis geführt haben, verfolgen wir nun einen anderen Ansatz. Unsere Container-Klasse ist bereits vollständig transparent und durch die Verwendung von PNG-Grafiken (Portable Network Graphics) mit Alpha-Kanal als Hintergrund können wir nun den gewünschten Opacity-Effekt produzieren. Und das sogar in beliebigen Shapes und Farbennuancen. Hier zunächst einmal das zu erreichende Ziel als Grafik:

![Transparente Container-Form mit semitransparenter Grafik](https://jochen.kirstaetter.name/files/SemitransparentContainer.png)  
*Transparente Container-Form mit semitransparenter Grafik*  
Hier kommt ausschliesslich eine Hintergrundgrafik zum Einsatz, die zur Laufzeit mittels GDI+ ad hoc generiert und dargestellt wird. Der Rahmen wird durch Image.BorderStyle = 1 erzeugt. Wie man sehr gut sehen, besteht die Hintergrundgrafik aus zwei Bereichen - semitransparente Titlebar und nichttransparenter Hintergrund. Dies wird in einem Zug in der Methode CreateBackground des Containers erzeugt.  

```foxpro
Procedure This.CreateBackground
  *===================================================
  * Erstellen der 'Background'-Grafik im Fluge... mittels GDIPlusX aus VFPX
  * GDIPlusX wird im Hauptprogramm bereits aktiviert.
  * _SCREEN.AddProperty("System", ;
  * NEWOBJECT("xfcSystem", LOCFILE("system.vcx","vcx")))
  *===================================================
  With This
    Local llOk
    m.llOk = .T.

    If m.llOk
      m.llOk = DoDefault()
    EndIf

    If m.llOk
      With _Screen.System.Drawing
        * Create an empty bitmap
        Local loBitmap As xfcBitmap, ;
          lnLeft, lnTop, lnWidth, lnHeight, ;
          lnOffset, laPoints[1]
        Dimension laPoints[8]

        m.lnWidth = This.Width
        m.lnHeight = This.Height
        m.lnOffset = 2
        loBitmap = .Bitmap.New(m.lnWidth, m.lnHeight)

        * Initialize the graphics object
        Local loGfx As xfcGraphics
        loGfx = .Graphics.FromImage(loBitmap)

        * Make all image transparent
        loGfx.Clear(.Color.FromARGB(0,0,0,0))

        * Draw the 'background' polygon w/ rounded corners.
        m.lnLeft = 10
        m.lnTop = 35
        m.laPoints[1] = .Point.New(m.lnLeft + m.lnOffset, m.lnTop)
        m.laPoints[2] = .Point.New(m.lnWidth - m.lnLeft - m.lnOffset, m.lnTop)
        m.laPoints[3] = .Point.New(m.lnWidth - m.lnLeft, m.lnTop + m.lnOffset)
        m.laPoints[4] = .Point.New(m.lnWidth - m.lnLeft, m.lnHeight - m.lnOffset - m.lnLeft)
        m.laPoints[5] = .Point.New(m.lnWidth - m.lnLeft - m.lnOffset, m.lnHeight - m.lnLeft)
        m.laPoints[6] = .Point.New(m.lnLeft + m.lnOffset, m.lnHeight - m.lnLeft)
        m.laPoints[7] = .Point.New(m.lnLeft, m.lnHeight - m.lnOffset - m.lnLeft)
        m.laPoints[8] = .Point.New(m.lnLeft, m.lnTop + m.lnOffset)
        loGfx.FillPolygon(.SolidBrush.New(.Color.FromARGB( ;
          Int(255 * This.BackOpacity / 100),This.BackColor)), ;
          @laPoints)

        * Draw the 'titlebar' polygon w/ rounded corners.
        m.lnLeft = This.lblCaption.Left - 3
        m.lnTop = 1
        m.lnHeight = 25
        m.laPoints[1] = .Point.New(m.lnLeft, m.lnTop)
        m.laPoints[2] = .Point.New(m.lnWidth - m.lnOffset - m.lnTop, m.lnTop)
        m.laPoints[3] = .Point.New(m.lnWidth - m.lnTop, m.lnTop + m.lnOffset)
        m.laPoints[4] = .Point.New(m.lnWidth - m.lnTop, m.lnHeight - m.lnOffset)
        m.laPoints[5] = .Point.New(m.lnWidth - m.lnOffset - m.lnTop, m.lnHeight)
        m.laPoints[6] = .Point.New(m.lnLeft, m.lnHeight)
        m.laPoints[7] = .Point.New(m.lnLeft - m.lnOffset, m.lnHeight - m.lnOffset)
        m.laPoints[8] = .Point.New(m.lnLeft - m.lnOffset, m.lnTop + m.lnOffset)
        loGfx.FillPolygon(.SolidBrush.New(.Color.FromARGB( ;
          Int(255 * This.ForeOpacity / 100),This.ForeColor)), ;
          @laPoints)

        * Save as PNG to keep transparencies
        Local lcFilename, loPng
        m.lcFilename = Addbs(GetEnv("APPDATA")) + This.Name + ".png"
        loBitmap.Save(m.lcFilename, .Imaging.ImageFormat.Png)
      EndWith

      .AddObject("Background", "Image")
      .Background.Move( ;
        0, 0, ;
        .Width, .Height ;
        )
      .Background.BorderStyle = 1
      .Background.Zorder(1)
      .Background.Picture = m.lcFilename
      .Background.Anchor = 15
      .Background.Visible = .T.
    EndIf
  EndWith
EndProc
```
  
Die Kommentare im Quellcode erklären die Vorgehensweise ausreichend. Dennoch möchte ich hier kleinere Anmerkungen zum Code geben. Die Farbgebung der beiden grafischen Elemente - Titlebar und Background - erfolgt durch die Verwendung der Container-Eigenschaften ForeColor (für Titlebar) und BackColor (für Background). Da der Container eh vollständig transparent ist, kann man die Properties bedenkenlos zweckentfremden. Zumindest spart man sich hierdurch eigene Namen und kann den Color Picker im PropertySheet verwenden. Zusätzlich habe ich entsprechende Eigenschaften für die Opacity - ForeOpacity und BackOpacity - in Prozent angelegt. Somit können wir durch Setzen von vier Eigenschaften am Container den gewünschten Effekt unserer Semitransparenz in beliebigen Farben regulieren.

![Beliebige Variationen für Farbgebung und Opacity sind über Eigenschaften möglich](https://jochen.kirstaetter.name/files/BackOpacity.png)  
*Beliebige Variationen für Farbgebung und Opacity sind über Eigenschaften möglich*

Mit einer wenig Umstellung im Code könnte man auch die nachträgliche Veränderung der Hintergrundgrafik durch erneute Generierung realisieren. Ob das sinnvoll ist, sei dem Entwickler bzw. dem Anwender selbst überlassen.

## Verwaltung der 'Forms' an zentraler Stelle
Da es sich bei unseren 'Formularen' ja um Container handelt, benötigen wir auch einen Mechanismus zum Laden der Instanzen. Das größte Problem, dass es in Verbindung mit VFP-Containern zu lösen gilt, ist das Fehlen der freien Instanzierung wie es bei Forms und Formklassen möglich ist. Container können in VFP nur aggregiert werden, damit sie sichtbar werden. Bei einer zweiten Betrachtung scheint die Lösung dennoch recht einfach zu sein, da wird bereits ein globales Form immer zur Verfügung haben: _Screen

Schaut man sich übrigens die Vorgehensweise bei VFP-Forms an, erkennt man auch sehr schnell, dass diese ebenfalls über den _Screen verwaltet werden: _Screen-Forms ist ein Array mit sämtlichen Referenzen der Formobjekte. Und durch Nachbildung dieser Funktionalität erreichen wir das gleiche Resultat. Wir aggregieren unsere Container ebenfalls an das _Screen-Form(set) und legen die Verwaltung in einer Collection (anstelle eines Arrays) ab. Dadurch werden die Containerinstanzen an eine globale Stelle aggregiert und stehen in der gesamten Anwendung jederzeit zur Verfügung. Durch Vergabe von dynamischen Namen können wir ebenfalls stressfrei multiple Instanzen der gleichen Containerklasse erzielen und nutzen.

Dazu erstellen wir uns einen generischen Container-Loader, der diese Aufgabe übernimmt. Die Loaderklasse erstellen wir übrigens in einem PRG namens *container.prg*. 🤪 Auf diese Weise können wir unsere Containerobjekte über zwei gleichwertige Wege erzeugen:  
``  
In Analogie zum Aufruf von VFP-Formularen mittels *DO Form &lt;SCX&gt; WITH &lt;Parameter&gt;* bietet unser Programm eine vergleichbare Funktionalität gemäß folgender Syntax:  
`DO Container With <Klasse>, <Bibliothek>, <Parameter>`  
Auf Grund der Aggregation des ContainerLoaders an _Screen können wir ebenfalls folgenden Aufruf nutzen:  
`_Screen.Containers.LoadContainer(<Klasse>, <Bibliothek>, <Parameter>)`  
Durch die Verwendung einer Collection für unsere Container anstelle eines Arrays wie bei _Screen.Forms haben wir die Möglichkeit sowohl über einen Index als auch über einen Schlüssel (Namen) auf die Objektreferenz zuzugreifen.  
Bis denne, JoKi