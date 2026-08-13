---
uid: in-80-zeilen-um-die-vfp-tabelle
title: In 80 Zeilen um die VFP-Tabelle
slug: in-80-zeilen-um-die-vfp-tabelle
date: 2005-04-29
status: published
type: post
description: In 80 Zeilen um die VFP-Tabelle Ups, I did it again...Oder so ähnlich, aber da ich gestern / heute ein wenig durch meine Kollegen zu Zwangsarbeit genötigt wurde, dachte ich mir die Zeit des Wartens könnte man anderweitig nutzen.Nun, in Vorbereitung für den kommenden Webcast zu Visual FoxPro und Visual
tags:
- Development
keywords: Development
metaTitle: In 80 Zeilen um die VFP-Tabelle
metaDescription: In 80 Zeilen um die VFP-Tabelle Ups, I did it again...Oder so ähnlich, aber da ich gestern / heute ein wenig durch meine Kollegen zu Zwangsarbeit genötigt wurde, dachte ich mir die Zeit des Wartens könnte man anderweitig nutzen.Nun, in Vorbereitung für den kommenden Webcast zu Visual FoxPro und Visual
image: content/images/2023/09/in80linesofcode.png
ogTitle: In 80 Zeilen um die VFP-Tabelle
ogDescription: Ups, I did it again...Oder so ähnlich, aber da ich gestern / heute ein wenig durch meine Kollegen zu Zwangsarbeit genötigt wurde, dachte ich mir die Zeit des Wartens könnte man anderweitig nutzen.Nun...
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
authorImage: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorSlug: joki
canonicalUrl: https://jochen.kirstaetter.name/in-80-zeilen-um-die-vfp-tabelle/
imageUrl: https://jochen.kirstaetter.name/content/images/2023/09/in80linesofcode.png
twitterImageUrl: https://jochen.kirstaetter.name/content/images/2023/09/in80linesofcode.png
authorImageUrl: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: content/images/2023/09/in80linesofcode.png
featured: false
publishedAt: 2005-04-29T00:00:00Z
updatedAt: 2023-09-18T18:28:57Z
excerpt: Ups, I did it again...Oder so ähnlich, aber da ich gestern / heute ein wenig durch meine Kollegen zu Zwangsarbeit genötigt wurde, dachte ich mir die Zeit des Wartens könnte man anderweitig nutzen.Nun...
twitterTitle: In 80 Zeilen um die VFP-Tabelle
twitterDescription: Ups, I did it again...Oder so ähnlich, aber da ich gestern / heute ein wenig durch meine Kollegen zu Zwangsarbeit genötigt wurde, dachte ich mir die Zeit des Wartens könnte man anderweitig nutzen.Nun...
twitterImage: 
facebookTitle: In 80 Zeilen um die VFP-Tabelle
facebookDescription: Ups, I did it again...Oder so ähnlich, aber da ich gestern / heute ein wenig durch meine Kollegen zu Zwangsarbeit genötigt wurde, dachte ich mir die Zeit des Wartens könnte man anderweitig nutzen.Nun...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---

Ups, I did it again...  
  
Oder so ähnlich, aber da ich gestern / heute ein wenig durch meine Kollegen zu Zwangsarbeit genötigt wurde, dachte ich mir die Zeit des Wartens könnte man anderweitig nutzen.  
  
Nun, in Vorbereitung für den kommenden Webcast zu Visual FoxPro und Visual Studio 2005 brauche ich ein wenig Übung und ein, zwei Beispiele wie man von C# auf die Datenbankfähigkeiten von Visual FoxPro zugreift. Well, gedacht, gemacht...  
  
Und so habe ich mir dann einen wirklich simplen VFP-Befehl als Vorlage genommen:  
  
[code]Browse[/code]  
  
Mit dem Browse-Befehl kann man den Inhalt einer Tabelle in einem Grid anzeigen lassen und manipulieren. Sofern keine Tabelle im aktuellen Arbeitsbereich geöffnet ist, bietet Visual FoxPro den Datei-Auswahldialog für DBFs an.  
  
Für einen VFP-Entwickler gehört dieser Befehl zum Standardrüstzeug. Egal, ob auf lokal oder remote liegende VFP-Tabellen oder ResultSets aus ODBC-Connections (Views und Cursor) zugegriffen wird.  
  
Und damit wären wir auch bei einer sinnvollen Aufgabe für meine weiteren Schritte im Reich des .NET Frameworks unter der Herrscher des C#. Wir schreiben eine Windows-Anwendung zum Öffnen, Anzeigen und Manipulieren von Visual FoxPro Tabellen. Klingt spassig, oder?  
  
