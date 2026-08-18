from _typeshed import Incomplete
from collections.abc import Sequence
from typing import ClassVar, Literal

from ..functions import _BrushArg, _PenArg
from .GraphicsObject import GraphicsObject
from .InfiniteLine import InfiniteLine

__all__ = ["LinearRegionItem"]

class LinearRegionItem(GraphicsObject):
    sigRegionChangeFinished: Incomplete
    sigRegionChanged: Incomplete
    Vertical: ClassVar[Literal[0]]
    Horizontal: ClassVar[Literal[1]]
    orientation: Literal["vertical", "horizontal"]
    blockLineSignal: bool
    moving: bool
    mouseHovering: bool
    span: Sequence[float]
    swapMode: Literal["sort", "block", "push"] | None
    clipItem: Incomplete
    lines: tuple[InfiniteLine, InfiniteLine]
    def __init__(
        self,
        values: Sequence[float] = (0, 1),
        orientation: Literal["vertical", "horizontal"] = "vertical",
        brush: _BrushArg = None,
        pen: _PenArg = None,
        hoverBrush: _BrushArg = None,
        hoverPen: _PenArg = None,
        movable: bool = True,
        bounds: Sequence[float] | None = None,
        span: Sequence[float] = (0, 1),
        swapMode: Literal["sort", "block", "push"] | None = "sort",
        clipItem=None,
    ) -> None: ...
    def getRegion(self) -> tuple[float, float]: ...
    def setRegion(self, rgn: Sequence[float]) -> None: ...
    brush: Incomplete
    currentBrush: Incomplete
    def setBrush(self, *br: _BrushArg, **kargs) -> None: ...
    hoverBrush: Incomplete
    def setHoverBrush(self, *br: _BrushArg, **kargs) -> None: ...
    def setBounds(self, bounds: Sequence[float] | None) -> None: ...
    movable: Incomplete
    def setMovable(self, m: bool = True) -> None: ...
    def setSpan(self, mn: float, mx: float) -> None: ...
    def setClipItem(self, item=None) -> None: ...
    def boundingRect(self): ...
    def paint(self, p, *args) -> None: ...
    def dataBounds(self, axis: int, frac: float = 1.0, orthoRange: Sequence[float] | None = None): ...
    def lineMoved(self, i: int) -> None: ...
    def lineMoveFinished(self) -> None: ...
    cursorOffsets: Incomplete
    startPositions: Incomplete
    def mouseDragEvent(self, ev) -> None: ...
    def mouseClickEvent(self, ev) -> None: ...
    def hoverEvent(self, ev) -> None: ...
    def setMouseHover(self, hover: bool) -> None: ...
