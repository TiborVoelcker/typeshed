# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

import re
from _typeshed import Incomplete
from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import Any, Literal, TypeVar, overload
from typing_extensions import Self, TypeAlias

import numpy as np
from numpy.typing import ArrayLike, DTypeLike, NDArray

from .Qt import QtGui  # type: ignore[import-not-found, import-untyped]  # pyright: ignore[reportMissingImports]

__all__ = [
    "siScale",
    "siFormat",
    "siParse",
    "siEval",
    "siApply",
    "Color",
    "mkColor",
    "mkBrush",
    "mkPen",
    "hsvColor",
    "CIELabColor",
    "colorCIELab",
    "colorDistance",
    "colorTuple",
    "colorStr",
    "intColor",
    "glColor",
    "makeArrowPath",
    "eq",
    "affineSliceCoords",
    "affineSlice",
    "interweaveArrays",
    "interpolateArray",
    "subArray",
    "transformToArray",
    "transformCoordinates",
    "solve3DTransform",
    "solveBilinearTransform",
    "clip_scalar",
    "clip_array",
    "rescaleData",
    "applyLookupTable",
    "makeRGBA",
    "makeARGB",
    "makeQImage",
    "imageToArray",
    "colorToAlpha",
    "gaussianFilter",
    "downsample",
    "arrayToQPath",
    "isocurve",
    "traceImage",
    "isosurface",
    "invertQTransform",
    "pseudoScatter",
    "toposort",
    "disconnect",
    "SignalBlock",
]

_T = TypeVar("_T")

# Everything `mkColor` accepts. `QColor` and the Qt global colors are part of
# this union at runtime, but `pyqtgraph.Qt` is not stubbed here (see README.md),
# so they are covered by the trailing `Incomplete`.
_ColorArg: TypeAlias = (
    str  # a single-letter name from `Colors`, an SVG keyword, or "#RGB"/"#RGBA"/"#RRGGBB"/"#RRGGBBAA"
    | int  # index into the `intColor` palette
    | float  # greyscale, 0.0-1.0
    | tuple[int, int]  # (index, hues), as passed to `intColor`
    | tuple[int, int, int]
    | tuple[int, int, int, int]
    | Sequence[int]
    | Incomplete  # QColor, Qt.GlobalColor
)

Colors: dict[str, Incomplete]  # undocumented
SI_PREFIXES: str  # undocumented
SI_PREFIXES_ASCII: str  # undocumented
SI_PREFIX_EXPONENTS: dict[str, int]  # undocumented
FLOAT_REGEX: re.Pattern[str]  # undocumented
INT_REGEX: re.Pattern[str]  # undocumented

def siScale(x: float, minVal: float = 1e-25, allowUnicode: bool = True) -> tuple[float, str]: ...
def siFormat(
    x: float,
    precision: int = 3,
    suffix: str = "",
    space: bool | str = True,
    error: float | None = None,
    minVal: float = 1e-25,
    allowUnicode: bool = True,
) -> str: ...
def siParse(s: str, regex: re.Pattern[str] = ..., suffix: str | None = None) -> tuple[str, str, str]: ...
@overload
def siEval(s: str, typ: Callable[[str], _T], regex: re.Pattern[str] = ..., suffix: str | None = None) -> _T: ...
@overload
def siEval(s: str, typ: Callable[[str], float] = ..., regex: re.Pattern[str] = ..., suffix: str | None = None) -> float: ...
def siApply(val: _T, siprefix: str) -> _T: ...

class Color(QtGui.QColor):
    def __init__(self, *args: _ColorArg) -> None: ...
    def glColor(self) -> tuple[float, float, float, float]: ...
    def __getitem__(self, ind: int) -> int: ...