Spass hat es auf Fälle gemacht.  
Also, Visual Studio angeworfen, neues C# Windows-Anwendung Projekt namens VfpBrowse erstellt. Die automatisch erstellte Form-Klasse polieren wir ein wenig auf und verpassen ihr noch ein paar Felder, die wir im weiteren Verlauf brauchen werden:  
  
[code]public class frmVfpBrowse : System.Windows.Forms.Form  
{  
private string path;  
private string file;  
private OleDbDataAdapter da;  
private DataSet ds;  
//...  
}[/code]  
  
Jetzt kümmern wir uns ein wenig um die optische Ausstattung und werfen ein paar Controls auf die leere Form:  
\* Label  
\* Textbox  
\* Button für den Auswahldialog  
\* FileDialog-Komponente  
\* Button für Browse  
\* Button für Update  
\* und zu guter Letzt ein DataGrid  
  
Das Ganze hübsch angeordnet und per Anchor-Eigenschaft festgetackert.  
  
  
So, jetzt kümmern wir uns um die Ereignisse, die Auftreten können. Da hätten wir zuerst den Click für die Dateiauswahl; diesem geben wir die FileDialog-Komponente für die Selektion der anzuzeigenden VFP-Tabelle.  
  
[code]  
private void cmdSelect\_Click(object sender, System.EventArgs e)  
{  
try  
{  
openFileDialog1.Filter = "Visual FoxPro tables (*.dbf)|*.dbf";  
openFileDialog1.FilterIndex = 2;  
openFileDialog1.RestoreDirectory = true;  
}  
catch (Exception ex)  
{  
Debug.WriteLine(ex.ToString());  
}  
  
if(openFileDialog1.ShowDialog() == DialogResult.OK)  
{  
txtTable.Text = openFileDialog1.FileName;  
}  
}[/code]  
  
Als nächstes das Click-Ereignis des Browse-Button; hier nutzen wir die Fähigkeiten der OleDb-Klassen des .NET Framework. Mittels OleDbConnection öffnen wir die VFP-Tabelle, selektieren alles komplett in einen DataAdapter und füllen ein ungebundenes DataSet, welches dem DataGrid als Datenquelle zum Futtern zugeworfen wird. Fein, fein... damit haben wir die Anzeige der Tabelle.  
  
[code]  
private void cmdBrowse\_Click(object sender, System.EventArgs e)  
{  
try  
{  
this.path = Path.GetDirectoryName(txtTable.Text);  
this.file = Path.GetFileNameWithoutExtension(txtTable.Text);  
}  
catch (Exception ex)  
{  
Debug.WriteLine(ex.ToString());  
}  
  
string ConnString = "Provider=vfpoledb.1;Data Source=" + this.path +  
";Persist Security Info=false;";  
OleDbConnection Conn = new OleDbConnection(ConnString);  
try  
{  
Conn.Open();  
}  
catch (Exception ex)  
{  
Debug.WriteLine(ex.ToString());  
}  
  
try  
{  
this.da = new OleDbDataAdapter("SELECT \* FROM " + this.file, Conn);  
OleDbCommandBuilder cb = new OleDbCommandBuilder(this.da);  
da.InsertCommand = cb.GetInsertCommand();  
da.UpdateCommand = cb.GetUpdateCommand();  
da.DeleteCommand = cb.GetDeleteCommand();  
}  
catch (Exception ex)  
{  
Debug.WriteLine(ex.ToString());  
}  
  
this.ds = new DataSet();  
this.ds.Clear();  
try  
{  
this.da.Fill(this.ds);  
grdTable.DataSource = this.ds.Tables[0];  
}  
catch (Exception ex)  
{  
Debug.WriteLine(ex.ToString());  
}  
}[/code]  
  
Als nächstes spendieren wir dem Update-Button die Fähigkeit per DataSet der Änderungen und dem bekannten DataAdapter die geänderten Informationen zurück in die VFP-Tabelle zu schreiben. Achja, dem DataAdapter haben wir natürlich im Vorfeld bereits von einem OleDbCommandBuilder erklären lassen, wie sowas zu funktionieren hat.  
  
[code]  
private void cmdUpdate\_Click(object sender, System.EventArgs e)  
{  
if(this.ds.HasChanges())  
{  
DataSet dc = this.ds.GetChanges();  
try  
{  
this.da.Update(dc);  
this.ds.AcceptChanges();  
}  
catch (Exception ex)  
{  
Debug.WriteLine(ex.ToString());  
}  
}  
}[/code]  
  
