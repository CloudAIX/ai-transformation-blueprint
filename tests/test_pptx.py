"""Tests for PPTX generation."""

import tempfile
from pathlib import Path

from blueprint.examples import create_example_blueprint
from blueprint.pptx_gen import generate_blueprint_pptx


def test_pptx_generates():
    """PPTX generation completes without error."""
    bp = create_example_blueprint()
    with tempfile.TemporaryDirectory() as td:
        out = Path(td) / "test_blueprint.pptx"
        result = generate_blueprint_pptx(bp, out)
        assert result.exists()
        assert result.stat().st_size > 0


def test_pptx_slide_count():
    """PPTX has expected number of slides (13 = 1 title + 2 maturity + 5 dept + 1 roles + 1 skills + 1 change + 1 timeline + 1 ROI)."""
    bp = create_example_blueprint()
    with tempfile.TemporaryDirectory() as td:
        out = Path(td) / "test_blueprint.pptx"
        generate_blueprint_pptx(bp, out)
        from pptx import Presentation
        prs = Presentation(str(out))
        assert len(prs.slides) == 13


def test_pptx_returns_path():
    """generate_blueprint_pptx returns the output path."""
    bp = create_example_blueprint()
    with tempfile.TemporaryDirectory() as td:
        out = Path(td) / "test_blueprint.pptx"
        result = generate_blueprint_pptx(bp, out)
        assert isinstance(result, Path)
        assert result == out
