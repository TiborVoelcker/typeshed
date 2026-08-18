from collections.abc import Sequence
from typing import Any, Literal
from typing_extensions import TypeAlias

import numpy as np
from numpy.typing import ArrayLike, DTypeLike, NDArray

from ...metaarray import MetaArray

# These functions accept either a plain array or a MetaArray, and return the
# same flavour they were given.
_ArrayOrMeta: TypeAlias = NDArray[Any] | MetaArray

def downsample(
    data: _ArrayOrMeta,
    n: int | Sequence[int],
    axis: int | Sequence[int] = 0,
    xvals: Literal["subsample", "downsample"] = "subsample",
) -> _ArrayOrMeta: ...

# `b` and `a` are the numerator/denominator coefficients of a linear filter.
def applyFilter(data: _ArrayOrMeta, b: ArrayLike, a: ArrayLike, padding: int = 100, bidir: bool = True) -> _ArrayOrMeta: ...
def besselFilter(
    data: _ArrayOrMeta, cutoff: float, order: int = 1, dt: float | None = None, btype: str = "low", bidir: bool = True
) -> _ArrayOrMeta: ...

# `order` is accepted but unused; the order is computed from the passband and stopband specs.
def butterworthFilter(
    data: _ArrayOrMeta,
    wPass: float,
    wStop: float | None = None,
    gPass: float = 2.0,
    gStop: float = 20.0,
    order: int = 1,
    dt: float | None = None,
    btype: str = "low",
    bidir: bool = True,
) -> _ArrayOrMeta: ...
def rollingSum(data: NDArray[Any], n: int) -> NDArray[Any]: ...
def mode(data: NDArray[Any], bins: int | None = None) -> np.float64: ...
def modeFilter(data: _ArrayOrMeta, window: int = 500, step: int | None = None, bins: int | None = None) -> _ArrayOrMeta: ...
def denoise(data: _ArrayOrMeta, radius: int = 2, threshold: float = 4) -> _ArrayOrMeta: ...
def adaptiveDetrend(data: _ArrayOrMeta, x: NDArray[Any] | None = None, threshold: float = 3.0) -> _ArrayOrMeta: ...
def histogramDetrend(
    data: _ArrayOrMeta, window: int = 500, bins: int = 50, threshold: float = 3.0, offsetOnly: bool = False
) -> _ArrayOrMeta: ...

# Each element is either a record array or a `(name, dtype, data)` tuple; a
# `None` dtype is guessed with `suggestDType`.
def concatenateColumns(data: Sequence[NDArray[Any] | tuple[str, DTypeLike | None, ArrayLike]]) -> NDArray[np.void]: ...
def suggestDType(x: object) -> np.dtype[Any] | type[object]: ...
def removePeriodic(
    data: _ArrayOrMeta, f0: float = 60.0, dt: float | None = None, harmonics: int = 10, samples: int = 4
) -> _ArrayOrMeta: ...
