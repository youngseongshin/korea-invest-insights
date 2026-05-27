---
title: "Korea ADR ở mức 67: Tại Sao Chỉ Số Có Thể Trụ Vững Dù Hầu Hết Cổ Phiếu Đang Yếu"
slug: "korea-adr-breadth-narrow-leadership-kospi-kosdaq-2026-05-27"
date: 2026-05-27T16:25:00+09:00
description: "Dữ liệu local từ Research OS cho thấy tỷ lệ tăng-giảm 20 ngày của Hàn Quốc giảm từ 113,1 vào giữa tháng 4 xuống còn 67,3 vào ngày 26/5. KOSPI và KOSDAQ không trong giai đoạn risk-on rộng rãi; dòng tiền đang dồn vào hạ tầng AI, nút cổ chai bán dẫn, back-end, substrate, đóng tàu và quốc phòng."
categories: ["Thị Trường Hàn Quốc", "Vĩ Mô - Góc Nhìn", "Chuỗi Cung Ứng Công Nghệ Hàn Quốc"]
tags:
  - "Korea ADR"
  - "Độ rộng thị trường"
  - "KOSPI"
  - "KOSDAQ"
  - "Hạ tầng AI"
  - "Bán dẫn back-end"
  - "Dẫn dắt thị trường"
  - "Research OS"
series: ["Korea Market Regime"]
---

> Bài viết này tiếp nối [khung phân tích risk-off phức hợp và các điều kiện phục hồi](/post/macro-snapshot-complex-risk-off-recovery-triggers-2026-05-17/), [tỷ lệ sở hữu nước ngoài trên KOSPI so với Samsung và SK Hynix](/post/korea-foreign-ownership-kospi-samsung-hynix-divergence-2026-05-26/), [phân tích dòng tiền nhà đầu tư nước ngoài tại Hàn Quốc](/post/korea-foreign-investor-flow-memory-megacap-rotation-2026-05-24/) và [bản đồ smart money Quỹ Tăng Trưởng Quốc Gia / KOSDAQ](/post/national-growth-fund-kosdaq-smart-money-policy-bottlenecks-2026-05-24/). Các bài trước đã phân tích cổng vĩ mô, dòng tiền vào mega-cap KOSPI và dòng vốn chính sách trên KOSDAQ. Bài này đặt ra một câu hỏi đơn giản hơn: **sức khỏe thực sự của thị trường bên dưới chỉ số là như thế nào?**

## TL;DR

* ADR 20 ngày của Hàn Quốc giảm từ **113,1 xuống 67,3** trong tháng qua. KOSPI giảm từ **116,3 xuống 68,5** và KOSDAQ từ **111,6 xuống 66,7**. Cổ phiếu bình quân đã trong vùng điều chỉnh dù chỉ số vẫn trụ được.
* Đây không phải risk-on diện rộng. Đây là **dẫn dắt hẹp** tập trung vào các nút cổ chai hạ tầng AI, MLCC / FC-BGA / SOCAMM / bán dẫn back-end, và một số tên tuổi đóng tàu / quốc phòng / điện năng.
* Giao dịch tiếp theo không phải đuổi theo cổ phiếu dẫn đầu tuyến một. Đó là theo dõi **ADR phục hồi + thanh khoản tăng + dòng tiền ngoại / tổ chức đầu tiên vào các ứng viên tuyến hai**. Màn hình lọc local chỉ ra HPSP, SFA Semicon, Hana Micron, Dongjin Semichem và KMW.

![Xu hướng ADR thị trường chứng khoán Hàn Quốc: ADR 20 ngày và tỷ lệ tăng hàng ngày trong tháng qua](korea-adr-breadth-chart-2026-05-26.jpg)

<small>Nguồn: Research OS local DB `prices_daily` + `universe.csv`. Dữ liệu chốt tại phiên đóng cửa ngày 26/5/2026. Dữ liệu nội phiên ngày 27/5 không được tính vào.</small>

---

## 1. ADR Cho Ta Biết Điều Gì

ADR đo độ rộng thị trường, không phải mức chỉ số.

Công thức rất đơn giản.

