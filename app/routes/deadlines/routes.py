from app.routes.deadlines import bp
from flask import make_response
from flask import jsonify
from flask import request

from app.dao.deadlines_dao import DeadlineDao

deadline_dao = DeadlineDao()

@bp.route("/deadlines", methods=["GET"])
def get_deadlines():
    try:
        data = deadline_dao.get_all_deadline()
        print(data)
        return jsonify(data)
    except:
        data = {
            "massege": "Что-то пошло не так"
        }
        return make_response(jsonify(data), 500)
    

@bp.route("/deadlines", methods=["POST"])
def post_deadlines():
    try:
        deadline_info = request.get_json()

        if deadline_info["priority"] > 3 or deadline_info["priority"] < 0:
                return False

        data, code = deadline_dao.new_deadline(deadline_info=deadline_info)
        
        return make_response(jsonify(data), code)
    except:
        data = {
            "massege": "Что-то пошло не так"
        }
        return make_response(jsonify(data), 500)


@bp.route("/deadlines", methods=["PUT"])
def update_deadlines():
    try:
        deadline_id: int = request.args.get("id")
        deadline_info: dict = request.get_json()

        data, code = deadline_dao.update_deadline(deadline_id=deadline_id,
                deadline_info=deadline_info)
        return make_response(jsonify(data), code)
    except:
        data = {
            "massege": "Что-то пошло не так"
        }
        return make_response(jsonify(data), 500)
    

@bp.route("/deadlines", methods=["DELETE"])
def delete_deadline():
    try:
        deadline_id: int = request.args.get("id")
        
        data, code = deadline_dao.delete_deadline(deadline_id=deadline_id)
        return make_response(jsonify(data), code)
    except:
        data = {
            "massege": "Что-то пошло не так"
        }
        return make_response(jsonify(data), 500)