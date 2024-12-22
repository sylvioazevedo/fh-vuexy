from fh_vuexy import *

def LeftMenu(session):

    access_token = session['access_token'] if 'access_token' in session else None
    items = (VerticalMenuItem('Dashboard', icon='ti ti-home', href='/', active=session['active'] == 'Dashboard'), Divider())

    if access_token:

        user = session['user']
        role = user['role']

        items += (
            VerticalMenuGroup(
                'Components',
                VerticalMenuItem('Forms', icon='ti ti-forms', href='/forms', active=session['active'] == 'Forms'),
                VerticalMenuItem('Cards', icon='ti ti-id', href='/cards', active=session['active'] == 'Cards'),
                icon='ti ti-package',
                active=session['active'] in ['Forms', 'Cards']
            ),
            # kenkun|left_menu                        
            VerticalMenuItem('Tests', icon='ti ti-point', href='/test', active=session['active'] == 'Tests'),
            Divider() if role == 'admin' else None,
            VerticalMenuItem('Users', icon='ti ti-user', href='/user', active=session['active'] == 'Users') if role == 'admin' else None,
            Divider(),
            VerticalMenuItem('Logout', icon='ti ti-logout', href='/auth/logout'),
        )

    return \
        VerticalMenu(
            'layout-menu',
            items,
            brand_logo=Img(src='/img/logo/st_logo.png', alt='brand-logo', width=24, cls='brand-logo'),
            brand_text='Vuexy'                
        ),