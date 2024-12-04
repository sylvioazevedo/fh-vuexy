from controller.hanzo_client import HanzoClient
from etc.settings import APP_NAME, HANZO_API_URI
from fh_vuexy import *
from view.templates.main_layout import MainLayout

def DatatablePage(session, message = None):

    session['active'] = 'Users'

    hanzo = HanzoClient(api_url=HANZO_API_URI, session=session)
    hanzo.set_access_token(session['access_token'])
    hanzo.set_refresh_token(session['refresh_token'])

    users = hanzo.list_users()

    return \
        MainLayout(f'{APP_NAME} - Users',
            Page(None,                        
                Div(
                    Div(
                        Table(
                            Thead(
                                Tr(
                                    Th(),
                                    Th(),
                                    Th('id'),
                                    Th('Name'),
                                    Th('Email'),
                                    Th('Date'),
                                    Th('Salary'),
                                    Th('Status'),
                                    Th('Action')
                                )
                            ),
                            cls='datatables-basic table'
                        ),
                        cls='card-datatable table-responsive pt-0'
                    ),
                    cls='card'
                ),
                Div(
                    Div(
                        H5('New Record', id='exampleModalLabel', cls='offcanvas-title'),
                        Button(type='button', data_bs_dismiss='offcanvas', aria_label='Close', cls='btn-close text-reset'),
                        cls='offcanvas-header border-bottom'
                    ),
                    Div(
                        Form(
                            Div(
                                Label('Full Name', fr='basicFullname', cls='form-label'),
                                Div(
                                    Span(
                                        I(cls='ti ti-user'),
                                        id='basicFullname2',
                                        cls='input-group-text'
                                    ),
                                    Input(type='text', id='basicFullname', name='basicFullname', placeholder='John Doe', aria_label='John Doe', aria_describedby='basicFullname2', cls='form-control dt-full-name'),
                                    cls='input-group input-group-merge'
                                ),
                                cls='col-sm-12'
                            ),
                            Div(
                                Label('Post', fr='basicPost', cls='form-label'),
                                Div(
                                    Span(
                                        I(cls='ti ti-briefcase'),
                                        id='basicPost2',
                                        cls='input-group-text'
                                    ),
                                    Input(type='text', id='basicPost', name='basicPost', placeholder='Web Developer', aria_label='Web Developer', aria_describedby='basicPost2', cls='form-control dt-post'),
                                    cls='input-group input-group-merge'
                                ),
                                cls='col-sm-12'
                            ),
                            Div(
                                Label('Email', fr='basicEmail', cls='form-label'),
                                Div(
                                    Span(
                                        I(cls='ti ti-mail'),
                                        cls='input-group-text'
                                    ),
                                    Input(type='text', id='basicEmail', name='basicEmail', placeholder='john.doe@example.com', aria_label='john.doe@example.com', cls='form-control dt-email'),
                                    cls='input-group input-group-merge'
                                ),
                                Div('You can use letters, numbers & periods', cls='form-text'),
                                cls='col-sm-12'
                            ),
                            Div(
                                Label('Joining Date', fr='basicDate', cls='form-label'),
                                Div(
                                    Span(
                                        I(cls='ti ti-calendar'),
                                        id='basicDate2',
                                        cls='input-group-text'
                                    ),
                                    Input(type='text', id='basicDate', name='basicDate', aria_describedby='basicDate2', placeholder='MM/DD/YYYY', aria_label='MM/DD/YYYY', cls='form-control dt-date'),
                                    cls='input-group input-group-merge'
                                ),
                                cls='col-sm-12'
                            ),
                            Div(
                                Label('Salary', fr='basicSalary', cls='form-label'),
                                Div(
                                    Span(
                                        I(cls='ti ti-currency-dollar'),
                                        id='basicSalary2',
                                        cls='input-group-text'
                                    ),
                                    Input(type='number', id='basicSalary', name='basicSalary', placeholder='12000', aria_label='12000', aria_describedby='basicSalary2', cls='form-control dt-salary'),
                                    cls='input-group input-group-merge'
                                ),
                                cls='col-sm-12'
                            ),
                            Div(
                                Button('Submit', type='submit', cls='btn btn-primary data-submit me-sm-4 me-1'),
                                Button('Cancel', type='reset', data_bs_dismiss='offcanvas', cls='btn btn-outline-secondary'),
                                cls='col-sm-12'
                            ),
                            id='form-add-new-record',
                            onsubmit='return false',
                            cls='add-new-record pt-0 row g-2'
                        ),
                        cls='offcanvas-body flex-grow-1'
                    ),
                    id='add-new-record',
                    cls='offcanvas offcanvas-end'
                )

            ),
            session=session
        )
