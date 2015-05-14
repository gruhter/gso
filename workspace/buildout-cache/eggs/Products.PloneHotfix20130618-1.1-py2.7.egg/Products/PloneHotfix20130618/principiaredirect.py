from urlparse import urlparse

from OFS.Application import Application
from zExceptions import BadRequest
from zExceptions import Redirect


def PrincipiaRedirect(self, destination, URL1):
    """Utility function to allow user-controlled redirects"""

    # Relative URLs aren't part of the spec, but are accepted by some
    # browsers.
    for part, base in zip(urlparse(destination)[:3],
                          urlparse(self.REQUEST['BASE1'])[:3]):
        if not part:
            continue
        if not part.startswith(base):
            raise BadRequest

    if destination.find('//') >= 0:
        raise Redirect(destination)
    raise Redirect("%s/%s" % (URL1, destination))


Application.PrincipiaRedirect = \
Application.ZopeRedirect = \
Application.Redirect = PrincipiaRedirect
