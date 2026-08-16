# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from _typeshed import Incomplete
from collections.abc import Sequence
from typing import NamedTuple
from typing_extensions import TypeAlias

from ..colormap import ColorMap
from ..Qt import QtWidgets

__all__ = ["ColorMapMenu"]

# A colormap name, a (name, source) pair, or a `ColorMap` itself.
_ColorMapSpecifier: TypeAlias = str | tuple[str, str] | ColorMap

class PrivateActionData(NamedTuple):
    name: str | None
    source: str | ColorMap | None

class ColorMapMenu(QtWidgets.QMenu):
    sigColorMapTriggered: Incomplete
    def __init__(
        self,
        *,
        userList: Sequence[_ColorMapSpecifier] | None = None,
        showGradientSubMenu: bool = False,
        showColorMapSubMenus: bool = False,
    ) -> None: ...
    def onTriggered(self, action) -> None: ...
    def buildGradientSubMenu(self) -> None: ...
    def buildLocalSubMenu(self) -> None: ...
    def buildCetLocalSubMenu(self) -> None: ...
    def buildCetExternalSubMenu(self) -> None: ...
    def buildMplCategorySubMenu(self) -> None: ...
    def buildMplOthersSubMenu(self) -> None: ...
    def buildColorcetSubMenu(self) -> None: ...
    def buildSubMenu(self, names: Sequence[str], source: str | None, sort: bool = True) -> None: ...
    @staticmethod
    def actionDataToColorMap(data: PrivateActionData) -> ColorMap: ...
