"""Tests for the AI Maturity Model."""

import pytest
from blueprint.maturity import (
    MATURITY_LEVELS,
    MATURITY_LABELS,
    MATURITY_COLOURS,
    get_maturity_level,
    classify_maturity,
)
from blueprint.models import MaturityLevel


def test_maturity_levels_count():
    """6 levels: 0-5."""
    assert len(MATURITY_LEVELS) == 6


def test_maturity_levels_order():
    """Levels are ordered 0 through 5."""
    for i, level in enumerate(MATURITY_LEVELS):
        assert level.level == i


def test_maturity_level_names():
    """Verify expected level names."""
    expected = ["No AI", "Spicy Autocomplete", "AI-Assisted", "AI-Integrated", "AI-Native", "Dark Factory"]
    for lvl, name in zip(MATURITY_LEVELS, expected):
        assert lvl.name == name


def test_maturity_level_fields():
    """Every level has description, healthcare_example, and non-empty indicators."""
    for lvl in MATURITY_LEVELS:
        assert isinstance(lvl, MaturityLevel)
        assert lvl.description
        assert lvl.healthcare_example
        assert len(lvl.indicators) > 0


def test_get_maturity_level_valid():
    """get_maturity_level returns correct level for 0-5."""
    for i in range(6):
        lvl = get_maturity_level(i)
        assert lvl.level == i


def test_get_maturity_level_invalid():
    """Out of range raises ValueError."""
    with pytest.raises(ValueError):
        get_maturity_level(-1)
    with pytest.raises(ValueError):
        get_maturity_level(6)


def test_classify_maturity_boundaries():
    """classify_maturity rounds to nearest level."""
    assert classify_maturity(0.0).level == 0
    assert classify_maturity(0.4).level == 0
    assert classify_maturity(0.5).level == 0  # round(0.5) = 0 in Python (banker's rounding)
    assert classify_maturity(1.0).level == 1
    assert classify_maturity(2.5).level == 2  # banker's rounding
    assert classify_maturity(4.6).level == 5
    assert classify_maturity(5.0).level == 5


def test_classify_maturity_clamp():
    """Scores outside 0-5 are clamped."""
    assert classify_maturity(-1.0).level == 0
    assert classify_maturity(10.0).level == 5


def test_maturity_labels():
    """MATURITY_LABELS has all 6 levels."""
    assert len(MATURITY_LABELS) == 6
    for i in range(6):
        assert i in MATURITY_LABELS


def test_maturity_colours():
    """MATURITY_COLOURS has all 6 levels."""
    assert len(MATURITY_COLOURS) == 6
    for i in range(6):
        assert i in MATURITY_COLOURS
