from fh_vuexy import *

def TopMenu(session):

    access_token = session['access_token'] if 'access_token' in session else None

    if access_token:
        user = session['user']
        role: str = user['role']

        items = (
            NavBarAvatar(
                user['name'] if 'name' in user else user['username'],
                role.title(),
                NavBarAvatarItem(
                    'My Profile',
                    icon='ti ti-user me-3 ti-md',
                    href='/profile'
                ),                
                NavBarAvatarItem(
                    'Settings',
                    icon='ti ti-settings me-3 ti-md',
                    href='#'
                ) if role == 'admin' else None,
                # NavBarAvatarNotifyItem(
                #     'Billing',
                #     notify='4',
                #     icon='ti ti-file-dollar me-3 ti-md',
                #     href='#'
                # ),
                Divider(),
                NavBarDropDownButton('Logout', icon='ti ti-logout', href='#', cls='btn-danger'),
                img_src='/img/avatars/1.png',
                status='offline'
            )
        )
    else:
        items = StyledButton('Login', icon='ti ti-login-2', cls='btn btn-primary', href='/auth')

    return \
        NavBarLayout(
            items,
            id='layout-navbar',
            light_controls=True
        )