"""
pip install pyyaml
"""

from yaml import load, dump, FullLoader

stream = open('config.yaml', 'r')
config = load(stream, Loader=FullLoader)

print(config)
