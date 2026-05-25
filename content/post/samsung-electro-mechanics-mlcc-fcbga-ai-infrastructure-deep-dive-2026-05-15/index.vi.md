---
title: "Samsung Electro-Mechanics — Hạ tầng vô hình của AI Silicon. Phân tích MLCC (ổn định nguồn điện), FC-BGA (đế chip) và Module Camera"
date: 2026-05-15
description: "Samsung Electro-Mechanics lần đầu tiên vượt ngưỡng 3 nghìn tỷ KRW doanh thu trong một quý. Doanh thu 1Q26 đạt 3,21 nghìn tỷ KRW, lợi nhuận hoạt động 280,6 tỷ KRW. MLCC máy chủ AI và đế chip FC-BGA đang bước vào giai đoạn giá, sản lượng và tỷ lệ sử dụng công suất đồng thời tăng. SEMCO không sản xuất chip. Họ sản xuất 'linh kiện ổn định nguồn điện (MLCC)' và 'đế kết nối chip với bo mạch chủ (FC-BGA)' — những thứ chip AI cần để thực sự hoạt động bên trong máy chủ. Bài viết này mổ xẻ ba mảng kinh doanh — Component, Package Solution và Optics — để giải thích tại sao công ty đang được định giá lại từ 'nhà sản xuất linh kiện smartphone' thành 'nền tảng linh kiện hạ tầng AI', và những kỳ vọng nào đã được phản ánh vào mức giá cổ phiếu hiện tại là 1,02 triệu KRW."
categories: ["Sector-Deep-Dive"]
tags:
  - "Samsung Electro-Mechanics"
  - "009150"
  - "MLCC"
  - "FC-BGA"
  - "AI silicon"
  - "package substrate"
  - "Korea stocks"
slug: samsung-electro-mechanics-mlcc-fcbga-ai-infrastructure-deep-dive-2026-05-15
---

*Samsung Electro-Mechanics (SEMCO, KRX 009150) lần đầu tiên vượt ngưỡng 3 nghìn tỷ KRW doanh thu trong một quý. Doanh thu 1Q26 đạt 3,21 nghìn tỷ KRW, lợi nhuận hoạt động 280,6 tỷ KRW. Doanh thu mảng đế chip tăng +45% so với cùng kỳ năm trước, trở thành nhân vật chính dẫn dắt làn sóng định giá lại. Cổ phiếu tăng từ 830.000 KRW cuối tháng Tư lên 1.024.000 KRW vào giữa tháng Năm — tương đương mức tăng +23%. Giá mục tiêu của các công ty môi giới nhảy từ 1,0 triệu KRW lên 1,5 triệu KRW chỉ trong vài tuần. Thế nhưng rất ít nhà đầu tư có thể trả lời rõ ràng: SEMCO thực sự làm gì, tại sao lại được xếp vào nhóm "hưởng lợi từ AI", và ba mảng kinh doanh của họ hoạt động ra sao. Bài viết này mổ xẻ SEMCO đến từng bộ phận.*

---

## Những điểm cốt lõi

* <strong>SEMCO không phải nhà sản xuất chip.</strong> Họ làm ra <strong>linh kiện ổn định nguồn điện (MLCC)</strong> và <strong>đế kết nối chip AI với bo mạch chủ (FC-BGA)</strong> — những thứ chip AI cần để hoạt động được bên trong máy chủ.
* <strong>Ba mảng kinh doanh</strong>: Component (MLCC, 46% doanh thu, 67% lợi nhuận), Package Solution (FC-BGA, 20% doanh thu, 15% lợi nhuận), Optics (module camera, 34% doanh thu, 18% lợi nhuận).
* <strong>Sự chuyển dịch cốt lõi</strong>: trước đây là "nhà sản xuất linh kiện smartphone." Ngày nay, luận điểm định giá lại xoay quanh <strong>MLCC cao cấp cho máy chủ AI / xEV + FC-BGA cho bộ tăng tốc AI trong bối cảnh thiếu cung có tính cấu trúc</strong>.
* <strong>Kết quả 1Q26</strong>: doanh thu 3,21 nghìn tỷ KRW (+17% YoY), lợi nhuận hoạt động 280,6 tỷ KRW (+40% YoY). Loại trừ khoản chi trả thôi việc một lần 71,4 tỷ KRW, lợi nhuận hoạt động thực chất đạt 352,0 tỷ KRW.
* <strong>Mảng quan trọng nhất</strong>: Component (MLCC) bảo vệ nền lợi nhuận. Package Solution (FC-BGA) là động lực tăng giá cổ phiếu. Optics là khoản cược vào tương lai.
* <strong>Ở mức giá 1,02 triệu KRW hiện tại</strong>: đắt theo con số năm 2026, chỉ có thể bảo vệ được nếu chu kỳ đế chip AI tiếp tục chạy đến 2027–2028. Chiến lược kiên nhẫn — chờ thêm kết quả kinh doanh — hợp lý hơn là chạy theo đà tăng.

