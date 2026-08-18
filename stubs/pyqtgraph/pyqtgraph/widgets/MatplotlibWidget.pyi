# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

import typing
from _typeshed import Incomplete
from typing import ClassVar

from ..Qt import QtWidgets

__all__ = ["MatplotlibWidget"]

class MatplotlibWidget(QtWidgets.QWidget):
    parent_default: ClassVar[None]
    figsize_default: ClassVar[tuple[float, float]]
    dpi_default: ClassVar[int]
    @typing.overload
    def __init__(self, figsize: tuple[float, float] = (5.0, 4.0), dpi: int = 100, parent=None) -> None: ...
    @typing.overload
    def __init__(self, parent=None, figsize: tuple[float, float] = (5.0, 4.0), dpi: int = 100) -> None: ...
    fig: Incomplete  # matplotlib.figure.Figure
    canvas: Incomplete  # matplotlib.backends.backend_qtagg.FigureCanvasQTAgg
    toolbar: Incomplete  # matplotlib.backends.backend_qtagg.NavigationToolbar2QT
    vbox: Incomplete
    # returns the `matplotlib.figure.Figure` being displayed
    def getFigure(self): ...
    def draw(self) -> None: ...
