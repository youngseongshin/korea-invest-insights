---
title: "Nhu cầu token của Goldman và đỉnh ASP bộ nhớ của J.P. Morgan: hai dự báo có thực sự mâu thuẫn?"
slug: "goldman-token-demand-vs-jpm-memory-asp-peakout-korea-semiconductor-2026-05-31"
date: 2026-05-31T11:00:00+09:00
description: "Goldman Sachs cho rằng các tác nhân AI sẽ nâng lượng token lên 24 lần đến năm 2030 trong khi chi phí trên mỗi token giảm 60-70% mỗi năm. J.P. Morgan cho rằng mức tăng so với cùng kỳ của ASP DRAM và NAND sẽ chững lại từ năm 2027. Tách hai dự báo tưởng chừng đối lập thành P, Q và C, một lộ trình nhất quán hiện ra: alpha dịch chuyển khỏi beta bộ nhớ năm 2026 sang ngăn xếp cắt giảm chi phí token sau năm 2027."
categories: ["Korea Market", "Sector-Deep-Dive", "AI Infrastructure"]
tags:
  - "삼성전자"
  - "SK하이닉스"
  - "HBM"
  - "메모리 ASP"
  - "eSSD"
  - "AI 토큰"
  - "추론비용"
  - "Goldman Sachs"
  - "J.P. Morgan"
  - "AI 인프라"
  - "Research OS"
series: ["Korea Market Regime"]
draft: false
---

> Bài viết này là phần tiếp theo của [Hợp đồng tương lai token AI và chi phí trên mỗi token](/vi/post/ai-token-futures-cost-per-token-korea-semiconductor-thesis-2026-05-30/), [Phân tích chuyên sâu Samsung Electronics 2026](/vi/post/kr-deep-dive-samsung-electronics-2026-04-16/), [SK Hynix: ông trùm HBM](/vi/post/kr-deep-dive-sk-hynix-2026-04-16/) và [Hạ tầng AI của Hàn Quốc sau Q1 FY27 của Nvidia](/vi/post/nvidia-q1-fy27-korea-ai-infra-supply-chain-2026-05-21/). Nếu các bài trước nhìn riêng chi phí trên mỗi token, từng doanh nghiệp và sự lan tỏa của hạ tầng AI, thì bài này <strong>hợp nhất hai dự báo khác nhau — Goldman về nhu cầu và J.P. Morgan về giá bộ nhớ — vào một khung duy nhất</strong> và sắp xếp trục thời gian đầu tư từ 2026 đến 2030.

## TL;DR

* Goldman Sachs nhìn thấy <strong>sự bùng nổ của lượng token (24 lần đến năm 2030) cùng với chi phí trên mỗi token lao dốc (60-70% mỗi năm)</strong>. J.P. Morgan nhìn thấy <strong>tốc độ tăng so với cùng kỳ (YoY) của ASP DRAM và NAND chững lại từ năm 2027</strong>. Vì theo dõi các biến số khác nhau, hai dự báo không xung đột trực diện.
* Kết hợp lại, một lộ trình duy nhất xuất hiện: <strong>2026 là beta ASP bộ nhớ, 2027 là đỉnh (peak-out) của động lượng giá, và 2028-2030 là sự dịch chuyển alpha sang các linh kiện và hệ thống hạ thấp chi phí trên mỗi token</strong>.
* Vì vậy kết luận đầu tư không phải là "mua bộ nhớ vô hạn". Năm 2026, beta bộ nhớ như HBM, DRAM máy chủ và eSSD có lợi, nhưng sau đó phải <strong>chọn lọc nơi có nút thắt cổ chai</strong> — ASIC, mạng AI, quang học, các hãng dẫn đầu HBM, eSSD, đóng gói tiên tiến và MLCC/FC-BGA.
* Hai cách hiểu sai phổ biến nhất là: (1) nhìn vào peak-out của J.P. Morgan và kết luận "chu kỳ hạ tầng AI đã kết thúc", và (2) nhìn vào nhu cầu của Goldman và kết luận "giá bộ nhớ sẽ tiếp tục bùng nổ đến năm 2030". Cả hai đều quá đà.

---

## 1. Hai gã khổng lồ, hai dự báo tưởng chừng đối lập

Trước cùng một kỷ nguyên AI, hai ngân hàng đầu tư toàn cầu đã vẽ ra những bức tranh dường như chỉ về hai hướng trái ngược.

