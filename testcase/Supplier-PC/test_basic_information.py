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
@allure.feature("供应商后台")
@allure.story("基础信息模块测试用例")
@allure.description("店铺基本信息修改")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_alter_store_message():
    """店铺基本信息修改"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "store_id": "6",  #店铺id(修改必传)
        "name": "供应商店铺1014",    #店铺名称
        "tel": "18812341234",   #电话
        "business_hours": "8-20",  #营业时间8-20
        "email": "1473166229@qq.com",   #邮箱
        "tag": '["中国重庆","供应商"]',    #标签数组形式
        "cover": '["http://cdn.aitaoba.net/20220511/1652257349365.jpg","http://cdn.aitaoba.net/20220511/1652257351337.jpg"]',   #展示图数组形式
        "longitude": "39",  #商家经度
        "latitude": "40",   #商家维度
        "introduction": "一家店铺",  #简介
        "province_name": "重庆",  #省份名称
        "province_id": "500000",
        "city_name": "重庆市",  #市区名称
        "city_id": "500100",
        "area_name": "渝北区",  #区
        "area_id": "500112",
        "detailed_address": "xxx广场" #详细地址
    }
    url = URL + "/Supplier/Supplier/doSaveInfo"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("供应商后台")
@allure.story("基础信息模块测试用例")
@allure.description("店铺详情")
@allure.severity(allure.severity_level.NORMAL)
def test_2_store_detail():
    """店铺详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "store_id": "6"  #店铺id
    }
    url = URL + "/Supplier/Supplier/info"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("供应商后台")
@allure.story("基础信息模块测试用例")
@allure.description("售后配置")
@allure.severity(allure.severity_level.CRITICAL)
def test_3_after_sale_configure():
    """售后配置"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "store_id": "6",  #店铺id
        "receipt_name": "xiaoming", #收货人
        "receipt_tel": "13412341234",  #收货人联系方式
        "receipt_address": "中国重庆渝北xxx广场"  #收货地址
    }
    url = URL + "/Supplier/Supplier/afterSales"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()











