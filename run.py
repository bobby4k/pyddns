"""
    
    
"""
from turtle import update
from loguru import logger #

from config import GLOBAL_CONFIGS #
import functions as func #
from aliyundns import Sample as Aliyun #


from alibabacloud_tea_util.models import RuntimeOptions
runtime = RuntimeOptions(
    autoretry=True,  # 是否开启重试 默认关闭
    max_attempts=GLOBAL_CONFIGS['sdk']['max_attempts']  # 重试次数 默认3次
)


class Run:
    _kp_ali_client_obj = None
    _kp_out_ip = None
    _kp_update_domains = dict()
    
    def __init__(self) -> None:
        log_config = GLOBAL_CONFIGS['log']
        logger.add(log_config['filename'], rotation=log_config['rotation'], backtrace=True, diagnose=True)

    def main(self) -> None:
        try:
            if self.checked(): return
        except:
            logger.exception("checked runtime except ?")

        self.update_records()
        # try:
        #     self.update_records()
        # except:
        #     logger.exception("update records runtime except ?")
    #END main

    def update_records(self):    
        """
        循环修改域名记录
        """
        if len(self._kp_update_domains) == 0: return
        
        config = GLOBAL_CONFIGS['sdk']
        #初始化aliyun
        aliyun_obj = Aliyun(
            access_key_id= config['access_key_id'],
            access_key_secret= config['access_key_secret'],
            config_endpoint = config['config_endpoint'],
            )
        #通过阿里云修改
        for (k,v) in self._kp_update_domains.items():
            subdomain_name = f'{v[0]}.{k}'
            domain_name = k
            domain_records = aliyun_obj.describe_domain_records(domain_name=domain_name)
            
            for record in domain_records:
                #1 排除不使用子域名
                if record.status != 'ENABLE' and record.domain_name != k:
                        continue
                
                #2 再循环一次，子域名更新
                for sub,sub_ip in v:
                    if sub == record.rr: 
                        update_params = dict(
                            rr=record.rr,
                            type=record.type,
                            value=self._kp_out_ip,
                            record_id=record.record_id,
                        )
                        aliyun_obj.update_domain_record_async(**update_params)
                        print(sub,sub_ip, update_params)
                #END subdomain
            #END records
        #END for domains
        
    #END update_records

    def checked(self) -> bool:
        """
        检查域名ip是否和本程序公网ip相同
        """
        is_checked = True #True通过， False未通过
        out_ip = func.get_out_ip(1)
        logger.info(f"get out ip:{out_ip}")
        
        if func.str_is_ip(out_ip) == False:
            assert RuntimeError("can't get out ip")
        #记录服务所在公网ip
        self._kp_out_ip = out_ip

        for (k,v) in GLOBAL_CONFIGS['domains'].items():
            for rr in v:
                domain_ip = func.get_host_byname(f"{rr}.{k}")
                # domain_ip = func.get_host_iplist(f"{rr}.{k}")
                logger.info(f"get domain:{rr}.{k} ip:{domain_ip}")

                if func.str_is_ip(domain_ip) == False:
                    assert RuntimeError(f"can't get domain ip :{rr}.{k}")

                if domain_ip != out_ip:
                    is_checked = False
                    logger.info(f"wrong: domain:{rr}.{k} withip:{domain_ip}")

                    if self._kp_update_domains.__contains__(k) == False:
                        self._kp_update_domains[k] = []
                    
                    self._kp_update_domains[k].append((rr, domain_ip))
                #END wrong ip
        
        return is_checked
    #END checked

#END class Run

def main():
    Run().main()

if __name__ == '__main__':
    main()