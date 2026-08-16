from _typeshed import StrPath
from collections.abc import Mapping
from typing import Any, ClassVar
from xml.dom.minidom import Element

from ..parametertree import Parameter
from .Exporter import Exporter

__all__ = ["SVGExporter"]

class SVGExporter(Exporter):
    Name: ClassVar[str]
    allowCopy: bool
    params: Parameter
    def __init__(self, item) -> None: ...
    def widthChanged(self) -> None: ...
    def heightChanged(self) -> None: ...
    def parameters(self) -> Parameter: ...
    # Returns the encoded document when *toBytes* is set, and None otherwise.
    def export(self, fileName: StrPath | None = None, toBytes: bool = False, copy: bool = False): ...

def generateSvg(item, options: Mapping[str, Any] | None = None) -> str: ...
def _generateItemSvg(
    item, nodes: dict[str, Element] | None = None, root=None, options: Mapping[str, Any] | None = None
) -> tuple[Element, list[Element]] | None: ...
