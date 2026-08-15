/*
Language: Visual FoxPro (FoxPro, VFP, PRG)
Author: Rick Strahl <rstrahl@west-wind.com>
Website: https://west-wind.com
Gist: https://gist.github.com/RickStrahl/abe68c71410b261ec0e230325d98b1a1

Original Source:
https://gist.githubusercontent.com/RickStrahl/abe68c71410b261ec0e230325d98b1a1/raw/1247a6a2021ae3d68742e728dfb1f9432b6f4b2b/foxpro-highlighjs-addin.js
Copyright (c) Rick Strahl, West Wind Technologies. All rights reserved.

Usage:
<script src="./scripts/highlight.min.js"></script>
<script src="./public/js/foxpro-highlightjs-addin.js"></script>
*/

/** @type LanguageFn */
function hljsFoxPro(hljs) {
  return {
    aliases: ['foxpro', 'vfp', 'fox', 'prg', 'visualfoxpro', 'xbase'],
    case_insensitive: true,
    keywords: {
      keyword:
        "additive " +
        "by " +
        "case catch cursor custom " +
        "declare define do " +
        "each else endcase enddefine enddo endfor endfunc endif endprintjob endproc endscan endtext endtry endwith error exit " +
        "finally for from function func " +
        "hidden " +
        "if " +
        "local lparameter lparameters " +
        "next noshow " +
        "otherwise " +
        "parameters printjob procedure proc protected public " +
        "scan " +
        "text then throw to try " +
        "while with " +
        "activate add alter alternate ansi app append array assert asserts assist autoincerror autosave average " +
        "bar begin bell blank blocksize border box browse browseime brstatus build " +
        "calculate call cancel carry catch cd century change chdir class classlib clear clock close collate color compatible compile confirm connection connections console continue copy count coverage cpcompile cpdialog create currency cursor cursor " +
        "database datasession date deactivate debug debugout decimals declare default define delete deleted delimiters development device dimension dir directory display dll dlls dock doevents dohistory drop " +
        "echo edit eject end enginebehavior erase error escape eventlist events eventtracking exact exclusive exe export extended external " +
        "fdow fields file files filter finally find fixed flush form format free from fullpath function fweek " +
        "gather general get getexpr gets go goto " +
        "headings help hide hours " +
        "id import in index indexes input insert intensity into " +
        "join " +
        "key keyboard keycomp " +
        "label library list load local locate lock logerrors loop lparameters " +
        "mackey macro macros margin mark md memo memory memowidth menu menus message mkdir modify mouse move mtdll multilocks " +
        "near nocptrans note notify nulldisplay nowshow " +
        "object objects odometer of off oleobject on open optimize order " +
        "pack pad page palette parameters path pdsetup play point pop popup popups printer private procedure procedures project public push " +
        "query quit" +
        "rd read readborder readerror recall refresh reindex relation release remove rename replace report reprocess resource restore resume retry return rmdir rollback run " +
        "safety save scan scatter scheme screen scroll seconds seek select selection separator set show shutdown size skip skip sort space sql status step store strictdate structure sum suspend sysformats sysmenu " +
        "table tables tablevalidate tag talk textmerge this throw to topic total transaction trbetween trigger try type typeahead " +
        "udfparms unbindevents unique unlock update use " +
        "validate view views " +
        "wait where window windows windows win32api " +
        "zap zoom",
      built_in:
        'abs aclass acopy acos adatabases adbobjects addbs addproperty adel adir adlls adockstate aelement aerror aevents afields afont agetclass agetfileversion ains ainstance alanguage alen alias alines alltrim amembers amouseobj anetresources aprinters aprocinfo asc ascan aselobj asessions asin asort astackinfo asubscript at at_c ataginfo atan atc atcc atcline atline atn2 aused avcxclasses ' +
        'bar barcount barprompt between bindevent bintoc bitand bitclear bitlshift bitnot bitor bitrshift bitset bittest bitxor bof ' +
        'candidate capslock cdow cdx ceiling chr chrsaw chrtran chrtranc cmonth cntbar cntpad col com comarray comclassinfo compobj comprop comreturnerror cos cpconvert cpcurrent cpdbf createbinary createobject createobjectex createoffline ctobin ctod ctot curdir cursorgetprop cursorsetprop cursortoxml curval ' +
        'date datetime day dbc dbf dbgetprop dbsetprop dbused ddeaborttrans ddeadvise ddeenabled ddeexecute ddeinitiate ddelasterror ddepoke dderequest ddesetoption ddesetservice ddesettopic ddeterminate defaultext deleted descending difference directory diskspace displaypath dmy dodefault doevents dow drivetype dropoffline dtoc dtor dtos dtot ' +
        'editsource empty eof error evaluate eventhandler evl execscript exp ' +
        'fchsize fclose fcount fcreate fdate feof ferror fflush fgets field file filetostr filter fklabel fkmax fldlist flock floor fontmetric fopen forceext forcepath found fputs fread fseek fsize ftime fullpath function command fv fwrite ' +
        'getbar getcolor getcp getdir getenv getfile getfldstate getfont getinterface getnextmodified getobject getpad getpem getpict getprinter getwordcount getwordnum getcursoradapter gomonth ' +
        'header home hour ' +
        'idxcollate iif imestatus indbc indexseek inkey inlist inputbox insmode int integer isalpha isblank iscolor isdigit isexclusive isflocked isleadbyte islower ismouse isnull isreadonly isrlocked isupper ' +
        'justdrive justext justfname justpath juststem ' +
        'key keymatch ' +
        'lastkey left leftc len lenc like likec lineno loadpicture locfile lock log log10 lookup lower ltrim lupdate ' +
        'max mcol mdown mdx mdy memlines memory menu message messagebox min minute mline mod month mrkbar mrkpad mrow mton mwindow ' +
        'ndx newobject normalize nowait noshow ntom numlock nvl ' +
        'objnum objtoclient objvar occurs oemtoansi oldval on order os ' +
        'pad padl padr padc parameters payment pcol pcount pemstatus pi popup primary printstatus prmbar prmpad program prompt proper prow prtinfo putfile pv ' +
        'quarter ' +
        'raiseevent rand rat ratc ratline rdlevel readkey reccount recno recsize refresh relation replicate requery rgb rgbscheme right rightc rlock round row rtod rtrim ' +
        'savepicture scheme scols sec seconds seek set setfldstate sign sin skpbar skppad soundex space sqlcancel sqlcolumns sqlcommit sqlconnect sqldisconnect sqlexec sqlgetprop sqlmoreresults sqlprepare sqlrollback sqlsetprop sqlstringconnect sqltables sqrt srows str strconv strextract strtofile strtran stuff stuffc substr substrc syss overview sysmetric ' +
        'tablerevert tableupdate tag tagcount tagno tan target textmerge time transform trim ttoc ttod txnlevel txtwidth type ' +
        'unbindevents unique updated upper used ' +
        'val varread vartype version ' +
        'wborder wchild wcols wdockable week wexist wfont wlast wlcol wlrow wmaximum wminimum wontop woutput wparent wread wrows wtitle wvisible ' +
        'xmltocursor xmlupdategram ' +
        'year_alignment _asciicols _asciirows _assist _beautify _box _browser _builder _calcmem _calcvalue _cliptext _converter _coverage _coverage _curobj ' +
        '_dblclick _diarydate _dos _foxdoc _foxgraph _gallery _gengraph _genhtml _genmenu _genpd _genscrn _genxtab _getexpr _include _indent ' +
        '_lmargin _mac _mda_appnd _mda_avg _mda_brow _mda_calc _mda_copy _mda_count _mda_label _mda_pack _mda_reprt _mda_rindx _mda_setup _mda_sort ' + 
        '_mda_sp100 _mda_sp200 _mda_sp300 _mda_sum _mda_total _mdata _mdiary _med_clear _med_copy _med_cut _med_cvtst _med_find _med_finda _med_goto _med_insob ' +
        '_med_link _med_obj _med_paste _med_pref _med_pstlk _med_redo _med_repl _med_repla _med_slcta _med_sp100 _med_sp200 _med_sp300 _med_sp400 _med_sp500 _med_undo _medit ' +
        '_mfi_clall _mfi_close _mfi_export _mfi_import _mfi_new _mfi_open _mfi_pgset _mfi_prevu _mfi_print _mfi_quit _mfi_revrt _mfi_savas _mfi_save _mfi_send ' +
        '_mfi_setup _mfi_sp100 _mfi_sp200 _mfi_sp300 _mfi_sp400 _mfile _mfiler _mfirst _mlabel _mlast _mline _mmacro _mmbldr _mpr_beaut _mpr_cancl ' +
        '_mpr_compl _mpr_do _mpr_docum _mpr_formwz _mpr_gener _mpr_graph _mpr_resum _mpr_sp100 _mpr_sp200 _mpr_sp300 _mpr_suspend _mprog _mproj _mrc_appnd ' + 
        '_mrc_chnge _mrc_cont _mrc_delet _mrc_goto _mrc_locat _mrc_recal _mrc_repl _mrc_seek _mrc_sp100 _mrc_sp200 _mrecord _mreport _mrqbe _mscreen _msm_data ' +
        '_msm_edit _msm_file _msm_format _msm_prog _msm_recrd _msm_systm _msm_text _msm_tools _msm_view _msm_windo _mst_about _mst_ascii _mst_calcu ' + 
        '_mst_captr _mst_dbase _mst_diary _mst_filer _mst_help _mst_hphow _mst_hpsch _mst_macro _mst_office _mst_puzzl _mst_sp100 _mst_sp200 _mst_sp300 ' +
        '_mst_specl _msysmenu _msystem _mtable _mtb_appnd _mtb_cpart _mtb_delet _mtb_delrc _mtb_goto _mtb_link _mtb_mvfld _mtb_mvprt _mtb_props _mtb_recal ' +
        '_mtb_sp100 _mtb_sp200 _mtb_sp300 _mtb_sp400 _mtb_szfld _mwi_arran _mwi_clear _mwi_cmd _mwi_color _mwi_debug _mwi_hide _mwi_hidea _mwi_min ' +
        '_mwi_move _mwi_rotat _mwi_showa _mwi_size _mwi_sp100 _mwi_sp200 _mwi_toolb _mwi_trace _mwi_view _mwi_zoom _mwindow _mwizards _mwz_all _mwz_form ' +
        '_mwz_foxdoc _mwz_import _mwz_label _mwz_mail _mwz_pivot _mwz_query _mwz_reprt _mwz_setup _mwz_table _mwz_upsizing _netware _oracle _padvance ' + 
        '_pageno _pbpage _pcolno _pcopies _pdparms _pdriver _pdsetup _pecode _peject _pepage _pform _plength _plineno _ploffset _ppitch _pquality _pretext ' + 
        '_pscode _pspacing _pwait _rmargin _runactivedoc _samples _screen _shell _spellchk _sqlserver _startup _tabs _tally _text _throttle _transport ' +
        '_triggerlevel _unix _webdevonly _webmenu _webmsfthomepage _webvfphomepage _webvfponlinesupport _windows _wizard _wrap _scctext _vfp',
      literal: '\\.t\\. \\.f\\. null'
    },
    illegal: '//',
    contains: [
      {
        className: 'string',
        begin: '\'', end: '\''
      },
      {
        className: 'string',
        begin: '"', end: '"'
      },
      {
        className: 'string',
        begin: '\\[', end: '\\]'
      },
      {
        className: 'meta',
        begin: '#', end: '$',
        keywords: {'meta-keyword': '#if #elseif #endif #define #undefine'}
      },
      hljs.COMMENT(
        /(^\s*\*)|(\&\&)/,
        /$/,
        {
          relevance: 0
        }),
      hljs.C_NUMBER_MODE
    ]
  };
}

function registerVfpLanguage(hljs) {
  if (!hljs || typeof hljs.registerLanguage !== 'function') return;
  if (hljs.getLanguage('foxpro') || hljs.getLanguage('vfp')) return;
  hljs.registerLanguage('foxpro', hljsFoxPro);
  var vfpDef = hljs.getLanguage('foxpro');
  if (vfpDef && !hljs.getLanguage('vfp')) {
    hljs.registerLanguage('vfp', function() { return vfpDef; });
  }
}

if (typeof window !== 'undefined') {
  window.hljsFoxPro = hljsFoxPro;
  window.registerVfpLanguage = registerVfpLanguage;
  if (window.hljs && typeof window.hljs.registerLanguage === 'function') {
    registerVfpLanguage(window.hljs);
  }
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = hljsFoxPro;
}
