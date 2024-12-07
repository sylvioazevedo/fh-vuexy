from etc.settings import APP_NAME
from fh_vuexy import *
from view.templates.main_layout import MainLayout

def {{domain.title()}}IndexPage(session, **kwargs):
    {{domain}}_list = kwargs.get('{{domain}}_list', [])
    message = kwargs.get('message', None)
    
    # pagination
    page = int(kwargs.get('page', 1))
    per_page = int(kwargs.get('max', 1))
    count = kwargs.get('count', 0)
    page_range, total_pages = paginate(count, page, per_page)

    return \
        MainLayout(f'{APP_NAME} - {{domain.title()}}s',
            FormPage(
                Div(
                    Div(
                        Div(
                            Div(
                                Alert(Small(message), type=AlertTypeT.Info, icon='ti ti-ban', cls='mb-2') if message else None,
                                H5('{{domain.title()}}s', cls='card-title mb-0'),
                                cls='head-label text-start'
                            ),
                            Div(
                                A(I(cls='ti ti-plus me-2'), 'Add {{domain.title()}}', cls='btn btn-primary create-new waves-effect', href='/{{domain}}/create'),
                                cls='text-end'
                            ),
                            cls='card-header d-flex justify-content-between align-items-center'
                        ),
                        SimpleTable(
                            headers = [
                                {% for field in fields -%}
                                {% if field.name != 'password' -%}
                                '{{field.name}}',
                                {%- endif %}
                                {%- endfor %}                                
                                'Actions'
                            ],
                            rows=[ 
                                [                                    
                                    {% for field in fields -%}
                                    {% if field.name != 'password' -%}
                                    TableRow(A(d['{{field.name}}'] if '{{field.name}}' in d else '-', href=f'/{{domain}}/show/{d["_id"]["$oid"]}')),
                                    {%- endif %}
                                    {% endfor %}

                                    TableRow(
                                        TableActionButton(href=f'/{{domain}}/edit/{d["_id"]["$oid"]}', icon='ti ti-pencil', cls='btn-text-primary'),
                                        TableActionButton(href=f'/{{domain}}/delete/{d["_id"]["$oid"]}', icon='ti ti-trash', cls='btn-text-danger', onclick='return confirm("Are you sure you want to delete this {{domain}}?")'),
                                        width='20px'
                                    )
                                ] for d in {{domain}}_list
                            ],                            
                        ),
                        TablePagination('/{{domain}}', page, page_range, total_pages),
                        cls='table-responsive text-nowrap'
                    ),
                    cls='card'
                ),
            ),
            session=session
        )
