from fh_vuexy import *
from view.templates.main_layout import MainLayout

def MainPage(session):

    session['active'] = 'Dashboard'

    return \
        MainLayout('Vuejs Vuexy Template',
            Page(
                'Dashboard',
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