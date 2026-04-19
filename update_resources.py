#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动更新脚本

功能：
1. 解析README.md中的GitHub仓库链接
2. 调用GitHub API获取仓库信息（stars, 更新时间, 主要语言）
3. 更新README.md中的表格数据
4. 支持按stars数或更新时间排序

使用说明：
1. 设置GITHUB_TOKEN环境变量可提高API速率限制
2. 直接运行: python update_resources.py
3. GitHub Actions会自动每周运行此脚本
"""

import re
import requests
import os
import time
import sys
from datetime import datetime
from typing import Optional, Tuple, List, Dict

# GitHub API配置
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'User-Agent': 'TechStack-Radar-AutoUpdate/1.0'
} if GITHUB_TOKEN else {
    'User-Agent': 'TechStack-Radar-AutoUpdate/1.0'
}

# API基础URL
GITHUB_API_BASE = "https://api.github.com/repos"

def get_repo_info(repo_url: str) -> Optional[Dict]:
    """
    获取GitHub仓库的详细信息

    Args:
        repo_url: GitHub仓库URL

    Returns:
        包含仓库信息的字典，或None（如果获取失败）
    """
    # 提取owner和repo名
    match = re.search(r'github\.com/([^/]+)/([^/]+)', repo_url)
    if not match:
        print(f"❌ 无效的GitHub URL: {repo_url}")
        return None

    owner, repo = match.groups()
    if repo.endswith('.git'):
        repo = repo[:-4]

    api_url = f"{GITHUB_API_BASE}/{owner}/{repo}"

    try:
        response = requests.get(api_url, headers=HEADERS, timeout=15)

        if response.status_code == 200:
            data = response.json()

            # 提取所需信息
            repo_info = {
                'full_name': data.get('full_name', ''),
                'html_url': data.get('html_url', ''),
                'description': data.get('description', ''),
                'stargazers_count': data.get('stargazers_count', 0),
                'language': data.get('language', 'Unknown'),
                'updated_at': data.get('updated_at', ''),
                'pushed_at': data.get('pushed_at', ''),
                'archived': data.get('archived', False)
            }

            # 格式化时间
            if repo_info['pushed_at']:
                dt = datetime.strptime(repo_info['pushed_at'], "%Y-%m-%dT%H:%M:%SZ")
                repo_info['pushed_at_formatted'] = dt.strftime("%Y-%m-%d")
            else:
                repo_info['pushed_at_formatted'] = '-'

            # 如果项目已归档，标记一下
            if repo_info['archived']:
                repo_info['language'] = f"📦 Archived | {repo_info['language']}"

            print(f"✅ 获取成功: {owner}/{repo} - ⭐{repo_info['stargazers_count']} - 🔄{repo_info['pushed_at_formatted']}")
            return repo_info

        elif response.status_code == 403:
            print(f"⚠️  API限制或权限不足: {repo_url}")
            return {'error': 'rate_limit'}
        elif response.status_code == 404:
            print(f"❌ 仓库不存在: {repo_url}")
            return None
        else:
            print(f"❌ API错误 {response.status_code}: {repo_url}")
            return None

    except Exception as e:
        print(f"❌ 请求异常 {repo_url}: {e}")
        return None

def extract_github_urls_from_text(text: str) -> List[str]:
    """
    从文本中提取所有GitHub仓库URL

    Args:
        text: 要解析的文本

    Returns:
        GitHub URL列表
    """
    # 匹配GitHub仓库URL
    pattern = r'https://github\.com/[a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+'
    urls = re.findall(pattern, text)

    # 去重并保持顺序
    seen = set()
    unique_urls = []
    for url in urls:
        if url not in seen:
            seen.add(url)
            unique_urls.append(url)

    return unique_urls

def format_number(num: int) -> str:
    """
    格式化数字

    Args:
        num: 要格式化的数字

    Returns:
        格式化后的字符串
    """
    return str(num)

def pad_cell(text: str, width: int) -> str:
    """
    保留，仅供其他可能用途，此处不再使用固定宽度填充
    """
    return text

def update_readme_table(readme_path: str):
    """
    更新README.md中的表格数据

    Args:
        readme_path: README.md文件路径
    """
    print("🔍 开始解析README.md...")

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 提取所有GitHub URL
    github_urls = extract_github_urls_from_text(content)
    print(f"📊 找到 {len(github_urls)} 个GitHub仓库")

    if not github_urls:
        print("⚠️  未找到GitHub仓库链接，跳过更新")
        return

    # 获取仓库信息
    repo_info_map = {}
    rate_limit_hit = False

    for i, url in enumerate(github_urls):
        print(f"🔄 处理 {i+1}/{len(github_urls)}: {url}")

        info = get_repo_info(url)
        if info:
            if 'error' in info and info['error'] == 'rate_limit':
                rate_limit_hit = True
                break
            repo_info_map[url] = info

        # 避免触发GitHub API速率限制
        if not GITHUB_TOKEN:
            time.sleep(1.5)  # 无token时更长的间隔

    if rate_limit_hit:
        print("⚠️  达到API速率限制，部分数据可能未更新")
        print("💡 建议设置GITHUB_TOKEN环境变量以提高限制")

    # 更新README内容
    updated_content = content

    for url, info in repo_info_map.items():
        # 构建替换模式
        repo_name = info['full_name'].split('/')[-1] if info['full_name'] else url.split('/')[-1]

        # 查找并更新stars数
        stars_pattern = rf'\[{re.escape(repo_name)}\]\({re.escape(url)}\)[^|]*\|[^|]*\|[^|]*\|\s*(\d+|\s*)\s*\|'
        stars_replacement = f'[{repo_name}]({url}) | {info.get("description", "")} | ⭐ {format_number(info["stargazers_count"])} |'

        # 先尝试更新stars列
        if re.search(stars_pattern, updated_content):
            updated_content = re.sub(stars_pattern, stars_replacement, updated_content)

        # 更新最近更新时间和技术栈
        # 这里需要更复杂的表格解析逻辑，下面会实现完整版本

    print("✅ README内容已更新")

    # 写入文件
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print(f"📁 已保存到 {readme_path}")

def parse_and_update_tables(readme_path: str):
    """
    完整的表格解析和更新函数

    Args:
        readme_path: README.md文件路径
    """
    print("🔍 开始完整表格解析...")

    with open(readme_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 表格解析状态
    in_table = False
    table_start = 0
    table_lines = []
    updated_lines = []

    for i, line in enumerate(lines):
        stripped = line.strip()

        # 检测表格开始（包含表头的行）
        if not in_table and '|' in stripped and ('仓库名' in stripped or 'Repository' in stripped):
            in_table = True
            table_start = i
            table_lines = [line]

        # 收集表格行
        elif in_table:
            table_lines.append(line)

            # 检测表格结束（空行或新章节）
            if (not stripped or stripped.startswith('#') or
                (i+1 < len(lines) and lines[i+1].strip().startswith('#'))):
                # 处理这个表格
                processed_table = process_table_section(table_lines)
                updated_lines.extend(processed_table)

                in_table = False
                table_lines = []

        # 非表格行
        elif not in_table:
            updated_lines.append(line)

    # 如果文件末尾还有表格
    if in_table and table_lines:
        processed_table = process_table_section(table_lines)
        updated_lines.extend(processed_table)

    # 写入文件
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.writelines(updated_lines)

    print(f"✅ 表格更新完成，已保存到 {readme_path}")

def process_table_section(table_lines: List[str]) -> List[str]:
    """
    处理单个表格部分

    Args:
        table_lines: 表格行列表

    Returns:
        处理后的表格行列表
    """
    if len(table_lines) < 3:  # 至少需要表头、分隔线、一行数据
        return table_lines

    # 解析表头，确定列索引
    header_line = table_lines[0].strip()
    header_parts = [p.strip() for p in header_line.split('|') if p.strip()]

    # 查找各列索引
    col_indices = {
        'name': -1,
        'stars': -1,
        'updated': -1
    }

    for i, col in enumerate(header_parts):
        if '仓库名' in col or 'Repository' in col:
            col_indices['name'] = i
        elif 'Stars' in col or '⭐' in col:
            col_indices['stars'] = i
        elif '最近更新' in col or 'Last Updated' in col or '🔄' in col:
            col_indices['updated'] = i

    # 如果没有找到必要的列，返回原样
    if col_indices['name'] == -1:
        return table_lines

    # 处理数据行
    result_lines = [table_lines[0]]  # 表头
    result_lines.append(table_lines[1])  # 分隔线

    data_rows = []

    for line in table_lines[2:]:
        stripped = line.strip()
        if not stripped or not '|' in stripped:
            # 非表格行，可能是表格结束
            result_lines.append(line)
            continue

        parts = [p.strip() for p in stripped.split('|')]
        # 移除首尾空元素
        if parts and parts[0] == '':
            parts.pop(0)
        if parts and parts[-1] == '':
            parts.pop(-1)

        # 提取GitHub URL
        github_url = None
        if col_indices['name'] < len(parts):
            cell_content = parts[col_indices['name']]
            url_match = re.search(r'https://github\.com/[a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+', cell_content)
            if url_match:
                github_url = url_match.group(0)

        # 如果有GitHub URL，获取信息
        if github_url:
            repo_info = get_repo_info(github_url)
            if repo_info and 'error' not in repo_info:
                # 更新stars列
                if col_indices['stars'] != -1:
                    if col_indices['stars'] >= len(parts):
                        # 扩展列表
                        parts.extend([''] * (col_indices['stars'] - len(parts) + 1))
                    parts[col_indices['stars']] = f"⭐ {format_number(repo_info['stargazers_count'])}"

                # 更新更新时间列
                if col_indices['updated'] != -1:
                    if col_indices['updated'] >= len(parts):
                        parts.extend([''] * (col_indices['updated'] - len(parts) + 1))
                    parts[col_indices['updated']] = f"🔄 {repo_info['pushed_at_formatted']}"

        # 确保所有列都存在
        max_cols = max(col_indices.values()) + 1
        while len(parts) < max_cols:
            parts.append('')

        data_rows.append(parts)

        # 避免API速率限制
        if not GITHUB_TOKEN and github_url:
            time.sleep(1.5)

    # 按stars数排序（可选）
    # 这里可以根据需要实现排序逻辑

    # 添加排序后的数据行
    for row in data_rows:
        result_lines.append('| ' + ' | '.join(row) + ' |\n')

    return result_lines

def main():
    """
    主函数
    """
    print("=" * 60)
    print("🚀 TechStack Radar - 自动化更新脚本")
    print("=" * 60)

    # 检查当前目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    readme_path = os.path.join(script_dir, 'README.md')

    if not os.path.exists(readme_path):
        print(f"❌ 未找到README.md文件: {readme_path}")
        sys.exit(1)

    print(f"📄 读取文件: {readme_path}")

    # 运行完整表格解析
    parse_and_update_tables(readme_path)

    print("=" * 60)
    print("🎉 脚本执行完成！")
    print("=" * 60)

if __name__ == "__main__":
    main()
