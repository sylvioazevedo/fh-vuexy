from dateutil.parser import isoparse
from etc.settings import APP_NAME
from fh_vuexy import *
from view.templates.main_layout import MainLayout

def ShowTestPage(session, *args, **kwargs):    
    
    test = kwargs.get('test', {})
    message = kwargs.get('message', None)

    return \
        MainLayout(f'{APP_NAME} - Show Test',       
            FormPage(                
                Div(
                    Div(
                        Div(
                            Alert(Small(message), type=AlertTypeT.Info, icon='ti ti-ban', cls='mb-2') if message else None,
                            Div(
                                H5('Show Test', cls='card-title mb-0'),
                                cls='head-label text-start'
                            ),  
                            cls='card-header d-flex justify-content-between align-items-center'
                        ),
                        Form(
                            Div(
                                Div(
                                    Label('Date Created', for_='date_created', cls='form-label'),
                                    Span((isoparse(test['date_created']['$date']).strftime("%Y-%m-%d %H:%M:%S") if test['date_created'] else '-') if 'date_created' in test else '-', cls='form-control-plaintext'),
                                    cls='col-md-6 mb-3'
                                ),
                                Div(
                                    Label('Last Updated', for_='last_updated', cls='form-label'),
                                    Span((isoparse(test['last_updated']['$date']).strftime("%Y-%m-%d %H:%M:%S") if test['last_updated'] else '-') if 'last_updated' in test else '-', cls='form-control-plaintext'),
                                    cls='col-md-6 mb-3'
                                ),
                                Div(
                                    Label('Name', for_='name', cls='form-label'),
                                    Span(test['name'] if 'name' in test else '-', cls='form-control-plaintext'),
                                    cls='col-md-6 mb-3'
                                ),
                                Div(
                                    Label('Description', for_='description', cls='form-label'),
                                    Span(test['description'] if 'description' in test else '-', cls='form-control-plaintext'),
                                    cls='col-md-6 mb-3'
                                ),
                                Div(
                                    Label('Birthday', for_='birthday', cls='form-label'),
                                    Span((isoparse(test['birthday']['$date']).strftime("%Y-%m-%d %H:%M:%S") if test['birthday'] else '-') if 'birthday' in test else '-', cls='form-control-plaintext'),
                                    cls='col-md-6 mb-3'
                                ),
                                Div(
                                    Label('Id', for_='id'),
                                    Span(test['_id'] if '_id' in test else '-', cls='form-control-plaintext'),                                    
                                    cls='col-md-6 mb-3'
                                ),
                                cls='row g-6'
                            ),
                            Div(
                                A((I(cls='ti ti-edit me-2'), 'Edit'), cls='btn btn-primary me-2', href=f'/test/edit/{test["_id"]}'),
                                A((I(cls='ti ti-trash me-2'),'Delete'), cls='btn btn-danger me-2', href=f'/test/delete/{test["_id"]}', onclick='return confirm("Are you sure you want to delete this test?")'),
                                A((I(cls='ti ti-arrow-left me-2'), 'Back'), cls='btn btn-secondary me-2', href='/test'),
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
                   