# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from _typeshed import Incomplete
from collections.abc import Mapping
from typing import Any, ClassVar

from ...Qt import QtWidgets
from ..Parameter import Parameter
from ..ParameterItem import ParameterItem

class ParameterControlledButton(QtWidgets.QPushButton):
    settableAttributes: ClassVar[set[str]]
    def __init__(self, parameter: Parameter | None = None, parent=None) -> None: ...
    def updateOpts(self, param: Parameter, opts: Mapping[str, Any]) -> None: ...
    def onNameChange(self, param: Parameter, name: str) -> None: ...

class ActionParameterItem(ParameterItem):
    layoutWidget: Incomplete
    layout: Incomplete
    button: ParameterControlledButton
    def __init__(self, param: Parameter, depth: int) -> None: ...
    def treeWidgetChanged(self) -> None: ...
    def titleChanged(self) -> None: ...

class ActionParameter(Parameter):
    itemClass: type[ActionParameterItem]
    sigActivated: Incomplete
    def activate(self) -> None: ...
