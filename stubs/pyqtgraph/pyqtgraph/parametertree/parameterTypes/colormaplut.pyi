from ..Parameter import Parameter
from .basetypes import WidgetParameterItem

class ColorMapLutParameterItem(WidgetParameterItem):
    hideWidget: bool
    # Returns a `pyqtgraph.ColorMapButton`; its value is a `pyqtgraph.ColorMap`.
    def makeWidget(self): ...

class ColorMapLutParameter(Parameter):
    itemClass: type[ColorMapLutParameterItem]
