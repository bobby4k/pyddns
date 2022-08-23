# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
# https://next.api.aliyun.com/document/Alidns/2015-01-09/overview
import re
import sys

from typing import List
from urllib import response

from alibabacloud_alidns20150109.client import Client as Alidns20150109Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_alidns20150109 import models as alidns_20150109_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


class Sample:
    access_key_id = None
    access_key_secret = None
    config_endpoint = 'alidns.cn-hangzhou.aliyuncs.com'

    _client = None

    def __init__(self,
        access_key_id: str,
        access_key_secret: str,
        config_endpoint:str = None,
        ) -> None:
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.config_endpoint = self.config_endpoint if config_endpoint == None else config_endpoint

    def create_client(self,
        # access_key_id: str,
        # access_key_secret: str,
    ) -> Alidns20150109Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        if isinstance(self._client, Alidns20150109Client):
            print(self._client)
            return self._client
        
        config = open_api_models.Config(
            # 您的 AccessKey ID,
            access_key_id=self.access_key_id,
            # 您的 AccessKey Secret,
            access_key_secret=self.access_key_secret
        )
        # 访问的域名
        config.endpoint = self.config_endpoint
        # config.endpoint = f'alidns.cn-hangzhou.aliyuncs.com'
        self._client = Alidns20150109Client(config)
        return self._client

    def describe_domain_records(self,domain_name:str) -> list:

        client = self.create_client()
        describe_domain_records_request = alidns_20150109_models.DescribeDomainRecordsRequest(
            domain_name=domain_name
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            response = client.describe_domain_records_with_options(describe_domain_records_request, runtime)
            if 200 == response.status_code:
                # a = response.body.domain_records.record.pop()
                # print(a.record_id, a.rr, a.status, a.domain_name)
                return response.body.domain_records.record
            else:
                assert RuntimeError(f"response status code:{response.status_code}")
        except Exception as error:
            # 如有需要，请打印 error
            UtilClient.assert_as_string(error.message)
    #END describe records

    def update_domain_record_async(self, record_id:str,
                                        rr:str, type:str, value:str,
                                        ) -> None:
        client = self.create_client()
        update_domain_record_request = alidns_20150109_models.UpdateDomainRecordRequest(
            record_id=record_id,
            rr=rr,
            type=type,
            value=value,
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            response = client.update_domain_record_with_options(update_domain_record_request, runtime)
            if 200==response.status_code:
                return response.body.record_id
            else:
                return False
        except Exception as error:
            # 如有需要，请打印 error
            UtilClient.assert_as_string(error.message)
    #END update record
#END class

if __name__ == '__main__':
    pass