import yaml


class Users:
    """Change path to your own users.yml file"""

    def __init__(self, user_type, cus=None, accounts_list=None, email=None, phone=None):
        """Constructor"""
        self.user_type = user_type
        with open("/Users/evosm/Projects/Alfred/main/users/users.yml", 'r') as f:
            data_map = yaml.safe_load(f)
            self.cus = data_map['users'][self.user_type]['cus']
            self.accounts_list = data_map['users'][self.user_type]['account_list']
            self.email = data_map['users'][self.user_type]['email']
            self.phone = data_map['users'][self.user_type]['phone']

    def get_user(self):
        return self.cus