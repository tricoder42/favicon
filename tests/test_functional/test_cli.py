# coding: utf-8
from __future__ import unicode_literals

import subprocess


def test_module_installed():
    """
    Check favicon module is installed properly and can be invoked via -m.
    """

    call_args = ['python', '-m', 'favicon', '-v']
    assert subprocess.call(call_args) == 0
