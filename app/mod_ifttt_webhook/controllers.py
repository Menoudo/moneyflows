# Import flask dependencies
from flask import Blueprint

# Import the database object from the main app module


# Import module models (i.e. User)

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_ifttt_webhook = Blueprint('ifttt_webhook', __name__, url_prefix='/ifttt')


@mod_ifttt_webhook.route('/')
def home():
    return 'ifttt loads ok!'
