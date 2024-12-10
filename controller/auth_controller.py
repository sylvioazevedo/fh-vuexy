from datetime import datetime as dt
from base.engine import get_app
from etc import settings
from fh_vuexy import *
from service.hanzo_service import HanzoService
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

                    # file extensions
                    r'.*\.css', r'.*\.js', r'.*\.map', r'.*\.svg', r'.*\.jpg', r'.*\.jpg', r'.*\.png', r'.*\.ico',
                    r'.*\.mp3', r'.*\.wav', r'.*\.ogg', r'.*\.woff2', r'.*\.woff', r'.*\.ttf', r'.*\.eot', r'.*\.otf'
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

    auth_server = HanzoService(session=session)

    try:
        auth_server.login(username, password)                
        session['user'] = auth_server.find_user_by_username(username)
    
        return Redirect('/')
    
    except Exception as e:
        return login(session, str(e))
    
@rt('/logout')
def logout(session):
    session.clear()
    return Redirect('/auth')