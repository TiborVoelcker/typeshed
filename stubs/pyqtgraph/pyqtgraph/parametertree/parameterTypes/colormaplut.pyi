from ..Parameter import Parameter
from .basetypes import WidgetParameterItem

class ColorMapLutParameterItem(WidgetParameterItem):
    hideWidget: bool
    def makeWidget(self): ...

class ColorMapLutParameter(Parameter):
    itemClass: type[ColorMapLutParameterItem]
