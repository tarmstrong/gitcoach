#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_gitcoach
----------------------------------

Tests for `gitcoach` module.
"""

from nose.tools import eq_
from gitcoach import coach


def test_find_relevant_correlations():
    cors = {('f1', 'f2'): 1, ('f2', 'f3'): 2}
    expected_result = {
        'f1': 1, 'f3': 2,
    }
    result = coach.find_relevant_correlations(cors, 'f2')
    eq_(result, expected_result)


def test_normalize_correlations():
    cors = {'f2': 1, 'f3': 2}
    expected_result = {
        'f2': 0.25, 'f3': 0.5,
    }
    result = coach.normalize_correlations(cors, 4)
    eq_(result, expected_result)


def test_filter_threshold():
    cors = {'f1': 0.2, 'f2': 0.3, 'f3': 0.7, 'f4': 0.95}
    expected_result = {
        'f4': 0.95,
    }
    result = coach.filter_threshold(cors, 0.9)
    eq_(result, expected_result)


def test_filter_threshold_equal():
    '''Ensure filter_threshold doesn't reject correlations when they are
    on the threshold.'''
    cors = {'f1': 0.2, 'f2': 0.3, 'f3': 0.7, 'f4': 0.95}
    expected_result = {
        'f4': 0.95,
    }
    result = coach.filter_threshold(cors, 0.95)
    eq_(result, expected_result)


def test_filter_threshold_lots():
    cors = {'f1': 0.2, 'f2': 0.3, 'f3': 0.7, 'f4': 0.95}
    expected_result = {
        'f2': 0.3, 'f3': 0.7, 'f4': 0.95
    }
    result = coach.filter_threshold(cors, 0.21)
    eq_(result, expected_result)