---

## 1. Điểm khởi đầu — tại sao SEMCO được xem là "hưởng lợi từ AI"?

### 1.1 Hạ tầng vô hình của AI Silicon

Trong bài viết trước về Samsung Electronics, tôi gọi HBM là "bàn làm việc của AI silicon." Nhưng dù có bàn làm việc tốt nhất (bộ nhớ) và máy tính mạnh nhất (GPU), hệ thống vẫn sẽ không hoạt động nếu <strong>nguồn điện không ổn định (hệ thống sẽ crash) hoặc chip không được kết nối đúng cách với bo mạch chủ (luồng dữ liệu bị đứt gãy).</strong>

Chính xác đây là những gì SEMCO sản xuất — "hạ tầng vô hình."

```
Vai trò của linh kiện SEMCO trong máy chủ AI:

1. MLCC — con đập điện siêu nhỏ
   → Tích trữ điện trong tích tắc và cấp ra ổn định
   → Chip AI tiêu thụ điện đột biến khi xử lý tính toán;
     MLCC hấp thụ các dao động đó
   → Một máy chủ AI dùng hàng chục nghìn MLCC

2. FC-BGA — chỗ đứng của chip
   → Đế mạch mật độ cao kết nối chip AI
     (GPU, CPU) với bo mạch chủ
   → Truyền cả điện năng lẫn tín hiệu giữa chip và bo mạch
   → Chip AI càng lớn và phức tạp,
     đế chip càng rộng và càng nhiều lớp

3. Module camera — đôi mắt
   → Camera cho điện thoại, ô tô, robot
   → Không trực tiếp gắn với AI, nhưng là tiềm năng thực sự
     khi mảng kinh doanh mở rộng sang ô tô và robot
```

### 1.2 Tại sao nguồn cung đang thắt chặt?

Trong bài về Samsung Electronics, tôi lưu ý HBM đang "hút cạn công suất fab." Hiện tượng tương tự đang diễn ra với MLCC và FC-BGA.

```
MLCC:
→ Máy chủ AI tiêu thụ nhiều điện và dao động mạnh
→ Số lượng MLCC trên mỗi máy chủ tăng vọt
→ Cùng lúc đó, nhu cầu từ xEV cũng bùng nổ
→ Không thể tăng cung nhanh — linh kiện cao áp, chịu nhiệt cao,
  độ tin cậy cao cần chu kỳ chứng nhận dài
→ Giá đang bắt đầu tăng

FC-BGA:
→ Chip AI lớn hơn → đế chip lớn hơn
→ Đế lớn hơn → nhiều lớp hơn → tỷ lệ lỗi tăng
   (tỷ lệ đế sản xuất không có khuyết tật giảm xuống)
→ Tấm panel lớn hơn cũng chứa được ít sản phẩm hơn trên mỗi dây chuyền
→ Xây dựng fab đế chip mới từ đầu mất 2–3 năm
→ Nhu cầu tăng ngay bây giờ; nguồn cung mới có ý nghĩa là sự kiện của 2028+
→ Từ nay đến 2027 là "cửa sổ thiếu cung"
```

<strong>Tóm gọn một dòng</strong>: SEMCO không làm chip AI; họ làm <strong>linh kiện nguồn điện và kết nối mà chip AI không thể hoạt động thiếu</strong> — và những linh kiện đó đang thiếu cung ngay hôm nay.

---

## 2. Mổ xẻ ba mảng kinh doanh

### 2.1 Cơ cấu của SEMCO

