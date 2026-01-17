import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def PlotBinnedLatLong(binned_data):
    """
    Visualizes binned geographic coordinates on a heatmap.

    Parameters
    ----------
    binned_data : String
        Output of LatLongBinning

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
    
    # 2. Create a DataFrame for easy plotting
    df = pd.DataFrame({'lat': latitudes, 'lon': longitudes})
    
    # 3. Pivot the data to create a density matrix
    # We count occurrences of each lat/long pair
    heatmap_data = df.groupby(['lat', 'lon']).size().unstack(fill_value=0)
    
    # Sort index so latitude increases upwards on the Y-axis
    heatmap_data = heatmap_data.sort_index(ascending=False)

    # 4. Plotting
    plt.figure(figsize=(10, 6))
    ax = sns.heatmap(heatmap_data, cmap="YlGnBu", cbar_kws={'label': 'Frequency'})
    
    plt.title("Geographic Bin Density Heatmap")
    plt.xlabel("Longitude Bins")
    plt.ylabel("Latitude Bins")
    
    return ax