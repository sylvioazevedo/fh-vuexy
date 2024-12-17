from etc.settings import APP_NAME
from fh_vuexy import *
from view.templates.main_layout import MainLayout

def TestIndexPage(session, **kwargs):
    test_list = kwargs.get('test_list', [])
    message = kwargs.get('message', None)
    
    # pagination
    page = int(kwargs.get('page', 1))
    per_page = int(kwargs.get('max', 1))
    count = kwargs.get('count', 0)
    page_range, total_pages = paginate(count, page, per_page)

    return \
        MainLayout(f'{APP_NAME} - Tests',
            FormPage(
                Div(
                    Div(
                        Div(
                            Div(
                                Alert(Small(message), type=AlertTypeT.Info, icon='ti ti-ban', cls='mb-2') if message else None,
                                H5('Tests', cls='card-title mb-0'),
                                cls='head-label text-start'
                            ),
                            Div(
                                A(I(cls='ti ti-plus me-2'), 'Add Test', cls='btn btn-primary create-new waves-effect', href='/test/create'),
                                cls='text-end'
                            ),
                            cls='card-header d-flex justify-content-between align-items-center'
                        ),
                        SimpleTable(
                            headers = [
                                'date_created','last_updated','name','description','birthday',                                
                                'Actions'
                            ],
                            rows=[ 
                                [                                    
                                    TableRow(A(d['date_created'] if 'date_created' in d else '-', href=f'/test/show/{d["_id"]["$oid"]}')),
                                    TableRow(A(d['last_updated'] if 'last_updated' in d else '-', href=f'/test/show/{d["_id"]["$oid"]}')),
                                    TableRow(A(d['name'] if 'name' in d else '-', href=f'/test/show/{d["_id"]["$oid"]}')),
                                    TableRow(A(d['description'] if 'description' in d else '-', href=f'/test/show/{d["_id"]["$oid"]}')),
                                    TableRow(A(d['birthday'] if 'birthday' in d else '-', href=f'/test/show/{d["_id"]["$oid"]}')),
                                    

                                    TableRow(
                                        TableActionButton(href=f'/test/edit/{d["_id"]["$oid"]}', icon='ti ti-pencil', cls='btn-text-primary'),
                                        TableActionButton(href=f'/test/delete/{d["_id"]["$oid"]}', icon='ti ti-trash', cls='btn-text-danger', onclick='return confirm("Are you sure you want to delete this test?")'),
                                        width='20px'
                                    )
                                ] for d in test_list
                            ],                            
                        ),
                        TablePagination('/test', page, page_range, total_pages),
                        cls='table-responsive text-nowrap'
                    ),
                    cls='card'
                ),
            ),
            session=session
        )