def mkColor(*args: _ColorArg): ...
def mkBrush(*args: _ColorArg, **kwds: _ColorArg): ...
def mkPen(*args, **kargs): ...
def hsvColor(hue: float, sat: float = 1.0, val: float = 1.0, alpha: float = 1.0): ...
def CIELabColor(L: float, a: float, b: float, alpha: float = 1.0): ...
def colorCIELab(qcol) -> NDArray[np.float64]: ...
def colorDistance(colors: Sequence[Incomplete], metric: str = "CIE76") -> NDArray[np.float64]: ...
def colorTuple(c) -> tuple[int, int, int, int]: ...
def colorStr(c) -> str: ...
def intColor(
    index: int,
    hues: int = 9,
    values: int = 1,
    maxValue: int = 255,
    minValue: int = 150,
    maxHue: int = 360,
    minHue: int = 0,
    sat: int = 255,
    alpha: int = 255,
): ...
def glColor(*args: _ColorArg, **kargs: _ColorArg) -> tuple[float, float, float, float]: ...
def makeArrowPath(
    headLen: float = 20,
    headWidth: float | None = None,
    tipAngle: float = 20,
    tailLen: float = 20,
    tailWidth: float = 3,
    baseAngle: float = 0,
): ...
def eq(a: object, b: object) -> bool: ...
def affineSliceCoords(
    shape: Sequence[int], origin: ArrayLike, vectors: ArrayLike, axes: Sequence[int]
) -> NDArray[np.float64]: ...
@overload
def affineSlice(
    data: NDArray[Any],
    shape: Sequence[int],
    origin: ArrayLike,
    vectors: ArrayLike,
    axes: Sequence[int],
    order: int = 1,
    *,
    returnCoords: Literal[True],
    **kargs,
) -> tuple[NDArray[Any], NDArray[np.float64]]: ...
@overload
def affineSlice(
    data: NDArray[Any],
    shape: Sequence[int],
    origin: ArrayLike,
    vectors: ArrayLike,
    axes: Sequence[int],
    order: int = 1,
    returnCoords: Literal[False] = False,
    **kargs,
) -> NDArray[Any]: ...
def interweaveArrays(*args: NDArray[Any]) -> NDArray[Any]: ...
def interpolateArray(data: NDArray[Any], x: ArrayLike, default: float = 0.0, order: int = 1) -> NDArray[Any]: ...
def subArray(data: ArrayLike, offset: int, shape: Sequence[int], stride: Sequence[int]) -> NDArray[Any]: ...
def transformToArray(tr) -> NDArray[np.float64]: ...
def transformCoordinates(tr, coords: NDArray[Any], transpose: bool = False) -> NDArray[Any]: ...
def solve3DTransform(points1: ArrayLike, points2: ArrayLike) -> NDArray[np.float64]: ...
def solveBilinearTransform(points1: ArrayLike, points2: ArrayLike) -> NDArray[np.float64]: ...
def clip_scalar(val: _T, vmin: _T, vmax: _T) -> _T: ...

# Replaced by `numpy.clip` when running against numpy >= 1.25
clip_array: Incomplete

def rescaleData(
    data: NDArray[Any], scale: float, offset: float, dtype: DTypeLike | None = None, clip: tuple[float, float] | None = None
) -> NDArray[Any]: ...
def applyLookupTable(data: NDArray[Any], lut: NDArray[Any]) -> NDArray[Any]: ...
def makeRGBA(*args, **kwds) -> tuple[NDArray[np.ubyte], bool]: ...
def makeARGB(
    data: NDArray[Any],
    lut: NDArray[Any] | None = None,
    levels: ArrayLike | None = None,
    scale: float | None = None,
    useRGBA: bool = False,
    maskNans: bool = True,
    output: NDArray[Any] | None = None,
) -> tuple[NDArray[np.ubyte], bool]: ...
def makeQImage(imgData: NDArray[Any], alpha: bool | None = None, copy: bool = True, transpose: bool = True): ...
def imageToArray(img, copy: bool = False, transpose: bool = True) -> NDArray[np.ubyte]: ...
def colorToAlpha(data: NDArray[Any], color: ArrayLike) -> NDArray[np.ubyte]: ...
def gaussianFilter(data: NDArray[Any], sigma: float | Sequence[float]) -> NDArray[Any]: ...
def downsample(
    data: NDArray[Any], n: int, axis: int | Sequence[int] = 0, xvals: str = "subsample"
): ...  # ndarray, or MetaArray when given one
def arrayToQPath(x: NDArray[Any], y: NDArray[Any], connect: str | NDArray[Any] = "all", finiteCheck: bool = True): ...
@overload
def isocurve(data: NDArray[Any], level: float, connected: bool = False, extendToEdge: bool = False, *, path: Literal[True]): ...
@overload
def isocurve(
    data: NDArray[Any], level: float, connected: bool = False, extendToEdge: bool = False, path: Literal[False] = False
) -> list[Incomplete]: ...
def traceImage(image: NDArray[Any], values: ArrayLike, smooth: float = 0.5) -> list[Incomplete]: ...
def isosurface(data: NDArray[Any], level: float) -> tuple[NDArray[np.float32], NDArray[np.uint32]]: ...
def invertQTransform(tr): ...
def pseudoScatter(
    data: NDArray[Any],
    spacing: float | None = None,
    shuffle: bool = True,
    bidir: bool = False,
    method: Literal["exact", "histogram"] = "exact",
) -> NDArray[np.float64]: ...
def toposort(
    deps: Mapping[_T, Iterable[_T]],
    nodes: Iterable[_T] | None = None,
    seen: set[_T] | None = None,
    stack: list[_T] | None = None,
    depth: int = 0,
) -> list[_T]: ...
def disconnect(signal, slot) -> bool: ...

class SignalBlock:
    signal: Incomplete
    slot: Incomplete
    def __init__(self, signal, slot) -> None: ...
    reconnect: bool
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: object) -> None: ...
