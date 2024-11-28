from fh_vuexy import *
from view.templates.main_layout import MainLayout

def CardsPage(session):
    
    session['active'] = 'Cards'

    return \
        MainLayout('Cards page',
            Page(
                'Cards',                
                Div(
                    Div(
                        Div(
                            Img(src='/img/elements/2.jpg', alt='Card image cap', cls='card-img-top'),
                            Div(
                                H5('Card title', cls='card-title'),
                                P("Some quick example text to build on the card title and make up the bulk of the card's content.", cls='card-text'),
                                A('Go somewhere', href='javascript:void(0)', cls='btn btn-outline-primary'),
                                cls='card-body'
                            ),
                            cls='card h-100'
                        ),
                        cls='col-md-6 col-lg-4'
                    ),
                    Div(
                        Div(
                            Div(
                                H5('Card title', cls='card-title'),
                                H6('Support card subtitle', cls='card-subtitle'),
                                cls='card-body'
                            ),
                            Img(src='/img/elements/10.jpg', alt='Card image cap', cls='img-fluid'),
                            Div(
                                P('Bear claw sesame snaps gummies chocolate.', cls='card-text'),
                                A('Card link', href='javascript:void(0);', cls='card-link'),
                                A('Another link', href='javascript:void(0);', cls='card-link'),
                                cls='card-body'
                            ),
                            cls='card h-100'
                        ),
                        cls='col-md-6 col-lg-4'
                    ),
                    Div(
                        Div(
                            Div(
                                H5('Card title', cls='card-title'),
                                H6('Support card subtitle', cls='card-subtitle'),
                                Img(src='/img/elements/4.jpg', alt='Card image cap', cls='img-fluid d-flex mx-auto my-6 rounded'),
                                P('Bear claw sesame snaps gummies chocolate.', cls='card-text'),
                                A('Card link', href='javascript:void(0);', cls='card-link'),
                                A('Another link', href='javascript:void(0);', cls='card-link'),
                                cls='card-body'
                            ),
                            cls='card h-100'
                        ),
                        cls='col-md-6 col-lg-4'
                    ),
                    cls='row mb-12 g-6'
                ),

                H5('Content types', cls='pb-1 mb-6'),

                Div(
                    Div(
                        H6('Body', cls='mt-2 text-muted'),
                        Div(
                            Div(
                                P('This is some text within a card body. Jelly lemon drops tiramisu chocolate cake cotton candy\r\n                        soufflé oat cake sweet roll. Sugar plum marzipan dragée topping cheesecake chocolate bar. Danish\r\n                        muffin icing donut.', cls='card-text'),
                                cls='card-body'
                            ),
                            cls='card mb-6'
                        ),
                        H6('Titles, text, and links', cls='mt-2 text-muted'),
                        Div(
                            Div(
                                H5('Card title', cls='card-title mb-1'),
                                Div('Card subtitle', cls='card-subtitle mb-4'),
                                P("Some quick example text to build on the card title and make up the bulk of the card's content.", cls='card-text'),
                                A('Card link', href='javascript:void(0)', cls='card-link'),
                                A('Another link', href='javascript:void(0)', cls='card-link'),
                                cls='card-body'
                            ),
                            cls='card mb-6'
                        ),
                        H6('List groups', cls='mt-2 text-muted'),
                        Div(
                            Ul(
                                Li('Cras justo odio', cls='list-group-item'),
                                Li('Dapibus ac facilisis in', cls='list-group-item'),
                                Li('Vestibulum at eros', cls='list-group-item'),
                                cls='list-group list-group-flush'
                            ),
                            cls='card mb-6'
                        ),
                        cls='col-md-6 col-lg-4'
                    ),
                    Div(
                        H6('Images', cls='mt-2 text-muted'),
                        Div(
                            Img(src='/img/elements/5.jpg', alt='Card image cap', cls='card-img-top'),
                            Div(
                                P("Some quick example text to build on the card title and make up the bulk of the card's content.", cls='card-text'),
                                P('Cookie topping caramels jujubes gingerbread. Lollipop apple pie cupcake candy canes cookie ice\r\n                        cream. Wafer chocolate bar carrot cake jelly-o.', cls='card-text'),
                                cls='card-body'
                            ),
                            cls='card'
                        ),
                        cls='col-md-6 col-lg-4'
                    ),
                    Div(
                        H6('Kitchen sink', cls='mt-2 text-muted'),
                        Div(
                            Img(src='/img/elements/7.jpg', alt='Card image cap', cls='card-img-top'),
                            Div(
                                H5('Card title', cls='card-title'),
                                P('Some quick example text to build on the card title.', cls='card-text'),
                                cls='card-body'
                            ),
                            Ul(
                                Li('Cras justo odio', cls='list-group-item'),
                                Li('Vestibulum at eros', cls='list-group-item'),
                                cls='list-group list-group-flush'
                            ),
                            Div(
                                A('Card link', href='javascript:void(0)', cls='card-link'),
                                A('Another link', href='javascript:void(0)', cls='card-link'),
                                cls='card-body'
                            ),
                            cls='card'
                        ),
                        cls='col-md-6 col-lg-4'
                    ),
                    cls='row mb-12 g-6'
                ),

                H6('Header and footer', cls='pb-1 mb-6 text-muted'),

                Div(
                    Div(
                        Div(
                            Div('Featured', cls='card-header'),
                            Div(
                                H5('Special title treatment', cls='card-title'),
                                P('With supporting text below as a natural lead-in to additional content natural lead-in to\r\n                        additional content.', cls='card-text'),
                                A('Go somewhere', href='javascript:void(0)', cls='btn btn-primary'),
                                cls='card-body'
                            ),
                            cls='card'
                        ),
                        cls='col-md-6 col-lg-4'
                    ),
                    Div(
                        Div(
                            H5('Quote', cls='card-header'),
                            Div(
                                Blockquote(
                                    P('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.Lorem\r\n                          ipsum dolor sit amet, consectetur.'),
                                    Footer(
                                        'Someone famous in',
                                        Cite('Source Title', title='Source Title'),
                                        cls='blockquote-footer'
                                    ),
                                    cls='blockquote mb-0'
                                ),
                                cls='card-body'
                            ),
                            cls='card'
                        ),
                        cls='col-md-6 col-lg-4'
                    ),
                    Div(
                        Div(
                            Div('Featured', cls='card-header'),
                            Div(
                                H5('Special title treatment', cls='card-title'),
                                P('With supporting text below as a natural.', cls='card-text'),
                                A('Go somewhere', href='javascript:void(0)', cls='btn btn-primary'),
                                cls='card-body'
                            ),
                            Div('2 days ago', cls='card-footer text-muted'),
                            cls='card text-center'
                        ),
                        cls='col-md-6 col-lg-4'
                    ),
                    cls='row mb-12 g-6'
                ),

                H5('Text alignment', cls='pb-1 mb-6'),

                Div(
                    Div(
                        Div(
                            Div(
                                H5('Special title treatment', cls='card-title'),
                                P('With supporting text below as a natural lead-in to additional content.', cls='card-text'),
                                A('Go somewhere', href='javascript:void(0)', cls='btn btn-primary'),
                                cls='card-body'
                            ),
                            cls='card'
                        ),
                        cls='col-md-6 col-lg-4'
                    ),
                    Div(
                        Div(
                            Div(
                                H5('Special title treatment', cls='card-title'),
                                P('With supporting text below as a natural lead-in to additional content.', cls='card-text'),
                                A('Go somewhere', href='javascript:void(0)', cls='btn btn-primary'),
                                cls='card-body'
                            ),
                            cls='card text-center'
                        ),
                        cls='col-md-6 col-lg-4'
                    ),
                    Div(
                        Div(
                            Div(
                                H5('Special title treatment', cls='card-title'),
                                P('With supporting text below as a natural lead-in to additional content.', cls='card-text'),
                                A('Go somewhere', href='javascript:void(0)', cls='btn btn-primary'),
                                cls='card-body'
                            ),
                            cls='card text-end'
                        ),
                        cls='col-md-6 col-lg-4'
                    ),
                    cls='row mb-12 g-6'
                ),

                H5('Navigation', cls='pb-1 mb-6'),

                Div(
                    Div(
                        Div(
                            Div(
                                Div(
                                    Ul(
                                        Li(
                                            Button('Home', type='button', role='tab', data_bs_toggle='tab', data_bs_target='#navs-tab-home', aria_controls='navs-tab-home', aria_selected='true', cls='nav-link active'),
                                            cls='nav-item'
                                        ),
                                        Li(
                                            Button('Profile', type='button', role='tab', data_bs_toggle='tab', data_bs_target='#navs-tab-profile', aria_controls='navs-tab-profile', aria_selected='false', cls='nav-link'),
                                            cls='nav-item'
                                        ),
                                        Li(
                                            Button('Disabled', type='button', data_bs_toggle='tab', role='tab', aria_selected='false', cls='nav-link disabled'),
                                            cls='nav-item'
                                        ),
                                        role='tablist',
                                        cls='nav nav-tabs'
                                    ),
                                    cls='nav-align-top'
                                ),
                                cls='card-header px-0 pt-0'
                            ),
                            Div(
                                Div(
                                    Div(
                                        H5('Special title treatment', cls='card-title'),
                                        P('With supporting text below as a natural lead-in to additional content.', cls='card-text'),
                                        A('Go home', href='javascript:void(0);', cls='btn btn-primary'),
                                        id='navs-tab-home',
                                        role='tabpanel',
                                        cls='tab-pane fade show active'
                                    ),
                                    Div(
                                        H5('Special title treatment', cls='card-title'),
                                        P('With supporting text below as a natural lead-in to additional content.', cls='card-text'),
                                        A('Go profile', href='javascript:void(0);', cls='btn btn-primary'),
                                        id='navs-tab-profile',
                                        role='tabpanel',
                                        cls='tab-pane fade'
                                    ),
                                    cls='tab-content p-0'
                                ),
                                cls='card-body'
                            ),
                            cls='card text-center'
                        ),
                        cls='col-md-6'
                    ),
                    Div(
                        Div(
                            Div(
                                Div(
                                    Ul(
                                        Li(
                                            Button('Home', type='button', role='tab', data_bs_toggle='tab', data_bs_target='#navs-pills-tab-home', aria_controls='navs-pills-tab-home', aria_selected='true', cls='nav-link active'),
                                            cls='nav-item'
                                        ),
                                        Li(
                                            Button('Profile', type='button', role='tab', data_bs_toggle='tab', data_bs_target='#navs-pills-tab-profile', aria_controls='navs-pills-tab-profile', aria_selected='false', cls='nav-link'),
                                            cls='nav-item'
                                        ),
                                        Li(
                                            Button('Disabled', type='button', role='tab', data_bs_toggle='tab', aria_selected='false', cls='nav-link disabled'),
                                            cls='nav-item'
                                        ),
                                        role='tablist',
                                        cls='nav nav-pills row-gap-2'
                                    ),
                                    cls='nav-align-top'
                                ),
                                cls='card-header'
                            ),
                            Div(
                                Div(
                                    Div(
                                        H5('Special title treatment', cls='card-title'),
                                        P('With supporting text below as a natural lead-in to additional content.', cls='card-text'),
                                        A('Go home', href='javascript:void(0);', cls='btn btn-primary'),
                                        id='navs-pills-tab-home',
                                        role='tabpanel',
                                        cls='tab-pane fade show active'
                                    ),
                                    Div(
                                        H5('Special title treatment', cls='card-title'),
                                        P('With supporting text below as a natural lead-in to additional content.', cls='card-text'),
                                        A('Go profile', href='javascript:void(0);', cls='btn btn-primary'),
                                        id='navs-pills-tab-profile',
                                        role='tabpanel',
                                        cls='tab-pane fade'
                                    ),
                                    cls='tab-content p-0'
                                ),
                                cls='card-body'
                            ),
                            cls='card text-center'
                        ),
                        cls='col-md-6'
                    ),
                    cls='row mb-12 g-6'
                ),

                H5('Images caps & overlay', cls='pb-1 mb-6'),

                Div(
                    Div(
                        Div(
                            Img(src='/img/elements/13.jpg', alt='Card image cap', cls='card-img-top'),
                            Div(
                                H5('Card title', cls='card-title'),
                                P('This is a wider card with supporting text below as a natural lead-in to additional content. This\r\n                        content is a little bit longer.', cls='card-text'),
                                P(
                                    Small('Last updated 3 mins ago', cls='text-muted'),
                                    cls='card-text'
                                ),
                                cls='card-body'
                            ),
                            cls='card'
                        ),
                        cls='col-md-6 col-xl-4'
                    ),
                    Div(
                        Div(
                            Div(
                                H5('Card title', cls='card-title'),
                                P('This is a wider card with supporting text below as a natural lead-in to additional content. This\r\n                        content is a little bit longer.', cls='card-text'),
                                P(
                                    Small('Last updated 3 mins ago', cls='text-muted'),
                                    cls='card-text'
                                ),
                                cls='card-body'
                            ),
                            Img(src='/img/elements/1.jpg', alt='Card image cap', cls='card-img-bottom'),
                            cls='card'
                        ),
                        cls='col-md-6 col-xl-4'
                    ),
                    Div(
                        Div(
                            Img(src='/img/elements/8.jpg', alt='Card image', cls='card-img'),
                            Div(
                                H5('Card title', cls='card-title'),
                                P('This is a wider card with supporting text below as a natural lead-in to additional content. This\r\n                        content is a little bit longer.', cls='card-text'),
                                P('Last updated 3 mins ago', cls='card-text'),
                                cls='card-img-overlay'
                            ),
                            cls='card bg-dark border-0 text-white'
                        ),
                        cls='col-md-6 col-xl-4'
                    ),
                    cls='row mb-12 g-6'
                ),

                H5('Horizontal', cls='pb-1 mb-6'),

                Div(
                    Div(
                        Div(
                            Div(
                                Div(
                                    Img(src='/img/elements/9.jpg', alt='Card image', cls='card-img card-img-left'),
                                    cls='col-md-4'
                                ),
                                Div(
                                    Div(
                                        H5('Card title', cls='card-title'),
                                        P('This is a wider card with supporting text below as a natural lead-in to additional content.\r\n                            This content is a little bit longer.', cls='card-text'),
                                        P(
                                            Small('Last updated 3 mins ago', cls='text-muted'),
                                            cls='card-text'
                                        ),
                                        cls='card-body'
                                    ),
                                    cls='col-md-8'
                                ),
                                cls='row g-0'
                            ),
                            cls='card'
                        ),
                        cls='col-md'
                    ),
                    Div(
                        Div(
                            Div(
                                Div(
                                    Div(
                                        H5('Card title', cls='card-title'),
                                        P('This is a wider card with supporting text below as a natural lead-in to additional content.\r\n                            This content is a little bit longer.', cls='card-text'),
                                        P(
                                            Small('Last updated 3 mins ago', cls='text-muted'),
                                            cls='card-text'
                                        ),
                                        cls='card-body'
                                    ),
                                    cls='col-md-8'
                                ),
                                Div(
                                    Img(src='/img/elements/12.jpg', alt='Card image', cls='card-img card-img-right'),
                                    cls='col-md-4'
                                ),
                                cls='row g-0'
                            ),
                            cls='card'
                        ),
                        cls='col-md'
                    ),
                    cls='row mb-12 g-6'
                ),

                H5('Style variation', cls='pb-1 mb-4'),

                H6('Default(solid)', cls='pb-1 mb-4 text-muted'),

                Div(
                    Div(
                        Div(
                            Div(
                                H5('Primary card title', cls='card-title text-white'),
                                P('Some quick example text to build on the card title and make up.', cls='card-text'),
                                cls='card-body'
                            ),
                            cls='card bg-primary text-white'
                        ),
                        cls='col-md-6 col-xl-4'
                    ),
                    Div(
                        Div(
                            Div(
                                H5('Secondary card title', cls='card-title text-white'),
                                P('Some quick example text to build on the card title and make up.', cls='card-text'),
                                cls='card-body'
                            ),
                            cls='card bg-secondary text-white'
                        ),
                        cls='col-md-6 col-xl-4'
                    ),
                    Div(
                        Div(
                            Div(
                                H5('Success card title', cls='card-title text-white'),
                                P('Some quick example text to build on the card title and make up.', cls='card-text'),
                                cls='card-body'
                            ),
                            cls='card bg-success text-white'
                        ),
                        cls='col-md-6 col-xl-4'
                    ),
                    Div(
                        Div(
                            Div(
                                H5('Danger card title', cls='card-title text-white'),
                                P('Some quick example text to build on the card title and make up.', cls='card-text'),
                                cls='card-body'
                            ),
                            cls='card bg-danger text-white'
                        ),
                        cls='col-md-6 col-xl-4'
                    ),
                    Div(
                        Div(
                            Div(
                                H5('Warning card title', cls='card-title text-white'),
                                P('Some quick example text to build on the card title and make up.', cls='card-text'),
                                cls='card-body'
                            ),
                            cls='card bg-warning text-white'
                        ),
                        cls='col-md-6 col-xl-4'
                    ),
                    Div(
                        Div(
                            Div(
                                H5('Info card title', cls='card-title text-white'),
                                P('Some quick example text to build on the card title and make up.', cls='card-text'),
                                cls='card-body'
                            ),
                            cls='card bg-info text-white'
                        ),
                        cls='col-md-6 col-xl-4'
                    ),
                    cls='row g-6 mb-6'
                ),

                H6('Label', cls='pb-1 mb-4 text-muted'),

                Div(
                    Div(
                        Div(
                            Div(
                                H5('Primary card title', cls='card-title text-primary'),
                                P('Some quick example text to build on the card title and make up.', cls='card-text text-primary'),
                                cls='card-body'
                            ),
                            cls='card shadow-none bg-primary-subtle'
                        ),
                        cls='col-md-6 col-xl-4'
                    ),
                    Div(
                        Div(
                            Div(
                                H5('Secondary card title', cls='card-title text-secondary'),
                                P('Some quick example text to build on the card title and make up.', cls='card-text text-secondary'),
                                cls='card-body'
                            ),
                            cls='card shadow-none bg-secondary-subtle'
                        ),
                        cls='col-md-6 col-xl-4'
                    ),
                    Div(
                        Div(
                            Div(
                                H5('Success card title', cls='card-title text-success'),
                                P('Some quick example text to build on the card title and make up.', cls='card-text text-success'),
                                cls='card-body'
                            ),
                            cls='card shadow-none bg-success-subtle'
                        ),
                        cls='col-md-6 col-xl-4'
                    ),
                    Div(
                        Div(
                            Div(
                                H5('Danger card title', cls='card-title text-danger'),
                                P('Some quick example text to build on the card title and make up.', cls='card-text text-danger'),
                                cls='card-body'
                            ),
                            cls='card shadow-none bg-danger-subtle'
                        ),
                        cls='col-md-6 col-xl-4'
                    ),
                    Div(
                        Div(
                            Div(
                                H5('Warning card title', cls='card-title text-warning'),
                                P('Some quick example text to build on the card title and make up.', cls='card-text text-warning'),
                                cls='card-body'
                            ),
                            cls='card shadow-none bg-warning-subtle'
                        ),
                        cls='col-md-6 col-xl-4'
                    ),
                    Div(
                        Div(
                            Div(
                                H5('Info card title', cls='card-title text-info'),
                                P('Some quick example text to build on the card title and make up.', cls='card-text text-info'),
                                cls='card-body'
                            ),
                            cls='card shadow-none bg-info-subtle'
                        ),
                        cls='col-md-6 col-xl-4'
                    ),
                    cls='row g-6 mb-4'
                ),

                H6('Outline', cls='pb-1 mb-4 text-muted'),

                Div(
                    Div(
                        Div(
                            Div(
                                H5('Primary card title', cls='card-title text-primary'),
                                P('Some quick example text to build on the card title and make up.', cls='card-text text-primary'),
                                cls='card-body'
                            ),
                            cls='card shadow-none bg-transparent border border-primary'
                        ),
                        cls='col-md-6 col-xl-4'
                    ),
                    Div(
                        Div(
                            Div(
                                H5('Secondary card title', cls='card-title text-secondary'),
                                P('Some quick example text to build on the card title and make up.', cls='card-text text-secondary'),
                                cls='card-body'
                            ),
                            cls='card shadow-none bg-transparent border border-secondary'
                        ),
                        cls='col-md-6 col-xl-4'
                    ),
                    Div(
                        Div(
                            Div(
                                H5('Success card title', cls='card-title text-success'),
                                P('Some quick example text to build on the card title and make up.', cls='card-text text-success'),
                                cls='card-body'
                            ),
                            cls='card shadow-none bg-transparent border border-success'
                        ),
                        cls='col-md-6 col-xl-4'
                    ),
                    Div(
                        Div(
                            Div(
                                H5('Danger card title', cls='card-title text-danger'),
                                P('Some quick example text to build on the card title and make up.', cls='card-text text-danger'),
                                cls='card-body'
                            ),
                            cls='card shadow-none bg-transparent border border-danger'
                        ),
                        cls='col-md-6 col-xl-4'
                    ),
                    Div(
                        Div(
                            Div(
                                H5('Warning card title', cls='card-title text-warning'),
                                P('Some quick example text to build on the card title and make up.', cls='card-text text-warning'),
                                cls='card-body'
                            ),
                            cls='card shadow-none bg-transparent border border-warning'
                        ),
                        cls='col-md-6 col-xl-4'
                    ),
                    Div(
                        Div(
                            Div(
                                H5('Info card title', cls='card-title text-info'),
                                P('Some quick example text to build on the card title and make up.', cls='card-text text-info'),
                                cls='card-body'
                            ),
                            cls='card shadow-none bg-transparent border border-info'
                        ),
                        cls='col-md-6 col-xl-4'
                    ),
                    cls='row g-6'
                ),

                H5('Card layout', cls='pb-1 my-12'),

                H6('Card Groups', cls='pb-1 mb-6 text-muted'),

                Div(
                    Div(
                        Img(src='/img/elements/4.jpg', alt='Card image cap', cls='card-img-top'),
                        Div(
                            H5('Card title', cls='card-title'),
                            P('This is a wider card with supporting text below as a natural lead-in to additional content. This\r\n                      content is a little bit longer.', cls='card-text'),
                            cls='card-body'
                        ),
                        Div(
                            Small('Last updated 3 mins ago', cls='text-muted'),
                            cls='card-footer'
                        ),
                        cls='card'
                    ),
                    Div(
                        Img(src='/img/elements/5.jpg', alt='Card image cap', cls='card-img-top'),
                        Div(
                            H5('Card title', cls='card-title'),
                            P('This card has supporting text below as a natural lead-in to additional content.', cls='card-text'),
                            cls='card-body'
                        ),
                        Div(
                            Small('Last updated 3 mins ago', cls='text-muted'),
                            cls='card-footer'
                        ),
                        cls='card'
                    ),
                    Div(
                        Img(src='/img/elements/1.jpg', alt='Card image cap', cls='card-img-top'),
                        Div(
                            H5('Card title', cls='card-title'),
                            P('This is a wider card with supporting text below as a natural lead-in to additional content. This\r\n                      card has even longer content than the first to show that equal height action.', cls='card-text'),
                            cls='card-body'
                        ),
                        Div(
                            Small('Last updated 3 mins ago', cls='text-muted'),
                            cls='card-footer'
                        ),
                        cls='card'
                    ),
                    cls='card-group mb-12'
                ),

                H6('Grid Card', cls='pb-1 mb-6 text-muted'),

                Div(
                    Div(
                        Div(
                            Img(src='/img/elements/2.jpg', alt='Card image cap', cls='card-img-top'),
                            Div(
                                H5('Card title', cls='card-title'),
                                P('This is a longer card with supporting text below as a natural lead-in to additional content.\r\n                        This content is a little bit longer.', cls='card-text'),
                                cls='card-body'
                            ),
                            cls='card h-100'
                        ),
                        cls='col'
                    ),
                    Div(
                        Div(
                            Img(src='/img/elements/10.jpg', alt='Card image cap', cls='card-img-top'),
                            Div(
                                H5('Card title', cls='card-title'),
                                P('This is a longer card with supporting text below as a natural lead-in to additional content.\r\n                        This content is a little bit longer.', cls='card-text'),
                                cls='card-body'
                            ),
                            cls='card h-100'
                        ),
                        cls='col'
                    ),
                    Div(
                        Div(
                            Img(src='/img/elements/4.jpg', alt='Card image cap', cls='card-img-top'),
                            Div(
                                H5('Card title', cls='card-title'),
                                P('This is a longer card with supporting text below as a natural lead-in to additional content.', cls='card-text'),
                                cls='card-body'
                            ),
                            cls='card h-100'
                        ),
                        cls='col'
                    ),
                    Div(
                        Div(
                            Img(src='/img/elements/13.jpg', alt='Card image cap', cls='card-img-top'),
                            Div(
                                H5('Card title', cls='card-title'),
                                P('This is a longer card with supporting text below as a natural lead-in to additional content.\r\n                        This content is a little bit longer.', cls='card-text'),
                                cls='card-body'
                            ),
                            cls='card h-100'
                        ),
                        cls='col'
                    ),
                    Div(
                        Div(
                            Img(src='/img/elements/14.jpg', alt='Card image cap', cls='card-img-top'),
                            Div(
                                H5('Card title', cls='card-title'),
                                P('This is a longer card with supporting text below as a natural lead-in to additional content.\r\n                        This content is a little bit longer.', cls='card-text'),
                                cls='card-body'
                            ),
                            cls='card h-100'
                        ),
                        cls='col'
                    ),
                    Div(
                        Div(
                            Img(src='/img/elements/15.jpg', alt='Card image cap', cls='card-img-top'),
                            Div(
                                H5('Card title', cls='card-title'),
                                P('This is a longer card with supporting text below as a natural lead-in to additional content.\r\n                        This content is a little bit longer.', cls='card-text'),
                                cls='card-body'
                            ),
                            cls='card h-100'
                        ),
                        cls='col'
                    ),
                    cls='row row-cols-1 row-cols-md-3 g-6 mb-12'
                ),

                H6('Masonry', cls='pb-1 mb-6 text-muted'),

                Div(
                    Div(
                        Div(
                            Img(src='/img/elements/5.jpg', alt='Card image cap', cls='card-img-top'),
                            Div(
                                H5('Card title that wraps to a new line', cls='card-title'),
                                P('This is a longer card with supporting text below as a natural lead-in to additional content.\r\n                        This content is a little bit longer.', cls='card-text'),
                                cls='card-body'
                            ),
                            cls='card'
                        ),
                        cls='col-sm-6 col-lg-4'
                    ),
                    Div(
                        Div(
                            Figure(
                                Blockquote(
                                    P('A well-known quote, contained in a blockquote element.'),
                                    cls='blockquote'
                                ),
                                Figcaption(
                                    'Someone famous in',
                                    Cite('Source Title', title='Source Title'),
                                    cls='blockquote-footer mb-0 text-muted'
                                ),
                                cls='p-4 mb-0'
                            ),
                            cls='card p-4'
                        ),
                        cls='col-sm-6 col-lg-4'
                    ),
                    Div(
                        Div(
                            Img(src='/img/elements/13.jpg', alt='Card image cap', cls='card-img-top'),
                            Div(
                                H5('Card title', cls='card-title'),
                                P('This card has supporting text below as a natural lead-in to additional content.', cls='card-text'),
                                P(
                                    Small('Last updated 3 mins ago', cls='text-muted'),
                                    cls='card-text'
                                ),
                                cls='card-body'
                            ),
                            cls='card'
                        ),
                        cls='col-sm-6 col-lg-4'
                    ),
                    Div(
                        Div(
                            Figure(
                                Blockquote(
                                    P('A well-known quote, contained in a blockquote element.'),
                                    cls='blockquote'
                                ),
                                Figcaption(
                                    'Someone famous in',
                                    Cite('Source Title', title='Source Title'),
                                    cls='blockquote-footer mb-0 text-white'
                                ),
                                cls='mb-0'
                            ),
                            cls='card bg-primary text-white text-center p-4'
                        ),
                        cls='col-sm-6 col-lg-4'
                    ),
                    Div(
                        Div(
                            Div(
                                H5('Card title', cls='card-title'),
                                P('This card has a regular title and short paragraph of text below it.', cls='card-text'),
                                P(
                                    Small('Last updated 3 mins ago', cls='text-muted'),
                                    cls='card-text'
                                ),
                                cls='card-body'
                            ),
                            cls='card text-center'
                        ),
                        cls='col-sm-6 col-lg-4'
                    ),
                    Div(
                        Div(
                            Img(src='/img/elements/4.jpg', alt='Card image cap', cls='card-img'),
                            cls='card'
                        ),
                        cls='col-sm-6 col-lg-4'
                    ),
                    Div(
                        Div(
                            Figure(
                                Blockquote(
                                    P('A well-known quote, contained in a blockquote element.'),
                                    cls='blockquote'
                                ),
                                Figcaption(
                                    'Someone famous in',
                                    Cite('Source Title', title='Source Title'),
                                    cls='blockquote-footer mb-0 text-muted'
                                ),
                                cls='mb-0'
                            ),
                            cls='card p-4 text-end'
                        ),
                        cls='col-sm-6 col-lg-4'
                    ),
                    Div(
                        Div(
                            Div(
                                H5('Card title', cls='card-title'),
                                P('This is another card with title and supporting text below. This card has some additional content\r\n                        to make it slightly taller overall.', cls='card-text'),
                                P(
                                    Small('Last updated 3 mins ago', cls='text-muted'),
                                    cls='card-text'
                                ),
                                cls='card-body'
                            ),
                            cls='card'
                        ),
                        cls='col-sm-6 col-lg-4'
                    ),
                    data_masonry='{"percentPosition": true }',
                    cls='row g-6'
                )
            ),
            session=session
        )