# -*- coding: utf-8 -*-

from rqalpha.apis import *
from rqalpha import run_func


def init(context):
    logger.info("init")
    context.s1 = "000001.XSHE"
    update_universe(context.s1)
    context.fired = False


def before_trading(context):
    logger.info("tushare api demo")

def handle_bar(context, bar_dict):
    if not context.fired:
        # order_percent并且传入1代表买入该股票并且使其占有投资组合的100%
        order_percent(context.s1, 1)
        context.fired = True

config = {
    "base": {
        "start_date": "2021-01-01",
        "end_date": "2021-02-01",
        "benchmark": "000300.XSHG",
        "frequency": "1d",
        "matching_type": "current_bar",
        "accounts": {
            "stock": 100000
        }
    },
    "extra": {
        "log_level": "verbose",
    },
    "mod": {
        "tushare": {
            "enabled": True,
            "lib": "rqalpha_mod_tushare",
            "data_source": "tspro",
            "priority": 100
        },
        "sys_analyser": {
            "enabled": True,
            "plot": True
        }
    }
}



# 您可以指定您要传递的参数
run_func(init=init, before_trading=before_trading, handle_bar=handle_bar, config=config)