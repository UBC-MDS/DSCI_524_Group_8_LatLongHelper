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