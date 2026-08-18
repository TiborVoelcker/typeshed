import contextlib
import inspect
from collections.abc import Callable, Generator, Iterable, Mapping, Sequence
from typing import Any, ClassVar, Literal

from .Parameter import Parameter

class PARAM_UNSET: ...

class RunOptions:
    ON_ACTION: ClassVar[Literal["action"]]
    ON_CHANGED: ClassVar[Literal["changed"]]
    ON_CHANGING: ClassVar[Literal["changing"]]

class InteractiveFunction:
    __qualname__: str
    parameters: dict[str, Parameter]
    extra: dict[str, Any]
    function: Callable[..., Any]
    closures: dict[str, Callable[[], Any]]
    parametersNeedRunKwargs: bool
    parameterCache: dict[str, Any]
    def __init__(
        self, function: Callable[..., Any], *, closures: Mapping[str, Callable[[], Any]] | None = None, **extra
    ) -> None: ...
    def __call__(self, **kwargs): ...
    def updateCachedParameterValues(self, param: Parameter, value) -> None: ...
    def hookupParameters(self, params: Iterable[Parameter] | None = None, clearOld: bool = True) -> None: ...
    def removeParameters(self, clearCache: bool = True) -> None: ...
    def runFromChangedOrChanging(self, param: Parameter, value): ...
    def runFromAction(self, **kwargs): ...
    def disconnect(self) -> bool: ...
    def setDisconnected(self, disconnected: bool) -> bool: ...
    def reconnect(self) -> bool: ...

class Interactor:
    runOptions: str | Sequence[str]
    parent: Parameter | None
    titleFormat: str | Callable[[str], str] | None
    nest: bool
    existOk: bool
    runActionTemplate: dict[str, Any]
    # `**kwargs` accepts the same keys as `setOpts`.
    def __init__(self, **kwargs) -> None: ...
    # `**opts` accepts: runOptions, parent, titleFormat, nest, existOk, runActionTemplate.
    def setOpts(self, **opts) -> dict[str, Any]: ...
    @contextlib.contextmanager
    def optsContext(self, **opts) -> Generator[None]: ...
    def interact(
        self,
        function: Callable[..., Any] | InteractiveFunction,
        *,
        ignores: Sequence[str] | None = None,
        runOptions: str | Sequence[str] | type[PARAM_UNSET] = ...,
        parent: Parameter | None | type[PARAM_UNSET] = ...,
        titleFormat: str | Callable[[str], str] | None | type[PARAM_UNSET] = ...,
        nest: bool | type[PARAM_UNSET] = ...,
        runActionTemplate: Mapping[str, Any] | type[PARAM_UNSET] = ...,
        existOk: bool | type[PARAM_UNSET] = ...,
        **overrides,
    ) -> Parameter | list[Parameter]: ...
    # `__call__` is `functools.wraps(interact)`-ed, so it has the same signature.
    def __call__(
        self,
        function: Callable[..., Any] | InteractiveFunction,
        *,
        ignores: Sequence[str] | None = None,
        runOptions: str | Sequence[str] | type[PARAM_UNSET] = ...,
        parent: Parameter | None | type[PARAM_UNSET] = ...,
        titleFormat: str | Callable[[str], str] | None | type[PARAM_UNSET] = ...,
        nest: bool | type[PARAM_UNSET] = ...,
        runActionTemplate: Mapping[str, Any] | type[PARAM_UNSET] = ...,
        existOk: bool | type[PARAM_UNSET] = ...,
        **overrides,
    ) -> Parameter | list[Parameter]: ...
    def decorate(self, **kwargs) -> Callable[[Callable[..., Any] | InteractiveFunction], InteractiveFunction]: ...
    def resolveAndHookupParameterChild(
        self, functionGroup: Parameter | None, childOpts: Mapping[str, Any], interactiveFunction: InteractiveFunction
    ) -> Parameter: ...
    def functionToParameterDict(self, function: Callable[..., Any], **overrides) -> dict[str, Any]: ...
    def createFunctionParameter(
        self, name: str, signatureParameter: inspect.Parameter | None, overridesInfo
    ) -> dict[str, Any]: ...
    def getOpts(self) -> dict[str, Any]: ...

interact: Interactor
