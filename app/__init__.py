from flask_restx import Api
from flask import Blueprint

# from main.controller.user_controller import api as users_ns
from .main.controller.user_controller import api as users_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.search_controller import api as search_ns
# 각 controller에서 만든 api 함수를 가져와서 아래 blueprint에 등록해서 사용가능하도록

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Sogaing-Register API Server',
          version='1.0',
          description="Team Facade's Sogang-Register Restful API web service"
          )

api.add_namespace(users_ns, path='/user')
api.add_namespace(auth_ns, path='/auth')
api.add_namespace(search_ns, path='/search')