```text
ADR ngày = số cổ phiếu tăng / số cổ phiếu giảm × 100
ADR 20D = tổng số cổ phiếu tăng trong 20 phiên / tổng số cổ phiếu giảm trong 20 phiên × 100
Tỷ lệ tăng = số cổ phiếu tăng / tổng số cổ phiếu × 100
```

ADR bằng 100 nghĩa là số cổ phiếu tăng và giảm cân bằng nhau. Dưới 80, cổ phiếu giảm đang thống trị rõ ràng. Nếu ADR nằm trong vùng 60–70 trong khi chỉ số vẫn vững, thị trường thường đang được chống đỡ bởi một vài bluechip vốn hóa lớn hoặc một nhóm theme hẹp.

Đó chính xác là tình trạng của Hàn Quốc hiện tại.

| Thị trường | ADR 20D ngày 16/4/2026 | ADR 20D ngày 26/5/2026 | Thay đổi | Nhận định |
|---|---:|---:|---:|---|
| KOSPI | 116,3 | 68,5 | -47,8 điểm | Độ rộng nhóm bluechip đã yếu đi |
| KOSDAQ | 111,6 | 66,7 | -44,9 điểm | Độ rộng vừa và nhỏ đã nguội rõ rệt |
| Toàn thị trường | 113,1 | 67,3 | -45,8 điểm | Cổ phiếu bình quân đã yếu |

Điểm quan trọng là đây không chỉ là vấn đề của KOSDAQ. ADR 20 ngày của KOSPI cũng đã rơi xuống 68,5. Vì vậy nhận định đúng không phải là "KOSDAQ yếu nhưng KOSPI vẫn khỏe." Mà là:

> Độ rộng thị trường Hàn Quốc đã thu hẹp, và dòng vốn sống sót đang dồn vào hạ tầng AI, đóng tàu, quốc phòng và một vài nhóm dẫn dắt còn lại.

---

## 2. Tại Sao Đợt Hồi Phục Cuối Tháng 5 Vẫn Chưa Đủ

Ngày 20/5, chỉ có 333 cổ phiếu tăng trong khi 2.082 cổ phiếu giảm. ADR ngày là **16,0** và tỷ lệ tăng là **13,5%**. Đó gần như là một phiên đầu hàng ngắn hạn.

Đợt hồi phục ngày 21–22/5 rất mạnh.

| Ngày | Tăng | Giảm | ADR ngày | ADR 20D | Tỷ lệ tăng | Nhận định |
|---|---:|---:|---:|---:|---:|---|
| 2026-05-20 | 333 | 2.082 | 16,0 | 58,3 | 13,5% | Đầu hàng ngắn hạn |
| 2026-05-21 | 1.695 | 720 | 235,5 | 61,9 | 68,6% | Hồi phục kỹ thuật |
| 2026-05-22 | 2.097 | 283 | 742,2 | 67,9 | 86,1% | Hồi phục mạnh |
| 2026-05-26 | 749 | 1.660 | 45,1 | 67,3 | 30,2% | Độ rộng yếu trở lại |

Vấn đề nằm ở ngày 26/5. Sau đợt hồi phục mạnh, số cổ phiếu giảm lại tăng lên 1.660 và tỷ lệ tăng rớt về 30,2%.

Như vậy trạng thái hiện tại chưa phải mở rộng độ rộng được xác nhận. Đây là nỗ lực tạo đáy về độ rộng vẫn đang bị thử thách.

Điều này liên hệ trực tiếp với [khung risk-off vĩ mô trước đó](/post/macro-snapshot-complex-risk-off-recovery-triggers-2026-05-17/). Điều kiện đặt ra là giá dầu, lãi suất dài hạn, USD, KRW, tín dụng Trung Quốc và dòng tiền ngoại cần ổn định đồng thời. Dữ liệu ADR cho thấy sự phục hồi đó vẫn chưa lan rộng ra toàn thị trường.

---

## 3. Chế Độ Thị Trường Hiện Tại: Dẫn Dắt Hẹp

Chế độ thị trường chứng khoán Hàn Quốc hiện tại là **Dẫn Dắt Hẹp / Risk-On Chọn Lọc**.

