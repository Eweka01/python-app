from flask import Flask, jsonify
import datetime
import socket


app = Flask(__name__)


@app.route('/api/v1/info')

def info():
    return jsonify({
    	'time': datetime.datetime.now().strftime("%I:%M:%S%p  on %B %d, %Y"),
    	'hostname': socket.gethostname(),
        'message': 'You are doing great, big man Gabbi mann!! <3',
        'deployed_on': 'kubernetes'
    })

@app.route('/api/v1/healthz')

def health():
	# Do an actual check here
    return jsonify({'status': 'up'}), 200

if __name__ == '__main__':

    import os
    port = int(os.environ.get('PORT', 5002))
    app.run(host="0.0.0.0", port=port)



#'/api/v1/details'
#'api/v1/healthz'
