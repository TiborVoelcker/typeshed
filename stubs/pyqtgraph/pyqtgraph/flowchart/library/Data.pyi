# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from _typeshed import Incomplete
from collections.abc import Callable, Mapping
from typing import Any, ClassVar

from numpy.typing import NDArray

from ...graphicsItems.LinearRegionItem import LinearRegionItem
from ...metaarray import MetaArray
from ...Qt import QtWidgets
from ...widgets.TreeWidget import TreeWidget
from ..Node import Node
from ..Terminal import Terminal
from .common import CtrlNode

class ColumnSelectNode(Node):
    nodeName: ClassVar[str]
    columns: set[str]
    columnList: Incomplete  # QListWidget
    # An index for a record array, or a MetaArray axis index or name.
    axis: int | str
    def __init__(self, name: str) -> None: ...
    # Returns one entry per selected column.
    def process(self, In: NDArray[Any] | MetaArray, display: bool = True) -> dict[str, Any]: ...  # type: ignore[override]
    def ctrlWidget(self): ...
    def updateList(self, data: NDArray[Any] | MetaArray) -> None: ...
    def itemChanged(self, item) -> None: ...  # `item` is a QListWidgetItem
    def saveState(self) -> dict[str, Any]: ...
    def restoreState(self, state: Mapping[str, Any]) -> None: ...

class RegionSelectNode(CtrlNode):
    nodeName: ClassVar[str]
    uiTemplate: Incomplete
    items: dict[Terminal, LinearRegionItem]
    def __init__(self, name: str) -> None: ...
    def displayToggled(self, b: bool) -> None: ...
    def movableToggled(self, b: bool) -> None: ...
    # Keys: "selected", "widget" and "region".
    def process(self, data=None, display: bool = True) -> dict[str, Any]: ...  # type: ignore[override]
    def rgnChanged(self, item: LinearRegionItem) -> None: ...

class TextEdit(QtWidgets.QTextEdit):
    on_update: Callable[[], object]
    lastText: str | None
    def __init__(self, on_update: Callable[[], object]) -> None: ...
    def focusOutEvent(self, ev) -> None: ...

class EvalNode(Node):
    nodeName: ClassVar[str]
    ui: Incomplete  # QWidget
    layout: Incomplete  # QGridLayout
    text: TextEdit
    def __init__(self, name: str) -> None: ...
    def ctrlWidget(self): ...
    def setCode(self, code: str) -> None: ...
    def code(self) -> str: ...
    # Whatever the user's expression or script evaluates to; normally a
    # {output terminal name: value} dict.
    def process(self, display: bool = True, **args) -> Any: ...
    def saveState(self) -> dict[str, Any]: ...
    def restoreState(self, state: Mapping[str, Any]) -> None: ...

class ColumnJoinNode(Node):
    nodeName: ClassVar[str]
    ui: Incomplete  # QWidget
    layout: Incomplete  # QGridLayout
    tree: TreeWidget
    addInBtn: Incomplete  # QPushButton
    remInBtn: Incomplete  # QPushButton
    def __init__(self, name: str) -> None: ...
    def ctrlWidget(self): ...
    def addInput(self) -> None: ...  # type: ignore[override]
    def remInput(self) -> None: ...
    def process(self, display: bool = True, **args) -> dict[str, Any]: ...
    def order(self) -> list[str]: ...
    def saveState(self) -> dict[str, Any]: ...
    def restoreState(self, state: Mapping[str, Any]) -> None: ...
    def terminalRenamed(self, term: Terminal, oldName: str) -> None: ...

class Mean(CtrlNode):
    nodeName: ClassVar[str]
    uiTemplate: Incomplete
    def processData(self, data: NDArray[Any] | MetaArray): ...

class Max(CtrlNode):
    nodeName: ClassVar[str]
    uiTemplate: Incomplete
    def processData(self, data: NDArray[Any] | MetaArray): ...

class Min(CtrlNode):
    nodeName: ClassVar[str]
    uiTemplate: Incomplete
    def processData(self, data: NDArray[Any] | MetaArray): ...

class Stdev(CtrlNode):
    nodeName: ClassVar[str]
    uiTemplate: Incomplete
    def processData(self, data: NDArray[Any] | MetaArray): ...

class Index(CtrlNode):
    nodeName: ClassVar[str]
    uiTemplate: Incomplete
    # Any sequence works when the selected axis is 0.
    def processData(self, data): ...

class Slice(CtrlNode):
    nodeName: ClassVar[str]
    uiTemplate: Incomplete
    # Any sequence works when the selected axis is 0.
    def processData(self, data): ...

class AsType(CtrlNode):
    nodeName: ClassVar[str]
    uiTemplate: Incomplete
    def processData(self, data: NDArray[Any] | MetaArray): ...
