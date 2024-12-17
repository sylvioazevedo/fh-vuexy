from etc.settings import APP_NAME
from fh_vuexy import *
from view.templates.main_layout import MainLayout



def NewTestPage(session, *args, **kwargs):    
    
    

    message = kwargs.get('message', None)

    return \
        MainLayout(f'{APP_NAME} - New Test',
            FormPage(                
                Div(
                    Div(
                        Div(
                            Div(
                                Alert(Small(message), type=AlertTypeT.Info, icon='ti ti-ban', cls='mb-2') if message else None,
                                H5('New Test', cls='card-title mb-0'),
                                cls='head-label text-start'
                            ),  
                            cls='card-header d-flex justify-content-between align-items-center'
                        ),
                        Form(
                            Div(
                                Div(
                                    Label('Name', _for='name'),
                                    Input(id='name', name='name', type='text', cls='form-control', placeholder='Name', required=True),                                    
                                    Div('Field [name] is required.', cls='invalid-feedback'),
                                    cls='col-md-6 mb-3'                        
                                ),
                                Div(
                                    Label('Description', _for='description'),
                                    Input(id='description', name='description', type='text', cls='form-control', placeholder='Description', required=True),                                    
                                    Div('Field [description] is required.', cls='invalid-feedback'),
                                    cls='col-md-6 mb-3'                        
                                ),
                                cls='row g-6'
                            ),
                            Div(
                                Button(I(cls='ti ti-device-floppy me-2'), 'Save', cls='btn btn-primary me-2', role='submit', type='submit'),
                                A((I(cls='ti ti-arrow-left me-2'), 'Back'), cls='btn btn-secondary me-2', href='/test'),
                                cls='pt-6'
                            ),
                            id='form-new',
                            method='POST',
                            action='/test/save',
                            cls='card-body form needs-validation',
                            novalidate=True                       
                        ),
                        cls='card'
                    ),
                    cls='col-12'
                ),                                        
            ),
            session=session
        )