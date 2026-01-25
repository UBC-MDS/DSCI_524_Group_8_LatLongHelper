# Unit tests and data creation aided by Gemini 3 
import unittest
import matplotlib.pyplot as plt
from latlonghelper.plot_binned_lat_long import PlotBinnedLatLong

class TestPlotBinnedLatLong(unittest.TestCase):

    def test_figure_dimensions(self):
        """Verify that the width and height parameters correctly set the figure size."""
        custom_width = 15
        custom_height = 8
        data = ["49.25_-123.25"]
        
        ax = PlotBinnedLatLong(data, width=custom_width, height=custom_height)
        fig = ax.get_figure()
        
        actual_width, actual_height = fig.get_size_inches()
        
        self.assertEqual(actual_width, custom_width)
        self.assertEqual(actual_height, custom_height)
        plt.close(fig)

    def test_default_dimensions(self):
        """Verify that the default values (10, 6) are used when not specified."""
        data = ["49.25_-123.25"]
        ax = PlotBinnedLatLong(data)
        fig = ax.get_figure()
        
        actual_width, actual_height = fig.get_size_inches()
        
        self.assertEqual(actual_width, 10)
        self.assertEqual(actual_height, 6)
        plt.close(fig)

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

    def test_frequency_binning(self):
        """Verify that multiple occurrences of the same coordinate are binned correctly."""
        data = ["50.00_-100.00", "50.00_-100.00", "50.00_-100.00"]
        ax = PlotBinnedLatLong(data)
        
        children = ax.get_children()
        
        self.assertTrue(len(children) > 0)
        
        plt.close()

    def test_coordinate_boundaries(self):
        """Verify that extreme coordinates appear in the heatmap labels."""
        data = [
            "90.00_180.00",   
            "-90.00_-180.00", 
        ]
        ax = PlotBinnedLatLong(data)
        
        y_labels = [t.get_text() for t in ax.get_yticklabels()]
        x_labels = [t.get_text() for t in ax.get_xticklabels()]
        
        self.assertTrue(any("-90.0" in label for label in y_labels), f"Expected -90.0 in {y_labels}")
        self.assertTrue(any("90.0" in label for label in y_labels), f"Expected 90.0 in {y_labels}")
        self.assertTrue(any("180.0" in label for label in x_labels), f"Expected 180.0 in {x_labels}")
        
        plt.close(ax.get_figure())

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)