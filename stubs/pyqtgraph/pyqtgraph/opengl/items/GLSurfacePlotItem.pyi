from typing import Any

from numpy.typing import ArrayLike, NDArray
from OpenGL.GL import *  # type: ignore[import-not-found, import-untyped]  # pyright: ignore[reportMissingImports]

from ..GLGraphicsItem import GLGraphicsItem
from .GLMeshItem import GLMeshItem

__all__ = ["GLSurfacePlotItem"]

class GLSurfacePlotItem(GLMeshItem):
    # `x`, `y`, `z` and `colors` are passed to `setData()`; all other keyword
    # arguments go to `GLMeshItem.__init__()`.
    def __init__(
        self,
        x: NDArray[Any] | None = None,
        y: NDArray[Any] | None = None,
        z: NDArray[Any] | None = None,
        colors: ArrayLike | None = None,
        parentItem: GLGraphicsItem | None = None,
        **kwds,
    ) -> None: ...
    # `x` and `y` are 1D grid positions, `z` is a 2D (len(x), len(y)) array of
    # heights and `colors` is a (width, height, 4) array. `None` leaves the
    # corresponding data unchanged.
    def setData(
        self,
        x: NDArray[Any] | None = None,
        y: NDArray[Any] | None = None,
        z: NDArray[Any] | None = None,
        colors: ArrayLike | None = None,
    ) -> None: ...
    def generateFaces(self) -> None: ...
