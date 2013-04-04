from __future__ import absolute_import, unicode_literals


class MissingRole(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class MissingPrivilege(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class MissingResource(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
