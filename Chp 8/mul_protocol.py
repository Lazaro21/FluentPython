from typing import Protocol, Any


class SupportsMul(Protocol):
    def __mul__(self, other: Any) -> bool: ...
