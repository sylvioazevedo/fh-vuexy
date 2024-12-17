
from base.engine import get_app
from fh_vuexy import Link, Script, Redirect
from service.crud_service import CrudService as TestService

from view.test import TestIndexPage
from view.test.create import NewTestPage
from view.test.show import ShowTestPage
from view.test.edit import EditTestPage

hdrs_ext = (    
    Link(rel='stylesheet', href='/vendor/libs/@form-validation/form-validation.css'),
)

ftrs_ext = (        
    Script(src='/vendor/libs/@form-validation/popular.js'),
    Script(src='/vendor/libs/@form-validation/bootstrap5.js'),
    Script(src='/vendor/libs/@form-validation/auto-focus.js'),
    
    Script(src='/js/custom/form-validation.js'),    
)

test_app, rt = get_app(hdrs_ext=hdrs_ext, ftrs_ext=ftrs_ext)

@rt('/')
def index(session, sort:str =None, order: str=None, page: int=1, max: int=10, message:str =None):

    session['active'] = 'Tests'    

    try:
        service = TestService(session)
        test_list = service.find_all_by('test', sort=sort, order=order, page=page, max=max)
        count = service.count('test')

        return TestIndexPage(session, message=message, test_list=test_list, page=page, count=count, max=max)

    except Exception as e:

        if e.args[0] == 404:            
            return TestIndexPage(session, message='No tests found.', test_list=[], page=1, count=0, max=10)

        session['error'] = f'{str(e)}'
        return Redirect('/')

@rt('/create')
def get(session, message=None):

    session['active'] = 'Tests'    
    return NewTestPage(session, message=message)

@rt('/show/{id}')
def get(id: str, session, message=None):

    session['active'] = 'Tests'

    try:
        service = TestService(session)
        test = service.find_by_id('test', id)

        return ShowTestPage(session, message=message, test=test)

    except Exception as e:
        session['error'] = f'{str(e)}'
        return Redirect('/')

@rt('/edit/{id}')
def edit(id:str, session, message=None, error=None):

    session['active'] = 'Tests'

    try:
        service = TestService(session)
        test = service.find_by_id('test', id)

        return EditTestPage(session, message=message, test=test)
    
    except Exception as e:
        session['error'] = f'{str(e)}'
        return Redirect('/')

@rt('/save')
def post(test:dict, session):

    try:    
        service = TestService(session)
        resp = service.insert('test', test)

        if  not 'id' in resp:
            return NewTestPage(session, message=f'Error saving test [{test['_id']}].', roles=service.list('role'))
        
        test['_id'] = resp['id']
        
        return index(session, message=f'Test [{resp['id']}:{test['_id']}] successfully created.')

    except Exception as e:
        return edit(test['_id'], session, error=f'Error updating test [{test["_id"]}] - {str(e)}')

@rt('/update')
def post(test: dict, session):

    try:
        service = TestService(session)
        service.update('test', test)
        
        return index(session, message=f'Test [{test["_id"]}] successfully updated.')
    
    except Exception as e:        
        return edit(test['_id'], session, error=f'Error updating test [{test["_id"]}] - {str(e)}')

@rt('/delete/{id}')
def get(id: str, session):

    try:
        service = TestService(session)
        service.delete('test', id)
        
        return index(session, message=f'Test [{id}] successfully removed.')

    except Exception as e:        
        return index(session, error=f'Error deleting test [{id}] - {str(e)}')