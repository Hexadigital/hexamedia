# Core
AUTHOR = 'Hexadigital'
BOOTSTRAP_THEME = 'slate'
DEFAULT_LANG = 'en'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PATH = 'content'
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['i18n_subsites']
SITENAME = 'HexaMedia'
SITEURL = 'https://hexa.media'
#THEME = 'pelican-bootstrap3'
THEME = 'bootstrap-next'
TIMEZONE = 'America/Detroit'

STATIC_PATHS = ['images', 'files', 'js']

#BOOTSTRAP_NAVBAR_INVERSE = True

# About Me
ABOUT_ME = '''Nice to meet you! I'm Hex, a VTuber focusing on playing games from start to end, from all eras and for all platforms. In my free time, I enjoy gardening and coding.'''

AVATAR = 'images/avatar.png'

# Blogroll
'''LINKS = (
    ('Pelican', 'https://getpelican.com/'),
)'''

# Footer
FOOTER_IMAGES = ['images/budgie.png']

# RSS
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
RSS_FEED_SUMMARY_ONLY = False

# Social widget
SOCIAL = (
    ('Discord', 'https://discord.gg/a9khY6U'),
    ('Fediverse', 'https://bird.band/@Hexadigital'),
    #('Patreon', 'https://www.patreon.com/hexadigital'),
    ('Steam', 'https://store.steampowered.com/curator/34633900/'),
    ('Twitch', 'https://www.twitch.tv/hexadigital'),
    ('Twitter', 'https://twitter.com/Hexadigital_'),
    ('YouTube', 'https://www.youtube.com/c/HexsGameplay'),
)

USE_PAGER = True
DEFAULT_PAGINATION = 10

# URL Rules
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'
TAG_URL = 'tagged/{slug}.html'
TAG_SAVE_AS = 'tagged/{slug}.html'
AUTHOR_SAVE_AS = ''
RELATIVE_URLS = True