<strong>Goldman Sachs</strong> (bài viết chính thức, ngày 5 tháng 5 năm 2026) nhìn vào phía nhu cầu. Cốt lõi là hai điểm.

- <strong>Lượng token tăng 24 lần đến năm 2030.</strong> Dự báo là lượng dùng hằng tháng đạt 120 triệu tỷ (quadrillion) token vào năm 2030; tính ngược lại, mức nền năm 2026 vào khoảng 5 quadrillion. Đó là mức tăng trung bình khoảng 121% mỗi năm trong bốn năm.
- Đồng thời, <strong>chi phí suy luận trên mỗi token giảm 60-70% mỗi năm.</strong> Động lực là sự cải thiện hiệu suất chip và kiến trúc trung tâm dữ liệu tốt hơn.

![Chỉ số tái dựng kinh tế token AI của Goldman Sachs — lượng dùng tăng 24 lần trong khi chi phí trên mỗi token giảm 39-123 lần](goldman-ai-token-economics-reconstructed-index.png)

<small>Nguồn: biểu đồ tái dựng đơn giản chỉ số hóa các con số trong bài viết chính thức của Goldman Sachs (2026-05-05). Đây không phải biểu đồ gốc mà là các con số gốc — "24 lần token đến năm 2030, chi phí trên mỗi token giảm 60-70% mỗi năm" — được đưa lên thang logarit.</small>

Trong biểu đồ trên, đường màu xanh (lượng dùng) đi lên dốc đứng, còn các đường cam và xanh lá (chi phí trên mỗi token) đi xuống còn dốc hơn. Với mức giảm 60% mỗi năm, chi phí sau bốn năm vào khoảng 2,6% mức của năm 2026 (cải thiện khoảng 39 lần); với 70%, vào khoảng 0,8% (cải thiện khoảng 123 lần).

Ngược lại, tài liệu của <strong>J.P. Morgan</strong> nhìn vào giá. Bức tranh là ASP của DRAM và NAND tăng mạnh trong năm 2026 nhưng, <strong>từ cuối năm 2026 sang đầu năm 2027, tốc độ tăng so với cùng kỳ giảm nhanh.</strong>

![Biến động so với cùng kỳ của ASP DRAM và NAND theo J.P. Morgan — đỉnh năm 2026 và chững lại từ năm 2027](jpm-dram-nand-asp-yoy-peakout-chart.png)

<small>Nguồn: hình ảnh tải lên trong phiên (DRAM theo WSTS / J.P. Morgan estimates, NAND theo Gartner / J.P. Morgan estimates). Các con số chi tiết như FY26 DRAM +53% và NAND +30%, FY27 DRAM +1% và NAND -6% dựa trên bản tóm tắt thứ cấp; bảng gốc chưa được xác minh.</small>

Bề ngoài, "nhu cầu bùng nổ" (Goldman) và "đà tăng giá bộ nhớ chững lại" (J.P. Morgan) dường như mâu thuẫn. Nhưng nhìn kỹ, hai dự báo <strong>đang nói về những thứ khác nhau.</strong>

---

## 2. Vì sao đây không phải mâu thuẫn — tách P, Q và C

Lợi nhuận của một công ty bộ nhớ được phân tách thành một phép nhân đơn giản.

> Doanh thu = lượng xuất hàng (Q) × giá bán bình quân (P), và kinh tế token = lượng dùng (Q) × chi phí trên mỗi token (C).

Qua lăng kính này, rõ ràng hai dự báo đang theo dõi những biến số khác nhau.

| Khía cạnh | Goldman Sachs | J.P. Morgan |
|---|---|---|
| Biến số theo dõi | Lượng token (Q), chi phí trên mỗi token (C) | Biến động YoY của ASP DRAM/NAND (động lượng P) |
| Thông điệp cốt lõi | Lượng dùng AI bùng nổ dài hạn, chi phí trên mỗi token lao dốc | Tốc độ tăng giá bộ nhớ chững lại từ năm 2027 |
| Trục thời gian | 2026-2030 | Cuối 2026 đến đầu 2027 |

Ở đây có một cái bẫy phải nêu rõ. <strong>Trục tung của biểu đồ J.P. Morgan không phải là mức tuyệt đối của giá mà là "tốc độ tăng so với cùng kỳ (YoY %)".</strong> Hai thứ hoàn toàn khác nhau.

Hãy lấy một ví dụ.

| Thời điểm | Chỉ số ASP | YoY |
|---|---:|---:|
| Q4/25 | 100 | – |
| Q4/26 | 300 | +200% |
| Q4/27 | 315 | +5% |

