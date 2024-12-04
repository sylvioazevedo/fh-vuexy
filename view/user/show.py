from etc.settings import APP_NAME
from fh_vuexy import *
from view.templates.main_layout import MainLayout

def ShowUserPage(session, *args, **kwargs):    
    
    user = kwargs.get('user', {})
    message = kwargs.get('message', None)

    return \
        MainLayout(f'{APP_NAME} - Show User',       
            Page(
                None,                
                Div(
                    Div(
                        Div(
                            Alert(Small(message), type=AlertTypeT.Info, icon='ti ti-ban', cls='mb-2') if message else None,
                            Div(
                                H5('Show User', cls='card-title mb-0'),
                                cls='head-label text-start'
                            ),  
                            cls='card-header d-flex justify-content-between align-items-center'
                        ),
                        Form(
                            Div(
                                Div(
                                    Label('Name', for_='Name', cls='form-label'),
                                    Span(user['name'] if 'name' in user else '-', cls='form-control-plaintext'),
                                    cls='col-md-6 mb-3'
                                ),                                
                                Div(
                                    Label('Email', for_='email'),
                                    Span(user['email'] if 'email' in user else '-', cls='form-control-plaintext'),
                                    cls='col-md-6 mb-3'
                                ),
                                Div(
                                    Label('username', for_='username', cls='form-label'),
                                    Span(user['username'] if 'username' in user else '-', cls='form-control-plaintext'),
                                    cls='col-md-6 mb-3'
                                ),
                                Div(
                                    Label('Role', for_='role'),
                                    Span(user['role'] if 'role' in user else '-', cls='form-control-plaintext'),                                    
                                    cls='col-md-6 mb-3'
                                ),
                                Div(
                                    Label('Id', for_='id'),
                                    Span(user['_id'] if '_id' in user else '-', cls='form-control-plaintext'),                                    
                                    cls='col-md-6 mb-3'
                                ),
                                cls='row g-6'
                            ),
                            Div(
                                A((I(cls='ti ti-edit me-2'), 'Edit'), cls='btn btn-primary me-2', href=f'/user/edit/{user["_id"]}'),
                                A((I(cls='ti ti-trash me-2'),'Delete'), cls='btn btn-danger me-2', href=f'/user/delete/{user["_id"]}', onclick='return confirm("Are you sure you want to delete this user?")'),
                                A((I(cls='ti ti-arrow-left me-2'), 'Back'), cls='btn btn-secondary me-2', href='/user'),
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
                   
