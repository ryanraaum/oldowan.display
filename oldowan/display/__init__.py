"""This is the oldowan.display package."""

import os

VERSION = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'VERSION')).read().strip()

__all__ = []

#try:
    #from oldowan.display.html_display import html_display
#except:
    #from html_display import html_display