Cool, oder?  
Nunja, das ist erst die halbe Miete, denn die richtige Arbeitserleichterung unter Visual FoxPro besteht darin, dass die Feldinhalte direkt geändert und bei einem Zeilenwechsel ad hoc zurückgeschrieben werden.  
Hehe, hier für habe ich mir einen Trick einfallen lassen: Das entsprechende Ereignis des DataGrid wird an die gleiche Methode wie der Update-Button gebunden...  
  
[code]  
this.grdTable.CurrentCellChanged += new System.EventHandler(this.cmdUpdate\_Click);  
[/code]  
  
*flupp* Fertig!  
  
So, ihr Lieben und jetzt das Ganze noch mal zusammenhängend für die Programmsammlung zuhause. Achja, das komplette Projekt ist als ZIP-Archiv ebenfalls verfügbar. Viel Spass!  
  
[code]  
using System;  
using System.Drawing;  
using System.Diagnostics;  
using System.Collections;  
using System.ComponentModel;  
using System.Windows.Forms;  
using System.IO;  
using System.Data;  
using System.Data.OleDb;  
  
  
namespace VfpBrowse  
{  
///  
/// Zusammenfassung für frmVfpBrowse.  
///  
public class frmVfpBrowse : System.Windows.Forms.Form  
{  
private string path;  
private string file;  
private OleDbDataAdapter da;  
private DataSet ds;  
  
private System.Windows.Forms.OpenFileDialog openFileDialog1;  
private System.Windows.Forms.Button cmdSelect;  
private System.Windows.Forms.Button cmdBrowse;  
private System.Windows.Forms.Button cmdUpdate;  
private System.Windows.Forms.DataGrid grdTable;  
private System.Windows.Forms.Label lblTable;  
private System.Windows.Forms.TextBox txtTable;  
///  
/// Erforderliche Designervariable.  
///  
private System.ComponentModel.Container components = null;  
  
public frmVfpBrowse()  
{  
//  
// Erforderlich für die Windows Form-Designerunterstützung  
//  
InitializeComponent();  
this.grdTable.CurrentCellChanged += new System.EventHandler(this.cmdUpdate\_Click);  
  
//  
// TODO: Fügen Sie den Konstruktorcode nach dem Aufruf von InitializeComponent hinzu  
//  
}  
  
///  
/// Die verwendeten Ressourcen bereinigen.  
///  
protected override void Dispose( bool disposing )  
{  
if( disposing )  
{  
if (components != null)  
{  
components.Dispose();  
}  
}  
base.Dispose( disposing );  
}  
  
#region Vom Windows Form-Designer generierter Code  
///  
/// Erforderliche Methode für die Designerunterstützung.  
/// Der Inhalt der Methode darf nicht mit dem Code-Editor geändert werden.  
///  
private void InitializeComponent()  
{  
this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();  
this.txtTable = new System.Windows.Forms.TextBox();  
this.cmdSelect = new System.Windows.Forms.Button();  
this.cmdBrowse = new System.Windows.Forms.Button();  
this.cmdUpdate = new System.Windows.Forms.Button();  
this.grdTable = new System.Windows.Forms.DataGrid();  
this.lblTable = new System.Windows.Forms.Label();  
((System.ComponentModel.ISupportInitialize)(this.grdTable)).BeginInit();  
this.SuspendLayout();  
//  
// txtTable  
//  
this.txtTable.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)  
| System.Windows.Forms.AnchorStyles.Right)));  
this.txtTable.Location = new System.Drawing.Point(167, 5);  
this.txtTable.Name = "txtTable";  
this.txtTable.Size = new System.Drawing.Size(312, 20);  
this.txtTable.TabIndex = 0;  
this.txtTable.Text = "";  
//  
// cmdSelect  
//  
this.cmdSelect.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));  
this.cmdSelect.Location = new System.Drawing.Point(486, 4);  
this.cmdSelect.Name = "cmdSelect";  
this.cmdSelect.Size = new System.Drawing.Size(24, 23);  
this.cmdSelect.TabIndex = 1;  
this.cmdSelect.Text = "...";  
this.cmdSelect.Click += new System.EventHandler(this.cmdSelect\_Click);  
//  
// cmdBrowse  
//  
this.cmdBrowse.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));  
this.cmdBrowse.Location = new System.Drawing.Point(517, 4);  
this.cmdBrowse.Name = "cmdBrowse";  
this.cmdBrowse.TabIndex = 2;  
this.cmdBrowse.Text = "Browse";  
this.cmdBrowse.Click += new System.EventHandler(this.cmdBrowse\_Click);  
//  
// cmdUpdate  
//  
this.cmdUpdate.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));  
this.cmdUpdate.Location = new System.Drawing.Point(8, 384);  
this.cmdUpdate.Name = "cmdUpdate";  
this.cmdUpdate.TabIndex = 3;  
this.cmdUpdate.Text = "Update";  
this.cmdUpdate.Click += new System.EventHandler(this.cmdUpdate\_Click);  
//  
// grdTable  
//  
this.grdTable.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)  
| System.Windows.Forms.AnchorStyles.Left)  
| System.Windows.Forms.AnchorStyles.Right)));  
this.grdTable.DataMember = "";  
this.grdTable.HeaderForeColor = System.Drawing.SystemColors.ControlText;  
this.grdTable.Location = new System.Drawing.Point(8, 32);  
this.grdTable.Name = "grdTable";  
this.grdTable.Size = new System.Drawing.Size(584, 344);  
this.grdTable.TabIndex = 4;  
//  
// lblTable  
//  
this.lblTable.AutoSize = true;  
this.lblTable.Location = new System.Drawing.Point(8, 8);  
this.lblTable.Name = "lblTable";  
this.lblTable.Size = new System.Drawing.Size(156, 16);  
this.lblTable.TabIndex = 5;  
this.lblTable.Text = "Browse a Visual FoxPro table:";  
//  
// frmVfpBrowse  
//  
this.AutoScaleBaseSize = new System.Drawing.Size(5, 13);  
this.ClientSize = new System.Drawing.Size(600, 414);  
this.Controls.Add(this.lblTable);  
this.Controls.Add(this.grdTable);  
this.Controls.Add(this.cmdUpdate);  
this.Controls.Add(this.cmdBrowse);  
this.Controls.Add(this.cmdSelect);  
this.Controls.Add(this.txtTable);  
this.Name = "frmVfpBrowse";  
this.Text = "Browse Visual FoxPro DBFs";  
this.Load += new System.EventHandler(this.frmVfpBrowse\_Load);  
((System.ComponentModel.ISupportInitialize)(this.grdTable)).EndInit();  
this.ResumeLayout(false);  
  
}  
#endregion  
  
