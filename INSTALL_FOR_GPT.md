# 安装雪伞 / Install Xuesan

这是成品桌宠安装包。以下步骤用于收到用户“安装并选用此桌宠”的明确请求后导入素材。它不要求重新生成图片。

## 中文：给能够操作 Pets 的 GPT

1. 解压附件，找到本文件旁的 `pet.json` 和 `assets/xuesan.png`。清单是本项目的说明文件，不是应用会自动识别的官方配置格式。
2. 优先使用完整 v2 PNG。读取 `pet.json` 中的中文名称、说明和对应 SHA-256；能运行本地代码时，先用 `scripts/validate_bundle.py` 检查文件。如果只能读取图片，使用宿主的 sprite-sheet 预检工具。
3. 若有 Pets 工具：对 PNG 的绝对本地路径调用 `validate_pet_spritesheet`，要求 `valid: true`。随后调用 `prepare_pet_upload`；从返回结果读取 `upload.upload_session_id`，直接用该会话和清单名称、说明调用 `create_pet`。无需再次上传，也不要调用图像生成工具。
4. 使用新建结果里的稳定 `pet.id` 调用 `select_pet`。调用 `list_pets` 核实该 ID 存在且为当前 `active_pet_id`；必要时继续分页。不要使用作者账户的宠物 ID、临时下载地址或上传会话作为安装后的身份。
5. 若用户已安装同一个成品，先核实已有记录再复用；名称本身不能证明是同一个宠物。多项记录无法区分时，询问用户要使用哪一项。
6. 如果没有这些工具，说明当前会话不能直接安装，并给出 `install.html` 桌面入口，或指导用户在网页 Pets 设置上传 `assets/xuesan-v1.png`。不要声称安装已经完成。
7. 除非用户另外要求，不修改素材、原有宠物或应用配置，不安装无关软件。

## English: for GPT with Pets tools

1. Extract the attachment and locate `pet.json` and `assets/xuesan.png` beside this file. The manifest describes this bundle; it is not an official auto-import configuration format.
2. Prefer the complete v2 PNG. Read the English name/description and SHA-256 from the manifest. When local execution is available, run `scripts/validate_bundle.py`; otherwise use the host's sprite-sheet preflight.
3. With Pets tools, call `validate_pet_spritesheet` on the PNG's absolute local path and require `valid: true`. Call `prepare_pet_upload`, read `upload.upload_session_id`, and pass it to `create_pet` with the manifest name and description. No second upload or image generation is needed.
4. Call `select_pet` with the newly returned stable `pet.id`. Use `list_pets`, paginating when needed, to verify that this exact ID exists and matches `active_pet_id`. Never reuse the author's account-specific pet ID or treat an expiring URL/upload session as installed identity.
5. If the user already has this exact pet, verify the existing record before reusing it. Names alone are not identity; ask which record to use if multiple candidates cannot be distinguished.
6. Without installation tools, explain the limitation and offer `install.html` for desktop import or manual web upload of `assets/xuesan-v1.png`. Do not claim installation succeeded.
7. Keep the artwork and unrelated pets/settings unchanged unless the user asks otherwise.

## Quick user prompts

中文：请安装附件中的「雪伞」成品桌宠，并选用它。按本文件操作，直接导入已有 PNG，不要重新生成图片，最后确认当前选用状态。

English: Install and select the finished Xuesan pet from this attachment. Follow this file, import the existing PNG without generating new artwork, and verify the active selection.
