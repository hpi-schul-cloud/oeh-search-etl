# -*- coding: utf-8 -*-
from pathlib import Path  # python3 only
import converter.env as env

# Scrapy settings for project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "converter_search_idx"

SPIDER_MODULES = ["converter.spiders"]
NEWSPIDER_MODULE = "converter.spiders"

LOG_FILE = env.get("LOG_FILE", allow_null=True)
LOG_LEVEL = env.get("LOG_LEVEL", default="INFO")
LOG_FORMATTER = "converter.custom_log_formatter.CustomLogFormatter"

# Default behaviour for regular crawlers of non-license-controlled content
# When set True, every item will have GROUP_EVERYONE attached in edu-sharing
# When set False, no permissions are set at all, which can be helpful if you want to control them later (e.g. via inherition)
DEFAULT_PUBLIC_STATE = False

# Splash (Web Thumbnailer)
# Will be rolled out via docker-compose by default
SPLASH_URL = (
    None if env.get_bool("DISABLE_SPLASH", default=False) else env.get("SPLASH_URL")
)
SPLASH_WAIT = 2  # seconds to let the page load
SPLASH_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
}  # use chrome to not create warnings on pages

# edu-sharing config
EDU_SHARING_BASE_URL = env.get("EDU_SHARING_BASE_URL")
EDU_SHARING_USERNAME = env.get("EDU_SHARING_USERNAME")
EDU_SHARING_PASSWORD = env.get("EDU_SHARING_PASSWORD")

# Thumbnail config
THUMBNAIL_SMALL_SIZE = 250 * 250
THUMBNAIL_SMALL_QUALITY = 40
THUMBNAIL_LARGE_SIZE = 800 * 800
THUMBNAIL_LARGE_QUALITY = 60
THUMBNAIL_MAX_SIZE = (
    1 * 1024 * 1024
)  # max size for images that can not be converted (e.g. svg)


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'converter_search_idx (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'converter.middlewares.OerScrapySpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#   'converter.middlewares.OerScrapyDownloaderMiddleware': 543,
#  'converter.middlewares.CustomRetryMiddleware' : 340,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
    #  'scrapy.extensions.telnet.TelnetConsole': None,
    #  'scrapy.extensions.closespider.CLOSESPIDER_PAGECOUNT': 4,
}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
storeMode = env.get("MODE", default='edu-sharing')
ITEM_PIPELINES = {
    "converter.pipelines.EduSharingCheckPipeline": 0,
    "converter.pipelines.FilterSparsePipeline": 25,
    "converter.pipelines.LOMFillupPipeline": 100,
    "converter.pipelines.NormLicensePipeline": 125,
    "converter.pipelines.ConvertTimePipeline": 200,
    "converter.pipelines.ProcessValuespacePipeline": 250,
    "converter.pipelines.ProcessThumbnailPipeline": 300,
    (
        "converter.pipelines.DummyPipeline"
        if storeMode == "None"
        else "converter.pipelines.CSVStorePipeline"
        if storeMode == 'csv'
        else "converter.pipelines.JSONStorePipeline"
        if storeMode == 'json'
        else "converter.pipelines.EduSharingStorePipeline"
    ): 1000,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = False
# The initial download delay
AUTOTHROTTLE_START_DELAY = 1
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Enables useful test exports with `scrapy crawl -o my-test-output.json <spider>`
FEED_EXPORT_FIELDS = [
    "collection",
    "fulltext",
    "hash",
    "lastModified",
    "license",
    "lom",
    "origin",
    "permissions",
    "publisher",
    "ranking",
    # Response cannot be serialized since it has `bytes` keys
    # "response",
    "sourceId",
    # Too much clutter
    "thumbnail",
    "type",
    "uuid",
    "valuespaces",
]
FEED_EXPORT_INDENT = 2
FEED_EXPORT_ENCODING = "utf-8"
