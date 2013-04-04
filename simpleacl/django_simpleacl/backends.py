# -*- mode: python; coding: utf-8; -*-
from __future__ import absolute_import, unicode_literals
from ..exceptions import MissingRole, MissingPrivilege, MissingContext
from .utils import get_acl, get_role, get_privilege, get_context


class PermissionBackend(object):
    """Per object level permission backend."""
    supports_object_permissions = True
    supports_anonymous_user = True
    supports_inactive_user = True

    def authenticate(self, username, password):
        return None

    def has_perm(self, user, perm, obj=None):
        """This method checks if the user_obj has perm on obj.

        Returns True or False
        """
        acl = get_acl()
        role = acl.add_role(get_role(user))
        privilege = acl.add_privilege(get_privilege(perm))
        context = acl.add_context(get_context(obj))
        try:
            return acl.is_allowed(role, privilege, context)
        except (MissingRole, MissingPrivilege, MissingContext):
            raise
            return False