import pytest
from collections.abc import Iterator
from typing import TYPE_CHECKING

from typehint_rev2 import modifiedTop

def test_top_tuples()->None:
    fruit = 'mango pear apple kiwi banana'.split()
    series:Iterator[tuple[int,str]] = (
        (len(s),s) for s in fruit
    )
    result = modifiedTop(series,3)
    expected = [(6, 'banana'), (5, 'mango'), (5, 'apple')]
    # The typing.TYPE_CHECKING constant is always False at runtime, but type checkers pretend it is True when they are type checking.
    if TYPE_CHECKING:
        #here reveal_type is not a regular function and is not called a runtime, but it is mypy debugging facility.
        reveal_type(series)
        reveal_type(expected)
        reveal_type(result)

    assert result == expected

# An Intentional type Error

def test_top_objects_error()->None:
    series = [object() for _ in range(4)]
    if TYPE_CHECKING:
        reveal_type(series)
    with pytest.raises(TypeError) as excinfo:
        modifiedTop(series,3) # this will result into an error

    assert "'<' not supported in " in str(excinfo.value)