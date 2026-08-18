from _typeshed import Incomplete
from typing import Any

import numpy as np
from numpy.typing import NDArray
from OpenGL.GL import *  # type: ignore[import-not-found, import-untyped]  # pyright: ignore[reportMissingImports]

from ..GLGraphicsItem import GLGraphicsItem, _GLOptionsArg

__all__ = ["GLImageItem"]

class GLImageItem(GLGraphicsItem):
    smooth: bool
    texture: Incomplete
    # `data` must be a 3D (x, y, RGBA) array of dtype ubyte.
    def __init__(
        self,
        data: NDArray[np.uint8],
        smooth: bool = False,
        glOptions: _GLOptionsArg = "translucent",
        parentItem: GLGraphicsItem | None = None,
    ) -> None: ...
    def initializeGL(self) -> None: ...
    data: NDArray[Any]
    def setData(self, data: NDArray[np.uint8]) -> None: ...
    def paint(self) -> None: ...
