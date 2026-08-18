from typing import Any, Literal

from ..Parameter import Parameter
from .basetypes import WidgetParameterItem

class FontParameterItem(WidgetParameterItem):
    hideWidget: bool
    # Returns a QFontComboBox; its value is a QFont.
    def makeWidget(self): ...
    def updateDisplayLabel(self, value=None) -> None: ...

class FontParameter(Parameter):
    itemClass: type[FontParameterItem]
    def saveState(self, filter: Literal["user"] | None = None) -> dict[str, Any]: ...
