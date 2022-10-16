import requests,json,pytest,allure
URL = "http://liyou.api.sauou.com/"
"""@allure.severity装饰器按严重性级别来标记case　　　
执行指定测试用例 --allure-severities blocker
BLOCKER = 'blocker'　　阻塞缺陷(功能未实现，无法下一步)
CRITICAL = 'critical'　严重缺陷(功能点缺失)
NORMAL = 'normal'　　  一般缺陷(边界情况，格式错误)
MINOR = 'minor'　　    次要缺陷(界面错误与ui需求不符)
TRIVIAL = 'trivial'　　轻微缺陷(必须项无提示，或者提示不规范)　
标记用例等级：@allure.severity(allure.severity_level.TRIVIAL)"""
@allure.feature("小程序用户端")
@allure.story("我的模块测试用例")
@allure.description("用户头像修改")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_alter_user_avatar():
    """用户头像修改"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid":"1", #用户id
        "avatar":"https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKnD4njC4N3GWC58Vg8ThGbrrndm9EfkhJoFwvoPzcjHUBZDmCT230ENIjXe8F2lzhklcBdTqSslg/132"
    }
    url = URL + "/h5/user.User/setAvatar"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("我的模块测试用例")
@allure.description("修改手机号")
@allure.severity(allure.severity_level.CRITICAL)
def test_2_alter_phone():
    """修改手机号"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid":"1", #用户id
        "phone":"18875272519",
        "smsCode":"9112", #短信验证码
    }
    url = URL + "/h5/user.User/setPhone"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("我的模块测试用例")
@allure.description("发送获取短信验证码")
@allure.severity(allure.severity_level.CRITICAL)
def test_3_send_get_verification_code ():
    """发送、获取验证码"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "phone":"18875272819"
    }
    url = URL + "/h5/user.Common/sendSMS"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("我的模块测试用例")
@allure.description("用户信息")
@allure.severity(allure.severity_level.NORMAL)
def test_4_user_message():
    """用户信息"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid":"1" #用户id
    }
    url = URL + "/h5/user.User/getUser"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("我的模块测试用例")
@allure.description("我的团队")
@allure.severity(allure.severity_level.NORMAL)
def test_5_my_team():
    """我的团队"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid":"1", #用户id
        "page":"1",
        "pagesize":"10"
    }
    url = URL + "/h5/user.user_team/myTeam"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("我的模块测试用例")
@allure.description("推广分享海报")
@allure.severity(allure.severity_level.NORMAL)
def test_6_popularize_share_posters():
    """推广分享海报"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid":"1" #用户id
    }
    url = URL + "/h5/user.Common/GetPromote"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("我的模块测试用例")
@allure.description("地址新增、修改")
@allure.severity(allure.severity_level.CRITICAL)
def test_7_add_address():
    """地址新增、修改"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        # "id":"1", #修改必填地址主键id
        "uid":"1", #用户id
        "contacts":"测试928", #联系人
        "contact_number":"17623400167", #联系电话
        "province_id":"110000", #省份id
        "province_name":"北京", #省份名
        "city_id":"110100", #城市id
        "city_name":"北京市", #城市名
        "area_id":"110101", #地区id
        "area_name":"东城区", #地区名
        "detailed_address":"xxx大楼25号", #详细地址
        "id_default":"0"#是否默认地址 1 默认 2 否
    }
    url = URL + "/h5/user.user_address/doSave"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("我的模块测试用例")
@allure.description("地址删除")
@allure.severity(allure.severity_level.CRITICAL)
def test_8_delete_address():
    """地址删除"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "id":"1" #地址id
    }
    url = URL + "/h5/user.user_address/del"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("我的模块测试用例")
@allure.description("收货地址列表")
@allure.severity(allure.severity_level.NORMAL)
def test_9_ship_address_list():
    """收货地址列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid":"1" #用户id
    }
    url = URL + "/h5/user.user_address/getList"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("我的模块测试用例")
@allure.description("账户明细")
@allure.severity(allure.severity_level.NORMAL)
def test_10_account_detail():
    """账户明细"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid":"1", #用户id
        "month":"2022-7", #月份
        "page":"1",
        "pagesize":"10"
    }
    url = URL + "/h5/user.capital_flow/getList"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("我的模块测试用例")
