---
title: "KOSPI lệch MA60 +28,6%: không phải gọi đỉnh, mà là tín hiệu giảm rủi ro một phần"
date: 2026-06-21T02:35:00+09:00
description: "Tái dựng khung đo quá nóng của KOSPI bằng độ lệch so với MA60, cho thấy +28,6% nên được hiểu là tín hiệu tái cân bằng rủi ro hơn là gọi đỉnh."
categories: ["Exclusive Analysis", "Market-Outlook", "Risk-Management"]
tags: ["KOSPI", "disparity", "market breadth", "risk management", "RSI", "ATR", "Samsung Electronics", "SK Hynix", "narrow market"]
series: ["exclusive-analysis", "korea-market-flow", "risk-management"]
slug: "kospi-disparity60-overheat-framework-partial-trim-2026-06-21"
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Bối cảnh
> Bài này tiếp nối các phân tích về [độ khó khi vượt KOSPI thuần](/vi/post/kospi-benchmark-hard-to-beat-narrow-market-monte-carlo-2026-06-20/), [thị trường Hàn Quốc do ETF flow dẫn dắt](/vi/post/korea-etf-flow-led-market-volatility-strategy-2026-06-13/) và [thanh khoản nhiều nhưng breadth yếu](/vi/post/korea-market-liquidity-foreign-reallocation-adr-narrow-leadership-2026-06-03/).

## TL;DR

- Ngày 19/6/2026, KOSPI đóng cửa ở **9.052**, MA60 là **7.039**, và độ lệch so với MA60 là **+28,6%**.
- Đây là quá nóng trung hạn, nhưng không phải bằng chứng chắc chắn của đỉnh. Trong 355 phiên từ đầu 2025, tín hiệu quá nóng theo MA20/60/120 vẫn có lợi suất trung bình 5 ngày và 20 ngày dương.
- Tuy vậy, khi độ lệch MA60 vượt +20%, xác suất giảm -5% trong 10 phiên tăng từ 16% lên **63%**.
- Nhưng 41 ngày tín hiệu không phải 41 mẫu độc lập. Chúng chỉ là **8 episode**, trong đó 6 episode có đủ cửa sổ tương lai.
- Kết luận: **giảm rủi ro một phần là hợp lý, nhưng chưa phải tín hiệu thoát toàn bộ**. Độ lệch và biến động đã bật; độ dốc MA20 vẫn tăng.

<div class="thesis-callout">
  <div class="thesis-callout__label">Điểm chính</div>
  <div class="thesis-callout__body">
    Độ lệch MA60 +28,6% không nói <strong>“đây là đỉnh”</strong>. Nó nói xu hướng đã chạy quá nhanh, nên giảm đuổi giá, thu hồi một phần ngân sách rủi ro và chờ nhịp điều chỉnh sạch hơn.
  </div>
</div>

## Khung tái dựng

| Mục | Thiết lập |
|---|---|
| Chỉ số | KOSPI, `^KS11` |
| Giai đoạn | 2025-01-02 đến 2026-06-19 |
| Mẫu | 355 phiên |
| Giá | Đóng cửa |
| Độ lệch | `đóng cửa / MA N ngày - 1` |
| Cửa sổ | 20, 60, 120 ngày |
| Điều chỉnh | Đáy -5% hoặc tệ hơn trong 10 phiên kế tiếp |

## Trạng thái hiện tại

| Chỉ báo | Giá trị tái dựng |
|---|---:|
| KOSPI đóng cửa | **9.052** |
| MA20 / lệch20 | **8.322 / +8,77%** |
| MA60 / lệch60 | **7.039 / +28,61%** |
| MA120 / lệch120 | **6.088 / +48,69%** |
| Độ dốc MA20 5 phiên | **+4,25%** |
| RSI(14) | **SMA 57,3 / Wilder 65,9** |
| ATR(20)% | **vùng 4%** |

Đây không phải tín hiệu RSI. Đây là tín hiệu tốc độ quá nhanh so với MA60 và biến động cao.

## Quá nóng không gọi đỉnh tốt

| Tín hiệu | Số ngày | Lợi suất +5D | Lợi suất +20D |
|---|---:|---:|---:|
| Lệch20 ≥ 7% | 74 | +2,68% | +9,07% |
| Lệch60 ≥ 12% | 120 | +2,26% | +6,88% |
| Lệch120 ≥ 20% | 107 | +2,55% | +9,11% |
| Baseline | 335 | +1,86% | +7,83% |

Trong xu hướng mạnh, quá nóng có thể là tăng tốc trước khi là đỉnh.

## Nhưng xác suất pullback tăng

| Điều kiện | Số ngày | Giảm -5% trong 10 phiên |
|---|---:|---:|
| Baseline | tất cả | **16%** |
| Lệch60 ≥ 15% | 89 | **36%** |
| Lệch60 ≥ 18% | 54 | **48%** |
| Lệch60 ≥ 20% | 41 | **63%** |
| Lệch60 ≥ 22% | 33 | **67%** |
| Lệch60 ≥ 25% | 26 | **65%** |

Tín hiệu đúng là rủi ro pullback tăng, không phải bán tất cả.

## Ba cổng hiện tại

| Cổng | Quy tắc | Hiện tại | Trạng thái |
|---|---|---:|---|
| Quá tốc trung hạn | Lệch60 ≥ 18-20% | **+28,6%** | Bật |
| Biến động | ATR ≥ 2,2% | **vùng 4%** | Bật |
| Xu hướng xấu đi | Độ dốc MA20 giảm | **+4,25%** | Chưa bật |

Hai cổng đã bật, vì vậy không nên đuổi giá quá mạnh. Nhưng cổng thứ ba chưa bật, nên chưa phải tín hiệu thoát toàn bộ.

## Kết luận

KOSPI lệch MA60 +28,6% là quá nóng thật. Nhưng dữ liệu không ủng hộ kết luận “đỉnh đã xác nhận”.

Khung này nên được dùng như công cụ tái cân bằng: ngừng đuổi giá, thu hồi một phần ngân sách rủi ro, và chờ xu hướng yếu đi hoặc nhịp pullback rõ hơn.
