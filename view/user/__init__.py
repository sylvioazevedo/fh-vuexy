from etc.settings import APP_NAME
from fh_vuexy import *
from view.templates.main_layout import MainLayout

def UserIndexPage(session, message = None, *args, **kwargs):

    users = args[0]

    if not users:
        users = kwargs.get('users', [])

    return \
        MainLayout(f'{APP_NAME} - Users',
            Page(
                None,                
                Div(
                    Div(
                        Div(
                            Div(
                                H5('Users', cls='card-title mb-0'),
                                cls='head-label text-start'
                            ),  
                            Div(                      
                                A(I(cls='ti ti-plus me-2'), 'Add User', cls='btn btn-primary create-new waves-effect', href='/user/create'),                            
                                cls='text-end'                            
                            ),
                            cls='card-header d-flex justify-content-between align-items-center'
                        ),
                        Table(
                            Thead(
                                Tr(
                                    Th('Username'),
                                    Th('Email'),
                                    Th('Role'),
                                    Th('Actions'),
                                )
                            ),
                            Tbody(
                                *[Tr(
                                    Td(
                                        A(user['username'], href=f'/user/show/{user["_id"]["$oid"]}')
                                    ),
                                    Td(user['email'] if 'email' in user else '-'),
                                    Td(user['role'] if 'role' in user else '-'),
                                    Td(
                                        TableActionButton(href=f'/user/edit/{user["_id"]["$oid"]}', icon='ti ti-pencil', cls='btn-text-primary'),
                                        TableActionButton(href=f'/user/delete/{user["_id"]["$oid"]}', icon='ti ti-trash', cls='btn-text-danger', onclick='return confirm("Are you sure you want to delete this user?")'),
                                        width='20px',
                                    ),
                                    # make background color grey of the row alternate depending on the i index value
                                    cls='table-light' if i % 2 == 0 else '',
                                ) for i, user in enumerate(users)],
                                cls='table-border-bottom-0'
                            ),
                            cls='table table-sm table-hover'
                        ),
                        cls='table-responsive text-nowrap'
                    ),
                    cls='card'
                ),                                        
            ),
            session=session
        )

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
                            Input(type='hidden', name='_method', value='PUT'),
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
                            method='POST',
                            cls='card-body form'
                        ),
                        cls='card'
                    ),
                    cls='col-12'
                ),
            ),
            session=session
        )

