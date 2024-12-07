from etc.settings import APP_NAME
from fh_vuexy import *
from view.templates.main_layout import MainLayout


def EditUserPage(session, **kwargs):
    
    user = kwargs.get('user', {})
    role_list = ["admin", "user"]    
    
    
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
                                    Label('Username', _for='username'),
                                    Input(id='username', name='username', type='text', cls='form-control', placeholder='Username', value=user['username'] if 'username' in user else '', required=True),                                    
                                    Div('Field [username] is required.', cls='invalid-feedback'),
                                    cls='col-md-6 mb-3'                        
                                ),
                                Div(
                                    Label('Password', _for='password'),
                                    Input(id='password', name='password', type='password', cls='form-control', placeholder='********'),
                                    Div('Please inform a password.', cls='invalid-feedback'),
                                    cls='col-md-6 mb-3'
                                ),
                                Div(
                                    Label('Name', _for='name'),
                                    Input(id='name', name='name', type='text', cls='form-control', placeholder='Name', value=user['name'] if 'name' in user else '', required=True),                                    
                                    Div('Field [name] is required.', cls='invalid-feedback'),
                                    cls='col-md-6 mb-3'                        
                                ),
                                Div(
                                    Label('Email', _for='email'),
                                    Input(id='email', name='email', type='email', cls='form-control', placeholder='E-mail: joe@doe.com', value=user['email'] if 'email' in user else '', required=True),
                                    Div('Field [e-mail] is required. [x@x.com.x]', cls='invalid-feedback'),
                                    cls='col-md-6 mb-3'
                                ),
                                Div(
                                    Label('Role', _for='role'),
                                    Select(
                                        Option('Select Role', value=True, disable=True, selected=True),
                                        *[Option(value, value=value, selected='selected' if user['role'] == value else '' ) for value in role_list],
                                        id='role', name='role', cls='form-select', required=True
                                    ),                                                                        
                                    Div('Please select a Role.', cls='invalid-feedback'),
                                    cls='col-md-6 mb-3'
                                ),                                
                                Div(                  
                                    Div(                  
                                        Input(id='enabled', name='enabled', type='checkbox', cls='form-check-input', checked='checked' if 'enabled' in user and user['enabled'] else ''),
                                        Label('Enabled', _for='enabled', cls='form-check-label'),
                                        cls='form-check form-switch form-check-primary'
                                    ),
                                    cls='col-md-12 mb-3'
                                ),
                                Div(                  
                                    Div(                  
                                        Input(id='expired', name='expired', type='checkbox', cls='form-check-input', checked='checked' if 'expired' in user and user['expired'] else ''),
                                        Label('Expired', _for='expired', cls='form-check-label'),
                                        cls='form-check form-switch form-check-primary'
                                    ),
                                    cls='col-md-12 mb-3'
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