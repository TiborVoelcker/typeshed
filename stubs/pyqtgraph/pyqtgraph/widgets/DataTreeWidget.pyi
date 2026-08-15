# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from _typeshed import Incomplete

from ..Qt import QtWidgets  # type: ignore[import-not-found, import-untyped]  # pyright: ignore[reportMissingImports]

__all__ = ["DataTreeWidget"]

class DataTreeWidget(QtWidgets.QTreeWidget):
    def __init__(self, parent=None, data=None) -> None: ...
    widgets: Incomplete
    nodes: Incomplete
    def setData(self, data, hideRoot: bool = False) -> None: ...
    def buildTree(self, data, parent, name: str = "", hideRoot: bool = False, path=()) -> None: ...
    def parse(self, data): ...
