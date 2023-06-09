'''
@Author: tongxiao
@FileName: __init__.py
@CreateTime: 2023-04-21 00:55:37
@Description:

'''

from nonebot import get_driver, CommandGroup
from .config import Config
from nonebot.rule import to_me, Rule

event_rules = to_me()

plan_cmd_group = CommandGroup("plan", rule=event_rules, priority=10)
event_cmd_group = CommandGroup("event", rule=event_rules, priority=10)

event_remind_config = Config.parse_obj(get_driver().config)

special_chinese_char_map_dict = {
    "，": ",",
    "：": ":",
    "、": ",",
    "？": "?",
    "；": ";",
    "。": ".",
    "“": "\"",
    "”": "\""
}


from .event_list import event_base_matcher, event_lister
from .event_register import event_rgst
from .event_delete import event_del
from .event_reminder import scheduler as event_scheduler
from .plan_list import plan_base_matcher, plan_lister
from .plan_handle import (
    plan_rgst,
    plan_del,
    scheduler as plan_scheduler
)
