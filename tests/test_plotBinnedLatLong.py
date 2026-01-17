# Unit tests and data creation aided by Gemini 3 
import unittest
import matplotlib.pyplot as plt
from latlonghelper.plot_binned_lat_long import PlotBinnedLatLong

class TestPlotBinnedLatLong(unittest.TestCase):

    def test_return_type(self):
        """Check if the function returns a Matplotlib Axes object."""
        data = ["49.25_-123.25", "49.26_-123.26"]
        ax = PlotBinnedLatLong(data)
        self.assertIsInstance(ax, plt.Axes)
        plt.close()

    def test_single_coordinate(self):
        """Ensure it handles a list with only one coordinate."""
        data = ["45.00_-120.00"]
        try:
            PlotBinnedLatLong(data)
        except Exception as e:
            self.fail(f"PlotBinnedLatLong failed on single coordinate: {e}")
        plt.close()

    def test_parsing_logic(self):
        """Check if it correctly parses the underscore-separated strings."""
        data = ["10.00_20.00"]
        ax = PlotBinnedLatLong(data)
        
        labels = [float(t.get_text()) for t in ax.get_yticklabels() if t.get_text()]
        
        self.assertIn(10.0, labels)
        plt.close()

    def test_empty_input(self):
        """Ensure the function handles or raises an error for empty lists."""
        with self.assertRaises(Exception):
            PlotBinnedLatLong([])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)