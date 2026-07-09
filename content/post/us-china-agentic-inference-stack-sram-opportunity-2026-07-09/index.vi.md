---
title: "Hạ tầng suy luận AI tác tử của Mỹ và Trung Quốc đang tách hướng, cơ hội của SRAM nằm ở đâu"
date: 2026-07-09T17:20:00+09:00
description: "Vì sao hạ tầng suy luận AI của Mỹ và Trung Quốc đi theo hai hướng khác nhau, và cơ hội cho HBM, SRAM/LPU, thiết bị điện, đóng gói tiên tiến và cổ phiếu Hàn Quốc nằm ở đâu."
categories: ["Theme-Analysis", "Korea Semiconductors", "AI Infrastructure"]
tags: ["AI inference", "agentic AI", "SRAM", "LPU", "HBM", "Vera Rubin", "LPX", "Samsung Electronics", "SK hynix", "HD Hyundai Electric", "Hanmi Semiconductor"]
slug: us-china-agentic-inference-stack-sram-opportunity-2026-07-09
series: ["hbm", "exclusive-analysis"]
valley_cashtags: ["005930.KS", "000660.KS", "267260.KS", "010120.KS", "298040.KS", "042700.KS", "NVDA"]
draft: false
---

## Tóm tắt

Mỹ và Trung Quốc đều đang mở rộng hạ tầng suy luận AI, nhưng điểm nghẽn của hai bên không giống nhau. Mỹ bị giới hạn bởi điện, mật độ rack, HBM, đóng gói tiên tiến và hiệu suất token trên mỗi MW. Trung Quốc bị giới hạn bởi logic tiên tiến và khả năng tiếp cận HBM, nên phải dựa nhiều hơn vào Ascend, mạng quang, mở rộng song song và tầng bộ nhớ nội địa.

Với cổ phiếu Hàn Quốc, cơ hội rõ nhất không phải là suy diễn ngay sang linh kiện quang cho Trung Quốc. Cơ hội trực tiếp hơn nằm ở hạ tầng kiểu Mỹ: HBM4/HBM4E, thiết bị điện, thiết bị đóng gói HBM và quyền chọn chưa được định giá đầy đủ của Samsung Electronics trong foundry SRAM/LPU, lưu trữ AI và tầng bộ nhớ.

## 1. Phần nào của luận điểm có thể kiểm chứng

Luận điểm gốc từ bài viết của YS-VC là hợp lý: suy luận AI không còn là câu chuyện GPU chung chung. Mỗi khu vực đang giải một ràng buộc vật lý khác nhau.

| Luận điểm | Đánh giá | Ý nghĩa đầu tư |
|---|---|---|
| Hạ tầng suy luận của Mỹ và Trung Quốc đang tách hướng | Phần lớn đúng | Mỹ tối ưu điện và rack, Trung Quốc né giới hạn logic và HBM |
| Mỹ đi về GPU/HBM/SRAM ở cấp rack | Đúng | Vera Rubin, LPX, HBM4 và SRAM/LPU đi vào cùng một hệ thống |
| Trung Quốc dùng Ascend, mạng quang và tầng bộ nhớ riêng | Đúng một phần | Hướng đi hợp lý, nhưng CloudMatrix cần kiểm chứng độc lập |
| Kiểm soát xuất khẩu của Mỹ giới hạn compute NVIDIA cho Trung Quốc | Đúng | Trung Quốc khó dựa vào GPU và HBM cao cấp |
| HBM vẫn là điểm kiểm soát cốt lõi | Đúng | BIS xem HBM là quan trọng cho training và inference quy mô lớn |

## 2. Vì sao hai hạ tầng tách hướng

AI tác tử làm số token tăng mạnh. Agent lập trình, agent nghiên cứu, voice agent và agent doanh nghiệp đọc ngữ cảnh dài, gọi công cụ, đọc kết quả rồi sinh câu trả lời mới. Do đó prefill, decode, KV cache, lưu trữ, mạng và điện đều trở thành nút thắt.

| Hạng mục | Mỹ | Trung Quốc |
|---|---|---|
| Nút thắt chính | Điện, mật độ rack, biến áp, HBM4, đóng gói | Logic tiên tiến, HBM, kiểm soát xuất khẩu |
| Hướng kiến trúc | Vera Rubin, LPX/LPU, HBM4, rack công suất cao | Huawei Ascend, mạng quang, mở rộng song song |
| Điểm mạnh | GPU, HBM và đóng gói hàng đầu | Mở rộng điện nhanh hơn, hạ tầng do nhà nước thúc đẩy |
| Điểm yếu | Kết nối lưới điện, thời gian có điện, biến áp | Thiếu logic EUV tiên tiến, HBM hạn chế |
| Cổ phiếu Hàn Quốc | HBM, thiết bị điện, thiết bị HBM, foundry | Hạn chế nếu chưa có bằng chứng nhà cung cấp |

IEA ước tính nhu cầu điện của data center có thể đạt khoảng 945TWh vào năm 2030. ([IEA][1]) Energy Connects dẫn dữ liệu BloombergNEF cho biết Trung Quốc có thể bổ sung hơn 3,4TW công suất phát điện trong 5 năm, gần gấp 6 lần Mỹ. ([Energy Connects][2]) Vì vậy Mỹ phải tối ưu token trên mỗi MW, trong khi Trung Quốc có thể dựa nhiều hơn vào mở rộng hạ tầng.

## 3. Hạ tầng Mỹ: HBM cộng với SRAM/LPU

