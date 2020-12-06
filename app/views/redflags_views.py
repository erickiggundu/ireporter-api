from flask import Response, Blueprint
import json

redflag_blueprint = Blueprint("Redflag Bluepring", __name__)

@redflag_blueprint.route('/redflags', methods=['POST'])
def create__redflag():
    response = Reponse(json.dumps({"message":"redflag created successfully"}), status = 200, content_type = "application/json")
    return response

