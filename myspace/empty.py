
from flask import Flask
import flask_limiter as Limiter
import time


class RateLimit:
    def __init__(self, max_calls, period):
        self.max_calls = max_calls
        self.period = period
        self.calls = []

    def allow_call(self):
        now = time.time()
        self.calls = [t for t in self.calls if t > now - self.period]
        if len(self.calls) < self.max_calls:
            self.calls.append(now)
            return True
        return False
    

limiter = RateLimit(10, 1)

app = Flask(__name__)

@app.route('/hello')
# @limiter.limit("5 per seconds")
def index():
  is_allowed = limiter.allow_call()
  if not is_allowed:
    return {'error': 'Rate limit exceeded'}, 429
  
  return {'hello': 'world'}


if __name__ == '__main__':
  app.run()





@app.route('/hello')
def hello():
    return 'hello world'

@app.route('/hi')
def hi():
  return 'hi hi'


   


