"""Tests for the interface."""
import os

import pytest

from kgtool.interface import *

chemkg = ChemKG.dev()  # .dev()  ### defaults to dev_url and default_graph


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


def test_uploadTurtle():
    # will raise Exception on err
    absolute_path = os.path.dirname(__file__)
    file_path = os.path.join(absolute_path, "query2.ttl")

    assert (
        chemkg.uploadTurtle(
            file_path,
        )
        is not None
    )


def test_uploadFile():
    # will raise Exception on err
    absolute_path = os.path.dirname(__file__)
    file_path = os.path.join(absolute_path, "query2.ttl")

    assert (
        chemkg.uploadFile(
            file_path,
            "query22_DOI",
        )
        is not None
    )


def test_getGraphs():
    assert chemkg.getGraphs() is not None


def test_getGraph():
    assert chemkg.getGraph() is not None


def test_runSparql():
    assert chemkg.runSparql("SELECT * WHERE { ?s ?p ?o } LIMIT 10") is not None
