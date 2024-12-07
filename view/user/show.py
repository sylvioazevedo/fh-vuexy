from dateutil.parser import isoparse
from etc.settings import APP_NAME
from fh_vuexy import *
from view.templates.main_layout import MainLayout

def ShowUserPage(session, *args, **kwargs):    
    
    user = kwargs.get('user', {})
    message = kwargs.get('message', None)

    return \
        MainLayout(f'{APP_NAME} - Show User',       
            FormPage(                
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
                                    Label('Date Created', for_='date_created', cls='form-label'),
                                    Span((isoparse(user['date_created']['$date']).strftime("%Y-%m-%d %H:%M:%S") if user['date_created'] else '-') if 'date_created' in user else '-', cls='form-control-plaintext'),
                                    cls='col-md-6 mb-3'
                                ),
                                Div(
                                    Label('Last Updated', for_='last_updated', cls='form-label'),
                                    Span((isoparse(user['last_updated']['$date']).strftime("%Y-%m-%d %H:%M:%S") if user['last_updated'] else '-') if 'last_updated' in user else '-', cls='form-control-plaintext'),
                                    cls='col-md-6 mb-3'
                                ),
                                Div(
                                    Label('Expiration Date', for_='expiration_date', cls='form-label'),
                                    Span((isoparse(user['expiration_date']['$date']).strftime("%Y-%m-%d %H:%M:%S") if user['expiration_date'] else '-') if 'expiration_date' in user else '-', cls='form-control-plaintext'),
                                    cls='col-md-6 mb-3'
                                ),
                                Div(
                                    Label('Username', for_='username', cls='form-label'),
                                    Span(user['username'] if 'username' in user else '-', cls='form-control-plaintext'),
                                    cls='col-md-6 mb-3'
                                ),
                                Div(
                                    Label('Name', for_='name', cls='form-label'),
                                    Span(user['name'] if 'name' in user else '-', cls='form-control-plaintext'),
                                    cls='col-md-6 mb-3'
                                ),
                                Div(
                                    Label('Email', for_='email', cls='form-label'),
                                    Span(user['email'] if 'email' in user else '-', cls='form-control-plaintext'),
                                    cls='col-md-6 mb-3'
                                ),
                                Div(
                                    Label('Role', for_='role', cls='form-label'),
                                    Span(user['role'] if 'role' in user else '-', cls='form-control-plaintext'),
                                    cls='col-md-6 mb-3'
                                ),
                                Div(
                                    Label('Enabled', for_='enabled', cls='form-label'),
                                    Span(user['enabled'] if 'enabled' in user else '-', cls='form-control-plaintext'),
                                    cls='col-md-6 mb-3'
                                ),
                                Div(
                                    Label('Expired', for_='expired', cls='form-label'),
                                    Span(user['expired'] if 'expired' in user else '-', cls='form-control-plaintext'),
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
                   