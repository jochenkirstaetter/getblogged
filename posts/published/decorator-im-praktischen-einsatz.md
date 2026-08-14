---
uid: decorator-im-praktischen-einsatz
title: Decorator im praktischen Einsatz
slug: decorator-im-praktischen-einsatz
date: 2006-11-02
status: published
type: post
description: "Decorator im praktischen Einsatz Ja, ich wei&#223;... Decorator hier, Decorator dort. :icon_biggrin: - Langsam reicht es doch mal wieder. Nun, ja ihr habt ja recht. Nach den bisherigen Blogeintr&#228;genDesign Pattern: Decorator<a href='/Anmerkungen-zum-Decorator-Design-Pattern'>Anmerkungen zum Decorator Design Pattern</a>m&#246;chte ich die Serie &#252;ber dieses Entwurfsmuster mit diesem Beitrag vorerst abschliessen.Warum der Nachschlag? Wieder einmal"
tags:
- Community
keywords: Community
metaTitle: Decorator im praktischen Einsatz
metaDescription: "Decorator im praktischen Einsatz Ja, ich wei&#223;... Decorator hier, Decorator dort. :icon_biggrin: - Langsam reicht es doch mal wieder. Nun, ja ihr habt ja recht. Nach den bisherigen Blogeintr&#228;genDesign Pattern: Decorator<a href='/Anmerkungen-zum-Decorator-Design-Pattern'>Anmerkungen zum Decorator Design Pattern</a>m&#246;chte ich die Serie &#252;ber dieses Entwurfsmuster mit diesem Beitrag vorerst abschliessen.Warum der Nachschlag? Wieder einmal"
image: ''
ogTitle: Decorator im praktischen Einsatz
ogDescription: "Ja, ich weiß... Decorator hier, Decorator dort. \U0001F601 - Langsam reicht es doch mal wieder. Nun, ja ihr habt ja recht. Nach den bisherigen Blogeinträgen"
layout: post
bodyClass: post-template tag-community
postClass: post tag-community
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
canonicalUrl: https://jochen.kirstaetter.name/decorator-im-praktischen-einsatz/
imageUrl: ''
twitterImageUrl: ''
authorImageUrl: content/images/2018/10/JoKi_StAubin_100px.webp
authorPageUrl: https://jochen.kirstaetter.name/author/joki/
tagName: ''
tagDescription: ''
featureImage: ''
featured: false
publishedAt: 2006-11-02T13:04:34Z
updatedAt: 2018-04-02T08:39:11Z
excerpt: "Ja, ich weiß... Decorator hier, Decorator dort. \U0001F601 - Langsam reicht es doch mal wieder. Nun, ja ihr habt ja recht. Nach den bisherigen Blogeinträgen"
twitterTitle: Decorator im praktischen Einsatz
twitterDescription: "Ja, ich weiß... Decorator hier, Decorator dort. \U0001F601 - Langsam reicht es doch mal wieder. Nun, ja ihr habt ja recht. Nach den bisherigen Blogeinträgen"
twitterImage: 
facebookTitle: Decorator im praktischen Einsatz
facebookDescription: "Ja, ich weiß... Decorator hier, Decorator dort. \U0001F601 - Langsam reicht es doch mal wieder. Nun, ja ihr habt ja recht. Nach den bisherigen Blogeinträgen"
facebookImage: ''
codeinjectionHead: 
codeinjectionFoot: 
---
Ja, ich weiß... Decorator hier, Decorator dort. 😁 - Langsam reicht es doch mal wieder. Nun, ja ihr habt ja recht. Nach den bisherigen Blogeinträgen

- [Design Pattern: Decorator](xref:design-pattern-decorator)
- [Anmerkungen zum Decorator Design Pattern](xref:anmerkungen-zum-decorator)

möchte ich die Serie über dieses Entwurfsmuster mit diesem Beitrag vorerst abschliessen.  
Warum der Nachschlag? Wieder einmal die Unterhaltung mit Olaf Doschke im Forum der dFPUG. Es ist sehr anregend mit anderen Entwicklern über die Thematik und Implementierung zu sprechen. Olaf hatte noch sehr gute Anregungen für die Realisierung und Verbesserung des bisherigen Quellcodes. Zu meiner Entschuldigung möchte ich aber auch sagen, dass der Einstiegsartikel nicht mit den Details des Fehlerhandlings 'langweilen' sollte, sondern primär die Anwendbarkeit des Entwurfsmusters verdeutlichen.

