"""
    返回全局配置信息
    域名修改之后，阿里云会发送邮件通知, 可根据情况做转发提醒;
        发件人: system@notice.aliyun.com
    PS: so 邮件提醒就暂时不写了，虽然也没几行代码 懒
"""
GLOBAL_CONFIGS = {
    'sdk' : dict(
        # 您的AccessKey ID,
        access_key_id="your key",
        # 您的AccessKey Secret,
        access_key_secret="your key secret",
        #最大重试次数
        max_attempts = 3,
        #aliyun域名
        config_endpoint = 'alidns.cn-hangzhou.aliyuncs.com',
    ),
    
    'log': dict(
        filename = 'runtime.log',
        rotation = '1 week',
    ),

    'domains': {
        #DomainName : RR
        'your-domain.com': ['test',],
    },
    
}



def main():
    return GLOBAL_CONFIGS

if __name__ == '__main__':
    main()

