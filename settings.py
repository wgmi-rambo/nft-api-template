import logging
import os
from pathlib import Path

FLASK_ENV = os.environ.get("FLASK_ENV", "production")
INFURA_URL = os.environ.get("INFURA_URL")
CONTRACT_ADDRESS = os.environ.get("CONTRACT_ADDRESS")

BASE_DIR = Path(__file__).resolve(strict=True).parent
DATA_DIR = os.path.join(BASE_DIR, "data")
METADATA_DIR = os.path.join(DATA_DIR, "metadata")

TOKEN_COUNT_FILEPATH = os.path.join(DATA_DIR, "token_count.txt")
CONTRACT_METADATA_FILEPATH = os.path.join(DATA_DIR, "metadata", "contract.json")
TOKENS_METADATA_FILEPATH = os.path.join(DATA_DIR, "metadata", "tokens.json")


# Setup logging #
logging.basicConfig(
    format="%(asctime)s:%(levelname)s - %(name)s:%(message)s",
    datefmt="%m/%d %I:%M:%S %p",
    level=logging.INFO,
)

if FLASK_ENV == "development":
    logging.basicConfig(format="%(levelname)s %(name)s: %(message)s", level=logging.WARNING)
