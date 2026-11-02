import unittest
from energy_grid_ledger import utils_hashing


class TestUtilsHashing(unittest.TestCase):
    def test_hash_bytes_empty(self):
        with self.assertRaises(ValueError):
            utils_hashing.hash_bytes()

    def test_hash_bytes_nonempty(self):
        data = b'Hello, World!'
        result = utils_hashing.hash_bytes(data)
        self.assertIsInstance(result, str)

    def test_hash_bytes_chain_prevhash_none(self):
        new_data = b'New Data'
        with self.assertRaises(ValueError):
            utils_hashing.hash_bytes_chain(None, new_data)

    def test_hash_bytes_chain_prevhash_nonempty(self):
        prev_hash = '1234567890abcdef'
        new_data = b'New Data'
        result = utils_hashing.hash_bytes_chain(prev_hash, new_data)
        self.assertIsInstance(result, str)


if __name__ == '__main__':
    unittest.main()
