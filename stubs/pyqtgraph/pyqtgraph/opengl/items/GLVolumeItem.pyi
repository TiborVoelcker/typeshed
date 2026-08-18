from _typeshed import Incomplete
from typing import Any

import numpy as np
from numpy.typing import NDArray
from OpenGL.GL import *  # type: ignore[import-not-found, import-untyped]  # pyright: ignore[reportMissingImports]

from ..GLGraphicsItem import GLGraphicsItem, _GLOptionsArg

__all__ = ["GLVolumeItem"]

class GLVolumeItem(GLGraphicsItem):
    # Density of slices to render through the volume; 1 means one slice per voxel.
    sliceDensity: int
    smooth: bool
    data: NDArray[Any] | None
    texture: Incomplete
    # `data` must be a 4D (x, y, z, RGBA) array of dtype ubyte.
    def __init__(
        self,
        data: NDArray[np.uint8],
        sliceDensity: int = 1,
        smooth: bool = True,
        glOptions: _GLOptionsArg = "translucent",
        parentItem: GLGraphicsItem | None = None,
    ) -> None: ...
    def setData(self, data: NDArray[np.uint8]) -> None: ...
    def paint(self) -> None: ...
    # `ax` is the axis index (0, 1 or 2); `d` is the direction along it (-1 or 1).
    def drawVolume(self, ax: int, d: int) -> None: ...
