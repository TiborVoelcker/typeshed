# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from _typeshed import Incomplete

from ...Qt import QtWidgets  # type: ignore[import-not-found]  # pyright: ignore[reportMissingImports]
from ..Parameter import Parameter
from ..ParameterItem import ParameterItem

class ParameterControlledButton(QtWidgets.QPushButton):
    settableAttributes: Incomplete
    def __init__(self, parameter=None, parent=None) -> None: ...
    def updateOpts(self, param, opts) -> None: ...
    def onNameChange(self, param, name) -> None: ...

class ActionParameterItem(ParameterItem):
    layoutWidget: Incomplete
    layout: Incomplete
    button: Incomplete
    def __init__(self, param, depth) -> None: ...
    def treeWidgetChanged(self) -> None: ...
    def titleChanged(self) -> None: ...

class ActionParameter(Parameter):
    itemClass: type[ActionParameterItem]
    sigActivated: Incomplete
    def activate(self) -> None: ...
