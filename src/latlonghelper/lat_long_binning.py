import math

def LatLongBinning(latitude: float, longitude: float, grid_size_latitude: float = 0.01, grid_size_longitude: float = 0.01):
    """
    A function that is used to bin latitude and longitude into different groups

    Parameters
    ----------
    latitude : float
        Latitude in degrees (-90 to 90)
    longitude : float
        Longitude in degrees (-180 to 180)
    grid_size_latitude (optional) : float
        Grid size of latitude in degrees 
    grid_size_longitude (optional) : float
        Grid size of longitude in degrees 

    Returns
    -------
    str
        Identifier of the binned latitude–longitude grid cell

    Example
    -------
    >>> LatLongBinning(49.2593, -123.2475)
    '49.25_-123.25'    
    """
    # Type checks (optional but good defensive practice)
    if not isinstance(latitude, (int, float)) or not isinstance(longitude, (int, float)):
        raise TypeError("latitude and longitude must be numeric")
    if not isinstance(grid_size_latitude, (int, float)) or not isinstance(grid_size_longitude, (int, float)):
        raise TypeError("grid_size_latitude and grid_size_longitude must be numeric")

    # Range checks
    if not (-90 <= latitude <= 90):
        raise ValueError("latitude must be between -90 and 90 degrees inclusive")
    if not (-180 <= longitude <= 180):
        raise ValueError("longitude must be between -180 and 180 degrees inclusive")

    # Grid checks
    if grid_size_latitude <= 0 or grid_size_longitude <= 0:
        raise ValueError("grid sizes must be > 0")

    # Bin to lower boundary
    lat_binned = math.floor(latitude / grid_size_latitude) * grid_size_latitude
    lon_binned = math.floor(longitude / grid_size_longitude) * grid_size_longitude

    # Decide formatting precision (basic approach)
    lat_decimals = max(0, len(str(grid_size_latitude).split(".")[1]) if "." in str(grid_size_latitude) else 0)
    lon_decimals = max(0, len(str(grid_size_longitude).split(".")[1]) if "." in str(grid_size_longitude) else 0)

    return f"{lat_binned:.{lat_decimals}f}_{lon_binned:.{lon_decimals}f}"