| Tiêu chí | Nhận định |
|---|---|
| Độ rộng thị trường | Yếu. ADR 20D toàn thị trường là 67,3 |
| Dẫn dắt | Rất mạnh ở hạ tầng AI và một số nhóm đóng tàu / quốc phòng |
| Độ khó giao dịch | Cao. Chọn cổ phiếu quan trọng hơn hướng đi của chỉ số |
| Mở vị thế mới | Ưu tiên pullback và cổ phiếu tuyến hai hơn đuổi theo dẫn đầu tuyến một |
| Quan điểm danh mục | Giữ lãnh đạo tương đối mạnh, thay thế vị thế yếu, tránh dùng hết tiền mặt trước khi độ rộng phục hồi |

Sai lầm phổ biến là nói "chỉ số đang giữ vững nên toàn thị trường ổn." Với ADR ở vùng 60, hầu hết cổ phiếu không ổn. Sai lầm ngược lại là nói "độ rộng xấu nên tránh tất cả." Điều đó cũng sai, vì dòng vốn vẫn rất tích cực trong một nhóm ngành hẹp.

Các nhóm sống sót gồm:

1. **Nút cổ chai hạ tầng AI:** Samsung Electro-Mechanics, Jeju Semiconductor, Daeduck Electronics, Simmtech, Haesung DS, Hana Micron, HPSP
2. **Mega-cap bộ nhớ:** SK Hynix, Samsung Electronics
3. **Đóng tàu / quốc phòng / SMR hạt nhân:** HD Hyundai Heavy Industries, Hanwha Ocean, Doosan Fuel Cell
4. **Điện năng / quang học / mạng lưới:** một số tên tuổi cáp điện, RF và quang học chọn lọc

Thị trường yếu, nhưng các nhóm dẫn dắt không chết. Đó không phải mâu thuẫn. Khi độ rộng sụp đổ, dòng vốn thường dồn mạnh hơn vào số ít theme vẫn còn hiệu quả.

---

## 4. Thực Tế Dẫn Dắt Ở Đâu Trong Tháng Qua

Danh sách dẫn dắt tháng qua tập trung vào hạ tầng AI và đóng tàu / quốc phòng.

Lợi nhuận tính bằng %, thanh khoản và dòng tiền tính bằng đơn vị 100 triệu KRW.

| Cổ phiếu | 1T | 5N | Thanh khoản TB | Ngoại 1T | Tổ chức 1T | Bán lẻ 1T | Nhận định |
|---|---:|---:|---:|---:|---:|---:|---|
| Jeju Semiconductor | +173,6 | +28,4 | 3.692,8 | +1.440,8 | +595,8 | -1.962,1 | Khám phá cấp hai LPDDR. Đang nóng |
| Samsung Electro-Mechanics | +146,0 | +52,5 | 8.986,4 | -9.036,0 | +4.953,0 | +3.922,2 | Dẫn đầu MLCC + FC-BGA. Tổ chức dẫn dắt |
| Daeduck Electronics | +81,4 | +20,5 | 1.198,1 | +524,4 | +827,0 | -954,7 | Cốt lõi FC-BGA / MLB |
| Simmtech | +74,5 | +32,3 | 822,6 | +678,3 | +1.376,0 | -2.070,4 | Cốt lõi SOCAMM / substrate |
| Haesung DS | +72,7 | +19,2 | 297,3 | +132,7 | +656,4 | -53,9 | Lựa chọn tản nhiệt / substrate |
| Hana Micron | +48,3 | +5,0 | 1.200,6 | +2.172,5 | +158,3 | +135,8 | Phục hồi back-end do ngoại dẫn dắt |
| HD Hyundai Heavy Industries | +51,0 | +21,1 | 3.642,0 | -5.344,5 | +7.038,2 | -1.987,9 | Đóng tàu + lựa chọn hạt nhân do tổ chức dẫn dắt |
| Hanwha Ocean | +2,1 | +16,3 | 2.369,4 | +1.472,3 | +1.393,3 | +6.409,7 | Dòng tiền 5 ngày cải thiện, vẫn là laggard |

Điểm mấu chốt là không phải tất cả các nhóm dẫn dắt đều có chất lượng dòng tiền như nhau.

