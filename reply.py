from wxpy import *
import time
from tuling import get_response
bot=Bot()
user=bot.friends(update=False)

for  items in range(len(user)):
    user[items]

my_friend = bot.friends().search('南枝盈盈')[0]
# @bot.register()
# def print_messages(msg):
#     print(msg)

@bot.register()
def auto_reply(msg):

    #print(get_response(msg))
    return get_response(msg)

# 堵塞线程，并进入 Python 命令行
embed()