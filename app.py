from fh_vuexy import *

from view.cards_page import CardsPage
from view.forms_page import FormsPage
from view.main_page import MainPage
from view.profile_page import ProfilePage

reg_re_param("static", "ico|gif|jpg|jpeg|webm|css|js|woff|png|svg|mp4|webp|ttf|otf|eot|woff2|txt|html|map|json|mp3")

hdrs = (
    Meta(charset='utf-8'),
    Meta(name='viewport', content='width=device-width, initial-scale=1.0, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0'),
) + vuexy_hdrs + (Favicon('/img/favicon/favicon.ico', '/img/favicon/favicon.ico'),)

app, rt = fast_app(
        pico=False,
        default_hdrs=False,
        hdrs=hdrs,
        ftrs=vuexy_ftrs,        
        static_path='assets',
        htmlkw={
            'lang': 'en',
            'class': 'light-style layout-navbar-fixed layout-menu-fixed layout-compact',
            'dir': 'ltr',
            'data-theme': 'theme-default',
            'data-assets-path': '/',
            'data-templates': 'vertical-menu-template-starter',
            'data-style': 'light',            
        },
        bodykw={'style': 'background-image: url("/img/backgrounds/7.jpg"); background-size: cover;'}
    )

@rt('/')
def index(session):
    return MainPage(session)

@rt('/cards')
def index(session):
    return CardsPage(session)


@rt('/forms')
def index(session):
    return FormsPage(session)

@rt('/profile')
def index(session):    
    return ProfilePage(session)

serve()


