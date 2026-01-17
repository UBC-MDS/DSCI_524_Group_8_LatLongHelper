import math

def LatLongDistance(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    """
    A function that calculates the distance between two geographic points given their latitude 
    and longitude coordinates.

    Addendum:
    The use of the Haversine formula for distance calculation was suggested by ChatGPT. 
    The Haversine formula was chosen because it accounts for the curvature of the Earth, 
    providing an accurate “great-circle” distance between two points given their latitude 
    and longitude, rather than assuming a flat surface.

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
    
    Example
    -------
    >>> LatLongDistance(40.7128, -74.0060, 34.0522, -118.2437)
    3935.75
    """
    
    # Input validation
    if not (-90 <= latitude_1 <= 90):
        raise ValueError("latitude_1 must be between -90 and 90 degrees")
    if not (-90 <= latitude_2 <= 90):
        raise ValueError("latitude_2 must be between -90 and 90 degrees")
    if not (-180 <= longitude_1 <= 180):
        raise ValueError("longitude_1 must be between -180 and 180 degrees")
    if not (-180 <= longitude_2 <= 180):
        raise ValueError("longitude_2 must be between -180 and 180 degrees")

    # Convert degrees to radians
    lat1_rad = math.radians(latitude_1)
    lon1_rad = math.radians(longitude_1)
    lat2_rad = math.radians(latitude_2)
    lon2_rad = math.radians(longitude_2)

    # Haversine formula
    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    a = math.sin(delta_lat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Earth radius in kilometers
    earth_radius_km = 6371.0
    distance = earth_radius_km * c

    return round(distance, 2)