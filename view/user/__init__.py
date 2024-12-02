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

