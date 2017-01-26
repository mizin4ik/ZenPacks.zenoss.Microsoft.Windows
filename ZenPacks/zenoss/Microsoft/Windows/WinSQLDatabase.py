##############################################################################
#
# Copyright (C) Zenoss, Inc. 2016, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################
from . import schema


class WinSQLDatabase(schema.WinSQLDatabase):
    '''
    Base class for WinSQLDatabase classes.

    This file exists to avoid ZenPack upgrade issues
    '''

    def getState(self):
        """Return database state if instance state is OK"""
        status = None
        instance = getattr(self, 'winsqlinstance', None)
        if instance:
            if instance().getStatus():
                return "Down"
        try:
            status = int(self.cacheRRDValue('status', None))
        except Exception:
            return 'Unknown'
        return 'Up' if status  else 'Down'
