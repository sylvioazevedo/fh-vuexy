from datetime import datetime as dt
from engine import get_app
from etc import settings
from fh_vuexy import *
from services.hanzo_client import HanzoClient
from view.auth import LoginPage

def check_auth(request, session):

    access_token = request.scope['access_token'] = session['access_token'] if 'access_token' in session else None
    request.scope['refresh_token'] = session['refresh_token'] if 'refresh_token' in session else None

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

    auth_server = HanzoClient(settings.HANZO_API_URI, session=session)

    try:
        auth_server.login(username, password)                
        session['user'] = auth_server.get_user_by_username(username)
    
        return Redirect('/')
    
    except Exception as e:
        return login(session, str(e))
    
@rt('/logout')
def logout(session):
    session.clear()
    return Redirect('/auth')