Từ Q4/26 sang Q4/27, chỉ số giá <strong>vẫn tăng</strong>, từ 300 lên 315. Tuy nhiên tốc độ tăng so với cùng kỳ lao dốc từ +200% xuống +5%. Nghĩa là "peak-out" năm 2027 của J.P. Morgan có thể không có nghĩa là giá sụp đổ, mà là <strong>nhịp độ tăng chậm lại.</strong> Thị trường chứng khoán thường phản ánh <strong>hướng của tốc độ tăng</strong> này trước cả "lợi nhuận kỷ lục". Đó là lý do giá cổ phiếu có thể nguội đi trước, đúng lúc lợi nhuận đạt đỉnh.

Tóm lại, Goldman theo dõi <strong>Q (lượng dùng) và C (chi phí)</strong>, còn J.P. Morgan theo dõi <strong>nhịp độ của P (giá).</strong> Vì là các biến số khác nhau, cả hai có thể đúng cùng lúc.

---

## 3. Tổng chi phí suy luận thực ra có thể giảm

Ở đây nảy ra một kết luận trái với trực giác. Dù lượng dùng tăng 24 lần, nếu chi phí trên mỗi token giảm 60-70% mỗi năm, thì <strong>gánh nặng tổng chi phí suy luận thực ra có thể thấp hơn năm 2026.</strong>

Đó là phép tính đơn giản. Giả định cùng cơ cấu token và cùng độ phức tạp mô hình, tổng chi phí năm 2030 là chỉ số lượng dùng × chỉ số chi phí trên mỗi token.

- Giảm 60% mỗi năm: 24 × 2,6% ≈ <strong>61% của năm 2026</strong>
- Giảm 70% mỗi năm: 24 × 0,8% ≈ <strong>19% của năm 2026</strong>

![Gánh nặng tổng chi phí suy luận, độ nhạy đơn giản — dù lượng dùng 24 lần vẫn được mức giảm mạnh của chi phí trên mỗi token hấp thụ](goldman-total-inference-cost-burden-index.png)

<small>Đây là phép tính độ nhạy được đơn giản hóa rất nhiều. Nó không phản ánh cơ cấu token, kích thước mô hình, độ dài ngữ cảnh, sự gia tăng token suy luận (reasoning), đa phương thức, xử lý trùng lặp, ràng buộc độ trễ (latency) hay nút thắt băng thông bộ nhớ. Trên thực tế các yếu tố này có thể đẩy chi phí tăng trở lại.</small>

Biểu đồ này là cốt lõi logic của Goldman. <strong>Ai hạ được chi phí trên mỗi token thì rốt cuộc kiếm được tiền.</strong> Hơn cả việc lượng dùng tăng lên, chính sự cắt giảm chi phí khiến lượng dùng đó trở nên gánh nổi mới giữ cho dòng tiền của ngành sống. Tuy vậy, như lưu ý đã nêu, nếu độ dài ngữ cảnh hoặc token suy luận tăng nhanh, đường chi phí thực có thể giảm ít hơn biểu đồ này gợi ý.

---

## 4. Vì vậy trục thời gian thay đổi

Kết hợp hai dự báo, lộ trình sau đây nhất quán về mặt logic.

| Giai đoạn | Điều gì xảy ra | Nơi nào có lợi |
|---|---|---|
| <strong>2026</strong> | Lượng dùng tác nhân tăng vọt → phân bổ HBM, DRAM máy chủ, eSSD và NAND căng thẳng → ASP DRAM và NAND tăng mạnh | Beta ASP bộ nhớ vận hành mạnh |
| <strong>2027</strong> | Nền cao hơn cộng với một số bổ sung nguồn cung và hợp đồng dài hạn (LTA) làm chững lại tốc độ YoY của ASP. Bộ nhớ AI B2B vững; bộ nhớ tiêu dùng B2C vấp kháng cự giá | Giá cổ phiếu phản ánh "tốc độ tăng chững lại" trước "lợi nhuận đỉnh". Phân hóa theo phân khúc bắt đầu |
| <strong>2028-2030</strong> | Lượng dùng tiếp tục tăng, nhưng mức giảm chi phí trên mỗi token hấp thụ điều đó | Alpha dịch chuyển từ beta bộ nhớ phổ thông sang <strong>ngăn xếp cắt giảm chi phí token</strong> |

