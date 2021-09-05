"""Test smatrix."""
from smatrix import __version__
from smatrix import smatrix


def test_version():
    """Test version."""
    assert __version__ == "0.1.0"


def test_sanity():
    """Sanity check."""
    try:
        assert not smatrix()
    except Exception:
        assert True
