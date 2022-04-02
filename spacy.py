import json

import requests


class spacy:
    def __init__(self):
        self.search_params = {'query': '', 'state': ''}#, 'space.fields': '', 'expansions': ''}
        self.search_spaceids_params = {'ids': ''}#, 'space.fields': 'title,created_at', 'expansions': 'creator_id'}
        self.search_creatorid_params = {'user_ids': ''}#, 'space.fields': '', 'expansions': ''}
        self.headers = {'Authorization': ''}
        self.expansions = {'expansions': ''}
        self.spacefield = {'space.fields': ''}
        self.params = {}

        self.id = ''

    def create_headers(self, bearer_token):
        self.headers = {
            "Authorization": "Bearer {}".format(bearer_token)#,
        }

    def connect_to_search_space_endpoint(self):

        if self.search_params['query'] == '':
            raise Exception('[query] is required parameter.')

        if self.search_params['state'] == '':
            raise Exception('[state] is required parameter.')

        self.search_params.update(**self.expansions, **self.spacefield)

        search_url = "https://api.twitter.com/2/spaces/search"
        print(self.search_params)
        response = requests.request("GET", search_url, headers=self.headers, params=self.search_params)
        print(response.status_code)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)

        print(json.dumps(response.json(), indent=4, sort_keys=True))

    def connect_to_space_lookup_with_spaceids(self):

        if self.search_spaceids_params['ids'] == '':
            raise Exception('[ids] is required parameter.')

        self.params.update(**self.search_spaceids_params,**self.expansions, **self.spacefield)

        search_url = "https://api.twitter.com/2/spaces"
        response = requests.request("GET", search_url, headers=self.headers, params=self.params)
        print(response.status_code)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)

        print(json.dumps(response.json(), indent=4, sort_keys=True))

    def connect_to_space_lookup_with_spaceid(self):
        if self.space_id == '':
            raise Exception('[id] is required parameter')

        self.params.update(**self.spacefield, **self.expansions)

        search_url = "https://api.twitter.com/2/spaces/" + self.space_id
        response = requests.request("GET", search_url, headers=self.headers, params=self.params)
        print(self.params)
        print(response.status_code)

        if response.status_code != 200:
            raise Exception(response.status_code, response.text)

        print(json.dumps(response.json(), indent=4, sort_keys=True))

    def connect_to_space_lookup_with_creatorids(self):
        if self.search_creatorid_params == '':
            raise Exception('[user_ids] is required parameter')

        self.params.update(**self.search_creatorid_params, **self.spacefield, **self.expansions)

        search_url = "https://api.twitter.com/2/spaces/by/creator_ids"
        response = requests.request("GET", search_url, headers=self.headers, params=self.params)
        print(self.params)
        print(response.status_code)

        if response.status_code != 200:
            raise Exception(response.status_code, response.text)

        print(json.dumps(response.json(), indent=4, sort_keys=True))

    def create_params(self, *, user_ids='', ids='', id='', query='', state='', **kwargs):
        
        # search_spaces
        self.search_params['query'] = query
        self.search_params['state'] = state
        
        # space_lookup
        self.search_creatorid_params['user_ids'] = user_ids

        # space_lookup
        self.search_spaceids_params['ids'] = ids

        # space_lookup
        self.space_id = id
        
        if kwargs.get('expansions'):
            self.expansions['expansions'] = kwargs['expansions']
        
        if kwargs.get('fields'):
            self.spacefield['space.fields'] = kwargs['fields']
