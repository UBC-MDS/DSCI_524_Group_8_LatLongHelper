def LatLongDistance(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float):
    """
    A function that calculates the distance between two geographic points given their latitude and longitude coordinates.

    Parameters
    ----------
    latitude_1 : float
        Latitude of the first point in degrees (-90 to 90)
    longitude_1 : float
        Longitude of the first point in degrees (-180 to 180)
    latitude_2 : float
        Latitude of the second point in degrees (-90 to 90)
    longitude_2 : float
        Longitude of the second point in degrees (-180 to 180)

    Returns
    -------
    distance : float
        Distance between the two points (in kilometers)
    """
