# CyberForge - QWEN.md

## 项目概述

**CyberForge** 是一个网络安全资源导航仓库，专注于为安全从业者和爱好者整理优质工具和资源。项目核心是一个 README.md 文档，通过表格形式分类展示各类安全工具，并配备自动更新脚本每周同步 GitHub 仓库的 Stars 和更新时间数据。

**核心技术栈：** Python（自动更新脚本）、GitHub Actions（定时任务）

---

## 目录结构

```
CyberForge/
├── README.md              # 资源导航主文档（核心内容）
├── update_resources.py    # 自动更新脚本
├── requirements.txt       # Python 依赖
├── .gitignore
└── .github/
    └── workflows/
        └── auto_update.yml  # GitHub Actions 定时任务
```

---

## 主要文件说明

### README.md
资源导航主文档，包含以下分类：

**🛡️ 传统安全项目**
- 信息收集（企业信息、网络测绘、子域名、端口扫描、目录扫描、JS/URL收集、指纹识别）
- Web安全（渗透框架、OWASP Top10、Payload列表、Web漏洞）
- 漏洞扫描与利用
- POC资源
- BurpSuite/浏览器插件
- 内网渗透（C2、权限提升）
- 基础设施（代理池、环境搭建）
- 面试题

**🤖 AI时代资源**
- AI学习资料
- AI编码助手（Claude Code、Cursor、Qwen Code 等）
- Claude Code 相关项目
- MCP（Model Context Protocol）资源
- Skills（安全技能包）
- 渗透智能体
- AI工具

### update_resources.py
自动更新脚本，功能包括：
- 解析 README.md 中的 GitHub 仓库链接
- 调用 GitHub API 获取仓库信息（Stars、更新时间、语言）
- 更新 README.md 中的表格数据
- 支持设置 `GITHUB_TOKEN` 环境变量避免 API 速率限制

### .github/workflows/auto_update.yml
- **触发方式：** 每周一 UTC 0点（北京时间周一 08:00）自动运行
- **手动触发：** 支持 workflow_dispatch 手动执行
- **工作流程：** Checkout → 安装依赖 → 运行更新脚本 → 提交变更

---

## 常用操作

### 本地运行更新脚本

```bash
# 安装依赖
pip install -r requirements.txt

# 运行更新脚本（无需 token，有速率限制）
python update_resources.py

# 使用 GitHub Token 提升 API 限制
export GITHUB_TOKEN=your_token_here
python update_resources.py
```

### 查看 GitHub Actions 日志

仓库页面 → Actions → "🔄 Auto Update Resource Catalog" → 查看运行历史

---

## 添加新资源

在 README.md 中对应的分类表格下添加新行，格式如下：

```markdown
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [仓库名](https://github.com/owner/repo) | 简要描述 | - | - |
```

**注意：** 脚本会自动更新 Stars 和更新时间列，无需手动填写。

---

## 注意事项

1. **API 速率限制：** 无 GitHub Token 时每分钟约 60 次请求，有 Token 约 5000 次
2. **已归档仓库：** 脚本会标记为 `📦 Archived`，方便识别不再维护的项目
3. **表格格式依赖：** 脚本依赖特定表格格式（表头需包含"仓库名"、"Stars"、"最近更新"）
4. **提交约定：** 自动提交信息格式为 `🔄 Auto-update resource catalog - YYYY-MM-DD`