///  
/// Der Haupteinstiegspunkt für die Anwendung.  
///  
[STAThread]  
static void Main()  
{  
Application.Run(new frmVfpBrowse());  
}  
  
private void frmVfpBrowse\_Load(object sender, System.EventArgs e)  
{  
  
}  
  
private void cmdSelect\_Click(object sender, System.EventArgs e)  
{  
try  
{  
openFileDialog1.Filter = "Visual FoxPro tables (*.dbf)|*.dbf";  
openFileDialog1.FilterIndex = 2;  
openFileDialog1.RestoreDirectory = true;  
}  
catch (Exception ex)  
{  
Debug.WriteLine(ex.ToString());  
}  
  
if(openFileDialog1.ShowDialog() == DialogResult.OK)  
{  
txtTable.Text = openFileDialog1.FileName;  
}  
}  
  
private void cmdBrowse\_Click(object sender, System.EventArgs e)  
{  
try  
{  
this.path = Path.GetDirectoryName(txtTable.Text);  
this.file = Path.GetFileNameWithoutExtension(txtTable.Text);  
}  
catch (Exception ex)  
{  
Debug.WriteLine(ex.ToString());  
}  
  
string ConnString = "Provider=vfpoledb.1;Data Source=" + this.path + ";Persist Security Info=false;";  
OleDbConnection Conn = new OleDbConnection(ConnString);  
try  
{  
Conn.Open();  
}  
catch (Exception ex)  
{  
Debug.WriteLine(ex.ToString());  
}  
  
try  
{  
this.da = new OleDbDataAdapter("SELECT \* FROM " + this.file, Conn);  
OleDbCommandBuilder cb = new OleDbCommandBuilder(this.da);  
da.InsertCommand = cb.GetInsertCommand();  
da.UpdateCommand = cb.GetUpdateCommand();  
da.DeleteCommand = cb.GetDeleteCommand();  
}  
catch (Exception ex)  
{  
Debug.WriteLine(ex.ToString());  
}  
  
this.ds = new DataSet();  
this.ds.Clear();  
try  
{  
this.da.Fill(this.ds);  
grdTable.DataSource = this.ds.Tables[0];  
}  
catch (Exception ex)  
{  
Debug.WriteLine(ex.ToString());  
}  
}  
  
private void cmdUpdate\_Click(object sender, System.EventArgs e)  
{  
if(this.ds.HasChanges())  
{  
DataSet dc = this.ds.GetChanges();  
try  
{  
this.da.Update(dc);  
this.ds.AcceptChanges();  
}  
catch (Exception ex)  
{  
Debug.WriteLine(ex.ToString());  
}  
}  
}  
  
}  
}[/code]