Samsung Electro-Mechanics tăng 146,0% trong một tháng, nhưng khối ngoại đã bán ròng 903,6 tỷ KRW. Tổ chức và bán lẻ hấp thụ nguồn cung đó. Điều này phù hợp với [bài phân tích vốn hóa 100 nghìn tỷ KRW của SEMCO](/post/samsung-electro-mechanics-100tn-murata-hyundai-market-cap-2026-05-26/): câu chuyện tái định giá linh kiện thụ động AI là có thực, nhưng hiệu quả khi đuổi theo đã giảm.

Hana Micron, ngược lại, tăng 48,3% với mua ròng nước ngoài 217,25 tỷ KRW trong một tháng. Đó là lý do nó trông giống ứng viên mở rộng back-end tuyến hai hơn là một cổ phiếu dẫn đầu tuyến một đã được sở hữu quá nhiều.

HD Hyundai Heavy Industries bị khối ngoại bán nhưng được tổ chức mua mạnh. Điều này liên kết với [phân tích quyền chọn SMR của HD Hyundai Heavy Industries](/post/hd-hyundai-heavy-industries-smr-terrapower-natrium-option-2026-05-27/): câu chuyện đóng tàu / động cơ / SMR vẫn còn sống, nhưng đà tăng do tổ chức dẫn dắt và vị trí giá hiện tại rất quan trọng.

---

## 5. KOSDAQ Yếu, Hay Đang Phục Hồi Chọn Lọc?

ADR 20D của KOSDAQ là 66,7. Bề ngoài là yếu. Nhưng điều đó không có nghĩa là phải tránh toàn bộ KOSDAQ.

[Bài viết trước về smart money KOSDAQ và đà phục hồi của Pearl Abyss](/post/kosdaq-smart-money-return-pearl-abyss-rebound-2026-05-22/) đã lập luận rằng dòng tiền có thể xoay chiều trước giá. Dữ liệu ADR thu hẹp khung nhìn đó lại.

Điều quan trọng không phải là mua rộng rãi KOSDAQ. Mà là tìm **các cổ phiếu tuyến hai nơi thanh khoản đang bắt đầu tăng tốc, dòng tiền ngoại/tổ chức dương, và khoảng cách so với đường MA 20 ngày vẫn ở mức quản lý được**.

Màn hình lọc local nổi bật:

| Hạng | Cổ phiếu | Theme | 5N | 20N | TK TB 5N | Tăng tốc TK | Khoảng cách MA 20N | fi5 | Nhận định |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | HPSP | Thiết bị bán dẫn / hạ tầng AI | +12,7 | +3,4 | 1.989,2 | 1,28x | +2,9 | +509,3 | Ứng viên tuyến hai sạch nhất |
| 2 | SFA Semicon | Back-end | +19,9 | -2,5 | 3.020,5 | 3,41x | +7,4 | +259,1 | Ứng viên mở rộng back-end |
| 3 | Hana Micron | Back-end | -1,2 | +16,6 | 1.386,3 | 1,18x | +3,8 | +129,4 | Ứng viên pullback |
| 4 | Dongjin Semichem | Vật liệu | +5,4 | -4,0 | 642,5 | 1,15x | +3,1 | +447,4 | Ứng viên phục hồi dòng tiền vật liệu |
| 5 | KMW | RF / AI-RAN | +11,7 | +20,8 | 259,0 | 1,30x | n/a | +226,8 | Ứng viên xác nhận sự kiện AI-RAN |

`fi5` là mua ròng nước ngoài cộng tổ chức trong 5 ngày. Một số trường dữ liệu dòng tiền local có thể bị thiếu hoặc không đầy đủ, vì vậy cần xác thực dòng tiền qua Kiwoom / KRX trước khi ra quyết định cổ phiếu cụ thể.

---

## 6. Các Điều Kiện Kích Hoạt Mở Rộng Độ Rộng

Đây chưa phải vùng mua rộng thị trường. Với ADR toàn thị trường là 67,3, cổ phiếu giảm vẫn đang thống trị.

Danh sách kiểm tra xác nhận:

