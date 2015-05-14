try:
    from AccessControl.class_init import InitializeClass
except ImportError:
    from Globals import InitializeClass
from AccessControl.Permissions import access_contents_information
try:
    from AccessControl.security import _getSecurity
except ImportError:
    from Products.Five.security import _getSecurity
from OFS.ObjectManager import ObjectManager


methods = (
    'hasObject',
    'tpValues',
    'superValues',
    'objectIds_d',
    'objectValues_d',
    'objectItems_d',
    'objectMap_d',
)
# can't use protectName since permissions won't be registered yet.
security = _getSecurity(ObjectManager)
security.declareProtected(access_contents_information, *methods)
InitializeClass(ObjectManager)
