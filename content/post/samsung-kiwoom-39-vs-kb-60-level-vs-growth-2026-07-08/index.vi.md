---
title: "Samsung: 390k của Kiwoom vs 600k của KB, qua các con số — 'mức' và 'tốc độ tăng' không mâu thuẫn (2026-07-08)"
slug: samsung-kiwoom-39-vs-kb-60-level-vs-growth-2026-07-08
date: 2026-07-08T09:30:00+09:00
description: "Cùng một ngày, Kiwoom hạ mục tiêu Samsung xuống 390.000 KRW còn KB nâng lên 600.000. Trông có vẻ mâu thuẫn, nhưng qua các con số chúng không bác bỏ nhau. Kiwoom nói về sự giảm tốc của TỐC ĐỘ tăng lợi nhuận (đạo hàm bậc hai); KB nói về MỨC tuyệt đối. Cả hai đều đúng. Mấu chốt là cách điều chỉnh dự phòng — trong tổng dự phòng thưởng nằm trong OP báo cáo Q2 là 89,4 nghìn tỷ, chỉ ~5 nghìn tỷ KRW là thực sự một lần (một khoản truy hồi của Q1; dự phòng vẫn có trong Q3), và khi chỉ chuẩn hóa phần đó, QoQ của Q3 gần +16–19%, không phải +26% hay +4,7%. Sự giảm tốc từ Q2 sang Q3 theo TrendForce, và P/E 2026E ~6,7x tại giá đóng cửa 296.000 KRW — bài này giảm tối đa phán xét mua/bán và mổ xẻ lập luận và dữ liệu của cả hai báo cáo."
categories: ["Sector-Deep-Dive", "한국 시장"]
tags:
  - "Samsung Electronics"
  - "bán dẫn"
  - "bộ nhớ"
  - "HBM"
  - "DRAM"
  - "NAND"
  - "Kiwoom"
  - "KB Securities"
  - "ASP"
  - "bộ nhớ AI"
  - "định giá"
  - "cổ phiếu Hàn Quốc"
---

> 🔗 **Đọc cùng**: [Nhu cầu token của Goldman vs đỉnh ASP của JPMorgan — hai dự báo có thực sự mâu thuẫn?](/post/goldman-token-demand-vs-jpm-memory-asp-peakout-korea-semiconductor-2026-05-31/) · [Samsung Electronics: cổ phiếu đầu tàu bộ nhớ AI của Hàn Quốc (phân tích sâu)](/post/kr-deep-dive-samsung-electronics-2026-07-07/) · [Cuộc đua huy động vốn của big tech — CapEx AI chưa hề co lại](/post/hyperscaler-financing-race-ai-capex-memory-bottleneck-2026-07-07/) · [IPO của CXMT — tách rủi ro HBM khỏi rủi ro DRAM khách hàng](/post/cxmt-ipo-memory-price-risk-hbm-client-dram-2026-06-21/)

*Cùng một buổi sáng, Kiwoom hạ giá mục tiêu Samsung xuống 390.000 KRW còn KB nâng lên 600.000. Trông như một cú va chạm trực diện. Nhưng khi mổ xẻ cả hai báo cáo qua các con số, chúng không bác bỏ nhau. Chúng đang sờ vào những phần khác nhau của cùng một con voi. Bài này giảm tối đa phán xét "ai đúng" và tập trung mổ xẻ những gì mỗi báo cáo thực sự lập luận — lý lẽ và con số của nó.*

---

## TL;DR

