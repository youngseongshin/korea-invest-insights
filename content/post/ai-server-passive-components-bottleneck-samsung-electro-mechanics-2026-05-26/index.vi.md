---
title: "Nút thắt linh kiện thụ động trong máy chủ AI: vì sao các bộ phận ổn định nguồn trở nên quan trọng"
date: 2026-05-26
description: "Nút thắt của máy chủ AI không chỉ là GPU. Đó còn là MLCC, tụ silicon, cuộn cảm và bộ lọc có thông số cao hơn để ổn định nguồn cho hệ GPU/HBM. Bài viết giải thích tác động với Samsung Electro-Mechanics."
categories: ["Stock-Analysis"]
tags: ["Samsung Electro-Mechanics", "009150", "AI Server", "MLCC", "Silicon Capacitor", "FC-BGA", "Power Integrity", "HBM", "GPU"]
slug: ai-server-passive-components-bottleneck-samsung-electro-mechanics-2026-05-26
valley_body_mode: teaser
valley_cashtags: ["삼성전기"]
valley_cashtag_exclude: ["삼성전자", "SK하이닉스"]
---

> Bài tiếp theo trong chuỗi Samsung Electro-Mechanics. Xem thêm [SEMCO đạt vốn hóa 100 nghìn tỷ won](/vi/post/samsung-electro-mechanics-100tn-murata-hyundai-market-cap-2026-05-26/), [hợp đồng tụ silicon](/vi/post/samsung-electro-mechanics-silicon-capacitor-1p5tn-2026-05-21/) và [MLCC so với tụ silicon](/vi/post/mlcc-silicon-capacitor-ai-package-power-integrity-2026-05-22/).

## TL;DR

- Nút thắt linh kiện thụ động trong máy chủ AI không phải là thiếu GPU, mà là nhu cầu ổn định nguồn điện cho GPU/HBM ngày càng khắt khe.
- Rack NVIDIA DGX GB200 tiêu thụ khoảng <strong>120kW</strong>; Lenovo GB300 NVL72 được mô tả ở mức <strong>135kW TDP</strong> và tối đa <strong>155kW peak</strong> mỗi rack. ([NVIDIA][1], [Lenovo][2])
- MLCC, tụ silicon và cuộn cảm giống như bộ giảm chấn điện của máy chủ AI.
- Cơ hội nằm ở linh kiện AI server hiệu năng cao: điện dung lớn, ESR/ESL thấp, nhiễu thấp, chiều cao thấp.
- Samsung Electro-Mechanics đáng chú ý vì kết hợp <strong>MLCC + FC-BGA + tụ silicon</strong>.

## Giải thích đơn giản

Nếu máy chủ AI là một động cơ đua, GPU là động cơ, HBM là bình nhiên liệu tốc độ cao, substrate là đường chạy, còn MLCC/tụ silicon giữ cho áp lực nguồn không rung lắc.

TDK mô tả chuỗi nguồn trong data center là <strong>UPS → PSU → IBC → VRM → điện áp CPU/GPU</strong>, mỗi tầng đều cần hiệu suất, ripple thấp, chịu nhiệt và độ tin cậy dài hạn. ([TDK][3])

Samsung Electro-Mechanics cho biết GPU/CPU hoạt động dưới 1V và dòng điện có thể thay đổi ngay lập tức hàng chục đến hàng trăm ampere; vì vậy MLCC điện dung cao gần GPU phải đóng vai trò bộ đệm dòng. ([Samsung Electro-Mechanics][4])

## MLCC và tụ silicon

| Linh kiện | Vị trí | Vai trò |
|---|---|---|
| MLCC | Trên bo mạch và quanh chip | Ổn định nguồn diện rộng |
| Tụ silicon | Bên trong hoặc sát package GPU/HBM | Giảm dao động nguồn ở khoảng cách cực gần |

Samsung Electro-Mechanics công bố hợp đồng tụ silicon khoảng <strong>1.5 nghìn tỷ won</strong> cho giai đoạn <strong>2027-2028</strong>. Công ty cho biết linh kiện này cải thiện độ ổn định nguồn bên trong package bán dẫn hiệu năng cao cho máy chủ AI. ([Samsung Electro-Mechanics][8])

## Hàm ý đầu tư

Luận điểm không phải “mọi MLCC đều tăng”. Luận điểm là:

```text
Công suất rack tăng
  → dao động dòng tức thời lớn hơn
  → nhu cầu power integrity gần GPU/HBM tăng
  → MLCC cao cấp, FC-BGA và tụ silicon có giá trị hơn
```

Cần theo dõi ASP MLCC cho AI server, doanh thu tụ silicon từ 2027, khách hàng/platform mới, tăng trưởng FC-BGA cho server/network và biên lợi nhuận hoạt động của tập đoàn.

[1]: https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
[2]: https://lenovopress.lenovo.com/lp2357-lenovo-nvidia-gb300-nvl72-rack-scale-ai
[3]: https://product.tdk.com/en/techlibrary/applicationnote/mlcc-solution-for-data-center-psu.html
[4]: https://product.samsungsem.com/product-news/view.do?idx=3622&language=en
[5]: https://developer.nvidia.com/blog/how-new-gb300-nvl72-features-provide-steady-power-for-ai/
[6]: https://www.thelec.net/news/articleView.html?idxno=5588
[7]: https://product.samsungsem.com/product-news/view.do?idx=3742&language=en
[8]: https://m.samsungsem.com/kr/newsroom/news/view.do?id=10309
