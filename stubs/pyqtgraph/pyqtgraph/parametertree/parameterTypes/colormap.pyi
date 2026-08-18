from .basetypes import SimpleParameter, WidgetParameterItem

class ColorMapParameterItem(WidgetParameterItem):
    hideWidget: bool
    asSubItem: bool
    # Returns a `pyqtgraph.GradientWidget`; its value is a `pyqtgraph.ColorMap`.
    def makeWidget(self): ...

class ColorMapParameter(SimpleParameter):
    itemClass: type[ColorMapParameterItem]
