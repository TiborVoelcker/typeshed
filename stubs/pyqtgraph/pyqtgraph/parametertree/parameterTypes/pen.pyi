from _typeshed import Incomplete
from collections.abc import Callable, Mapping, MutableMapping
from typing import Any, Literal

from ...SignalProxy import SignalProxy
from ...widgets.PenPreviewLabel import PenPreviewLabel
from ..Parameter import Parameter
from . import GroupParameterItem
from .basetypes import GroupParameter

class PenParameterItem(GroupParameterItem):
    defaultBtn: Incomplete
    itemWidget: Incomplete
    penLabel: PenPreviewLabel
    def __init__(self, param: Parameter, depth: int) -> None: ...
    def optsChanged(self, param: Parameter, opts: Mapping[str, Any]) -> None: ...
    def treeWidgetChanged(self) -> None: ...
    defaultClicked: Incomplete
    makeDefaultButton: Incomplete
    def valueChanged(self, param: Parameter, val) -> None: ...
    def updateDefaultBtn(self) -> None: ...

def cap_first(s: str) -> str: ...

class PenParameter(GroupParameter):
    itemClass: type[PenParameterItem]
    pen: Incomplete
    valChangingProxy: SignalProxy
    # `**opts` adds "color", "width", "style", "capStyle", "joinStyle" and "cosmetic" to the
    # standard Parameter options. Passing "children" raises KeyError.
    def __init__(self, **opts) -> None: ...
    # `Parameter.setDefault` takes `updatePristineValues` positionally, which
    # `**kwargs` cannot accept — a genuine LSP violation upstream.
    def setDefault(self, val, **kwargs) -> None: ...  # type: ignore[override]
    # `saveState` encodes the pen as (color, width, style, capStyle, joinStyle, cosmetic).
    def saveState(self, filter: Literal["user"] | None = None) -> dict[str, Any]: ...
    def restoreState(
        self,
        state: Mapping[str, Any],
        recursive: bool = True,
        addChildren: bool = True,
        removeChildren: bool = True,
        blockSignals: bool = True,
    ) -> None: ...
    def setValue(self, value, blockSignal: Callable[..., Any] | None = None): ...
    def applyOptsToPen(self, **opts) -> dict[str, Any]: ...
    def setOpts(self, **opts) -> None: ...
    # Accepts anything `pyqtgraph.mkPen` accepts, plus the tuple produced by `saveState`.
    def mkPen(self, *args, **kwargs): ...
    def penPropertySetter(self, p: Parameter, value) -> None: ...
    @staticmethod
    def updateFromPen(param: Parameter | MutableMapping[str, Any], pen) -> None: ...
