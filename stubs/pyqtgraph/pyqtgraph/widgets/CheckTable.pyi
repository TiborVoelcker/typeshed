# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from _typeshed import Incomplete
from collections.abc import Sequence
from typing import TypedDict

from ..Qt import QtWidgets
from .VerticalLabel import VerticalLabel

__all__ = ["CheckTable"]

class _CheckTableState(TypedDict):
    cols: Sequence[str]
    # one entry per row: the row name followed by one bool per column
    rows: list[list[str | bool]]

class CheckTable(QtWidgets.QWidget):
    sigStateChanged: Incomplete
    layout: Incomplete
    headers: list[VerticalLabel]
    columns: Sequence[str]
    rowNames: list[str]
    rowWidgets: list[list[Incomplete]]
    oldRows: dict[str, list[str | bool]]
    def __init__(self, columns: Sequence[str]) -> None: ...
    def updateRows(self, rows: Sequence[str]) -> None: ...
    def addRow(self, name: str) -> None: ...
    def removeRow(self, name: str) -> None: ...
    def checkChanged(self, state: int) -> None: ...
    def saveState(self) -> _CheckTableState: ...
    def restoreState(self, state: _CheckTableState) -> None: ...
