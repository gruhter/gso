from ZPublisher.BaseRequest import BaseRequest
from ZPublisher.HTTPRequest import HTTPRequest

to_patch = [BaseRequest, HTTPRequest]

try:
    from zope.publisher.base import BaseRequest as ZPBaseRequest
    from zope.publisher.ftp import FTPRequest
    from zope.publisher.http import HTTPRequest as ZPHTTPRequest
    to_patch += [ZPBaseRequest, FTPRequest, ZPHTTPRequest]
except ImportError:
    pass


for c in to_patch:
    try:
        del c.__doc__
    except:
        pass
