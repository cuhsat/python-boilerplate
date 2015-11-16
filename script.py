#!/usr/bin/env python
"""
License (SHORTCUT)

License description.

Year Author <author@domain.org>
"""
import os
import re
import sys


__all__, __version__ = ["Foo"], "0.0.0"


class Foo(object):
    """
    Foo class.
    """
    def bar(self):
        """
        Bar method.
        """
        return "Done"


def main(script, arg=None, *args):
    """
    Usage: %s ARG [ARGS...]

    Options:
      -h, --help      Shows the usage
      -l, --license   Shows the license
      -v, --version   Shows the version

    Report bugs to <author@domain.org>
    """
    try:
        script = os.path.basename(script)

        if arg in ("/?", "-h", "--help"):
            print(re.sub("(?m)^ {4}", "", main.__doc__ % script).strip())

        elif arg in ("-l", "--license"):
            print(__doc__.strip())

        elif arg in ("-v", "--version"):
            print(__version__)

        elif arg:
            print("Unknown option or parameter not given.")
            print("Please use --help for help on options.")
            return 2 # Incorrect usage

        else:
            print(Foo().bar())

    except Exception as ex:
        return "%s error: %s" % (script, ex)


if __name__ == "__main__":
    sys.exit(main(*sys.argv))
