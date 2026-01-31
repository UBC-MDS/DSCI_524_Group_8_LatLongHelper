"""
Unit tests for the `lat_long_binning` function.

These tests verify that latitude–longitude binning behaves correctly for:
- valid numeric inputs,
- boundary conditions,
- invalid coordinate ranges,
- invalid grid sizes, and
- incorrect input types.

The tests ensure that the function both returns the expected bin identifiers
and raises appropriate exceptions when inputs are invalid.
"""

import pytest
from latlonghelper.lat_long_binning import lat_long_binning


@pytest.mark.parametrize(
    "latitude, longitude, grid_lat, grid_lon, expected",
    [
        (49.2593, -123.2475, 0.01, 0.01, "49.25_-123.25"),      # matches doc example
        (-49.2593, 123.2475, 0.01, 0.01, "-49.26_123.24"),      # negative latitude floors down
        (90.0, 180.0, 0.5, 0.5, "90.0_180.0"),                  # inclusive upper boundary
        (-90.0, -180.0, 1.0, 1.0, "-90.0_-180.0"),              # inclusive lower boundary
    ]
)
def test_latlongbinning_valid(latitude, longitude, grid_lat, grid_lon, expected):
    """
    Test that valid latitude and longitude values are correctly binned.

    This test covers:
    - standard positive coordinates,
    - negative coordinates,
    - boundary values, and
    - different grid sizes.
    """
    assert lat_long_binning(latitude, longitude, grid_lat, grid_lon) == expected


@pytest.mark.parametrize(
    "latitude, longitude",
    [
        (90.00001, 0),
        (-90.00001, 0),
        (0, 180.00001),
        (0, -180.00001),
    ]
)
def test_latlongbinning_out_of_range(latitude, longitude):
    """
    Test that latitude or longitude values outside the valid range
    raise a ValueError.
    """
    with pytest.raises(ValueError, match="between"):
        lat_long_binning(latitude, longitude)


@pytest.mark.parametrize(
    "grid_lat, grid_lon",
    [(0, 0.01), (0.01, 0), (-0.5, 0.5), (0.5, -0.5)]
)
def test_latlongbinning_bad_grid(grid_lat, grid_lon):
    """
    Test that non-positive grid sizes raise a ValueError.
    """
    with pytest.raises(ValueError, match="grid sizes must be > 0"):
        lat_long_binning(0, 0, grid_lat, grid_lon)


def test_latlongbinning_type_errors():
    """
    Test that non-numeric latitude or longitude inputs raise a TypeError.
    """
    with pytest.raises(TypeError, match="must be numeric"):
        lat_long_binning("49", -123.0)  # type: ignore
        
@pytest.mark.parametrize(
    "latitude, longitude, grid_lat, grid_lon",
    [
        (49.0, "not_a_number", 0.01, 0.01),   # longitude type error
        (49.0, -123.0, "0.01", 0.01),         # grid_size_latitude type error
        (49.0, -123.0, 0.01, "0.01"),         # grid_size_longitude type error
    ]
)
def test_lat_long_binning_more_type_errors(latitude, longitude, grid_lat, grid_lon):
    with pytest.raises(TypeError, match="must be numeric"):
        lat_long_binning(latitude, longitude, grid_lat, grid_lon)
