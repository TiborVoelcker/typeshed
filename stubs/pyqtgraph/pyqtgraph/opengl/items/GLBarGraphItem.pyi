from typing import Any

from numpy.typing import NDArray

from ..GLGraphicsItem import GLGraphicsItem
from .GLMeshItem import GLMeshItem

__all__ = ["GLBarGraphItem"]

class GLBarGraphItem(GLMeshItem):
    # `pos` is a (..., 3) array of bar positions (the corner of each bar) and
    # `size` a (..., 3) array of the size of each bar.
    def __init__(self, pos: NDArray[Any], size: NDArray[Any], parentItem: GLGraphicsItem | None = None) -> None: ...
