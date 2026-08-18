# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from _typeshed import Incomplete
from typing import Any

import numpy as np
from numpy.typing import NDArray
from OpenGL.GL import *  # type: ignore[import-not-found, import-untyped]  # pyright: ignore[reportMissingImports]

from ..Qt import QtWidgets

__all__ = ["RawImageWidget", "RawImageGLWidget"]

class RawImageWidget(QtWidgets.QWidget):
    scaled: bool
    # the `(img, args, kargs)` passed to the last `setImage` call
    opts: tuple[Any, ...] | None
    image: Incomplete  # QImage
    def __init__(self, parent=None, scaled: bool = False) -> None: ...
    # `img` has shape (x, y), (x, y, 3) or (x, y, 4); the extra arguments go to `functions.makeARGB`
    def setImage(self, img: NDArray[Any], *args, **kargs) -> None: ...
    def paintEvent(self, ev) -> None: ...

class RawImageGLWidget(QtWidgets.QOpenGLWidget):
    scaled: bool
    image: NDArray[np.ubyte] | None
    uploaded: bool
    smooth: bool
    opts: tuple[Any, ...] | None
    def __init__(self, parent=None, scaled: bool = False) -> None: ...
    def setImage(self, img: NDArray[Any], *args, **kargs) -> None: ...
    texture: Incomplete
    def initializeGL(self) -> None: ...
    def uploadTexture(self) -> None: ...
    def paintGL(self) -> None: ...
