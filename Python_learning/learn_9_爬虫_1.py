# robots.txt ---- 爬虫协议(君子协议)
# Host: # 爬虫只能访问指定的主机
# User-Agent: # 用户代理，通过请求头表示，确认爬虫身份
# Disallow: # 禁止爬虫访问的路径
# Allow: # 允许爬虫访问的路径
# Sitemap: # 提供站点地图的URL
# Crawl-delay: # 爬虫爬取延迟时间，单位秒
#

# 尝试爬取ACFUN的排名页面
from datetime import datetime
import json
import re
import requests


# 定义url
acfun_rank_url = "https://www.acfun.cn/rest/pc-direct/rank/channel?channelId=&subChannelId=&rankLimit=30&rankPeriod=DAY"

# 定义请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.acfun.cn/rank/list/",  # 带上这个，服务器才会放心给你数据
    #    "Accept": "application/json, text/plain, */*"
    # ACFUN的反爬虫机制检测到了我们的请求，拒绝了我们的请求，
    # 我们需要添加请求头，来模拟浏览器的请求，才能成功获取到响应
    # 模拟浏览器：
    # 1. 打开浏览器，右键点击“检查”，在“网络”标签中，点击“发送请求”，即可查看请求头
    # 2. 可以在代码中添加请求头，来模拟浏览器的请求
    # 3. 注意：请求头中的User-Agent需要与浏览器中的User-Agent一致，才能成功获取到响应
}

