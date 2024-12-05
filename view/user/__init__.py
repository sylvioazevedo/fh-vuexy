from etc.settings import APP_NAME
from fh_vuexy import *
from view.templates.main_layout import MainLayout

def UserIndexPage(session, **kwargs):
    users = kwargs.get('users', [])
    message = kwargs.get('message', None)
    
    # pagination
    page = int(kwargs.get('page', 1))
    per_page = int(kwargs.get('max', 1))
    count = kwargs.get('count', 0)
    page_range, total_pages = paginate(count, page, per_page)

    return \
        MainLayout(f'{APP_NAME} - Users',
            Page(
                None,
                Div(
                    Div(
                        Div(
                            Div(
                                Alert(Small(message), type=AlertTypeT.Info, icon='ti ti-ban', cls='mb-2') if message else None,
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
                                    Th('Name'),
                                    Th('Username'),
                                    Th('Email'),
                                    Th('Role'),
                                    Th('Actions'),
                                )
                            ),
                            Tbody(
                                *[Tr(
                                    Td(
                                        A(user['name'], href=f'/user/show/{user["_id"]["$oid"]}')
                                    ),
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
                                    cls='table-light' if i % 2 == 0 else '',
                                ) for i, user in enumerate(users)],
                                cls='table-border-bottom-0'
                            ),
                            cls='table table-sm table-hover mb-3'
                        ),
                        TablePagination('/user', page, page_range, total_pages),
                        cls='table-responsive text-nowrap'
                    ),
                    cls='card'
                ),
            ),
            session=session
        )
