---
title: "Dòng tái cân bằng ETF chủ đề Hàn Quốc: mua tái phân bổ ở bán dẫn phụ trợ, áp lực giảm tỷ trọng ở nhóm dẫn đầu"
date: 2026-06-12T17:40:00+09:00
description: "Lần chạy đầu tiên của KR Theme ETF Rebalance Flow v1 cho thấy tín hiệu dòng tiền cơ học từ tái cân bằng và giới hạn tỷ trọng ETF chủ đề Hàn Quốc. Tín hiệu mạnh nhất ngày 12/6/2026 nằm ở thiết bị và vật liệu bán dẫn."
categories: ["Korean-Equities", "Market-Flow", "ETF-Flow"]
tags: ["ETF Hàn Quốc", "tái cân bằng ETF", "bán dẫn", "dòng tiền thụ động"]
series: ["korea-rerating-2026", "korea-market-flow"]
slug: "kr-theme-etf-rebalance-flow-semicap-cap-trim-2026-06-12"
draft: false
---

## TL;DR

- Thesis OS đã thêm **KR Theme ETF Rebalance Flow v1**, công cụ theo dõi dòng tiền cơ học từ tái cân bằng ETF chủ đề Hàn Quốc.
- Lần chạy đầu tiên quét **31 ETF**, có **30 ETF hợp lệ**, xử lý **291 dòng cổ phiếu thành phần** và tạo **69 ứng viên**.
- Có **60 ứng viên mua do tái phân bổ** và **9 ứng viên chịu áp lực giảm tỷ trọng do giới hạn cap**.
- Tín hiệu mạnh nhất không phải hạt nhân/SMR mà là **thiết bị và vật liệu bán dẫn**.
- Leeno Industrial, EO Technics, Soulbrain, DB HiTek, Hanmi Semiconductor, ISC và Wonik IPS là nhóm nổi bật.

## 1. Công cụ này đo gì

Công cụ ước tính proxy tái phân bổ tỷ trọng:

```text
Dòng tiền ETF = NAV ETF × thay đổi tỷ trọng mục tiêu
Dòng tiền cổ phiếu = tổng dòng tiền từ các ETF
Cường độ = dòng tiền ước tính / giá trị giao dịch bình quân 20 ngày
```

Dữ liệu đến từ Naver ETF surface (`constituentList`, `totalNav`) và cơ sở dữ liệu giá nội bộ. Nếu một cổ phiếu vượt giới hạn tỷ trọng giả định, mô hình giảm về mức cap và phân bổ phần dư cho các cổ phiếu còn dưới cap.

Đây không phải dữ liệu PCF chính thức. Cần kiểm tra PDF/PCF của nhà phát hành, phương pháp chỉ số, quy tắc cap thực tế và khối lượng giao dịch cuối phiên.

| Chỉ tiêu | Giá trị |
|---|---:|
| Ngày | 2026-06-12 |
| ETF quét | 31 |
| ETF hợp lệ | 30 |
| Dòng thành phần | 291 |
| Ứng viên | 69 |
| Mua tái phân bổ | 60 |
| Giảm tỷ trọng cap | 9 |
| Độ tin cậy | trung bình-thấp |

## 2. Ứng viên mua tái phân bổ

| Cổ phiếu | Dòng tiền ước tính | Flow/ADV20 | Biến động ngày |
|---|---:|---:|---:|
| Leeno Industrial | 270.4 tỷ KRW | +2.68x | +4.7% |
| EO Technics | 197.8 tỷ KRW | +2.49x | +21.4% |
| Soulbrain | 69.4 tỷ KRW | +2.44x | +24.4% |
| DB HiTek | 264.3 tỷ KRW | +2.02x | +12.3% |
| Hanmi Semiconductor | 721.0 tỷ KRW | +1.81x | +24.1% |
| ISC | 92.0 tỷ KRW | +1.76x | +20.7% |
| Wonik IPS | 211.1 tỷ KRW | +1.63x | +30.0% |

Ý nghĩa chính là cường độ so với thanh khoản. Cổ phiếu hạng hai có thể phản ứng mạnh hơn cổ phiếu dẫn đầu nếu dòng tiền ETF lớn so với giá trị giao dịch bình quân.

## 3. Nhóm chịu áp lực giảm tỷ trọng

| Cổ phiếu | Dòng tiền ước tính | Flow/ADV20 | Diễn giải |
|---|---:|---:|---|
| SK Hynix | -1.76 nghìn tỷ KRW | -0.15x | áp lực kỹ thuật, không phải luận điểm short |
| Samsung Electronics | -49.4 tỷ KRW | -0.00x | tác động tương đối thấp |
| Samsung Electro-Mechanics | -514.9 tỷ KRW | -0.21x | cần theo dõi áp lực kỹ thuật |
| LS ELECTRIC | -47.0 tỷ KRW | -0.15x | tránh đuổi giá nếu chưa xác nhận |
| Doosan Enerbility | -26.5 tỷ KRW | -0.07x | theo dõi nhóm hạt nhân |

## 4. Cách dùng

Đây là bộ lọc sự kiện, không phải tín hiệu mua cuối cùng.

| Bước | Điều cần xác nhận |
|---|---|
| 1 | PDF/PCF chính thức của ETF |
| 2 | Phương pháp chỉ số và quy tắc cap thực tế |
| 3 | Khối lượng đóng cửa và giao dịch cuối phiên |
| 4 | Sức mạnh tương đối T+1/T+3 |
| 5 | Dòng chương trình, nước ngoài hoặc tổ chức cùng chiều |

## Kết luận

Lần chạy đầu tiên cho thấy dòng tái cân bằng ETF chủ đề đang nghiêng về **bán dẫn phụ trợ**. Đây là tín hiệu đáng theo dõi, nhưng chỉ có thể nâng cấp thành tín hiệu giao dịch sau khi có xác nhận chính thức và dữ liệu giao dịch thực tế.
