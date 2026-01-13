import pytest
from src.latlonghelper.latlongbinning import latlongbinning

@pytest.mark.parametrize(
    "latitude, longitude, grid_lat, grid_lon, expected",
    [
        (49.2593, -123.2475, 0.01, 0.01, "49.25_-123.25"),     # matches doc example
        (-49.2593, 123.2475, 0.01, 0.01, "-49.26_123.24"),     # negative lat floors “down”
        (90.0, 180.0, 0.5, 0.5, "90.0_180.0"),                 # inclusive boundary
        (-90.0, -180.0, 1.0, 1.0, "-90_-180"),                 # exact boundary with int grid
    ]
)
def test_latlongbinning_valid(latitude, longitude, grid_lat, grid_lon, expected):
    assert latlongbinning(latitude, longitude, grid_lat, grid_lon) == expected


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
    with pytest.raises(ValueError, match="between"):
        latlongbinning(latitude, longitude)


@pytest.mark.parametrize("grid_lat, grid_lon", [(0, 0.01), (0.01, 0), (-0.5, 0.5), (0.5, -0.5)])
def test_latlongbinning_bad_grid(grid_lat, grid_lon):
    with pytest.raises(ValueError, match="grid sizes must be > 0"):
        latlongbinning(0, 0, grid_lat, grid_lon)


def test_latlongbinning_type_errors():
    with pytest.raises(TypeError, match="must be numeric"):
        latlongbinning("49", -123.0)  # type: ignore