from credstash import getSecret, KmsError, IntegrityError, ItemNotFound
import yaml

DEFAULT_REGION = "us-east-1"


class ConfigFetcher(object):
    def __init__(self, config_path, env, appid, client):
        with open(config_path, 'r') as stream:
            self.yaml_file = yaml.load(stream)
        self.env = env
        self.appid = appid
        self.client = client

    def get_config_value(self, key):

        value = self._get_value_from_yaml(key)

        if not value:
            try:
                value = self._get_credential(key)
            except (KmsError, IntegrityError) as ex:
                raise Exception("Replace this", ex)  # TODO: Replace with Django ex
            except ItemNotFound:
                pass

        if not value:
            raise Exception(key + " not found.")  # TODO: Replace with Django ex

        return value

    def _get_value_from_yaml(self, key):

        value = ''
        if key in self.yaml_file and self.env:
            if self.env in self.yaml_file.get(key):
                value = self.yaml_file[key][self.env]
            else:
                value = self.yaml_file.get(key, '')

        return value

    def _get_credential(self, key):

        context = {}
        if self.env:
            context['env'] = self.env
        if self.appid:
            context['appid'] = self.appid
        if self.client:
            context['client'] = self.client

        secret = getSecret(key, region=DEFAULT_REGION, context=context)

        return secret
