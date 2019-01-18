from flask import Flask 
app = Flask(__name__)

from codebase.apis.routes import mod
from codebase.site.routes import mod

app.register_blueprint(site.routes.mod)
app.register_blueprint(apis.routes.mod, url_prefix='/api')