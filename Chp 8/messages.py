from typing import Optional


def word_count(count: int, word: str, plural: Optional[str] = None) -> str:
    if count == 1:
        return f'1 {word}'
    count_str = str(count) if count > 1 else 'no'
    complement = plural if plural else word + 's'
    return f'{count_str} {complement}'
