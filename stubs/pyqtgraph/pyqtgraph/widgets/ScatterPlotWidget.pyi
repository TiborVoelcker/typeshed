# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from _typeshed import Incomplete
from collections.abc import Mapping, Sequence
from typing import Any

import numpy as np
from numpy.typing import NDArray

from ..graphicsItems.PlotDataItem import PlotDataItem
from ..graphicsItems.TextItem import TextItem
from ..parametertree import Parameter, ParameterTree
from ..Qt import QtWidgets
from .ColorMapWidget import ColorMapParameter
from .DataFilterWidget import DataFilterParameter
from .PlotWidget import PlotWidget

__all__ = ["ScatterPlotWidget"]

class ScatterPlotWidget(QtWidgets.QSplitter):
    sigScatterPlotClicked: Incomplete
    sigScatterPlotHovered: Incomplete
    ctrlPanel: Incomplete
    fieldList: Incomplete
    ptree: ParameterTree
    filter: DataFilterParameter
    colorMap: ColorMapParameter
    params: Parameter
    plot: PlotWidget
    filterText: TextItem
    data: NDArray[Any] | None
    indices: NDArray[np.intp] | None
    mouseOverField: str | None
    scatterPlot: PlotDataItem | None
    selectionScatter: PlotDataItem | None
    selectedIndices: Sequence[int]
    style: dict[str, Any]
    def __init__(self, parent=None) -> None: ...
    fields: dict[str, Mapping[str, Any]]
    # `fields` has the same format as `ColorMapParameter.setFields`, but must be
    # a sequence of `(fieldName, {options})` pairs rather than a mapping
    def setFields(self, fields: Sequence[tuple[str, Mapping[str, Any]]], mouseOverField: str | None = None) -> None: ...
    def setSelectedFields(self, *fields: str) -> None: ...
    filtered: NDArray[Any] | None
    filteredIndices: NDArray[np.intp] | None
    # `data` must be a numpy record array
    def setData(self, data: NDArray[Any]) -> None: ...
    def setSelectedIndices(self, inds: Sequence[int]) -> None: ...
    # `points` are `SpotItem`s as emitted by `sigScatterPlotClicked`
    def setSelectedPoints(self, points) -> None: ...
    def fieldSelectionChanged(self) -> None: ...
    def filterChanged(self, f: DataFilterParameter) -> None: ...
    def updatePlot(self) -> None: ...
    def updateSelected(self) -> None: ...
    def plotClicked(self, plot, points, ev) -> None: ...
    def plotHovered(self, plot, points, ev) -> None: ...
