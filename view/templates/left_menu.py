from fh_vuexy import *

def LeftMenu(session):

    return \
        VerticalMenu(
            'layout-menu',
            items=(
                VerticalMenuItem('Dashboard', icon='ti ti-home', href='/', active=session['active'] == 'Dashboard'),
                VerticalMenuItem('Page 2', icon='ti ti-smart-home', href='#'),
                VerticalMenuItem('Page 3', icon='ti ti-app-window', href='#'),
                VerticalMenuItem('Forms', icon='ti ti-forms', href='/forms', active=session['active'] == 'Forms'),
                VerticalMenuItem('Cards', icon='ti ti-id', href='/cards', active=session['active'] == 'Cards'),
            ),
            brand_logo=Img(src='/img/logo/vuexy.svg', alt='brand-logo', class_='brand-logo'),
            brand_text='Vuexy'                
        ),