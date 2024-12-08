from fh_vuexy import *
from view.templates.main_layout import MainLayout

def MainPage(session, **kwargs):

    session['active'] = 'Dashboard'    

    # check if there is a error message
    error = session.pop('error', None)

    return \
        MainLayout('Vuejs Vuexy Template',
            Page(                
                'Dashboard',
                Alert( f'{error}', type=AlertTypeT.Danger) if error else None,
                P(
                    'Sample page.',
                    Br(),
                    'For more layout options, ',
                    A(
                        href="",
                        target="_blank",
                        cls="fw-medium"
                    ),
                    ' refer ',
                    A(
                        'Layout docs',
                        href="https://demos.pixinvent.com/vuexy-html-admin-template/documentation//layouts.html",
                        target="_blank",
                        cls="fw-medium"
                    )                  
                )
            ),
            session=session
        )