# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from _typeshed import Incomplete

from ..Qt import QtCore, QtWidgets  # type: ignore[import-not-found]  # pyright: ignore[reportMissingImports]
from .PlotCurveItem import PlotCurveItem
from .PlotDataItem import PlotDataItem

__all__ = ["FillBetweenItem"]

class FillBetweenItem(QtWidgets.QGraphicsPathItem):
    curves: Incomplete
    def __init__(
        self,
        curve1: PlotDataItem | PlotCurveItem,
        curve2: PlotDataItem | PlotCurveItem,
        brush=None,
        pen=None,
        fillRule: QtCore.Qt.FillRule = ...,
    ) -> None: ...
    def fillRule(self): ...
    def setFillRule(self, fillRule: QtCore.Qt.FillRule = ...): ...
    def setBrush(self, *args, **kwds) -> None: ...
    def setPen(self, *args, **kwds) -> None: ...
    def setCurves(self, curve1: PlotDataItem | PlotCurveItem, curve2: PlotDataItem | PlotCurveItem): ...
    def curveChanged(self) -> None: ...
    def updatePath(self) -> None: ...
