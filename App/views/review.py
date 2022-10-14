from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity

from App.controllers import(
    create_review,
    rate_review
)

review_views = Blueprint('review_views', __name__, template_folder='../templates')

@review_views.route('/', methods=['GET'])
def get_review_action():
    