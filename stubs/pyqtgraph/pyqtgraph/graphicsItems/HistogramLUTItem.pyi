from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Literal, TypedDict
from typing_extensions import TypeAlias

import numpy as np
from numpy.typing import NDArray

from ..functions import _BrushArg
from .AxisItem import AxisItem
from .GradientEditorItem import GradientEditorItem, _GradientState
from .GraphicsWidget import GraphicsWidget
from .ImageItem import ImageItem
from .LinearRegionItem import LinearRegionItem
from .PlotCurveItem import PlotCurveItem
from .ViewBox import ViewBox

__all__ = ["HistogramLUTItem"]

_LevelMode: TypeAlias = Literal["mono", "rgba"]

class _HistogramLUTState(TypedDict):
    gradient: _GradientState
    levels: tuple[float, float] | list[tuple[float, float]]
    mode: _LevelMode

class HistogramLUTItem(GraphicsWidget):
    sigLookupTableChanged: Incomplete
    sigLevelsChanged: Incomplete
    sigLevelChangeFinished: Incomplete
    lut: NDArray[np.ubyte] | None
    imageItem: Incomplete
    levelMode: _LevelMode
    orientation: Literal["vertical", "horizontal"]
    gradientPosition: Literal["left", "right", "top", "bottom"]
    layout: Incomplete
    vb: ViewBox
    gradient: GradientEditorItem
    # [mono, r, g, b, a]
    regions: list[LinearRegionItem]
    region: LinearRegionItem
    axis: AxisItem
    plots: list[PlotCurveItem]
    plot: PlotCurveItem
    def __init__(
        self,
        image: ImageItem | None = None,
        fillHistogram: bool = True,
        levelMode: _LevelMode = "mono",
        gradientPosition: Literal["left", "right", "top", "bottom"] = "right",
        orientation: Literal["vertical", "horizontal"] = "vertical",
    ) -> None: ...
    def fillHistogram(self, fill: bool = True, level: float = 0.0, color: _BrushArg = (100, 100, 200)) -> None: ...
    def paint(self, p, *args) -> None: ...
    def setHistogramRange(self, mn: float, mx: float, padding: float = 0.1) -> None: ...
    def getHistogramRange(self) -> list[float]: ...
    def autoHistogramRange(self) -> None: ...
    def disableAutoHistogramRange(self) -> None: ...
    def setImageItem(self, img: ImageItem) -> None: ...
    def viewRangeChanged(self) -> None: ...
    def gradientChanged(self) -> None: ...
    # None in 'rgba' level mode.
    def getLookupTable(self, img: NDArray[np.generic] | None = None, n: int | None = None, alpha: bool | None = None): ...
    def regionChanged(self) -> None: ...
    def regionChanging(self) -> None: ...
    def imageChanged(self, autoLevel: bool = False, autoRange: bool = False) -> None: ...
    # A `(min, max)` pair in 'mono' mode, one such pair per channel in 'rgba' mode.
    def getLevels(self) -> tuple[float, float] | list[tuple[float, float]]: ...
    def setLevels(
        self, min: float | None = None, max: float | None = None, rgba: Sequence[Sequence[float]] | None = None
    ) -> None: ...
    def setLevelMode(self, mode: _LevelMode) -> None: ...
    def saveState(self) -> _HistogramLUTState: ...
    def restoreState(self, state: _HistogramLUTState) -> None: ...
