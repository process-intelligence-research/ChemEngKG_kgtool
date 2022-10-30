"""Tests for the interface."""
import pytest

from dbtool.interface import *


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


def test_fullGraph():
    assert fullGraph() is not None


def test_uploadTurtle():
    # will raise Exception on err
    assert (
        uploadTurtle(
            "/Users/marvinkleinpass/Developer/TU_DELFT/dbtool/tests/test_interface/query2.ttl"
        )
        is None
    )


def test_uploadFile():
    # will raise Exception on err
    assert (
        uploadFile(
            "/Users/marvinkleinpass/Developer/TU_DELFT/dbtool/tests/test_interface/query2.ttl",
            "query22_DOI",
        )
        is None
    )
