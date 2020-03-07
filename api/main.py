from flask import Flask, request, json
from project import db, utils

application = Flask(__name__)
parsed_records_col = db.mongo_database().parsed_records


@application.route("/data")
def data():
    try:
        week_start = utils.datetime(request.values.get('week_start'))
        week_end = utils.datetime(request.values.get('week_end'))
        status, response = 200, db.find_records_in(parsed_records_col, week_start, week_end)
    except AttributeError as err:
        status, response = 400, {'error': 'bad_request', 'message': str(err)}

    return application.response_class(
        response=json.dumps(response),
        status=status,
        mimetype='application/json'
    )


if __name__ == "__main__":
    application.run()
