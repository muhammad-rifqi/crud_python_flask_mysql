class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.lables = {
            'username' : 'Username:',
            'password' : 'Password:'
        }
    def setUsername(self, username):
        self.username = username
    def setPassword(self, password):
        self.password = password
    def authenticate(self):
        if self.username == 'demo' and self.password == 'flask':
            return True
        else:
            return False

        
