from typing import Any, Literal

from .basetypes import SimpleParameter, WidgetParameterItem

class ColorParameterItem(WidgetParameterItem):
    hideWidget: bool
    # Returns a `pyqtgraph.ColorButton`.
    def makeWidget(self): ...

class ColorParameter(SimpleParameter):
    itemClass: type[ColorParameterItem]
    # Returns a QColor, or None when no value is set.
    def value(self): ...
    def saveState(self, filter: Literal["user"] | None = None) -> dict[str, Any]: ...
