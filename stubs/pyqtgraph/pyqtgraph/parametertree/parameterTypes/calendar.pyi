from typing import Any, Literal

from ..Parameter import Parameter
from .basetypes import WidgetParameterItem

class CalendarParameterItem(WidgetParameterItem):
    asSubItem: bool
    hideWidget: bool
    # Returns a QCalendarWidget.
    def makeWidget(self): ...

class CalendarParameter(Parameter):
    itemClass: type[CalendarParameterItem]
    # `**opts` adds "format" (default "TextDate") to the standard Parameter options; it is any value
    # accepted by `QDate.toString`/`fromString`, or the name of a `QtCore.Qt.DateFormat` member.
    def __init__(self, **opts) -> None: ...
    def saveState(self, filter: Literal["user"] | None = None) -> dict[str, Any]: ...
