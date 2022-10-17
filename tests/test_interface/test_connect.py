"""Tests for the interface."""
import pytest

from dbtool.interface import connect


@pytest.mark.parametrize(
    ("options", "result"),
    [
        ("Test Options 1", 0),
        ("Test Options 2", 0),
        ("Test Options 3", 0),
    ],
)
def test_connect(options, result):
    """Test with parametrization."""
    assert connect(options) == result
