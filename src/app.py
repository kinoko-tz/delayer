import time
import uuid
import datetime

from flask.app import Flask
from flask import jsonify
from flask_api import status


app = Flask('delay-response-server')


@app.route('/delay/v1/<int:delay_time>')
def delay_response(delay_time: int):
    if not 0 <= delay_time <= 10:
        return jsonify({
            'error': 'delay time path parameter should be 0 ~ 10 seconds.'
        }), status.HTTP_400_BAD_REQUEST

    time.sleep(delay_time)
    return jsonify({
        'id': uuid.uuid1(),
        'delayTime': delay_time,
        'called_at': datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S,%f')
    }), status.HTTP_200_OK


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000
        # debug=True
    )
