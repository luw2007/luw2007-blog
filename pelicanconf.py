AUTHOR = "luw2007"
SITENAME = "luw2007-blog DEV"
SITETITLE = "luw2007 blog Dev - Blogging about programming"
SITEDESCRIPTION = "luw2007 Developer - Blogging about programming"
SITEURL = "https://luw2007.github.io"

DEFAULT_LANG = "zh"
TIMEZONE = "Asia/Shanghai"
DEFAULT_DATE_FORMAT = "%m-%d-%Y"

PATH = "content"
ARTICLE_PATHS = ["archives"]
PAGE_PATHS = ["pages"]
THEME = "themes/tuxlite_tbs"
OUTPUT_PATH = "output"
STATIC_PATHS = ["extra"]
EXTRA_PATH_METADATA = {
    "extra/googlee68dad2e8b5371e9.html": {"path": "googlee68dad2e8b5371e9.html"},
    "extra/lxc-cgroup.html": {"path": "lxc-cgroup.html"},
    "extra/tag-blog.html": {"path": "tag/blog.html"},
    "extra/category-misc.html": {"path": "category/misc.html"},
}

FEED_DOMAIN = SITEURL
FEED_ALL_RSS = "feeds/all.rss.xml"
TAG_FEED_RSS = "feeds/{slug}.rss.xml"

MARKUP = ("md",)
DEFAULT_PAGINATION = 9
REVERSE_ARCHIVE_ORDER = True

LINKS = (
    ("Python", "https://python.org"),
    ("Douban", "https://douban.com"),
)