* **Kiwoom nói về sự giảm tốc của tốc độ tăng (dG/dt, đạo hàm bậc hai); KB nói về mức tuyệt đối của lợi nhuận.** Chúng cùng tồn tại về mặt toán học, và trong các con số đã cho, cả hai đều đúng. Khung "báo cáo đối lập" tự nó là một sự đặt vấn đề sai.
* **Tất cả phụ thuộc vào cách điều chỉnh dự phòng.** Dự phòng thưởng trong OP báo cáo Q2 là 89,4 nghìn tỷ tổng khoảng 17,6 nghìn tỷ, nhưng phần thực sự **một lần** chỉ là khoản truy hồi **\~5 nghìn tỷ** cho phần Q1 thiếu trích (phần còn lại lặp lại mỗi quý, kể cả Q3). Chỉ chuẩn hóa 5 nghìn tỷ đó thì QoQ Q3 không phải tiêu đề +26% cũng không phải +4,7% khi bỏ toàn bộ dự phòng, mà là **\~+16–19%**. Gia tốc tăng chậm lại (đúng hướng Kiwoom) nhưng không sụp đổ (mức của KB vẫn đứng).
* **Thị trường đã trả lời.** Ngay sau một quý kỷ lục, cổ phiếu rơi mạnh và một ngắt mạch (circuit breaker) đã kích hoạt. Cái thị trường định giá không phải là sự sụp đổ nhu cầu mà là **đỉnh của tốc độ tăng + trạng thái vị thế cực đoan**.

---

## 1. Mỗi báo cáo thực sự nói gì

Sự thật trước. Các bài đưa tin liên quan của cả hai báo cáo đã được kiểm chứng, và các con số dưới đây theo cơ sở báo chí/công bố của công ty. Dù vậy, **bản PDF gốc đầy đủ ngày 2026-07-08 của cả hai công ty chứng khoán (kèm bảng định giá chi tiết) không lấy được trực tiếp.** Phần đó không chắc chắn và để trong [Blocked] bên dưới.

| Mục | Kiwoom | KB Securities |
|---|---|---|
| Giá mục tiêu | 430k → **390k KRW** (hạ) | 550k → **600k KRW** (nâng) |
| Khuyến nghị | Duy trì Mua | Mua |
| Khung cốt lõi | **tốc độ** tăng lợi nhuận nửa cuối chậm lại | **mức** lợi nhuận / độ bền của nhu cầu AI |
| Ước tính OP Q3 | \~**112 nghìn tỷ KRW** | \~**110 nghìn tỷ KRW** |
| Cơ sở | tăng giá PC/điện thoại → lo ngại nhu cầu → OEM mua bộ nhớ thận trọng hơn | mở rộng CapEx AI, thiếu hụt đến nửa đầu 2028, hợp đồng dài hạn |

Một sự thật nổi bật ngay. **Ước tính OP Q3 của họ về cơ bản giống nhau — 112 vs 110 nghìn tỷ**, và cả hai khớp đồng thuận (\~111 nghìn tỷ). Vậy Kiwoom không hạ "mức" lợi nhuận. Cái nó hạ là **bội số** áp vào giá mục tiêu. Điều đó định nghĩa bản chất cuộc tranh luận — **đây là tranh luận về P/E, không phải EPS.**

Cái KB thêm vào trên mức lợi nhuận là một tập hợp quyền chọn: quy mô đầu tư AI toàn cầu (\~800 tỷ USD năm nay → 1,1 nghìn tỷ năm sau → 1,5 nghìn tỷ năm 2028), thiếu hụt đến nửa đầu 2028, đàm phán giá HBM 2027, mua lại/hủy cổ phiếu và cổ tức đặc biệt, khả năng có hợp đồng đúc mới, và việc xem xét niêm yết ADR. Nhiều thứ trong số này vẫn là **quyền chọn sự kiện hoặc ước tính**, và cần tách khỏi sự thật đã xác nhận.

## 2. Mức vs tốc độ tăng — tất cả nằm ở cách điều chỉnh dự phòng

Một cổ phiếu giao dịch tốc độ thay đổi của lợi nhuận, không phải mức. Nên "lợi nhuận kỷ lục (mức)" và "sự giảm tốc của gia tốc tăng (tốc độ)" có thể cùng đúng. Nhưng có một cái bẫy phổ biến khi thể hiện điều này bằng con số: **cách bạn điều chỉnh dự phòng thưởng.**

Trên cơ sở KB, OP điều chỉnh (trừ dự phòng thưởng) Q2 là **107 nghìn tỷ** và OP báo cáo (kèm dự phòng) là **89,4 nghìn tỷ**. Chênh lệch khoảng **17,6 nghìn tỷ** là tổng dự phòng thưởng ghi nhận trong Q2.

