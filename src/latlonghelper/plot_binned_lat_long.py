import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_binned_lat_long(binned_data, width=10, height=6):
    """
    Visualize binned geographic coordinates on a heatmap.

    This function takes the output of `lat_long_binning` and visualizes the
    spatial density of points using a heatmap, where each cell represents a
    latitude–longitude bin and the color intensity indicates the number of
    observations in that bin.

    Parameters
    ----------
    binned_data : iterable of str
        Binned geographic coordinates formatted as "<latitude>_<longitude>",
        for example "49.25_-123.25". Each element represents one observation.
    width : int, optional
        Width of the figure in inches (default is 10).
    height : int, optional
        Height of the figure in inches (default is 6).

    Returns
    -------
    matplotlib.axes.Axes
        The Matplotlib Axes object containing the heatmap.

    Examples
    --------
    >>> ax = plot_binned_lat_long(binned_data)
    >>> plt.show()
    """

    latitudes = []
    longitudes = []

    # Parse latitude and longitude values
    for item in binned_data:
        lat_str, lon_str = item.split("_")
        latitudes.append(float(lat_str))
        longitudes.append(float(lon_str))

    df = pd.DataFrame({"lat": latitudes, "lon": longitudes})

    # Create heatmap data
    heatmap_data = df.groupby(["lat", "lon"]).size().unstack(fill_value=0)

    # Sort latitude bins from north to south
    heatmap_data = heatmap_data.sort_index(ascending=False)

    plt.figure(figsize=(width, height))
    ax = sns.heatmap(
        heatmap_data,
        cmap="YlGnBu",
        cbar_kws={"label": "Frequency"},
    )

    plt.title("Geographic Bin Density Heatmap")
    plt.xlabel("Longitude Bins")
    plt.ylabel("Latitude Bins")

    return ax