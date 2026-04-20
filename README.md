# ⚔️ CyberForge

**网络安全人员的资源雷达**

---
[![Stars](https://img.shields.io/github/stars/clearly3/CyberForge?style=flat-square&color=yellow)](https://github.com/clearly3/CyberForge/stargazers)&nbsp;
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](#)&nbsp;
[![Security](https://img.shields.io/badge/Security-FF4D4D?style=flat-square)](#)&nbsp;
[![AI-Agent](https://img.shields.io/badge/AI--Agent-00FF88?style=flat-square)](#)&nbsp;
[![Pentest](https://img.shields.io/badge/Pentest-FFA116?style=flat-square&logo=linux&logoColor=white)](#)&nbsp;
[![Auto Sync](https://img.shields.io/badge/AUTO--SYNC-WEEKLY-7B61FF?style=flat-square)](#)&nbsp;

---

## 📖 简介

这是一个专注**网络安全**、**渗透测试**与**AI安全领域**的开源资源导航。我们整理在以往的岁月中好用、优秀的工具、资源，同样也收集在AI时代好用、有趣、值得学习和研究的开源项目，过滤噪音，帮助网络安全从业人员和爱好者在浩如烟海的GitHub中快速找到真正值得投入精力的资源。

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
  - [AI编码助手](#AI编码助手)
  - [about claude-code](#about-claude-code)
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
| [ENScan_GO](https://github.com/wgpsec/ENScan_GO) | 只需输入名称即可收集该企业及其分支的互联网暴露信息 | 4336    | 2026-03-30 |
#### 子域名收集
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [Oneforall](https://github.com/shmilylty/OneForAll)        | 强大的子域名收集工具，支持暴力枚举和多种API源收集 | 9737    | 2025-09-12 |
| [subfinder](https://github.com/projectdiscovery/subfinder) | 从30余种数据源快速被动收集子域名          | 13458   | 2026-04-18 |
#### 端口扫描
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [nmap](https://github.com/nmap/nmap)                                      | 是的，它仍然是最好用的端口扫描器之一          | 12729   | 2026-04-16 |
| [naabu](https://github.com/projectdiscovery/naabu)                        | 一款用Go语言编写的快速端口扫描器，注重可靠性和简洁性 | 5887    | 2026-04-13 |
| [Smap](https://github.com/s0md3v/Smap)                                    | 无缝替代nmap的端口扫描工具             | 3211    | 2026-04-13 |
| [masnmapscan-V1.0](https://github.com/hellogoldsnakeman/masnmapscan-V1.0) | 结合了masscan和nmap的端口扫描器       | 831     | 2026-02-06 |
| [webfinder-next](https://github.com/Liqunkit/webfinder-next)              | Java语言开发的快速端口扫描器            | 88      | 2022-04-24 |
#### 目录扫描
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [dirsearch](https://github.com/maurosoria/dirsearch) | 一个好用的目录扫描工具 | 14186   | 2026-03-16 |
#### URL收集
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [katana](https://github.com/projectdiscovery/katana)       | 强大的爬虫框架，支持多种参数传入，全面收集目标URL | 16549   | 2026-04-16 |
| [urlhunter](https://github.com/utkusen/urlhunter)          | 被动收集目标在互联网暴露的URL信息         | 1678    | 2025-01-23 |
| [urlfinder](https://github.com/projectdiscovery/urlfinder) | 无需主动扫描、快速被动收集目标URL的工具      | 860     | 2026-01-05 |
#### 指纹识别
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [dismap](https://github.com/zhzyker/dismap)       | 辅助红队快速定位目标资产信息                 | 2143    | 2024-01-29 |
| [hfinger](https://github.com/HackAllSec/hfinger)  | 一个用于web框架、CDN和CMS指纹识别的高性能命令行工具 | 300     | 2026-04-09 |
| [P1finger](https://github.com/P001water/P1finger) | 面向红队的指纹识别工具                    | 440     | 2025-08-05 |
#### 综合工具
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [TscanPlus](https://github.com/TideSec/TscanPlus) | 支持信息收集、资产测绘、漏洞扫描的强大工具     | 3277    | 2026-04-08 |
| [Fine](https://github.com/fasnow/fine)            | 针对企业信息收集、目标资产探测、小程序反编译的工具 | 1278    | 2026-04-02 |
| [mitan](https://github.com/kkbo8005/mitan)        | Java编写的信息收集、资产测绘于一体的综合工具  | 1760    | 2025-05-10 |
#### 资产收集与测绘平台
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [nemo_go](https://github.com/hanc00l/nemo_go) | 自动化信息收集 | 2039    | 2026-02-09 |
### web安全
#### web渗透框架
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [BurpSuite](https://github.com/yaklang/yakit) | 最受欢迎的web应用测试框架，功能强大，插件丰富          | 7179    | 2026-04-17 |
| [Yakit](https://github.com/yaklang/yakit)     | 单兵作战武器库                           | 7179    | 2026-04-17 |
| [Caido](https://github.com/caido/caido)       | rust语言编写的轻量的web应用测试框架，正在撼动burp的地位 | 2291    | 2026-04-10 |
#### OWASP-Web-Top10
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [sqlmap](https://github.com/sqlmapproject/sqlmap)              | 发现sql注入后，快速利用它           | 37100   | 2026-04-17 |
| [ByPassTamperPlus](https://github.com/Tas9er/ByPassTamperPlus) | 提升sqlmap绕过waf能力的Tamper合集 | 114     | 2026-02-12 |
| [ghauri](https://github.com/r0oth3x49/ghauri)                  | 与sqlmap神似的注入漏洞扫描工具       | 3969    | 2025-10-04 |
| [XSStrike](https://github.com/s0md3v/XSStrike)                 | 号称最好用的xss扫描器             | 14899   | 2025-04-26 |
| [liffy](https://github.com/mzfr/liffy)                         | 本地文件包含漏洞扫描工具             | 947     | 2025-10-01 |
| [SSRFmap](https://github.com/swisskyrepo/SSRFmap)              | 自动SSRF模糊测试与利用工具          | 3531    | 2025-09-04 |
| [SSTImap](https://github.com/vladko312/SSTImap)                | 发现模版注入时自动化利用             | 1469    | 2026-03-22 |
#### payload-list
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) | 几乎包含所有常见web漏洞payload的仓库 | 77007   | 2026-04-18 |
| [Payloader](https://github.com/3516634930/Payloader/)                       | 渗透测试payload速查           | 335     | 2026-03-11 |
#### web漏洞
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [nomore403](https://github.com/devploit/nomore403) | 执行低误报的40x绕过方案      | 1584    | 2026-04-12 |
| [plecost](https://github.com/Plecost/plecost)      | 针对WordPress的漏洞扫描工具 | 364     | 2026-04-17 |
#### webshell管理工具
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [Godzilla](https://github.com/BeichenDream/Godzilla) | 好用的webshell管理工具           | 4365    | 2024-07-17 |
| [EtherGhost](https://github.com/Marven11/EtherGhost) | 游魂-支持PHP/JSP的webshell管理工具 | 673     | 2026-02-12 |
#### 信息泄露
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [GitHack](https://github.com/lijiejie/GitHack)           | .git文件夹泄露漏洞利用        | 3536    | 2023-02-01 |
| [gitleaks](https://github.com/gitleaks/gitleaks)         | 一个秘钥泄露扫描工具           | 26056   | 2026-03-25 |
| [idea_exploit](https://github.com/lijiejie/idea_exploit) | 扫描idea配置文件中可能存在的敏感信息 | 371     | 2022-08-05 |
| [heapdump_tool](https://github.com/wyzxxz/heapdump_tool) | heapdump泄露利用工具       | 1445    | 2024-05-21 |
#### 字典
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [nemo_go](https://github.com/TheKingOfDuck/fuzzDicts)                                 | Web Pentesting Fuzz 字典,一个就够了       | 8278    | 2023-11-13 |
| [Web-Fuzzing-Box](https://github.com/gh0stkey/Web-Fuzzing-Box)                        | Web 模糊测试字典与一些Payloads              | 2705    | 2026-03-23 |
| [AppSec-Payloads](https://github.com/sh377c0d3/AppSec-Payloads)                       | 包含漏洞payloads和web应用测试中各类场景的fuzz字典集合 | 925     | 2026-04-01 |
| [Blasting_dictionary](https://github.com/rootphantomer/Blasting_dictionary)           | 高效字典                               | 5276    | 2022-03-21 |
| [lutfumertceylan/top25-parameter](https://github.com/lutfumertceylan/top25-parameter) | 统计常见web漏洞常出没的25个参数                 | 1833    | 2024-06-09 |
### 漏洞扫描
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [nuclei](https://github.com/projectdiscovery/nuclei) | 基于yaml语法定制漏洞模版的快速、低误报率的漏洞扫描工具 | 27993   | 2026-04-18 |
| [afrog](https://github.com/zan8in/afrog)             | 轻量快速的扫描器，有着适合国内环境的poc         | 4242    | 2026-04-14 |
| [xray](https://github.com/chaitin/xray)              | 强大的支持被动式的web漏洞扫描器             | 11510   | 2024-10-29 |
| [dddd](https://github.com/SleepingBag945/dddd)       | 只需一个参数即可完成信息收集到漏洞检测的全自动扫描     | 1841    | 2024-08-02 |
| [VscanPlus](https://github.com/youki992/VscanPlus)   | vscan二次开发的版本，批量快速检测网站安全隐患     | 331     | 2026-03-10 |
### 漏洞利用
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [ShiroAttack2](https://github.com/SummerSec/ShiroAttack2)     | shiro反序列化漏洞综合利用工具 | 2465    | 2026-04-12 |
| [I-Wanna-Get-All](https://github.com/R4gd0ll/I-Wanna-Get-All) | 综合漏洞后渗透利用工具       | 1711    | 2025-12-11 |
### POC资源
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [cve](https://github.com/trickest/cve)                                         | 这是一个cve漏洞仓库，作者声称所有poc均公开可用 | 7699    | 2026-04-19 |
| [PoC-in-GitHub](https://github.com/nomi-sec/PoC-in-GitHub)                     | 一个持续更新的cve漏洞仓库             | 7653    | 2026-04-20 |
| [Vulnerability-Wiki-PoC](https://github.com/SourByte05/Vulnerability-Wiki-PoC) | 2024-至今1Day漏洞PoC深度研究与复现归档  | 779     | 2026-04-16 |
| [Awesome-POC](https://github.com/Threekiii/Awesome-POC)                        | 一个漏洞 PoC 知识库               | 4926    | 2026-03-23 |
| [POC](https://github.com/eeeeeeeeee-code/POC)                                  | wy876的POC镜像仓库              | 1904    | 2026-03-31 |
| [nuclei_poc](https://github.com/adysec/nuclei_poc)                             | 一个nuclei的模版仓库              | 2041    | 2026-04-19 |
### BurpSuite插件
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [BypassPro](https://github.com/0x727/BypassPro)           | 自动化绕过40x和waf的burp插件 | 1129    | 2026-02-28 |
| [burp-ai-agent](https://github.com/six2dez/burp-ai-agent) | 让AI与BurpSuite无缝衔接   | 988     | 2026-04-09 |
### 浏览器插件
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [HackTools](https://github.com/LasCC/HackTools)             | 面向红队和渗透测试人员的一体化浏览器插件        | 6683    | 2025-01-05 |
| [SnowEyes](https://github.com/SickleSec/SnowEyes)           | 网站解析、网页敏感信息检测、指纹识别的chrome插件 | 800     | 2026-01-13 |
| [keyFinder](https://github.com/momenbasel/keyFinder)        | 被动发现各种API密钥和敏感信息的浏览器插件      | 644     | 2026-04-14 |
| [VueCrack](https://github.com/Ad1euDa1e/VueCrack)           | 红队浏览器插件-检测VUE站点未授权漏洞        | 752     | 2025-09-09 |
| [CloudVueRoute](https://github.com/cloud-jie/CloudVueRoute) | 快速提取Vue应用中路由信息的浏览器脚本        | 129     | 2026-04-15 |
| [Vue-Router](https://github.com/dear-cell/Vue-Router)       | 自动测试Vue路由接口的chorme插件        | 9       | 2025-02-25 |
### 内网渗透
#### 内网信息收集
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [e0e1-config](https://github.com/eeeeeeeeee-code/e0e1-config) | 收集浏览器、数据库连接工具等敏感信息的后渗透工具 | 582     | 2026-03-01 |
| [MX1014](https://github.com/L-codes/MX1014)                   | 大小仅2M左右，适合红队在内网进行快速端口扫描  | 172     | 2025-05-28 |
#### C2
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [sliver](https://github.com/BishopFox/sliver)       | 可跨平台运行，支持linux后门生成的C2           | 11029   | 2026-04-19 |
| [Viper](https://github.com/FunnyWolf/Viper)         | 基于人工智能的对抗模拟和红队演练平台              | 5027    | 2026-03-31 |
| [XiebroC2](https://github.com/INotGreen/XiebroC2)   | 神似Cobalt Strike的C2客户端、功能多样且强大   | 1393    | 2025-02-28 |
| [Wyrm](https://github.com/0xflux/Wyrm)              | 红队后渗透框架                         | 482     | 2026-03-15 |
| [Spark](https://github.com/0xflux/Spark)            | 一个免费、安全、开源、基于网页、跨平台且功能丰富的远程管理工具 | -       | -          |
| [conquest](https://github.com/jakobfriedl/conquest) | 基于Nim语言开发的高度可定制的C2框架            | 350     | 2026-04-18 |
#### 权限提升
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [RedSun](https://github.com/Nightmare-Eclipse/RedSun) | 利用windows defender进行提权 | 1572    | 2026-04-15 |
### 基础设施
#### 代理池
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [ProxyPool](https://github.com/XiaomingX/proxy-pool)  | 帮助用户自动维护高质量的代理池            | 133     | 2026-03-08 |
| [Deadpool](https://github.com/thinkoaa/Deadpool)      | Go编写的代理池轮询工具               | 674     | 2025-04-21 |
| [mubeng](https://github.com/mubeng/mubeng)            | 一款速度极快、使用便捷的代理服务器检测和IP轮换工具 | 2084    | 2025-10-08 |
| [fir-proxy](https://github.com/11firefly11/fir-proxy) | 一个轮换代理的图形化代理池程序            | 569     | 2025-12-04 |
#### 环境搭建
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [f8x](https://github.com/ffffffff0x/f8x)                                           | 红蓝队环境自动化部署工具            | 2117    | 2026-04-15 |
| [redc](https://github.com/wgpsec/redc)                                             | 集成了AI的红队基础设施部署GUI工具     | 149     | 2026-04-18 |
| [penetration-suite-toolkit](https://github.com/makoto56/penetration-suite-toolkit) | 包含常见渗透测试工具环境的windows虚拟机 | 2938    | 2025-06-11 |
| [copy-cert](https://github.com/virusdefender/copy-cert)                            | 通过生成ssl证书伪造c2流量         | 349     | 2024-10-03 |
## 🤖 AI时代足够好用的资源项目

### AI编码助手

| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [Claude Code](https://github.com/anthropics/claude-code) | 最好用、最受欢迎的AI编码助手               | 115910  | 2026-04-18 |
| [Codex](https://github.com/openai/codex)                 | OpenAI推出的编程助手，支持代码生成、解释和调试    | 76335   | 2026-04-20 |
| [Cursor](https://cursor.com/)                            | 基于VSCode深度定制的AI原生IDE          | -       | -          |
| [OpenCode](https://opencode.ai/)                         | 完全开源免费的AI编码工具                 | -       | -          |
| [Trae](https://www.trae.cn/)                             | 字节跳动推出的AI原生集成开发环境             | -       | -          |
| [Kiro](https://kiro.dev/)                                | 亚马逊推出的AI IDE                  | -       | -          |
| [Qoder](https://qoder.com/)                              | 阿里巴巴开发的编程智能体，特色是专家团开发         | -       | -          |
| [qwen-code](https://github.com/QwenLM/qwen-code)         | 阿里巴巴推出的基于Qwen3-Coder的命令行编程智能体 | 23560   | 2026-04-20 |
| [kimi-cli](https://github.com/MoonshotAI/kimi-cli)       | kimi推出的命令行通用智能体工具             | 7913    | 2026-04-17 |
| [Lingma](https://lingma.aliyun.com/)                     | 阿里云推出的免费的图形化编程智能体             | -       | -          |
### about-claude-code
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [cc-haha](https://github.com/NanmiCoder/cc-haha)                         | 基于cc泄露源码打造的本地可运行的claude-claude客户端 | 6990    | 2026-04-19 |
| [claude-code-ccb](https://github.com/claude-code-best/claude-code)       | 高度可自定义的claude-code开源构建版           | 16361   | 2026-04-19 |
| [clawgod](https://github.com/0Chencc/clawgod)                            | 一个claude code补丁，解锁了禁止网络安全相关测试的限制  | 794     | 2026-04-16 |
| [claude-code-book](https://github.com/lintsinghua/claude-code-book)      | 当所有人都在教你怎么用AI Agent——这本书带你拆开它     | 2825    | 2026-04-06 |
| [claude-hud](https://github.com/jarrodwatts/claude-hud)                  | 实时查看cc的上下文、工具调用、待办事项等状态的插件        | 19988   | 2026-04-18 |
| [claude-plugin-wechat](https://github.com/lc2panda/claude-plugin-wechat) | 微信、飞书无缝对接Claude-Code              | 54      | 2026-04-13 |
### MCP
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [web-search-fast](https://github.com/uk0/web-search-fast)                    | 一个简单的本地 web search mcp | 40      | 2026-03-23 |
| [cve-mcp-server](https://github.com/mukul975/cve-mcp-server)                 | AI驱动的安全情报聚合与风险判断工具     | 251     | 2026-04-14 |
| [chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 让AI调试浏览器               | 36222   | 2026-04-19 |
### skills
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [pua](https://github.com/tanweai/pua)                                                               | 一个赋予AI agent高能动性的skills               | 16416   | 2026-04-19 |
| [wooyun-legacy](https://github.com/tanweai/wooyun-legacy)                                           | 给AI安全报告加上真实案例背书和数据支撑                  | 1568    | 2026-03-08 |
| [xianzhi-research](https://github.com/tanweai/xianzhi-research)                                     | 声称能让AI能够像顶尖安全研究员一样思考                  | 160     | 2026-01-29 |
| [web3-bug-bounty-hunting-ai-skills](https://github.com/shuvonsec/web3-bug-bounty-hunting-ai-skills) | 一个应用于AI的智能合约安全知识库                     | 54      | 2026-03-15 |
| [Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)        | 内置754个安全技能，将人类安全专家的实践经验转化为AI可执行的结构化知识 | 4778    | 2026-04-18 |
| [superpowers](https://github.com/obra/superpowers)                                                  | 提升agent的自主性和规范性，头脑风暴skills            | 159964  | 2026-04-16 |
| [awesome-claude-skills-security](https://github.com/Eyadkelleh/awesome-claude-skills-security)      | 为claude-code提供安全性测试和CTF解题的能力          | 182     | 2026-03-21 |
### 渗透智能体
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [strix](https://github.com/usestrix/strix)               | 开源AI黑客将发现并修复您应用的漏洞                 | 24226   | 2026-04-16 |
| [airecon](https://github.com/pikpikcu/airecon)           | 一个借助本地大模型进行类似人工的渗透测试活动的开源工具        | 389     | 2026-04-19 |
| [pentagi](https://github.com/vxcontrol/pentagi)          | 利用前沿AI技术进行自动化渗透测试，适用于安全专家、研究人员和爱好者 | 15213   | 2026-04-16 |
| [superclaw](https://github.com/SuperagenticAI/superclaw) | 一个基于AI的，场景驱动、行为优先的安全测试工具           | 229     | 2026-02-02 |
### 好用的AI工具
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [claudecodeui](https://github.com/siteboon/claudecodeui)                          | 提供一个web-ui，更好的管理AI编程工具会话和使用它们         | 10001   | 2026-04-18 |
| [cc-switch](https://github.com/farion1231/cc-switch)                              | 更方便配置claude-code和其他AI编码助手的客户端程序       | 47220   | 2026-04-20 |
| [rtk](https://github.com/rtk-ai/rtk)                                              | 让你的AI节省60%-90%的token                  | 30057   | 2026-04-19 |
| [openai-captcha-detection](https://github.com/XiaomingX/openai-captcha-detection) | 借助AI来进行高准确率的验证码识别                     | 204     | 2025-08-31 |
| [vibe-kanban](https://github.com/BloopAI/vibe-kanban)                             | 卡片式的任务编排，让你的claude-code、codex工作效率大大提高 | 25279   | 2026-04-18 |
### 项目结构

```
CyberForge/
├── README.md
├── update_resources.py
├── requirements.txt
└── .github/workflows/
    └── auto_update.yml
```
---

**保持更新，持续学习！**
