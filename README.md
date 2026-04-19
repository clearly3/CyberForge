# 🚀 TechStack Radar - 多技术领域资源大全

[![GitHub Stars](https://img.shields.io/github/stars/YOUR_USERNAME/MultiTech-Resource-Catalog?style=for-the-badge)](https://github.com/YOUR_USERNAME/MultiTech-Resource-Catalog/stargazers)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/YOUR_USERNAME/MultiTech-Resource-Catalog?style=for-the-badge)](https://github.com/YOUR_USERNAME/MultiTech-Resource-Catalog/commits/main)
[![License](https://img.shields.io/github/license/YOUR_USERNAME/MultiTech-Resource-Catalog?style=for-the-badge)](https://github.com/YOUR_USERNAME/MultiTech-Resource-Catalog/blob/main/LICENSE)
[![Auto Update](https://img.shields.io/badge/🔄-每周自动更新-blue?style=for-the-badge)](https://github.com/YOUR_USERNAME/MultiTech-Resource-Catalog/actions/workflows/auto_update.yml)

---

## 📖 简介

**TechStack Radar** 是一个精心策划的多技术领域开源资源目录，专注于**安全工具、AI开发、人工智能、渗透测试和开发工具**。本目录旨在为技术从业者、安全研究人员和AI开发者提供一个全面、最新的技术资源参考。

### ✨ 主要特性

- **🔄 自动更新**: 每周自动从GitHub API获取项目最新信息（Stars数、更新时间）
- **📊 多维度数据**: 包含项目地址，Stars、最近更新等信息
- **🏷️ 智能分类**: 按技术领域和用途分类，便于快速查找

### 📈 数据统计

> 📊 **最后更新**: 2026-04-17 | **总项目数**: 0 | **分类数**: 5
> ⚡ **更新频率**: 每周一自动更新 | 🛠️ **自动化脚本**: Python + GitHub Actions

---

## 📚 目录索引

- [🛡️时至今日仍旧好用的安全项目](#时至今日仍旧好用的安全项目)
  - [信息收集](#信息收集)
    - [企业信息收集](#企业信息收集)
    - [子域名收集](#子域名收集)
    - [端口扫描](#端口扫描)
    - [目录扫描](#目录扫描)
    - [URL收集](#URL收集)
    - [指纹识别](#指纹识别)
    - [综合工具](#综合工具)
    - [资产收集与测绘平台](#资产收集与测绘平台)
  - [web安全](#web安全)
    - [web渗透框架](#web渗透框架)
    - [OWASP Web Top10](#OWASP-Web-Top10)
    - [payload list](#payload-list)
    - [web漏洞](#web漏洞)
    - [webshell管理工具](#webshell管理工具)
    - [信息泄露](#信息泄露)
    - [字典](#字典)
  - [漏洞扫描](#漏洞扫描)
  - [漏洞利用](#渗透测试工具)
  - [POC资源](#POC资源)
  - [BurpSuite插件](#BurpSuite插件)
  - [浏览器插件](#浏览器插件)
  - [内网渗透](#内网渗透)
    - [内网信息收集](#内网信息收集)
    - [C2](#C2)
    - [权限提升](#权限提升)
  - [基础设施](#基础设施)
    - [代理池](#内网信息收集)
    - [环境搭建](#环境搭建)
  - [代码审计](#代码审计)
  - [蓝队工具资源](#蓝队工具资源)
- [🤖AI时代足够好用的资源项目](#AI时代足够好用的资源项目)
  - [AI编码助手](#AI编码助手)about claude code
  - [about-claude-code](#about-claude-code)
  - [MCP](#MCP)
  - [skills](#skills)
  - [渗透智能体](#渗透智能体)
  - [好用的AI工具](#好用的AI工具)



---

## 🛡️ 时至今日仍旧好用的安全项目

### 信息收集
#### 企业信息收集
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [ENScan_GO](https://github.com/wgpsec/ENScan_GO) | 只需输入名称即可收集该企业及其分支的互联网暴露信息 |  |  |

#### 子域名收集
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [Oneforall](https://github.com/shmilylty/OneForAll) | 强大的子域名收集工具，支持暴力枚举和多种API源收集 |  |  |
| [subfinder](https://github.com/projectdiscovery/subfinder) | 从30余种数据源快速被动收集子域名 |  |  |

#### 端口扫描
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [naabu](https://github.com/projectdiscovery/naabu) | 一款用Go语言编写的快速端口扫描器，注重可靠性和简洁性 |  |  |
| [Smap](https://github.com/s0md3v/Smap) | 无缝替代nmap的端口扫描工具 |  |  |
| [masnmapscan-V1.0](https://github.com/hellogoldsnakeman/masnmapscan-V1.0) | 结合了masscan和nmap的端口扫描器 |  |  |
| [webfinder-next](https://github.com/Liqunkit/webfinder-next) | Java语言开发的快速端口扫描器 |  |  |

#### 目录扫描
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [dirsearch](https://github.com/maurosoria/dirsearch) | 一个好用的目录扫描工具 |  |  |

#### URL收集
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [katana](https://github.com/projectdiscovery/katana) | 强大的爬虫框架，支持多种参数传入，全面收集目标URL |  |  |
| [urlhunter](https://github.com/utkusen/urlhunter) | 被动收集目标在互联网暴露的URL信息 |  |  |
| [urlfinder](https://github.com/projectdiscovery/urlfinder) | 无需主动扫描、快速被动收集目标URL的工具 |  |  |

#### 指纹识别
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [dismap](https://github.com/zhzyker/dismap) | 辅助红队快速定位目标资产信息 |  |  |
| [hfinger](https://github.com/HackAllSec/hfinger) | 一个用于web框架、CDN和CMS指纹识别的高性能命令行工具 |  |  |
| [P1finger](https://github.com/P001water/P1finger) | 面向红队的指纹识别工具 |  |  |

#### 综合工具
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [TscanPlus](https://github.com/TideSec/TscanPlus) | 支持信息收集、资产测绘、漏洞扫描的强大工具 |  |  |
| [Fine](https://github.com/fasnow/fine) | 针对企业信息收集、目标资产探测、小程序反编译的工具 |  |  |
| [mitan](https://github.com/kkbo8005/mitan) | Java编写的信息收集、资产测绘于一体的综合工具 |  |  |

#### 资产收集与测绘平台
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [nemo_go](https://github.com/hanc00l/nemo_go) | 自动化信息收集 |  |  |

### web安全
#### web渗透框架
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [BurpSuite](https://github.com/yaklang/yakit) | 最受欢迎的web应用测试框架，功能强大，插件丰富 |  |  |
| [Yakit](https://github.com/yaklang/yakit) | 单兵作战武器库 |  |  |
| [Caido](https://github.com/caido/caido) | rust语言编写的轻量的web应用测试框架，正在撼动burp的地位 |  |  |

#### OWASP-Web-Top10
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [sqlmap](https://github.com/sqlmapproject/sqlmap) | 发现sql注入后，快速利用它 |  |  |
| [ByPassTamperPlus](https://github.com/Tas9er/ByPassTamperPlus) | 提升sqlmap绕过waf能力的Tamper合集 |  |  |
| [ghauri](https://github.com/r0oth3x49/ghauri) | 与sqlmap神似的注入漏洞扫描工具 |  |  |
| [XSStrike](https://github.com/s0md3v/XSStrike) | 号称最好用的xss扫描器 |  |  |
| [liffy](https://github.com/mzfr/liffy) | 本地文件包含漏洞扫描工具 |  |  |
| [SSRFmap](https://github.com/swisskyrepo/SSRFmap) | 自动SSRF模糊测试与利用工具 |  |  |
| [xray](https://github.com/mzfr/liffy) | 本地文件包含漏洞扫描工具 |  |  |
| [liffy](https://github.com/mzfr/liffy) | 本地文件包含漏洞扫描工具 |  |  |

#### payload-list
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) | 几乎包含所有常见web漏洞payload的仓库 |  |  |
| [Payloader](https://github.com/3516634930/Payloader/) | 渗透测试payload速查 |  |  |

#### web漏洞
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [nomore403](https://github.com/devploit/nomore403) | 执行低误报的40x绕过方案 |  |  |
| [plecost](https://github.com/Plecost/plecost) | 针对WordPress的漏洞扫描工具 |  |  |

#### webshell管理工具
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [Godzilla](https://github.com/BeichenDream/Godzilla) | 好用的webshell管理工具 |  |  |
| [EtherGhost](https://github.com/Marven11/EtherGhost) | 游魂-支持PHP/JSP的webshell管理工具 |  |  |

#### 信息泄露
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [GitHack](https://github.com/lijiejie/GitHack) | .git文件夹泄露漏洞利用 |  |  |
| [gitleaks](https://github.com/gitleaks/gitleaks) | 一个秘钥泄露扫描工具 |  |  |
| [idea_exploit](https://github.com/lijiejie/idea_exploit) | 扫描idea配置文件中可能存在的敏感信息 |  |  |

#### 字典
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [nemo_go](https://github.com/hanc00l/nemo_go) | 自动化信息收集 |  |  |
| [Fine](https://github.com/yaklang/yakit) | 针对企业信息收集、目标资产探测、小程序反编译的工具 |  |  |
| [BurpSuite](https://github.com/yaklang/yakit) | 无需主动扫描、快速被动收集目标URL的工具 |  |  |

### 漏洞扫描
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [nuclei](https://github.com/projectdiscovery/nuclei) | 基于yaml语法定制漏洞模版的快速、低误报率的漏洞扫描工具 |  |  |
| [afrog](https://github.com/zan8in/afrog) | 轻量快速的扫描器，有着适合国内环境的poc |  |  |
| [xray](https://github.com/chaitin/xray) | 强大的支持被动式的web漏洞扫描器 |  |  |
| [dddd](https://github.com/SleepingBag945/dddd) | 只需一个参数即可完成信息收集到漏洞检测的全自动扫描 |  |  |
| [VscanPlus](https://github.com/youki992/VscanPlus) | vscan二次开发的版本，批量快速检测网站安全隐患 |  |  |

### 漏洞利用
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [ShiroAttack2](https://github.com/SummerSec/ShiroAttack2) | shiro反序列化漏洞综合利用工具 |  |  |
| [I-Wanna-Get-All](https://github.com/R4gd0ll/I-Wanna-Get-All) | 综合漏洞后渗透利用工具 |  |  |

### POC资源
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [cve](https://github.com/trickest/cve) | 这是一个cve漏洞仓库，作者声称所有poc均公开可用 |  |  |
| [PoC-in-GitHub](https://github.com/nomi-sec/PoC-in-GitHub) | 一个持续更新的cve漏洞仓库 |  |  |
| [Vulnerability-Wiki-PoC](https://github.com/SourByte05/Vulnerability-Wiki-PoC) | 2024-至今1Day漏洞PoC深度研究与复现归档 |  |  |
| [Awesome-POC](https://github.com/Threekiii/Awesome-POC) | 一个漏洞 PoC 知识库 |  |  |
| [POC](https://github.com/eeeeeeeeee-code/POC) | wy876的POC镜像仓库 |  |  |
| [nuclei_poc](https://github.com/adysec/nuclei_poc) | 一个nuclei的模版仓库 |  |  |

### BurpSuite插件
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [BypassPro](https://github.com/0x727/BypassPro) | 自动化绕过40x和waf的burp插件 |  |  |
| [burp-ai-agent](https://github.com/six2dez/burp-ai-agent) | 让AI与BurpSuite无缝衔接 |  |  |


### 浏览器插件
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [HackTools](https://github.com/LasCC/HackTools) | 面向红队和渗透测试人员的一体化浏览器插件 |  |  |
| [SnowEyes](https://github.com/SickleSec/SnowEyes) | 网站解析、网页敏感信息检测、指纹识别的chrome插件 |  |  |
| [keyFinder](https://github.com/momenbasel/keyFinder) | 被动发现各种API密钥和敏感信息的浏览器插件 |  |  |
| [VueCrack](https://github.com/Ad1euDa1e/VueCrack) | 红队浏览器插件-检测VUE站点未授权漏洞 |  |  |
| [CloudVueRoute](https://github.com/cloud-jie/CloudVueRoute) | 快速提取Vue应用中路由信息的浏览器脚本 |  |  |
| [Vue-Router](https://github.com/dear-cell/Vue-Router) | 自动测试Vue路由接口的chorme插件 |  |  |

### 内网渗透
#### 内网信息收集
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [e0e1-config](https://github.com/eeeeeeeeee-code/e0e1-config) | 收集浏览器、数据库连接工具等敏感信息的后渗透工具 |  |  |
| [MX1014](https://github.com/L-codes/MX1014) | 大小仅2M左右，适合红队在内网进行快速端口扫描 |  |  |

#### C2
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [sliver](https://github.com/BishopFox/sliver) | 可跨平台运行，支持linux后门生成的C2 |  |  |
| [Viper](https://github.com/FunnyWolf/Viper) | 基于人工智能的对抗模拟和红队演练平台 |  |  |
| [XiebroC2](https://github.com/INotGreen/XiebroC2) | 神似Cobalt Strike的C2客户端、功能多样且强大 |  |  |
| [Wyrm](https://github.com/0xflux/Wyrm) | 红队后渗透框架 |  |  |
| [Spark](https://github.com/0xflux/Spark) | 一个免费、安全、开源、基于网页、跨平台且功能丰富的远程管理工具 |  |  |
| [conquest](https://github.com/jakobfriedl/conquest) | 基于Nim语言开发的高度可定制的C2框架 |  |  |

#### 权限提升
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [RedSun](https://github.com/Nightmare-Eclipse/RedSun) | 利用windows defender进行提权 |  |  |

### 基础设施
#### 代理池
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [ProxyPool](https://github.com/XiaomingX/proxy-pool) | 帮助用户自动维护高质量的代理池 |  |  |
| [Deadpool](https://github.com/thinkoaa/Deadpool) | Go编写的代理池轮询工具 |  |  |
| [mubeng](https://github.com/mubeng/mubeng) | 一款速度极快、使用便捷的代理服务器检测和IP轮换工具 |  |  |
| [fir-proxy](https://github.com/11firefly11/fir-proxy) | 一个轮换代理的图形化代理池程序 |  |  |

#### 环境搭建
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [f8x](https://github.com/ffffffff0x/f8x) | 红蓝队环境自动化部署工具 |  |  |
| [redc](https://github.com/wgpsec/redc) | 集成了AI的红队基础设施部署GUI工具 |  |  |
| [penetration-suite-toolkit](https://github.com/makoto56/penetration-suite-toolkit) | 包含常见渗透测试工具环境的windows虚拟机 |  |  |
| [copy-cert](https://github.com/virusdefender/copy-cert) | 通过生成ssl证书伪造c2流量 |  |  |

---

## 🤖 AI时代足够好用的资源项目

### AI编码助手

| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [Claude Code](https://github.com/anthropics/claude-code) | 最好用、最受欢迎的AI编码助手 |  |  |
| [Codex](https://github.com/openai/codex) | OpenAI推出的编程助手，支持代码生成、解释和调试 |  |  |
| [Cursor](https://cursor.com/) | 基于VSCode深度定制的AI原生IDE |  |  |
| [OpenCode](https://opencode.ai/) | 完全开源免费的AI编码工具 |  |  |
| [Trae](https://www.trae.cn/) | 字节跳动推出的AI原生集成开发环境 |  |  |
| [Kiro](https://kiro.dev/) | 亚马逊推出的AI IDE |  |  |
| [Qoder](https://qoder.com/) | 阿里巴巴开发的编程智能体，特色是专家团开发 |  |  |
| [qwen-code](https://github.com/QwenLM/qwen-code) | 阿里巴巴推出的基于Qwen3-Coder的命令行编程智能体 |  |  |
| [kimi-cli](https://github.com/MoonshotAI/kimi-cli) | kimi推出的命令行通用智能体工具 |  |  |
| [Lingma](https://lingma.aliyun.com/) | 阿里云推出的免费的图形化编程智能体 |  |  |

### about-claude-code
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [cc-haha](https://github.com/NanmiCoder/cc-haha) | 基于cc泄露源码打造的本地可运行的claude-claude客户端 |  |  |
| [claude-code-ccb](https://github.com/claude-code-best/claude-code) | 高度可自定义的claude-code开源构建版 |  |  |
| [clawgod](https://github.com/0Chencc/clawgod) | 一个claude code补丁，解锁了禁止网络安全相关测试的限制 |  |  |
| [claude-code-book](https://github.com/lintsinghua/claude-code-book) | 当所有人都在教你怎么用AI Agent——这本书带你拆开它 |  |  |
| [claude-hud](https://github.com/jarrodwatts/claude-hud) | 实时查看cc的上下文、工具调用、待办事项等状态的插件 |  |  |
| [claude-plugin-wechat](https://github.com/lc2panda/claude-plugin-wechat) | 微信、飞书无缝对接Claude-Code |  |  |

### MCP
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [web-search-fast](https://github.com/uk0/web-search-fast) | 一个简单的本地 web search mcp |  |  |
| [cve-mcp-server](https://github.com/mukul975/cve-mcp-server) |  AI驱动的安全情报聚合与风险判断工具 |  |  |
| [chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 让AI调试浏览器 |  |  |

### skills
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [pua](https://github.com/tanweai/pua) | 一个赋予AI agent高能动性的skills |  |  |
| [wooyun-legacy](https://github.com/tanweai/wooyun-legacy) | 给AI安全报告加上真实案例背书和数据支撑 |  |  |
| [xianzhi-research](https://github.com/tanweai/xianzhi-research) | 声称能让AI能够像顶尖安全研究员一样思考 |  |  |
| [web3-bug-bounty-hunting-ai-skills](https://github.com/shuvonsec/web3-bug-bounty-hunting-ai-skills) | 一个应用于AI的智能合约安全知识库 |  |  |
| [Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | 内置754个安全技能，将人类安全专家的实践经验转化为AI可执行的结构化知识 |  |  |
| [superpowers](https://github.com/obra/superpowers) | 提升agent的自主性和规范性，头脑风暴skills |  |  |
| [awesome-claude-skills-security](https://github.com/Eyadkelleh/awesome-claude-skills-security) | 为claude-code提供安全性测试和CTF解题的能力 |  |  |

### 渗透智能体
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [strix](https://github.com/usestrix/strix) | 开源AI黑客将发现并修复您应用的漏洞 |  |  |
| [airecon](https://github.com/pikpikcu/airecon) | 一个借助本地大模型进行类似人工的渗透测试活动的开源智能体 |  |  |
| [pentagi](https://github.com/vxcontrol/pentagi) | 利用前沿AI技术进行自动化渗透测试，适用于安全专家、研究人员和爱好者 |  |  |
| [superclaw](https://github.com/SuperagenticAI/superclaw) | 一个基于AI的，场景驱动、行为优先的安全测试工具 |  |  |

### 好用的AI工具
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [claudecodeui](https://github.com/siteboon/claudecodeui) | 提供一个web-ui，更好的管理AI编程工具会话和使用它们 |  |  |
| [cc-switch](https://github.com/farion1231/cc-switch) | 更方便配置claude-code和其他AI编码助手的客户端程序 |  |  |
| [rtk](https://github.com/rtk-ai/rtk) |  让你的AI节省60%-90%的token |  |  |
| [openai-captcha-detection](https://github.com/XiaomingX/openai-captcha-detection) | 借助AI来进行高准确率的验证码识别 |  |  |
| [vibe-kanban](https://github.com/BloopAI/vibe-kanban) | 卡片式的任务编排，让你的claude-code、codex工作效率大大提高 |  |  |


---

## 🔧 使用与贡献

### 如何使用

1. 浏览对应分类查找相关工具
2. 点击仓库名访问GitHub项目页面
3. 查看Stars数和最近更新了解项目活跃度
4. 根据图标类型选择适合的工具

### 如何贡献

我们欢迎社区贡献！如需添加新项目，请：

1. Fork本仓库
2. 在对应分类的表格中添加新行
3. 确保"仓库名"列为有效的GitHub URL
4. 提交Pull Request

**格式要求**:
- "仓库名"列: 必须包含完整的GitHub URL
- "描述"列: 简洁明了的中文或英文描述
- "🏷️"列: 根据项目类型添加对应图标（如🛡️安全、🌐浏览器插件、🤖AI工具等）

### 自动更新说明

- 本目录使用自动化脚本每周更新Stars数和最近更新时间
- 添加新项目时只需提供GitHub URL，脚本会自动获取其他信息
- 如需手动触发更新，请前往GitHub Actions页面运行工作流

---

## ⚙️ 技术架构

### 自动化系统

- **更新脚本**: `update_resources.py` - Python脚本，解析README并调用GitHub API
- **工作流**: `.github/workflows/auto_update.yml` - GitHub Actions每周自动运行
- **数据获取**: 通过GitHub REST API获取 `stargazers_count` 和 `pushed_at`

### 项目结构

```
MultiTech-Resource-Catalog/
├── README.md                    # 主目录文件
├── reademe_en.md                # 英文版本
├── update_resources.py          # 自动化更新脚本
├── requirements.txt             # Python依赖
├── .github/workflows/
│   └── auto_update.yml          # 自动更新工作流
├── CONTRIBUTING.md              # 贡献指南（可选）
└── LICENSE                      # 许可证文件
```

---

## 📄 许可证

本项目采用 [MIT License](LICENSE) 开源协议。

---

## 🙏 致谢

感谢所有开源项目的贡献者，以及参考项目的启发：

- [All-Defense-Tool](https://github.com/L0una/All-Defense-Tool) - 安全工具目录设计参考
- [Awesome-Hacking](https://github.com/Hack-with-Github/Awesome-Hacking) - 资源聚合思路参考

**保持更新，持续学习！** 🚀

> 📧 如有建议或问题，请通过GitHub Issues提交反馈。
