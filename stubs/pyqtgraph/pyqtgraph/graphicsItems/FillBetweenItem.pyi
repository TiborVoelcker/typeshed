# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from ..functions import _BrushArg, _PenArg
from ..Qt import QtCore, QtWidgets
from .PlotCurveItem import PlotCurveItem
from .PlotDataItem import PlotDataItem

__all__ = ["FillBetweenItem"]

class FillBetweenItem(QtWidgets.QGraphicsPathItem):
    curves: list[PlotDataItem | PlotCurveItem] | None
    def __init__(
        self,
        curve1: PlotDataItem | PlotCurveItem,
        curve2: PlotDataItem | PlotCurveItem,
        brush: _BrushArg = None,
        pen: _PenArg = None,
        fillRule: QtCore.Qt.FillRule = ...,
    ) -> None: ...
    def fillRule(self): ...
    def setFillRule(self, fillRule: QtCore.Qt.FillRule = ...) -> None: ...
    def setBrush(self, *args: _BrushArg, **kwds: _BrushArg) -> None: ...
    def setPen(self, *args: _PenArg, **kwds) -> None: ...
    def setCurves(self, curve1: PlotDataItem | PlotCurveItem, curve2: PlotDataItem | PlotCurveItem) -> None: ...
    def curveChanged(self) -> None: ...
    def updatePath(self) -> None: ...
