from controller.hanzo_client import HanzoClient
from engine import get_app
from etc.settings import APP_NAME, HANZO_API_URI
from fh_vuexy import Link, Script, Redirect
from view.user import UserIndexPage
from view.user.create import NewUserPage
from view.user.show import ShowUserPage
from view.user.edit import EditUserPage
from view.user.datatable import DatatablePage

hdrs_ext = (
    Link(rel='stylesheet', href='/vendor/libs/datatables-bs5/datatables.bootstrap5.css'),
    Link(rel='stylesheet', href='/vendor/libs/datatables-responsive-bs5/responsive.bootstrap5.css'),
    Link(rel='stylesheet', href='/vendor/libs/datatables-checkboxes-jquery/datatables.checkboxes.css'),
    Link(rel='stylesheet', href='/vendor/libs/datatables-buttons-bs5/buttons.bootstrap5.css'),
    Link(rel='stylesheet', href='/vendor/libs/flatpickr/flatpickr.css'),
    Link(rel='stylesheet', href='/vendor/libs/datatables-rowgroup-bs5/rowgroup.bootstrap5.css'),
    Link(rel='stylesheet', href='/vendor/libs/@form-validation/form-validation.css'),
)

ftrs_ext = (    
    Script(src='/vendor/libs/datatables-bs5/datatables-bootstrap5.js'),
    Script(src='/vendor/libs/moment/moment.js'),
    Script(src='/vendor/libs/flatpickr/flatpickr.js'),

    Script(src='/vendor/libs/@form-validation/popular.js'),
    Script(src='/vendor/libs/@form-validation/bootstrap5.js'),
    Script(src='/vendor/libs/@form-validation/auto-focus.js'),

    Script(src='/js/tables-datatables-basic.js'),    
)

user_app, rt = get_app(hdrs_ext=hdrs_ext, ftrs_ext=ftrs_ext)

hanzo = HanzoClient(HANZO_API_URI)

@rt('/')
def index(session, message=None):

    session['active'] = 'Users'
    hanzo.set_access_token(session['access_token'])
    hanzo.set_refresh_token(session['refresh_token'])       
    users = hanzo.list_users()

    return UserIndexPage(session, message, users)

@rt('/create')
def get(session, message=None):

    session['active'] = 'Users'
    hanzo.set_access_token(session['access_token'])
    hanzo.set_refresh_token(session['refresh_token']) 
    roles = hanzo.list_roles()
    return NewUserPage(session, message, roles)

@rt('/show/{id}')
def get(id: str, session, message=None):

    session['active'] = 'Users'
    hanzo.set_access_token(session['access_token'])
    hanzo.set_refresh_token(session['refresh_token'])       
    user = hanzo.get_user(id)

    return ShowUserPage(session, message, user)

@rt('/edit/{id}')
def get(id:str, session, message=None):
    hanzo.set_access_token(session['access_token'])
    hanzo.set_refresh_token(session['refresh_token'])       
    user = hanzo.get_user(id)
    roles = hanzo.list_roles()
    return EditUserPage(session, message, user, roles)

@rt('/dt')
def index(session, message=None):
    return DatatablePage(session, message)

@rt('/save')
def post():
    pass

@rt('/update')
def post(user: dict, session):

    print(user)

    hanzo.set_access_token(session['access_token'])
    hanzo.set_refresh_token(session['refresh_token'])       
    hanzo.update_user(user)
    
    return Redirect('/user')

@rt('/delete/{id}')
def get(id: str):
    pass
