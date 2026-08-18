from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Any, ClassVar

import numpy as np
from numpy.typing import NDArray

from ...graphicsItems.ROI import PolyLineROI
from ...metaarray import MetaArray
from ...Point import Point
from ..Node import Node
from .common import CtrlNode, PlottingCtrlNode, metaArrayWrapper
from .functions import _ArrayOrMeta

class Downsample(CtrlNode):
    nodeName: ClassVar[str]
    uiTemplate: Incomplete
    def processData(self, data: _ArrayOrMeta) -> _ArrayOrMeta: ...

class Subsample(CtrlNode):
    nodeName: ClassVar[str]
    uiTemplate: Incomplete
    def processData(self, data: _ArrayOrMeta) -> _ArrayOrMeta: ...

class Bessel(CtrlNode):
    nodeName: ClassVar[str]
    uiTemplate: Incomplete
    def processData(self, data: _ArrayOrMeta) -> _ArrayOrMeta: ...

class Butterworth(CtrlNode):
    nodeName: ClassVar[str]
    uiTemplate: Incomplete
    def processData(self, data: _ArrayOrMeta) -> _ArrayOrMeta: ...

class ButterworthNotch(CtrlNode):
    nodeName: ClassVar[str]
    uiTemplate: Incomplete
    def processData(self, data: _ArrayOrMeta) -> _ArrayOrMeta: ...

class Mean(CtrlNode):
    nodeName: ClassVar[str]
    uiTemplate: Incomplete
    @metaArrayWrapper
    def processData(self, data: _ArrayOrMeta) -> _ArrayOrMeta: ...

class Median(CtrlNode):
    nodeName: ClassVar[str]
    uiTemplate: Incomplete
    @metaArrayWrapper
    def processData(self, data: _ArrayOrMeta) -> _ArrayOrMeta: ...

class Mode(CtrlNode):
    nodeName: ClassVar[str]
    uiTemplate: Incomplete
    @metaArrayWrapper
    def processData(self, data: _ArrayOrMeta) -> _ArrayOrMeta: ...

class Denoise(CtrlNode):
    nodeName: ClassVar[str]
    uiTemplate: Incomplete
    def processData(self, data: _ArrayOrMeta) -> _ArrayOrMeta: ...

class Gaussian(CtrlNode):
    nodeName: ClassVar[str]
    uiTemplate: Incomplete
    @metaArrayWrapper
    def processData(self, data: _ArrayOrMeta) -> _ArrayOrMeta: ...

class Derivative(CtrlNode):
    nodeName: ClassVar[str]
    def processData(self, data: _ArrayOrMeta) -> _ArrayOrMeta: ...

class Integral(CtrlNode):
    nodeName: ClassVar[str]
    @metaArrayWrapper
    def processData(self, data: _ArrayOrMeta) -> _ArrayOrMeta: ...

class Detrend(CtrlNode):
    nodeName: ClassVar[str]
    @metaArrayWrapper
    def processData(self, data: _ArrayOrMeta) -> _ArrayOrMeta: ...

class RemoveBaseline(PlottingCtrlNode):
    nodeName: ClassVar[str]
    line: PolyLineROI
    def __init__(self, name: str) -> None: ...
    def connectToPlot(self, node: Node) -> None: ...
    def disconnectFromPlot(self, plot) -> None: ...  # `plot` is a PlotItem
    # Needs time values, so only a MetaArray will do.
    def processData(self, data: MetaArray) -> MetaArray: ...
    # Returns the points snapped onto `data`, plus the index of each within it.
    def adjustXPositions(self, pts: Sequence[Point], data: NDArray[Any]) -> tuple[list[Point], list[NDArray[np.intp]]]: ...

class AdaptiveDetrend(CtrlNode):
    nodeName: ClassVar[str]
    uiTemplate: Incomplete
    def processData(self, data: _ArrayOrMeta) -> _ArrayOrMeta: ...

class HistogramDetrend(CtrlNode):
    nodeName: ClassVar[str]
    uiTemplate: Incomplete
    def processData(self, data: _ArrayOrMeta) -> _ArrayOrMeta: ...

class RemovePeriodic(CtrlNode):
    nodeName: ClassVar[str]
    uiTemplate: Incomplete
    # Needs time values, so only a MetaArray will do.
    def processData(self, data: MetaArray) -> MetaArray: ...
