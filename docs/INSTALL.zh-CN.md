# 中文安装指南

[返回首页](../README.md) · [English](INSTALL.en.md)

## 用 GPT 导入

下载快速安装包，把 ZIP 和“请安装并选用附件中的雪伞桌宠”这句话交给能够读取文件、且具有 Pets 工具的会话。完整工具流程写在 [INSTALL_FOR_GPT.md](../INSTALL_FOR_GPT.md)。

安装使用成品 `assets/xuesan.png`，不会重新绘制角色。只有创建和选用结果得到确认，才算安装成功。

## 桌面应用导入

解压后打开 `install.html`，点击安装按钮；Windows 可运行 `install.cmd`。导入入口采用官方的 `codex://pets/install` 协议，图片来自本仓库的固定 HTTPS 地址，格式参数为 v2。应用会显示自己的安装流程；安装后在 Pets 设置里选择它。

命令行可先查看将打开的地址：

```powershell
powershell -NoProfile -File .\scripts\install.ps1 -PrintOnly
```

桌面导入与 Work 中的账户宠物可能属于不同存储范围；在实际使用的界面中选用对应的宠物。

## 网页手动上传

使用九行动作版 `assets/xuesan-v1.png`。它由完整素材的前九行直接导出，没有重新生成动作。完整 v2 则保留额外的十六方向视线。

普通聊天若没有宠物工具，无法自动完成账户设置；可使用页面中的手动上传功能。

## 排查

| 情况 | 处理 |
| --- | --- |
| 点击安装后没有反应 | 确认桌面应用和宠物导入功能可用，再在应用内打开 Pets 设置 |
| GPT 表示没有 Pets 工具 | 使用桌面入口或网页手动上传 |
| 网页提示尺寸不支持 | 上传 `xuesan-v1.png`，不是完整 v2 PNG |
| 下载后只看到一张大图 | 那是动画表；不要裁掉透明部分或转成 JPEG |
| 已有同名宠物 | 检查是否是此成品，避免仅凭名称重复导入 |

来源：[官方 Pets 说明](https://learn.chatgpt.com/docs/pets)、[桌面安装协议](https://learn.chatgpt.com/docs/app/commands)。核对日期：2026-10-12。
