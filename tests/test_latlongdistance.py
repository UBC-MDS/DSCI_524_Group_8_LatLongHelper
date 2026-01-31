"""
Unit tests for the `lat_long_distance` function.

These tests verify:
- correct distance calculations for known geographic locations,
- handling of edge cases such as identical points and antipodal points,
- appropriate errors for out-of-range inputs,
- type checking for invalid input types, and
- mathematical properties such as symmetry.

The distance calculations are based on the Haversine formula.
"""

import pytest
from latlonghelper.lat_long_distance import lat_long_distance


# -----------------------------
# Valid distance tests
# -----------------------------
@pytest.mark.parametrize(
    "lat1, lon1, lat2, lon2, expected",
    [
        (40.7128, -74.0060, 34.0522, -118.2437, 3935.75),  # New York → Los Angeles
        (51.5074, -0.1278, 48.8566, 2.3522, 343.56),       # London → Paris
        (0, 0, 0, 0, 0),                                   # Same point
        (0, 0, 0, 180, 20015.09),                          # Antipodal points
    ]
)
def test_lat_long_distance_valid(lat1, lon1, lat2, lon2, expected):
    """
    Test that valid latitude–longitude pairs return correct distances.
    """
    result = lat_long_distance(lat1, lon1, lat2, lon2)
    assert round(result, 2) == expected


# -----------------------------
# Out-of-range inputs
# -----------------------------
@pytest.mark.parametrize(
    "lat1, lon1, lat2, lon2",
    [
        (-91, 0, 0, 0),
        (91, 0, 0, 0),
        (0, -181, 0, 0),
        (0, 0, 0, 181),
    ]
)
def test_lat_long_distance_out_of_range(lat1, lon1, lat2, lon2):
    """
    Test that latitude or longitude values outside valid ranges raise ValueError.
    """
    with pytest.raises(ValueError, match="must be between"):
        lat_long_distance(lat1, lon1, lat2, lon2)

@pytest.mark.parametrize(
    "lat1, lon1, lat2, lon2",
    [
        (0, 0, -91, 0),   # latitude_2 too low
        (0, 0, 91, 0),    # latitude_2 too high
    ]
)
def test_lat_long_distance_lat2_out_of_range(lat1, lon1, lat2, lon2):
    with pytest.raises(ValueError, match="must be between"):
        lat_long_distance(lat1, lon1, lat2, lon2)

# -----------------------------
# Type errors
# -----------------------------
@pytest.mark.parametrize(
    "lat1, lon1, lat2, lon2",
    [
        ("40.7128", -74.0060, 34.0522, -118.2437),
        (40.7128, None, 34.0522, -118.2437),
    ]
)
def test_lat_long_distance_type_errors(lat1, lon1, lat2, lon2):
    """
    Test that non-numeric inputs raise a TypeError.
    """
    with pytest.raises(TypeError):
        lat_long_distance(lat1, lon1, lat2, lon2)


# -----------------------------
# Mathematical properties
# -----------------------------
def test_lat_long_distance_is_symmetric():
    """
    Test that distance calculation is symmetric:
    distance(A, B) == distance(B, A).
    """
    lat1, lon1 = 40.7128, -74.0060
    lat2, lon2 = 34.0522, -118.2437

    d1 = lat_long_distance(lat1, lon1, lat2, lon2)
    d2 = lat_long_distance(lat2, lon2, lat1, lon1)

    assert round(d1, 6) == round(d2, 6)


# -----------------------------
# Extreme valid inputs
# -----------------------------
def test_lat_long_distance_north_to_south_pole():
    """
    Test distance between the North Pole and South Pole.
    """
    result = lat_long_distance(90, 0, -90, 0)
    assert round(result, 2) == 20015.09
