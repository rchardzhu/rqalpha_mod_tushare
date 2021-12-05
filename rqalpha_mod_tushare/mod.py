from rqalpha.interface import AbstractMod

from .tushare_kdatasource import TushareKDataSource
    

class TushareKDataMode(AbstractMod):
    def __init__(self):
        pass

    def start_up(self, env, mod_config):
        # 设置 data_source 为 TushareKDataSource 类的对象
        if mod_config.data_source != "ts" and mod_config.data_source != "tspro":
            print("tushare data_source only support ts or tspro")
            return
        TushareKDataSource.data_source = mod_config.data_source
        env.set_data_source(TushareKDataSource(env.config.base.data_bundle_path, {}))

    def tear_down(self, code, exception=None):
        pass