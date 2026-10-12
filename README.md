# 雪伞 · Xuesan

[English](README.en.md) · **简体中文**

黑红长发、白色双角、冰蓝和服和红色纸伞。把已经制作完成的「雪伞」带进 ChatGPT，陪你工作。

| 待机 | 挥手 | 跳跃 |
| :---: | :---: | :---: |
| ![待机](previews/idle.gif) | ![挥手](previews/waving.gif) | ![跳跃](previews/jumping.gif) |

**[下载快速安装包](https://raw.githubusercontent.com/WMXhy/The-desk-favorite-of-Chat-GPT/main/downloads/Xuesan-Quick-Install.zip)** · [查看所有动画](previews/) · [安装说明](docs/INSTALL.zh-CN.md)

## 最快的方式：下载后交给 GPT

1. 下载上面的 **Xuesan-Quick-Install.zip**。
2. 把 ZIP 交给支持 **Pets 工具**、能够读取附件的 ChatGPT Work / Codex 会话。
3. 发送下面这句话：

> 请安装附件中的「雪伞」成品桌宠，并选用它。按照 INSTALL_FOR_GPT.md 操作，直接使用已经完成的 PNG 动画表，不要重新生成图片。安装后确认它是当前选用的宠物。

包里已放好图片、名称、介绍、文件校验值和中英文安装指引。GPT 只需导入现有素材，不需要重新绘图。详细操作见 [INSTALL_FOR_GPT.md](INSTALL_FOR_GPT.md)。

如果该会话没有安装宠物的工具，请使用下面的桌面导入入口或手动上传方式；普通聊天会话无法保证替你完成账户配置。

## 直接导入桌面版

解压安装包，双击 **install.html**，再点击「安装雪伞 / Install Xuesan」。Windows 也可以双击 **install.cmd**。两者都会打开桌面应用自身的导入流程；按应用提示完成导入，在 Pets 设置中选择它。

需要已安装支持宠物导入的 ChatGPT / Codex 桌面应用。安装页不会收集登录信息，也不会直接修改你的应用配置文件。[桌面安装链接的官方说明](https://learn.chatgpt.com/docs/app/commands)

## 网页手动上传

进入 **Settings → Personalization → Pet → Select pet → Upload pet**，上传 **assets/xuesan-v1.png**，然后选择新宠物。网页手动上传使用九行兼容版；支持 v2 的 Pets 工具和桌面导入优先使用 **assets/xuesan.png**。[Pets 官方说明](https://learn.chatgpt.com/docs/pets)

## 包含什么

| 文件 | 用途 |
| --- | --- |
| `assets/xuesan.png` | 完整 v2：1536 × 2288，九组动作＋十六个视线方向 |
| `assets/xuesan-v1.png` | v1 兼容版：1536 × 1872，保留同一套九组动作 |
| `INSTALL_FOR_GPT.md` | 给 GPT 的中英文导入步骤 |
| `pet.json` | 本项目的名称、说明、版本、文件路径与 SHA-256 清单 |
| `install.html` / `install.cmd` | 桌面应用的导入入口 |
| `previews/` | 各动作 GIF、视线循环、动作视频和检查图 |
| `scripts/validate_bundle.py` | 可选的本地素材完整性检查 |

九组动作：待机、向右跑、向左跑、挥手、跳跃、受挫、等待输入、思考工作、检查。完整格式见 [FORMAT.md](docs/FORMAT.md)，导出校验见 [VALIDATION.md](docs/VALIDATION.md)。

## 常见问题

- **安装会重新生成角色吗？** 不需要。本仓库提供成品素材。
- **为什么有两张 PNG？** v2 带完整视线动画；v1 是保留相同动作像素的兼容导出版。
- **这是独立桌宠程序吗？** 它是 ChatGPT 的宠物素材包，运行需要相应应用的 Pets 功能。
- **支持所有 GPT 账户吗？** 功能与工具可用性取决于账户、工作区和应用版本；不提供所有账户通用的一键安装保证。
- **下载整仓库可以吗？** 可以使用 GitHub 的 Code → Download ZIP，或克隆仓库；快速包只是省去无关文件。

本仓库允许下载成品作为个人桌宠使用。脚本与文档使用 MIT 许可；美术说明见 [ASSET_USAGE.md](ASSET_USAGE.md)，来源说明见 [CREDITS.md](docs/CREDITS.md)。
