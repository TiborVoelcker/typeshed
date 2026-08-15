# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from _typeshed import Incomplete

from ..Qt import QtWidgets  # type: ignore[import-not-found]  # pyright: ignore[reportMissingImports]

__all__ = ["CheckTable"]

class CheckTable(QtWidgets.QWidget):
    sigStateChanged: Incomplete
    layout: Incomplete
    headers: Incomplete
    columns: Incomplete
    rowNames: Incomplete
    rowWidgets: Incomplete
    oldRows: Incomplete
    def __init__(self, columns) -> None: ...
    def updateRows(self, rows) -> None: ...
    def addRow(self, name) -> None: ...
    def removeRow(self, name) -> None: ...
    def checkChanged(self, state) -> None: ...
    def saveState(self): ...
    def restoreState(self, state) -> None: ...
