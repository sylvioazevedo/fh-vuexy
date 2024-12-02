from etc.settings import APP_NAME
from fh_vuexy import *
from view.templates.main_layout import MainLayout

def ShowUserPage(session, message = None, *args, **kwargs):

    user = args[0] if args else None

    if not user:
        user = kwargs.get('user', {})    

    return \
        MainLayout(f'{APP_NAME} - Show User',       
            Page(
                None,                
                Div(
                    Div(
                        Div(
                            Div(
                                H5('Show User', cls='card-title mb-0'),
                                cls='head-label text-start'
                            ),  
                            cls='card-header d-flex justify-content-between align-items-center'
                        ),
                        Form(
                            Div(
                                Div(
                                    Label('Username', for_='username', cls='form-label'),
                                    Span(user['name'] if 'name' in user else '-', cls='form-control-plaintext'),
                                    cls='col-md-6 mb-3'
                                ),
                                Div(
                                    Label('Email', for_='email'),
                                    Span(user['email'] if 'email' in user else '-', cls='form-control-plaintext'),
                                    cls='col-md-6 mb-3'
                                ),
                                Div(
                                    Label('Role', for_='role'),
                                    Span(user['role'] if 'role' in user else '-', cls='form-control-plaintext'),                                    
                                    cls='col-md-6 mb-3'
                                ),
                                cls='row g-6'
                            ),
                            Div(
                                A('Edit', cls='btn btn-primary me-2', href=f'/user/edit/{user["_id"]}'),
                                A('Delete', cls='btn btn-danger me-2', href=f'/user/delete/{user["_id"]}'),
                                A('Back', cls='btn btn-secondary me-2', href='/user'),
                                cls='pt-6'
                            ),
                            cls='card-body form'
                        ),
                        cls='card'
                    ),
                    cls='col-12'
                ),                                        
            ),
            session=session
        )
                   