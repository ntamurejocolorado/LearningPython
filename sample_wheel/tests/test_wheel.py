#!/usr/bin/env python

"""Tests for sample_wheel package."""

import sample_wheel

def test_package_publishes_version_info():
    """Tests that the sample_wheel publishes the current version"""

    assert hasattr(sample_wheel, '__version__')