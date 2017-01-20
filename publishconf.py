#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import sys

sys.path.append(os.curdir)

from pelicanconf import *  # noqa


SITEURL = 'https://blog.data.gouv.fr'
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom'
CATEGORY_FEED_ATOM = 'feeds/%s.atom'

# Not useable
# ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{name}/'
# CATEGORY_URL = 'category/{slug}/'
# TAG_URL = 'tag/{slug}/'
# PAGE_URL = '{name}/'
# Pages

# Pretty URLS
# Tricks github pages by using slash-ended pretty url and fallback on index.html
PAGE_URL = '{name}/'
PAGE_SAVE_AS = '{name}/index.html'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{name}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{name}/index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

TAGS_URl = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'

AUTHOR_URL = 'authors/{slug}/'
AUTHOR_SAVE_AS = 'authors/{slug}/index.html'

ARCHIVES_URL = 'archvives/'
ARCHIVES_SAVE_AS = 'archvives/index.html'


DELETE_OUTPUT_DIRECTORY = True

PLUGINS += (  # noqa
    # 'image_optimizer',
    'gzip_cache',
)
