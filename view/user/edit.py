from etc.settings import APP_NAME
from fh_vuexy import *
from view.templates.main_layout import MainLayout


def EditUserPage(session, message = None, *args, **kwargs):

    user = args[0] if args else None

    if not user:
        user = kwargs.get('user', {})

    roles = args[1] if len(args) > 1 else None    

    if not roles:
        roles = kwargs.get('roles', [])

    return \
        MainLayout(f'{APP_NAME} - Edit User',
            Page(
                None,                
                Div(
                    Div(
                        Div(
                            Div(
                                H5('Edit User', cls='card-title mb-0'),
                                cls='head-label text-start'
                            ),  
                            cls='card-header d-flex justify-content-between align-items-center'
                        ),
                        Form(
                            Input(type='hidden', name='_id', value=user['_id'] if '_id' in user else ''),
                            Div(
                                Div(
                                    Label('Username', for_='username'),
                                    Input(id='username', name='username', type='text', cls='form-control', placeholder='Enter username', value=user['username'] if 'username' in user else ''),
                                    cls='col-md-6 mb-3'
                                ),
                                Div(
                                    Label('Email', for_='email'),
                                    Input(id='email', name='email', type='email', cls='form-control', placeholder='Enter email', value=user['email'] if 'email' in user else ''),
                                    cls='col-md-6 mb-3'
                                ),
                                Div(
                                    Label('Role', for_='role'),
                                    Select(
                                        Option('Select Role', value=''),
                                        *[Option(role['role'], value=role['role'], selected='selected' if role['role'] == user['role'] else '') for role in roles],
                                        value = user['role'] if 'role' in user else '',
                                        id='role', name='role', cls='form-select'
                                    ),
                                    cls='col-md-6 mb-3'
                                ),
                                cls='row g-6'
                            ),                            
                            Div(
                                Button('Save', cls='btn btn-primary', role='submit', type='submit'),
                                cls='pt-6'
                            ),
                            action='/user/update',
                            method='PUT',
                            cls='card-body form'                            
                        ),
                        cls='card'
                    ),
                    cls='col-12'
                ),                                        
            ),
            session=session
        )
