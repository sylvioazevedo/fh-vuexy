from fh_vuexy import *
from view.templates.main_layout import MainLayout

def FormsPage(session):

    session['active'] = 'Forms'
    
    return \
        MainLayout('Forms page',
            Page(
                'Forms',                
                Div(
                    Div(
                        Div(
                            Div(
                                H5('Basic Layout', cls='mb-0'),
                                Small('Default label', cls='text-muted float-end'),
                                cls='card-header d-flex justify-content-between align-items-center'
                            ),
                            Div(
                                Form(
                                    Div(
                                        Label('Full Name', fr='basic-default-fullname', cls='form-label'),
                                        Input(type='text', id='basic-default-fullname', placeholder='John Doe', cls='form-control'),
                                        cls='mb-6'
                                    ),
                                    Div(
                                        Label('Company', fr='basic-default-company', cls='form-label'),
                                        Input(type='text', id='basic-default-company', placeholder='ACME Inc.', cls='form-control'),
                                        cls='mb-6'
                                    ),
                                    Div(
                                        Label('Email', fr='basic-default-email', cls='form-label'),
                                        Div(
                                            Input(type='text', id='basic-default-email', placeholder='john.doe', aria_label='john.doe', aria_describedby='basic-default-email2', cls='form-control'),
                                            Span('@example.com', id='basic-default-email2', cls='input-group-text'),
                                            cls='input-group input-group-merge'
                                        ),
                                        Div('You can use letters, numbers & periods', cls='form-text'),
                                        cls='mb-6'
                                    ),
                                    Div(
                                        Label('Phone No', fr='basic-default-phone', cls='form-label'),
                                        Input(type='text', id='basic-default-phone', placeholder='658 799 8941', cls='form-control phone-mask'),
                                        cls='mb-6'
                                    ),
                                    Div(
                                        Label('Message', fr='basic-default-message', cls='form-label'),
                                        Textarea(id='basic-default-message', placeholder='Hi, Do you have a moment to talk Joe?', cls='form-control'),
                                        cls='mb-6'
                                    ),
                                    Button('Send', type='submit', cls='btn btn-primary')
                                ),
                                cls='card-body'
                            ),
                            cls='card'
                        ),
                        cls='col-xl mb-6'
                    ),
                    Div(
                        Div(
                            Div(
                                H5('Basic with Icons', cls='mb-0'),
                                Small('Merged input group', cls='text-muted float-end'),
                                cls='card-header d-flex justify-content-between align-items-center'
                            ),
                            Div(
                                Form(
                                    Div(
                                        Label('Full Name', fr='basic-icon-default-fullname', cls='form-label'),
                                        Div(
                                            Span(
                                                I(cls='ti ti-user'),
                                                id='basic-icon-default-fullname2',
                                                cls='input-group-text'
                                            ),
                                            Input(type='text', id='basic-icon-default-fullname', placeholder='John Doe', aria_label='John Doe', aria_describedby='basic-icon-default-fullname2', cls='form-control'),
                                            cls='input-group input-group-merge'
                                        ),
                                        cls='mb-6'
                                    ),
                                    Div(
                                        Label('Company', fr='basic-icon-default-company', cls='form-label'),
                                        Div(
                                            Span(
                                                I(cls='ti ti-building'),
                                                id='basic-icon-default-company2',
                                                cls='input-group-text'
                                            ),
                                            Input(type='text', id='basic-icon-default-company', placeholder='ACME Inc.', aria_label='ACME Inc.', aria_describedby='basic-icon-default-company2', cls='form-control'),
                                            cls='input-group input-group-merge'
                                        ),
                                        cls='mb-6'
                                    ),
                                    Div(
                                        Label('Email', fr='basic-icon-default-email', cls='form-label'),
                                        Div(
                                            Span(
                                                I(cls='ti ti-mail'),
                                                cls='input-group-text'
                                            ),
                                            Input(type='text', id='basic-icon-default-email', placeholder='john.doe', aria_label='john.doe', aria_describedby='basic-icon-default-email2', cls='form-control'),
                                            Span('@example.com', id='basic-icon-default-email2', cls='input-group-text'),
                                            cls='input-group input-group-merge'
                                        ),
                                        Div('You can use letters, numbers & periods', cls='form-text'),
                                        cls='mb-6'
                                    ),
                                    Div(
                                        Label('Phone No', fr='basic-icon-default-phone', cls='form-label'),
                                        Div(
                                            Span(
                                                I(cls='ti ti-phone'),
                                                id='basic-icon-default-phone2',
                                                cls='input-group-text'
                                            ),
                                            Input(type='text', id='basic-icon-default-phone', placeholder='658 799 8941', aria_label='658 799 8941', aria_describedby='basic-icon-default-phone2', cls='form-control phone-mask'),
                                            cls='input-group input-group-merge'
                                        ),
                                        cls='mb-6'
                                    ),
                                    Div(
                                        Label('Message', fr='basic-icon-default-message', cls='form-label'),
                                        Div(
                                            Span(
                                                I(cls='ti ti-message-dots'),
                                                id='basic-icon-default-message2',
                                                cls='input-group-text'
                                            ),
                                            Textarea(id='basic-icon-default-message', placeholder='Hi, Do you have a moment to talk Joe?', aria_label='Hi, Do you have a moment to talk Joe?', aria_describedby='basic-icon-default-message2', cls='form-control'),
                                            cls='input-group input-group-merge'
                                        ),
                                        cls='mb-6'
                                    ),
                                    Button('Send', type='submit', cls='btn btn-primary')
                                ),
                                cls='card-body'
                            ),
                            cls='card'
                        ),
                        cls='col-xl mb-6'
                    ),
                    cls='row'
                ),
                Div(
                    H5('Multi Column with Form Separator', cls='card-header'),
                    Form(
                        H6('1. Account Details'),
                        Div(
                            Div(
                                Label('Username', fr='multicol-username', cls='form-label'),
                                Input(type='text', id='multicol-username', placeholder='john.doe', cls='form-control'),
                                cls='col-md-6'
                            ),
                            Div(
                                Label('Email', fr='multicol-email', cls='form-label'),
                                Div(
                                    Input(type='text', id='multicol-email', placeholder='john.doe', aria_label='john.doe', aria_describedby='multicol-email2', cls='form-control'),
                                    Span('@example.com', id='multicol-email2', cls='input-group-text'),
                                    cls='input-group input-group-merge'
                                ),
                                cls='col-md-6'
                            ),
                            Div(
                                Div(
                                    Label('Password', fr='multicol-password', cls='form-label'),
                                    Div(
                                        Input(type='password', id='multicol-password', placeholder='············', aria_describedby='multicol-password2', cls='form-control'),
                                        Span(
                                            I(cls='ti ti-eye-off'),
                                            id='multicol-password2',
                                            cls='input-group-text cursor-pointer'
                                        ),
                                        cls='input-group input-group-merge'
                                    ),
                                    cls='form-password-toggle'
                                ),
                                cls='col-md-6'
                            ),
                            Div(
                                Div(
                                    Label('Confirm Password', fr='multicol-confirm-password', cls='form-label'),
                                    Div(
                                        Input(type='password', id='multicol-confirm-password', placeholder='············', aria_describedby='multicol-confirm-password2', cls='form-control'),
                                        Span(
                                            I(cls='ti ti-eye-off'),
                                            id='multicol-confirm-password2',
                                            cls='input-group-text cursor-pointer'
                                        ),
                                        cls='input-group input-group-merge'
                                    ),
                                    cls='form-password-toggle'
                                ),
                                cls='col-md-6'
                            ),
                            cls='row g-6'
                        ),
                        Hr(cls='my-6 mx-n4'),
                        H6('2. Personal Info'),
                        Div(
                            Div(
                                Label('First Name', fr='multicol-first-name', cls='form-label'),
                                Input(type='text', id='multicol-first-name', placeholder='John', cls='form-control'),
                                cls='col-md-6'
                            ),
                            Div(
                                Label('Last Name', fr='multicol-last-name', cls='form-label'),
                                Input(type='text', id='multicol-last-name', placeholder='Doe', cls='form-control'),
                                cls='col-md-6'
                            ),
                            Div(
                                Label('Country', fr='multicol-country', cls='form-label'),
                                Select(
                                    Option('Select', value=''),
                                    Option('Australia', value='Australia'),
                                    Option('Bangladesh', value='Bangladesh'),
                                    Option('Belarus', value='Belarus'),
                                    Option('Brazil', value='Brazil'),
                                    Option('Canada', value='Canada'),
                                    Option('China', value='China'),
                                    Option('France', value='France'),
                                    Option('Germany', value='Germany'),
                                    Option('India', value='India'),
                                    Option('Indonesia', value='Indonesia'),
                                    Option('Israel', value='Israel'),
                                    Option('Italy', value='Italy'),
                                    Option('Japan', value='Japan'),
                                    Option('Korea, Republic of', value='Korea'),
                                    Option('Mexico', value='Mexico'),
                                    Option('Philippines', value='Philippines'),
                                    Option('Russian Federation', value='Russia'),
                                    Option('South Africa', value='South Africa'),
                                    Option('Thailand', value='Thailand'),
                                    Option('Turkey', value='Turkey'),
                                    Option('Ukraine', value='Ukraine'),
                                    Option('United Arab Emirates', value='United Arab Emirates'),
                                    Option('United Kingdom', value='United Kingdom'),
                                    Option('United States', value='United States'),
                                    id='multicol-country',
                                    data_allow_clear='true',
                                    cls='select2 form-select'
                                ),
                                cls='col-md-6'
                            ),
                            Div(
                                Label('Language', fr='multicol-language', cls='form-label'),
                                Select(
                                    Option('English', value='en', selected=''),
                                    Option('French', value='fr', selected=''),
                                    Option('German', value='de'),
                                    Option('Portuguese', value='pt'),
                                    id='multicol-language',
                                    multiple='',
                                    cls='select2 form-select'
                                ),
                                cls='col-md-6 select2-primary'
                            ),
                            Div(
                                Label('Birth Date', fr='multicol-birthdate', cls='form-label'),
                                Input(type='text', id='multicol-birthdate', placeholder='YYYY-MM-DD', cls='form-control dob-picker'),
                                cls='col-md-6'
                            ),
                            Div(
                                Label('Phone No', fr='multicol-phone', cls='form-label'),
                                Input(type='text', id='multicol-phone', placeholder='658 799 8941', aria_label='658 799 8941', cls='form-control phone-mask'),
                                cls='col-md-6'
                            ),
                            cls='row g-6'
                        ),
                        Div(
                            Button('Submit', type='submit', cls='btn btn-primary me-4'),
                            Button('Cancel', type='reset', cls='btn btn-label-secondary'),
                            cls='pt-6'
                        ),
                        cls='card-body'
                    ),
                    cls='card mb-6'
                ),
                Div(
                    Div(
                        H6('Collapsible Section'),
                        Div(
                            Div(
                                H2(
                                    Button('Delivery Address', type='button', data_bs_toggle='collapse', data_bs_target='#collapseDeliveryAddress', aria_expanded='true', aria_controls='collapseDeliveryAddress', cls='accordion-button'),
                                    id='headingDeliveryAddress',
                                    cls='accordion-header'
                                ),
                                Div(
                                    Div(
                                        Div(
                                            Div(
                                                Label('Full Name', fr='collapsible-fullname', cls='form-label'),
                                                Input(type='text', id='collapsible-fullname', placeholder='John Doe', cls='form-control'),
                                                cls='col-md-6'
                                            ),
                                            Div(
                                                Label('Phone No', fr='collapsible-phone', cls='form-label'),
                                                Input(type='text', id='collapsible-phone', placeholder='658 799 8941', aria_label='658 799 8941', cls='form-control phone-mask'),
                                                cls='col-md-6'
                                            ),
                                            Div(
                                                Label('Address', fr='collapsible-address', cls='form-label'),
                                                Textarea(name='collapsible-address', id='collapsible-address', rows='2', placeholder='1456, Mall Road', cls='form-control'),
                                                cls='col-12'
                                            ),
                                            Div(
                                                Label('Pincode', fr='collapsible-pincode', cls='form-label'),
                                                Input(type='text', id='collapsible-pincode', placeholder='658468', cls='form-control'),
                                                cls='col-md-6'
                                            ),
                                            Div(
                                                Label('Landmark', fr='collapsible-landmark', cls='form-label'),
                                                Input(type='text', id='collapsible-landmark', placeholder='Nr. Wall Street', cls='form-control'),
                                                cls='col-md-6'
                                            ),
                                            Div(
                                                Label('City', fr='collapsible-city', cls='form-label'),
                                                Input(type='text', id='collapsible-city', placeholder='Jackson', cls='form-control'),
                                                cls='col-md-6'
                                            ),
                                            Div(
                                                Label('State', fr='collapsible-state', cls='form-label'),
                                                Select(
                                                    Option('Select', value=''),
                                                    Option('Alabama', value='AL'),
                                                    Option('Alaska', value='AK'),
                                                    Option('Arizona', value='AZ'),
                                                    Option('Arkansas', value='AR'),
                                                    Option('California', value='CA'),
                                                    Option('Colorado', value='CO'),
                                                    Option('Connecticut', value='CT'),
                                                    Option('Delaware', value='DE'),
                                                    Option('District Of Columbia', value='DC'),
                                                    Option('Florida', value='FL'),
                                                    Option('Georgia', value='GA'),
                                                    Option('Hawaii', value='HI'),
                                                    Option('Idaho', value='ID'),
                                                    Option('Illinois', value='IL'),
                                                    Option('Indiana', value='IN'),
                                                    Option('Iowa', value='IA'),
                                                    Option('Kansas', value='KS'),
                                                    Option('Kentucky', value='KY'),
                                                    Option('Louisiana', value='LA'),
                                                    Option('Maine', value='ME'),
                                                    Option('Maryland', value='MD'),
                                                    Option('Massachusetts', value='MA'),
                                                    Option('Michigan', value='MI'),
                                                    Option('Minnesota', value='MN'),
                                                    Option('Mississippi', value='MS'),
                                                    Option('Missouri', value='MO'),
                                                    Option('Montana', value='MT'),
                                                    Option('Nebraska', value='NE'),
                                                    Option('Nevada', value='NV'),
                                                    Option('New Hampshire', value='NH'),
                                                    Option('New Jersey', value='NJ'),
                                                    Option('New Mexico', value='NM'),
                                                    Option('New York', value='NY'),
                                                    Option('North Carolina', value='NC'),
                                                    Option('North Dakota', value='ND'),
                                                    Option('Ohio', value='OH'),
                                                    Option('Oklahoma', value='OK'),
                                                    Option('Oregon', value='OR'),
                                                    Option('Pennsylvania', value='PA'),
                                                    Option('Rhode Island', value='RI'),
                                                    Option('South Carolina', value='SC'),
                                                    Option('South Dakota', value='SD'),
                                                    Option('Tennessee', value='TN'),
                                                    Option('Texas', value='TX'),
                                                    Option('Utah', value='UT'),
                                                    Option('Vermont', value='VT'),
                                                    Option('Virginia', value='VA'),
                                                    Option('Washington', value='WA'),
                                                    Option('West Virginia', value='WV'),
                                                    Option('Wisconsin', value='WI'),
                                                    Option('Wyoming', value='WY'),
                                                    id='collapsible-state',
                                                    data_allow_clear='true',
                                                    cls='select2 form-select'
                                                ),
                                                cls='col-md-6'
                                            ),
                                            Label('Address Type', cls='form-check-label'),
                                            Div(
                                                Div(
                                                    Input(name='collapsible-address-type', type='radio', value='', id='collapsible-address-type-home', checked='', cls='form-check-input'),
                                                    Label('Home (All day delivery)', fr='collapsible-address-type-home', cls='form-check-label'),
                                                    cls='form-check form-check-inline'
                                                ),
                                                Div(
                                                    Input(name='collapsible-address-type', type='radio', value='', id='collapsible-address-type-office', cls='form-check-input'),
                                                    Label('Office (Delivery between 10 AM - 5 PM)', fr='collapsible-address-type-office', cls='form-check-label'),
                                                    cls='form-check form-check-inline'
                                                ),
                                                cls='col mt-2'
                                            ),
                                            cls='row g-6'
                                        ),
                                        cls='accordion-body'
                                    ),
                                    id='collapseDeliveryAddress',
                                    data_bs_parent='#collapsibleSection',
                                    cls='accordion-collapse collapse show'
                                ),
                                cls='card accordion-item active'
                            ),
                            Div(
                                H2(
                                    Button('Delivery Options', type='button', data_bs_toggle='collapse', data_bs_target='#collapseDeliveryOptions', aria_expanded='false', aria_controls='collapseDeliveryOptions', cls='accordion-button collapsed'),
                                    id='headingDeliveryOptions',
                                    cls='accordion-header'
                                ),
                                Div(
                                    Div(
                                        Div(
                                            Div(
                                                Div(
                                                    Label(
                                                        Input(name='CustomRadioDelivery', type='radio', value='', id='radioStandard', checked='', cls='form-check-input'),
                                                        Span(
                                                            Span('Standard 3-5 Days', cls='h6 mb-0'),
                                                            Span('Free', cls='text-muted'),
                                                            cls='custom-option-header'
                                                        ),
                                                        Span(
                                                            Small('Friday, 15 Nov - Monday, 18 Nov'),
                                                            cls='custom-option-body'
                                                        ),
                                                        fr='radioStandard',
                                                        cls='form-check-label custom-option-content'
                                                    ),
                                                    cls='form-check custom-option custom-option-basic'
                                                ),
                                                cls='col-md mb-md-0 mb-2'
                                            ),
                                            Div(
                                                Div(
                                                    Label(
                                                        Input(name='CustomRadioDelivery', type='radio', value='', id='radioExpress', cls='form-check-input'),
                                                        Span(
                                                            Span('Express', cls='h6 mb-0'),
                                                            Span('$5.00', cls='text-muted'),
                                                            cls='custom-option-header'
                                                        ),
                                                        Span(
                                                            Small('Friday, 15 Nov - Sunday, 17 Nov'),
                                                            cls='custom-option-body'
                                                        ),
                                                        fr='radioExpress',
                                                        cls='form-check-label custom-option-content'
                                                    ),
                                                    cls='form-check custom-option custom-option-basic'
                                                ),
                                                cls='col-md mb-md-0 mb-2'
                                            ),
                                            Div(
                                                Div(
                                                    Label(
                                                        Input(name='CustomRadioDelivery', type='radio', value='', id='radioOvernight', cls='form-check-input'),
                                                        Span(
                                                            Span('Overnight', cls='h6 mb-0'),
                                                            Span('$10.00', cls='text-muted'),
                                                            cls='custom-option-header'
                                                        ),
                                                        Span(
                                                            Small('Friday, 15 Nov - Saturday, 16 Nov'),
                                                            cls='custom-option-body'
                                                        ),
                                                        fr='radioOvernight',
                                                        cls='form-check-label custom-option-content'
                                                    ),
                                                    cls='form-check custom-option custom-option-basic'
                                                ),
                                                cls='col-md'
                                            ),
                                            cls='row'
                                        ),
                                        cls='accordion-body'
                                    ),
                                    id='collapseDeliveryOptions',
                                    aria_labelledby='headingDeliveryOptions',
                                    data_bs_parent='#collapsibleSection',
                                    cls='accordion-collapse collapse'
                                ),
                                cls='card accordion-item'
                            ),
                            Div(
                                H2(
                                    Button('Payment Method', type='button', data_bs_toggle='collapse', data_bs_target='#collapsePaymentMethod', aria_expanded='false', aria_controls='collapsePaymentMethod', cls='accordion-button collapsed'),
                                    id='headingPaymentMethod',
                                    cls='accordion-header'
                                ),
                                Div(
                                    Form(
                                        Div(
                                            Div(
                                                Div(
                                                    Input(name='collapsible-payment', type='radio', value='credit-card', id='collapsible-payment-cc', checked='', cls='form-check-input form-check-input-payment'),
                                                    Label(
                                                        'Credit/Debit/ATM Card',
                                                        I(cls='ti ti-credit-card'),
                                                        fr='collapsible-payment-cc',
                                                        cls='form-check-label'
                                                    ),
                                                    cls='form-check form-check-inline'
                                                ),
                                                Div(
                                                    Input(name='collapsible-payment', type='radio', value='cash', id='collapsible-payment-cash', cls='form-check-input form-check-input-payment'),
                                                    Label(
                                                        'Cash On Delivery',
                                                        I(data_bs_toggle='tooltip', data_bs_placement='top', title='You can pay once you receive the product.', cls='ti ti-help'),
                                                        fr='collapsible-payment-cash',
                                                        cls='form-check-label'
                                                    ),
                                                    cls='form-check form-check-inline'
                                                ),
                                                cls='mb-6'
                                            ),
                                            Div(
                                                Div(
                                                    Div(
                                                        Label('Card Number', fr='creditCardMask', cls='form-label w-100'),
                                                        Div(
                                                            Input(type='text', id='creditCardMask', name='creditCardMask', placeholder='1356 3215 6548 7898', aria_describedby='creditCardMask2', cls='form-control credit-card-mask'),
                                                            Span(
                                                                Span(cls='card-type'),
                                                                id='creditCardMask2',
                                                                cls='input-group-text cursor-pointer p-1'
                                                            ),
                                                            cls='input-group input-group-merge'
                                                        ),
                                                        cls='mb-6'
                                                    ),
                                                    Div(
                                                        Div(
                                                            Div(
                                                                Label('Name', fr='collapsible-payment-name', cls='form-label'),
                                                                Input(type='text', id='collapsible-payment-name', placeholder='John Doe', cls='form-control'),
                                                                cls='mb-6'
                                                            ),
                                                            cls='col-12 col-md-6'
                                                        ),
                                                        Div(
                                                            Div(
                                                                Label('Exp. Date', fr='collapsible-payment-expiry-date', cls='form-label'),
                                                                Input(type='text', id='collapsible-payment-expiry-date', placeholder='MM/YY', cls='form-control expiry-date-mask'),
                                                                cls='mb-6'
                                                            ),
                                                            cls='col-6 col-md-3'
                                                        ),
                                                        Div(
                                                            Div(
                                                                Label('CVV Code', fr='collapsible-payment-cvv', cls='form-label'),
                                                                Div(
                                                                    Input(type='text', id='collapsible-payment-cvv', maxlength='3', placeholder='654', cls='form-control cvv-code-mask'),
                                                                    Span(
                                                                        I(data_bs_toggle='tooltip', data_bs_placement='top', title='Card Verification Value', cls='ti ti-help text-muted'),
                                                                        id='collapsible-payment-cvv2',
                                                                        cls='input-group-text cursor-pointer'
                                                                    ),
                                                                    cls='input-group input-group-merge'
                                                                ),
                                                                cls='mb-6'
                                                            ),
                                                            cls='col-6 col-md-3'
                                                        ),
                                                        cls='row'
                                                    ),
                                                    cls='col-12 col-md-8 col-xl-6'
                                                ),
                                                id='form-credit-card',
                                                cls='row'
                                            ),
                                            Div(
                                                Button('Submit', type='submit', cls='btn btn-primary me-4'),
                                                Button('Cancel', type='reset', cls='btn btn-label-secondary'),
                                                cls='mt-1'
                                            ),
                                            cls='accordion-body'
                                        )
                                    ),
                                    id='collapsePaymentMethod',
                                    aria_labelledby='headingPaymentMethod',
                                    data_bs_parent='#collapsibleSection',
                                    cls='accordion-collapse collapse'
                                ),
                                cls='card accordion-item'
                            ),
                            id='collapsibleSection',
                            cls='accordion'
                        ),
                        cls='col'
                    ),
                    cls='row my-6'
                ),
                Div(
                    Div(
                        H6('Form with Tabs', cls='mt-6'),
                        Div(
                            Div(
                                Div(
                                    Ul(
                                        Li(
                                            Button(
                                                Span(cls='ti ti-user ti-lg d-sm-none'),
                                                Span('Personal Info', cls='d-none d-sm-block'),
                                                type='button',
                                                data_bs_toggle='tab',
                                                data_bs_target='#form-tabs-personal',
                                                aria_controls='form-tabs-personal',
                                                role='tab',
                                                aria_selected='true',
                                                cls='nav-link active'
                                            ),
                                            cls='nav-item'
                                        ),
                                        Li(
                                            Button(
                                                Span(cls='ti ti-user-cog ti-lg d-sm-none'),
                                                Span('Account Details', cls='d-none d-sm-block'),
                                                type='button',
                                                data_bs_toggle='tab',
                                                data_bs_target='#form-tabs-account',
                                                aria_controls='form-tabs-account',
                                                role='tab',
                                                aria_selected='false',
                                                cls='nav-link'
                                            ),
                                            cls='nav-item'
                                        ),
                                        Li(
                                            Button(
                                                Span(cls='ti ti-link ti-lg d-sm-none'),
                                                Span('Social Links', cls='d-none d-sm-block'),
                                                type='button',
                                                data_bs_toggle='tab',
                                                data_bs_target='#form-tabs-social',
                                                aria_controls='form-tabs-social',
                                                role='tab',
                                                aria_selected='false',
                                                cls='nav-link'
                                            ),
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
                                        Form(
                                            Div(
                                                Div(
                                                    Label('First Name', fr='formtabs-first-name', cls='form-label'),
                                                    Input(type='text', id='formtabs-first-name', placeholder='John', cls='form-control'),
                                                    cls='col-md-6'
                                                ),
                                                Div(
                                                    Label('Last Name', fr='formtabs-last-name', cls='form-label'),
                                                    Input(type='text', id='formtabs-last-name', placeholder='Doe', cls='form-control'),
                                                    cls='col-md-6'
                                                ),
                                                Div(
                                                    Label('Country', fr='formtabs-country', cls='form-label'),
                                                    Select(
                                                        Option('Select', value=''),
                                                        Option('Australia', value='Australia'),
                                                        Option('Bangladesh', value='Bangladesh'),
                                                        Option('Belarus', value='Belarus'),
                                                        Option('Brazil', value='Brazil'),
                                                        Option('Canada', value='Canada'),
                                                        Option('China', value='China'),
                                                        Option('France', value='France'),
                                                        Option('Germany', value='Germany'),
                                                        Option('India', value='India'),
                                                        Option('Indonesia', value='Indonesia'),
                                                        Option('Israel', value='Israel'),
                                                        Option('Italy', value='Italy'),
                                                        Option('Japan', value='Japan'),
                                                        Option('Korea, Republic of', value='Korea'),
                                                        Option('Mexico', value='Mexico'),
                                                        Option('Philippines', value='Philippines'),
                                                        Option('Russian Federation', value='Russia'),
                                                        Option('South Africa', value='South Africa'),
                                                        Option('Thailand', value='Thailand'),
                                                        Option('Turkey', value='Turkey'),
                                                        Option('Ukraine', value='Ukraine'),
                                                        Option('United Arab Emirates', value='United Arab Emirates'),
                                                        Option('United Kingdom', value='United Kingdom'),
                                                        Option('United States', value='United States'),
                                                        id='formtabs-country',
                                                        data_allow_clear='true',
                                                        cls='select2 form-select'
                                                    ),
                                                    cls='col-md-6'
                                                ),
                                                Div(
                                                    Label('Language', fr='formtabs-language', cls='form-label'),
                                                    Select(
                                                        Option('English', value='en', selected=''),
                                                        Option('French', value='fr', selected=''),
                                                        Option('German', value='de'),
                                                        Option('Portuguese', value='pt'),
                                                        id='formtabs-language',
                                                        multiple='',
                                                        cls='select2 form-select'
                                                    ),
                                                    cls='col-md-6 select2-primary'
                                                ),
                                                Div(
                                                    Label('Birth Date', fr='formtabs-birthdate', cls='form-label'),
                                                    Input(type='text', id='formtabs-birthdate', placeholder='YYYY-MM-DD', cls='form-control dob-picker'),
                                                    cls='col-md-6'
                                                ),
                                                Div(
                                                    Label('Phone No', fr='formtabs-phone', cls='form-label'),
                                                    Input(type='text', id='formtabs-phone', placeholder='658 799 8941', aria_label='658 799 8941', cls='form-control phone-mask'),
                                                    cls='col-md-6'
                                                ),
                                                cls='row g-6'
                                            ),
                                            Div(
                                                Button('Submit', type='submit', cls='btn btn-primary me-4'),
                                                Button('Cancel', type='reset', cls='btn btn-label-secondary'),
                                                cls='pt-6'
                                            )
                                        ),
                                        id='form-tabs-personal',
                                        role='tabpanel',
                                        cls='tab-pane fade active show'
                                    ),
                                    Div(
                                        Form(
                                            Div(
                                                Div(
                                                    Label('Username', fr='formtabs-username', cls='form-label'),
                                                    Input(type='text', id='formtabs-username', placeholder='john.doe', cls='form-control'),
                                                    cls='col-md-6'
                                                ),
                                                Div(
                                                    Label('Email', fr='formtabs-email', cls='form-label'),
                                                    Div(
                                                        Input(type='text', id='formtabs-email', placeholder='john.doe', aria_label='john.doe', aria_describedby='formtabs-email2', cls='form-control'),
                                                        Span('@example.com', id='formtabs-email2', cls='input-group-text'),
                                                        cls='input-group input-group-merge'
                                                    ),
                                                    cls='col-md-6'
                                                ),
                                                Div(
                                                    Div(
                                                        Label('Password', fr='formtabs-password', cls='form-label'),
                                                        Div(
                                                            Input(type='password', id='formtabs-password', placeholder='············', aria_describedby='formtabs-password2', cls='form-control'),
                                                            Span(
                                                                I(cls='ti ti-eye-off'),
                                                                id='formtabs-password2',
                                                                cls='input-group-text cursor-pointer'
                                                            ),
                                                            cls='input-group input-group-merge'
                                                        ),
                                                        cls='form-password-toggle'
                                                    ),
                                                    cls='col-md-6'
                                                ),
                                                Div(
                                                    Div(
                                                        Label('Confirm Password', fr='formtabs-confirm-password', cls='form-label'),
                                                        Div(
                                                            Input(type='password', id='formtabs-confirm-password', placeholder='············', aria_describedby='formtabs-confirm-password2', cls='form-control'),
                                                            Span(
                                                                I(cls='ti ti-eye-off'),
                                                                id='formtabs-confirm-password2',
                                                                cls='input-group-text cursor-pointer'
                                                            ),
                                                            cls='input-group input-group-merge'
                                                        ),
                                                        cls='form-password-toggle'
                                                    ),
                                                    cls='col-md-6'
                                                ),
                                                cls='row g-6'
                                            ),
                                            Div(
                                                Button('Submit', type='submit', cls='btn btn-primary me-4'),
                                                Button('Cancel', type='reset', cls='btn btn-label-secondary'),
                                                cls='pt-6'
                                            )
                                        ),
                                        id='form-tabs-account',
                                        role='tabpanel',
                                        cls='tab-pane fade'
                                    ),
                                    Div(
                                        Form(
                                            Div(
                                                Div(
                                                    Label('Twitter', fr='formtabs-twitter', cls='form-label'),
                                                    Input(type='text', id='formtabs-twitter', placeholder='https://twitter.com/abc', cls='form-control'),
                                                    cls='col-md-6'
                                                ),
                                                Div(
                                                    Label('Facebook', fr='formtabs-facebook', cls='form-label'),
                                                    Input(type='text', id='formtabs-facebook', placeholder='https://facebook.com/abc', cls='form-control'),
                                                    cls='col-md-6'
                                                ),
                                                Div(
                                                    Label('Google+', fr='formtabs-google', cls='form-label'),
                                                    Input(type='text', id='formtabs-google', placeholder='https://plus.google.com/abc', cls='form-control'),
                                                    cls='col-md-6'
                                                ),
                                                Div(
                                                    Label('Linkedin', fr='formtabs-linkedin', cls='form-label'),
                                                    Input(type='text', id='formtabs-linkedin', placeholder='https://linkedin.com/abc', cls='form-control'),
                                                    cls='col-md-6'
                                                ),
                                                Div(
                                                    Label('Instagram', fr='formtabs-instagram', cls='form-label'),
                                                    Input(type='text', id='formtabs-instagram', placeholder='https://instagram.com/abc', cls='form-control'),
                                                    cls='col-md-6'
                                                ),
                                                Div(
                                                    Label('Quora', fr='formtabs-quora', cls='form-label'),
                                                    Input(type='text', id='formtabs-quora', placeholder='https://quora.com/abc', cls='form-control'),
                                                    cls='col-md-6'
                                                ),
                                                cls='row g-6'
                                            ),
                                            Div(
                                                Button('Submit', type='submit', cls='btn btn-primary me-4'),
                                                Button('Cancel', type='reset', cls='btn btn-label-secondary'),
                                                cls='pt-6'
                                            )
                                        ),
                                        id='form-tabs-social',
                                        role='tabpanel',
                                        cls='tab-pane fade'
                                    ),
                                    cls='tab-content p-0'
                                ),
                                cls='card-body'
                            ),
                            cls='card mb-6'
                        ),
                        cls='col'
                    ),
                    cls='row'
                ),
                Div(
                    H5('Form Alignment', cls='card-header'),
                    Div(
                        Div(
                            Form(
                                H3('Sign In', cls='mb-6'),
                                Div(
                                    Label('Username', fr='form-alignment-username', cls='form-label'),
                                    Input(type='text', id='form-alignment-username', placeholder='john.doe', cls='form-control'),
                                    cls='mb-6'
                                ),
                                Div(
                                    Label('Password', fr='form-alignment-password', cls='form-label'),
                                    Div(
                                        Input(type='password', id='form-alignment-password', placeholder='············', aria_describedby='form-alignment-password2', cls='form-control'),
                                        Span(
                                            I(cls='ti ti-eye-off'),
                                            id='form-alignment-password2',
                                            cls='input-group-text cursor-pointer'
                                        ),
                                        cls='input-group input-group-merge'
                                    ),
                                    cls='mb-6 form-password-toggle'
                                ),
                                Div(
                                    Label(
                                        Input(type='checkbox', cls='form-check-input'),
                                        Span('Remember me', cls='form-check-label'),
                                        cls='form-check m-0'
                                    ),
                                    cls='mb-6'
                                ),
                                Div(
                                    Button('Login', type='submit', cls='btn btn-primary'),
                                    cls='d-grid gap-2'
                                ),
                                cls='w-px-400 border rounded p-3 p-md-5'
                            ),
                            cls='d-flex align-items-center justify-content-center h-px-500'
                        ),
                        cls='card-body'
                    ),
                    cls='card'
                )
            ),
            session=session
        )