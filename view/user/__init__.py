from etc.settings import APP_NAME
from fh_vuexy import *
from view.templates.main_layout import MainLayout

def UserIndexPage(session, **kwargs):
    user_list = kwargs.get('user_list', [])
    message = kwargs.get('message', None)
    
    # pagination
    page = int(kwargs.get('page', 1))
    per_page = int(kwargs.get('max', 1))
    count = kwargs.get('count', 0)
    page_range, total_pages = paginate(count, page, per_page)

    return \
        MainLayout(f'{APP_NAME} - Users',
            FormPage(
                Div(
                    Div(
                        Div(
                            Div(
                                Alert(Small(message), type=AlertTypeT.Info, icon='ti ti-ban', cls='mb-2') if message else None,
                                H5('Users', cls='card-title mb-0'),
                                cls='head-label text-start'
                            ),
                            Div(
                                A(I(cls='ti ti-plus me-2'), 'Add User', cls='btn btn-primary create-new waves-effect', href='/user/create'),
                                cls='text-end'
                            ),
                            cls='card-header d-flex justify-content-between align-items-center'
                        ),
                        SimpleTable(
                            headers = [
                                
                                
                                'date_created',
                                
                                
                                
                                'last_updated',
                                
                                
                                
                                'expiration_date',
                                
                                
                                
                                'username',
                                
                                
                                
                                
                                
                                'name',
                                
                                
                                
                                'email',
                                
                                
                                
                                'role',
                                
                                
                                
                                'enabled',
                                
                                
                                
                                'expired',
                                
                                                                
                                'Actions'
                            ],
                            rows=[ 
                                [                                    
                                    
                                    
                                    TableRow(A(d['date_created'] if 'date_created' in d else '-', href=f'/user/show/{d["_id"]["$oid"]}')),
                                    
                                    
                                    
                                    TableRow(A(d['last_updated'] if 'last_updated' in d else '-', href=f'/user/show/{d["_id"]["$oid"]}')),
                                    
                                    
                                    
                                    TableRow(A(d['expiration_date'] if 'expiration_date' in d else '-', href=f'/user/show/{d["_id"]["$oid"]}')),
                                    
                                    
                                    
                                    TableRow(A(d['username'] if 'username' in d else '-', href=f'/user/show/{d["_id"]["$oid"]}')),
                                    
                                    
                                    
                                    
                                    
                                    TableRow(A(d['name'] if 'name' in d else '-', href=f'/user/show/{d["_id"]["$oid"]}')),
                                    
                                    
                                    
                                    TableRow(A(d['email'] if 'email' in d else '-', href=f'/user/show/{d["_id"]["$oid"]}')),
                                    
                                    
                                    
                                    TableRow(A(d['role'] if 'role' in d else '-', href=f'/user/show/{d["_id"]["$oid"]}')),
                                    
                                    
                                    
                                    TableRow(A(d['enabled'] if 'enabled' in d else '-', href=f'/user/show/{d["_id"]["$oid"]}')),
                                    
                                    
                                    
                                    TableRow(A(d['expired'] if 'expired' in d else '-', href=f'/user/show/{d["_id"]["$oid"]}')),
                                    
                                    

                                    TableRow(
                                        TableActionButton(href=f'/user/edit/{d["_id"]["$oid"]}', icon='ti ti-pencil', cls='btn-text-primary'),
                                        TableActionButton(href=f'/user/delete/{d["_id"]["$oid"]}', icon='ti ti-trash', cls='btn-text-danger', onclick='return confirm("Are you sure you want to delete this user?")'),
                                        width='20px'
                                    )
                                ] for d in user_list
                            ],                            
                        ),
                        TablePagination('/user', page, page_range, total_pages),
                        cls='table-responsive text-nowrap'
                    ),
                    cls='card'
                ),
            ),
            session=session
        )