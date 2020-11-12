from collections import namedtuple

from ._version import ___version___ as version


class Package(namedtuple("Package", ["version"])):
    pass


if __name__ == "__main__":
    print(Package(version))



