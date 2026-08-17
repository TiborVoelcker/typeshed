from _typeshed import Incomplete
from collections.abc import Mapping, Sequence
from typing import Any, ClassVar

import numpy as np
from numpy.typing import ArrayLike, NDArray

from ...graphicsItems.PlotDataItem import PlotDataItem
from ...graphicsItems.ScatterPlotItem import ScatterPlotItem
from ...widgets.ComboBox import ComboBox
from ..Node import Node
from ..Terminal import Terminal
from .common import CtrlNode

class PlotWidgetNode(Node):
    nodeName: ClassVar[str]
    sigPlotChanged: Incomplete
    plot: Incomplete  # the currently selected PlotWidget or PlotItem, or None
    plots: dict[str, Incomplete]  # the plots the user may select from
    ui: ComboBox | None
    items: dict[int, Incomplete]  # {id(value): graphics item shown for it}
    def __init__(self, name: str) -> None: ...
    def disconnected(self, localTerm: Terminal, remoteTerm: Terminal) -> None: ...
    def setPlot(self, plot) -> None: ...  # a PlotWidget or PlotItem
    def getPlot(self): ...
    # `In` is a multi-input terminal, so it arrives as {remote terminal: value}.
    def process(self, In: Mapping[Terminal, Any], display: bool = True) -> None: ...  # type: ignore[override]
    # The base returns a dict of output values; this override always returns None.
    def processBypassed(self, args) -> None: ...  # type: ignore[override]
    def ctrlWidget(self): ...
    def plotSelected(self, index: int) -> None: ...
    def setPlotList(self, plots: Mapping[str, Incomplete]) -> None: ...
    def updateUi(self) -> None: ...

class CanvasNode(Node):
    nodeName: ClassVar[str]
    canvas: Incomplete  # a Canvas, or None
    items: dict[int, Incomplete]  # {id(value): item added to the canvas}
    def __init__(self, name: str) -> None: ...
    def disconnected(self, localTerm: Terminal, remoteTerm: Terminal) -> None: ...
    def setCanvas(self, canvas) -> None: ...
    def getCanvas(self): ...
    # `In` is a multi-input terminal, so it arrives as {remote terminal: value}.
    def process(self, In: Mapping[Terminal, Any], display: bool = True) -> None: ...  # type: ignore[override]

class PlotCurve(CtrlNode):
    nodeName: ClassVar[str]
    uiTemplate: Incomplete
    item: PlotDataItem
    def __init__(self, name: str) -> None: ...
    def process(self, x: ArrayLike, y: ArrayLike, display: bool = True) -> dict[str, Any]: ...  # type: ignore[override]

class ScatterPlot(CtrlNode):
    nodeName: ClassVar[str]
    uiTemplate: Incomplete
    item: ScatterPlotItem
    keys: Sequence[str] | None
    def __init__(self, name: str) -> None: ...
    # `input` is a record array or a sequence of mappings.
    def process(self, input, display: bool = True) -> dict[str, Any]: ...  # type: ignore[override]
    def updateKeys(self, data: Mapping[str, Any] | Sequence[str] | NDArray[Any] | np.void) -> None: ...
    def saveState(self) -> dict[str, Any]: ...
    def restoreState(self, state: Mapping[str, Any]) -> None: ...
