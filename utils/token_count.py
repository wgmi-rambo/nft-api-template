"""
Method for retreiving the token count.

Uses the infura.io API.


Usage:

```python
# Set contract and abi
ABI_FILEPATH = os.path.join(settings.DATA_DIR, "abi.json")
CONTRACT = settings.CONTRACT_ADDRESS

ABI = ""
with open(ABI_FILEPATH, "r") as abi_file:
    ABI = abi_file.read()

total = token_count(CONTRACT, ABI)

logger.info("Current token_count: %s" % total)
```
"""

import json
import logging
import os
from datetime import datetime, timedelta

from web3 import Web3  # Connect to INFURA HTTP End Point

import settings

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def _get_live_token_count(address, abi) -> int:
    """Request contract call `totalSupply` using infura"""
    logger.info("Getting live token count.")

    token_count = 0

    try:
        # Check Connection
        w3 = Web3(Web3.HTTPProvider(settings.INFURA_URL))

        abi = json.loads(abi)
        address = Web3.toChecksumAddress(address)
        contract = w3.eth.contract(address=address, abi=abi)

        # Get token_count
        token_count = contract.functions.totalSupply().call()
    except Exception:
        logger.exception("Failed to get live token count.")

    return token_count


def _get_stored_token_count() -> int:
    logger.info("Getting stored token count.")

    token_count = 0

    try:
        with open(settings.TOKEN_COUNT_FILEPATH, "r") as token_count_file:
            _token_count = token_count_file.read()
            token_count = int(_token_count)
    except Exception:
        logger.exception("_get_stored_token_count() failed.")

    return token_count


def _store_token_count(token_count: int) -> None:
    logger.info("Storing token count (%s)." % token_count)
    try:
        with open(settings.TOKEN_COUNT_FILEPATH, "w") as token_count_file:
            token_count_file.write(str(token_count))
    except Exception:
        logger.exception("_store_token_count(%s) failed." % token_count)


def _is_stored_count_expired(now, filepath) -> bool:

    try:
        file_creation_time = os.path.getmtime(filepath)
    except Exception:
        logger.info("Stored token count not found.")
        return True

    now_minus_5 = (now - timedelta(minutes=5)).timestamp()

    if now_minus_5 < file_creation_time:
        logger.info("Stored token count is valid.")
        return False

    logger.info("Stored token count is expired.")

    return True


def _token_count(address, abi) -> int:
    """
    Takes a contract address and contract abi and return an int.
    """

    if _is_stored_count_expired(datetime.now(), settings.TOKEN_COUNT_FILEPATH):
        token_count = _get_live_token_count(address, abi)

        if token_count is not None:
            token_count = int(token_count)
            _store_token_count(token_count)
    else:
        token_count = _get_stored_token_count()

    return token_count


# Set contract and abi
ABI_FILEPATH = os.path.join(settings.DATA_DIR, "abi.json")
CONTRACT = settings.CONTRACT_ADDRESS

ABI = ""
with open(ABI_FILEPATH, "r") as abi_file:
    ABI = abi_file.read()


def token_count() -> int:
    """Overriding with hard-coded int to release all tokens' metadata."""

    # return _token_count(CONTRACT, ABI)
    return 8592
