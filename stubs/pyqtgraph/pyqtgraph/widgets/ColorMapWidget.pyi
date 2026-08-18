from _typeshed import Incomplete
from collections.abc import Callable, Mapping, Sequence
from typing import Any, ClassVar, Literal
from typing_extensions import TypeAlias

from numpy.typing import NDArray

from .. import parametertree as ptree

__all__ = ["ColorMapWidget", "ColorMapParameter"]

# `[(fieldName, {options}), ...]` or a mapping of the same; see `ColorMapParameter.setFields`.
_FieldSpecs: TypeAlias = Mapping[str, Mapping[str, Any]] | Sequence[tuple[str, Mapping[str, Any]]]

class ColorMapWidget(ptree.ParameterTree):
    sigColorMapChanged: Incomplete
    params: ColorMapParameter
    # `ColorMapParameter.setFields` and `.map`, bound in `__init__`
    setFields: Callable[[_FieldSpecs], None]
    map: Callable[..., NDArray[Any]]
    def __init__(self, parent=None) -> None: ...
    def mapChanged(self) -> None: ...
    def widgetGroupInterface(self): ...
    def saveState(self) -> dict[str, Any]: ...
    def restoreState(self, state: Mapping[str, Any]) -> None: ...
    def addColorMap(self, name: str) -> RangeColorMapItem | EnumColorMapItem: ...

class ColorMapParameter(ptree.types.GroupParameter):
    sigColorMapChanged: Incomplete
    fields: dict[str, Mapping[str, Any]]
    def __init__(self) -> None: ...
    def mapChanged(self) -> None: ...
    def addNew(self, name: str) -> RangeColorMapItem | EnumColorMapItem: ...  # type: ignore[override]
    def fieldNames(self) -> list[str]: ...
    def setFields(self, fields: _FieldSpecs) -> None: ...
    # `data` is a numpy record array (or a dict of scalars); the colors are
    # 0-255 ubyte for "byte" and 0.0-1.0 float for "float"
    def map(self, data, mode: Literal["byte", "float"] = "byte") -> NDArray[Any]: ...
    def saveState(self) -> dict[str, Any]: ...  # type: ignore[override]
    def restoreState(self, state: Mapping[str, Any]) -> None: ...  # type: ignore[override]

class RangeColorMapItem(ptree.types.ColorMapParameter):
    mapType: ClassVar[Literal["range"]]
    fieldName: str
    def __init__(self, name: str, opts: Mapping[str, Any]) -> None: ...
    def map(self, data) -> NDArray[Any]: ...

class EnumColorMapItem(ptree.types.GroupParameter):
    mapType: ClassVar[Literal["enum"]]
    fieldName: str
    def __init__(self, name: str, opts: Mapping[str, Any]) -> None: ...
    def map(self, data) -> NDArray[Any]: ...