> Ich hab mir auch überlegt, daß das ganze Problematisch werden kann, wenn oDecorated ein COM-Objekt ist. Dann läßt sich nämlich PEMSTATUS() nicht unbedenklich anwenden, da müßte dann wohl Ersatzweise eher AMEMBERS und ASCAN ran, wenn man es denn so umstellen wollte.

Ein sehr guter Einwand übrigens. Den habe ich zwar an anderen Stelle schon berücksichtigt, aber noch nicht in Verbindung mit dem Decorator, da ich noch nicht in Versuchung kam, einen COM-Server zu dekorieren. Aber in der Tat, ein sehr gutes Argument.

> Ich fände es übrigens völlig in Ordnung, wenn der Zugriff auf Protected-Eigenschaften/Methoden in die Hose geht, das wäre ja auch genau das Verhalten, was das Originalobjekt an den Tag legen würde.

Well, das ist eine Sache der Herangehensweise. Ich würde in so einem Falle lediglich einen ASSERT absetze, so dass eine Info für den Entwickler zur Verfügung steht, aber die Anwendung keinen Ausstieg provoziert. Hm, effektiv sollte man das eh komplett in einen Try..EndTry packen, dann ist man sicherlich etliche Sorgen los. Als Alternative verwende ich ihm nachfolgenden Code einen (Nach-)Lade-Mechanismus, falls die Eigenschaft nicht existieren sollte. Ich weiß, dass das nicht die feine englische Art ist, aber auf diese Weise provoziere ich erstens keinen Absturz und zweitens bietet mir dieser Ansatz einen einfachen Cache. Vorgesetzt natürlich, dass die Methode GetToken() in der jeweiligen Ableitung auch entsprechend implementiert ist.

Wenn wir also die bisherigen Erkenntnisse zusammenpacken, dann sollte unser Quellcode in etwa so aussehen:

```
*============================================================
* Interface definition for decorator classes
*============================================================
Define Class IDecorator As Relation
 oObject = .Null.

 Function Init(toObject As Object) As Boolean
  Return .T.
 EndFunc
 
 Function Destroy() As Boolean
  Return .T.
 EndFunc
 
 Function SetClient(toObject As Object) As VOID
 EndFunc

 Protected Function This_Access(tcPem As String) As Object
  Return This
 EndFunc
 
 Function GetToken(toObject As Object, tcToken As String) As Variant
  Return .Null.
 EndFunc
EndDefine

*============================================================
* 'Abstract' base class for Decorator Design Pattern
*============================================================
Define Class AbstractDecorator As IDecorator
 
 Function Init(toObject As Object) As Boolean
  Return This.SetClient(m.toObject)
 EndFunc
 
 Function Destroy() As Boolean
  This.oObject = .Null.
 EndFunc
 
 Function SetClient(toObject As Object) As VOID
  If Pcount() == 1 .And. ;
     Vartype(m.toObject) == "O"
  
   This.oObject = m.toObject
  EndIf
 EndFunc

 Function This_Access(tcPem As String) As Object
  Local loReturn, luValue, laMembers[1]
  m.loReturn = This
  m.luValue = .Null.

  If Vartype(This.oObject) == "O"
   AMembers(m.laMembers, This.oObject, 0, "GU")
   If (PemStatus(This.oObject, m.tcPem, 5) .And. ;
       Not PemStatus(This.oObject, m.tcPem, 2)) .Or. ;
      Ascan(m.laMembers, m.tcPem, 1, -1, 1, 1+2+4) > 0
    m.loReturn = This.oObject
   Else
    If Not PemStatus(This, m.tcPem, 5)
     Assert .F. Message "PEM: '" + m.tcPem + "' not available."
     AddProperty(This, m.tcPem, .F.)
     m.luValue = This.GetToken(This, m.tcPem)
     
     Store m.luValue To ("This." + m.tcPem)
    EndIf
   EndIf
  EndIf
  
  Return m.loReturn
 EndFunc
 
 Function GetToken(toObject As Object, tcToken As String) As Variant
  Return .Null.
 EndFunc
EndDefine
```

