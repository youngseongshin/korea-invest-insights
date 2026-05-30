---
title: "Bản đồ định giá hạ tầng AI: vì sao Samsung Electronics rẻ còn Samsung Electro-Mechanics đắt"
date: 2026-05-31T09:00:00+09:00
description: "GPU, HBM, CPU, MLCC và FC-BGA cùng nằm trong chu kỳ hạ tầng AI, nhưng không xứng đáng cùng một mức định giá. Bài viết tách bạch quyền định giá, hợp đồng dài hạn, lock-in khách hàng, gánh nặng capex và nghi ngờ lợi nhuận đỉnh."
categories: ["Market-Outlook"]
tags:
  - "hạ tầng AI"
  - "định giá"
  - "HBM"
  - "GPU"
  - "MLCC"
  - "FC-BGA"
  - "Samsung Electronics"
  - "Samsung Electro-Mechanics"
  - "SK hynix"
  - "Nvidia"
  - "bán dẫn Hàn Quốc"
slug: ai-infrastructure-multiple-map-gpu-hbm-mlcc-fcbga-samsung-2026-05-31
valley_cashtags:
  - 삼성전자
  - 삼성전기
  - SK하이닉스
draft: false
---

> Bối cảnh
> Bài này nối hai luận điểm trước: [Samsung Electronics và siêu chu kỳ bộ nhớ](/vi/post/samsung-electronics-stock-bonus-supercycle-buyback-2026-05-27/) và [Samsung Electro-Mechanics so với Murata / Ibiden](/vi/post/samsung-electro-mechanics-market-cap-murata-ibiden-premium-2026-05-28/). Câu hỏi là: cùng một chu kỳ AI, vì sao mỗi tầng lại được trả một bội số khác nhau?

## TL;DR

Thị trường không trả cùng một multiple cho mọi công ty "có liên quan đến AI". Multiple phụ thuộc vào <strong>độ bền lợi nhuận, quyền định giá, lock-in khách hàng, rủi ro mở rộng công suất và nghi ngờ lợi nhuận đỉnh</strong>.

Vùng nguy hiểm hiện nay là định giá MLCC / FC-BGA như thể đó là độc quyền cấu trúc giống GPU hoặc HBM. Đây là nút thắt thật, nhưng không phải nút thắt nào cũng có multiple kiểu NVIDIA.

Ý tưởng relative value mạnh nhất là <strong>Samsung Electronics</strong>. Công ty có HBM catch-up, chu kỳ giá bộ nhớ và tùy chọn foundry, nhưng snapshot dữ liệu công khai 2026-05-29/30 trong đầu vào cho thấy forward P/E khoảng 7.8x và P/B khoảng 4.4x. Samsung Electro-Mechanics có câu chuyện đúng, nhưng giá đã đi trước. ([Yahoo Finance][1])

## 1. Công thức

```text
Premium multiple
= quyền định giá × độ bền nhu cầu × lock-in khách hàng × chuyển đổi FCF

Discount multiple
= capex mở rộng × rủi ro dư cung × nghi ngờ lợi nhuận đỉnh × tập trung khách hàng
```

| Tầng | Yếu tố nâng multiple | Yếu tố giới hạn | Câu hỏi chính |
|---|---|---|---|
| GPU / platform | CUDA, hệ thống rack-scale, phần mềm, asset-light | ASIC tùy biến, kiểm soát xuất khẩu, sức ép hyperscaler | Khách hàng mua thời gian hay mua chip? |
| HBM | HBM4, sold-out, LTA, nhiều HBM hơn mỗi accelerator | chu kỳ bộ nhớ, capex, đa dạng hóa nhà cung cấp | Lợi nhuận theo chu kỳ hay franchise có hợp đồng? |
| CPU | server AI tăng, orchestration | dễ thay thế bằng ARM / CPU nội bộ | nút thắt chính hay phần phụ trợ? |
| FC-BGA | substrate lớn, nhiều lớp, chứng nhận khó | capex-heavy, khấu hao, ký ức dư cung ABF | capex có được LTA / prepayment bảo đảm không? |
| MLCC / Si-Cap | power integrity, linh kiện độ tin cậy cao | chu kỳ MLCC phổ thông, cạnh tranh | chặn giao hàng hay chỉ là passive component? |

