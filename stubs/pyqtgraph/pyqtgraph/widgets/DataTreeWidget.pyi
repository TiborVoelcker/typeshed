# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from _typeshed import Incomplete
from typing import Any

from ..Qt import QtWidgets

__all__ = ["DataTreeWidget"]

class DataTreeWidget(QtWidgets.QTreeWidget):
    def __init__(self, parent=None, data=None) -> None: ...
    widgets: list[Incomplete]
    nodes: dict[tuple[Any, ...], Incomplete]
    def setData(self, data, hideRoot: bool = False) -> None: ...
    def buildTree(self, data, parent, name: str = "", hideRoot: bool = False, path: tuple[Any, ...] = ()) -> None: ...
    # (type name, short description, sub-objects to parse, optional widget to show as a sub-node)
    def parse(self, data) -> tuple[str, str, dict[Any, Any], Incomplete]: ...