Übrigens nicht erschrecken, ob der vorangestellten Interface-Definiion, aber auf diese Weise mache ich mir das Leben ein wenig einfacher, falls ich mal was suchen sollte. 😁

Wie schon geschrieben, ist die Methode GetToken eigentlich überflüssig, aber dennoch ganz nett. Als beispielhaftes Einsatzgebiet möchte euch mal eine Ableitung des Decorators für Mehrsprachigkeit zeigen. Ich nehme an, dass der 'Nutzen' von GetToken klarer erscheinen dürfte, insbesondere warum ich von einem einfachen Cache spreche:

```
*============================================================
* Concrete class definition for encapsulated language handling.
* This class is referred as object 'Language' in AfpWiki.
*============================================================
Define Class LanguageDecorator As AbstractDecorator
 AfpWiki = "AfpWiki - A wiki engine based on Active_FoxPro_Pages"

 *------------------------------------------------------------
 * Try to gather information from somewhere else. 
 *------------------------------------------------------------
 Function GetToken(toObject As Object, tcToken As String) As Variant
  Local lcReturn

  *--- This could be any method on the decorated object.
  *--- ie. m.lcReturn = This.oObject.MsgSvc(m.tcToken)
  *---     m.lcReturn = This.oObject.QueryXml(m.tcToken)
  *---     m.lcReturn = This.oObject.SqlExecute(This.oObject.nHandle, m.tcToken)
  m.lcReturn = This.oObject.GetToken(This, m.tcToken)
  If Empty(m.lcReturn) .Or. IsNull(m.lcReturn)
   m.lcReturn = This.oObject.Language + ": '" + m.tcToken + "' not definied"
  EndIf

  Return m.lcReturn
 EndFunc
EndDefine
```

Zur Erläuterung: Sofern eine Eigenschaft nicht existieren sollte, können wir potentiell mittels GetToken eine externe Quelle nach dem Wert befragen. Dabei kann es sich um alle mögliche Arten von Quelle handeln - Web Service, Datenbank, XML-Datei, etc.. Den ermittelten Wert legen wir dann in die neu erzeugte Eigenschaft ab, und erreichen hierdurch den Cache-Effekt. Bei einer weiteren Anfrage auf die gleiche Eigenschaft können wir bereits die Information bieten und sparen uns den Remotezugriff auf unsere externe Quelle. Falls wir dennoch keine passable Information erhalten sollen, geben wir eben einen Defaultwert aus.

Ich verwende diesen Decorator wie gesagt für die Abbildung von Mehrsprachigkeit - pro Sprache eine Instanz des Decorators -, und habe dabei den Effekt, dass ich während der Laufzeit sofort erkennen kann, wo meine Übersetzungen bspw. noch lückenhaft sind. *Im übrigen wäre es denkbar, dass GetToken einen Fail-Safe auf die Standardsprache machen könnte...*

So, der Vollständidkeit wegen hier noch die Klassendefinition der Sprachklasse:

```
*============================================================
* 'Abstract' base class for all languages.
* This class defines the interface.
*============================================================
Define Class AbstractLanguage As Relation
 Language = ""
 
 Function GetToken(toObject As Object, tcToken As String) As Variant
   Return ""
 EndFunc
EndDefine

*------------------------------------------------------------
* German translations
*------------------------------------------------------------
Define Class LanguageDE As AbstractLanguage Of "abstract.prg" 
 Language = "de"
 
 CaptionBackup = "Sicherung oder Wiederherstellung des AfpWiki"
 CaptionBuild = "Erstellung AfpWiki"
 CaptionCategory = "Kategorische Ansicht"
 CaptionConnectionError = "Verbindungsfehler zur Datenbank"
 CaptionEdit = "Bearbeiten von "
 CaptionEmpty = "Neuer Eintrag "
 
 Function GetToken(toObject As Object, tcToken As String) As Variant
  Local lcReturn
  m.lcReturn = This.Language + ": '" + m.tcToken + "' nicht definiert"
  
  Return m.lcReturn
 EndFunc
EndDefine
```

Ups, nun habt ihr fast die vollständige Implementierung des Language-Handlings vom AfpWiki... 🤪