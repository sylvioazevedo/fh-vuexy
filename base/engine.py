from fh_vuexy import *

def get_app(**kwargs):
    
    return fast_app(
        pico=False,
        default_hdrs=False,
        hdrs=vuexy_hdrs + (kwargs['hdrs_ext'] if 'hdrs_ext' in kwargs else ('',)),
        ftrs=vuexy_ftrs + (kwargs['ftrs_ext'] if 'ftrs_ext' in kwargs else ('',)),
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
        bodykw={'style': 'background-image: url("/img/backgrounds/hanzo_wp.jpg"); background-size: cover;'},
        **kwargs
    )