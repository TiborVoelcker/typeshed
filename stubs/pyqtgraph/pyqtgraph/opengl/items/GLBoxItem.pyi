from OpenGL.GL import *  # type: ignore[import-not-found, import-untyped]  # pyright: ignore[reportMissingImports]

from ...functions import _ColorArg
from ..GLGraphicsItem import GLGraphicsItem, _GLOptionsArg

__all__ = ["GLBoxItem"]

class GLBoxItem(GLGraphicsItem):
    def __init__(
        self,
        size=None,
        color: _ColorArg | None = None,
        glOptions: _GLOptionsArg = "translucent",
        parentItem: GLGraphicsItem | None = None,
    ) -> None: ...
    # Either x/y/z, or a single QVector3D as `size`.
    def setSize(self, x: float | None = None, y: float | None = None, z: float | None = None, size=None) -> None: ...
    def size(self) -> list[float]: ...
    def setColor(self, *args: _ColorArg) -> None: ...
    def color(self): ...
    def paint(self) -> None: ...
