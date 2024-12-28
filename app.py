from base.engine import get_app

# kenkun|controllers
from controller.test_controller import test_app as test_routes
from controller.auth_controller import auth_app as auth_routes, beforeware
from controller.user_controller import user_app as user_routes

from view.cards_page import CardsPage
from view.forms_page import FormsPage
from view.main_page import MainPage
from view.not_found_page import NotFoundPage
from view.profile_page import ProfilePage

from fh_vuexy import *

reg_re_param("static", "ico|gif|jpg|jpeg|webm|css|js|woff|png|svg|mp4|webp|ttf|otf|eot|woff2|txt|html|map|json|mp3")

exception_handlers = {
    404: NotFoundPage
}
    
routes = [    
    # kenkun|routes    
    Mount('/test', test_routes, name='test'),
    Mount('/auth', auth_routes, name='auth'),
    Mount('/user', user_routes, name='user'),    
]

app, rt = get_app(routes=routes, before=beforeware, exception_handlers=exception_handlers)

@rt('/')
def index(session):        
    return MainPage(session)

@rt('/cards')
def index(session):
    return CardsPage(session)

@rt('/forms')
def index(session):
    return FormsPage(session)

@rt('/profile')
def index(session):    
    return ProfilePage(session)

#serve()

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=5001,
        ssl_keyfile=r"C:\Users\sazevedo\Documents\devel\certs\local\private.key",
        ssl_certfile=r"C:\Users\sazevedo\Documents\devel\certs\local\certificate.crt",
        timeout_keep_alive=120,        
        timeout_graceful_shutdown=3,
    )