@allure.description("我的收藏列表")
@allure.severity(allure.severity_level.NORMAL)
def test_11_my_collect_list():
    """我的收藏列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid":"1", #用户id
        "type":"1", #0商品 1 店铺
        "page":"1",
        "pagesize":"10"
    }
    url = URL + "/h5/user.User/myCollect"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

@allure.feature("小程序用户端")
@allure.story("我的模块测试用例")
@allure.description("我的收藏列表")
@allure.severity(allure.severity_level.CRITICAL)
def test_12_delete_my_collect():
    """删除我的收藏"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "ids": [  #收藏数组id
            1, 2
        ],
        "type": 0  #0商品 1 店铺
    }
    url = URL + "/h5/user.User/delCollect"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("我的模块测试用例")
@allure.description("保证金缴纳")
@allure.severity(allure.severity_level.CRITICAL)
def test_13_pay_margin():
    """保证金缴纳"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid": "1",
        "deposit_type": "1"  #保证金类型 1.个人保证金 2.服务商保证金 3.供应商保证金
    }
    url = URL + "/h5/user.user_deposit/payDeposit"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("我的模块测试用例")
@allure.description("保证金申请退还")
@allure.severity(allure.severity_level.CRITICAL)
def test_14_apply_refund_margin():
    """保证金申请退还"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid": "1",
        "deposit_type": "1"  #保证金类型 1.个人保证金 2.服务商保证金 3.供应商保证金
    }
    url = URL + "/h5/user.user_deposit/sendBack"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("我的模块测试用例")
@allure.description("服务商/供应商/个人认证")
@allure.severity(allure.severity_level.CRITICAL)
def test_15_certified_service_supplier_personal():
    """服务商/供应商/个人认证"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid":"1",
        "enterprise": "测试",  #企业名称
        "province_id":"110000",  #省份code
        "province_name":"北京",  #省份名称
        "city_id":"110100",  #市code
        "city_name":"北京市",  #市名称
        "area_id":"110101",  #区code
        "area_name":"东城区",  #区
        "detailed_address":"xxx广场28",  #详细地址
        "corporation":"企业法人928",  #企业法人
        "contact":"17623400167",  #联系方式
        "id_card":"500242199403102252",  #身份证号
        "id_card_img":"正反面",  #身份证正反面
        "license":"执照",  #营业执照
        "apply_type":"2",  #1.个人认证 2.服务商认证 3.供应商认证
        "realname":"luck"  #真实姓名
    }
    url = URL + "/h5/user.authorization_apply/apply"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("我的模块测试用例")
@allure.description("会员开通")
@allure.severity(allure.severity_level.CRITICAL)
def test_16_open_membership():
    """会员开通"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid": "1",
        "id": "1"
    }
    url = URL + "/h5/user.recharge_order/openVip"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("我的模块测试用例")
@allure.description("会员套餐信息")
@allure.severity(allure.severity_level.MINOR)
def test_17_membership_combo_message():
    """会员套餐信息"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    url = URL + "/h5/user.vip_set_meal/getSetMeal"
    res = requests.post(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("我的模块测试用例")
@allure.description("提现申请")
@allure.severity(allure.severity_level.CRITICAL)
def test_18_apply_withdrawal():
    """提现申请"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid": "1",
        "money": "0.001",
        "account_name": "测试", #姓名
        "account": "17623400167"  #支付宝账号
    }
    url = URL + "/h5/user.Withdraw/apply"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("我的模块测试用例")
@allure.description("提现记录")
@allure.severity(allure.severity_level.MINOR)
def test_19_withdrawal_record():
    """提现记录"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid": "1",
        "month": "2022-9",
        "page": "1",
        "pagesize": "10"
    }
    url = URL + "/h5/user.Withdraw/record"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()