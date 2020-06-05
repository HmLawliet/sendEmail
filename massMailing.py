import yagmail 

def mass_mailing(to,subject,contents,user=None,password=None,host=None):
    """
    发送邮件  包含群发
    :param to    list or str   str 为单发给一个人  list 为群发
    :param subject    str           邮件主题
    :param contents   list          包含 内容 html文本以及图片的其他附件
    :param user       str           发送者用户名
    :param password   str           发送者密码
    :param host       str           发送的代理服务器地址
    """
    user = user or 'houmin@wopuwulian.com'
    password = password or 'yourpassword'
    host = host or 'smtp.mxhichina.com'  # 阿里邮箱地址
    yag = yagmail.SMTP(user=user,password=password,host=host)   # pip install yagmail 
    yag.send(to=to,subject=subject,contents=contents)
    print(" send successed !!!")

if __name__ == "__main__":

    to = ['597010012@qq.com',]  # 'zhuyp@wopuwulian.com',

    subject = '测试群发功能'
    body = 'This is obviously the body'
    html = '<a href="https://cn.bing.com/">Click me!</a>' 
    img = r'D:\Projects\sendEmail\OIP.jpg'
    mass_mailing(to,subject,[body,html,img])
    pass 