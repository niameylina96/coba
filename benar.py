import os
import tempfile
import time

from branca.colormap import StepColormap
from branca.element import CssLink, Element, Figure, JavascriptLink, MacroElement
from branca.utilities import _parse_size, color_brewer

from folium.features import GeoJson, TopoJson
from folium.map import FitBounds
from folium.raster_layers import TileLayer
from folium.utilities import _validate_location

from jinja2 import Environment, PackageLoader, Template


ENV = Environment(loader=PackageLoader('folium', 'templates'))
map_1 = folium.Map(location=[107.619125, -6.917464])
map_1.simple_marker([107.668710, -6.972280], popup='SMAN 15')
map_1.simple_marker([107.668663, -6.972270], popup='SMAN 16')
map_1.simple_marker([107.668610, -6.972270], popup='SMA 16')
map_1.simple_marker([107.574970, -6.943540], popup='SMA 16')
map_1.create_map(path='output.html')

