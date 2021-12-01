"""
Retreive metadata. Uses memoization to reduce i/o.
"""

import json
import logging
from typing import Dict, List

import settings

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def memoize(f):
    memo = {}
    x = 1

    def helper():
        if x not in memo:
            memo[x] = f()
        return memo[x]

    return helper


def memoize_w_args(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


@memoize
def contract_metadata() -> Dict:
    contract_json = {}

    with open(settings.CONTRACT_METADATA_FILEPATH, "r") as contract_metadata_file:
        contract_json = json.load(contract_metadata_file)

    logger.debug("Contract metadata: %s" % contract_json)

    return contract_json


@memoize
def _all_token_metadata() -> List:
    tokens_json = []

    with open(settings.TOKENS_METADATA_FILEPATH, "r") as tokens_metadata_file:
        tokens_json = json.load(tokens_metadata_file)

    return tokens_json


@memoize_w_args
def token_metadata(token_id: int) -> Dict:
    all_token_data = _all_token_metadata()

    return all_token_data[token_id - 1]
