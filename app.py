#import os
import json
from flask import Flask

app = Flask(__name__)
#app.config.from_object(os.environ['APP_SETTINGS'])

@app.route('/')
def hello():
	return "Hello World!"

@app.route('/<name>')
def hell_name(name):
	return "Hello {}!".format(name)

@app.route('/<name>/<nick>')
def hello_name_nick(name, nick):
	return "Hello {}({})!".format(name, nick)

@app.route('/estimate', methods=['POST'])
def POST_estimate():
	


if __name__ == '__main__':
	app.run()