Thông điệp cốt lõi chỉ có một. Từ năm 2027, "giá DRAM và NAND còn tăng bao nhiêu nữa" ít quan trọng hơn <strong>"linh kiện và hệ thống nào hạ chi phí trên mỗi token."</strong>

---

## 5. Ví dụ ý tưởng đầu tư (điểm quan sát, không phải khuyến nghị)

Dưới đây không phải là khuyến nghị cổ phiếu, mà là <strong>ví dụ</strong> về "nên nhìn vào đâu trước" theo trục thời gian trên. Cổ phiếu AI và bộ nhớ đã được định giá lại nhanh chóng, nên đây không phải lời kêu gọi mua ngay bây giờ mà là tấm bản đồ cho thời điểm các điều kiện được thỏa mãn.

### Ví dụ 1 — Beta ASP bộ nhớ 2026

Giai đoạn phân bổ HBM, DRAM máy chủ và eSSD căng thẳng và giá DRAM, NAND tăng vọt. Các cổ phiếu bộ nhớ vốn hóa lớn như <strong>SK Hynix, Samsung Electronics và Micron</strong> hưởng lợi trực tiếp. Lập luận ngược lại là một khi đà chững lại của tốc độ tăng năm 2027 bắt đầu, giá cổ phiếu có thể bị nén bội số trước, dù lợi nhuận cao.

### Ví dụ 2 — Ngăn xếp cắt giảm chi phí token

Cốt lõi thực sự trong logic của Goldman không phải là lượng dùng tăng mà là <strong>chi phí trên mỗi token giảm.</strong> Khách hàng sẽ trả nhiều hơn cho chip và hệ thống hạ thấp chi phí trên mỗi token của họ. <strong>ASIC tùy biến, mạng AI và quang học, và các hãng dẫn đầu HBM</strong> phù hợp nhất ở đây. (Các nút thắt kết nối, đế (substrate) và điện năng thấy trong [read-through Marvell](/vi/post/marvell-q1-fy2027-korea-semiconductor-readthrough-2026-05-28/) chính là mạch này.)

### Ví dụ 3 — eSSD / NAND doanh nghiệp

Suy luận của tác nhân đòi hỏi nhiều hơn hẳn về truy xuất (RAG), nhật ký, ngữ cảnh, KV cache và lưu checkpoint so với huấn luyện đơn thuần. Nếu đúng là máy chủ AI dùng dung lượng SSD gấp khoảng 3 lần máy chủ thông thường, thì NAND có thể được phân loại lại không phải là tài sản chu kỳ phổ thông mà là <strong>nút thắt lưu trữ AI.</strong> Lập luận ngược lại là khả năng kháng cự giá của SSD tiêu dùng làm pha loãng sức mạnh của mảng doanh nghiệp.

### Ví dụ 4 — Đóng gói tiên tiến / MLCC / FC-BGA

Nếu dự báo token năm 2030 của Goldman đúng, độ phức tạp của kiến trúc máy chủ và rack tiếp tục tăng. Không chỉ GPU, ASIC và HBM tăng lên; nhu cầu về diện tích đế, ổn định nguồn điện, tụ tách (decoupling) và chất lượng tín hiệu tốc độ cao cũng tăng theo. Các nhà cung cấp MLCC và FC-BGA cao cấp như <strong>Samsung Electro-Mechanics</strong> thuộc nhóm này.

### Peak-out khác nhau theo phân khúc

Điều quan trọng không phải là "toàn bộ bộ nhớ" mà là sự khác biệt theo phân khúc. Logic peak-out của J.P. Morgan không áp dụng như nhau cho mọi loại bộ nhớ.

| Phân khúc | Khả năng peak-out áp dụng | Mức căng với nhu cầu dài hạn |
|---|---|---|
| HBM | Thấp-Trung bình | Cao (nhu cầu tiếp tục củng cố bức tường băng thông) |
| DRAM máy chủ | Trung bình | Trung bình |
| eSSD / NAND doanh nghiệp | Trung bình | Cao (có thể có nhu cầu cấu trúc) |
| DRAM di động | Cao | Thấp (kháng cự giá tiêu dùng nhanh) |
| DRAM/NAND phổ thông | Cao | Thấp (logic peak-out áp dụng tốt nhất) |

> Điều kiện chung: các ví dụ trên cần nhiều hơn "giảm quá đà" hay "vì là AI". Một ứng viên phải ở nơi mà <strong>đơn hàng thực, giá hợp đồng và ước tính lợi nhuận tăng mới, và nút thắt cùng rào cản gia nhập được xác nhận.</strong>

