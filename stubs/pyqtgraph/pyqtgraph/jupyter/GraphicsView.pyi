# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from _typeshed import Incomplete

import jupyter_rfb  # type: ignore[import-not-found, import-untyped]  # pyright: ignore[reportMissingImports]

from ..graphicsItems.GraphicsLayout import GraphicsLayout
from ..graphicsItems.PlotItem import PlotItem
from ..graphicsItems.ViewBox import ViewBox

__all__ = ["GraphicsLayoutWidget", "PlotWidget"]

class GraphicsView(jupyter_rfb.RemoteFrameBuffer):
    gfxView: Incomplete
    logical_size: tuple[float, float]
    pixel_ratio: float
    def __init__(self, **kwds) -> None: ...
    def get_frame(self): ...
    def handle_event(self, event) -> None: ...

class GraphicsLayoutWidget(GraphicsView):
    gfxLayout: GraphicsLayout
    def __init__(self, **kwds) -> None: ...
    def addPlot(self, *args, **kwds) -> PlotItem: ...
    def addViewBox(self, *args, **kwds) -> ViewBox: ...

class PlotWidget(GraphicsView):
    plotItem: PlotItem
    def __init__(self, **kwds) -> None: ...
    def getPlotItem(self) -> PlotItem: ...
    # Any other PlotItem method, forwarded to `self.plotItem`.
    def __getattr__(self, attr: str): ...
