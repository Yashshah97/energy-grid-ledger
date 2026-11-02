"""
Hash-chained log implementation.

This module provides a basic append-only ledger with hash-chaining for tamper-evidence.
"""

class HashChain:
    """
    A hash-chained log of events.

    Each event is represented as a string, and each new event's hash includes the previous event's hash.
    """

    def __init__(self):
        self.log = []
        self.hash = None

    def append(self, event: str) -> str:
        """
        Append an event to the log and update the hash.

        Args:
            event (str): The new event to append.

        Returns:
            str: The updated hash.
        """
        if not isinstance(event, str):
            raise ValueError("Event must be a string")

        new_hash = self._hash(self.log + [event])
        self.log.append((new_hash, event))
        return new_hash

    def _hash(self, data: list[str]) -> str:
        """
        Compute the hash of a list of strings.

        Args:
            data (list[str]): The list of strings to hash.

        Returns:
            str: The hexadecimal representation of the SHA-256 hash.
        """
        import hashlib
        m = hashlib.sha256()
        for s in data:
            m.update(s.encode())
        return m.hexdigest()

    def get_log(self) -> list[tuple[str, str]]:
        """
        Get the current log.

        Returns:
            list[tuple[str, str]]: The current log as a list of tuples containing the hash and event.
        """
        return self.log

def test_hash_chain():
    ledger = HashChain()
    assert ledger.append("Event 1") == "a" * 64
    assert ledger.get_log() == [("a" * 64, "Event 1")]
    new_hash = ledger.append("Event 2")
    assert len(ledger.get_log()) == 2
    assert ledger.get_log()[1][0] == new_hash

if __name__ == "__main__":
    test_hash_chain()
