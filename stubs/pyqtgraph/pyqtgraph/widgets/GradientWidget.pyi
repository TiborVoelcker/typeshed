from _typeshed import Incomplete
from typing import Literal
from typing_extensions import TypeAlias

from ..graphicsItems.GradientEditorItem import GradientEditorItem
from .GraphicsView import GraphicsView

__all__ = ["GradientWidget"]

_Orientation: TypeAlias = Literal["bottom", "top", "left", "right"]

class GradientWidget(GraphicsView):
    sigGradientChanged: Incomplete
    sigGradientChangeFinished: Incomplete
    maxDim: int
    item: GradientEditorItem
    def __init__(self, parent=None, orientation: _Orientation = "bottom", *args, **kargs) -> None: ...
    orientation: _Orientation
    def setOrientation(self, ort: _Orientation) -> None: ...
    def setMaxDim(self, mx: int | None = None) -> None: ...
    def __getattr__(self, attr: str): ...
    def widgetGroupInterface(self): ...
