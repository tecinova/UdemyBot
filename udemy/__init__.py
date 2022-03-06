# UdemyBot - A Simple Udemy Free Courses Scrapper

# Copyright (C) 2021-Present Gautam Kumar <https://github.com/gautamajay52>

import os

token = os.environ.get('5198316929:AAHOX1bvu6vjOXzJoih5sD0wNmEciHVkMdM')
api_id = os.environ.get('15195863')
api_hash = os.environ.get('4dad34223333dc397e0142223dac5c2b')

START = """
Hey, I'm an UdemyBot. ⚡

I can send you free Udemy Courses Links.

Commands:
    /discudemy page
    /udemy_freebies page
    /tutorialbar page
    /real_discount page
    /coursevania
    /idcoupons page

page - which page you wanted to scrap and send links. Default is 1
"""

CMD = "(discudemy|coursevania|udemy_freebies|tutorialbar|real_discount|idcoupons)"
