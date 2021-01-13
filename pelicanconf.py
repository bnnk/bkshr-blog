#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'BK Shrinandhan'
SITENAME = "BK Shrinandhan's Favorite Blog"
SITEURL = 'https://8000-e9d30ff6-55c7-4b37-ad4b-0308fbfb3295.ws-us03.gitpod.io'

HEADER_COVER='/assets/blog-cover.png'
PATH = 'content'
READ_MORE_LINK_FORMAT = '<a class="read-more" href="/{url}">ghg</a>'
SUMMARY_MAX_LENGTH = 20

TIMEZONE = 'Asia/Calcutta'

DEFAULT_LANG = 'en'

HEADER_COVERS_BY_TAG = {'cupcake': 'assets/images/rainbow_cupcake_cover.png', 'general':'https://casper.ghost.org/v1.0.0/images/writing.jpg'}

AUTHORS_BIO = {
  "zutrinken": {
    "name": "Zutr",
    "cover": "https://casper.ghost.org/v1.0.0/images/team.jpg",
    "image": "assets/images/blog_cover.png",
    "website": "http://blog.arulraj.net",
    "linkedin": "unavailable",
    "github": "arulrajnet",
    "location": "Chennai",
    "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"
  }
}


PLUGIN_PATHS = ["plugins"]
PLUGINS=["readtime","jinja2content","latex","read_more_link"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
THEME="atila"