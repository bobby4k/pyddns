# pyddns
    - 简版动态域名
    - 满足前提：
        - 1、域名托管：阿里云, 且使用阿里云解析
        - 2、网络条件：本程序可获取公网IP

## 建议运行环境
    - docker: python:3.10.6-slim-bullseye

## 阿里云API 云解析文档
    - 云解析OpenAPI概览:[https://next.api.aliyun.com/document/Alidns/2015-01-09/overview)](https://next.api.aliyun.com/document/Alidns/2015-01-09/overview)

    - API申请管理地址: [https://ram.console.aliyun.com/manage/ak](https://ram.console.aliyun.com/manage/ak)

## 使用步骤
    - 1、部署
        - 下载release或者git clone代码
        - cd pyddns/
        - pip install -r requirements.txt
        - 修改config文件, 添加配置
            access_key_id
            access_key_secret
        - 添加需要同步的域名
            注意: 一个域名可以对用多个子域名
    - 2、至少测试运行一次
        - cd pyddns/
        - python ./run.py
    - 3、添加crontab
        - crontab -e 
        - */600 * * * * python /opt/pyddns/run.py
