---
title: "Đà tăng của ARM — nút thắt AI tiếp theo nằm ở CPU điều phối, kết nối quang và ổn định nguồn"
date: 2026-05-22T21:40:00+09:00
description: "Đà tăng của ARM không chỉ là câu chuyện CPU trở lại. Nó cho thấy nút thắt của hạ tầng AI đang dịch chuyển từ GPU sang CPU điều phối, di chuyển dữ liệu bộ nhớ, kết nối quang, ổn định nguồn, substrate tốc độ cao và test socket. Thesis của ARM đúng, nhưng giá cổ phiếu đã phản ánh khá nhiều kịch bản thành công dài hạn."
categories: ["Market-Outlook"]
tags:
  - "ARM"
  - "Marvell"
  - "NVIDIA"
  - "Samsung Electro-Mechanics"
  - "Samsung Electronics"
  - "SK hynix"
  - "HBM"
  - "AI infrastructure"
slug: arm-ai-cpu-rally-korea-semiconductor-value-chain-2026-05-22
draft: false
---

> Bài liên quan:
> [NVIDIA Q1 FY27 và hạ tầng AI Hàn Quốc](/vi/post/nvidia-q1-fy27-korea-ai-infra-supply-chain-2026-05-21/) / [Hợp đồng silicon capacitor của Samsung Electro-Mechanics](/vi/post/samsung-electro-mechanics-silicon-capacitor-1p5tn-2026-05-21/) / [MLCC và silicon capacitor](/vi/post/mlcc-silicon-capacitor-ai-package-power-integrity-2026-05-22/)

*Đà tăng của ARM không chỉ nói rằng “CPU lại quan trọng”. Nó nói rằng máy chủ AI đang chuyển từ một hộp GPU sang một hệ thống gồm CPU, XPU, HBM, kết nối quang, linh kiện ổn định nguồn, substrate tốc độ cao và hạ tầng kiểm thử. ARM là tín hiệu dễ thấy nhất. Nhưng alpha thực tế có thể nằm ở các nút thắt mà tín hiệu đó chỉ ra.*

## Tóm tắt chính

Đà tăng của ARM là một sự kiện tái phân loại: từ công ty thu phí IP di động sang nền tảng CPU cho trung tâm dữ liệu AI. Khi agent AI chạy liên tục, gọi công cụ, di chuyển dữ liệu và điều phối GPU, ASIC, bộ nhớ, CPU trở thành lớp điều phối của rack AI.

Chất xúc tác bên ngoài là kết quả của NVIDIA. NVIDIA công bố doanh thu Q1 FY27 **81,6 tỷ USD**, doanh thu Data Center **75,2 tỷ USD**, và hướng dẫn Q2 **91,0 tỷ USD ±2%**. Thị trường đọc đây là tăng tốc, không phải đỉnh chu kỳ. ([NVIDIA][1])

Câu chuyện của ARM cũng có cơ sở. FY26 doanh thu **4,92 tỷ USD**, royalty **2,61 tỷ USD**, licensing **2,31 tỷ USD**, EPS non-GAAP **1,77 USD**. Arm AGI CPU được định vị như nền tảng CPU cho trung tâm dữ liệu AI, với Meta là đối tác dẫn dắt; nhu cầu khách hàng FY27-FY28 đã vượt **2 tỷ USD**. ([Arm][2])

Vấn đề là định giá. Research OS local DB cho thấy ARM đóng cửa ngày 21/5/2026 ở **298,23 USD**. So với EPS non-GAAP FY26, P/E khoảng **168,5 lần**. Thesis đúng, nhưng cổ phiếu không rẻ.

Vì vậy, cơ hội tốt hơn có thể nằm ở Marvell, Samsung Electro-Mechanics, SK hynix, Samsung Electronics, substrate tốc độ cao và test socket.

---

## 1. Đà tăng của ARM thực sự nói gì

Gọi đây là “sự trở lại của CPU” là đúng nhưng chưa đủ. Điểm quan trọng hơn: nút thắt đang dịch chuyển.

```text
Thiếu GPU
→ thiếu HBM và đóng gói tiên tiến
→ nút thắt CPU điều phối, di chuyển bộ nhớ, kết nối quang
→ ổn định nguồn trong package, substrate tốc độ cao, kiểm thử
```

