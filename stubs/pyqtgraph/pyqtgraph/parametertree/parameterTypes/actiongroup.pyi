from _typeshed import Incomplete
from collections.abc import Mapping
from typing import Any
from typing_extensions import deprecated

from ..Parameter import Parameter
from .action import ParameterControlledButton
from .basetypes import GroupParameter, GroupParameterItem

class ActionGroupParameterItem(GroupParameterItem):
    itemWidget: Incomplete
    button: ParameterControlledButton
    def __init__(self, param: Parameter, depth: int) -> None: ...
    def treeWidgetChanged(self) -> None: ...
    def optsChanged(self, param: Parameter, opts: Mapping[str, Any]) -> None: ...

class ActionGroupParameter(GroupParameter):
    itemClass: type[ActionGroupParameterItem]
    sigActivated: Incomplete
    def __init__(self, **opts) -> None: ...
    def activate(self) -> None: ...
    # `**opts` accepts the same keys as `ParameterControlledButton.settableAttributes`.
    def setButtonOpts(self, **opts) -> None: ...

@deprecated("`ActionGroup` is deprecated; use `ActionGroupParameter` instead.")
class ActionGroup(ActionGroupParameter):
    sigActivated: Incomplete
    def __init__(self, **opts) -> None: ...
    def activate(self) -> None: ...
