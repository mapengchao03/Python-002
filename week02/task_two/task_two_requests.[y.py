import requests
import json
from fake_useragent import UserAgent


# 手机号，密码
params = {
    'mobile': '+86158******',
    'password': 'SPIDER******'
}

# 随机user-agent, 禁止从ssl获取，目的提升访问效率
ua = UserAgent(verify_ssl=False)

get_url = 'https://shimo.im/login?from=home'

post_url = 'https://shimo.im/lizard-api/auth/password/login'

# 实例化session
session = requests.session()

# 目的获取cookies
res = session.get(get_url, headers={'User-Agent': ua.random})

print(res.status_code)

# 请求真实登陆链接
response = session.post(post_url, headers={'User-Agent': ua.random}, data=json.dumps(params))

print(response.text)