Đây là điểm đính chính then chốt. **Không được bỏ toàn bộ 17,6 nghìn tỷ đó như "một lần."** Dự phòng thưởng gắn với lợi nhuận và được ghi nhận mỗi quý — **kết quả Q3 cũng sẽ mang dự phòng.** Phần thực sự một lần của Q2 là khoản truy hồi: phần thưởng bị trích thiếu ở Q1 so với lợi nhuận của nó, được ghi nhận muộn vào Q2. Khoản truy hồi này ước tính khoảng **5 nghìn tỷ KRW, theo tỷ lệ với OP Q1 (\~57 nghìn tỷ)** (89,4 nghìn tỷ của Q2 ≈ +56% so với Q1).

Vì vậy khi chuẩn hóa nền, bạn chỉ cộng lại khoản **một lần \~5 nghìn tỷ**, không phải 17,6 nghìn tỷ — giữ nguyên dự phòng bình thường của từng quý.

* **OP chuẩn hóa Q2 ≈ 89,4 + 5 = \~94 nghìn tỷ**
* **OP ước tính Q3 ≈ 110–112 nghìn tỷ** (khoản này cũng gồm dự phòng bình thường)
* **QoQ Q3 chuẩn hóa ≈ 112 ÷ 94 ≈ +18%** (khoảng +16% trên 110) → **\~+16–19%**

Đặt ba con số cạnh nhau, ảo giác lộ ra:

* **Tiêu đề "Q3 +26%"** — dùng báo cáo Q2 bị dự phòng đè xuống (89,4) làm mẫu số, phóng đại gia tốc.
* **+4,7% nếu bỏ toàn bộ 17,6 nghìn tỷ** — một so sánh bất đối xứng, bỏ dự phòng Q2 nhưng giữ dự phòng Q3, nên ngược lại đánh giá thấp tăng trưởng.
* **\~+16–19% sau khi chỉ chuẩn hóa khoản một lần (\~5 nghìn tỷ)** — đây là gần thực tế nhất.

Tóm lại: **mức lợi nhuận là kỷ lục (KB đúng).** Gia tốc tăng có chậm lại từ nhịp cực đoan của Q2 (hướng của Kiwoom đúng). Nhưng sự chậm lại đó không phải một vách đứng ở Q3; đó là một **đường cong dần dần** — Q2 (bùng nổ) → Q3 (\~+16–19%) → Q4 (124 ÷ 112 ≈ +10,7%). Hai báo cáo không mâu thuẫn; chúng **nhìn vào các đạo hàm khác nhau (mức vs tốc độ thay đổi) của cùng một đường cong lợi nhuận**, và sự giảm tốc nhẹ hơn nhiều so với phép tính "bỏ toàn bộ dự phòng".

## 3. Dữ liệu thị trường in ra ngày 7 tháng 7

Thực ra cuộc tranh luận đã được thị trường phân xử sớm một ngày. **Ngày 7 tháng 7, khi Samsung báo cáo quý kỷ lục (OP sơ bộ Q2 89,4 nghìn tỷ), cổ phiếu rơi mạnh — hơn \~5% — về vùng 300.000 KRW, và ngắt mạch lần thứ 6 của năm kích hoạt.** Dữ liệu dòng tiền trong các bài đưa tin liên quan giải thích bối cảnh.

* **Tỷ lệ sở hữu nước ngoài đã rơi xuống mức thấp nhất 17 năm**, cộng thêm việc khối ngoại chốt lời quy mô lớn.
* **Dư nợ ký quỹ của nhà đầu tư cá nhân ở mức cao kỷ lục**, khiến vị thế lệch cực đoan về một phía.
* Cùng lúc, **rủi ro địa chính trị quanh eo biển Hormuz (đòn tấn công của CENTCOM Mỹ vào Iran) đẩy giá dầu vọt lên**, và cổ phiếu bán dẫn Mỹ giảm theo.

