from _typeshed import Incomplete
from collections.abc import Sequence

import numpy as np
from numpy.typing import NDArray

from ..functions import _PenArg
from .GraphicsObject import GraphicsObject
from .ScatterPlotItem import ScatterPlotItem

__all__ = ["GraphItem"]

class GraphItem(GraphicsObject):
    scatter: ScatterPlotItem
    adjacency: NDArray[np.integer[Incomplete]] | None
    pos: Incomplete  # (N, 2) array of node positions, or None
    picture: Incomplete
    pen: Incomplete  # a QPen, a record array of per-line pens, "default" or None
    # Accepts the same keywords as `setData`.
    def __init__(self, **kwds) -> None: ...
    # Accepts `pos`, `adj`, `pen`, `symbolPen`, `symbolBrush` plus any keyword
    # accepted by `ScatterPlotItem.setData`.
    def setData(self, **kwds) -> None: ...
    def setPen(self, *args: _PenArg, **kwargs) -> None: ...
    def generatePicture(self) -> None: ...
    def paint(self, p, *args) -> None: ...
    def boundingRect(self): ...
    # Forwarded to `ScatterPlotItem.dataBounds(ax, frac=1.0, orthoRange=None)`.
    def dataBounds(self, *args, **kwds) -> Sequence[float | None]: ...
    def pixelPadding(self) -> float: ...
