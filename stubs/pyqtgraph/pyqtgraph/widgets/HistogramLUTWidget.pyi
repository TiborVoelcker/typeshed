from typing import Literal

from ..graphicsItems.HistogramLUTItem import HistogramLUTItem
from .GraphicsView import GraphicsView

__all__ = ["HistogramLUTWidget"]

class HistogramLUTWidget(GraphicsView):
    item: HistogramLUTItem
    orientation: Literal["vertical", "horizontal"]
    def __init__(self, parent=None, *args, **kargs) -> None: ...
    def sizeHint(self): ...
    def __getattr__(self, attr: str): ...
