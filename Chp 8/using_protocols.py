from typing import TypeVar

from mul_protocol import SupportsMul

MulT = TypeVar('MulT', bound=SupportsMul)


def double(x: MulT) -> MulT:
    return x * 2