| Điều kiện | Ngưỡng | Ý nghĩa |
|---|---|---|
| ADR 20D phục hồi về 80 | ADR toàn thị trường trên 80 | Sự thống trị của cổ phiếu giảm đang giảm bớt |
| ADR 20D phục hồi về 100 | ADR toàn thị trường trên 100 | Tăng và giảm đang cân bằng |
| Tỷ lệ tăng ngày trên 55% | 2–3 phiên liên tiếp | Đợt hồi không chỉ là một ngày bùng phát |
| Thanh khoản KOSDAQ tăng | Thanh khoản tăng cùng số cổ phiếu tăng nhiều hơn | Độ rộng vừa/nhỏ có thể mở rộng |
| Bán ròng ngoại được hấp thụ | Tỷ giá ổn định và chỉ số giữ/tăng | Hấp thụ nhiều hơn là risk-off thực sự |

Theo ngành, chuỗi cần theo dõi là:

| Ngành | Tín hiệu | Ý nghĩa |
|---|---|---|
| Tuyến hai hạ tầng AI | HPSP, SFA Semicon, Hana Micron, Dongjin Semichem tăng thanh khoản | Mở rộng nội bộ trong nhóm bán dẫn |
| Quang học / RF / AI-RAN | KMW, RFHIC, Oi Solution dòng tiền xoay chiều | Liên kết Marvell / NVIDIA AI-RAN |
| FC-BGA / MLB | Daeduck, ISU Petasys, Korea Circuit tăng tốc trở lại | Xác nhận custom ASIC / mạng AI |
| Test socket / back-end | ISC, Leeno, TSE, Doosan Tesna thanh khoản tăng | Mở rộng hạ tầng test SOCAMM / ASIC |
| Đóng tàu / quốc phòng tuyến hai | Dòng tiền xoay sang laggard trong đợt pullback của dẫn đầu | Luân chuyển trong theme dẫn dắt hiện có |

Điều này liên kết lại với [bài preview nút cổ chai AI Hàn Quốc từ Marvell / Broadcom](/post/marvell-broadcom-earnings-korea-ai-bottleneck-preview-2026-05-23/). Nếu thị trường đang luân chuyển từ trade HBM đơn thuần sang custom ASIC, mạng AI, kết nối quang và power integrity, ADR rộng có thể vẫn yếu trong khi các nút cổ chai hạ tầng phía dưới tiếp tục thu hút thanh khoản.

---

## 7. Đọc Thực Tế

Băng chuyền thị trường Hàn Quốc hiện tại có thể tóm gọn trong hai dòng:

> Thị trường rộng đang yếu.  
> Nhóm dẫn dắt chưa chết.

Kế hoạch hành động phải phản ánh cả hai điều đó.

| Hành động | Điều kiện | Mục tiêu |
|---|---|---|
| Giữ dẫn đầu hiện tại | Sức mạnh tương đối vẫn còn dù ADR yếu | Samsung Electro-Mechanics, Daeduck và các tên hạ tầng AI |
| Tránh đuổi theo dẫn đầu tuyến một | ADR 20D dưới 80 | Các tên dẫn đầu tuyến một đang nóng |
| Theo dõi ứng viên tuyến hai | Tăng tốc thanh khoản + fi5 dương + khoảng cách MA quản lý được | HPSP, SFA Semicon, Hana Micron |
| Thay thế vị thế yếu | Danh mục kém hơn thị trường và dòng tiền yếu | Vị thế ngoài nhóm dẫn dắt / cốt lõi |
| Quản lý tiền mặt | Tập trung danh mục cao trước khi độ rộng phục hồi | Không triển khai hết tiền khi độ rộng vẫn yếu |

Đuổi theo dẫn đầu tuyến một không hiệu quả lúc này. Samsung Electro-Mechanics, Jeju Semiconductor và Simmtech đã tăng mạnh. Nhưng né tránh toàn bộ cổ phiếu vì độ rộng yếu sẽ bỏ lỡ chế độ dẫn dắt hẹp này.

Quan điểm rõ ràng hơn là: **giữ dẫn đầu, theo dõi tuyến hai, và yêu cầu ADR trên 80 trước khi mở rộng exposure.**

---

## 8. Kết Luận

Hàn Quốc không phải thị trường chết. Nhưng cũng không phải thị trường rộng.

