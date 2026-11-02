"""Smoke tests for utils_hashing."""
import unittest

from energy_grid_ledger import utils_hashing


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(utils_hashing, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(utils_hashing) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