| Mảng | Sản phẩm chính | Doanh thu 2025 | Tỷ trọng | Lợi nhuận 2025 | Tỷ trọng LN | Biên |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| <strong>Component</strong> | <strong>MLCC, cuộn cảm, điện trở chip</strong> | <strong>5,20 nghìn tỷ KRW</strong> | <strong>46%</strong> | <strong>609,4 tỷ KRW</strong> | <strong>67%</strong> | <strong>11,7%</strong> |
| Package Solution | Đế chip FC-BGA | 2,30 nghìn tỷ KRW | 20% | 135,2 tỷ KRW | 15% | 5,9% |
| Optics | Module camera | 3,81 nghìn tỷ KRW | 34% | 168,7 tỷ KRW | 18% | 4,4% |
| <strong>Tổng</strong> | | <strong>11,31 nghìn tỷ KRW</strong> | <strong>100%</strong> | <strong>913,3 tỷ KRW</strong> | <strong>100%</strong> | <strong>8,1%</strong> |

```
Vai trò của từng mảng trong SEMCO:
Component (MLCC)         = bảo vệ lợi nhuận (67% lợi nhuận hoạt động)
Package Solution (FC-BGA) = dẫn dắt giá cổ phiếu (tăng trưởng +45% YoY)
Optics (camera)          = mở rộng quy mô doanh thu + tiềm năng tương lai
```

---

## 3. Component (MLCC) — con hào lợi nhuận

### 3.1 MLCC là gì?

MLCC = Multi-Layer Ceramic Capacitor (Tụ điện gốm đa lớp). Cái tên nghe kỹ thuật, nhưng nhiệm vụ rất đơn giản — <strong>tích trữ điện trong tích tắc và cấp điện ổn định cho các chip lân cận</strong>.

```
Ví von: bể nước trong hệ thống ống nước

Nếu nước từ vòi chảy lúc mạnh lúc yếu, áp lực sẽ không ổn định.
Bể nước dự trữ một lượng nước và cấp ra đều đặn.

MLCC làm điều tương tự với điện:
Nếu dòng điện dao động, chip sẽ hoạt động sai.
MLCC tạm thời tích điện và cấp ra ổn định.

Kích thước: nhỏ hơn hạt gạo (0,1mm–3mm)
Số lượng: \~1.000 chiếc trong smartphone, hàng chục nghìn chiếc trong máy chủ AI
```

### 3.2 Tại sao MLCC của SEMCO lại quan trọng?

```
Cấu trúc thị trường MLCC:
#1 Murata (Nhật Bản)           \~33% thị phần
#2 Samsung Electro-Mechanics   \~23%
#3 Taiyo Yuden (Nhật Bản)
#4 Yageo (Đài Loan)

→ Bốn tên đầu kiểm soát phần lớn thị trường
→ Rào cản gia nhập cao: hàng trăm lớp gốm dày vài micromet
   phải xếp đều đặn rồi nung ở nhiệt độ cao mà không có lỗi
→ SEMCO nắm giữ công nghệ xếp lớp lên đến 600 tầng

Tại sao MLCC cho máy chủ AI lại đặc biệt khó:
→ Yêu cầu điện áp, điện dung và khả năng chịu nhiệt cao hơn
   so với linh kiện cho điện thoại
→ Chu kỳ chứng nhận dài; lỗi ngoài thực địa có thể làm sập cả máy chủ
→ Danh sách nhà cung cấp được chứng nhận rất hẹp
→ Sự hẹp này chuyển hóa thành sức mạnh định giá và biên lợi nhuận
```

### 3.3 Kết quả 1Q26 và triển vọng

Doanh thu Component trong 1Q26 đạt 1,41 nghìn tỷ KRW (+16% YoY), tỷ lệ sử dụng công suất ở mức 93% (so với 70% của Package và 66% của Optics — cao nhất trong toàn công ty).

Ban lãnh đạo cho biết nhu cầu MLCC cao cấp cho máy chủ AI và trung tâm dữ liệu vẫn mạnh sang quý 2. Cả sản lượng lẫn giá bán bình quân (ASP) của MLCC dự kiến đều tăng so với quý trước.

