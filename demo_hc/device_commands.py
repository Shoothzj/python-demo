from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkiotda.v5 import *
from huaweicloudsdkiotda.v5.region.iotda_region import IoTDARegion

from demo_hc.hc_config import read_hc_config

config = read_hc_config()
ak = config['ak']
sk = config['sk']
# 创建认证
credentials = BasicCredentials(ak, sk) \
    # 创建IoTDAClient实例并初始化
client = IoTDAClient.new_builder() \
    .with_credentials(credentials) \
    .with_region(IoTDARegion.CN_NORTH_4) \
    .build()

client = IoTDAClient.new_builder() \
    .with_credentials(credentials) \
    .with_region(IoTDARegion.value_of("cn-north-4")) \
    .build()

try:
    request = CreateCommandRequest()
    request.device_id = "5e77933553efb708b428f03e_hezhangjian"
    request.body = DeviceCommandRequest(
        paras={"value": 40},
        command_name="switch",
        service_id="LightControl"
    )
    response = client.create_command(request)
    print(response)
except exceptions.ClientRequestException as e:
    print(e.status_code)
    print(e.request_id)
    print(e.error_code)
    print(e.error_msg)
