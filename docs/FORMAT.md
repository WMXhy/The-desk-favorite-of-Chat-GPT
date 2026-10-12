# Sprite formats / 动画格式

The asset files are transparent PNGs. The project manifest `pet.json` is a convenience description for humans and assistants, not an official app configuration file.

| Format | Dimensions | Grid | Populated cells |
| --- | --- | --- | --- |
| v2 / full | 1536 × 2288 | 8 × 11 | 73 |
| v1 / compatibility | 1536 × 1872 | 8 × 9 | 57 |

Cell size: **192 × 208**. Unused cells are fully transparent. Both files are below 20 MiB.

| Zero-based row | State | Frames |
| --- | --- | --- |
| 0 | idle / 待机 | 6 |
| 1 | running-right / 向右跑 | 8 |
| 2 | running-left / 向左跑 | 8 |
| 3 | waving / 挥手 | 4 |
| 4 | jumping / 跳跃 | 5 |
| 5 | failed / 受挫 | 8 |
| 6 | waiting / 等待输入 | 6 |
| 7 | running / 思考工作 | 6 |
| 8 | review / 检查 | 6 |
| 9 | look 000–157.5° | 8 |
| 10 | look 180–337.5° | 8 |

Look order is clockwise in screen coordinates: 000° up, 090° right, 180° down, 270° left, in 22.5° increments. v1 omits the last two rows only.

中文：兼容版仅导出前九行；没有镜像、重新绘图或逐帧缩放。名称和介绍可通过安装会话选用中文或英文，图片内容相同。
