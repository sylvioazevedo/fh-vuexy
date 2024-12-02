from controller.user_controller import user_app as user_routes
from engine import get_app
from fh_vuexy import *
from view.auth import routes as auth_routes
from view.cards_page import CardsPage
from view.forms_page import FormsPage
from view.main_page import MainPage
from view.not_found_page import NotFoundPage
from view.profile_page import ProfilePage


reg_re_param("static", "ico|gif|jpg|jpeg|webm|css|js|woff|png|svg|mp4|webp|ttf|otf|eot|woff2|txt|html|map|json|mp3")

exception_handlers = {
    404: NotFoundPage
}

routes = [
    Mount('/auth', auth_routes.auth_app, name='auth'),
    Mount('/user', user_routes, name='user'),
]

app, rt = get_app(routes=routes, before=auth_routes.beforeware, exception_handlers=exception_handlers)

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

serve()