Thông điệp rõ ràng. Thị trường chưa bao giờ định giá một sự sụp đổ nhu cầu AI. Một ngắt mạch trên lợi nhuận kỷ lục cho thấy cái thị trường giao dịch không phải "mức" lợi nhuận mà là **đỉnh của gia tốc tăng cộng với việc giải tỏa vị thế cực đoan, đông đúc**. Nếu vậy, lời phản bác "lo ngại AI chỉ là tiếng ồn" nhắm vào thứ mà thị trường không lo (sụp đổ nhu cầu).

## 4. Dữ liệu giá — ASP vẫn tăng, nhưng độ dốc bẻ cong

Cơ sở dữ liệu ngành cho lập luận của Kiwoom là **sự chậm lại của mức tăng giá hợp đồng bộ nhớ**. Điểm phân biệt thiết yếu: tốc độ tăng chậm hơn không phải là giá giảm. Trên cơ sở TrendForce, mức tăng giá hợp đồng được nêu như sau.

| Kỳ | Mức tăng giá HĐ DRAM phổ thông | Mức tăng NAND Flash |
|---|---|---|
| Q2 (QoQ) | **+58\~63%** | **+70\~75%** |
| Q3 (QoQ) | **+13\~18%** | **+10\~15%** |

Vậy giá **vẫn tăng trong Q3** — nhưng độ dốc giảm mạnh, từ cú tăng vọt Q2 xuống mức trên dưới 10 mấy phần trăm. Câu của Kiwoom rằng "mức tăng giá nửa cuối khó vượt kỳ vọng thêm một biên độ lớn" nên đọc không phải là kết thúc chu kỳ, mà là **thu hẹp biên độ vượt kỳ vọng**. Dữ liệu này khớp về hướng với sự giảm tốc dần của tốc độ tăng ở Mục 2 (Q3 \~+16–19%).

## 5. Định giá là chuyện P/E, không phải EPS

Khoảng cách giữa mục tiêu 390k và 600k không phải chênh lệch ước tính lợi nhuận mà là **bội số áp dụng (P/E)**. Cắm giá đóng cửa 296.000 KRW và EPS 2026E có thể kiểm chứng vào một phép tính nhanh (EPS: Kiwoom 43.429 / KB 44.379, xấp xỉ 44.000):

* **Hiện tại 296.000 ÷ EPS 2026E \~44.000 ≈ P/E 6,7x**
* **Mục tiêu Kiwoom 390.000 ÷ 44.000 ≈ 8,9x**
* **Mục tiêu KB 600.000 ÷ 44.000 ≈ 13,6x**
* **Mục tiêu KB 600.000 ÷ EPS 2027E 58.361 ≈ 10,3x**

Cấu trúc các con số cho thấy: Samsung giao dịch quanh **6–7x trên lợi nhuận 2026**. Về mặt tuyệt đối là thấp. Nhưng cổ phiếu bộ nhớ hầu như luôn trông rẻ khi EPS đỉnh đã hiện. Con số 390k áp khoảng 9x lên lợi nhuận 2026 — gần một **bội số neo vào kết quả hiện có thể kiểm chứng** — còn 600k giả định một **tái định giá lên bội số cao hơn** chỉ đứng vững nếu chấp nhận độ bền lợi nhuận 2027. Nói cách khác, nút thắt của cuộc tranh luận không phải bản thân lợi nhuận, mà là **khi nào P/E thấp bị phá vỡ (tức bằng chứng về độ bền lợi nhuận).**

## 6. Vì sao Q, không phải P, mới là trục thật — sự phân đôi nhu cầu bộ nhớ

Cuộc tranh luận chủ yếu xoay quanh giá (P), nhưng biến thật mà Kiwoom gieo là sản lượng (Q). Cốt lõi cơ chế của Kiwoom là: "tăng giá linh kiện → tăng giá bộ thiết bị (PC/điện thoại) → lo ngại nhu cầu → thay đổi trong cách OEM mua bộ nhớ". Hiện vẫn ở giai đoạn **kháng giá**; câu hỏi là liệu điều đó có chuyển thành **cắt giảm sản lượng đặt hàng** thực sự.

Sự phân tách thiết yếu là nhu cầu bộ nhớ không phải một đường cong duy nhất.

