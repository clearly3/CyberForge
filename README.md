# CyberForge

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

这是一个**网络安全**、**渗透测试**与**AI安全领域**的开源资源导航。我们整理在以往的岁月中好用、优秀的工具、资源，同样也收集在AI时代好用、有趣、值得学习和研究的开源项目，过滤噪音，帮助网络安全从业人员和爱好者在浩如烟海的GitHub中快速找到真正值得投入精力的资源。

---

## 📚 目录索引

- [🛡️时至今日仍旧好用的安全项目](#时至今日仍旧好用的安全项目)
  - [信息收集](#信息收集)
    - [企业信息收集](#企业信息收集)
    - [网络空间测绘](#网络空间测绘)
    - [子域名收集](#子域名收集)
    - [端口扫描](#端口扫描)
    - [目录扫描&fuzz](#目录扫描&fuzz)
    - [JS&URL收集](#JS&URL收集)
    - [指纹识别](#指纹识别)
    - [综合工具](#综合工具)
    - [资产收集与测绘平台](#资产收集与测绘平台)
  - [web安全](#web安全)
    - [web渗透测试框架&抓包工具](#web渗透测试框架&抓包工具)
    - [web漏洞](#web漏洞)
    - [webshell管理工具](#webshell管理工具)
    - [信息泄露](#信息泄露)
    - [字典&payload](#字典&payload)
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
  - [靶场](#靶场)
  - [面试题](#面试题)
- [🤖AI时代足够好用的资源项目](#AI时代足够好用的资源项目)
  - [学习资料](#学习资料)
  - [AI编码助手](#编码助手&智能体)
  - [MCP](#MCP)
  - [skills](#skills)
  - [渗透智能体](#渗透智能体)
  - [好用的AI工具](#好用的AI工具)
- [信息获取](#信息获取)

---

## 🛡️ 时至今日仍旧好用的安全项目

### 信息收集
#### 企业信息收集
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [ENScan_GO](https://github.com/wgpsec/ENScan_GO) | 只需输入名称即可收集该企业及其分支的互联网暴露信息                | 4614    | 2026-03-30 |
| [ICP_Query](https://github.com/HG-ha/ICP_Query)  | 查询域名、APP、小程序、快应用以及企业的ICP备案信息，提供完全本地化的API | 1010    | 2026-08-04 |
#### 网络空间测绘
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [uncover](https://github.com/projectdiscovery/uncover)    | 利用多个搜索引擎快速发现互联网上暴露的主机。 | 3035    | 2026-08-05 |
| [FofaMap](https://github.com/asaotomo/FofaMap)            | 集成AI的智能测绘工具            | 699     | 2026-08-16 |
| [ThunderSearch](https://github.com/xzajyjs/ThunderSearch) | 轻量、小巧的测绘工具             | 670     | 2024-12-06 |
#### 子域名收集
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [Oneforall](https://github.com/shmilylty/OneForAll)          | 强大的子域名收集工具，支持暴力枚举和多种API源收集 | 9989    | 2026-05-11 |
| [subfinder](https://github.com/projectdiscovery/subfinder)   | 从30余种数据源快速被动收集子域名          | 14213   | 2026-08-12 |
| [csprecon](https://github.com/edoardottt/csprecon)           | 通过csp策略发现子域名               | 523     | 2026-08-12 |
| [shuffledns](https://github.com/projectdiscovery/shuffledns) | 子域名爆破工具                    | 1660    | 2026-08-10 |
#### 端口扫描
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [nmap](https://github.com/nmap/nmap)                                      | 是的，它仍然是最好用的端口扫描器之一          | 13365   | 2026-08-14 |
| [naabu](https://github.com/projectdiscovery/naabu)                        | 一款用Go语言编写的快速端口扫描器，注重可靠性和简洁性 | 6181    | 2026-08-13 |
| [Smap](https://github.com/s0md3v/Smap)                                    | 无缝替代nmap的端口扫描工具             | 3281    | 2026-08-15 |
| [masnmapscan-V1.0](https://github.com/hellogoldsnakeman/masnmapscan-V1.0) | 结合了masscan和nmap的端口扫描器       | 837     | 2026-02-06 |
| [webfinder-next](https://github.com/Liqunkit/webfinder-next)              | Java语言开发的快速端口扫描器            | 89      | 2022-04-24 |
| [TXPortMap](https://github.com/4dogs-cn/TXPortMap)                        | 轻量端口扫描器，内置指纹                | 672     | 2023-10-27 |
#### 目录扫描&fuzz
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [dirsearch](https://github.com/maurosoria/dirsearch) | 一个好用的目录扫描工具   | 14630   | 2026-08-16 |
| [feroxbuster](https://github.com/epi052/feroxbuster) | web敏感路径快速探测   | 8018    | 2026-04-15 |
| [fuff](https://github.com/ffuf/ffuf)                 | web-fuzz神器    | 16534   | 2026-07-19 |
| [arjun](https://github.com/s0md3v/Arjun)             | http参数fuzz小工具 | 6379    | 2025-02-20 |
#### JS&URL收集
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [katana](https://github.com/projectdiscovery/katana)       | 强大的爬虫框架，支持多种参数传入，全面收集目标URL                   | 17326   | 2026-08-16 |
| [urlfinder](https://github.com/pingc0y/URLFinder)          | 一款快速、全面、易用的页面信息提取工具，可快速发现和提取页面中的JS、URL和敏感信息。 | 3165    | 2026-06-17 |
| [urlhunter](https://github.com/utkusen/urlhunter)          | 被动收集目标在互联网暴露的URL信息                           | 1698    | 2025-01-23 |
| [urlfinder](https://github.com/projectdiscovery/urlfinder) | 无需主动扫描、快速被动收集目标URL的工具                        | 897     | 2026-08-10 |
| [xnLinkFinder](https://github.com/xnl-h4ck3r/xnLinkFinder) | 发现潜在的url参数、端点                                | 1584    | 2026-03-08 |
#### 指纹识别
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [dismap](https://github.com/zhzyker/dismap)         | 辅助红队快速定位目标资产信息                 | 2163    | 2024-01-29 |
| [TideFinger](https://github.com/TideSec/TideFinger) | 指纹识别小工具，汲取整合了多个web指纹库          | 2084    | 2023-05-23 |
| [hfinger](https://github.com/HackAllSec/hfinger)    | 一个用于web框架、CDN和CMS指纹识别的高性能命令行工具 | 328     | 2026-07-16 |
| [P1finger](https://github.com/P001water/P1finger)   | 面向红队的指纹识别工具                    | 456     | 2025-08-05 |
| [Ehole](https://github.com/EdgeSecurityTeam/EHole)  | 红队重点攻击系统指纹探测工具                 | 3509    | 2024-04-02 |
| [Finger](https://github.com/EASY233/Finger)         | 一款红队在大量的资产中存活探测与重点攻击系统指纹探测工具   | 1726    | 2023-12-22 |
#### 综合工具
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [TscanPlus](https://github.com/TideSec/TscanPlus) | 支持信息收集、资产测绘、漏洞扫描的强大工具     | 4194    | 2026-08-16 |
| [Fine](https://github.com/fasnow/fine)            | 针对企业信息收集、目标资产探测、小程序反编译的工具 | 1367    | 2026-05-19 |
| [mitan](https://github.com/kkbo8005/mitan)        | Java编写的信息收集、资产测绘于一体的综合工具  | 1868    | 2026-08-15 |
#### 资产收集与测绘平台
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [ARL](https://github.com/adysec/ARL)                    | ARL资产侦察灯塔系统 | 888     | 2026-08-16 |
| [nemo_go](https://github.com/hanc00l/nemo_go)           | 自动化信息收集     | 2083    | 2026-08-15 |
| [ScopeSentry](https://github.com/Autumn-27/ScopeSentry) | 一站式信息收集     | 1573    | 2026-07-26 |
| [xingrin](https://github.com/yyhuni/xingrin)            | 开源攻击面管理平台   | 642     | 2026-07-22 |
### web安全
#### web渗透测试框架&抓包工具
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [BurpSuite](https://portswigger.net/burp/communitydownload)       | 最受欢迎的web应用测试框架，功能强大，插件丰富          | -       | -          |
| [Yakit](https://github.com/yaklang/yakit)                         | 单兵作战武器库                           | 7682    | 2026-08-14 |
| [Caido](https://github.com/caido/caido)                           | rust语言编写的轻量的web应用测试框架，正在撼动burp的地位 | 2541    | 2026-07-10 |
| [zap](https://github.com/zaproxy/zaproxy)                         | Web应用扫描器，它免费且开源                   | 15620   | 2026-08-13 |
| [ChYing](https://github.com/yhy0/ChYing)                          | 开源的类BurpSuite应用                   | 718     | 2026-07-24 |
| [anything-analyzer](https://github.com/Mouseww/anything-analyzer) | 全协议抓包，把流量交给AI自动逆向分析，并支持流量继续转发     | 3519    | 2026-08-07 |
#### web漏洞
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [sqlmap](https://github.com/sqlmapproject/sqlmap)              | 发现sql注入后，快速利用它           | 38204   | 2026-08-16 |
| [ByPassTamperPlus](https://github.com/Tas9er/ByPassTamperPlus) | 提升sqlmap绕过waf能力的Tamper合集 | 123     | 2026-02-12 |
| [ghauri](https://github.com/r0oth3x49/ghauri)                  | 与sqlmap神似的注入漏洞扫描工具       | 4063    | 2025-10-04 |
| [XSStrike](https://github.com/s0md3v/XSStrike)                 | 号称最好用的xss扫描器             | 15139   | 2025-04-26 |
| [liffy](https://github.com/mzfr/liffy)                         | 本地文件包含漏洞扫描工具             | 979     | 2026-05-19 |
| [SSRFmap](https://github.com/swisskyrepo/SSRFmap)              | 自动SSRF模糊测试与利用工具          | 3603    | 2026-08-10 |
| [SSTImap](https://github.com/vladko312/SSTImap)                | 发现模版注入时自动化利用             | 1609    | 2026-04-25 |
| [nomore403](https://github.com/devploit/nomore403)             | 执行低误报的40x绕过方案            | 1831    | 2026-06-21 |
#### webshell管理工具
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [Godzilla](https://github.com/BeichenDream/Godzilla) | 好用的webshell管理工具           | 4453    | 2024-07-17 |
| [Behinder](https://github.com/rebeyond/Behinder/)    | “冰蝎”动态二进制加密网站管理客户端        | 6190    | 2023-08-24 |
| [EtherGhost](https://github.com/Marven11/EtherGhost) | 游魂-支持PHP/JSP的webshell管理工具 | 690     | 2026-08-07 |
#### 信息泄露
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [GitHack](https://github.com/lijiejie/GitHack)            | .git文件夹泄露漏洞利用                     | 3571    | 2023-02-01 |
| [gitleaks](https://github.com/gitleaks/gitleaks)          | 一个秘钥泄露扫描工具                        | 28760   | 2026-07-29 |
| [idea_exploit](https://github.com/lijiejie/idea_exploit)  | 扫描idea配置文件中可能存在的敏感信息              | 369     | 2022-08-05 |
| [heapdump_tool](https://github.com/wyzxxz/heapdump_tool)  | heapdump泄露利用工具                    | 1453    | 2024-05-21 |
| [API-Explorer](https://github.com/mrknow001/API-Explorer) | 在你拿到一个泄漏的飞书、企微、钉钉或者地图api的时候、快速利用它 | 793     | 2024-10-15 |
#### 字典&payload
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [fuzzDicts](https://github.com/TheKingOfDuck/fuzzDicts)                                | Web Pentesting Fuzz 字典,一个就够了       | 8417    | 2023-11-13 |
| [Web-Fuzzing-Box](https://github.com/gh0stkey/Web-Fuzzing-Box)                         | Web 模糊测试字典与一些Payloads              | 2787    | 2026-03-23 |
| [AppSec-Payloads](https://github.com/sh377c0d3/AppSec-Payloads)                        | 包含漏洞payloads和web应用测试中各类场景的fuzz字典集合 | 945     | 2026-04-01 |
| [Blasting_dictionary](https://github.com/rootphantomer/Blasting_dictionary)            | 高效字典                               | 5284    | 2022-03-21 |
| [lutfumertceylan/top25-parameter](https://github.com/lutfumertceylan/top25-parameter)  | 统计常见web漏洞常出没的25个参数                 | 1846    | 2024-06-09 |
| [PentesterSpecialDict](https://github.com/evilc0deooo/PentesterSpecialDict)            | 构建优化高效的渗透 fuzz 字典合集                | 1910    | 2025-06-17 |
| [SecDictionary](https://github.com/SexyBeast233/SecDictionary)                         | 实战沉淀字典                             | 1578    | 2026-08-16 |
| [Dictionary-Of-Pentesting](https://github.com/insightglacier/Dictionary-Of-Pentesting) | 渗透测试、SRC漏洞挖掘、爆破、Fuzzing等字典收集项目     | 2070    | 2023-07-21 |
| [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)            | 几乎包含所有常见web漏洞payload的仓库            | 80102   | 2026-08-09 |
| [Payloader](https://github.com/3516634930/Payloader/)                                  | 渗透测试payload速查                      | 494     | 2026-07-16 |
### 漏洞扫描
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [nuclei](https://github.com/projectdiscovery/nuclei) | 基于yaml语法定制漏洞模版的快速、低误报率的漏洞扫描工具 | 30546   | 2026-08-16 |
| [afrog](https://github.com/zan8in/afrog)             | 轻量快速的扫描器，有着适合国内环境的poc         | 4368    | 2026-08-04 |
| [plecost](https://github.com/Plecost/plecost)        | 针对WordPress的漏洞扫描工具            | 381     | 2026-08-05 |
| [VscanPlus](https://github.com/youki992/VscanPlus)   | vscan二次开发的版本，批量快速检测网站安全隐患     | 350     | 2026-03-10 |
| [xray](https://github.com/chaitin/xray)              | 强大的支持被动式的web漏洞扫描器             | 11706   | 2024-10-29 |
| [dddd](https://github.com/SleepingBag945/dddd)       | 只需一个参数即可完成信息收集到漏洞检测的全自动扫描     | 1923    | 2024-08-02 |
### 漏洞利用
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [I-Wanna-Get-All](https://github.com/R4gd0ll/I-Wanna-Get-All)      | 综合漏洞后渗透利用工具       | 1783    | 2025-12-11 |
| [ShiroAttack2](https://github.com/SummerSec/ShiroAttack2)          | shiro反序列化漏洞综合利用工具 | 2614    | 2026-06-04 |
| [ThinkphpGUI](https://github.com/Lotus6/ThinkphpGUI)               | thinkphp全版本漏洞检测工具 | 1593    | 2022-06-01 |
| [WeaverExploit_All](https://github.com/zhaoyumi/WeaverExploit_All) | 泛微漏洞批量检测工具        | 479     | 2023-12-14 |
| [NacosExploit](https://github.com/h0ny/NacosExploit)               | Nacos综合漏洞利用工具     | 680     | 2025-11-03 |
| [Frchannel](https://github.com/7wkajk/Frchannel)                   | 帆软反序列化漏洞利用工具      | 427     | 2025-01-25 |
### POC资源
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [cve](https://github.com/trickest/cve)                                         | 这是一个cve漏洞仓库，作者声称所有poc均公开可用 | 8003    | 2026-08-16 |
| [PoC-in-GitHub](https://github.com/nomi-sec/PoC-in-GitHub)                     | 一个持续更新的cve漏洞仓库             | 7973    | 2026-08-16 |
| [Vulnerability-Wiki-PoC](https://github.com/SourByte05/Vulnerability-Wiki-PoC) | 2024-至今1Day漏洞PoC深度研究与复现归档  | 1064    | 2026-08-13 |
| [Awesome-POC](https://github.com/Threekiii/Awesome-POC)                        | 一个漏洞 PoC 知识库               | 5147    | 2026-05-11 |
| [POC](https://github.com/eeeeeeeeee-code/POC)                                  | wy876的POC镜像仓库              | 2151    | 2026-07-13 |
| [nuclei_poc](https://github.com/adysec/nuclei_poc)                             | 一个nuclei的模版仓库              | 2132    | 2026-08-12 |
### BurpSuite插件
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [BypassPro](https://github.com/0x727/BypassPro)                 | 自动化绕过40x和waf的burp插件                                | 1315    | 2026-05-10 |
| [APIKit](https://github.com/API-Security/APIKit)                | 被动挖掘各种API泄露                                        | 2286    | 2024-04-02 |
| [Wsdler](https://github.com/NetSPI/Wsdler)                      | 解析wsdler请求，并自动化测试其中的接口                             | 284     | 2018-06-25 |
| [nowafpls](https://github.com/assetnote/nowafpls)               | 在burp数据包中插入垃圾数据绕过waf                               | 1502    | 2025-07-14 |
| [burp-awesome-tls](https://github.com/sleeyax/burp-awesome-tls) | 将burp流量伪造成多种浏览器                                    | 1889    | 2026-08-13 |
| [HaE](https://github.com/gh0stkey/HaE)                          | 检查经过burp的流量，挖掘敏感信息，并高亮显示                           | 4362    | 2026-07-31 |
| [TsojanScan](https://github.com/Tsojan/TsojanScan)              | 一个集成常见漏洞探测的BurpSuite插件                             | 1563    | 2026-07-20 |
| [burp-ai-agent](https://github.com/six2dez/burp-ai-agent)       | 让AI与BurpSuite无缝衔接                                  | 1408    | 2026-08-05 |
| [burp-mcp](https://github.com/PortSwigger/mcp-server)           | 使用MCP协议将Burp Suite与AI客户端集成                         | 1070    | 2026-08-14 |
| [BurpMCP-Ultra](https://github.com/Cy-S3c/BurpMCP-Ultra)        | 将burp的api结构化为100多种工具，并集成多种漏洞检测功能，理论上强于官方的burpmcp工具 | 190     | 2026-08-05 |
### 浏览器插件
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [wappalyzer](https://chromewebstore.google.com/detail/wappalyzer-technology-pro/gppongmhjkpfnbhagpmjfkannfbllamg?hl=zh-CN&utm_source=ext_sidebar) | 快速识别目标网站技术栈的浏览器插件             | -       | -          |
| [HackTools](https://github.com/LasCC/HackTools)                                                                                                   | 面向红队和渗透测试人员的一体化浏览器插件          | 6984    | 2025-01-05 |
| [SnowEyes](https://github.com/SickleSec/SnowEyes)                                                                                                 | 网站解析、网页敏感信息检测、指纹识别的chrome插件   | 902     | 2026-08-10 |
| [keyFinder](https://github.com/momenbasel/keyFinder)                                                                                              | 被动发现各种API密钥和敏感信息的浏览器插件        | 697     | 2026-07-19 |
| [VueCrack](https://github.com/Ad1euDa1e/VueCrack)                                                                                                 | 红队浏览器插件-检测VUE站点未授权漏洞          | 915     | 2026-05-07 |
| [CloudVueRoute](https://github.com/cloud-jie/CloudVueRoute)                                                                                       | 快速提取Vue应用中路由信息的浏览器脚本          | 130     | 2026-04-15 |
| [Heimdallr](https://github.com/Ghr07h/Heimdallr)                                                                                                  | 识别目标是否是蜜罐                     | 1680    | 2023-01-19 |
| [random-user-agent](https://github.com/tarampampam/random-user-agent)                                                                             | 自动伪造浏览器的UA头为任意值               | 752     | 2026-08-14 |
| [DotGit](https://github.com/davtur19/DotGit)                                                                                                      | 被动监测目标网站是否有.git/.svn/.hg等文件泄露 | 480     | 2026-07-31 |
| [onetab](https://chromewebstore.google.com/detail/onetab/chphlpgkkbolifaimnlloiipkdnihall)                                                        | 管理你的浏览器标签页                    | -       | -          |
| [Webpack_extract](https://github.com/xz-zone/Webpack_extract)                                                                                     | 一键收集、分析js                     | 323     | 2026-06-11 |
| [AntiDebug_Breaker](https://github.com/0xsdeo/AntiDebug_Breaker)                                                                                  | js逆向插件                        | 2104    | 2026-06-16 |
### 内网渗透
#### 内网信息收集
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [HackBrowserData](https://github.com/moonD4rk/HackBrowserData) | 提取和解密浏览器数据，支持多种数据类型，可在各种操作系统（macOS、Windows、Linux）上运行。 | 14426   | 2026-08-07 |
| [e0e1-config](https://github.com/eeeeeeeeee-code/e0e1-config)  | 收集浏览器、数据库连接工具等敏感信息的后渗透工具                              | 601     | 2026-03-01 |
| [MX1014](https://github.com/L-codes/MX1014)                    | 大小仅2M左右，适合红队在内网进行快速端口扫描                               | 174     | 2026-08-11 |
#### C2
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [sliver](https://github.com/BishopFox/sliver)        | 可跨平台运行，支持linux后门生成的C2         | 11686   | 2026-08-16 |
| [Viper](https://github.com/FunnyWolf/Viper)          | 基于人工智能的对抗模拟和红队演练平台            | 5260    | 2026-05-31 |
| [Supershell](https://github.com/tdragon6/Supershell) | Supershell是一个通过WEB服务访问的C2远控平台 | 1810    | 2026-04-03 |
| [XiebroC2](https://github.com/INotGreen/XiebroC2)    | 神似Cobalt Strike的C2客户端、功能多样且强大 | 1391    | 2025-02-28 |
| [Wyrm](https://github.com/0xflux/Wyrm)               | 红队后渗透框架                       | 511     | 2026-03-15 |
| [conquest](https://github.com/jakobfriedl/conquest)  | 基于Nim语言开发的高度可定制的C2框架          | 418     | 2026-08-12 |
#### 权限提升
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [RedSun](https://github.com/Nightmare-Eclipse/RedSun)     | 利用windows defender进行提权    | 2126    | 2026-04-15 |
| [Exploit-Street](https://github.com/MzHmO/Exploit-Street) | 一个2023-2025的windows提权漏洞合集 | 962     | 2026-08-07 |
| [dirtyfrag](https://github.com/V4bel/dirtyfrag)           | 2026年5月出现的linux提权0day     | 4982    | 2026-05-10 |
### 基础设施
#### 代理池
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [proxy_pool](https://github.com/jhao104/proxy_pool)                                | ProxyPool 爬虫代理IP池          | 23601   | 2026-06-15 |
| [Deadpool](https://github.com/thinkoaa/Deadpool)                                   | Go编写的代理池轮询工具               | 713     | 2026-05-06 |
| [mubeng](https://github.com/mubeng/mubeng)                                         | 一款速度极快、使用便捷的代理服务器检测和IP轮换工具 | 2423    | 2025-10-08 |
| [ProxyPool](https://github.com/XiaomingX/proxy-pool)                               | 帮助用户自动维护高质量的代理池            | 134     | 2026-03-08 |
| [camoufox](https://github.com/daijro/camoufox)                                     | 反检测浏览器                     | 11152   | 2026-08-12 |
| [f8x](https://github.com/ffffffff0x/f8x)                                           | 红蓝队环境自动化部署工具               | 2155    | 2026-07-25 |
| [redc](https://github.com/wgpsec/redc)                                             | 集成了AI的红队基础设施部署GUI工具        | 187     | 2026-08-10 |
| [penetration-suite-toolkit](https://github.com/makoto56/penetration-suite-toolkit) | 包含常见渗透测试工具环境的windows虚拟机    | 2967    | 2025-06-11 |
| [copy-cert](https://github.com/virusdefender/copy-cert)                            | 通过生成ssl证书伪造c2流量            | 350     | 2024-10-03 |
| [ТОСГОНЫ机场](https://www.mouu.one/#/login)                                          |                            |         |            |
| [一元机场](https://xn--4gq62f52gdss.com/#/login)                                       |                            |         |            |
| [赔钱机场](https://pqjc.site/order)                                                    |                            |         |            |
### 靶场
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [vulntarget](https://github.com/crow821/vulntarget)       | 贴切实战攻防、应急的靶场    | 967     | 2026-04-02 |
| [vulhub](https://github.com/vulhub/vulhub)                | 各类nday复现环境      | 21128   | 2026-07-22 |
| [FastJsonParty](https://github.com/lemono0/FastJsonParty) | fastjson全版本漏洞环境 | 1245    | 2024-07-12 |
### 面试题
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [Sec-Interview](https://github.com/duckpigdog/Sec-Interview/) | 涵盖护网、红队、逆向、密码学、二进制、AI、区块链的面试题 | 795     | 2026-03-11 |
## 🤖 AI时代足够好用的资源项目
### 学习资料
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [dive-into-llms](https://github.com/Lordog/dive-into-llms)                   | 上海交大《动手学大模型Dive into LLMs》系列编程实践教程 | 49439   | 2025-10-10 |
| [self-llm](https://github.com/datawhalechina/self-llm)                       | 教会你如何正确使用开源大模型                     | 31725   | 2026-07-30 |
| [happy-llm](https://github.com/datawhalechina/happy-llm)                     | 从核心原理搞懂大模型并构建一个大模型                 | 32993   | 2026-08-08 |
| [llm-universe](https://github.com/datawhalechina/llm-universe)               | 大模型应用开发项目，教会你基于大模型开发上层应用           | 13791   | 2026-07-28 |
| [hello-agents](https://github.com/datawhalechina/hello-agents)               | 从零开始的智能体原理与实践教程                    | 73212   | 2026-08-14 |
| [learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)        | 通过claude code的源码学习AI工具的开发          | 74384   | 2026-08-16 |
| [claude-code-book](https://github.com/lintsinghua/claude-code-book)          | 当所有人都在教你怎么用AI Agent——这本书带你拆开它      | 4103    | 2026-06-19 |
| [agentic-design-patterns](https://github.com/xindoo/agentic-design-patterns) | 谷歌出品智能体开发教程                        | 7671    | 2026-07-22 |
### 编码助手&智能体
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [Claude Code](https://github.com/anthropics/claude-code)           | 最好用、最受欢迎的AI编码助手                   | 141659  | 2026-08-14 |
| [Codex](https://github.com/openai/codex)                           | OpenAI推出的编程助手，支持代码生成、解释和调试        | 106274  | 2026-08-17 |
| [Cursor](https://cursor.com/)                                      | 基于VSCode深度定制的AI原生IDE              | -       | -          |
| [OpenCode](https://opencode.ai/)                                   | 完全开源免费的AI编码工具                     | -       | -          |
| [Trae](https://www.trae.cn/)                                       | 字节跳动推出的AI原生集成开发环境                 | -       | -          |
| [Kiro](https://kiro.dev/)                                          | 亚马逊推出的AI IDE                      | -       | -          |
| [Qoder](https://qoder.com/)                                        | 阿里巴巴开发的编程智能体，特色是专家团开发             | -       | -          |
| [qwen-code](https://github.com/QwenLM/qwen-code)                   | 阿里巴巴推出的基于Qwen3-Coder的命令行编程智能体     | 27078   | 2026-08-17 |
| [codebuddy](https://www.codebuddy.cn/ide/)                         | 腾讯旗下的AI-IDE                       | -       | -          |
| [kimi-code](https://github.com/MoonshotAI/kimi-cli)                | kimi推出的命令行通用智能体工具                 | 11193   | 2026-08-03 |
| [DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | 国内开发者开发的ds编程工具                    | 34646   | 2026-08-16 |
| [CodeWhale(deepseek-tui)](https://github.com/Hmbown/CodeWhale)     | 专为deepseek打造的AI编码助手               | 40822   | 2026-08-17 |
| [Lingma](https://lingma.aliyun.com/)                               | 阿里云推出的免费的图形化编程智能体                 | -       | -          |
| [cc-haha](https://github.com/NanmiCoder/cc-haha)                   | 基于cc泄露源码打造的本地可运行的claude-claude客户端 | 14137   | 2026-08-14 |
| [claude-code-ccb](https://github.com/claude-code-best/claude-code) | 高度可自定义的claude-code开源构建版           | 22061   | 2026-08-10 |
| [openclaw](https://github.com/openclaw/openclaw)                   | 你的个人AI助手                          | 386469  | 2026-08-17 |
| [workbuddy](https://copilot.tencent.com/work/)                     | 腾讯出品，AI工作台                        | -       | -          |
### MCP
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [百度搜索开放平台-MCP广场](https://www.mcpworld.com/)                                  | 一个mcp广场              | -       | -          |
| [cve-mcp-server](https://github.com/mukul975/cve-mcp-server)                 | AI驱动的安全情报聚合与风险判断工具   | 1134    | 2026-08-05 |
| [chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 让AI调试浏览器             | 49264   | 2026-08-16 |
| [claude-plugin-wechat](https://github.com/lc2panda/claude-plugin-wechat)     | 微信、飞书无缝对接Claude-Code | 60      | 2026-08-15 |
### skills
#### 安全相关
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [wooyun-legacy](https://github.com/tanweai/wooyun-legacy)                                    | 给AI安全报告加上真实案例背书和数据支撑                   | 1754    | 2026-07-14 |
| [Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | 内置754个安全技能，将人类安全专家的实践经验转化为AI可执行的结构化知识  | 27994   | 2026-08-08 |
| [ctf-skills](https://github.com/ljagiello/ctf-skills)                                        | 一个适用于ctf的skills，包含漏洞利用、逆向、取证分析、情报获取等技能 | 3000    | 2026-07-31 |
| [AboutSecurity](https://github.com/wgpsec/AboutSecurity)                                     | 为AI制定的渗透测试方法论                          | 1664    | 2026-07-19 |
| [hack-skills](https://github.com/yaklang/hack-skills)                                        | yakit官方出品，让AI拥有多项渗透测试技能                | 1771    | 2026-06-16 |
| [reverse-skill](https://github.com/zhaoxuya520/reverse-skill)                                | 逆向/渗透/安全技能路由包                          | 25695   | 2026-08-16 |
| [anthropic-skills](https://github.com/anthropics/skills)                                     | anthropic官方的skill仓库                    | 169755  | 2026-08-13 |
| [superpowers](https://github.com/obra/superpowers)                                           | 提升agent的自主性和规范性，头脑风暴skills             | 272807  | 2026-08-13 |
| [pua](https://github.com/tanweai/pua)                                                        | 一个赋予AI agent高能动性的skills                | 19436   | 2026-07-16 |
### 渗透智能体
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [CyberStrikeAI](https://github.com/Ed1s0nZ/CyberStrikeAI) | 一款AI原生安全测试平台集成100+安全工具                 | 5773    | 2026-08-15 |
| [strix](https://github.com/usestrix/strix)                | 开源AI黑客将发现并修复您应用的漏洞                     | 53381   | 2026-08-14 |
| [pentest-ai](https://github.com/0xSteph/pentest-ai)       | 可以作为mcp接入claude-code，也可以作为独立的agent工具使用 | 1596    | 2026-08-16 |
| [airecon](https://github.com/pikpikcu/airecon)            | 一个借助本地大模型进行类似人工的渗透测试活动的开源智能体           | 956     | 2026-06-20 |
| [pentagi](https://github.com/vxcontrol/pentagi)           | 利用前沿AI技术进行自动化渗透测试，适用于安全专家、研究人员和爱好者     | 21856   | 2026-08-06 |
| [aster](https://github.com/Q16G/aster)                    | 在终端中完成代码审计、渗透测试、主机防护                   | 83      | 2026-07-12 |
### 好用的AI工具
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [claudecodeui](https://github.com/siteboon/claudecodeui) | 提供一个web-ui，更好的管理AI编程工具会话和使用它们    | 13314   | 2026-08-14 |
| [cc-switch](https://github.com/farion1231/cc-switch)     | 配置claude-code、会话、mcp管理           | 127602  | 2026-08-16 |
| [rtk](https://github.com/rtk-ai/rtk)                     | 让你的AI节省60%-90%的token             | 76297   | 2026-08-16 |
| [claude-hud](https://github.com/jarrodwatts/claude-hud)  | 实时查看cc的上下文、工具调用、待办事项等状态的插件       | 27426   | 2026-08-15 |
| [clawgod](https://github.com/0Chencc/clawgod)            | 一个claude code补丁，解锁了禁止网络安全相关测试的限制 | 1893    | 2026-08-16 |
## 信息获取
| 仓库名 | 描述 | Stars | 最近更新 |
|--------|------|-------|----------|
| [公众号](https://github.com/DropsOfZut/awesome-security-weixin-official-accounts) | 网络安全类公众号推荐            | 2260    | 2026-08-16 |
| [来福电台](https://laifufm.com/)                                                   | 在每天的早咖啡时间根据你的喜好定制推送内容 | -       | -          |
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