NVIDIA mô tả LPX là bộ tăng tốc suy luận cho Vera Rubin. Cấu trúc này kết hợp GPU Rubin dùng HBM với Groq 3 LPX dùng LPU nền SRAM. ([NVIDIA LPX][3])

| Chỉ tiêu | Công bố của NVIDIA LPX |
|---|---:|
| Token trong hệ thống agent | Tối đa 15 lần |
| Vera Rubin NVL72 + LPX | Throughput trên mỗi MW tối đa 35 lần |
| SRAM mỗi LPU accelerator | 500MB |
| Băng thông SRAM mỗi LPU accelerator | 150TB/s |
| Rack LPX | 256 chip LPU |
| SRAM mỗi rack LPX | 128GB |
| DDR5 mỗi rack LPX | 12TB |
| Băng thông SRAM mỗi rack | 40PB/s |

Đây không phải là câu chuyện thay thế HBM. HBM vẫn là trung tâm của Rubin GPU. SRAM/LPU bổ sung cho HBM bằng cách xử lý phần decode cần độ trễ thấp.

## 4. Trung Quốc là tín hiệu cạnh tranh, không phải giao dịch cổ phiếu Hàn Quốc rõ ràng

Nếu Trung Quốc không được tiếp cận tự do với GPU và HBM cao cấp, việc dùng nhiều chip hơn, mạng tốt hơn và mảng quang là hợp lý. Nhưng điều đó không tự động tạo doanh thu cho doanh nghiệp Hàn Quốc. Chuỗi cung ứng AI của Trung Quốc ngày càng nội địa hóa, và dữ liệu hiệu năng, độ lỗi, tổng chi phí của các hệ thống như CloudMatrix vẫn cần chứng cứ độc lập.

## 5. Bản đồ cổ phiếu Hàn Quốc

| Tầng | Nút thắt | Doanh nghiệp Hàn Quốc | Nhận định |
|---|---|---|---|
| HBM4/HBM4E | Bộ nhớ cho Vera Rubin và AI server | SK hynix, Samsung Electronics | Hưởng lợi cấu trúc. SK hynix dẫn đầu, Samsung là quyền chọn phục hồi |
| Foundry SRAM/LPU | Accelerator decode độ trễ thấp | Samsung Electronics | Chưa rõ doanh thu, nhưng quyền chọn quan trọng |
| Lưu trữ AI/KV cache | eSSD, PCIe 6.0, bộ nhớ agent | Samsung Electronics, FADU | Mở rộng tầng bộ nhớ bên dưới HBM |
| Thiết bị HBM | TC bonder, đóng gói tiên tiến | Hanmi Semiconductor | Nút thắt thật, nhưng cần theo dõi khách hàng và định giá |
| Thiết bị điện | Biến áp, switchgear, kết nối lưới | HD Hyundai Electric, LS ELECTRIC, Hyosung Heavy | Hưởng lợi trực tiếp từ data center Mỹ |
| Mạng quang Trung Quốc | Module quang cho cụm AI Trung Quốc | Bằng chứng Hàn Quốc hạn chế | Tránh nếu chưa có chuỗi cung ứng xác nhận |

## 6. Kết luận đầu tư

| Ưu tiên | Tiếp xúc | Nhận định |
|---:|---|---|
| 1 | Samsung Electronics | Ứng viên mua có điều kiện nếu HBM4E, SRAM/LPU và lưu trữ AI hiện rõ hơn |
| 2 | HD Hyundai Electric | Chờ, vì chất lượng tốt nhưng đơn hàng đã được thị trường biết |
| 3 | SK hynix | Chờ, vì dẫn đầu HBM nhưng đã đông người nắm giữ |
| 4 | Hanmi Semiconductor | Theo dõi, cần đơn hàng lặp lại và đa dạng khách hàng |
| 5 | Hưởng lợi từ mạng quang Trung Quốc | Tránh nếu chưa có bằng chứng trực tiếp |

Cơ hội Hàn Quốc không phải là “mạng quang Trung Quốc”. Cơ hội rõ hơn là nút thắt của AI factory kiểu Mỹ: điện, HBM, SRAM/LPU, đóng gói tiên tiến và lưu trữ. SK hynix có thể có vị thế kinh doanh tốt nhất, HD Hyundai Electric có độ thuần thiết bị điện cao nhất, nhưng quyền chọn tái định giá bất đối xứng nhất là Samsung Electronics nếu thị trường không còn nhìn công ty chỉ như kẻ đi sau trong HBM.

## Nguồn

- [YS-VC](https://www.ys-vc.com/blog/us-china-ai-inference-stack-divergence)
- [IEA](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai)
- [Energy Connects](https://www.energyconnects.com/news/renewables/2026/february/china-ramps-up-energy-boom-flagged-by-musk-as-key-to-ai-race/)
- [NVIDIA LPX](https://www.nvidia.com/en-us/data-center/lpx/)
- [Samsung Newsroom](https://news.samsung.com/global/samsung-unveils-hbm4e-showcasing-comprehensive-ai-solutions-nvidia-partnership-and-vision-at-nvidia-gtc-2026)
- [BIS](https://www.bis.gov/press-release/commerce-strengthens-export-controls-restrict-chinas-capability-produce-advanced-semiconductors-military)
- [Yonhap](https://en.yna.co.kr/view/AEN20260128002800320)
- [The Elec](https://www.thelec.net/news/articleView.html?idxno=11132)
- [Seoul Economic Daily](https://en.sedaily.com/finance/2026/07/06/hd-hyundai-electric-raises-2026-order-target-23-percent-on)
