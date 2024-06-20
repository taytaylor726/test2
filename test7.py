import streamlit as st
import requests
from urllib.parse import quote

# ... (函数定义保持不变)
def fetch_and_save_baike_content(keyword):
    url1 = 'https://baike.baidu.com/item/'
    keyword = quote(keyword, encoding='utf-8', errors='replace')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    url = url1 + keyword
    response = requests.get(url, headers=headers)

    # 验证链接是否正确
    st.write(f"正在访问的链接是: {url}")
    if response.status_code == 200:
        with open("baidu.txt", 'wb') as fo:  # 注意：这里我修改了文件路径为当前目录下
            fo.write(response.content)
        st.success("写入文件成功")
    else:
        st.error(f"请求失败，状态码: {response.status_code}")

    # 高德地图API的基础URL和API Key


amap_api_base_url = 'https://restapi.amap.com/v3/geocode/geo'
amap_api_key = '72b92e4ca894584ed2c6d8cab32ca303'  # 替换成你的实际Key


# 定义一个函数来查询并显示地理位置的经纬度
def fetch_location_coordinates(address):
    params = {
        'address': address,
        'key': amap_api_key,
        'output': 'json'
    }
    response = requests.get(amap_api_base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if 'geocodes' in data and data['geocodes']:
            geocode = data['geocodes'][0]
            location = geocode['location']
            return location
        else:
            return "未找到地理位置信息"
    else:
        return f"Error: {response.status_code}, {response.text}"
# Streamlit应用的入口点
if __name__ == "__main__":
    # 设置应用标题
    st.set_page_config(page_title="教育技术与地图经纬度查询的交互式地理学习系统",
                       page_icon="🌐",  # 可选：添加页面图标
                       layout="wide")  # 可选：设置布局为宽版

    st.title("教育技术与地图经纬度查询的交互式地理学习系统")
    st.markdown("---")  # 添加分隔线

    # 百度百科查询
    with st.sidebar:  # 将输入字段和按钮放在侧边栏
        baike_keyword = st.text_input("请输入你要查询的百度百科关键词：")
        if st.button("查询并保存百度百科内容"):
            fetch_and_save_baike_content(baike_keyword)

            # 地理位置查询
    with st.sidebar:
        location_address = st.text_input("请输入你要查询的地理位置：")
        if st.button("查询地理位置经纬度"):
            coordinates = fetch_location_coordinates(location_address)
            st.markdown("---")  # 在结果前添加分隔线
            st.write(f"经纬度: {coordinates}")

            # 如果需要，可以在主区域添加更多内容或说明
    st.markdown("**欢迎来到教育技术与地图经纬度查询的交互式地理学习系统！**")
    st.markdown("在这里，你可以查询百度百科内容，并通过高德地图API查询地理位置的经纬度。")