Agent AI không phải một yêu cầu web đơn giản. Nó gọi nhiều mô hình, dùng công cụ, đọc tài liệu, truy vấn cơ sở dữ liệu và lưu kết quả trung gian. GPU xử lý tính toán; CPU điều phối thứ tự công việc, bộ nhớ, mạng, bảo mật và vận hành hệ thống.

Do đó CPU trở thành “trạm điều khiển” của rack AI. Đây là lý do thị trường bắt đầu định giá lại ARM.

---

## 2. Arm AGI CPU: từ IP sang nền tảng silicon

ARM đưa **Arm AGI CPU** vào trung tâm câu chuyện. Công ty mô tả đây là sản phẩm silicon cho trung tâm dữ liệu agentic AI, với Meta là đối tác chính. Các hệ thống thương mại có thể được đặt từ ASRock, Lenovo, Quanta và Supermicro. ([Arm][2])

Mô hình cũ:

```text
cấp phép IP
→ khách hàng tự thiết kế và sản xuất chip
→ ARM nhận phí license và royalty
```

Mô hình mới:

```text
IP + subsystem + silicon sản xuất
→ khách hàng triển khai nền tảng Arm nhanh hơn ở quy mô data center
→ ARM kiểm soát nền tảng nhiều hơn
```

Nhưng điều này tạo rủi ro xung đột kênh. Khi ARM tự bán chip, một số khách hàng có thể coi ARM là đối thủ. Vì vậy thông tin Bloomberg về cuộc điều tra FTC đối với cách cấp phép của ARM là rủi ro cần theo dõi. ([Bloomberg][3])

---

## 3. Định giá: câu chuyện đúng, giá khó

Ở **298,23 USD**, với EPS non-GAAP FY26 **1,77 USD**:

```text
P/E non-GAAP FY26 = 298,23 / 1,77 = khoảng 168,5 lần
```

So với doanh thu FY26 **4,92 tỷ USD**, vốn hóa vùng hơn 300 tỷ USD hàm ý P/S trên 60 lần.

Đây không phải mức giá cho lợi nhuận hiện tại. Đây là mức giá đặt cược vào giai đoạn 2030-2031: CPU data center, doanh thu AGI CPU, royalty cao hơn và mở rộng Armv9/Neoverse.

Quan điểm: **không đuổi theo giá hiện tại / chờ**.

---

## 4. Alpha tốt hơn 1: Marvell và nút thắt kết nối

Nếu ARM đại diện cho lớp điều phối CPU, Marvell đại diện cho **custom compute + kết nối quang + switching**.

Marvell báo cáo doanh thu FY26 **8,195 tỷ USD** và EPS non-GAAP **2,84 USD**. Công ty kỳ vọng FY27 tiến gần **11 tỷ USD**, với data center dẫn dắt tăng trưởng và doanh thu interconnect tăng hơn 50%. ([Marvell][4])

Marvell không chỉ là công ty chip mạng. Nó có custom AI silicon, kết nối quang, PCIe/CXL switching và quan hệ NVLink Fusion. Celestial AI bổ sung nền tảng Photonic Fabric; Marvell đặt mục tiêu run-rate 500 triệu USD vào FY28 và 1 tỷ USD vào FY29 nếu đạt mốc. ([Marvell Celestial][5])

Nhưng MRVL cũng đã tăng mạnh. Research OS local DB cho thấy giá đóng cửa ngày 21/5/2026 là **190,69 USD**. Quan điểm: **chờ / mua khi điều chỉnh**.

---

## 5. Alpha tốt hơn 2: Samsung Electro-Mechanics và ổn định nguồn

Ở Hàn Quốc, nút thắt thứ hai rõ nhất là Samsung Electro-Mechanics.

Ngày 20/5/2026, công ty công bố hợp đồng silicon capacitor khoảng **1,5 nghìn tỷ KRW** trong hai năm. Linh kiện này được lắp bên trong package bán dẫn hiệu năng cao như GPU AI và HBM để ổn định nguồn. ([Samsung Electro-Mechanics][6])

Điểm chính không phải “MLCC tăng”. Mà là:

```text
Trước đây:
MLCC + camera module + FC-BGA

Sau đây:
linh kiện ổn định nguồn bên trong package AI
+ FC-BGA
+ MLCC cho AI
```

