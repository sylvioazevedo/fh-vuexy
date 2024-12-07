from etc.settings import APP_NAME
from fh_vuexy import *
from view.templates.main_layout import MainLayout


def New{{domain.title()}}Page(session, *args, **kwargs):    
    
    {% for field in fields -%}
    {% if (field.metadata and 'list' in field.metadata) -%}
    {{field.name}}_list = {{field.metadata|string|replace('list: ', '') }}    
    {% endif -%}
    {% endfor %}

    message = kwargs.get('message', None)

    return \
        MainLayout(f'{APP_NAME} - New {{domain.title()}}',
            FormPage(                
                Div(
                    Div(
                        Div(
                            Div(
                                Alert(Small(message), type=AlertTypeT.Info, icon='ti ti-ban', cls='mb-2') if message else None,
                                H5('New {{domain.title()}}', cls='card-title mb-0'),
                                cls='head-label text-start'
                            ),  
                            cls='card-header d-flex justify-content-between align-items-center'
                        ),
                        Form(
                            Div(
                                {% for field in fields -%}
                                {% if (field.metadata and 'list' in field.metadata) -%}
                                Div(
                                    Label('{{field.name.replace('_', ' ').title()}}', _for='{{field.name}}'),
                                    Select(
                                        Option('Select {{field.name.replace('_', ' ').title()}}', value=True, disable=True, selected=True),
                                        *[Option(value, value=value) for value in {{field.name}}_list],
                                        id='{{field.name}}', name='{{field.name}}', cls='form-select', required=True
                                    ),                                                                        
                                    Div('Please select a {{field.name.replace('_', ' ').title()}}.', cls='invalid-feedback'),
                                    cls='col-md-6 mb-3'
                                ),                                
                                {% else -%}
                                {% if field.type.__name__ == 'str' -%}
                                {% if field.name == 'password' -%}
                                Div(
                                    Label('Password', _for='password'),
                                    Input(id='password', name='password', type='password', cls='form-control', placeholder='********', required=True),
                                    Div('Please inform a password.', cls='invalid-feedback'),
                                    cls='col-md-6 mb-3'
                                ),
                                {% elif field.name == 'email' -%}
                                Div(
                                    Label('Email', _for='email'),
                                    Input(id='email', name='email', type='email', cls='form-control', placeholder='E-mail: joe@doe.com', required=True),
                                    Div('Field [e-mail] is required. [x@x.com.x]', cls='invalid-feedback'),
                                    cls='col-md-6 mb-3'
                                ),
                                {% else -%}
                                Div(
                                    Label('{{field.name.replace('_', ' ').title()}}', _for='{{field.name}}'),
                                    Input(id='{{field.name}}', name='{{field.name}}', type='text', cls='form-control', placeholder='{{field.name.replace('_', ' ').title()}}', required=True),                                    
                                    Div('Field [{{field.name}}] is required.', cls='invalid-feedback'),
                                    cls='col-md-6 mb-3'                        
                                ),
                                {% endif -%}
                                {% elif field.type.__name__ == 'bool' -%}
                                Div(                  
                                    Div(                  
                                        Input(id='{{field.name}}', name='{{field.name}}', type='checkbox', cls='form-check-input'),
                                        Label('{{field.name.replace('_', ' ').title()}}', _for='{{field.name}}', cls='form-check-label'),
                                        cls='form-check form-switch form-check-primary'
                                    ),
                                    cls='col-md-12 mb-3'
                                ),                                
                                {% else -%}
                                {% endif -%}
                                {% endif -%}
                                {% endfor -%}
                                cls='row g-6'
                            ),
                            Div(
                                Button(I(cls='ti ti-device-floppy me-2'), 'Save', cls='btn btn-primary me-2', role='submit', type='submit'),
                                A((I(cls='ti ti-arrow-left me-2'), 'Back'), cls='btn btn-secondary me-2', href='/{{domain}}'),
                                cls='pt-6'
                            ),
                            id='form-new',
                            method='POST',
                            action='/{{domain}}/save',
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