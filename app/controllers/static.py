from flask import (
    Blueprint, send_from_directory
)

bp = Blueprint('static', __name__)

@bp.route('/favicon.ico', methods=['GET'])
def index():
    return send_from_directory('public', filename='favicon.ico')
