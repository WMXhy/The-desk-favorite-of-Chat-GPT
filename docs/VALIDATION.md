# Export validation / 导出校验

Checked on **2026-10-12**.

| Asset | Dimensions | Populated cells | Host preflight |
| --- | --- | --- | --- |
| `assets/xuesan.png` | 1536 × 2288 | 73 | valid: true |
| `assets/xuesan-v1.png` | 1536 × 1872 | 57 | valid: true |

- Both exports pass the Pets sprite-sheet preflight. Actual responses are saved in [server-preflight.json](server-preflight.json).
- Local checking verifies SHA-256, encoded size, PNG/RGBA format, transparent background, required/unused cells, and exact preservation of the v2 action pixels in v1.
- All nine action GIFs have the required frame counts. The look GIF has 16 frames; the idle/jump transition has 17. Metadata is in [preview-metadata.json](preview-metadata.json).
- The MP4 is H.264 and was decoded successfully.
- Windows launcher links were inspected with `-PrintOnly` for both formats. The launcher follows the documented desktop import protocol.
- This export does not change the author's existing pet. Recipient installation still runs through the recipient's own app or Pets tools.

## Optional local check

Python and Pillow are needed only for this diagnostic; they are not required to open the desktop installer.

```sh
python -m pip install -r requirements.txt
python scripts/validate_bundle.py
```

中文：两种 PNG 均已通过实际服务端预检。本地脚本检查哈希、透明背景、网格和所需帧，并确认兼容版逐像素保留原有九组动作。预览由导出的 PNG 直接解码生成，未重新绘图。
