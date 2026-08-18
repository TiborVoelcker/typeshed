from OpenGL.GL import *  # type: ignore[import-not-found, import-untyped]  # pyright: ignore[reportMissingImports]

from ..GLGraphicsItem import GLGraphicsItem, _GLOptionsArg

__all__ = ["GLAxisItem"]

class GLAxisItem(GLGraphicsItem):
    antialias: bool
    def __init__(
        self,
        size=None,
        antialias: bool = True,
        glOptions: _GLOptionsArg = "translucent",
        parentItem: GLGraphicsItem | None = None,
    ) -> None: ...
    # Either x/y/z, or a single QVector3D as `size`.
    def setSize(self, x: float | None = None, y: float | None = None, z: float | None = None, size=None) -> None: ...
    def size(self) -> list[float]: ...
    def paint(self) -> None: ...
