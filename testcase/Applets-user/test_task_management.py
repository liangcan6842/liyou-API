import requests,json,pytest,allure
URL = "http://192.168.110.167:566"
"""@allure.severity装饰器按严重性级别来标记case　　　
执行指定测试用例 --allure-severities blocker
BLOCKER = 'blocker'　　阻塞缺陷(功能未实现，无法下一步)
CRITICAL = 'critical'　严重缺陷(功能点缺失)
NORMAL = 'normal'　　  一般缺陷(边界情况，格式错误)
MINOR = 'minor'　　    次要缺陷(界面错误与ui需求不符)
TRIVIAL = 'trivial'　　轻微缺陷(必须项无提示，或者提示不规范)　
标记用例等级：@allure.severity(allure.severity_level.TRIVIAL)"""
@allure.feature("小程序用户端")
@allure.story("任务管理模块测试用例")
@allure.description("任务发布")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_publish_task():
    """任务发布"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid": "1", #用户id
        "title": "测试929", #任务标题
        "classify_id": "1", #分类id
        "budget": "10000", #预算金额
        "deposit": "2", #托管金额 不是必填 输入后会调起支付
        "subject": "0", #主体性质：0.个人 1.公司
        "tag": "标签929", #任务标签 ['标签1','标签二']
        "describe": "测试任务", #任务描述
        "number": "2", #可报名人数
        "scale": "1", #服务商规模 1全部 2个人 3.公司
        "province_id": "500000", #省份code
        "province_name": "重庆市", #省份名称
        "city_id": "500100", #市code
        "city_name": "重庆市", #市区名称
        "appendix": "https://img.daidaipets.com/20220727/1658916778977.jpg" #附件url
    }
    url = URL + "/h5/user.user_task/apply"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("任务管理模块测试用例")
@allure.description("我的任务列表")
@allure.severity(allure.severity_level.NORMAL)
def test_2_my_task_list():
    """我的任务列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid": "1", #用户id
        "status": "0" #0.全部 1.审核中 2.进行中 3.待评价
    }
    url = URL + "/h5/user.user_task/myTaskList"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("任务管理模块测试用例")
@allure.description("我的任务详情")
@allure.severity(allure.severity_level.NORMAL)
def test_3_my_task_detail():
    """我的任务详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "id": "1" #任务id
    }
    url = URL + "/h5/user.user_task/detail"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("任务管理模块测试用例")
@allure.description("我的任务取消发布")
@allure.severity(allure.severity_level.NORMAL)
def test_4_my_task_cancel_publish():
    """我的任务取消发布"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "id": "1",
        "uid": "1"
    }
    url = URL + "/h5/user.user_task/cancel"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("任务管理模块测试用例")
@allure.description("任务分类")
@allure.severity(allure.severity_level.MINOR)
def test_5_task_type():
    """任务分类"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    url = URL + "/h5/user.common/getClassify"
    res = requests.post(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("任务管理模块测试用例")
@allure.description("任务报名")
@allure.severity(allure.severity_level.CRITICAL)
def test_6_my_task_sign_up():
    """任务报名"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "task_id": "1",
        "uid": "1"
    }
    url = URL + "/h5/user.task_apply/apply"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("任务管理模块测试用例")
@allure.description("参与任务列表")
@allure.severity(allure.severity_level.NORMAL)
def test_7_participate_task_list():
    """参与任务列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid": "1",
        "status": "0",
        "page": "1",
        "pagesize": "10"
    }
    url = URL + "/h5/user.user_task/joinTaskList"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("任务管理模块测试用例")
@allure.description("参与任务详情")
@allure.severity(allure.severity_level.MINOR)
def test_8_participate_task_detail():
    """参与任务详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "id": "1"
    }
    url = URL + "/h5/user.user_task/joinTaskDetail"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("任务管理模块测试用例")
@allure.description("悬赏任务")
@allure.severity(allure.severity_level.MINOR)
def test_9_reward_task():
    """悬赏任务"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "classify_id": "",
        "page": "1",
        "pagesize": "10"
    }
    url = URL + "/h5/user.Task/getList"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("任务管理模块测试用例")
@allure.description("悬赏任务详情")
@allure.severity(allure.severity_level.MINOR)
def test_10_reward_task_detail():
    """悬赏任务详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "id": "1" #悬赏id
    }
    url = URL + "/h5/user.Task/detail"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("任务管理模块测试用例")
@allure.description("悬赏任务投诉")
@allure.severity(allure.severity_level.CRITICAL)
def test_11_reward_task_complaint():
    """悬赏任务投诉"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "tid": "2", #被投诉的悬赏id
        "t_uid": "2", #被投诉人id
        "content": "内容虚假", #投诉内容
        "uid": "1" #投诉人id
    }
    url = URL + "/h5/user.task_report/apply"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("任务管理模块测试用例")
@allure.description("确认完成任务发起")
@allure.severity(allure.severity_level.CRITICAL)
def test_12_lunch_comfirm_complete_task():
    """确认完成任务发起"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "id": "1", #任务id
        "uid": "1" #用户id
    }
    url = URL + "/h5/user.task_examine/acceptingEnd"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("任务管理模块测试用例")
@allure.description("确认完成任务")
@allure.severity(allure.severity_level.CRITICAL)
def test_13_comfirm_complete_task():
    """确认完成任务"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "id": "1", #任务id
        "uid": "1" #用户id
    }
    url = URL + "/h5/user.user_task/endTask"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("任务管理模块测试用例")
@allure.description("发起验收")
@allure.severity(allure.severity_level.CRITICAL)
def test_14_lunch_check_accept():
    """发起验收"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "id": "1", #任务id
        "amount": "", #验收金额
        "annex": "" #附件地址
    }
    url = URL + "/h5/user.task_examine/apply"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("任务管理模块测试用例")
@allure.description("确认验收")
@allure.severity(allure.severity_level.CRITICAL)
def test_15_comfirm_check_accept():
    """确认验收"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "examine_id": "1", #任务项目验收主键
        "uid": "1", #验收人
        "is_accepting": "1" #验收状态 1.确认验收 2.拒绝
    }
    url = URL + "/h5/user.task_examine/doAccepting"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("任务管理模块测试用例")
@allure.description("任务评价")
@allure.severity(allure.severity_level.CRITICAL)
def test_16_task_evaluate():
    """任务评价"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "tid": "1", #任务id
        "uid": "1", #评价人
        "service_score": "8", #评分
        "comment": "测试929", #评论内容
        "pics": "" #评价数组
    }
    url = URL + "/h5/user.task_reply/doReply"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("任务管理模块测试用例")
@allure.description("服务商选定")
@allure.severity(allure.severity_level.CRITICAL)
def test_17_designate_service():
    """选定服务商"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "id": "1",
        "apply_id": "1"
    }
    url = URL + "/h5/user.Task/bindUid"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()





































































