import logging

from AccessControl import Unauthorized
from Acquisition import aq_inner
try:
    try:
        from Products.Archetypes.UIDCatalog import UIDCatalogBrains
    except ImportError:
        from Products.Archetypes.ReferenceEngine import UIDCatalogBrains
    try:
        from Products.Archetypes.UIDCatalog import UIDResolver
    except ImportError:
        from Products.Archetypes.ReferenceEngine import ReferenceResolver as UIDResolver
    try:
        from Products.Archetypes.ReferenceEngine import ReferenceEngine
    except ImportError:
        from Products.Archetypes.ReferenceEngine import ReferenceCatalog as ReferenceEngine
    from Products.CMFCore.utils import getToolByName
    try:
        from Products.Archetypes.UIDCatalog import logger
    except ImportError:
        logger = logging.getLogger('Archetypes')
    PATCH_AT = True
except ImportError:
    PATCH_AT = False
from Products.ZCatalog.ZCatalog import ZCatalog
from zExceptions import NotFound
try:
    from ZODB.POSException import ConflictError
except ImportError:
    class ConflictError(Exception):
        pass


if PATCH_AT:
    # There doesn't seem to be a clear reason why this was even overridden in
    # the first place.
    del UIDResolver.resolve_url

    UIDCatalogBrains.getObject__roles__ = ()
    ReferenceEngine.getBackReferences__roles__ = ()
    ReferenceEngine.getReferences__roles__ = ()


ZCatalog.resolve_path__roles__ = ()
ZCatalog.resolve_url__roles__ = ()
