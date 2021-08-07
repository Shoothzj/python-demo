import configparser

config = configparser.ConfigParser()
config.read("config/grafana.ini")

config['smtp']['enabled'] = 'true'

with open('example.ini', 'w') as configfile:
    config.write(configfile)
