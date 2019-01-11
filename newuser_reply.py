from wxpy import *
import time
import re
'''
邀请进群自动@相应的用户
实现方式：接受Note类型的提示信息，通过re找到名字，找到nickname，发送字符串信息
'''
from tuling import get_response
bot=Bot()
user=bot.friends(update=False) #全部好友信息
group=bot.groups(update=False) #全部群组信息（保存为联系人的群）
company_group = ensure_one(bot.groups().search('微信测试'))  #查找制定群聊名称群聊名称
for  items in range(len(user)):
    user[items]

my_friend = bot.friends().search('南枝盈盈')[0]
# @bot.register()
# def print_messages(msg):
#     print(msg)

@bot.register(company_group)
def auto_reply(msg):


    print(msg,msg.type,type(msg))
    #tt=get_response(msg)

    if msg.type=='Note':

        new_user= re.findall('".+"', msg.text)
        new_user_str=new_user[0][1:-1]
        print(new_user_str)  # 切片
        time.sleep(3)

        if '邀请' in msg.text:
            fri=bot.friends().search(new_user_str)[0]
            print(fri)
            return "@{0} :欢迎进群".format(fri.nick_name)
        else:
            return


# 堵塞线程，并进入 Python 命令行
embed()
