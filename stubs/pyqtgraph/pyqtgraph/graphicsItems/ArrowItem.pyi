# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from _typeshed import Incomplete
from collections.abc import Sequence

from ..Qt import QtWidgets

__all__ = ["ArrowItem"]

class ArrowItem(QtWidgets.QGraphicsPathItem):
    opts: dict[str, Incomplete]
    # Accepts `pos` plus any keyword accepted by `setStyle`.
    def __init__(self, parent=None, **opts) -> None: ...
    path: Incomplete
    def setStyle(self, **opts) -> None: ...
    def paint(self, p, *args) -> None: ...
    def shape(self): ...
    def dataBounds(self, ax: int, frac: float, orthoRange: Sequence[float] | None = None) -> list[float]: ...
    def pixelPadding(self) -> float: ...
