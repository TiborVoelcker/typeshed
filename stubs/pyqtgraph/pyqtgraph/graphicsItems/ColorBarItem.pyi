from _typeshed import Incomplete
from collections.abc import Iterable
from typing import Literal
from typing_extensions import TypeAlias

from ..colormap import ColorMap
from ..functions import _BrushArg, _PenArg
from ..widgets.ColorMapMenu import ColorMapMenu
from .AxisItem import AxisItem
from .ImageItem import ImageItem
from .LinearRegionItem import LinearRegionItem
from .PColorMeshItem import PColorMeshItem
from .PlotItem import PlotItem

__all__ = ["ColorBarItem"]

_ImageLike: TypeAlias = ImageItem | PColorMeshItem

class ColorBarItem(PlotItem):
    sigLevelsChanged: Incomplete
    sigLevelsChangeFinished: Incomplete
    img_list: list[Incomplete]  # list of `weakref.ref` to the controlled image items
    values: tuple[float, float]
    rounding: float
    horizontal: bool
    lo_lim: float | None
    hi_lim: float | None
    colorMapMenu: bool | ColorMapMenu
    axis: AxisItem
    bar: Incomplete
    interactive: bool
    region: LinearRegionItem | None
    region_changed_enable: bool
    def __init__(
        self,
        values: tuple[float, float] | None = None,
        width: float = 25,
        colorMap: ColorMap | str | None = None,
        label: str | None = None,
        interactive: bool = True,
        limits: tuple[float | None, float | None] | None = None,
        rounding: float = 1,
        orientation: Literal["horizontal", "h", "vertical", "v"] = "vertical",
        pen: _PenArg = "w",
        hoverPen: _PenArg = "r",
        hoverBrush: _BrushArg = "#FF000080",
        *,
        colorMapMenu: bool | ColorMapMenu = True,
    ) -> None: ...
    def setImageItem(self, img: _ImageLike | Iterable[_ImageLike], insert_in: PlotItem | None = None) -> None: ...
    def setColorMap(self, colorMap: ColorMap | str) -> None: ...
    def colorMap(self) -> ColorMap | None: ...
    def setLevels(
        self,
        values: tuple[float | None, float | None] | None = None,
        low: float | None = None,
        high: float | None = None,
        update_items: bool = True,
    ) -> None: ...
    def levels(self) -> tuple[float, float]: ...
    def mouseClickEvent(self, ev) -> None: ...
