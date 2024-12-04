from etc.settings import APP_NAME
from fh_vuexy import *
from view.templates.main_layout import MainLayout

def LoginPage(session, error = None):

    session['active'] = 'Login'

    return \
        MainLayout(f'{APP_NAME} - Login',
            Page(
                Div(
                    Div(
                        Form(
                            Alert(Small(error), type=AlertTypeT.Danger, icon='ti ti-ban', cls='mb-2') if error else None,
                            H4('Sign In', cls='card-title mL-2'),
                            Div(
                                Label('Username', fr='username', cls='form-label'),
                                Input(placeholder='John Doe', id='username', type='text', cls='form-control'),
                                cls='mb-3',
                            ),
                            Div(
                                Label('Password', fr='password', cls='form-label'),
                                Div(
                                    Input(
                                        placeholder='********',
                                        id='password',
                                        type='password',
                                        cls='form-control',
                                        aria_describedby='toggle-password',
                                    ),
                                    Span(
                                        I(cls='fe fe-eye-off'),
                                        id='toggle-password',
                                        cls='input-group-text cursor-pointer',
                                    ),
                                    cls='input-group input-group-merge'
                                ),
                                cls='form-password-toggle mb-3',
                            ),
                            Div(
                                Button(Span(I(cls='ti ti-login-2 me-2'), 'Sign In'), cls='btn btn-primary btn-block', type='submit'),
                                cls='d-grip gap-2'
                            ),
                            cls = 'card-body w-px-400 border rounded p-3 p-md-5',
                            action='/auth/login',
                            method='POST'
                        ),                        
                        cls='card'
                    ),
                    cls='d-flex align-items-center justify-content-center h-px-500'    
                ),
                
            ),
            session=session
        )