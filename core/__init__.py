from pkg_resources import DistributionNotFound, get_distribution, resource_filename

try:
    __version__ = get_distribution("hypercube-core").version
except DistributionNotFound:
    __version__ = "unknown"

PYINSTALLER_SPEC_PATH = resource_filename("hypercube", "pyinstaller.spec")
