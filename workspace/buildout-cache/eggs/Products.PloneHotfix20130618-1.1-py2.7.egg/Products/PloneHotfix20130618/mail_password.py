from AccessControl import getSecurityManager
from AccessControl.SecurityManagement import newSecurityManager
from AccessControl.SecurityManagement import setSecurityManager
from Products.CMFCore.utils import getToolByName
try:
    from Products.CMFPlone.RegistrationTool import _
except ImportError:
    # < Plone 4.1
    _ = str
try:
    from Products.CMFPlone.RegistrationTool import get_member_by_login_name
except ImportError:
    # < Plone 4.1
    def get_member_by_login_name(tool, login, raise_exceptions=False):
        membership = getToolByName(tool, 'portal_membership')
        member = membership.getMemberById(login)
        return member
from Products.CMFPlone.RegistrationTool import RegistrationTool
try:
    from Products.PluggableAuthService.permissions import SetOwnPassword
except ImportError:
    SetOwnPassword = 'Set own password'


RegistrationTool._original_mailPassword = RegistrationTool.mailPassword

exc_class = ValueError
try:
    from Products.CMFPlone.migrations import v2_5
except ImportError:
    try:
        from Products.CMFPlone.factory import _IMREALLYPLONE4
    except ImportError:
        from AccessControl import Unauthorized as exc_class


def mailPassword(self, login, REQUEST):
    request = REQUEST or self.REQUEST
    portal = getToolByName(self, 'portal_url').getPortalObject()
    member = get_member_by_login_name(self, login, raise_exceptions=False)

    # member.getUser gives us the wrong context for setting up a
    # SecurityManager.
    acl_users = getToolByName(portal, 'acl_users')
    user = acl_users.getUserById(member.getId())

    orig_sm = getSecurityManager()
    try:
        newSecurityManager(request, user)
        tmp_sm = getSecurityManager()
        if not tmp_sm.checkPermission(SetOwnPassword, portal):

            # Re-use this ready-translated message for now
            exc = exc_class(
                    _(u"Mailing forgotten passwords has been disabled."))

            # Work around bug in mail_password under Py>2.6
            if hasattr(exc, 'message'):
                exc.message = exc.message
            raise exc
    finally:
        setSecurityManager(orig_sm)
    return self._original_mailPassword(login, REQUEST)


RegistrationTool.mailPassword = mailPassword
