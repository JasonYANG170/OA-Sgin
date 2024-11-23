import requests
import json
from datetime import datetime, timedelta
print("OA-Sgin V1.0")
print("本程序将为您自动完成OA签到，开源协议GPT3.0")
print("项目地址:https://github.com/JasonYANG170/OA-Sgin")
print("Wiki文档:https://github.com/JasonYANG170/OA-Sgin/wiki")
print("使用教程请查看Wiki文档")
# 手动输入信息

longitude = input("请输入经度 (longitude): ")
latitude = input("请输入纬度 (latitude): ")
signaddress = input("请输入地址 (signaddress): ")
start_date = input("请输入起始日期 (格式 YYYY-MM-DD): ")
end_date = input("请输入结束日期 (格式 YYYY-MM-DD): ")
student_id = input("请输入 studentid: ")
access_token = input("请输入 X-Access-Token: ")

# URL 和请求头
url = "http://stu-oa.xxgcxy.cn/scloudoa/jobInternship/internshipSignIn/add"
headers = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 15; Pixel 9 Build/AP3A.241105.008; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160117 MMWEBSDK/20240801 MMWEBID/1136 MicroMessenger/8.0.51.2702(0x28003342) WeChat/arm64 Weixin GPVersion/1 NetType/WIFI Language/zh_CN ABI/arm64",
    'Accept-Encoding': "gzip, deflate",
    'Content-Type': "application/json",
    'X-Access-Token': access_token,
    'Origin': "http://stu-oa.xxgcxy.cn",
    'X-Requested-With': "com.tencent.mm",
    'Referer': "http://stu-oa.xxgcxy.cn/scloudapp/",
    'Accept-Language': "zh-CN,zh-SG;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6"
}

# 日期格式转换
start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")

# 日期范围内逐日请求
current_date = start_date_obj
while current_date <= end_date_obj:
    date_str = current_date.strftime("%Y-%m-%d")
    payload = {
        "probationaryworkplacementstudentid": int(student_id),
        "longitude": float(longitude),
        "latitude": float(latitude),
        "date": date_str,
        "signaddress": signaddress
    }

    # 发送 POST 请求
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    # 打印结果
    print(f"请求日期: {date_str}, 响应: {response.text}")

    # 日期加1天
    current_date += timedelta(days=1)
