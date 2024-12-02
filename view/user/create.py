from etc.settings import APP_NAME
from fh_vuexy import *
from view.templates.main_layout import MainLayout


def NewUserPage(session, message = None):

    return \
        MainLayout(f'{APP_NAME} - New User',
            Page(
                None,                
                Div(
                    Div(
                        Div(
                            Div(
                                H5('New User', cls='card-title mb-0'),
                                cls='head-label text-start'
                            ),  
                            cls='card-header d-flex justify-content-between align-items-center'
                        ),
                        Form(
                            Div(
                                Div(
                                    Label('Username', for_='username'),
                                    Input(id='username', name='username', type='text', cls='form-control', placeholder='Enter username'),
                                    cls='mb-3'
                                ),
                                Div(
                                    Label('Email', for_='email'),
                                    Input(id='email', name='email', type='email', cls='form-control', placeholder='Enter email'),
                                    cls='mb-3'
                                ),
                                Div(
                                    Label('Role', for_='role'),
                                    Select(
                                        Option('Select Role', value=''),
                                        Option('Admin', value='admin'),
                                        Option('User', value='user'),
                                        id='role', name='role', cls='form-select'
                                    ),

                                    Select(
                                        Option('Select Role', value=''),
                                        *[Option(role['role'], value=role['role'], selected='selected' if role['role'] == user['role'] else '') for role in roles],
                                        id='role', name='role', cls='form-select', readonly='readonly'
                                    ),
                                    cls='mb-3'
                                ),
                                Div(
                                    Button('Save', cls='btn btn-primary', type='submit'),
                                    cls='mb-3'
                                ),
                                cls='form-group'
                            ),
                            cls='form'
                        ),
                        cls='card'
                    ),
                    cls='col-12'
                ),                                        
            ),
            session=session
        )
