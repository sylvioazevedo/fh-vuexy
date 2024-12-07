from dateutil.parser import isoparse
from etc.settings import APP_NAME
from fh_vuexy import *
from view.templates.main_layout import MainLayout

def Show{{domain.title()}}Page(session, *args, **kwargs):    
    
    {{domain}} = kwargs.get('{{domain}}', {})
    message = kwargs.get('message', None)

    return \
        MainLayout(f'{APP_NAME} - Show {{domain.title()}}',       
            FormPage(                
                Div(
                    Div(
                        Div(
                            Alert(Small(message), type=AlertTypeT.Info, icon='ti ti-ban', cls='mb-2') if message else None,
                            Div(
                                H5('Show {{domain.title()}}', cls='card-title mb-0'),
                                cls='head-label text-start'
                            ),  
                            cls='card-header d-flex justify-content-between align-items-center'
                        ),
                        Form(
                            Div(
                                {% for field in fields -%}
                                {% if field.name != 'password' -%}
                                {% if field.type.__name__ == 'datetime' -%}
                                Div(
                                    Label('{{field.name.replace('_', ' ').title()}}', for_='{{field.name}}', cls='form-label'),
                                    Span((isoparse({{domain}}['{{field.name}}']['$date']).strftime("%Y-%m-%d %H:%M:%S") if {{domain}}['{{field.name}}'] else '-') if '{{field.name}}' in {{domain}} else '-', cls='form-control-plaintext'),
                                    cls='col-md-6 mb-3'
                                ),
                                {% else -%}
                                Div(
                                    Label('{{field.name.replace('_', ' ').title()}}', for_='{{field.name}}', cls='form-label'),
                                    Span({{domain}}['{{field.name}}'] if '{{field.name}}' in {{domain}} else '-', cls='form-control-plaintext'),
                                    cls='col-md-6 mb-3'
                                ),
                                {% endif -%}
                                {% endif -%}
                                {% endfor -%}
                                Div(
                                    Label('Id', for_='id'),
                                    Span({{domain}}['_id'] if '_id' in {{domain}} else '-', cls='form-control-plaintext'),                                    
                                    cls='col-md-6 mb-3'
                                ),
                                cls='row g-6'
                            ),
                            Div(
                                A((I(cls='ti ti-edit me-2'), 'Edit'), cls='btn btn-primary me-2', href=f'/{{domain}}/edit/{{'{'}}{{domain}}["_id"]}'),
                                A((I(cls='ti ti-trash me-2'),'Delete'), cls='btn btn-danger me-2', href=f'/{{domain}}/delete/{{'{'}}{{domain}}["_id"]}', onclick='return confirm("Are you sure you want to delete this {{domain}}?")'),
                                A((I(cls='ti ti-arrow-left me-2'), 'Back'), cls='btn btn-secondary me-2', href='/{{domain}}'),
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
                   
