import pytest
from latlonghelper.lat_long_distance import LatLongDistance

# -----------------------------
# Valid distance tests
# -----------------------------
@pytest.mark.parametrize(
    "lat1, lon1, lat2, lon2, expected",
    [
        (40.7128, -74.0060, 34.0522, -118.2437, 3935.75),  # NY → LA
        (51.5074, -0.1278, 48.8566, 2.3522, 343.56),       # London → Paris
        (0, 0, 0, 0, 0),                                   # Same point
        (0, 0, 0, 180, 20015.09),                          # Opposite sides of Earth
    ]
)
def test_latlongdistance_valid(lat1, lon1, lat2, lon2, expected):
    result = LatLongDistance(lat1, lon1, lat2, lon2)
    assert round(result, 2) == expected

# -----------------------------
# Out of range inputs
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
def test_latlongdistance_out_of_range(lat1, lon1, lat2, lon2):
    with pytest.raises(ValueError, match="must be between"):
        LatLongDistance(lat1, lon1, lat2, lon2)

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
def test_latlongdistance_type_errors(lat1, lon1, lat2, lon2):
    with pytest.raises(TypeError):
        LatLongDistance(lat1, lon1, lat2, lon2)
