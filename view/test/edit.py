from etc.settings import APP_NAME
from fh_vuexy import *
from view.templates.main_layout import MainLayout


def EditTestPage(session, **kwargs):
    
    test = kwargs.get('test', {})
    
    
    message = kwargs.get('message', None)
    error = kwargs.get('error', None)

    return \
        MainLayout(f'{APP_NAME} - Edit Test',
            FormPage(                
                Div(
                    Div(
                        Div(
                            Div(
                                Alert(Small(message), type=AlertTypeT.Info, icon='ti ti-ban', cls='mb-2') if message else None,
                                Alert(Small(error), type=AlertTypeT.Danger, icon='ti ti-ban', cls='mb-2') if error else None,
                                H5('Edit Test', cls='card-title mb-0'),
                                cls='head-label text-start'
                            ),  
                            cls='card-header d-flex justify-content-between align-items-center'
                        ),
                        Form(
                            Input(type='hidden', name='_id', value=test['_id'] if '_id' in test else ''),
                            Div(
                                Div(
                                    Label('Name', _for='name'),
                                    Input(id='name', name='name', type='text', cls='form-control', placeholder='Name', value=test['name'] if 'name' in test else '', required=True),                                    
                                    Div('Field [name] is required.', cls='invalid-feedback'),
                                    cls='col-md-6 mb-3'                        
                                ),
                                Div(
                                    Label('Description', _for='description'),
                                    Input(id='description', name='description', type='text', cls='form-control', placeholder='Description', value=test['description'] if 'description' in test else '', required=True),                                    
                                    Div('Field [description] is required.', cls='invalid-feedback'),
                                    cls='col-md-6 mb-3'                        
                                ),
                                Div(
                                    Label('Birthday', _for='birthday'),
                                    Input(id='birthday', name='birthday', type='date', cls='form-control', value=test['birthday'] if 'birthday' in test else '', required=True),
                                    Div('Field [birthday] is required.', cls='invalid-feedback'),
                                    cls='col-md-6 mb-3'
                                ),     
                                cls='row g-6'
                            ),
                            Div(
                                Button((I(cls='ti ti-device-floppy me-2'),'Save'), cls='btn btn-primary me-2', role='submit', type='submit'),
                                A((I(cls='ti ti-trash me-2'),'Delete'), cls='btn btn-danger me-2', href=f'/test/delete/{test["_id"]}', onclick='return confirm("Are you sure you want to delete this test?")'),
                                A((I(cls='ti ti-arrow-left me-2'), 'Back'), cls='btn btn-secondary me-2', href='/test'),
                                cls='pt-6'
                            ),
                            id='form-update',                            
                            method='POST',
                            action='/test/update',
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