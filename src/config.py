import configparser
config = configparser.ConfigParser()
config.read('config.ini')
units = config['DEFAULT']['units']
appid = config['DEFAULT']['appid']
url = config['DEFAULT']['url']