<strong>Thay đổi quan trọng nhất</strong>: một số dòng sản phẩm MLCC đang <strong>bắt đầu tăng giá</strong>. Murata và Taiyo Yuden ghi nhận tỷ lệ book-to-bill lần lượt là 1,36 và 1,31 — cao nhất trong năm năm (kể từ 2021). "BB > 1" đơn giản là đơn đặt hàng nhiều hơn lượng giao; khoảng cách nay đã đủ lớn để nói về tình trạng thiếu cung thực sự.

---

## 4. Package Solution (FC-BGA) — linh hồn của làn sóng định giá lại

### 4.1 FC-BGA là gì?

FC-BGA = Flip Chip Ball Grid Array — một <strong>đế mạch mật độ cao</strong> kết nối chip AI (GPU, CPU) với bo mạch chủ.

```
Ví von: chỗ đứng của chip

Chip AI nhỏ mà dày đặc, chứa hàng chục tỷ bóng bán dẫn.
Bạn không thể hàn thẳng chip lên bo mạch chủ của máy chủ.
Cần một "chỗ đứng" trung gian để truyền điện và tín hiệu
giữa chip và bo mạch. Chỗ đứng đó chính là đế FC-BGA.

Tại sao khó làm:
→ Chip AI lớn hơn → đế chip lớn hơn
   (đế cho máy chủ có diện tích >4 lần đế PC thông dụng,
   với hơn 20 lớp)
→ Đế lớn hơn bị vênh → chip mất tiếp xúc
→ Nhiều lớp phải căn chỉnh chính xác → tỷ lệ lỗi tăng mạnh
→ Đường mạch phải được khắc ở 5–10 micromet
   (khoảng 1/10 chiều rộng của sợi tóc người)

SEMCO trở thành công ty Hàn Quốc đầu tiên sản xuất hàng loạt
FC-BGA cho máy chủ vào tháng 10 năm 2022. Năm 2025, công ty
công bố quan hệ đối tác cung cấp đế chip trung tâm dữ liệu với AMD.
```

### 4.2 Tại sao đây là "linh hồn của làn sóng định giá lại"

Lý do cổ phiếu SEMCO tăng từ 830.000 lên 1.024.000 KRW chính là Package Solution.

```
Package Solution trong 1Q26:
Doanh thu: 725 tỷ KRW (+45% YoY, +12% QoQ)
Động lực tăng trưởng: FC-BGA cao cấp cho bộ tăng tốc AI, CPU máy chủ,
                      mạng lưới trung tâm dữ liệu

Tại sao thị trường hứng khởi:
1. Khách hàng muốn nhiều hơn công suất hiện tại
   → cầu > cung → quyền định giá thuộc về SEMCO

2. Một khách hàng big-tech mới trao chương trình
   đế mạng trung tâm dữ liệu AI
   → nhiều khách hàng = doanh thu tương lai lớn hơn

3. Đàm phán thỏa thuận dài hạn (LTA) đang diễn ra
   → không phải đột biến một quý — cầu có cấu trúc → mở rộng bội số

4. Ban lãnh đạo báo hiệu capex 2026 có thể tăng gấp đôi so với 2025
   → đầu tư tăng mạnh = tín hiệu tin tưởng rằng nhu cầu là thực
```

### 4.3 Điều chỉ SEMCO làm được

```
Nhà sản xuất đế chip thông thường: chỉ làm FC-BGA
SEMCO: làm cả FC-BGA lẫn MLCC

Tại sao điều này quan trọng:

Máy chủ AI giảm tổn thất điện bằng cách đặt linh kiện
cung cấp điện trực tiếp dưới chip. Điều đó có nghĩa là
chồng lên — hoặc nhúng vào — MLCC trên hoặc trong đế chip.

Vì SEMCO làm được cả hai, họ có thể phát triển
tích hợp "MLCC trong đế chip" ngay nội bộ.

Murata (chỉ MLCC) và Ibiden (chỉ đế chip) không thể làm điều này
trong nhà máy của mình.

→ Năng lực kép này có thể là con hào bền vững nhất của SEMCO dài hạn.
```

### 4.4 Điều chưa được chứng minh

Biên lợi nhuận hoạt động của Package Solution năm 2025 <strong>chỉ đạt 5,9%</strong>. Doanh thu tăng +13% YoY nhưng lợi nhuận giảm -14%. Nguyên nhân? Chi phí nguyên liệu thô (CCL, prepreg) tăng +19% trong khi giá bán bình quân chỉ tăng +4%.

