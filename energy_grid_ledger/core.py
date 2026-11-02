"""
Energy Grid Ledger Core Module.

This module contains the core logic for the Energy Grid Ledger. It provides classes and functions for creating,
manipulating, and validating events in the ledger.
"""

import hashlib
from typing import List, Dict, Any

class Event:
    """Represents a single event in the ledger."""

    def __init__(self, timestamp: float, data: Dict[str, Any]):
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    @staticmethod
    def calculate_hash(data: Dict[str, Any]) -> str:
        """Calculates a SHA-256 hash of the event's data."""
        return hashlib.sha256(str(data).encode()).hexdigest()

class Ledger:
    """Represents the append-only ledger."""

    def __init__(self):
        self.events = []

    def add_event(self, event: Event) -> None:
        """Adds an event to the ledger and updates hashes accordingly."""
        self.events.append(event)
        for i in range(len(self.events) - 1, 0, -1):
            self.events[i].hash = self.calculate_hash(i)

    @staticmethod
    def calculate_hash(index: int) -> str:
        """Calculates a SHA-256 hash of the event at the given index."""
        data = {
            'index': index,
            'timestamp': self.events[index].timestamp,
            'data': self.events[index].data
        }
        return hashlib.sha256(str(data).encode()).hexdigest()

    def get_event(self, index: int) -> Event:
        """Returns the event at the given index."""
        return self.events[index]

def create_event(timestamp: float, data: Dict[str, Any]) -> Event:
    """
    Creates a new event.

    Args:
        timestamp (float): The timestamp of the event.
        data (Dict[str, Any]): The data associated with the event.

    Returns:
        Event: The created event.
    """
    return Event(timestamp, data)

def create_ledger() -> Ledger:
    """Creates a new ledger."""
    return Ledger()
