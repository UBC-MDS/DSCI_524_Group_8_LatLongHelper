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