Tính đến phiên đóng cửa ngày 26/5/2026, ADR 20 ngày toàn thị trường là **67,3**. KOSPI là **68,5** và KOSDAQ là **66,7**. Đó là nền tảng yếu để mua cổ phiếu bình quân. Đồng thời, Samsung Electro-Mechanics, Jeju Semiconductor, Daeduck Electronics, Simmtech, Hana Micron và HD Hyundai Heavy Industries vẫn cho thấy sức dẫn dắt mạnh.

Vì vậy chế độ thị trường là **dẫn dắt hẹp**, không phải risk-on diện rộng.

Ba điều cần kiểm tra:

1. ADR toàn thị trường có phục hồi trên 80 không?
2. Thanh khoản KOSDAQ và số cổ phiếu tăng có cùng tăng lên không?
3. Dòng tiền ngoại và tổ chức có bắt đầu xuất hiện ở các tên hạ tầng AI tuyến hai không?

Cho đến khi các điều kiện đó cải thiện, đuổi theo dẫn đầu tuyến một kém hấp dẫn hơn quan sát các ứng viên tuyến hai. Nếu độ rộng phục hồi, thị trường có thể mở rộng. Nếu không, chỉ có số ít dẫn đầu sống sót. Quan điểm đúng không phải lạc quan cũng không phải bi quan. Đó là chấp nhận rằng độ rộng thị trường đang hẹp và đi theo nơi thanh khoản thực và dòng tiền chất lượng đang xuất hiện.

---

## Phụ Lục. Phân Loại Bằng Chứng

### [Sự Kiện]

* Tính đến ngày 26/5/2026, ADR 20D toàn thị trường là **67,3**.
* Ngày 16/4/2026, ADR 20D toàn thị trường là **113,1**.
* Ngày 26/5/2026, có 749 cổ phiếu Hàn Quốc tăng, 1.660 giảm, và ADR ngày là **45,1**.
* Danh sách dẫn đầu tháng qua bao gồm Samsung Electro-Mechanics, Jeju Semiconductor, Daeduck Electronics, Simmtech, Haesung DS, Hana Micron và HD Hyundai Heavy Industries.
* HPSP, SFA Semicon, Hana Micron và Dongjin Semichem đạt kết quả tương đối tốt trên các điều kiện thanh khoản và dòng tiền trong màn hình lọc.

### [Suy Luận]

* Thị trường hiện tại là dẫn dắt hẹp, không phải risk-on rộng.
* Quan trọng hơn chỉ đơn thuần mua ròng nước ngoài là liệu một ngành có thể giữ giá và thu hút thanh khoản dù bị ngoại bán hay không.
* Trong hạ tầng AI, luân chuyển có thể di chuyển từ SOCAMM / LPDDR sang FC-BGA / MLB, back-end, quang học và RF.
* Tăng tốc thanh khoản và xoay chiều dòng tiền tuyến hai có kỳ vọng giá trị tốt hơn so với đuổi theo dẫn đầu tuyến một sau những đợt tăng lớn.

### [Suy Đoán]

* Kết quả Marvell có thể củng cố theme custom ASIC, quang học và AI-RAN mạnh hơn chỉ riêng SOCAMM.
* Kết quả Broadcom có thể tái kích hoạt mạng AI, FC-BGA / ABF và các tên MLB tốc độ cao.
* Nếu ADR phục hồi trên 80, xác suất mở rộng tuyến hai tăng lên.

### [Chưa Có Dữ Liệu]

* ADR đóng cửa ngày 27/5/2026 không được tính vào bài này.
* Một số trường dữ liệu dòng tiền 5 ngày có thể bị thiếu hoặc không đầy đủ trong DB local.
* Các ứng viên AI-RAN như RFHIC và Oi Solution cần xác thực dòng tiền riêng qua Kiwoom / KRX trước khi đưa ra phán xét cụ thể ở cấp độ cổ phiếu.

<small>Nguồn dữ liệu: Research OS local DB `prices_daily`, `universe.csv`, `korea_adr_recent_20260526.csv`, `korea_leaders_20260415_20260526.csv`, `second_line_theme_flow_candidates_20260527.csv`. Dữ liệu chốt: phiên đóng cửa ngày 26/5/2026. Đây là bình luận nghiên cứu, không phải tư vấn đầu tư.</small>

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