Silicon capacitor không thay thế toàn bộ MLCC. Nó là linh kiện bổ sung hiệu năng cao ở bên trong hoặc rất gần package AI GPU/HBM. Điều này có thể tái phân loại Samsung Electro-Mechanics thành nhà cung cấp linh kiện ổn định nguồn cho package AI.

---

## 6. Bộ nhớ Hàn Quốc: SK hynix và Samsung Electronics

Đà tăng của ARM cũng tích cực cho bộ nhớ. Nhiều CPU điều phối hơn đồng nghĩa với nhiều bộ nhớ phía CPU hơn, nhiều dữ liệu di chuyển tới HBM hơn, và nhu cầu server DRAM / LPDDR / DDR / CXL cao hơn.

| Công ty | Vai trò | Quan điểm |
|---|---|---|
| SK hynix | người thắng HBM đã được chứng minh | giữ / mua khi điều chỉnh |
| Samsung Electronics | lựa chọn bắt kịp HBM + IDM rộng | theo dõi / mua khi có xác nhận |

Samsung cần bằng chứng: chứng nhận HBM4, sản lượng, biên lợi nhuận và giảm lỗ foundry.

---

## 7. Substrate tốc độ cao và test socket

Khi rack AI dày đặc hơn, substrate và kiểm thử hưởng lợi.

| Lớp | Ứng viên | Cần xác nhận |
|---|---|---|
| PCB tốc độ cao | Isu Petasys, Daeduck, TLB, Korea Circuit, Simmtech | doanh thu AI, số lớp, ASP, OPM |
| Test socket | ISC, LEENO, TSE | khách hàng ASIC/HBM/CXL, mix sản phẩm |
| Package substrate | Samsung Electro-Mechanics, Daeduck, Korea Circuit | FC-BGA utilization, qualification, margin |

Nguyên tắc: **đừng mua chỉ vì có chữ AI; hãy mua khách hàng, đơn hàng và biên lợi nhuận đã được xác nhận.**

---

## Kết luận

ARM là tín hiệu đúng. Máy chủ AI không còn là hộp GPU; chúng là hệ thống gồm CPU, XPU, HBM, kết nối quang, ổn định nguồn, substrate và kiểm thử.

Nhưng đuổi theo ARM sau cú tăng có thể là nhầm lẫn giữa tín hiệu và tài sản. Câu hỏi quan trọng hơn là: nút thắt nào chưa được định giá đầy đủ?

**ARM là tín hiệu. Alpha nằm ở nút thắt.**

---

*Bài viết này chỉ nhằm mục đích nghiên cứu và bình luận, không phải tư vấn đầu tư. Dữ liệu giá ARM và MRVL dựa trên Research OS local DB, giá đóng cửa Mỹ ngày 21/5/2026. Dữ liệu doanh nghiệp lấy từ NVIDIA, Arm, Marvell và Samsung Electro-Mechanics. Mốc dữ liệu: 22/5/2026 KST.*

[1]: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-First-Quarter-Fiscal-2027/default.aspx "NVIDIA Announces Financial Results for First Quarter Fiscal 2027"
[2]: https://newsroom.arm.com/news/arm-q4-fye26-results "Arm delivers record-breaking quarter and full-year results"
[3]: https://www.bloomberg.com/news/articles/2026-05-15/arm-holdings-said-to-face-us-antitrust-probe-over-chip-tech "Arm Holdings Said to Face US Antitrust Probe Over Chip Tech"
[4]: https://d1io3yog0oux5.cloudfront.net/_cde1ddaaf3189b05accbc0f122d6a0c2/marvell/db/3715/35343/pdf/2026_03_05_Marvell_Q4_FY26_financial_business_results_FINAL.pdf "Marvell FY26 and Q4 FY26 Financial and Business Results"
[5]: https://d1io3yog0oux5.cloudfront.net/_a2ff1b1766821fdbdf60a17efbf050dd/marvell/files/pages/marvell/db/3831/description/2025-12_02-Marvell-to-Acquire-Celestial-AI-vF2.pdf "Marvell to Acquire Celestial AI"
[6]: https://samsungsem.com/global/newsroom/news/view.do?id=10310 "Samsung Electro-Mechanics Signs 1.5 Trillion KRW Silicon Capacitor Supply Contract"
