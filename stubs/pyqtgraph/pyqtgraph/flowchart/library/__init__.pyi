from _typeshed import Incomplete
from collections import OrderedDict
from collections.abc import Sequence

from ..Node import Node
from ..NodeLibrary import NodeLibrary

LIBRARY: NodeLibrary
NODE_LIST: OrderedDict[str, type[Node]]
# Nests one level per path component, with node classes as leaves.
NODE_TREE: OrderedDict[str, Incomplete]

def registerNodeType(nodeClass: type[Node], paths: Sequence[Sequence[str]], override: bool = False) -> None: ...
def getNodeTree() -> OrderedDict[str, Incomplete]: ...
def getNodeType(name: str) -> type[Node]: ...

nodes: list[type[Node]]  # undocumented; leftover loop variable
