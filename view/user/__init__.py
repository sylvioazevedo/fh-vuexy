from etc.settings import APP_NAME
from fh_vuexy import *
from view.templates.main_layout import MainLayout

def paginate(items, page, per_page, max_pages=5):
    total_items = len(items)
    total_pages = (total_items + per_page - 1) // per_page
    start = (page - 1) * per_page
    end = start + per_page
    items_on_page = items[start:end]

    half_max_pages = max_pages // 2
    if total_pages <= max_pages:
        page_range = range(1, total_pages + 1)
    elif page <= half_max_pages:
        page_range = range(1, max_pages + 1)
    elif page > total_pages - half_max_pages:
        page_range = range(total_pages - max_pages + 1, total_pages + 1)
    else:
        page_range = range(page - half_max_pages, page + half_max_pages + 1)

    return items_on_page, page_range, total_pages

def UserIndexPage(session, **kwargs):
    users = kwargs.get('users', [])
    message = kwargs.get('message', None)
    page = int(kwargs.get('page', 1))
    per_page = 10

    users_on_page, page_range, total_pages = paginate(users, page, per_page)

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
                                ) for i, user in enumerate(users_on_page)],
                                cls='table-border-bottom-0'
                            ),
                            cls='table table-sm table-hover'
                        ),
                        Nav(
                            Ul(
                                Li(
                                    A('Previous', href=f'/user?page={page-1}', tabindex='-1', cls='page-link') if page > 1 else None,
                                    cls='page-item' if page > 1 else 'page-item disabled'
                                ),
                                *[Li(
                                    A(str(p), href=f'/user?page={p}', cls='page-link') if p != page else A(str(p), href='#', cls='page-link'),
                                    cls='page-item' if p != page else 'page-item active'
                                ) for p in page_range],
                                Li(
                                    A('Next', href=f'/user?page={page+1}', cls='page-link') if page < total_pages else None,
                                    cls='page-item' if page < total_pages else 'page-item disabled'
                                ),
                                cls='pagination'
                            ),
                            aria_label='...'
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

