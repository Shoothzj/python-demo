import os

from configobj import ConfigObj

# 源文件
config = ConfigObj("function.yaml")
# 目的文件
config.filename = "function.yaml"
config['workId'] = os.getenv("HOSTNAME")
config['workHostname'] = os.getenv("HOSTNAME")
config['configurationStoreServers'] = os.getenv("PULSAR_FUNCTION_ZOOKEEPER_SERVERS")
config['pulsarServiceUrl'] = os.getenv("PULSAR_FUNCTION_SERVICE_URL")
config['pulsarWebServiceUrl'] = os.getenv("PULSAR_FUNCTION_WEB_SERVICE_URL")
config['pulsarFunctionsCluster'] = os.getenv("PULSAR_FUNCTION_CLUSTER")
config['useCompactedMetadataTopic'] = True

# 写入文件
config.write()
