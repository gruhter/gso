from plone.app.portlets.storage import PortletAssignmentMapping, BaseMapping

def __getitem__(self, key):
    return BaseMapping.__getitem__(self, key).__of__(self)

PortletAssignmentMapping.__getitem__ = __getitem__
