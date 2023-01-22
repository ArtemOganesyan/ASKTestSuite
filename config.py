import os

import yaml
from yaml.loader import SafeLoader

def get():
    print(os.getcwd())
    with open('/Users/artemkrylov/git/ASKTestSuite/config.yaml') as config:
        data = yaml.load(config, Loader=SafeLoader)
    return data
