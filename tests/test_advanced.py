# -*- coding: utf-8 -*-

from .context import sample

import unittest
from unittest import mock


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(sample.hmm())
        
    def test_thought_with_mocking(self):
        with mock.patch("sample.helpers.get_answer", return_value=False):
            result = sample.hmm()
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
