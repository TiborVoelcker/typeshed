from collections import OrderedDict
from collections.abc import Mapping, Sequence
from typing import Any
from typing_extensions import TypeAlias

from ..Parameter import Parameter
from .basetypes import WidgetParameterItem

# `limits` is either a sequence of values (stringified for display) or a {label: value} mapping.
_Limits: TypeAlias = Sequence[Any] | Mapping[str, Any]

class ListParameterItem(WidgetParameterItem):
    targetValue: Any
    forward: OrderedDict[str, Any]
    reverse: tuple[list[Any], list[str]]
    def __init__(self, param: Parameter, depth: int) -> None: ...
    widget: Any
    # Returns a QComboBox.
    def makeWidget(self): ...
    def value(self): ...
    def setValue(self, val) -> None: ...
    def limitsChanged(self, param: Parameter, limits: _Limits) -> None: ...
    def updateDisplayLabel(self, value=None) -> None: ...

class ListParameter(Parameter):
    itemClass: type[ListParameterItem]
    forward: OrderedDict[str, Any]
    reverse: tuple[list[Any], list[str]]
    # `**opts` adds "limits" to the standard Parameter options.
    def __init__(self, **opts) -> None: ...
    def setLimits(self, limits: _Limits) -> None: ...
    @staticmethod
    def mapping(limits: _Limits) -> tuple[OrderedDict[str, Any], tuple[list[Any], list[str]]]: ...
