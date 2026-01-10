# latlonghelper

A package for cleaning and utilizing geospatial data. Allows the use of geospatial data to help create summarizations such as distance or create rudimentary plots via the binning functionality included in the package.

Functions included:
- `LatLongDistance`: calculates the distance (in kilometres) between two geographic points given their latitude and longitude coordinates.
- `LatLongBinning`: bins latitude and longitude into different groups to aid in grouping or for use in `PlotBinnedLatLong`.
- `PlotBinnedLatLong`: Visualizes binned geographic coordinates on a heatmap.

`LatLongDistance` is a common function found in many packages such as [GeoPy](https://geopy.readthedocs.io/en/stable/) and [Haversine](https://pypi.org/project/haversine/). However, binning and plotting such binned latitudes and longitudes does not currently exist. Current methods to bin require the use of multiple `Pandas` functions to do so. We aim to create a simplification of the binning and their plot without the user's having to rely on multiple uses and transformation on their part.

## Installation

```bash
$ pip install latlonghelper
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

It is licensed under the terms of the MIT license.

## Contributors

`latlonghelper` was created by Paul Raadnui, Ashifa Hassam and Amar Gill.

## Credits

`latlonghelper` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