# 发送请求
response = requests.get(acfun_rank_url, headers=headers)
response.encoding = response.apparent_encoding
request_time = datetime.now().strftime('%Y年%m月%d日 %H:%M:%S秒')
request_time_desc = datetime.now().strftime('%Y年%m月%d日')
# 打印响应内容
# print(response.text)
# 输出到文件（wsl输出到windows系统）
with open("/mnt/c/Users/WhisperTang/Desktop/acfun_rank.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(json.loads(response.text), ensure_ascii=False, indent=2))
    print("文件已保存")

# with open("/mnt/c/Users/WhisperTang/Desktop/acfun_rank.json", "r", encoding="utf-8") as f:
#     data = json.load(f)
#     with open("/mnt/c/Users/WhisperTang/Desktop/acfun_rank.json.json", "w", encoding="utf-8") as f:
#         json.dump(data, f, ensure_ascii=False, indent=4)

# 解析json数据并转换为html文件

with open("/mnt/c/Users/WhisperTang/Desktop/acfun_rank.json", "r", encoding="utf-8") as f:
    data = json.load(f)


def convert_timestamp(ms_timestamp):
    """将毫秒时间戳转换为可读时间"""
    if not ms_timestamp:
        return "未知时间"
    # AC Fun的时间戳通常是毫秒级
    sec_timestamp = ms_timestamp / 1000
    return datetime.fromtimestamp(sec_timestamp).strftime('%Y-%m-%d %H:%M:%S')


def generate_acfun_html(json_path, output_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 开始构建 HTML 字符串
    html_content = """
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title> ACFUN %s 排行榜 </title>
        <style>
            :root {
                --primary-color: #ac0030; /* A站红 */
                --bg-color: #f4f4f4;
                --card-bg: #ffffff;
                --text-dark: #333;
                --text-light: #666;
                --border-color: #ddd;
            }
            body {
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                background-color: var(--bg-color);
                color: var(--text-dark);
                margin: 0;
                padding: 20px;
                line-height: 1.6;
            }
            .header {
                text-align: center;
                padding: 30px 0;
                background: var(--card-bg);
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                margin-bottom: 30px;
            }
            .header h1 {
                color: var(--primary-color);
                margin: 0;
            }
            .meta-info {
                color: var(--text-light);
                font-size: 0.9em;
            }
            .container {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
                gap: 20px;
                max-width: 1600px;
                margin: 0 auto;
            }
            .card {
                background: var(--card-bg);
                border-radius: 12px;
                overflow: hidden;
                box-shadow: 0 4px 15px rgba(0,0,0,0.08);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                display: flex;
                flex-direction: column;
            }
            .card:hover {
                transform: translateY(-5px);
                box-shadow: 0 10px 30px rgba(0,0,0,0.15);
            }
            .video-cover {
                width: 100%%;
                height: 180px;
                object-fit: cover;
                border-bottom: 1px solid var(--border-color);
            }
            .content {
                padding: 16px;
                flex: 1;
            }
            .title {
                font-size: 1.1em;
                font-weight: bold;
                margin: 0 0 10px 0;
                color: var(--text-dark);
                display: -webkit-box;
                -webkit-line-clamp: 2;
                -webkit-box-orient: vertical;
                overflow: hidden;
            }
            .up-info {
                display: flex;
                align-items: center;
                margin-bottom: 12px;
                font-size: 0.9em;
                color: var(--text-light);
            }
            .up-avatar {
                width: 28px;
                height: 28px;
                border-radius: 50%%;
                margin-right: 8px;
                object-fit: cover;
            }
            .stats {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 8px 4px;
                font-size: 0.85em;
                color: #888;
                margin-bottom: 12px;
            }
            .stat-item {
                background: #f9f9f9;
                padding: 4px 8px;
                border-radius: 4px;
                text-align: center;
            }
            .tags {
                display: flex;
                flex-wrap: wrap;
                gap: 4px;
                margin-bottom: 12px;
                font-size: 0.8em;
            }
            .tag {
                background: #eee;
                color: #555;
                padding: 2px 6px;
                border-radius: 3px;
            }
            .description {
                font-size: 0.85em;
                color: #555;
                background: #f9f9f9;
                padding: 10px;
                border-radius: 6px;
                margin-top: 10px;
                max-height: 60px;
                overflow-y: auto;
            }
            .tooltip {
                position: relative;
                cursor: help;
                border-bottom: 1px dotted var(--text-light);
            }
            .tooltip::after {
                content: attr(data-tip);
                position: absolute;
                bottom: 100%%;
                left: 50%%;
                transform: translateX(-50%%);
                width: max-content;
                max-width: 200px;
                background: #333;
                color: #fff;
                padding: 8px;
                border-radius: 4px;
                font-size: 0.8em;
                text-align: center;
                z-index: 10;
                opacity: 0;
                transition: opacity 0.3s;
                white-space: nowrap;
            }
            .tooltip:hover::after {
                opacity: 1;
            }
            .footer {
                text-align: center;
                padding: 30px 0;
                color: var(--text-light);
                font-size: 0.9em;
                margin-top: 50px;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1> %s ACFUN排行日榜 </h1>
            <div class="meta-info">
                <strong>数据源主机：</strong>""" + data.get("host-name", "未知") + """ |
                <strong>请求结果：</strong>""" + ("成功 (0)" if data.get("result") == 0 else "失败") + """ |
                <strong>数据量：</strong>""" + str(len(data.get("rankList", []))) + """ 个视频
            </div>
        </div>

        <div class="container">
    """
    # 遍历 rankList 生成卡片
    for index, item in enumerate(data.get("rankList", [])):
        # 提取基础信息
        title = item.get("contentTitle", "无标题")
        cover_url = item.get("videoCover", "")
        up_name = item.get("userName", "未知UP主")
        up_id = item.get("userId", "")
        up_url = f"https://www.acfun.cn/u/{up_id}" if up_id else "#"
        video_id = item.get("dougaId", "")
        video_url = f"https://www.acfun.cn/v/ac{video_id}" if video_id else "https://www.acfun.cn"
        up_avatar = item.get("userImg", "")
        view_count = item.get("viewCountShow", "0")
        danmu_count = item.get("danmuCountShow", "0")
        banana_count = item.get("bananaCountShow", "0")
        like_count = item.get("likeCountShow", "0")
        stow_count = item.get("stowCountShow", "0")
        create_time_desc = item.get("createTime", "未知时间")
        contribute_time_ms = item.get("contributeTime", 0)
        duration_ms = item.get("durationMillis", 0)
        channel_name = item.get("channel", {}).get("name", "未知频道")
        content_desc = item.get("contentDesc", "").replace(
            "<br/>", "\n")[:200] + "..." if item.get("contentDesc") else "暂无简介"

        # 处理时间戳
        contribute_time_str = convert_timestamp(contribute_time_ms)
        duration_str = f"{duration_ms // 60000}分{(duration_ms % 60000) // 1000}秒" if duration_ms > 0 else "未知"

        # 提取标签
        tags = [tag.get("name", "")
                for tag in item.get("tagList", [])[:3]]  # 只取前3个主要标签

        # 构建卡片 HTML
        # 点击封面跳转到视频详情页
        html_content += f"""
            <div class="card">
                    <!-- 点击封面跳转到视频详情页 -->
                    <a href="{video_url}" target="_blank" style="display: block; position: relative;">
                        <img class="video-cover" src="{cover_url}" alt="{title}" 
                             onerror="this.src='https://via.placeholder.com/320x180?text=Image+Not+Found';">
                    </a>    
                <div class="content">
                    <h3 class="title">
                            <a href="{video_url}" target="_blank" style="color: inherit; text-decoration: none;">
                                {title}
                            </a>
                        </h3>
                    <a href="{up_url}" target="_blank" style="text-decoration: none; color: inherit; display: contents;">
                        <div class="up-info">   
                            <img class="up-avatar" src="{up_avatar}" alt="{up_name}">
                            <span><strong>UP主：</strong>{up_name}</span>
                        </div>
                    </a>
                    <div class="stats">
                        <div class="stat-item">👁️ 观看: <span class="tooltip" data-tip="原始ID: {item.get('dougaId', 'N/A')}">{view_count}</span></div>
                        <div class="stat-item">🍌 香蕉: {banana_count}</div>
                        <div class="stat-item">💬 弹幕: {danmu_count}</div>
                        <div class="stat-item">👍 点赞: {like_count}</div>
                        <div class="stat-item">⏰ 时长: {duration_str}</div>
                        <div class="stat-item">📚 收藏: {stow_count}</div>
                    </div>

                    <div class="tags">
                        <span class="tag">榜单排名: {index+1}</span>
                        <span class="tag">频道: {channel_name}</span>
                        <span class="tag">热度: {item.get('recoReason', {}).get('tag', '无')}</span>
                        {''.join([f'<span class="tag">{tag}</span>' for tag in tags])}
                    </div>

                    <div class="description">
                        <strong>简介:</strong> {content_desc}
                        <br><small><strong>投稿时间:</strong> {contribute_time_str}</small>
                    </div>
                </div>
            </div>
        """

    html_content += """
        </div>
        <div class="footer">
            <p>数据生成于：%s </p>
        </div>
    </body>
    </html>
    """

    # 写入文件
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content %
                (request_time_desc, request_time_desc, request_time))

    print(f"✅ HTML 页面已生成！共处理了 {len(data.get('rankList', []))} 条数据。")
    print(f"📁 保存路径: {output_path}")


# --- 执行生成 ---
json_file_path = "/mnt/c/Users/WhisperTang/Desktop/acfun_rank.json"
output_html_path = "/mnt/c/Users/WhisperTang/Desktop/acfun_rank_full.html"

generate_acfun_html(json_file_path, output_html_path)

# with open("/mnt/c/Users/WhisperTang/Desktop/acfun_rank.html", "w", encoding="utf-8") as f:
#     f.write(html_content)
#     print(" 美化后的排行榜 HTML 文件已成功保存！")


# 前端网页结构
# 一个网页是由三个部分组成的，分别是: HTML、CSS、JS(JavaScript)。
# HTML:超文本标记语言，由一堆预设的标签( < h1>一级标题</h1>)构成。
# HTML负责网页的结构(页面元素和内容)CSS:层叠样式表。
# CSS负责网页的表现(页面元素的外观、位置等样式，如颜色、大小等)
# JS:全称为JavaScript，简称JS。负责网页的行为(交互效果，点击，滚动等)