* **Bộ nhớ tiêu dùng (DRAM/NAND di động/PC): co giãn.** Khi giá thiết bị tăng, nhu cầu thiết bị giảm; đây là nơi sản lượng lung lay trước.
* **Bộ nhớ AI (HBM, DRAM máy chủ, eSSD; nhu cầu hyperscaler): tương đối kém co giãn.** Một đường cầu riêng gắn với CapEx trung tâm dữ liệu.

Sự phân đôi này quan trọng vì **dù sản lượng tiêu dùng bị cắt trước, một tỷ trọng sản phẩm AI giá trị cao tăng lên có thể bù lại, nên ASP và biên gộp trộn có thể còn cải thiện.** Nghĩa là phần tiêu dùng trong nỗi lo của Kiwoom và phần AI trong luận điểm tăng của KB có thể cùng đúng, và kết quả thực do tốc độ tương đối của chúng quyết định. Trục thật của cuộc tranh luận không phải "giá có tăng không" mà là **"độ kém co giãn của nhu cầu HBM/máy chủ từ hyperscaler có giữ được không."**

## 7. Vậy nên theo dõi gì (các điểm kiểm tra dữ liệu)

Hơn cả một phán xét, điều quan trọng là **dữ liệu** sẽ xác nhận hoặc lật ngược lập luận trên. Khi tin ra, chỉ theo dõi các con số này.

* **Độ dốc ASP:** mức tăng giá hợp đồng DRAM/NAND Q3 có giữ trong dải TrendForce (DRAM +13\~18%, NAND +10\~15%) không; có tín hiệu giảm giá Q4 không?
* **Sản lượng đặt hàng (Q):** **sản lượng đặt hàng** bộ nhớ của OEM PC/điện thoại có vượt kháng giá thành cắt giảm thực sự không?
* **CapEx hyperscaler:** tại các earnings call big tech cuối tháng 7, hướng dẫn CapEx AI có được giữ, hay bị cắt tuyệt đối?
* **Thị phần HBM4:** thị phần HBM4/eSSD của Samsung có thực sự mở rộng không (đặc biệt thị phần sản lượng ở Nvidia)?
* **Nguồn cung Trung Quốc:** sự thâm nhập DRAM legacy và máy chủ của CXMT/YMTC có làm xói mòn cơ cấu sản phẩm không?
* **Khoản một lần / chính sách vốn:** kết quả cuối Q2 theo bộ phận và quy mô dự phòng thưởng chính xác; việc chính thức hóa mua lại/hủy cổ phiếu, cổ tức đặc biệt, ADR.

## 8. Tóm lại

Bản chất cuộc tranh luận không phải va chạm tăng-giảm mà là một **ảo giác trục thời gian**. KB đúng ở mức lợi nhuận, Kiwoom đúng ở tốc độ tăng, và vì thị trường giao dịch tốc độ tăng, giá ngắn hạn phản ứng với câu của Kiwoom trước — ngắt mạch trên lợi nhuận kỷ lục là dữ liệu đó. Đồng thời, nếu cơ sở về mức của KB (thiếu hụt đến 2028) là thật, cú rơi này nhiều khả năng là một đợt điều chỉnh trong chu kỳ hơn là đỉnh của nó. Cuối cùng, cái phân định giai đoạn tới không phải con số giá mục tiêu, mà hai dữ liệu quan sát được: **liệu kháng giá tiêu dùng có chuyển thành cắt giảm sản lượng đặt hàng, và liệu độ kém co giãn của nhu cầu máy chủ AI có giữ được.**

---

## Phân loại bằng chứng (Phụ lục)

### [Fact]
* Kiwoom: mục tiêu hạ 430k→390k, duy trì Mua, OP Q3 \~112 nghìn tỷ (khớp đồng thuận \~111 nghìn tỷ). (báo Hankyung)
* KB: mục tiêu nâng 550k→600k, OP Q3 \~110 nghìn tỷ, OP nửa cuối 234 nghìn tỷ (Q3 110 · Q4 124), OP điều chỉnh Q2 107 nghìn tỷ vs báo cáo 89,4. (báo Etoday)
* OP sơ bộ Q2 của Samsung 89,4 nghìn tỷ là công bố của công ty. Rơi mạnh ngay sau kỷ lục ngày 7/7; ngắt mạch lần thứ 6 của năm. (đưa tin liên quan)
* TrendForce: Q2 DRAM phổ thông +58\~63% / NAND +70\~75%; Q3 DRAM +13\~18% / NAND +10\~15%.
* EPS 2026E có thể kiểm chứng: Kiwoom 43.429 / KB 44.379; giá đóng cửa trước 296.000.