## 2. Đọc từng tầng

NVIDIA nhận multiple cao vì họ không chỉ bán GPU. Họ kiểm soát GPU, networking, software, reference architecture và hệ thống AI factory. Q1 FY2027 của NVIDIA đạt doanh thu 81.6 tỷ USD, Data Center 75.2 tỷ USD và guidance Q2 91.0 tỷ USD. ([NVIDIA Investor Relations][2])

HBM có lợi nhuận rất nóng nhưng vẫn bị thị trường coi là bộ nhớ chu kỳ. Nếu LTA trở thành hợp đồng giá / khối lượng / prepayment rõ ràng, HBM có thể được nhìn như high-value memory franchise thay vì DRAM commodity.

CPU là cần thiết nhưng không phải nút thắt chính. AMD tăng trưởng mạnh ở Data Center, nhưng multiple cao đòi hỏi cả EPYC và Instinct cùng thành công. Intel cần bằng chứng execution.

FC-BGA và MLCC là chủ đề đúng. Samsung Electro-Mechanics ghi nhận Q1 2026 tăng nhờ MLCC cho server AI và FC-BGA cho accelerator / server CPU, đồng thời ký hợp đồng silicon capacitor khoảng 1.5 nghìn tỷ won cho 2027-2028. ([Samsung Electro-Mechanics][7], [Samsung Electro-Mechanics][8])

Nhưng giá rất quan trọng. ResearchAndMarkets dự báo thị trường FC-BGA toàn cầu tăng từ 2.46 tỷ USD năm 2026 lên 3.74 tỷ USD năm 2032, CAGR 7.1%. Tăng trưởng này không dễ biện minh cho P/E 100x. ([Research and Markets][9])

## 3. Samsung Electronics vs Samsung Electro-Mechanics

Samsung Electronics là lựa chọn cân bằng hơn: HBM4E, DDR5, SOCAMM2, eSSD / KV-cache và Samsung Foundry tạo ra exposure rộng hơn với AI inference memory hierarchy.

Samsung Electro-Mechanics là công ty hiếm có MLCC + FC-BGA + Si-Cap. Điều đó có thể biến công ty thành nhà cung cấp power-integrity cho package AI. Nhưng giá hiện tại đòi hỏi dữ liệu: khách hàng Si-Cap mới, biên lợi nhuận, ASP MLCC AI, utilization FC-BGA và LTA.

## 4. Kết luận đầu tư

| Tên | Quan điểm | Lý do |
|---|---|---|
| Samsung Electronics | Under / ứng viên mua | multiple thấp so với HBM catch-up và memory option |
| NVIDIA | Fair đến tương đối under | tăng trưởng và margin vẫn hỗ trợ |
| SK hynix | under về cơ bản, chờ timing | HBM tốt nhưng P/B và đà tăng lớn |
| Samsung Electro-Mechanics | over / không đuổi giá | thesis đúng nhưng giá đã phản ánh nhiều |
| Murata / Ibiden | over | nút thắt thật nhưng định giá như độc quyền |

Sai lầm lớn nhất là gán multiple nền tảng cho mọi nhà cung cấp chỉ vì họ chạm vào chuỗi cung ứng NVIDIA.

[1]: https://finance.yahoo.com/quote/005930.KS/key-statistics/ "Samsung Electronics valuation"
[2]: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-First-Quarter-Fiscal-2027/default.aspx "NVIDIA FY2027 Q1 results"
[7]: https://m.samsungsem.com/global/newsroom/news/view.do?id=10266 "Samsung Electro-Mechanics Q1 2026"
[8]: https://samsungsem.com/global/newsroom/news/view.do?id=10310 "Samsung Electro-Mechanics silicon capacitor contract"
[9]: https://www.researchandmarkets.com/reports/6128754/fc-bga-market-global-forecast "FC-BGA market forecast"
