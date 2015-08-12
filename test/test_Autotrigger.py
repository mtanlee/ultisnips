from test.vim_test_case import VimTestCase as _VimTest
from test.constant import *

import subprocess


def has_patch(version, executable):
    output = subprocess.check_output([executable, "--version"])
    for line in output.split("\n"):
        if line.startswith("Included patches:"):
            patch = line.split('-')[1]

    return int(patch) >= version


def check_required_vim_version(test):
    if not has_patch(214, test.vim._vim_executable):
        return 'Vim newer than 7.4.214 is required'
    else:
        return None


class Autotrigger_CanMatchSimpleTrigger(_VimTest):
    skip_if = check_required_vim_version
    files = { 'us/all.snippets': r"""
        snippet a "desc" A
        autotriggered
        endsnippet
        """}
    keys = 'a'
    wanted = 'autotriggered'


class Autotrigger_CanMatchContext(_VimTest):
    skip_if = check_required_vim_version
    files = { 'us/all.snippets': r"""
        snippet a "desc" "snip.line == 2" Ae
        autotriggered
        endsnippet
        """}
    keys = 'a\na'
    wanted = 'autotriggered\na'


class Autotrigger_CanExpandOnTriggerWithLengthMoreThanOne(_VimTest):
    skip_if = check_required_vim_version
    files = { 'us/all.snippets': r"""
        snippet abc "desc" A
        autotriggered
        endsnippet
        """}
    keys = 'abc'
    wanted = 'autotriggered'
