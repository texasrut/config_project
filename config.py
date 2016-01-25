from configfetch import ConfigFetcher


class config(object):

    def __init__(self):
        self.configfetcher = ConfigFetcher('config.yaml', 'dev', '123123', 'hstm')


    @property
    def server(self):
        return self.configfetcher.get_config_value('server')

    @property
    def token_url(self):
        return self.configfetcher.get_config_value('token_url')

    @property
    def token_validation_url(self):
        return self.configfetcher.get_config_value('token_validation_url')

    @property
    def student_group_url(self):
        return self.configfetcher.get_config_value('student_group_url')

    @property
    def client_id(self):
        return self.configfetcher.get_config_value('client_id')

    @property
    def moo(self):
        return self.configfetcher.get_config_value('moo')

    @property
    def juice_secret(self):
        return self.configfetcher.get_config_value('juice-secret')

# token_url: "/STS/connect/accesstokenvalidation"
# token_validation_url: "/STS/connect/accesstokenvalidation"
# student_group_url: "/CSG/api/StudentGroup"
# client_id: "juice-app"