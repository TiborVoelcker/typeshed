from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Any

from numpy.typing import NDArray
from OpenGL.GL import *  # type: ignore[import-not-found, import-untyped]  # pyright: ignore[reportMissingImports]

from ..GLGraphicsItem import GLGraphicsItem

__all__ = ["GLTextItem"]

class GLTextItem(GLGraphicsItem):
    pos: NDArray[Any] | Sequence[float]
    color: Incomplete
    text: str
    font: Incomplete
    # Takes the `setData()` keys plus 'glOptions'.
    def __init__(self, parentItem: GLGraphicsItem | None = None, **kwds) -> None: ...
    # Accepted keys: 'pos', 'color', 'text', 'font'.
    def setData(self, **kwds) -> None: ...
    def paint(self) -> None: ...
