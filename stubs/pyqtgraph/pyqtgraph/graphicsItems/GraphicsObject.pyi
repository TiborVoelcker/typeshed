from ..Qt import QtWidgets  # type: ignore[import-not-found]  # pyright: ignore[reportMissingImports]
from .GraphicsItem import GraphicsItem

__all__ = ["GraphicsObject"]

class GraphicsObject(GraphicsItem, QtWidgets.QGraphicsObject):
    def __init__(self, *args) -> None: ...
    def itemChange(self, change, value): ...
