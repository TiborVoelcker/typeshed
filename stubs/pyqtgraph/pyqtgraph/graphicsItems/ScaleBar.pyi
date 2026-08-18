from _typeshed import Incomplete

from ..functions import _BrushArg, _PenArg
from ..Point import _PointLike
from .GraphicsObject import GraphicsObject
from .GraphicsWidgetAnchor import GraphicsWidgetAnchor
from .TextItem import TextItem

__all__ = ["ScaleBar"]

class ScaleBar(GraphicsWidgetAnchor, GraphicsObject):
    brush: Incomplete
    pen: Incomplete
    size: float
    offset: _PointLike
    bar: Incomplete
    text: TextItem
    def __init__(
        self,
        size: float,
        width: float = 5,
        brush: _BrushArg = None,
        pen: _PenArg = None,
        suffix: str = "m",
        offset: _PointLike | None = None,
    ) -> None: ...
    def changeParent(self) -> None: ...
    def updateBar(self) -> None: ...
    def boundingRect(self): ...
    def setParentItem(self, p): ...
