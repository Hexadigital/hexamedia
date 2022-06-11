AUTHOR = 'Hexadigital'
SITENAME = 'HexaMedia'
SITEURL = 'https://hexa.media'

PATH = 'content'

TIMEZONE = 'America/Detroit'

DEFAULT_LANG = 'en'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
RSS_FEED_SUMMARY_ONLY = False

BOOTSTRAP_THEME = 'slate'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['i18n_subsites']
THEME = '../pelican-themes/pelican-bootstrap3/'

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
'''SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)'''

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'
TAG_URL = 'tagged/{slug}.html'
TAG_SAVE_AS = 'tagged/{slug}.html'
AUTHOR_SAVE_AS = ''