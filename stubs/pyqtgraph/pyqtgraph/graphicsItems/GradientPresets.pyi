from typing import Literal, TypedDict
from typing_extensions import TypeAlias

__all__ = ["Gradients"]

# (position along the gradient, RGBA colour)
_GradientTick: TypeAlias = tuple[float, tuple[int, int, int, int]]

class _GradientPreset(TypedDict):
    ticks: list[_GradientTick]
    mode: Literal["rgb", "hsv"]

Gradients: dict[str, _GradientPreset]
