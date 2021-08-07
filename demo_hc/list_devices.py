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

try:
    # 实例化请求对象
    request = ListDevicesRequest()
    # 调用查询设备列表接口
    response = client.list_devices(request)
    print(response)
except exceptions.ClientRequestException as e:
    print(e.status_code)
    print(e.request_id)
    print(e.error_code)
    print(e.error_msg)
