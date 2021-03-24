import time
import os
import redis
from flask import Flask,render_template,jsonify

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)


@app.route('/flask', methods=["GET"])
def flask_app():
    return render_template('index.html')



@app.route('/test', methods=["GET"])
def test_new():
    return render_template('index.html')

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=os.getenv('PORT'))

#Need to Checkout This Link
#https://levelup.gitconnected.com/using-nginx-reverse-proxy-with-flask-and-docker-66854e940176
