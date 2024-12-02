from datetime import datetime as dt

import requests

class HanzoClient():

    def __init__(self, api_url:str=None):

        self.api_url = api_url if api_url else 'http://127.0.0.1:35777'

        # set headers
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        # connection tokens
        self.access_token = None
        self.refresh_token = None

        # get session
        self.session = requests.Session()

    def login(self, username:str, password:str):
        """
        login to the hanzo api
        """        

        url = f'{self.api_url}/login'
        data = {
            'username': username,
            'password': password
        }

        begin = dt.now()
        response = requests.post(url, json=data)
        print(f'login time: {dt.now() - begin}')

        if response.status_code != 200:
            raise Exception(f'Login request failed: {str(response.status_code)} - {response.reason}')
        
        response_data = response.json()

        self.access_token = response_data['access_token']
        self.refresh_token = response_data['refresh_token']

        # set authorization header
        self.headers['Authorization'] = 'Bearer ' + self.access_token

        return self.access_token, self.refresh_token
  
    def refresh(self):
        """
        refresh the access token
        """
        url = f'{self.api_url}/refresh'
        refresh_headers = {'Authorization': 'Bearer ' + self.refresh_token}

        response = requests.post(url, headers=refresh_headers)
        response_data = response.json()

        if response.status_code != 200:
            raise Exception(f'Refresh request failed: {str(response.status_code)} - {response.reason}')
        
        self.access_token = response_data['access_token']
        self.refresh_token = response_data['refresh_token']

        # set authorization header
        self.headers['Authorization'] = 'Bearer ' + self.access_token

        return self.access_token
        
        
    def set_access_token(self, access_token:str):
        """
        set the access token
        """
        self.access_token = access_token
        self.headers['Authorization'] = 'Bearer ' + self.access_token

    def set_refresh_token(self, refresh_token:str):
        """
        set the refresh token
        """
        self.refresh_token = refresh_token

    def session(self):
        """
        get the session details
        """
        url = f'{self.api_url}/session'
        response = requests.get(url, headers=self.headers)

        if response.status_code != 200:
            raise ConnectionError(f'Session request failed: {response.text}')

        return response.json()
    
    def get_access_token(self):
        """
        get the access token
        """
        return self.access_token
    
    def get_refresh_token(self):
        """
        get the refresh token
        """
        return self.refresh_token    

    def ping(self):
        """
        ping the hanzo api
        """
        url = f'{self.api_url}/ping'
        response = requests.get(url, headers=self.headers)

        if response.status_code != 200:
            raise ConnectionError(f'Ping request failed: {response.text}')

        return response.json()
    
    def list_users(self):
        """
        list all users
        """
        url = f'{self.api_url}/user'
        response = requests.get(url, headers=self.headers)

        if response.status_code != 200:
            data = response.json()

            if 'msg' in data and data['msg'] == 'Token has expired':
                self.refresh()
                response = requests.get(url, headers=self.headers)

                if response.status_code != 200:
                    raise ConnectionError(f'List users request failed: {response.status_code} - {response.reason}')               
            

        return response.json()    

    def insert_user(self, user):
        """
        insert a user
        """
        url = f'{self.api_url}/user'
        response = requests.post(url, headers=self.headers, json=user)

        if response.status_code != 200:
            raise ConnectionError(f'Insert user request failed: {response.text}')

        return response.json()
    
    def update_user(self, user):
        """
        update a user
        """
        url = f'{self.api_url}/user'
        response = requests.put(url, headers=self.headers, json=user)

        if response.status_code != 200:
            raise ConnectionError(f'Update user request failed: {response.text}')

        return response.json()
    
    def delete_user(self, user_id):
        """
        delete a user
        """
        url = f'{self.api_url}/user/{user_id}'
        response = requests.delete(url, headers=self.headers)

        if response.status_code != 200:
            raise ConnectionError(f'Delete user request failed: {response.text}')

        return response.json()
    
    def get_user(self, user_id):
        """
        get a user
        """
        url = f'{self.api_url}/user/{user_id}'
        response = requests.get(url, headers=self.headers)

        if response.status_code != 200:
            raise ConnectionError(f'Get user request failed: {response.text}')

        return response.json()
    
    def get_user_by_username(self, username):
        """
        get a user
        """
        url = f'{self.api_url}/user/info/{username}'
        response = self.session.get(url, headers=self.headers)

        if response.status_code != 200:
            raise ConnectionError(f'Get user request failed: {response.text}')

        return response.json()
    
    def list_roles(self):
        """
        list all roles
        """
        url = f'{self.api_url}/role'
        response = requests.get(url, headers=self.headers)

        if response.status_code != 200:
            raise ConnectionError(f'List roles request failed: {response.text}')

        return response.json()
                  