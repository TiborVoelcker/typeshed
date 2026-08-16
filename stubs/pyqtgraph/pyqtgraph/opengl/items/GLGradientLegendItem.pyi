from _typeshed import Incomplete

from ...colormap import ColorMap
from ..GLGraphicsItem import GLGraphicsItem

__all__ = ["GLGradientLegendItem"]

class GLGradientLegendItem(GLGraphicsItem):
    # Position of the colorbar on the screen, from the top left corner, in pixels.
    pos: tuple[float, float]
    # Size of the colorbar without the text, in pixels.
    size: tuple[float, float]
    fontColor: Incomplete
    gradient: ColorMap
    # "text" -> position in the gradient, from 0 to 1.
    labels: dict[str, float]
    # Takes the `setData()` keys plus 'glOptions'.
    def __init__(self, parentItem: GLGraphicsItem | None = None, **kwds) -> None: ...
    antialias: bool
    # Accepted keys: 'size', 'pos', 'gradient', 'labels', 'fontColor'.
    def setData(self, **kwds) -> None: ...
    def paint(self) -> None: ...
