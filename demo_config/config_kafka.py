from configobj import ConfigObj

config = ConfigObj("kafka.properties")
config.filename = "kafka.properties"
config['broker.id'] = "2"
config['advertised.listeners'] = "PLAINTEXT://localhost:9092"
config.write()
