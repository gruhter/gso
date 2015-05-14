import re

from Products.CMFPlone.URLTool import URLTool


orig = URLTool.isURLInPortal


def wrapped_in_portal(self, url, context=None):
    url = re.sub('^[\x00-\x20]+', '', url).strip()
    try:
        return orig(self, url, context)
    except TypeError, e:
        if 'isURLInPortal() takes exactly 2 arguments' in e.args[0]:
            return orig(self, url)
        else:
            raise

wrapped_in_portal.__doc__ = orig.__doc__
URLTool.isURLInPortal = wrapped_in_portal
