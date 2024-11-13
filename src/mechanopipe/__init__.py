"""A pipeline for mechanics."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("mechanopipe")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "Kevin Yamauchi"
__email__ = "kevin.yamauchi@gmail.com"
