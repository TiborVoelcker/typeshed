from _typeshed import Incomplete
from typing import Any

from numpy.typing import NDArray
from OpenGL.GL import *  # type: ignore[import-not-found, import-untyped]  # pyright: ignore[reportMissingImports]

from ..GLGraphicsItem import GLGraphicsItem
from .GLScatterPlotItem import GLScatterPlotItem

__all__ = ["GLGraphItem"]

class GLGraphItem(GLGraphicsItem):
    edges: NDArray[Any] | None
    # A QColor, or None to draw no edges.
    edgeColor: Incomplete
    edgeWidth: float
    scatter: GLScatterPlotItem
    def __init__(self, parentItem: GLGraphicsItem | None = None, **kwds) -> None: ...
    # Accepted keys: 'edges', 'edgeColor', 'edgeWidth', 'nodePositions', 'nodeColor',
    # 'nodeSize'; everything else is forwarded to `GLScatterPlotItem.setData()`.
    def setData(self, **kwds) -> None: ...
    def initializeGL(self) -> None: ...
    def paint(self) -> None: ...
