class Userdetails:
    def __init__(self, userid, username, password, role):
        self.userid = userid
        self.username = username
        self.password = password
        self.role = role

    # Getters
    def get_userid(self):
        return self.userid

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_role(self):
        return self.role

    # Setters
    def set_userid(self, userid):
        self.userid = userid

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def set_role(self, role):
        self.role = role