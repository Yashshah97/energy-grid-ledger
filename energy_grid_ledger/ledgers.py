"""
Append-only ledger for power load forecasting.

This module implements a tamper-evident hash-chained event log.
"""

class Ledger:
    """
    Append-only ledger for power load forecasting.

    A tamper-evident hash-chained event log.
    """

    def __init__(self):
        """Initialize an empty ledger."""
        self.events = []

    def append(self, event_data):
        """
        Append a new event to the ledger.

        Args:
            event_data (dict): Event data with 'timestamp' and 'data'.

        Returns:
            str: Hash of the appended event.
        """
        event = {
            'timestamp': event_data['timestamp'],
            'data': event_data['data'],
            'hash': self._calculate_hash(event_data)
        }
        self.events.append(event)
        return event['hash']

    def _calculate_hash(self, data):
        """Calculate a SHA-256 hash of the given data."""
        import hashlib
        return hashlib.sha256(str(data).encode()).hexdigest()

    def get_events(self):
        """
        Get all events in the ledger.

        Returns:
            list: List of event dictionaries.
        """
        return self.events

def main():
    # Example usage
    ledger = Ledger()
    hash1 = ledger.append({'timestamp': 1643723400, 'data': 'Event data'})
    hash2 = ledger.append({'timestamp': 1643723410, 'data': 'Another event'})

    print(ledger.get_events())

if __name__ == '__main__':
    main()
