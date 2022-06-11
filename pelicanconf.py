# Core
AUTHOR = 'Hexadigital'
BOOTSTRAP_THEME = 'slate'
DEFAULT_LANG = 'en'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PATH = 'content'
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['i18n_subsites']
SITENAME = 'HexaMedia'
SITEURL = 'https://hexa.media'
THEME = 'pelican-bootstrap3'
TIMEZONE = 'America/Detroit'

# About Me
ABOUT_ME = 'Hex is a software developer, game reviewer, gardener, music producer, streamer, and more.'
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

# Shariff
SHARIFF = True
SHARIFF_LANG = 'en'
SHARIFF_SERVICES = "[&quot;facebook&quot;,&quot;googleplus&quot;]"

# Social widget
SOCIAL = (
    ('Discord', 'https://discord.gg/a9khY6U'),
    ('Steam', 'https://store.steampowered.com/curator/34633900/'),
    ('Twitch', 'https://www.twitch.tv/hexadigital'),
    ('Twitter', 'https://twitter.com/HexsGameplay'),
    ('YouTube', 'https://www.youtube.com/c/HexsGameplay'),
)

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
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True