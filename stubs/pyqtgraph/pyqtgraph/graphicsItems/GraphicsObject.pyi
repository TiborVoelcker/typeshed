# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from ..Qt import QtWidgets
from .GraphicsItem import GraphicsItem

__all__ = ["GraphicsObject"]

class GraphicsObject(GraphicsItem, QtWidgets.QGraphicsObject):
    def __init__(self, *args) -> None: ...
    def itemChange(self, change, value): ...
