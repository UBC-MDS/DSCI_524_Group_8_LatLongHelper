import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def PlotBinnedLatLong(binned_data, width=10, height=6):
    """
    Visualizes binned geographic coordinates on a heatmap.
    
    This function takes the output of `LatLongBinning` and visualizes the spatial
    density of points using a heatmap, where each cell represents a latitude–
    longitude bin and the color intensity indicates the number of observations
    in that bin.
    
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
        Returns the plot object for display.

    Example
    -------
    >>> fig = PlotBinnedLatLong(binned_data)
    >>> plt.show()
    """
    
    latitudes = []
    longitudes = []
    
    for item in binned_data:
        lat_str, lon_str = item.split('_')
        latitudes.append(float(lat_str))
        longitudes.append(float(lon_str))
    
    df = pd.DataFrame({'lat': latitudes, 'lon': longitudes})
    
    heatmap_data = df.groupby(['lat', 'lon']).size().unstack(fill_value=0)
    
    heatmap_data = heatmap_data.sort_index(ascending=False)

    plt.figure(figsize=(width, height))
    ax = sns.heatmap(heatmap_data, cmap="YlGnBu", cbar_kws={'label': 'Frequency'})
    
    plt.title("Geographic Bin Density Heatmap")
    plt.xlabel("Longitude Bins")
    plt.ylabel("Latitude Bins")
    
    return ax
