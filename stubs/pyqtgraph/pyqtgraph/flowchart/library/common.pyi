from _typeshed import Incomplete
from collections.abc import Callable, Mapping, Sequence
from typing import Any, TypeVar
from typing_extensions import TypeAlias

from ...WidgetGroup import WidgetGroup
from ..Node import Node
from ..Terminal import Terminal

__all__ = ["CtrlNode", "PlottingCtrlNode", "metaArrayWrapper"]

_F = TypeVar("_F", bound=Callable[..., Any])

# `(name, type)` or `(name, type, opts)`, where type is one of "intSpin",
# "doubleSpin", "spin", "check", "combo" or "color".
_UiSpec: TypeAlias = tuple[str, str] | tuple[str, str, dict[str, Any]]

HAVE_METAARRAY: bool

# Returns `(widget, group, ctrls)`; `ctrls` maps each spec name to its widget.
def generateUi(opts: Sequence[_UiSpec]) -> tuple[Incomplete, WidgetGroup, dict[str, Incomplete]]: ...  # undocumented

class CtrlNode(Node):
    sigStateChanged: Incomplete
    ui: Incomplete  # QWidget
    stateGroup: WidgetGroup
    ctrls: dict[str, Incomplete]  # {name: QWidget}
    def __init__(
        self, name: str, ui: Sequence[_UiSpec] | None = None, terminals: Mapping[str, Mapping[str, Any]] | None = None
    ) -> None: ...
    def ctrlWidget(self): ...
    def changed(self) -> None: ...
    def process(self, In, display: bool = True) -> dict[str, Any]: ...  # type: ignore[override]
    def saveState(self) -> dict[str, Any]: ...
    def restoreState(self, state: Mapping[str, Any]) -> None: ...
    def hideRow(self, name: str) -> None: ...
    def showRow(self, name: str) -> None: ...

class PlottingCtrlNode(CtrlNode):
    plotTerminal: Terminal
    def __init__(
        self, name: str, ui: Sequence[_UiSpec] | None = None, terminals: Mapping[str, Mapping[str, Any]] | None = None
    ) -> None: ...
    def connected(self, term: Terminal, remote: Terminal) -> None: ...
    def disconnected(self, term: Terminal, remote: Terminal) -> None: ...
    def connectToPlot(self, node: Node) -> None: ...
    def disconnectFromPlot(self, plot) -> None: ...  # `plot` is a PlotItem
    def process(self, In, display: bool = True) -> dict[str, Any]: ...  # type: ignore[override]

def metaArrayWrapper(fn: _F) -> _F: ...
