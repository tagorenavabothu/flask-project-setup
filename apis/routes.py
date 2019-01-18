from flask import Blueprint

mod = Blueprint('api', __name__)

@mod.route('/')
def getStuff():
	return '{"result":"You are in the API"}'