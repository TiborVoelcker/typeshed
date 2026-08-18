from _typeshed import Incomplete
from typing import Any

from numpy.typing import ArrayLike, NDArray

from ..colormap import ColorMap
from ..functions import _PenArg
from .GraphicsObject import GraphicsObject

__all__ = ["NonUniformImage"]

class NonUniformImage(GraphicsObject):
    cmap: ColorMap | None
    lut: Incomplete  # a lookup-table array, a callable returning one, or None
    # Shadows `QGraphicsItem.data`; on an instance it is the `(x, y, z)` tuple
    # of `float64` arrays passed to `__init__`.
    data: Incomplete
    levels: tuple[float, float] | None
    border: Incomplete
    picture: Incomplete
    def __init__(self, x: ArrayLike, y: ArrayLike, z: ArrayLike, border: _PenArg = None) -> None: ...
    def setLookupTable(self, lut, update: bool = True, **kwargs) -> None: ...
    def setColorMap(self, cmap: ColorMap) -> None: ...
    # `kwds` are passed on to `numpy.histogram`.
    def getHistogram(self, **kwds) -> tuple[NDArray[Any], NDArray[Any]]: ...
    def setLevels(self, levels: tuple[float, float] | None) -> None: ...
    def getLevels(self) -> tuple[float, float]: ...
    def generatePicture(self) -> None: ...
    def paint(self, p, *args) -> None: ...
    def boundingRect(self): ...
