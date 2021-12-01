from flask import Flask, jsonify
from flask_talisman import Talisman

from utils import metadata, token_count

application = Flask(__name__)
Talisman(application)


@application.route("/")
def index():
    return "Nothing here :)"


@application.route("/contract/")
def contract():
    contract_metadata = metadata.contract_metadata()
    return jsonify(contract_metadata)


@application.route("/token/<int:token_id>")
def token_data(token_id):
    if token_id > 0 and token_id <= 888 and token_id <= token_count.token_count():
        token_metadata = metadata.token_metadata(token_id)
    else:
        token_metadata = {
            "msg": (
                "Item not minted yet. "
                "If you just minted this token, please allow up to 10 minutes."
            )
        }
    return jsonify(token_metadata)


if __name__ == "__main__":
    application.run()
