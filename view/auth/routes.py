from engine import get_app
from controller.hanzo_client import HanzoClient
from datetime import datetime as dt
from etc import settings
from fh_vuexy import *
from view.auth import LoginPage

import requests

def check_auth(request, session):

    access_token = request.scope['access_token'] = session['access_token'] if 'access_token' in session else None    

    if not access_token:
        return RedirectResponse(url='/auth', status_code=303)
    
beforeware = Beforeware(
                check_auth,
                skip=[
                    '/', '/auth', '/login',                     # routes
                    r'/favicon\.ico',                           # files
                    r'/img/.*', r'/audio/.*',                   # folders
                    r'.*\.css', r'.*\.js', r'.*\.map', r'.*\.svg',  # file extensions
                ]
            )

auth_app, rt = get_app()

@rt('/')
def login(session, message=None):
    return LoginPage(session, message)

@rt('/login')
async def post(request: Request, session):    

    form_data = await request.form()    

    username = form_data.get('username').strip()
    password = form_data.get('password').strip()

    print(f'username: {username}, password: {password}')

    auth_server = HanzoClient(settings.HANZO_API_URI)

    try:
        access_token, refresh_token = auth_server.login(username, password)        
        session['access_token'] = access_token
        session['refresh_token'] = refresh_token
        session['user'] = auth_server.get_user_by_username(username)
    
        return Redirect('/')
    
    except Exception as e:
        return login(session, str(e))
    
@rt('/logout')
def logout(session):
    session.clear()
    return Redirect('/auth')