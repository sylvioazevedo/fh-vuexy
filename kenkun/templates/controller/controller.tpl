
from base.engine import get_app
from fh_vuexy import Link, Script, Redirect
from service.crud_service import CrudService

from view.{{domain}} import {{domain.title()}}IndexPage
from view.{{domain}}.create import New{{domain.title()}}Page
from view.{{domain}}.show import Show{{domain.title()}}Page
from view.{{domain}}.edit import Edit{{domain.title()}}Page

hdrs_ext = (    
    Link(rel='stylesheet', href='/vendor/libs/@form-validation/form-validation.css'),
)

ftrs_ext = (        
    Script(src='/vendor/libs/@form-validation/popular.js'),
    Script(src='/vendor/libs/@form-validation/bootstrap5.js'),
    Script(src='/vendor/libs/@form-validation/auto-focus.js'),
    
    Script(src='/js/custom/form-validation.js'),    
)

{{domain}}_app, rt = get_app(hdrs_ext=hdrs_ext, ftrs_ext=ftrs_ext)

@rt('/')
def index(session, sort:str =None, order: str=None, page: int=1, max: int=10, message:str =None):

    session['active'] = '{{domain.title()}}s'    

    try:
        service = {{domain.title()}}Service(session)
        {{domain}}_list = service.find_all_by('{{domain}}', sort=sort, order=order, page=page, max=max)
        count = service.count('{{domain}}')

        return {{domain.title()}}IndexPage(session, message=message, {{domain}}_list={{domain}}_list, page=page, count=count, max=max)

    except Exception as e:
        session['error'] = f'{str(e)}'
        return Redirect('/')

@rt('/create')
def get(session, message=None):

    session['active'] = '{{domain.title()}}s'    
    return New{{domain.title()}}Page(session, message=message)

@rt('/show/{id}')
def get(id: str, session, message=None):

    session['active'] = '{{domain.title()}}s'

    try:
        service = {{domain.title()}}Service(session)
        {{domain}} = service.find_by_id('{{domain}}', id)

        return Show{{domain.title()}}Page(session, message=message, {{domain}}={{domain}})

    except Exception as e:
        session['error'] = f'{str(e)}'
        return Redirect('/')

@rt('/edit/{id}')
def edit(id:str, session, message=None, error=None):

    session['active'] = '{{domain.title()}}s'

    try:
        service = {{domain.title()}}Service(session)
        {{domain}} = service.find_by_id('{{domain}}', id)

        return Edit{{domain.title()}}Page(session, message=message, {{domain}}={{domain}})
    
    except Exception as e:
        session['error'] = f'{str(e)}'
        return Redirect('/')

@rt('/save')
def post({{domain}}:dict, session):

    try:    
        service = {{domain.title()}}Service(session)
        resp = service.insert('{{domain}}', {{domain}})

        if  not 'id' in resp:
            return New{{domain.title()}}Page(session, message=f'Error saving {{domain}} [{{'{'}}{{domain}}['_id']}].', roles=service.list('role'))
        
        {{domain}}['_id'] = resp['id']
        
        return index(session, message=f'{{domain.title()}} [{resp['id']}:{{'{'}}{{domain}}['_id']}] successfully created.')

    except Exception as e:
        return edit({{domain}}['_id'], session, error=f'Error updating {{domain}} [{{'{'}}{{domain}}["_id"]}] - {str(e)}')

@rt('/update')
def post({{domain}}: dict, session):

    try:
        service = {{domain.title()}}Service(session)
        service.update('{{domain}}', {{domain}})
        
        return index(session, message=f'{{domain.title()}} [{{domain}}["_id"]] successfully updated.')
    
    except Exception as e:        
        return edit({{domain}}['_id'], session, error=f'Error updating {{domain}} [{{'{'}}{{domain}}["_id"]}] - {str(e)}')

@rt('/delete/{id}')
def get(id: str, session):

    try:
        service = {{domain.title()}}Service(session)
        service.delete('{{domain}}', id)
        
        return index(session, message=f'{{domain.title()}} [{id}] successfully removed.')

    except Exception as e:        
        return index(session, error=f'Error deleting {{domain}} [{id}] - {str(e)}')