# -*- coding: utf-8 -*-
"""
    fabric_verbose
    ~~~~~~~~~~~~~~

    Fabric-Verbose

    :copyright: (c) 2014 by Suyeol Jeon.
    :license: MIT, see LICENSE for more details.
"""

__version_info__ = ('0', '1', '0')
__version__ = '.'.join(__version_info__)
__author__ = 'Suyeol Jeon'
__license__ = 'MIT'
__copyright__ = '(c) 2014 by Suyeol Jeon'
__all__ = ['verbose']

import sys

from fabric import api
from fabric.colors import blue, red


class verbose():
    def __init__(self, msg):
        self.msg = msg
        self.failed = False
        for func_name in ['local', 'run', 'sudo']:
            setattr(self, func_name, self._execute(func_name))

    def __enter__(self):
        sys.stdout.write(blue("* %s..." % self.msg))
        sys.stdout.flush()
        return self

    def __exit__(self, type, value, traceback):
        if not self.failed:
            print blue(" Done")

    def _execute(self, func_name):
        def __execute(*args, **kwargs):
            if func_name == 'local' and 'capture' not in kwargs:
                kwargs['capture'] = True
            rv = getattr(api, func_name)(*args, **kwargs)
            if rv.return_code:
                self.failed = True
                print red(" Failed")
                abort_msg = rv.stderr.strip() or rv.stdout.strip()
                api.abort(red(abort_msg))
        return __execute
