# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from _typeshed import Incomplete

from ..Qt import QtWidgets  # type: ignore[import-not-found, import-untyped]  # pyright: ignore[reportMissingImports]

__all__ = ["PathButton"]

class PathButton(QtWidgets.QPushButton):
    margin: Incomplete
    path: Incomplete
    def __init__(self, parent=None, path=None, pen: str = "default", brush=None, size=(30, 30), margin: int = 7) -> None: ...
    brush: Incomplete
    def setBrush(self, brush) -> None: ...
    pen: Incomplete
    def setPen(self, *args, **kwargs) -> None: ...
    def setPath(self, path) -> None: ...
    def paintEvent(self, ev) -> None: ...
