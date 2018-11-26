from wxpy import *
import time




#公众号群发消息
def public_sengall(msg):
    for items in range(len(public)):
        time.sleep(3)
    #     #user[items].get_avatar(save_path=fr'C:\Users\Administrator\Desktop\weixinpic\{items}.jpg')   #循环获取微信联系人头像
    #     print(user[items].name)
    #     print(user[items].remark_name)
    #     print(user[items].user_name)
        public[items].send(msg)    #更改消息内容
        print('消息发送至：(%d/%d)  %s'%(items+1,len(public),public[items].name))
    #bot.add_mp('爱奇艺')  添加公众号


    #public[0].send('hello')   #给公众号发短信


#联系人群发消息
def user_sendall(msg):
    for items in range(len(user)):
        time.sleep(3)
        user[items].send(msg)
        #print('消息发送至：'+user[items].name)
        print('消息发送至：(%d/%d)  %s' % (items + 1, len(user), user[items].name))


#群聊列表发送

def use_list_send(msg):
    for items in range(len(user_list)):
        time.sleep(3)
        user_list[items].send(msg)
        #print('消息发送至：'+user_list[items].name)
        print('消息发送至：(%d/%d)  %s' % (items + 1, len(user_list), user_list[items].name))

if __name__=='__main__':
    bot = Bot()
    myself = bot.self
    # 向文件传输助手发送消息
    # bot.file_helper.send('Hello from wxpyq!')
    # 获取联系人
    user = bot.friends(update=False)
    # print(user)

    # 获取活跃群联列表
    user_list = bot.groups(update=False)
    # print(user_list)

    # 获取公众号
    public = bot.mps(update=False)
    # print(public)

    # 获取所有聊天对象
    talck = bot.chats(update=False)
    # print(len(talck))

    tclk = bot.core.get_chatrooms(update=True)  # 获取群聊列  群聊必须保存为联系人

    # bot.dump_login_status()
    # print(len(tclk))
    # for ite in range(len(tclk)):
    #     print(tclk[ite]['NickName'])
    msg=input('请输入要发送的内容：')
    a = int(input('请选择要群发的类型：1/公众号，2/联系人，3/微信群：'))
    #print('等待发送中.....')
    if a==1:
        print('公众号获取中.........')

        public_sengall(msg)

    elif a==2:
        print('联系人获取中.........')
        user_sendall(msg)


    elif a==3:
        print('微信群获取中.........')
        use_list_send(msg)

