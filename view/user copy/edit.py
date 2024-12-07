from etc.settings import APP_NAME
from fh_vuexy import *
from view.templates.main_layout import MainLayout


def EditUserPage(session, **kwargs):
    
    user = kwargs.get('user', {})
    roles = kwargs.get('roles', [])
    message = kwargs.get('message', None)
    error = kwargs.get('error', None)

    return \
        MainLayout(f'{APP_NAME} - Edit User',
            FormPage(                
                Div(
                    Div(
                        Div(
                            Div(
                                Alert(Small(message), type=AlertTypeT.Info, icon='ti ti-ban', cls='mb-2') if message else None,
                                Alert(Small(error), type=AlertTypeT.Danger, icon='ti ti-ban', cls='mb-2') if error else None,
                                H5('Edit User', cls='card-title mb-0'),
                                cls='head-label text-start'
                            ),  
                            cls='card-header d-flex justify-content-between align-items-center'
                        ),
                        Form(
                            Input(type='hidden', name='_id', value=user['_id'] if '_id' in user else ''),                            
                            Div(
                                Div(
                                    Label('Name', for_='name'),
                                    Input(id='name', name='name', type='text', cls='form-control', placeholder='Name', value=user['name'] if 'username' in user else '', required=True),
                                    Div('Field [name] is required.', cls='invalid-feedback'),
                                    cls='col-md-6 mb-3'
                                ),                                
                                Div(
                                    Label('Email', for_='email'),
                                    Input(id='email', name='email', type='email', cls='form-control', placeholder='E-mail: joe@doe.com', value=user['email'] if 'email' in user else '', required=True),
                                    Div('Field [e-mail] is required. [x@x.com.x]', cls='invalid-feedback'),
                                    cls='col-md-6 mb-3'
                                ),
                                Div(
                                    Label('Username', for_='username'),
                                    Input(id='username', name='username', type='text', cls='form-control', placeholder='Username', value=user['username'] if 'username' in user else '', required=True),
                                    Div('Field [username] is required.', cls='invalid-feedback'),
                                    cls='col-md-6 mb-3'
                                ),
                                Div(
                                    Label('Password', for_='password'),
                                    Input(id='password', name='password', type='password', cls='form-control', placeholder='******'),
                                    cls='col-md-6 mb-3'
                                ),
                                Div(
                                    Label('Role', for_='role'),
                                    Select(
                                        Option('Select Role', value=True, disable=True, selected=True),
                                        *[Option(role['role'], value=role['role'], selected='selected' if role['role'] == user['role'] else '') for role in roles],
                                        value = user['role'] if 'role' in user else '',
                                        id='role', name='role', cls='form-select', required=True
                                    ),
                                    Div('Parameter [role] must be seletecd.', cls='invalid-feedback'),
                                    cls='col-md-6 mb-3'
                                ),
                                cls='row g-6'
                            ),                            
                            Div(
                                Button((I(cls='ti ti-device-floppy me-2'),'Save'), cls='btn btn-primary me-2', role='submit', type='submit'),
                                A((I(cls='ti ti-trash me-2'),'Delete'), cls='btn btn-danger me-2', href=f'/user/delete/{user["_id"]}', onclick='return confirm("Are you sure you want to delete this user?")'),
                                A((I(cls='ti ti-arrow-left me-2'), 'Back'), cls='btn btn-secondary me-2', href='/user'),
                                cls='pt-6'
                            ),
                            id='form-update',                            
                            method='POST',
                            action='/user/update',
                            cls='card-body form needs-validation',
                            novalidate=True                       
                        ),
                        cls='card'
                    ),
                    cls='col-12'
                ),                                        
            ),
            session=session
        )