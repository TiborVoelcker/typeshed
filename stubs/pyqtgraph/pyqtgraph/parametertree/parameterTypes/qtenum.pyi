from _typeshed import Incomplete
from collections.abc import Callable
from typing import Any, Literal

from .list import ListParameter

class QtEnumParameter(ListParameter):
    # `enum` is a Qt enum class; `searchObj` is only needed under PyQt5, where it must be the object
    # holding the enum members.
    enum: Incomplete
    searchObj: Incomplete
    enumMap: dict[str, Incomplete]
    def __init__(self, enum, searchObj=..., **opts) -> None: ...
    def setValue(self, value, blockSignal: Callable[..., Any] | None = None) -> None: ...
    def formattedLimits(self) -> dict[str, Incomplete]: ...
    def saveState(self, filter: Literal["user"] | None = None) -> dict[str, Any]: ...
