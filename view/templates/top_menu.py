from fh_vuexy import *

def TopMenu(session):
    return \
        NavBarLayout(
            NavBarAvatar(
                'John Doe', 'Admin',
                NavBarAvatarItem(
                    'My Profile',
                    icon='ti ti-user me-3 ti-md',
                    href='/profile'
                ),
                NavBarAvatarItem(
                    'Settings',
                    icon='ti ti-settings me-3 ti-md',
                    href='#'
                ),
                NavBarAvatarNotifyItem(
                    'Billing',
                    notify='4',
                    icon='ti ti-file-dollar me-3 ti-md',
                    href='#'
                ),
                Divider(),
                NavBarDropDownButton('Logout', icon='ti ti-power-off', href='#', cls='btn-danger'),
                img_src='/img/avatars/1.png',
                status='offline'
            ),
            id='layout-navbar',
            light_controls=True
        )