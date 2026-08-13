---
uid: vfp-datenbank-in--net
title: VFP Datenbank in .NET
slug: vfp-datenbank-in--net
date: 2005-04-04
status: published
type: post
description: VFP Datenbank in .NET Auf zu neuen Ufern und die ersten Schritte sehen bereits vielversprechend aus. Nachdem ich am letzten Sonntag abends im Hotel zur Entspannung mal ein wenig angefangen habe mit dem Visual Studio 2003 und C# zu experimentieren...Ja, wollte mal sehen, ob ich es schaffe einen simplen Browse
tags:
- Development
keywords: Development
metaTitle: VFP Datenbank in .NET
metaDescription: VFP Datenbank in .NET Auf zu neuen Ufern und die ersten Schritte sehen bereits vielversprechend aus. Nachdem ich am letzten Sonntag abends im Hotel zur Entspannung mal ein wenig angefangen habe mit dem Visual Studio 2003 und C# zu experimentieren...Ja, wollte mal sehen, ob ich es schaffe einen simplen Browse
image: ''
ogTitle: VFP Datenbank in .NET
ogDescription: Auf zu neuen Ufern und die ersten Schritte sehen bereits vielversprechend aus. Nachdem ich am letzten Sonntag abends im Hotel zur Entspannung mal ein wenig angefangen habe mit dem Visual Studio 2003...
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
canonicalUrl: https://jochen.kirstaetter.name/vfp-datenbank-in--net/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: https://jochen.kirstaetter.name/content/images/2018/10/JoKi_StAubin_100px.jpg
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2005-04-04T22:00:00Z
updatedAt: 2018-04-02T08:38:31Z
excerpt: Auf zu neuen Ufern und die ersten Schritte sehen bereits vielversprechend aus. Nachdem ich am letzten Sonntag abends im Hotel zur Entspannung mal ein wenig angefangen habe mit dem Visual Studio 2003...
twitterTitle: VFP Datenbank in .NET
twitterDescription: Auf zu neuen Ufern und die ersten Schritte sehen bereits vielversprechend aus. Nachdem ich am letzten Sonntag abends im Hotel zur Entspannung mal ein wenig angefangen habe mit dem Visual Studio 2003...
twitterImage: 
facebookTitle: VFP Datenbank in .NET
facebookDescription: Auf zu neuen Ufern und die ersten Schritte sehen bereits vielversprechend aus. Nachdem ich am letzten Sonntag abends im Hotel zur Entspannung mal ein wenig angefangen habe mit dem Visual Studio 2003...
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---

Auf zu neuen Ufern und die ersten Schritte sehen bereits vielversprechend aus. Nachdem ich am letzten Sonntag abends im Hotel zur Entspannung mal ein wenig angefangen habe mit dem Visual Studio 2003 und C# zu experimentieren...  
Ja, wollte mal sehen, ob ich es schaffe einen simplen Browse zu erstellen (gekürzte Fassung):  
  
Quellcode:  
  
using System;  
using System.Drawing;  
using System.Collections;  
using System.ComponentModel;  
using System.Windows.Forms;  
using System.Data;  
using System.Data.Common;  
using System.Data.OleDb;  
  
namespace Vfp4Net  
{  
public class VfpDataAccess : System.Windows.Forms.Form  
{  
private DataSet ds;  
  
public VfpDataAccess()  
{  
InitializeComponent();  
}  
  
[STAThread]  
static void Main()  
{  
Application.Run(new VfpDataAccess());  
}  
  
private void VfpDataAccess\_Load(object sender, System.EventArgs e)  
{  
string ConnectionString = @"Provider=vfpoledb.1;Data Source=C:FoxProVFP9SamplesNorthwind  
orthwind.dbc";  
OleDbConnection Connection = new OleDbConnection(ConnectionString);  
Connection.Open();  
  
string SqlQuery = "SELECT TOP 10 LastName, FirstName, Title FROM Employees ORDER BY employeeid";  
OleDbCommand Command = new OleDbCommand(SqlQuery, Connection);  
  
OleDbDataAdapter DataAdapter = new OleDbDataAdapter(SqlQuery, Connection);  
DataSet ds = new DataSet();  
DataAdapter.Fill(ds);  
this.ds = ds;  
  
Connection.Close();  
}  
  
private void cmdLoad\_Click(object sender, System.EventArgs e)  
{  
this.grdEmployees.DataBindings.Clear();  
this.grdEmployees.SetDataBinding(this.ds, "");  
}  
}  
}  
  
  
Wie man unschwer erkennen kann, war mir ein simples 'Hello World' als Einstieg zu - reden wir nicht drüber. Und das Ganze ohne den Guide To C#...  
  
Ich hoffe, dass es einigermaßen akzeptabler Code ist... Kommentare?  
  
Well, ist ja alles supertoll und auch easy zu verstehen, aber... Und jetzt fängt der Spass doch erst an. Sämtliche Quellen im Internet und in sonstiger Literatur haben leider einen extremen Schönheitsfehler bei der Beschreibung von ADO.NET: Die Datenquelle wird immer(!) - okay, zu 99,9% - als vorhanden vorausgesetzt.  
  
Schon probiert, eine neue Datenbank im SQL Server, Access oder Visual FoxPro per ADO.NET anzulegen? - Vergiss es!  
  
Nunja, es muss ja was geben. Nach einigen Recherchen, ein paar grauen Haaren mehr und Cola Light dann der erste Lichtfunke: ADOX - ActiveX Data Objects Extension  
Und hier haben wir auch den Schlüssel zum Erfolg (VFP Code):  
  
Quellcode:  
  
Adox = CreateObject("Adox.Catalog")  
oDbc = Adox.Create("Provider=vfpoledb.1;Data Source=C:WUTemp  
orthwind.dbc")  
? oDbc.ConnectionString  
  
  
Man muss nun dran denken, dass man einen COM Verweis im Projekt hinzufügt:  
  
\* Projektmappen-Explorer öffnen / anzeigen  
\* Rechtsklick auf Verweise  
\* Verweis hinzufügen...  
\* Auf den Tab COM wechseln und  
\* Microsoft ADO Ext. 2.8 for DDL and Security selektieren  
\* [ Auswählen ]  
\* [ OK ]  
  
Somit steht euch eine ADOX Proxy-Klasse in eurem Projekt zur Verfügung, welches für die Erstellung und Einstellung der Sicherheitsregeln der Datenbank genutzt werden kann. Derzeit stehen die ADOX Objekte und Methoden nicht als Managed Code Klassen zur Verfügung.  
Klar, wieso auch? - Datenbanken wachsen an Bäumen...  
  
Okay, hier noch das Resultat wie man bequem im .NET Framework mittels COM Interop auf die ADOX-Objekte zugreift und eine Visual FoxPro Datenbank erstellt:  
  
Quellcode:  
  
using ADOX;  
using System;  
  
string ConnectionString = @"Provider=vfpoledb.1;Data Source=C:FoxProVFP9SamplesNorthwind  
orthwind.dbc";  
  
CatalogClass adox = new CatalogClass();  
object oDbc = adox.Create(ConnectionString);  
  
  
Echt easy, wenn es weiß, oder?  
Nur bin ich mir noch ganz klar, wie ich die Klassendeklaration ADODB.Connection dem erzeugten object oDbc beibringe. Aber das wird auch noch klappen.  
  
Soviel zu meiner ersten Lektion in den Un-Tiefen von C# und dem .NET Framework.  
  
  
Bis denne, JoKi
