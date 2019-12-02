from flask import Flask
from flask_restplus import Api, Resource

from frp_sscce.reverse_proxy import ReverseProxied

__version__ = '0.1.0'

app = Flask(__name__)

api = Api(
    app,
    version=__version__,
    title='FRP-SSCCE',
    description='Example to show flask-restplus proxy issue.')

app.wsgi_app = ReverseProxied(app.wsgi_app)

# app.config['API_ROOT_PATH'] = lambda: app.wsgi_app.api_root
app.config['ERROR_404_HELP'] = False

app.secret_key = 'bf91a551d0e3ae30a21eafa3efc592e1cc41f83a179c34cfe3764fd7337fcdd1'
app.debug = True


@api.route('/hello/')
class Hello(Resource):
    @api.response(200, 'Success')
    @api.response(500, 'Internal server error')
    def get(self):
        return 'Hello World'
