from yaml import load, dump
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

credentials = {} 
with open('config.yaml', newline='') as configFile:
    globals()['credentials'] = load(configFile,Loader=Loader)