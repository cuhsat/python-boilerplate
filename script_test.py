#!/usr/bin/env python
"""
License (SHORTCUT)

License description.

Year Author <author@domain.org>
"""
import sys


from script import Foo


try:
    import pytest
except ImportError:
    sys.exit("Requires pytest (https://pytest.org)")


class TestFoo:
    """
    Foo unit tests.
    """
    def test_bar(self):
        """
        Bar test.
        """
        assert Foo().bar() == "Done"


def main(*args):
    """
    Starts unit testing and passes all arguments to py.test.
    """
    return pytest.main(list(args))


if __name__ == "__main__":
    sys.exit(main(*sys.argv))
