from _typeshed import Incomplete
from typing import Any

from numpy.typing import NDArray
from OpenGL.GL import *  # type: ignore[import-not-found, import-untyped]  # pyright: ignore[reportMissingImports]

from ..GLGraphicsItem import GLGraphicsItem
from ..shaders import ShaderProgram

__all__ = ["GLScatterPlotItem"]

class GLScatterPlotItem(GLGraphicsItem):
    pos: NDArray[Any] | None
    # A single size for every spot, or an (N,) array of sizes.
    size: float | NDArray[Any]
    # An (N, 4) array of floats, or a single color.
    color: Incomplete
    pxMode: bool
    shader: ShaderProgram | None
    # Takes the `setData()` keys plus 'glOptions'.
    def __init__(self, parentItem: GLGraphicsItem | None = None, **kwds) -> None: ...
    # Accepted keys: 'pos', 'color', 'size', 'pxMode'.
    def setData(self, **kwds) -> None: ...
    pointTexture: Incomplete
    def initializeGL(self) -> None: ...
    def paint(self) -> None: ...
