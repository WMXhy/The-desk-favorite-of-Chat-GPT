# Xuesan · 雪伞

**English** · [简体中文](README.md)

An anime companion with black-and-red hair, white horns, an ice-blue kimono, and a red parasol. Bring the finished Xuesan pet into ChatGPT without generating new artwork.

| Idle | Wave | Jump |
| :---: | :---: | :---: |
| ![Idle](previews/idle.gif) | ![Wave](previews/waving.gif) | ![Jump](previews/jumping.gif) |

**[Download the quick-install ZIP](https://raw.githubusercontent.com/WMXhy/The-desk-favorite-of-Chat-GPT/main/downloads/Xuesan-Quick-Install.zip)** · [Animations](previews/) · [Installation guide](docs/INSTALL.en.md)

## Download, then give it to GPT

1. Download **Xuesan-Quick-Install.zip**.
2. Attach it to a ChatGPT Work / Codex session with **Pets tools** and attachment access.
3. Send this prompt:

> Install the finished Xuesan pet in the attached ZIP and select it. Follow INSTALL_FOR_GPT.md and use the existing PNG sprite sheet directly. Do not generate new artwork. Verify that Xuesan is the active pet.

The package contains finished assets, names, descriptions, checksums, and bilingual import instructions. GPT can import the existing sheet instead of drawing a new pet. See [INSTALL_FOR_GPT.md](INSTALL_FOR_GPT.md).

If the session has no pet-installation tools, use desktop import or manual upload below. An ordinary chat cannot necessarily change your account settings.

## Import into the desktop app

Extract the ZIP, open **install.html**, and click **安装雪伞 / Install Xuesan**. On Windows, you can also run **install.cmd**. Complete the app's import flow and select the pet in its Pets settings.

A compatible ChatGPT / Codex desktop app is required. The launcher collects no login information and does not edit app configuration files directly. [Official desktop install-link documentation](https://learn.chatgpt.com/docs/app/commands)

## Manual web upload

Open **Settings → Personalization → Pet → Select pet → Upload pet**, upload **assets/xuesan-v1.png**, then select it. Use the nine-row file for manual web upload. Prefer **assets/xuesan.png** for v2-capable Pets tools and desktop import. [Official Pets documentation](https://learn.chatgpt.com/docs/pets)

## Files

| File | Purpose |
| --- | --- |
| `assets/xuesan.png` | Full v2: 1536 × 2288, nine actions and sixteen look directions |
| `assets/xuesan-v1.png` | v1 compatibility export: 1536 × 1872, the same nine actions |
| `INSTALL_FOR_GPT.md` | Bilingual instructions for a tool-enabled GPT session |
| `pet.json` | This project's names, descriptions, formats, asset paths, and SHA-256 hashes |
| `install.html` / `install.cmd` | Desktop import launchers |
| `previews/` | Action GIFs, look loop, video, and inspection sheets |
| `scripts/validate_bundle.py` | Optional local asset integrity check |

Actions: idle, run right, run left, wave, jump, failure, waiting for input, focused work, and review. See [FORMAT.md](docs/FORMAT.md) and [VALIDATION.md](docs/VALIDATION.md).

## FAQ

- **Will installation redraw the character?** No. These are finished assets.
- **Why two PNGs?** v2 includes look directions; v1 preserves the same action pixels for compatibility.
- **Is this a standalone desktop-pet program?** No. It needs the host application's Pets feature.
- **Does it work with every GPT account?** Availability depends on the account, workspace, and app version.
- **Can I download the repository instead?** Yes: Code → Download ZIP or git clone. The quick package simply omits unrelated files.

You may download the finished pet for personal use. Scripts and documentation use the MIT license. See [ASSET_USAGE.md](ASSET_USAGE.md) and [CREDITS.md](docs/CREDITS.md) for artwork notes.
