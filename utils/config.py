"""SITE CUSTOMIZATION.
PLEASE NOTE ANY CHANGE IN THIS FILE WILL MOSTLY AFFECT THE ENTIRE APPLICATION."""

"""This is the default port. You are free to change this."""
Ondiek_port=5050

"""Change this to the name of the application you are building. For example your name"""
Ondiek_name='Ondiek'

"""Dash graph properties"""
Ondiek_graph_config = {'displayModeBar': False, 'scrollZoom': False, 'staticPlot': False}

"""The color palettes to be applied to the graphs. The one below is a green color pellete. Change this
to whatever color palette you may wish"""
Ondiek_color_palette = ['#98FB98', '#7FFF00', '#00FF00', '#32CD32', '#00FF7F', '#3CB371', '#2E8B57', '#228B22', '#008000', '#006400']

"""The graphs  background colors as defined by plotly. This is a list hence will be referenced as a list"""

Ondiek_graph_background_color = ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]

"""Pick the background color to be used. this has to be in the range 0 - 6. Default is 5 for SIMPLE_WHITE"""
Ondiek_bg_color = Ondiek_graph_background_color[5]

"""This is the URL to redirect when the site name is clicked. If you are a creator you can redirect to your
social media page or else replace with '#' to redirect to home page"""
Ondiek_creator_url='https://www.linkedin.com/in/gaylord-odhiambo-992990150/'
