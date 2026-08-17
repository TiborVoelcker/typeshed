import threading
from _typeshed import Incomplete, StrPath
from collections.abc import Mapping
from typing import Any

from .remoteproxy import ClosedError as ClosedError, NoResultError as NoResultError, RemoteEventHandler

__all__ = ["Process", "QtProcess", "ForkedProcess", "ClosedError", "NoResultError"]

class Process(RemoteEventHandler):
    debug: bool
    proc: Incomplete
    def __init__(
        self,
        name: str | None = None,
        target=None,
        executable: StrPath | None = None,
        copySysPath: bool = True,
        debug: bool = False,
        timeout: float = 20,
        wrapStdout: bool | None = None,
        pyqtapis: Mapping[str, int] | None = None,
    ) -> None: ...
    def join(self, timeout: float = 10) -> None: ...
    def debugMsg(self, msg: str, *args: object) -> None: ...

class ForkedProcess(RemoteEventHandler):
    hasJoined: bool
    isParent: bool
    forkedProxies: dict[str, Incomplete]
    childPid: int | None
    def __init__(
        self, name: str | None = None, target: int = 0, preProxy: Mapping[str, Any] | None = None, randomReseed: bool = True
    ) -> None: ...
    def eventLoop(self) -> None: ...
    def join(self, timeout: float = 10) -> None: ...
    def kill(self) -> None: ...

class RemoteQtEventHandler(RemoteEventHandler):
    def __init__(self, *args, **kwds) -> None: ...
    timer: Incomplete
    def startEventTimer(self) -> None: ...
    # Swallows the base class's `int` return, a genuine LSP violation upstream.
    def processRequests(self) -> None: ...  # type: ignore[override]

class QtProcess(Process):
    def __init__(self, **kwds) -> None: ...
    timer: Incomplete
    def startEventTimer(self) -> None: ...
    def startRequestProcessing(self, interval: float = 0.01) -> None: ...
    def stopRequestProcessing(self) -> None: ...
    # Swallows the base class's `int` return, a genuine LSP violation upstream.
    def processRequests(self) -> None: ...  # type: ignore[override]

class FileForwarder(threading.Thread):
    input: Incomplete
    output: Incomplete
    lock: Incomplete
    daemon: bool
    color: str
    finish: bool
    def __init__(self, input, output, color: str) -> None: ...
    def run(self) -> None: ...
