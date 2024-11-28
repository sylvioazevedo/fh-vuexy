from fh_vuexy import *
from view.templates.footer import AppFooter
from view.templates.left_menu import LeftMenu
from view.templates.top_menu import TopMenu

def MainLayout(title, *content, session=None):
    return \
        Title(title), \
        Layout(
            LeftMenu(session),
            LayoutPage(
                TopMenu(session),
                *content,
                AppFooter(session)
            )
        )