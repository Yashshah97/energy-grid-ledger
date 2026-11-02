"""
Utility functions for hashing and cryptographic operations.

This module provides utility functions for hashing and cryptographic operations,
specifically designed to support the append-only ledger implementation.
"""

import hashlib
from typing import Optional, bytes


def hash_bytes(data: Optional[bytes] = None) -> str:
    """
    Compute the SHA-256 hash of the given data.

    Args:
        data (Optional[bytes]): The input data to be hashed. Defaults to None.

    Returns:
        str: The hexadecimal representation of the computed hash.
    """
    if data is not None:
        return hashlib.sha256(data).hexdigest()
    else:
        raise ValueError("Input data cannot be empty")


def hash_bytes_chain(prev_hash: Optional[str], new_data: bytes) -> str:
    """
    Compute the SHA-256 hash of the given new data, prepending the previous
    hash as additional input.

    Args:
        prev_hash (Optional[str]): The hexadecimal representation of the previous
            hash. Defaults to None.
        new_data (bytes): The new data to be hashed.

    Returns:
        str: The hexadecimal representation of the computed hash.
    """
    if prev_hash is not None:
        return hashlib.sha256((prev_hash.encode() + new_data).encode()).hexdigest()
    else:
        raise ValueError("Previous hash cannot be empty")
