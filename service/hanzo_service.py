from datetime import datetime as dt
from etc.settings import HANZO_API_URI

import requests

class HanzoService():

    def __init__(self, session=None):

        self.api_url = HANZO_API_URI if HANZO_API_URI else 'http://127.0.0.1:35777'

        # set headers
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        # connection tokens
        self.session = session        

        # set authorization header
        self.headers['Authorization'] = ('Bearer ' + self.session['access_token']) if 'access_token' in self.session else None

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

        self.session['access_token'] = response_data['access_token']
        self.session['refresh_token'] = response_data['refresh_token']

        # set authorization header
        self.headers['Authorization'] = 'Bearer ' + self.session['access_token']

  
    def refresh(self):
        """
        refresh the access token
        """
        url = f'{self.api_url}/refresh'
        refresh_headers = {'Authorization': 'Bearer ' + self.session['refresh_token']}

        response = requests.post(url, headers=refresh_headers)
        response_data = response.json()

        if response.status_code != 200:
            raise Exception(f'Refresh request failed: {str(response.status_code)} - {response.reason}')
        
        self.session['access_token'] = response_data['access_token']
        self.session['refresh_token'] = response_data['refresh_token']


        # set authorization header
        self.headers['Authorization'] = 'Bearer ' + self.session['access_token']        
        
    def set_access_token(self, access_token:str):
        """
        set the access token
        """
        self.session['access_token'] = access_token
        self.headers['Authorization'] = 'Bearer ' + self.session['access_token']

    def set_refresh_token(self, refresh_token:str):
        """
        set the refresh token
        """
        self.session['refresh_token'] = refresh_token

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
        return self.session['access_token']
    
    def get_refresh_token(self):
        """
        get the refresh token
        """
        return self.session['refresh_token']

    def ping(self):
        """
        ping the hanzo api
        """
        url = f'{self.api_url}/ping'
        response = requests.get(url, headers=self.headers)

        if response.status_code != 200:
            raise ConnectionError(f'Ping request failed: {response.text}')

        return response.json()
    
    def make_request(self, url, **kwargs):                
    
        method = kwargs.get('method', 'GET')

        if 'method' in kwargs:
            del kwargs['method']

        response = requests.request(url=url, method=method, headers=self.headers, **kwargs)

        if response.status_code != 200:
            data = response.json()

            if 'msg' in data and data['msg'] == 'Token has expired':
                self.refresh()
                response = requests.request(url=url, method=method, headers=self.headers, **kwargs)

                if response.status_code != 200:
                    raise ConnectionError(f'Request failed: {response.status_code} - {response.reason}<br/>URL: {url} - KWARGS: {kwargs}')

            else:                
                raise ConnectionError(f'Request failed: {response.status_code} - {response.reason}<br/>URL: {url} - KWARGS: {kwargs}')            
    
        return response.json()

    def list(self, collection):
        """
        list all documents in a collection
        """
        url = f'{self.api_url}/{collection}'
        
        return self.make_request(url)
        

    def insert(self, collection, doc):
        """
        insert a document into a collection
        """
        url = f'{self.api_url}/{collection}'
        return self.make_request(url, method='POST', json=doc)
    
    def update(self, collection, doc):
        """
        update a document in a collection
        """
        url = f'{self.api_url}/{collection}'
        return self.make_request(url, method='PUT', json=doc)
    
    def delete(self, collection, id):
        """
        delete a document with [id] in a collection
        """
        url = f'{self.api_url}/{collection}/{id}'
        return self.make_request(url, method='DELETE')
    
    def find_by_id(self, collection, id):
        """
        get a document with [id] in a collection
        """
        url = f'{self.api_url}/{collection}/{id}'
        return self.make_request(url)        
    
    def find_user_by_username(self, username):
        """
        get a user
        """
        url = f'{self.api_url}/user/info/{username}'
        return self.make_request(url)
    
    def list(self, collection):
        """
        list all roles
        """
        url = f'{self.api_url}/{collection}'
        return self.make_request(url)
    
    def find_all_by(self, collection, **kwargs):
        """
        find all by
        """
        url = f'{self.api_url}/{collection}/find'
        return self.make_request(url, params=kwargs)
    
    def count(self, collection):
        """
        count
        """
        url = f'{self.api_url}/{collection}/count'
        return self.make_request(url)
                  