### [Inference]
* Dự phòng thưởng trong Q2 báo cáo 89,4 tổng ≈17,6, nhưng chỉ \~5 là thực sự một lần (khoản truy hồi Q1, theo tỷ lệ OP Q1 \~57). Vì dự phòng cũng lặp lại ở Q3, bỏ toàn bộ 17,6 là so sánh bất đối xứng. Chỉ chuẩn hóa khoản một lần \~5 thì nền Q2 ≈94 và QoQ Q3 ≈ +16–19% (tiêu đề +26%; +4,7% nếu bỏ hết), Q4 ≈ +10,7%.
* Gia tốc tăng chậm lại dần: Q2 (bùng nổ) → Q3 (+16–19%) → Q4 (+10,7%). Luận điểm giảm tốc của Kiwoom đúng hướng nhưng nhẹ hơn ảo giác bỏ toàn bộ dự phòng.
* Trục thật là P/E, không phải EPS (nay \~6,7x → 390k ≈ 8,9x, 600k ≈ 13,6x trên 2026E / 10,3x trên 2027E).
* Nhu cầu bộ nhớ phân đôi thành tiêu dùng (co giãn) và AI (kém co giãn); cắt sản lượng tiêu dùng có thể được bù nếu cơ cấu AI cải thiện biên trộn.
* Cú rơi 7/7 đọc như đỉnh tốc độ tăng + giải tỏa vị thế cực đoan (ngoại thấp nhất 17 năm, ký quỹ cá nhân kỷ lục), không phải sụp đổ nhu cầu.

### [Speculation]
* Giá HBM 2027 gấp 2 lần so cùng kỳ (góc nhìn đàm phán của KB).
* Khả năng hợp đồng đúc mới, xem xét niêm yết ADR, cổ tức đặc biệt/mua lại (KB, quyền chọn sự kiện chưa xác nhận).
* Leo thang ở Hormuz như một kích hoạt vĩ mô khuếch đại việc giải tỏa vị thế mua đông đúc.

### [Blocked]
* Bản PDF gốc đầy đủ của Kiwoom/KB ngày 2026-07-08 và bảng định giá chi tiết.
* Kết quả cuối Q2 của Samsung theo bộ phận và quy mô dự phòng thưởng chính xác.
* Việc Samsung có chính thức theo đuổi ADR, cổ tức đặc biệt, hay hợp đồng đúc lớn mới hay không.
* Con số thị phần sản lượng HBM4 thực tế ở Nvidia.

*Nguồn: công bố chính thức của Samsung, báo Hankyung và Etoday, dự báo giá hợp đồng của TrendForce, các báo cáo công ty chứng khoán có thể kiểm chứng. Các mục không lấy được PDF gốc được đánh dấu [Blocked].*

---

*이 글은 리서치·정보 제공용이며 투자 조언이 아닙니다. 종목명은 분석을 위한 예시이며, 매수·매도 권유가 아닙니다. 본문의 주가·목표주가·이익 추정·EPS·PER은 보도 및 각 증권사·회사 발표 기준이고, 집계 기준·시점에 따라 값이 다를 수 있습니다. 데이터 기준일: 2026년 7월 8일 KST.*

*Tuyên bố miễn trừ: Chỉ nhằm mục đích nghiên cứu và thông tin. Không phải lời khuyên đầu tư. Tên công ty và công ty chứng khoán được nêu để minh họa phân tích. Giá, giá mục tiêu, ước tính lợi nhuận, EPS và P/E dựa trên báo chí và công bố của công ty/công ty chứng khoán, có thể khác nhau theo nguồn và thời điểm; các mục chưa kiểm chứng được đánh dấu [Speculation]/[Blocked]. Dữ liệu tính đến ngày 8 tháng 7 năm 2026 (KST).*
