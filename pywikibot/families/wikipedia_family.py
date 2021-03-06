# -*- coding: utf-8  -*-
"""Family module for Wikipedia."""
#
# (C) Pywikibot team, 2004-2016
#
# Distributed under the terms of the MIT license.
#
from __future__ import absolute_import, unicode_literals

from pywikibot import family

__version__ = '$Id$'


# The Wikimedia family that is known as Wikipedia, the Free Encyclopedia
class Family(family.SubdomainFamily, family.WikimediaFamily):

    """Family module for Wikipedia."""

    name = 'wikipedia'

    closed_wikis = [
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Afar_Wikipedia
        'aa',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Choctaw_Wikipedia
        'cho',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Hiri_Motu_Wikipedia
        'ho',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Herero_Wikipedia
        'hz',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Yi_Wikipedia
        'ii',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Kwanyama_Wikipedia
        'kj',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Kanuri_Wikipedia
        'kr',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Marshallese_Wikipedia
        'mh',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Moldovan_Wikipedia
        'mo',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Muscogee_Wikipedia
        'mus',
    ]

    removed_wikis = [
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Ndonga_Wikipedia
        'ng',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Siberian_Wikipedia
        'ru-sib',
        # Klingon, locked in 2005, and moved to http://klingon.wikia.com/
        'tlh',
        # https://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Tokipona_Wikipedia
        'tokipona',
    ]

    def __init__(self):
        """Constructor."""
        self.languages_by_size = [
            'en', 'sv', 'ceb', 'de', 'nl', 'fr', 'ru', 'it', 'es', 'war', 'pl',
            'vi', 'ja', 'pt', 'zh', 'uk', 'ca', 'fa', 'no', 'ar', 'sh', 'fi',
            'hu', 'id', 'ro', 'cs', 'ko', 'sr', 'ms', 'tr', 'eu', 'eo', 'min',
            'bg', 'da', 'kk', 'sk', 'hy', 'zh-min-nan', 'he', 'lt', 'hr', 'sl',
            'ce', 'et', 'gl', 'nn', 'uz', 'la', 'el', 'be', 'simple', 'vo',
            'th', 'hi', 'az', 'ur', 'ka', 'oc', 'ta', 'mk', 'mg', 'cy', 'lv',
            'new', 'bs', 'tt', 'tg', 'te', 'tl', 'pms', 'sq', 'br', 'be-tarask',
            'ky', 'ht', 'jv', 'zh-yue', 'ast', 'lb', 'ml', 'mr', 'bn', 'pnb',
            'af', 'sco', 'is', 'ga', 'ba', 'cv', 'fy', 'sw', 'lmo', 'my', 'an',
            'yo', 'ne', 'io', 'gu', 'nds', 'scn', 'bpy', 'pa', 'ku', 'als',
            'bar', 'kn', 'ia', 'qu', 'su', 'ckb', 'bat-smg', 'mn', 'arz', 'nap',
            'wa', 'gd', 'bug', 'yi', 'map-bms', 'am', 'si', 'mzn', 'fo', 'li',
            'nah', 'or', 'sah', 'vec', 'hsb', 'azb', 'os', 'sa', 'mrj', 'hif',
            'mhr', 'roa-tara', 'pam', 'ilo', 'eml', 'sd', 'xmf', 'ps', 'bh',
            'se', 'mi', 'hak', 'bcl', 'diq', 'gan', 'glk', 'vls', 'rue',
            'nds-nl', 'bo', 'fiu-vro', 'co', 'wuu', 'tk', 'sc', 'csb', 'vep',
            'lrc', 'szl', 'km', 'crh', 'gv', 'mai', 'kv', 'frr', 'zh-classical',
            'zea', 'as', 'so', 'cdo', 'nso', 'stq', 'kw', 'udm', 'ay', 'nrm',
            'lad', 'ie', 'koi', 'ace', 'rm', 'myv', 'pcd', 'lij', 'mt', 'fur',
            'gn', 'dsb', 'dv', 'cbk-zam', 'ksh', 'ext', 'kab', 'ang', 'ln',
            'mwl', 'lez', 'gag', 'ug', 'sn', 'frp', 'pag', 'pi', 'gom', 'nv',
            'av', 'pfl', 'xal', 'krc', 'haw', 'kaa', 'rw', 'bxr', 'pdc', 'to',
            'nov', 'kl', 'arc', 'pap', 'lo', 'kbd', 'bjn', 'jam', 'ha', 'tet',
            'ki', 'tyv', 'tpi', 'ig', 'na', 'lbe', 'jbo', 'roa-rup', 'ty', 'kg',
            'za', 'mdf', 'lg', 'wo', 'srn', 'ab', 'ltg', 'zu', 'sm', 'chr',
            'om', 'tcy', 'tn', 'chy', 'rmy', 'tw', 'cu', 'xh', 'tum', 'bi',
            'rn', 'pih', 'got', 'ch', 'ss', 'pnt', 'bm', 'ady', 'ts', 'iu',
            'ny', 'st', 'fj', 'ee', 'ak', 'ks', 'ik', 'sg', 've', 'ff', 'dz',
            'ti', 'cr', 'olo',
        ]

        # Sites we want to edit but not count as real languages
        self.test_codes = ['test', 'test2']

        super(Family, self).__init__()

        self.category_redirect_templates = {
            '_default': (),
            'ar': (u'تحويل تصنيف',
                   u'تحويلة تصنيف',
                   u'Category redirect',),
            'arz': (u'تحويل تصنيف',),
            'cs': (u'Zastaralá kategorie',),
            'da': (u'Kategoriomdirigering',),
            'en': (u'Category redirect',),
            'es': (u'Categoría redirigida',),
            'eu': (u'Kategoria redirect',),
            'fa': (u'رده بهتر',
                   u'انتقال رده',),
            'fr': (u'Redirection de catégorie',),
            'gv': (u'Aastiurey ronney',),
            'hi': (u'श्रेणीअनुप्रेषित',
                   u'Categoryredirect',),
            'hu': (u'Kat-redir',
                   u'Katredir',
                   u'Kat-redirekt',),
            'id': (u'Alih kategori',
                   u'Alihkategori',),
            'ja': (u'Category redirect',),
            'ko': (u'분류 넘겨주기',),
            'mk': (u'Премести категорија',),
            'ml': (u'Category redirect',),
            'ms': (u'Pengalihan kategori',
                   u'Categoryredirect',
                   u'Category redirect',),
            'mt': (u'Redirect kategorija',),
            'no': (u'Category redirect',
                   u'Kategoriomdirigering',
                   u'Kategori-omdirigering',),
            'pl': (u'Przekierowanie kategorii',
                   u'Category redirect',),
            'pt': (u'Redirecionamento de categoria',
                   u'Redircat',
                   u'Redirect-categoria',),
            'ro': (u'Redirect categorie',),
            'ru': (u'Переименованная категория',
                   u'Categoryredirect',
                   u'CategoryRedirect',
                   u'Category redirect',
                   u'Catredirect',),
            'sco': ('Category redirect',),
            'simple': (u'Category redirect',
                       u'Categoryredirect',
                       u'Catredirect',),
            'sh': (u'Prekat',
                   u'Preusmeri kategoriju',
                   u'Preusmjeri kategoriju',
                   u'Prekategorizuj',
                   u'Catred',
                   u'Catredirect',
                   u'Category redirect'),
            'sl': (u'Category redirect',),
            'sq': (u'Kategori e zhvendosur',
                   u'Category redirect',),
            'sv': (u'Kategoriomdirigering',
                   u'Omdirigering kategori',),
            'tl': (u'Category redirect',),
            'tr': (u'Kategori yönlendirme',
                   u'Kat redir',),
            'uk': (u'Categoryredirect',),
            'vi': (u'Đổi hướng thể loại',
                   u'Thể loại đổi hướng',
                   u'Chuyển hướng thể loại',
                   u'Categoryredirect',
                   u'Category redirect',
                   u'Catredirect',),
            'yi': (u'קאטעגאריע אריבערפירן',),
            'zh': (u'分类重定向',
                   u'Cr',
                   u'CR',
                   u'Cat-redirect',),
            'zh-yue': (u'Category redirect',
                       u'分類彈去',
                       u'分類跳轉',),
        }

        # families that redirect their interlanguage links here.
        self.interwiki_forwarded_from = [
            'commons',
            'incubator',
            'meta',
            'species',
            'strategy',
            'test',
        ]

        # Global bot allowed languages on
        # https://meta.wikimedia.org/wiki/Bot_policy/Implementation#Current_implementation
        self.cross_allowed = [
            'ab', 'ace', 'af', 'ak', 'als', 'am', 'an', 'ang', 'ar', 'arc',
            'arz', 'as', 'ast', 'av', 'ay', 'az', 'ba', 'bar', 'bat-smg', 'bcl',
            'be', 'be-tarask', 'bg', 'bh', 'bi', 'bjn', 'bm', 'bo', 'bpy', 'bug',
            'bxr', 'ca', 'cbk-zam', 'cdo', 'ce', 'ceb', 'ch', 'chr', 'chy',
            'ckb', 'co', 'cr', 'crh', 'csb', 'cu', 'cv', 'cy', 'da', 'diq',
            'dsb', 'dz', 'ee', 'el', 'eml', 'en', 'eo', 'et', 'eu', 'ext', 'fa',
            'ff', 'fi', 'fj', 'fo', 'frp', 'frr', 'fur', 'ga', 'gag', 'gan',
            'gd', 'glk', 'gn', 'got', 'gu', 'gv', 'ha', 'hak', 'haw', 'he',
            'hi', 'hif', 'hr', 'hsb', 'ht', 'hu', 'hy', 'ia', 'ie', 'ig', 'ik',
            'ilo', 'io', 'iu', 'ja', 'jbo', 'jv', 'ka', 'kaa', 'kab', 'kdb',
            'kg', 'ki', 'kk', 'kl', 'km', 'kn', 'ko', 'koi', 'krc', 'ks', 'ku',
            'kv', 'kw', 'ky', 'la', 'lad', 'lb', 'lbe', 'lez', 'lg', 'li',
            'lij', 'lmo', 'ln', 'lo', 'lt', 'ltg', 'lv', 'map-bms', 'mdf', 'mg',
            'mhr', 'mi', 'mk', 'ml', 'mn', 'mrj', 'ms', 'mwl', 'my', 'myv',
            'mzn', 'na', 'nah', 'nap', 'nds-nl', 'ne', 'new', 'nl', 'no', 'nov',
            'nrm', 'nso', 'nv', 'ny', 'oc', 'om', 'or', 'os', 'pa', 'pag',
            'pam', 'pap', 'pdc', 'pfl', 'pi', 'pih', 'pms', 'pnb', 'pnt', 'ps',
            'qu', 'rm', 'rmy', 'rn', 'roa-rup', 'roa-tara', 'ru', 'rue', 'rw',
            'sa', 'sah', 'sc', 'scn', 'sco', 'sd', 'se', 'sg', 'sh', 'si',
            'simple', 'sk', 'sm', 'sn', 'so', 'srn', 'ss', 'st', 'stq', 'su',
            'sv', 'sw', 'szl', 'ta', 'te', 'tet', 'tg', 'th', 'ti', 'tk', 'tl',
            'tn', 'to', 'tpi', 'tr', 'ts', 'tt', 'tum', 'tw', 'ty', 'udm', 'ug',
            'uz', 've', 'vec', 'vep', 'vls', 'vo', 'wa', 'war', 'wo', 'wuu',
            'xal', 'xh', 'yi', 'yo', 'za', 'zea', 'zh', 'zh-classical',
            'zh-min-nan', 'zh-yue', 'zu',
        ]

        # On most Wikipedias page names must start with a capital letter,
        # but some languages don't use this.
        self.nocapitalize = ['jbo']

        # Languages that used to be coded in iso-8859-1
        self.latin1old = [
            'de', 'en', 'et', 'es', 'ia', 'la', 'af', 'cs', 'fr', 'pt', 'sl',
            'bs', 'fy', 'vi', 'lt', 'fi', 'it', 'no', 'simple', 'gl', 'eu',
            'nds', 'co', 'mi', 'mr', 'id', 'lv', 'sw', 'tt', 'uk', 'vo', 'ga',
            'na', 'es', 'nl', 'da', 'dk', 'sv', 'test']

        # Subpages for documentation.
        # TODO: List is incomplete, to be completed for missing languages.
        # TODO: Remove comments for appropriate pages
        self.doc_subpages = {
            '_default': ((u'/doc', ),
                         ['ar', 'bn', 'cs', 'da', 'en', 'es',
                          'hu', 'id', 'ilo', 'ja', 'ms',
                          'ms', 'pt', 'ro', 'ru', 'simple', 'vi', 'zh']
                         ),
            'ca': (u'/ús', ),
            'de': (u'Doku', u'/Meta'),
            'dsb': (u'/Dokumentacija', ),
            'eu': (u'txantiloi dokumentazioa', u'/dok'),
            'fa': (u'/doc', u'/توضیحات'),
            # fi: no idea how to handle this type of subpage at :Metasivu:
            'fi': ((), ),
            'fr': (u'/documentation', ),
            'hsb': (u'/Dokumentacija', ),
            'it': (u'/Man', ),
            'ka': (u'/ინფო', ),
            'ko': (u'/설명문서', ),
            'no': (u'/dok', ),
            'nn': (u'/dok', ),
            'pl': (u'/opis', ),
            'sk': (u'/Dokumentácia', ),
            'sv': (u'/dok', ),
            'uk': (u'/Документація', ),
        }

    def get_known_families(self, site):
        """Override the family interwiki prefixes for each site."""
        # In Swedish Wikipedia 's:' is part of page title not a family
        # prefix for 'wikisource'.
        if site.code == 'sv':
            d = self.known_families.copy()
            d.pop('s')
            d['src'] = 'wikisource'
            return d
        else:
            return self.known_families

    def code2encodings(self, code):
        """Return a list of historical encodings for a specific site."""
        # Historic compatibility
        if code == 'pl':
            return 'utf-8', 'iso8859-2'
        if code == 'ru':
            return 'utf-8', 'iso8859-5'
        if code in self.latin1old:
            return 'utf-8', 'iso-8859-1'
        return self.code2encoding(code)
