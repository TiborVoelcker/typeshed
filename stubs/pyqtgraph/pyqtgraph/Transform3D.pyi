# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Any, Literal

import numpy as np
from numpy.typing import NDArray

from .Qt import QtGui

class Transform3D(QtGui.QMatrix4x4):
    # Either 16 numbers, a single 4x4 nested sequence/array, or a QMatrix4x4.
    def __init__(self, *args: float | Sequence[Sequence[float]] | NDArray[Any] | Incomplete) -> None: ...
    def matrix(self, nd: Literal[2, 3] = 3) -> NDArray[np.float64]: ...
    # Arrays and sequences are mapped element-wise; everything else is handed
    # to `QMatrix4x4.map()`.
    def map(self, obj): ...
    def inverted(self) -> tuple[Transform3D, bool]: ...
