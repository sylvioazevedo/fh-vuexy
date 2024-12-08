from service.hanzo_service import HanzoService
from webapp.base.engine import get_app
from etc.settings import APP_NAME, HANZO_API_URI
from fh_vuexy import Link, Script, Redirect
from view.user import UserIndexPage
from view.user.create import NewUserPage
from view.user.show import ShowUserPage
from view.user.edit import EditUserPage
from view.user.datatable import DatatablePage

hdrs_ext = (    
    Link(rel='stylesheet', href='/vendor/libs/@form-validation/form-validation.css'),
)

ftrs_ext = (        
    Script(src='/vendor/libs/@form-validation/popular.js'),
    Script(src='/vendor/libs/@form-validation/bootstrap5.js'),
    Script(src='/vendor/libs/@form-validation/auto-focus.js'),
    
    Script(src='/js/custom/form-validation.js'),    
)

user_app, rt = get_app(hdrs_ext=hdrs_ext, ftrs_ext=ftrs_ext)

@rt('/')
def index(session, sort:str =None, order: str=None, page: int=1, max: int=10, message:str =None):

    session['active'] = 'Users'
    service = HanzoService(session)
    user_list = service.find_all_by('user', sort=sort, order=order, page=page, max=max)
    count = service.count('user')

    return UserIndexPage(session, message=message, user_list=user_list, page=page, count=count, max=max)

@rt('/create')
def get(session, message=None):

    session['active'] = 'Users'
    service = HanzoService(session)
    roles = service.list('role')    
    return NewUserPage(session, message=message, roles=roles)

@rt('/show/{id}')
def get(id: str, session, message=None):

    session['active'] = 'Users'
    service = HanzoService(session)
    user = service.find_by_id('user', id)

    return ShowUserPage(session, message=message, user=user)

@rt('/edit/{id}')
def edit(id:str, session, message=None, error=None):
    service = HanzoService(session)
    user = service.find_by_id('user', id)
    roles = service.list('role')
    return EditUserPage(session, message=message, user=user, roles=roles)

@rt('/dt')
def dt(session, message=None):
    return DatatablePage(session, message=message)

@rt('/save')
def post(user:dict, session):
    
    service = HanzoService(session)
    resp = service.insert('user', user)

    if  not 'id' in resp:
        return NewUserPage(session, message=f'Error saving user [{user['username']}].', roles=service.list('role'))
    
    user['_id'] = resp['id']

    #return ShowUserPage(session, message=f'User [{resp['id']}:{user['username']}] successfully saved.', user=user)
    return index(session, message=f'User [{resp['id']}:{user['username']}] successfully created.')

@rt('/update')
def post(user: dict, session):

    try:
        service = HanzoService(session)
        service.update('user', user)
        
        return index(session, message=f'User [{user["_id"]}:{user["username"]}] successfully updated.')
    
    except Exception as e:        
        return edit(user['_id'], session, error=f'Error updating user [{user["username"]}] - {str(e)}')

@rt('/delete/{id}')
def get(id: str, session):

    service = HanzoService(session)
    service.delete('user', id)
    
    return index(session, message=f'User [{id}] successfully removed.')
