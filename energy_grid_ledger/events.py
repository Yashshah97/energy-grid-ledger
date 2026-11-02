"""
Module for representing individual events within the energy grid append-only ledger.

Each event in this module is immutable and has a unique identifier.
"""

class Event:
    """Represents an event in the energy grid append-only ledger."""
    
    def __init__(self, id: str, timestamp: float, data: dict):
        """
        Initializes an Event instance.

        Args:
            id (str): Unique identifier for this event.
            timestamp (float): Timestamp when this event occurred.
            data (dict): Data associated with this event.
        """
        self.id = id
        self.timestamp = timestamp
        self.data = data

    def __repr__(self):
        """Returns a string representation of the Event instance."""
        return f"Event(id='{self.id}', timestamp={self.timestamp}, data={self.data})"

    def __eq__(self, other):
        """
        Checks if this Event instance is equal to another.

        Args:
            other (Event): The Event instance to compare with.

        Returns:
            bool: True if both instances are equal, False otherwise.
        """
        return isinstance(other, Event) and self.id == other.id and self.timestamp == other.timestamp and self.data == other.data

    def __hash__(self):
        """Returns the hash value of this Event instance."""
        return hash((self.id, self.timestamp, self.data))
