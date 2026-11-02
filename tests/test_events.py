"""Smoke tests for events."""
import unittest

from energy_grid_ledger import events


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(events, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(events) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
