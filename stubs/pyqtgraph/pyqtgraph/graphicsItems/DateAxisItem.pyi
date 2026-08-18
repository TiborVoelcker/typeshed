from _typeshed import Incomplete
from collections import OrderedDict
from collections.abc import Sequence
from datetime import datetime
from typing import Literal, Protocol
from typing_extensions import TypeAlias

import numpy as np
from numpy.typing import NDArray

from .AxisItem import AxisItem

__all__ = ["DateAxisItem"]

# All of the module-level names below are undocumented, but they make up the
# tick-generation table that `DateAxisItem.zoomLevels` is built from.
MS_SPACING: float  # undocumented
SECOND_SPACING: int  # undocumented
MINUTE_SPACING: int  # undocumented
HOUR_SPACING: int  # undocumented
DAY_SPACING: int  # undocumented
WEEK_SPACING: int  # undocumented
MONTH_SPACING: int  # undocumented
YEAR_SPACING: int  # undocumented
MIN_REGULAR_TIMESTAMP: float  # undocumented
MAX_REGULAR_TIMESTAMP: float  # undocumented
SEC_PER_YEAR: float  # undocumented

def utcfromtimestamp(timestamp: float) -> datetime: ...  # undocumented

class _Stepper(Protocol):
    # Returns the first tick at or after `val` when `first` is True, otherwise
    # the tick following `val`; `inf` once `val` leaves the representable range.
    def __call__(self, val: float, n: int, first: bool) -> float: ...

def makeMSStepper(stepSize: float) -> _Stepper: ...  # undocumented
def makeSStepper(stepSize: float) -> _Stepper: ...  # undocumented
def makeMStepper(stepSize: int) -> _Stepper: ...  # undocumented
def makeYStepper(stepSize: int) -> _Stepper: ...  # undocumented

class TickSpec:
    spacing: float
    step: _Stepper
    # A list of step-size multipliers applied when the tick density gets too
    # high, or `None` to disable auto-skipping.
    autoSkip: Sequence[float] | None
    format: str
    def __init__(self, spacing: float, stepper: _Stepper, format: str, autoSkip: Sequence[float] | None = None) -> None: ...
    def makeTicks(self, minVal: float, maxVal: float, minSpc: float) -> tuple[NDArray[np.float64], int]: ...
    def skipFactor(self, minSpc: float) -> int: ...

class ZoomLevel:
    tickSpecs: Sequence[TickSpec]
    utcOffset: float
    exampleText: str
    def __init__(self, tickSpecs: Sequence[TickSpec], exampleText: str) -> None: ...
    # A list of `(average spacing, tick positions)` pairs.
    def tickValues(self, minVal: float, maxVal: float, minSpc: float) -> list[tuple[float, list[float]]]: ...

YEAR_MONTH_ZOOM_LEVEL: ZoomLevel  # undocumented
MONTH_DAY_ZOOM_LEVEL: ZoomLevel  # undocumented
DAY_HOUR_ZOOM_LEVEL: ZoomLevel  # undocumented
HOUR_MINUTE_ZOOM_LEVEL: ZoomLevel  # undocumented
HMS_ZOOM_LEVEL: ZoomLevel  # undocumented
MS_ZOOM_LEVEL: ZoomLevel  # undocumented

def getOffsetFromUtc() -> int: ...  # undocumented

_Orientation: TypeAlias = Literal["left", "right", "top", "bottom"]

class DateAxisItem(AxisItem):
    utcOffset: float
    zoomLevels: OrderedDict[float, ZoomLevel]
    autoSIPrefix: bool
    def __init__(self, orientation: _Orientation = "bottom", utcOffset: float | None = None, **kwargs) -> None: ...
    def tickStrings(self, values: Sequence[float], scale: float, spacing: float) -> list[str]: ...
    def tickValues(self, minVal: float, maxVal: float, size: float) -> list[tuple[float, Sequence[float]]]: ...
    zoomLevel: ZoomLevel
    minSpacing: float
    def setZoomLevelForDensity(self, density: float) -> None: ...
    def linkToView(self, view) -> None: ...
    fontMetrics: Incomplete
    def generateDrawSpecs(self, p): ...
