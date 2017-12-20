import json
import requests
import yaml

class Client:
    def __init__(self):
        with open('kintone.yml') as f:
            env = yaml.load(f)
            self.url = env['url'] # https://domain.cybozu.com/k/
            self.app_id = env['app_id']
            self.token = env['token']

        self._init_field_info()


    def _init_field_info(self):
        self.options = self._get_options()


    def _header(self):
        return {'Content-Type': 'application/json', 'X-Cybozu-API-Token': self.token}


    def _get_options(self):
        resp = requests.get(self.url + 'v1/form.json', data=json.dumps({'app': self.app_id}), headers=self._header())
        return list(filter(lambda prop: prop['type'] == 'CHECK_BOX', json.loads(resp.text)['properties']))[0]['options']

    def _create_record(self, checks):
        option_values = []
        for (i, checks) in enumerate(checks):
            if checks == True:
                option_values.append(self.options[i])

        return {
            'app': self.app_id,
            'record': {
                'チェックボックス': {
                    'value': option_values
                }
            }
        }


    def post_record(self, checks):
        record = self._create_record(checks)
        resp = requests.post(self.url + 'v1/record.json', data=json.dumps(record), headers=self._header())
        print(json.loads(resp.text))

