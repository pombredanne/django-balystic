import requests

def _url(path):
    return ''

class Client(object):
    """
    Encapsulates all the logic to consume the services provided
    by the balystic API.
    """
    USER_ENDPOINT = 'users/'

    def __init__(self, token, root):
        """
        Token should be provided by the admin of the community.
        Root must be the full path to the api root
        i.e. http://sample.7dhub.com/api/
        """
        self.headers = {'Authorization': 'TOKEN ' + token}
        self.root = root

    def _make_request(self, path, method):
        """
        Encapsulates error handling. Sets an standard way to handle
        requests across the client.
        Path should end with slash.
        """
        if method == 'GET':
            request_method = requests.get
        elif method == 'POST':
            request_method = requests.post
        elif method == 'DELETE':
            request_method = requests.delete
        full_path = self.root + path
        try:
            response = request_method(full_path, headers=self.headers)
            return response.json()
        except:
            pass

    def get_users(self):
        """
        Retrieves the list of users in the community.
        There are two kind of users, owners and regular users.
        """
        return self._make_request(self.USER_ENDPOINT, 'GET')

    def get_user_detail(self, username):
        """
        Retrieves an user detail.
        The user must be in the community for this to work.
        """
        return self._make_request(
            self.USER_ENDPOINT + username + '/', 'GET')