<strong>Câu hỏi then chốt: trong năm 2026, liệu tăng trưởng doanh thu có đi kèm phục hồi biên lợi nhuận không?</strong> Nếu chỉ có doanh thu tăng còn biên lợi nhuận dậm chân, mức giá hiện tại khó có thể bào chữa được. Liệu biên lợi nhuận Package Solution trong quý 2 có vượt 12% hay không chính là cửa ải lớn nhất để làn sóng định giá lại tiếp tục.

---

## 5. Optics (module camera) — doanh thu lớn, không phải nhân vật chính

Optics là mảng kinh doanh module camera cho smartphone và ô tô của SEMCO. Doanh thu 2025 đạt 3,81 nghìn tỷ KRW (34% toàn công ty), biên lợi nhuận 4,4%.

```
Thực trạng:
→ Doanh thu lớn (một phần ba toàn công ty)
→ Biên lợi nhuận thấp nhất trong danh mục (4,4%)
→ Nhạy cảm với chu kỳ smartphone cao cấp
→ Không phải nhân vật chính của làn sóng định giá lại

Tiềm năng tương lai:
→ Camera ADAS cho xe điện (số lượng camera trên mỗi xe đang tăng)
→ Camera giám sát lái xe trong cabin
→ Camera thị giác cho robot và humanoid
→ Ban lãnh đạo đề cập đến kế hoạch ra mắt sản phẩm cho robotaxi từ quý 2

Thị phần hiện tại: \~9% (giảm từ \~11% năm 2024)
→ Công nghệ thực sự, nhưng không phải luận điểm định giá lại
```

<strong>Góc nhìn nhà đầu tư</strong>: Optics bổ sung sự ổn định doanh thu nhưng không dẫn dắt giá cổ phiếu. MLCC và FC-BGA mới là thứ làm điều đó. Camera cho ô tô và robot là những quyền chọn dài hạn — không phải thứ đáng trả tiền ở bội số hiện tại.

---

## 6. Định giá — đã đắt, nhưng có lý do

### 6.1 Cổ phiếu đang ở đâu

Tính đến ngày 15/5, giá 1.024.000 KRW/cổ phiếu, vốn hóa thị trường \~76,5 nghìn tỷ KRW. Tăng +23% từ cuối tháng Tư.

| Tham chiếu | PER | Đọc |
| --- | ---: | --- |
| 12 tháng trailing | \~110x | Đắt về mặt quang học |
| Ước tính 2026 | \~58x | Khi phản ánh phục hồi lợi nhuận, thấp hơn |
| Ước tính 2027 | \~38x | Chỉ hợp lý nếu chu kỳ đế chip AI chạy đến 2027 |

### 6.2 Giá mục tiêu của môi giới đã chạy nhanh

```
Tháng 2  : Samsung Sec     1.450.000 KRW (theo BPS 2027)
Tháng 3  : Hana Sec        550.000 KRW (EPS 2026 × 37,5x)
Đầu tháng 4: SK Sec        600.000 KRW (PER peer toàn cầu 40x)
Giữa tháng 4: Hana Sec     810.000 KRW (EPS 2027 × 35x)
Đầu tháng 5: Hana Sec    1.000.000 KRW (EPS 2027 × 40x)
Giữa tháng 5: KB Sec      1.400.000 KRW
              NH IB / SK Sec 1.500.000 KRW

→ Giá mục tiêu đã tăng hơn gấp ba chỉ trong khoảng ba tháng.
```

<strong>Tại sao nhanh đến vậy?</strong> Chính khung định giá đã thay đổi. SEMCO từng được giao dịch như "nhà sản xuất linh kiện điện tử Hàn Quốc." Ngày nay, phía môi giới đặt chuẩn so sánh với <strong>các peer đế chip và linh kiện thụ động toàn cầu</strong> — Ibiden (Nhật), Unimicron (Đài Loan), Murata (Nhật). Áp dụng các bội số đó, giá mục tiêu nhảy vọt.

### 6.3 Giá trị hợp lý theo kịch bản

