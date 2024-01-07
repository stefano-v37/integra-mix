from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("integra_mix")
except PackageNotFoundError:
    pass