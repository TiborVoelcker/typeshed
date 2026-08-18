# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from _typeshed import Incomplete

from ..functions import _BrushArg, _PenArg
from ..Qt import QtWidgets

__all__ = ["PathButton"]

class PathButton(QtWidgets.QPushButton):
    margin: float
    path: Incomplete  # QPainterPath
    def __init__(
        self,
        parent=None,
        path=None,
        pen: _PenArg = "default",
        brush: _BrushArg = None,
        size: tuple[int, int] | None = (30, 30),
        margin: float = 7,
    ) -> None: ...
    brush: Incomplete
    def setBrush(self, brush: _BrushArg) -> None: ...
    pen: Incomplete
    def setPen(self, *args: _PenArg, **kwargs) -> None: ...
    def setPath(self, path) -> None: ...
    def paintEvent(self, ev) -> None: ...