| Kịch bản | EPS 2027E | PER áp dụng | Giá trị hợp lý | So với giá hiện tại |
| --- | ---: | ---: | ---: | ---: |
| Xấu (tăng giá MLCC bị kiềm chế, capex FC-BGA gây áp lực) | 22.000 KRW | 33x | 730.000 KRW | -29% |
| <strong>Cơ sở</strong> (chu kỳ AI tiếp tục + biên Package phục hồi) | <strong>26.800 KRW</strong> | <strong>43x</strong> | <strong>1.150.000 KRW</strong> | <strong>+12%</strong> |
| Tốt (tăng giá cả MLCC + FC-BGA cùng lúc + LTA) | 30.000 KRW | 50x | 1.500.000 KRW | +47% |

<strong>Ở mức giá 1,02 triệu KRW hiện tại, kịch bản cơ sở cho mức tăng +12%</strong> — và -29% nếu kịch bản xấu xảy ra, +47% nếu kịch bản tốt thành hiện thực. Ở mức giá này, chờ xác nhận từ kết quả kinh doanh tiếp theo hợp lý hơn là chạy theo đà tăng.

### 6.4 Khung tư duy quan trọng: không phải "rẻ," mà là "đắt nếu thiếu nâng ước tính liên tục"

```
SEMCO đang ở đâu ngày hôm nay:
"Đây có phải công ty tốt không?"    → Có
"Cổ phiếu có rẻ không?"             → Không
"Vậy thì không nên mua?"            → Không hẳn — có điều kiện

Các điều kiện:
→ Lợi nhuận hoạt động 2Q vượt 400 tỷ KRW (so với đồng thuận 378,8 tỷ KRW)
→ Tăng giá MLCC lan từ nhà phân phối sang khách hàng trực tiếp
→ Biên lợi nhuận Package Solution vượt 12%
→ LTA hoặc đầu tư trước từ khách hàng được chính thức hóa

Đáp ứng hai trong số này = luận điểm mua ở mức giá hiện tại còn hợp lệ.
Không đáp ứng điều nào = chờ giá giảm là quyết định đúng.
```

---

## 7. Những gì cần theo dõi từ đây

### 7.1 Yếu tố kích hoạt từ kết quả kinh doanh

| Yếu tố | Ngưỡng tích cực | Ngưỡng tiêu cực | Thời điểm |
| --- | --- | --- | --- |
| <strong>Lợi nhuận hoạt động 2Q</strong> | <strong>Vượt 400 tỷ KRW</strong> | Dưới 360 tỷ KRW | Cuối tháng 7 |
| Tăng giá MLCC | Lan sang khách hàng AI trực tiếp | Chỉ dừng ở pass-through chi phí | 2Q |
| Tỷ lệ sử dụng FC-BGA | Full công suất trong 2H | Khách hàng mới triển khai chậm | 3Q |
| Biên Package Solution | 12%+ trong 2Q | Dưới 10% | Cuối tháng 7 |
| Tồn kho kênh MLCC | \~4 tuần (thắt chặt) | 6+ tuần (nới lỏng) | Hàng quý |

### 7.2 Yếu tố kích hoạt từ bội số định giá

| Yếu tố | Tại sao quan trọng |
| --- | --- |
| Capex hạ tầng AI duy trì ổn định | Nhu cầu đầu cuối cho cả FC-BGA lẫn MLCC |
| Thỏa thuận dài hạn (LTA) với khách hàng | Chứng minh "không phải nhất thời" — cầu có cấu trúc |
| Tỷ lệ BB của Murata / Taiyo Yuden | Chỉ số dẫn đầu chu kỳ MLCC (cao nhất 5 năm hiện nay) |
| Kế hoạch công suất đế chip toàn cầu | Tình trạng thiếu cung kéo dài bao lâu |
| Liên doanh đế Glass Core | Lựa chọn đóng gói thế hệ tiếp theo (2027+) |

### 7.3 Rủi ro cần theo dõi

| Rủi ro | Mô tả |
| --- | --- |
| <strong>Đã đắt</strong> | PER 2027 \~38x. Nếu ước tính lợi nhuận bị hạ, cổ phiếu sẽ giảm mạnh |
| Gánh nặng capex FC-BGA | Capex tăng gấp đôi → khấu hao tăng gấp đôi; doanh thu phải theo kịp hoặc biên sẽ bị siết |
| Thất bại pass-through | Nếu lạm phát CCL, vàng, đồng không chuyển được vào giá bán, biên lợi nhuận chịu thiệt |
| Smartphone yếu | Module camera và một số SKU MLCC vẫn phụ thuộc chu kỳ điện thoại |
| Đỉnh capex AI | Nếu đầu tư máy chủ AI giảm tốc, nền cầu FC-BGA + MLCC suy yếu |

