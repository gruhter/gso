from urllib import quote

from AccessControl import getSecurityManager
from AccessControl import Unauthorized
from Products.CMFCore.permissions import ManageUsers
from Products.CMFCore.utils import _checkPermission
try:
    from Products.CMFPlone.MembershipTool import MembershipTool as CMFPMT
    PATCH_CMFPLONE = True
except ImportError:
    PATCH_CMFPLONE = False
try:
    from Products.PlonePAS.tools.membership import MembershipTool as PPASMT
    PATCH_PLONEPAS = True
except ImportError:
    PATCH_PLONEPAS = False


def check_portrait_change_permission(tool, member_id):
    authenticated_id = getSecurityManager().getUser().getId()
    if not member_id:
        member_id = authenticated_id
    if member_id != authenticated_id and not _checkPermission(ManageUsers, tool):
        raise Unauthorized


if PATCH_CMFPLONE:  # Plone < 4.x
    _old_cmfp_deletePersonalPortrait = CMFPMT.deletePersonalPortrait


    def patched_deletePersonalPortrait(self, member_id=None):
        """
        deletes the Portrait of member_id
        """

        check_portrait_change_permission(self, member_id)
        return _old_cmfp_deletePersonalPortrait(self, member_id)


    CMFPMT.deletePersonalPortrait = patched_deletePersonalPortrait


    _old_cmfp_changeMemberPortrait = CMFPMT.changeMemberPortrait

    def patched_changeMemberPortrait(self, portrait, member_id=None):
        """
        given a portrait we will modify the users portrait
        we put this method here because we do not want
        .personal or portrait in the catalog
        """

        check_portrait_change_permission(self, member_id)
        return _old_cmfp_changeMemberPortrait(self, portrait, member_id)


    CMFPMT.changeMemberPortrait = patched_changeMemberPortrait


if PATCH_PLONEPAS:
    _old_ppas_deletePersonalPortrait = PPASMT.deletePersonalPortrait


    def patched_deletePersonalPortrait(self, id=None):
        """deletes the Portait of a member.

        Modified from CMFPlone version to URL-quote the member id.
        """

        check_portrait_change_permission(self, id)
        return _old_ppas_deletePersonalPortrait(self, id)


    PPASMT.deletePersonalPortrait = patched_deletePersonalPortrait


    _old_ppas_changeMemberPortrait = PPASMT.changeMemberPortrait

    def patched_changeMemberPortrait(self, portrait, id=None):
        """update the portait of a member.

        Modified from CMFPlone version to URL-quote the member id.
        """

        check_portrait_change_permission(self, id)
        return _old_ppas_changeMemberPortrait(self, portrait, id)


    PPASMT.changeMemberPortrait = patched_changeMemberPortrait
