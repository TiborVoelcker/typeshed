# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from _typeshed import Incomplete
from typing import Any, Literal

import numpy as np
from numpy.typing import NDArray

from ..functions import _BrushArg
from ..Qt import QtWidgets
from .DataTreeWidget import DataTreeWidget

__all__ = ["DiffTreeWidget"]

class DiffTreeWidget(QtWidgets.QWidget):
    layout: Incomplete
    trees: list[DataTreeWidget]
    def __init__(self, parent=None, a=None, b=None) -> None: ...
    data: tuple[Any, Any]
    def setData(self, a, b) -> None: ...
    def compare(self, a, b, path: tuple[Any, ...] = ()) -> None: ...
    def compareArrays(self, a, b) -> NDArray[np.bool_]: ...
    def setColor(self, path: tuple[Any, ...], column: int, color: _BrushArg, tree: Literal[0, 1] | None = None) -> None: ...
