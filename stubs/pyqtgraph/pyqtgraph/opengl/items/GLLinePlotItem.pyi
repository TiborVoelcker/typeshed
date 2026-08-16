from _typeshed import Incomplete
from typing import Any

from numpy.typing import NDArray
from OpenGL.GL import *  # type: ignore[import-not-found, import-untyped]  # pyright: ignore[reportMissingImports]

from ..GLGraphicsItem import GLGraphicsItem

__all__ = ["GLLinePlotItem"]

class GLLinePlotItem(GLGraphicsItem):
    pos: NDArray[Any] | None
    # 'lines' or 'line_strip'.
    mode: str
    width: float
    # An (N, 4) array of floats, or a single color.
    color: Incomplete
    # Takes the `setData()` keys plus 'glOptions'.
    def __init__(self, parentItem: GLGraphicsItem | None = None, **kwds) -> None: ...
    antialias: bool
    # Accepted keys: 'pos', 'color', 'width', 'mode', 'antialias'.
    def setData(self, **kwds) -> None: ...
    def paint(self) -> None: ...
