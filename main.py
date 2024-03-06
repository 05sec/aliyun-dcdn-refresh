import os
from alibabacloud_tea_openapi.models import Config
from alibabacloud_dcdn20180115.client import Client as Client
from alibabacloud_dcdn20180115 import models as models

if __name__ == '__main__':
    config = Config(
        access_key_id=os.getenv('ACCESS_KEY_ID'),
        access_key_secret=os.getenv('ACCESS_KEY_SECRET')
    )
    config.endpoint = 'dcdn.aliyuncs.com'

    client = Client(config)
    request = models.RefreshDcdnObjectCachesRequest()
    request.force = True
    request.object_path = os.getenv('OBJECT_PATH')
    request.object_type = 'Directory'

    response = client.refresh_dcdn_object_caches(request)
    print(response)