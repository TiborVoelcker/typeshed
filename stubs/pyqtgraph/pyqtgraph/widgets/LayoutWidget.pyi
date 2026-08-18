# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from _typeshed import Incomplete
from typing import Literal
from typing_extensions import TypeAlias

from ..Qt import QtWidgets

__all__ = ["LayoutWidget"]

# `"next"` starts a new row before placing the widget
_RowArg: TypeAlias = int | Literal["next"] | None

class LayoutWidget(QtWidgets.QWidget):
    layout: Incomplete
    items: dict[Incomplete, tuple[int, int]]
    rows: dict[int, dict[int, Incomplete]]
    currentRow: int
    currentCol: int
    def __init__(self, parent=None) -> None: ...
    def nextRow(self) -> None: ...
    def nextColumn(self, colspan: int = 1) -> int: ...
    def nextCol(self, *args, **kargs) -> int: ...
    def addLabel(
        self, text: str = " ", row: _RowArg = None, col: int | None = None, rowspan: int = 1, colspan: int = 1, **kargs
    ): ...
    def addLayout(
        self, row: _RowArg = None, col: int | None = None, rowspan: int = 1, colspan: int = 1, **kargs
    ) -> LayoutWidget: ...
    def addWidget(self, item, row: _RowArg = None, col: int | None = None, rowspan: int = 1, colspan: int = 1) -> None: ...
    def getWidget(self, row: int, col: int): ...
