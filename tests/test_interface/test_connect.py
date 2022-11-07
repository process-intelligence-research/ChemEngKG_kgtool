"""Tests for the interface."""
import os

import pytest

from dbtool.interface import *

chemkg = ChemKG#.dev()  ### defaults to dev_url and default_graph


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
    assert chemkg.fullGraph() is not None


def test_uploadTurtle():
    # will raise Exception on err
    absolute_path = os.path.dirname(__file__)
    file_path = os.path.join(absolute_path, "query2.ttl")

    assert (
        chemkg.uploadTurtle(
            file_path,
        )
        is None
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
        is None
    )


def test_getGraphs():
    assert chemkg.getGraphs() is not None


def test_getGraph():
    assert chemkg.getGraph() is not None


def test_runSparql():
    assert chemkg.runSparql("SELECT * WHERE { ?s ?p ?o } LIMIT 10") is not None


def test_runCypher():
    assert chemkg.runCypher("MATCH (n) RETURN n LIMIT 10") is not None


def test_deleteAll():
    assert chemkg.deleteGraph() is not None


# def test_getGraph():
#     assert chemkg.getGraph("urn:uuid:1") is not None

# def test_deleteGraph():
#     assert chemkg.deleteGraph("urn:uuid:1") is not None
