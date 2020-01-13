"""Bokeh Visualization Template

This template is a general outline for turning your data into a
visualization using Bokeh.
"""
# Data handling
import pandas as pd
import numpy as np

# Bokeh libraries
from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel

# Prepare the data

# Determine where the visualization will be rendered
output_file('map_test.html',
            title = "Map Test")  # Render to static HTML, or
output_notebook()  # Render inline in a Jupyter Notebook

# Set up the figure(s)
fig = figure(title='My Coordinates',
             plot_height=600, plot_width=600,
             x_range=(0, 60), y_range=(0, 8),
             toolbar_location=None)  # Instantiate a figure() object

# Draw the coordinates as circles
        # fig.circle(x=x, y=y,
        #            color='green', size=10, alpha=0.5)


# Connect to and draw the data

# Organize the layout

# Preview and save
show(fig)  # See what I made, and save if I like it
