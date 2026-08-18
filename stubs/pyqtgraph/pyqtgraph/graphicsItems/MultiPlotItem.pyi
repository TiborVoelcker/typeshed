from . import GraphicsLayout
from .PlotItem import PlotItem

__all__ = ["MultiPlotItem"]

class MultiPlotItem(GraphicsLayout.GraphicsLayout):
    # `(plot, row, column)` for each generated plot; `None` once `close` has run.
    plots: list[tuple[PlotItem, int, int]] | None
    def __init__(self, *args, **kwds) -> None: ...
    # `data` must be a 2-D `metaarray.MetaArray`; `plotArgs` are passed on to `PlotItem.plot`.
    def plot(self, data, **plotArgs) -> None: ...
    def close(self) -> None: ...
