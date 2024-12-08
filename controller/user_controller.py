from service.hanzo_service import HanzoService as UserService
from base.engine import get_app
from fh_vuexy import Link, Script, Redirect

from view.user import UserIndexPage
from view.user.create import NewUserPage
from view.user.show import ShowUserPage
from view.user.edit import EditUserPage

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

    try:
        service = UserService(session)
        user_list = service.find_all_by('user', sort=sort, order=order, page=page, max=max)
        count = service.count('user')

        return UserIndexPage(session, message=message, user_list=user_list, page=page, count=count, max=max)

    except Exception as e:
        session['error'] = f'{str(e)}'
        return Redirect('/')

@rt('/create')
def get(session, message=None):

    session['active'] = 'Users'    
    return NewUserPage(session, message=message)

@rt('/show/{id}')
def get(id: str, session, message=None):

    session['active'] = 'Users'

    try:
        service = UserService(session)
        user = service.find_by_id('user', id)

        return ShowUserPage(session, message=message, user=user)

    except Exception as e:
        session['error'] = f'{str(e)}'
        return Redirect('/')

@rt('/edit/{id}')
def edit(id:str, session, message=None, error=None):

    session['active'] = 'Users'

    try:
        service = UserService(session)
        user = service.find_by_id('user', id)

        return EditUserPage(session, message=message, user=user)
    
    except Exception as e:
        session['error'] = f'{str(e)}'
        return Redirect('/')

@rt('/save')
def post(user:dict, session):

    try:    
        service = UserService(session)
        resp = service.insert('user', user)

        if  not 'id' in resp:
            return NewUserPage(session, message=f'Error saving user [{user['_id']}].', roles=service.list('role'))
        
        user['_id'] = resp['id']
        
        return index(session, message=f'User [{resp['id']}:{user['_id']}] successfully created.')

    except Exception as e:
        return edit(user['_id'], session, error=f'Error updating user [{user["_id"]}] - {str(e)}')

@rt('/update')
def post(user: dict, session):

    try:
        service = UserService(session)
        service.update('user', user)
        
        return index(session, message=f'User [user["_id"]] successfully updated.')
    
    except Exception as e:        
        return edit(user['_id'], session, error=f'Error updating user [{user["_id"]}] - {str(e)}')

@rt('/delete/{id}')
def get(id: str, session):

    try:
        service = UserService(session)
        service.delete('user', id)
        
        return index(session, message=f'User [{id}] successfully removed.')

    except Exception as e:        
        return index(session, error=f'Error deleting user [{id}] - {str(e)}')