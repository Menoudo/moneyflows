# Import flask dependencies
from flask import Blueprint, jsonify, request
import json

# Import the database object from the main app module
from app import db

# Import module models (i.e. User)
from app.mod_ifttt_webhook.models import Messages

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_ifttt_webhook = Blueprint('ifttt_webhook', __name__, url_prefix='/api', subdomain='')

# module token
__TOKEN__ = 'ww123'


class JsonSerializable(object):
    def toJson(self):
        return self.__dict__


class BankData(JsonSerializable):
    def __init__(self):
        self.a = 5
        self.e = 'adas'
        self.free = None


def authorize_api(token=None) -> bool:
    return token is not None and __TOKEN__ == token


@mod_ifttt_webhook.route('/<token>/setBankData')
def setBankData(token):
    if authorize_api(token):
        msg = request.args.get('msg', None)
        if msg is not None:
            try:
                message = Messages(msg)
                db.session.add(message)
                db.session.commit()
                return jsonify(auth=True, add=True)
            except:
                db.session.rollback()
                return jsonify(auth=True, add=False)
        return jsonify(auth=True, add=False, error='\'msg\' field is empty!')
    else:
        return jsonify(error='token not valid', auth=False)


@mod_ifttt_webhook.route('/<token>/getBankData')
def getBankData(token):
    if authorize_api(token):
        return jsonify(auth=True, data=[BankData().toJson()])
    else:
        return jsonify(error='token not valid', auth=False)

