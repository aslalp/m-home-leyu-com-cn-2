import json
import sys
from datetime import datetime

SITE_DATA = {
    "name": "乐鱼体育",
    "url": "https://m-home-leyu.com.cn",
    "tags": ["体育", "娱乐", "乐鱼", "体育平台"],
    "description": "乐鱼体育是专注于体育赛事直播与娱乐的综合平台，提供丰富的体育资讯与互动体验。",
    "keywords": ["乐鱼体育", "体育直播", "赛事资讯", "体育娱乐"],
    "version": "2.1.0",
    "last_updated": "2025-03-18"
}

def format_summary(data: dict) -> str:
    lines = []
    lines.append(f"站点名称：{data['name']}")
    lines.append(f"访问地址：{data['url']}")
    lines.append(f"核心标签：{', '.join(data['tags'])}")
    lines.append(f"简短说明：{data['description']}")
    lines.append(f"关键词：{' | '.join(data['keywords'])}")
    lines.append(f"数据版本：{data['version']}")
    lines.append(f"最后更新：{data['last_updated']}")
    return "\n".join(lines)

def generate_json_output(data: dict) -> str:
    output = {
        "name": data["name"],
        "url": data["url"],
        "tags": data["tags"],
        "description": data["description"],
        "keywords": data["keywords"],
        "version": data["version"],
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return json.dumps(output, ensure_ascii=False, indent=2)

def main():
    print("=== 结构化站点摘要 ===")
    print()
    print(format_summary(SITE_DATA))
    print()
    print("=== JSON 格式输出 ===")
    print()
    print(generate_json_output(SITE_DATA))
    print()
    print("生成完毕。")

if __name__ == "__main__":
    main()