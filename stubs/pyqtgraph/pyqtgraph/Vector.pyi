# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from _typeshed import Incomplete
from collections.abc import Iterator, Sequence
from typing import Literal
from typing_extensions import TypeAlias

from .Qt import QT_LIB as QT_LIB, QtGui  # type: ignore[import-not-found, import-untyped]  # pyright: ignore[reportMissingImports]

# Anything `Vector()` accepts: two or three numbers, a length-2/3 sequence, or a
# QVector3D / QPoint / QPointF / QSizeF (`Incomplete`, since `pyqtgraph.Qt` is
# not stubbed).
_VectorArg: TypeAlias = float | Sequence[float] | Incomplete

class Vector(QtGui.QVector3D):
    def __init__(self, *args: _VectorArg) -> None: ...
    def __len__(self) -> Literal[3]: ...
    def __getitem__(self, i: int) -> float: ...
    def __setitem__(self, i: int, x: float) -> None: ...
    def __iter__(self) -> Iterator[float]: ...
    # `None` when either vector has zero length.
    def angle(self, a: Vector) -> float | None: ...
    def __abs__(self) -> Vector: ...
