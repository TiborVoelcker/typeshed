# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

import typing
from _typeshed import Incomplete

from ..Qt import QtWidgets  # type: ignore[import-not-found, import-untyped]  # pyright: ignore[reportMissingImports]

__all__ = ["MatplotlibWidget"]

class MatplotlibWidget(QtWidgets.QWidget):
    parent_default: Incomplete
    figsize_default: Incomplete
    dpi_default: int
    @typing.overload
    def __init__(self, figsize=(5.0, 4.0), dpi: int = 100, parent=None) -> None: ...
    @typing.overload
    def __init__(self, parent=None, figsize=(5.0, 4.0), dpi: int = 100) -> None: ...
    def getFigure(self): ...
    def draw(self) -> None: ...