---

## 8. Kết nối với các bài viết khác

```
Bài về Samsung Electronics: "HBM là bàn làm việc của máy chủ AI"
→ SEMCO: "MLCC là bộ ổn định điện, FC-BGA là chỗ đứng của chip"

Bài về Jeju Semiconductor: "DRAM hàng hóa thiếu cung vì AI"
→ SEMCO: "Linh kiện nguồn điện và đế chip thiếu cung vì AI"

Bài về chuỗi giá trị robot: "Phần 1 đã ghi nhận SEMCO
đang ra mắt camera humanoid trong 2H"
→ SEMCO: kế hoạch đó nằm trong nhóm tiềm năng tương lai của Optics

Cả ba đều dựa trên cùng một logic:
Capex AI → thiếu cung linh kiện, vật liệu, đế chip →
quyền định giá thuộc về nhà cung cấp tắc nghẽn.
```

---

## 9. Kết luận một dòng

SEMCO là lớp hạ tầng vô hình của AI silicon. MLCC ổn định nguồn điện; FC-BGA kết nối chip với bo mạch. Cả hai đều thiếu cung. Giá MLCC đã bắt đầu tăng; cầu FC-BGA đã vượt qua công suất. Nếu cấu trúc này kéo dài đến 2027, SEMCO sẽ được định giá lại từ "nhà sản xuất linh kiện smartphone" thành "nền tảng linh kiện hạ tầng AI."

Nhưng ở mức giá 1,02 triệu KRW, phần lớn luận điểm đó đã được phản ánh vào giá. Tính theo lợi nhuận 2027, PER là \~38x — "công ty tốt" và "giá vào hàng tốt" là hai câu hỏi khác nhau. Để chạy theo đà tăng từ đây, con số phải xác nhận: lợi nhuận hoạt động 2Q vượt 400 tỷ KRW, tăng giá MLCC lan rộng, biên FC-BGA phục hồi.

<strong>Một dòng: đây không phải cổ phiếu rẻ — đây là cổ phiếu chỉ "không đắt" nếu nâng ước tính lợi nhuận tiếp tục diễn ra.</strong> Tốc độ điều chỉnh quan trọng hơn luồng tin tức tiêu đề.

---

*Bài viết này chỉ mang tính nghiên cứu và bình luận, không phải tư vấn đầu tư. Các số liệu doanh thu và lợi nhuận theo mảng dựa trên báo cáo thường niên 2025 và công bố kết quả 1Q26 của Samsung Electro-Mechanics. Lợi nhuận hoạt động 1Q26 là 280,6 tỷ KRW bao gồm khoản chi trả thôi việc một lần 71,4 tỷ KRW. Số liệu tỷ lệ sử dụng công suất (Component 93%, Package 70%, Optics 66%) là mức bình quân cả năm 2025. Thị phần MLCC \~23% là ước tính của chính công ty. Quan hệ đối tác đế chip với AMD dựa trên công bố chính thức của SEMCO. Tên khách hàng big-tech mới chưa được tiết lộ công khai. Các kịch bản định giá (Cơ sở 1,15 triệu KRW, Tốt 1,50 triệu KRW, Xấu 730.000 KRW) là ước tính của tác giả và có thể sai. Giá mục tiêu của môi giới (NH / SK 1,5 triệu KRW, KB 1,4 triệu KRW, Hana 1,0 triệu KRW, v.v.) phản ánh báo cáo của từng nhà môi giới và có thể thay đổi. Sản xuất hàng loạt liên doanh đế Glass Core là kế hoạch 2027+ và chưa được xác nhận. Tăng giá MLCC đang ở giai đoạn đầu trong một số kênh phân phối chọn lọc; pass-through rộng rãi hơn chưa được xác nhận. Phân tích có thể sai. Dữ liệu chốt đến ngày 15/5/2026 giờ KST.*

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
