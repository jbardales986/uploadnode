from flask import Flask
from redis import Redis
import os
import socket
app = Flask(__name__)
redis = Redis(host='redis', port=6379)
host = socket.gethostname()

@app.route('/')
def hello():
    redis.incr('hits')
    return '\nMonitor!\nvisualiza %s .\nMi host es %s\n\n' % (redis.get('hits') ,host)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
