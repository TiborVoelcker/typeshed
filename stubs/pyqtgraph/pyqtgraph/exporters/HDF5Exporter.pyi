from _typeshed import Incomplete, StrPath
from typing import ClassVar

from ..parametertree import Parameter
from .Exporter import Exporter

__all__ = ["HDF5Exporter"]

HAVE_HDF5: bool  # undocumented

class HDF5Exporter(Exporter):
    Name: ClassVar[str]
    windows: ClassVar[list[Incomplete]]
    allowCopy: bool
    params: Parameter
    def __init__(self, item) -> None: ...
    def parameters(self) -> Parameter: ...
    def export(self, fileName: StrPath | None = None) -> None: ...  # type: ignore[override]
