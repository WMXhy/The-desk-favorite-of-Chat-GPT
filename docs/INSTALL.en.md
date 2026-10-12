# Installation guide

[Home](../README.en.md) · [简体中文](INSTALL.zh-CN.md)

## Import with GPT

Attach the quick-install ZIP to a session that can read files and use Pets tools, and ask it to install and select Xuesan. [INSTALL_FOR_GPT.md](../INSTALL_FOR_GPT.md) provides the tool sequence.

The session imports the finished `assets/xuesan.png`; no artwork regeneration is required. Treat installation as successful only after creation and active selection are confirmed.

## Desktop import

Extract the bundle, open `install.html`, and click Install. Windows users can run `install.cmd`. The launcher uses the documented `codex://pets/install` protocol, a fixed HTTPS image URL from this repository, and sprite format v2. Complete the app's own import flow, then select the pet in Pets settings.

To inspect the link without opening the app:

```powershell
powershell -NoProfile -File .\scripts\install.ps1 -PrintOnly
```

Desktop and Work account pets may use separate storage. Select the pet in the interface you intend to use.

## Manual web upload

Use `assets/xuesan-v1.png`. It is the original sheet's first nine rows, preserving the action pixels. The full v2 file additionally includes sixteen look directions.

If an ordinary chat lacks pet tools, use the manual upload controls rather than expecting automatic account changes.

## Troubleshooting

| Situation | Action |
| --- | --- |
| Install button does nothing | Check app/feature availability and open the app's Pets settings |
| GPT has no Pets tools | Use desktop import or manual web upload |
| Web upload rejects dimensions | Upload `xuesan-v1.png`, not the complete v2 file |
| Download looks like one large image | It is a sprite sheet; keep transparency and PNG format |
| A pet with the same name exists | Verify the exact asset instead of blindly creating duplicates |

Sources: [Pets documentation](https://learn.chatgpt.com/docs/pets), [desktop import protocol](https://learn.chatgpt.com/docs/app/commands). Checked: 2026-10-12.