---

## 6. Hai cách hiểu sai phổ biến nhất

Trong giai đoạn này, thị trường dễ mắc hai sai lầm theo hai hướng trái ngược.

<strong>Hiểu sai 1 — "J.P. Morgan nói peak-out, vậy chu kỳ hạ tầng AI đã kết thúc."</strong> Không. Peak-out là sự chững lại của <strong>tốc độ tăng</strong> giá, không phải sự sụp đổ của <strong>mức</strong> giá. Và nó áp dụng tốt nhất cho bộ nhớ phổ thông và ít hơn cho các nút thắt như HBM, eSSD, ASIC và đóng gói.

<strong>Hiểu sai 2 — "Goldman nói token 24 lần, vậy giá DRAM và NAND cũng tiếp tục bùng nổ đến năm 2030."</strong> Điều này cũng quá đà. Goldman nói lượng dùng bùng nổ và <strong>chi phí trên mỗi token lao dốc</strong> cùng lúc. Nếu chi phí giảm nhanh, tốc độ tăng so với cùng kỳ của giá bộ nhớ có thể chững lại dù lượng dùng tăng.

Cách hiểu đúng nằm ở giữa. <strong>Một siêu chu kỳ bộ nhớ năm 2026, một peak-out của động lượng giá năm 2027, và sự mở rộng dài hạn của ngăn xếp cắt giảm chi phí token năm 2028-2030.</strong>

---

## 7. Bình luận của nhà quản lý quỹ

Hai dự báo không phải kẻ thù mà là hai trục của cùng một bức tranh. Goldman nói về "chúng ta sẽ dùng AI nhiều đến đâu và rẻ đến đâu"; J.P. Morgan nói về "trong quá trình đó, giá bộ nhớ còn tăng nhanh đến khi nào". Việc của nhà đầu tư không phải là chọn một trong hai mà là <strong>không bỏ lỡ các điểm bước ngoặt trên trục thời gian.</strong>

Hai lựa chọn nguy hiểm nhất là thế này.

* <strong>Vứt bỏ toàn bộ hạ tầng AI khi chỉ thấy một từ peak-out</strong> — sai lầm bán rẻ cả những người chiến thắng có nút thắt cổ chai.
* <strong>Đeo bám bộ nhớ phổ thông đến cùng chỉ vì nhu cầu token</strong> — sai lầm hứng trực diện sự nén bội số trong giai đoạn tốc độ tăng giá chững lại.

Các tín hiệu cần kiểm tra ngay bây giờ, nói đơn giản, là thế này.

| Bạn nhìn gì | Củng cố Goldman (nhu cầu) | Củng cố J.P. Morgan (peak-out) |
|---|---|---|
| Lượng token | Tăng trưởng cao duy trì | Tốc độ tăng chững lại |
| Chi phí trên mỗi token | Tiếp tục giảm hơn 60% mỗi năm | Nhịp giảm chững lại, chi phí độ trễ tăng |
| Hợp đồng dài hạn HBM | Giữ giá hoặc nâng giá | Tái đàm phán, hoãn khối lượng |
| Giá hợp đồng DRAM máy chủ | Tăng thêm | Tốc độ tăng chững lại, chiết khấu giao ngay |
| SSD doanh nghiệp | Hợp đồng dài hạn với CSP mở rộng | Kháng cự giá SSD tiêu dùng lan sang |

Tóm lại, <strong>thừa nhận beta bộ nhớ trong năm 2026 trong khi chuẩn bị, từ năm 2027, dịch chuyển trọng số sang các nút thắt hạ thấp chi phí trên mỗi token</strong> là tư thế hợp lý nhất có thể lúc này. Không phải đeo bám bộ nhớ đến cùng, cũng không phải vì sợ peak-out mà vứt bỏ tất cả.

<small>Bài viết này là một phân tích được tái dựng từ bài viết chính thức của Goldman Sachs (2026-05-05), các biểu đồ và bản tóm tắt thứ cấp liên quan đến J.P. Morgan, và dự báo chính thức của TrendForce. Toàn văn báo cáo gốc của J.P. Morgan, các bảng ASP theo quý và chi tiết theo phân khúc chưa được xác minh, và tên doanh nghiệp là ví dụ minh họa mạch phân tích, không phải khuyến nghị đầu tư. Quyết định đầu tư thực tế và trách nhiệm thuộc về chính nhà đầu tư.</small>
