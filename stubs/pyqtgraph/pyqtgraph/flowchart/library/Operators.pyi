from _typeshed import Incomplete
from typing import Any, ClassVar

from ..Node import Node
from .common import CtrlNode

class UniOpNode(Node):
    fn: str  # the name of the method called on the input
    def __init__(self, name: str, fn: str) -> None: ...
    def process(self, **args) -> dict[str, Any]: ...

class BinOpNode(CtrlNode):
    uiTemplate: Incomplete
    # The name of the method called on input A, or several names to try in order.
    fn: str | tuple[str, ...]
    def __init__(self, name: str, fn: str | tuple[str, ...]) -> None: ...
    def process(self, **args) -> dict[str, Any]: ...  # type: ignore[override]

class AbsNode(UniOpNode):
    nodeName: ClassVar[str]
    def __init__(self, name: str) -> None: ...

class AddNode(BinOpNode):
    nodeName: ClassVar[str]
    def __init__(self, name: str) -> None: ...

class SubtractNode(BinOpNode):
    nodeName: ClassVar[str]
    def __init__(self, name: str) -> None: ...

class MultiplyNode(BinOpNode):
    nodeName: ClassVar[str]
    def __init__(self, name: str) -> None: ...

class DivideNode(BinOpNode):
    nodeName: ClassVar[str]
    def __init__(self, name: str) -> None: ...

class FloorDivideNode(BinOpNode):
    nodeName: ClassVar[str]
    def __init__(self, name: str) -> None: ...
