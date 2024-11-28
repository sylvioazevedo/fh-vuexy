from fh_vuexy import *
from view.templates.main_layout import MainLayout

def ProfilePage(session):
    
    session['active'] = 'Profile'

    return \
    Html(        
        Header(vuexy_hdrs + (Link(rel='stylesheet', href='vendor/css/pages/page-profile.css'),)), \
        Body(
        MainLayout('Vuejs Vuexy Template',
            Page(
                'Profile',                
                Div(
                    Div(
                        Div(
                            Div(
                                Img(src='/img/pages/profile-banner.png', alt='Banner image', cls='rounded-top'),
                                cls='user-profile-header-banner'
                            ),
                            Div(
                                Div(
                                    Img(src='/img/avatars/1.png', alt='user image', cls='d-block h-auto ms-0 ms-sm-6 rounded user-profile-img'),
                                    cls='flex-shrink-0 mt-n2 mx-sm-0 mx-auto'
                                ),
                                Div(
                                    Div(
                                        Div(
                                            H4('John Doe', cls='mb-2 mt-lg-6'),
                                            Ul(
                                                Li(
                                                    I(cls='ti ti-palette ti-lg'),
                                                    Span('UX Designer', cls='fw-medium'),
                                                    cls='list-inline-item d-flex gap-2 align-items-center'
                                                ),
                                                Li(
                                                    I(cls='ti ti-map-pin ti-lg'),
                                                    Span('Vatican City', cls='fw-medium'),
                                                    cls='list-inline-item d-flex gap-2 align-items-center'
                                                ),
                                                Li(
                                                    I(cls='ti ti-calendar ti-lg'),
                                                    Span('Joined April 2021', cls='fw-medium'),
                                                    cls='list-inline-item d-flex gap-2 align-items-center'
                                                ),
                                                cls='list-inline mb-0 d-flex align-items-center flex-wrap justify-content-sm-start justify-content-center gap-4 my-2'
                                            ),
                                            cls='user-profile-info'
                                        ),
                                        A(
                                            I(cls='ti ti-user-check ti-xs me-2'),
                                            'Connected',
                                            href='javascript:void(0)',
                                            cls='btn btn-primary mb-1'
                                        ),
                                        cls='d-flex align-items-md-end align-items-sm-start align-items-center justify-content-md-between justify-content-start mx-5 flex-md-row flex-column gap-4'
                                    ),
                                    cls='flex-grow-1 mt-3 mt-lg-5'
                                ),
                                cls='user-profile-header d-flex flex-column flex-lg-row text-sm-start text-center mb-5'
                            ),
                            cls='card mb-6'
                        ),
                        cls='col-12'
                    ),
                    cls='row'
                ),
                Div(
                    Div(
                        Div(
                            Ul(
                                Li(
                                    A(
                                        I(cls='ti-sm ti ti-user-check me-1_5'),
                                        'Profile',
                                        href='javascript:void(0);',
                                        cls='nav-link active'
                                    ),
                                    cls='nav-item'
                                ),
                                Li(
                                    A(
                                        I(cls='ti-sm ti ti-users me-1_5'),
                                        'Teams',
                                        href='pages-profile-teams.html',
                                        cls='nav-link'
                                    ),
                                    cls='nav-item'
                                ),
                                Li(
                                    A(
                                        I(cls='ti-sm ti ti-layout-grid me-1_5'),
                                        'Projects',
                                        href='pages-profile-projects.html',
                                        cls='nav-link'
                                    ),
                                    cls='nav-item'
                                ),
                                Li(
                                    A(
                                        I(cls='ti-sm ti ti-link me-1_5'),
                                        'Connections',
                                        href='pages-profile-connections.html',
                                        cls='nav-link'
                                    ),
                                    cls='nav-item'
                                ),
                                cls='nav nav-pills flex-column flex-sm-row mb-6 gap-2 gap-lg-0'
                            ),
                            cls='nav-align-top'
                        ),
                        cls='col-md-12'
                    ),
                    cls='row'
                ),
                Div(
                    Div(
                        Div(
                            Div(
                                Small('About', cls='card-text text-uppercase text-muted small'),
                                Ul(
                                    Li(
                                        I(cls='ti ti-user ti-lg'),
                                        Span('Full Name:', cls='fw-medium mx-2'),
                                        Span('John Doe'),
                                        cls='d-flex align-items-center mb-4'
                                    ),
                                    Li(
                                        I(cls='ti ti-check ti-lg'),
                                        Span('Status:', cls='fw-medium mx-2'),
                                        Span('Active'),
                                        cls='d-flex align-items-center mb-4'
                                    ),
                                    Li(
                                        I(cls='ti ti-crown ti-lg'),
                                        Span('Role:', cls='fw-medium mx-2'),
                                        Span('Developer'),
                                        cls='d-flex align-items-center mb-4'
                                    ),
                                    Li(
                                        I(cls='ti ti-flag ti-lg'),
                                        Span('Country:', cls='fw-medium mx-2'),
                                        Span('USA'),
                                        cls='d-flex align-items-center mb-4'
                                    ),
                                    Li(
                                        I(cls='ti ti-language ti-lg'),
                                        Span('Languages:', cls='fw-medium mx-2'),
                                        Span('English'),
                                        cls='d-flex align-items-center mb-2'
                                    ),
                                    cls='list-unstyled my-3 py-1'
                                ),
                                Small('Contacts', cls='card-text text-uppercase text-muted small'),
                                Ul(
                                    Li(
                                        I(cls='ti ti-phone-call ti-lg'),
                                        Span('Contact:', cls='fw-medium mx-2'),
                                        Span('(123) 456-7890'),
                                        cls='d-flex align-items-center mb-4'
                                    ),
                                    Li(
                                        I(cls='ti ti-messages ti-lg'),
                                        Span('Skype:', cls='fw-medium mx-2'),
                                        Span('john.doe'),
                                        cls='d-flex align-items-center mb-4'
                                    ),
                                    Li(
                                        I(cls='ti ti-mail ti-lg'),
                                        Span('Email:', cls='fw-medium mx-2'),
                                        Span('john.doe@example.com'),
                                        cls='d-flex align-items-center mb-4'
                                    ),
                                    cls='list-unstyled my-3 py-1'
                                ),
                                Small('Teams', cls='card-text text-uppercase text-muted small'),
                                Ul(
                                    Li(
                                        Span('Backend Developer', cls='fw-medium me-2'),
                                        Span('(126 Members)'),
                                        cls='d-flex flex-wrap mb-4'
                                    ),
                                    Li(
                                        Span('React Developer', cls='fw-medium me-2'),
                                        Span('(98 Members)'),
                                        cls='d-flex flex-wrap'
                                    ),
                                    cls='list-unstyled mb-0 mt-3 pt-1'
                                ),
                                cls='card-body'
                            ),
                            cls='card mb-6'
                        ),
                        Div(
                            Div(
                                Small('Overview', cls='card-text text-uppercase text-muted small'),
                                Ul(
                                    Li(
                                        I(cls='ti ti-check ti-lg'),
                                        Span('Task Compiled:', cls='fw-medium mx-2'),
                                        Span('13.5k'),
                                        cls='d-flex align-items-end mb-4'
                                    ),
                                    Li(
                                        I(cls='ti ti-layout-grid ti-lg'),
                                        Span('Projects Compiled:', cls='fw-medium mx-2'),
                                        Span('146'),
                                        cls='d-flex align-items-end mb-4'
                                    ),
                                    Li(
                                        I(cls='ti ti-users ti-lg'),
                                        Span('Connections:', cls='fw-medium mx-2'),
                                        Span('897'),
                                        cls='d-flex align-items-end'
                                    ),
                                    cls='list-unstyled mb-0 mt-3 pt-1'
                                ),
                                cls='card-body'
                            ),
                            cls='card mb-6'
                        ),
                        cls='col-xl-4 col-lg-5 col-md-5'
                    ),
                    Div(
                        Div(
                            Div(
                                H5(
                                    I(cls='ti ti-chart-bar ti-lg text-body me-4'),
                                    'Activity Timeline',
                                    cls='card-action-title mb-0'
                                ),
                                cls='card-header align-items-center'
                            ),
                            Div(
                                Ul(
                                    Li(
                                        Span(cls='timeline-point timeline-point-primary'),
                                        Div(
                                            Div(
                                                H6('12 Invoices have been paid', cls='mb-0'),
                                                Small('12 min ago', cls='text-muted'),
                                                cls='timeline-header mb-3'
                                            ),
                                            P('Invoices have been paid to the company', cls='mb-2'),
                                            Div(
                                                Div(
                                                    Img(src='//img/icons/misc/pdf.png', alt='img', width='15', cls='me-2'),
                                                    Span('invoices.pdf', cls='h6 mb-0 text-body'),
                                                    cls='badge bg-lighter rounded d-flex align-items-center'
                                                ),
                                                cls='d-flex align-items-center mb-2'
                                            ),
                                            cls='timeline-event'
                                        ),
                                        cls='timeline-item timeline-item-transparent'
                                    ),
                                    Li(
                                        Span(cls='timeline-point timeline-point-success'),
                                        Div(
                                            Div(
                                                H6('Client Meeting', cls='mb-0'),
                                                Small('45 min ago', cls='text-muted'),
                                                cls='timeline-header mb-3'
                                            ),
                                            P('Project meeting with john @10:15am', cls='mb-2'),
                                            Div(
                                                Div(
                                                    Div(
                                                        Img(src='/img/avatars/1.png', alt='Avatar', cls='rounded-circle'),
                                                        cls='avatar avatar-sm me-3'
                                                    ),
                                                    Div(
                                                        P('Lester McCarthy (Client)', cls='mb-0 small fw-medium'),
                                                        Small('CEO of Pixinvent')
                                                    ),
                                                    cls='d-flex flex-wrap align-items-center mb-50'
                                                ),
                                                cls='d-flex justify-content-between flex-wrap gap-2 mb-2'
                                            ),
                                            cls='timeline-event'
                                        ),
                                        cls='timeline-item timeline-item-transparent'
                                    ),
                                    Li(
                                        Span(cls='timeline-point timeline-point-info'),
                                        Div(
                                            Div(
                                                H6('Create a new project for client', cls='mb-0'),
                                                Small('2 Day Ago', cls='text-muted'),
                                                cls='timeline-header mb-3'
                                            ),
                                            P('6 team members in a project', cls='mb-2'),
                                            Ul(
                                                Li(
                                                    Div(
                                                        Ul(
                                                            Li(
                                                                Img(src='/img/avatars/1.png', alt='Avatar', cls='rounded-circle'),
                                                                data_bs_toggle='tooltip',
                                                                data_popup='tooltip-custom',
                                                                data_bs_placement='top',
                                                                title='Vinnie Mostowy',
                                                                cls='avatar pull-up'
                                                            ),
                                                            Li(
                                                                Img(src='/img/avatars/4.png', alt='Avatar', cls='rounded-circle'),
                                                                data_bs_toggle='tooltip',
                                                                data_popup='tooltip-custom',
                                                                data_bs_placement='top',
                                                                title='Allen Rieske',
                                                                cls='avatar pull-up'
                                                            ),
                                                            Li(
                                                                Img(src='/img/avatars/2.png', alt='Avatar', cls='rounded-circle'),
                                                                data_bs_toggle='tooltip',
                                                                data_popup='tooltip-custom',
                                                                data_bs_placement='top',
                                                                title='Julee Rossignol',
                                                                cls='avatar pull-up'
                                                            ),
                                                            Li(
                                                                Span('+3', data_bs_toggle='tooltip', data_bs_placement='bottom', title='3 more', cls='avatar-initial rounded-circle pull-up text-heading'),
                                                                cls='avatar'
                                                            ),
                                                            cls='list-unstyled users-list d-flex align-items-center avatar-group m-0 me-2'
                                                        ),
                                                        cls='d-flex flex-wrap align-items-center'
                                                    ),
                                                    cls='list-group-item d-flex justify-content-between align-items-center flex-wrap border-top-0 p-0'
                                                ),
                                                cls='list-group list-group-flush'
                                            ),
                                            cls='timeline-event'
                                        ),
                                        cls='timeline-item timeline-item-transparent'
                                    ),
                                    cls='timeline mb-0'
                                ),
                                cls='card-body pt-3'
                            ),
                            cls='card card-action mb-6'
                        ),
                        Div(
                            Div(
                                Div(
                                    Div(
                                        H5('Connections', cls='card-action-title mb-0'),
                                        Div(
                                            Div(
                                                Button(
                                                    I(cls='ti ti-dots-vertical ti-md text-muted'),
                                                    type='button',
                                                    data_bs_toggle='dropdown',
                                                    aria_expanded='false',
                                                    cls='btn btn-icon btn-text-secondary rounded-pill dropdown-toggle hide-arrow p-0 text-muted'
                                                ),
                                                Ul(
                                                    Li(
                                                        A('Share connections', href='javascript:void(0);', cls='dropdown-item')
                                                    ),
                                                    Li(
                                                        A('Suggest edits', href='javascript:void(0);', cls='dropdown-item')
                                                    ),
                                                    Li(
                                                        Hr(cls='dropdown-divider')
                                                    ),
                                                    Li(
                                                        A('Report bug', href='javascript:void(0);', cls='dropdown-item')
                                                    ),
                                                    cls='dropdown-menu dropdown-menu-end'
                                                ),
                                                cls='dropdown'
                                            ),
                                            cls='card-action-element'
                                        ),
                                        cls='card-header align-items-center'
                                    ),
                                    Div(
                                        Ul(
                                            Li(
                                                Div(
                                                    Div(
                                                        Div(
                                                            Img(src='/img/avatars/2.png', alt='Avatar', cls='rounded-circle'),
                                                            cls='avatar me-2'
                                                        ),
                                                        Div(
                                                            H6('Cecilia Payne', cls='mb-0'),
                                                            Small('45 Connections'),
                                                            cls='me-2'
                                                        ),
                                                        cls='d-flex align-items-center'
                                                    ),
                                                    Div(
                                                        Button(
                                                            I(cls='ti ti-user-check ti-md'),
                                                            cls='btn btn-label-primary btn-icon'
                                                        ),
                                                        cls='ms-auto'
                                                    ),
                                                    cls='d-flex align-items-center'
                                                ),
                                                cls='mb-4'
                                            ),
                                            Li(
                                                Div(
                                                    Div(
                                                        Div(
                                                            Img(src='/img/avatars/3.png', alt='Avatar', cls='rounded-circle'),
                                                            cls='avatar me-2'
                                                        ),
                                                        Div(
                                                            H6('Curtis Fletcher', cls='mb-0'),
                                                            Small('1.32k Connections'),
                                                            cls='me-2'
                                                        ),
                                                        cls='d-flex align-items-center'
                                                    ),
                                                    Div(
                                                        Button(
                                                            I(cls='ti ti-user-x ti-md'),
                                                            cls='btn btn-primary btn-icon'
                                                        ),
                                                        cls='ms-auto'
                                                    ),
                                                    cls='d-flex align-items-center'
                                                ),
                                                cls='mb-4'
                                            ),
                                            Li(
                                                Div(
                                                    Div(
                                                        Div(
                                                            Img(src='/img/avatars/10.png', alt='Avatar', cls='rounded-circle'),
                                                            cls='avatar me-2'
                                                        ),
                                                        Div(
                                                            H6('Alice Stone', cls='mb-0'),
                                                            Small('125 Connections'),
                                                            cls='me-2'
                                                        ),
                                                        cls='d-flex align-items-center'
                                                    ),
                                                    Div(
                                                        Button(
                                                            I(cls='ti ti-user-x ti-md'),
                                                            cls='btn btn-primary btn-icon'
                                                        ),
                                                        cls='ms-auto'
                                                    ),
                                                    cls='d-flex align-items-center'
                                                ),
                                                cls='mb-4'
                                            ),
                                            Li(
                                                Div(
                                                    Div(
                                                        Div(
                                                            Img(src='/img/avatars/7.png', alt='Avatar', cls='rounded-circle'),
                                                            cls='avatar me-2'
                                                        ),
                                                        Div(
                                                            H6('Darrell Barnes', cls='mb-0'),
                                                            Small('456 Connections'),
                                                            cls='me-2'
                                                        ),
                                                        cls='d-flex align-items-center'
                                                    ),
                                                    Div(
                                                        Button(
                                                            I(cls='ti ti-user-check ti-md'),
                                                            cls='btn btn-label-primary btn-icon'
                                                        ),
                                                        cls='ms-auto'
                                                    ),
                                                    cls='d-flex align-items-center'
                                                ),
                                                cls='mb-4'
                                            ),
                                            Li(
                                                Div(
                                                    Div(
                                                        Div(
                                                            Img(src='/img/avatars/12.png', alt='Avatar', cls='rounded-circle'),
                                                            cls='avatar me-2'
                                                        ),
                                                        Div(
                                                            H6('Eugenia Moore', cls='mb-0'),
                                                            Small('1.2k Connections'),
                                                            cls='me-2'
                                                        ),
                                                        cls='d-flex align-items-center'
                                                    ),
                                                    Div(
                                                        Button(
                                                            I(cls='ti ti-user-check ti-md'),
                                                            cls='btn btn-label-primary btn-icon'
                                                        ),
                                                        cls='ms-auto'
                                                    ),
                                                    cls='d-flex align-items-center'
                                                ),
                                                cls='mb-6'
                                            ),
                                            Li(
                                                A('View all connections', href='javascript:;'),
                                                cls='text-center'
                                            ),
                                            cls='list-unstyled mb-0'
                                        ),
                                        cls='card-body'
                                    ),
                                    cls='card card-action mb-6'
                                ),
                                cls='col-lg-12 col-xl-6'
                            ),
                            Div(
                                Div(
                                    Div(
                                        H5('Teams', cls='card-action-title mb-0'),
                                        Div(
                                            Div(
                                                Button(
                                                    I(cls='ti ti-dots-vertical text-muted'),
                                                    type='button',
                                                    data_bs_toggle='dropdown',
                                                    aria_expanded='false',
                                                    cls='btn btn-icon btn-text-secondary dropdown-toggle hide-arrow p-0'
                                                ),
                                                Ul(
                                                    Li(
                                                        A('Share teams', href='javascript:void(0);', cls='dropdown-item')
                                                    ),
                                                    Li(
                                                        A('Suggest edits', href='javascript:void(0);', cls='dropdown-item')
                                                    ),
                                                    Li(
                                                        Hr(cls='dropdown-divider')
                                                    ),
                                                    Li(
                                                        A('Report bug', href='javascript:void(0);', cls='dropdown-item')
                                                    ),
                                                    cls='dropdown-menu dropdown-menu-end'
                                                ),
                                                cls='dropdown'
                                            ),
                                            cls='card-action-element'
                                        ),
                                        cls='card-header align-items-center'
                                    ),
                                    Div(
                                        Ul(
                                            Li(
                                                Div(
                                                    Div(
                                                        Div(
                                                            Img(src='/img/icons/brands/react-label.png', alt='Avatar', cls='rounded-circle'),
                                                            cls='avatar me-2'
                                                        ),
                                                        Div(
                                                            H6('React Developers', cls='mb-0'),
                                                            Small('72 Members'),
                                                            cls='me-2'
                                                        ),
                                                        cls='d-flex align-items-center'
                                                    ),
                                                    Div(
                                                        A(
                                                            Span('Developer', cls='badge bg-label-danger'),
                                                            href='javascript:;'
                                                        ),
                                                        cls='ms-auto'
                                                    ),
                                                    cls='d-flex align-items-center'
                                                ),
                                                cls='mb-4'
                                            ),
                                            Li(
                                                Div(
                                                    Div(
                                                        Div(
                                                            Img(src='/img/icons/brands/support-label.png', alt='Avatar', cls='rounded-circle'),
                                                            cls='avatar me-2'
                                                        ),
                                                        Div(
                                                            H6('Support Team', cls='mb-0'),
                                                            Small('122 Members'),
                                                            cls='me-2'
                                                        ),
                                                        cls='d-flex align-items-center'
                                                    ),
                                                    Div(
                                                        A(
                                                            Span('Support', cls='badge bg-label-primary'),
                                                            href='javascript:;'
                                                        ),
                                                        cls='ms-auto'
                                                    ),
                                                    cls='d-flex align-items-center'
                                                ),
                                                cls='mb-4'
                                            ),
                                            Li(
                                                Div(
                                                    Div(
                                                        Div(
                                                            Img(src='/img/icons/brands/figma-label.png', alt='Avatar', cls='rounded-circle'),
                                                            cls='avatar me-2'
                                                        ),
                                                        Div(
                                                            H6('UI Designers', cls='mb-0'),
                                                            Small('7 Members'),
                                                            cls='me-2'
                                                        ),
                                                        cls='d-flex align-items-center'
                                                    ),
                                                    Div(
                                                        A(
                                                            Span('Designer', cls='badge bg-label-info'),
                                                            href='javascript:;'
                                                        ),
                                                        cls='ms-auto'
                                                    ),
                                                    cls='d-flex align-items-center'
                                                ),
                                                cls='mb-4'
                                            ),
                                            Li(
                                                Div(
                                                    Div(
                                                        Div(
                                                            Img(src='/img/icons/brands/vue-label.png', alt='Avatar', cls='rounded-circle'),
                                                            cls='avatar me-2'
                                                        ),
                                                        Div(
                                                            H6('Vue.js Developers', cls='mb-0'),
                                                            Small('289 Members'),
                                                            cls='me-2'
                                                        ),
                                                        cls='d-flex align-items-center'
                                                    ),
                                                    Div(
                                                        A(
                                                            Span('Developer', cls='badge bg-label-danger'),
                                                            href='javascript:;'
                                                        ),
                                                        cls='ms-auto'
                                                    ),
                                                    cls='d-flex align-items-center'
                                                ),
                                                cls='mb-4'
                                            ),
                                            Li(
                                                Div(
                                                    Div(
                                                        Div(
                                                            Img(src='/img/icons/brands/twitter-label.png', alt='Avatar', cls='rounded-circle'),
                                                            cls='avatar me-2'
                                                        ),
                                                        Div(
                                                            H6('Digital Marketing', cls='mb-0'),
                                                            Small('24 Members'),
                                                            cls='me-w'
                                                        ),
                                                        cls='d-flex align-items-center'
                                                    ),
                                                    Div(
                                                        A(
                                                            Span('Marketing', cls='badge bg-label-secondary'),
                                                            href='javascript:;'
                                                        ),
                                                        cls='ms-auto'
                                                    ),
                                                    cls='d-flex align-items-center'
                                                ),
                                                cls='mb-6'
                                            ),
                                            Li(
                                                A('View all teams', href='javascript:;'),
                                                cls='text-center'
                                            ),
                                            cls='list-unstyled mb-0'
                                        ),
                                        cls='card-body'
                                    ),
                                    cls='card card-action mb-6'
                                ),
                                cls='col-lg-12 col-xl-6'
                            ),
                            cls='row'
                        ),
                        Div(
                            Div(
                                Table(
                                    Thead(
                                        Tr(
                                            Th(),
                                            Th(),
                                            Th('Project'),
                                            Th('Leader'),
                                            Th('Team'),
                                            Th('Progress', cls='w-px-200'),
                                            Th('Action')
                                        )
                                    ),
                                    cls='datatables-projects table border-top'
                                ),
                                cls='card-datatable table-responsive'
                            ),
                            cls='card mb-4'
                        ),
                        cls='col-xl-8 col-lg-7 col-md-7'
                    ),
                    cls='row'
                )
            ),
            session=session
        ), vuexy_ftrs),
        {
            'lang': 'en',
            'class': 'light-style layout-navbar-fixed layout-menu-fixed layout-compact',
            'dir': 'ltr',
            'data-theme': 'theme-default',
            'data-assets-path': '/',
            'data-templates': 'vertical-menu-template-starter',
            'data-style': 'light',            
        })