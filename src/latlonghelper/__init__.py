# read version from installed package
from importlib.metadata import version
__version__ = version("latlonghelper")

from .__about__ import __version__

# Import public functions/classes for API reference
from .lat_long_distance import LatLongDistance
from .lat_long_binning import LatLongBinning
from .plot_binned_lat_long import PlotBinnedLatLong

# Optional: define __all__ to list public API
__all__ = [
    "LatLongDistance",
    "LatLongBinning",
    "PlotBinnedLatLong",
]
