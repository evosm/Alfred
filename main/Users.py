import yaml


class Users:
    """Change path to your own users.yml file"""

    def __init__(self, user_type, cus=None, accounts_list=None, email=None, phone=None):
        """Constructor"""
        self.user_type = user_type
        self.cus = cus
        self.accounts_list = accounts_list
        self.email = email
        self.phone = phone

    def set_user(self):
        with open("/Users/evosm/Projects/Alfred/main/users/users.yml", 'r') as f:
            data_map = yaml.safe_load(f)
            self.cus = data_map['users'][self.user_type]['cus']
            self.accounts_list = data_map['users'][self.user_type]['account_list']
            self.email = data_map['users'][self.user_type]['email']
            self.phone = data_map['users'][self.user_type]['phone']