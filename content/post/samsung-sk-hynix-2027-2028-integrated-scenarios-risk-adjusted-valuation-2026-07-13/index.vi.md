---
title: "2028 Quan Trọng Hơn Chu Kỳ Bùng Nổ 2027: Kịch Bản Tích Hợp cho Samsung Electronics & SK Hynix"
description: "Bắt đầu từ kịch bản cơ sở là chu kỳ bùng nổ bộ nhớ năm 2027, phân tích này bổ sung các yếu tố mở rộng nguồn cung 2028, mức tăng hiệu quả suy luận, và rủi ro tái tài trợ hạ tầng AI. Chúng tôi so sánh Samsung Electronics và SK Hynix trên cơ sở xác suất có trọng số qua EPS theo kịch bản, PER giá trị hợp lý, và giá trị hiện tại, đồng thời xem xét cách hợp đồng cung ứng dài hạn HBM và mở rộng công suất bộ nhớ của Trung Quốc định hình lại thời gian tạo lợi nhuận."
date: 2026-07-13T20:39:17+09:00
lastmod: 2026-07-13T20:39:17+09:00
categories: ["Phân Tích Độc Quyền", "Bán Dẫn", "Vĩ Mô"]
tags:
  - "Samsung Electronics"
  - "SK Hynix"
  - "HBM"
  - "Bán Dẫn Bộ Nhớ"
  - "Hạ Tầng AI"
  - "Phân Tích Kịch Bản"
  - "Định Giá"
  - "CXMT"
  - "YMTC"
series: ["exclusive-analysis", "ai-hbm-2026"]
slug: "samsung-sk-hynix-2027-2028-integrated-scenarios-risk-adjusted-valuation-2026-07-13"
image: "/images/posts/samsung-hynix-2027-2028-scenario-map-2026-07-13.png"
valley_cashtags:
  - 삼성전자
  - SK하이닉스
draft: false
---

> Ngữ cảnh liên quan: Bài viết này là phần tiếp theo của [Mô Hình Cung-Cầu HBM 2030 — Kiểm Tra Chéo](/vi/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/), [Định Giá Samsung Electronics & SK Hynix Qua Lợi Nhuận Ước Tính Đến 2028E](/vi/post/samsung-hynix-2028e-profit-valuation-cycle-scenarios-2026-07-09/), và [Phân Tích Bán Tháo AI Hardware Ngày 13/7](/vi/post/kospi-9pct-selloff-ai-hardware-derating-korea-leverage-2026-07-13/). Chấp nhận chu kỳ bùng nổ 2027 là kịch bản cơ sở, bài viết định lượng xác suất mà điều kiện cung, hiệu quả và tài chính thay đổi đồng thời bắt đầu từ năm 2028.

## TL;DR

- Cung/cầu HBM có khả năng tiếp tục thắt chặt xuyên suốt năm 2027. Tuy nhiên, dự báo `nhu cầu 2030 26.7EB so với cung 10.6EB, thâm hụt 2.52×` không phải là dự báo kịch bản cơ sở — nó đòi hỏi nhiều giả định lạc quan phải đồng thời được duy trì.
- Năm quan trọng nhất không phải là 2027 mà là <strong>2028</strong>. Mở rộng nguồn cung từ Samsung Electronics, SK Hynix và Micron, tăng hiệu quả suy luận, và xác minh tái tài trợ trên toàn bộ trung tâm dữ liệu AI đều hội tụ trong cùng một giai đoạn.
- Hợp đồng cung ứng dài hạn HBM kéo dài thời gian tạo lợi nhuận nhưng không loại bỏ được chu kỳ. Chúng chuyển đổi rủi ro giá thành rủi ro gia hạn hợp đồng, rủi ro tín dụng khách hàng, rủi ro cơ cấu sản phẩm, và rủi ro định giá lại.
- Xác suất có điều kiện: P1 nhu cầu vượt trội duy trì 35%, P2 căng thẳng tín dụng cục bộ với tập trung lại vào hyperscaler 40%, P3 tăng hiệu quả và bình thường hóa nguồn cung 15%, P4 đóng băng tín dụng hệ thống 10%.
- EPS có trọng số xác suất cho 2027: Samsung Electronics 60,750원, SK Hynix 393,000원. Cho 2028: Samsung 49,900원, SK Hynix 316,000원.
- Giá trị hiện tại của giá trị cuối kỳ 2028 chiết khấu ở mức 11% hàng năm: Samsung Electronics 317,246원, SK Hynix 1,956,316원 — ngụ ý tiềm năng tăng giá lần lượt 24.7% và 6.0% so với giá đóng cửa KRX ngày 13/7. Khi rủi ro bình thường hóa 2028 được tích hợp, biên an toàn của Samsung rộng hơn; SK Hynix nhạy cảm hơn với việc liệu P1 có duy trì hay không.

<div class="thesis-callout">
  <div class="thesis-callout__label">Kết Luận</div>
  <div class="thesis-callout__body">
    Chu kỳ bùng nổ 2027 tương đối có thể nhìn thấy rõ. Câu hỏi khó hơn là <strong>liệu định giá HBM cao và lợi nhuận có kéo dài qua năm 2028 và xa hơn không</strong>. Giá hiện tại đang chiết khấu thời gian tồn tại của lợi nhuận vượt xa đỉnh 2027.
  </div>
</div>

![Bản Đồ Kịch Bản Tích Hợp 2027–2028 cho Samsung Electronics và SK Hynix](/images/posts/samsung-hynix-2027-2028-scenario-map-2026-07-13.png)

## 1. Câu Hỏi Phân Tích và Chất Lượng Bằng Chứng

Phân tích này gắn kết ba câu hỏi trong một khung phân tích thống nhất.

1. Chúng ta có thể đặt bao nhiêu niềm tin vào nhận định rằng cung/cầu HBM sẽ tiếp tục thắt chặt xuyên suốt năm 2027?
2. Nếu điều kiện cung, hiệu quả và tài chính thay đổi đồng thời vào năm 2028, lợi nhuận của Samsung Electronics và SK Hynix sẽ khác nhau như thế nào qua các kịch bản?
3. Với những thay đổi đó, giá cổ phiếu hiện tại đang giao dịch tại mức lợi nhuận ngụ ý nào?

Các con số trong báo cáo này phải được đọc theo danh mục.

| Danh Mục | Định Nghĩa | Ví Dụ Trong Báo Cáo Này |
|---|---|---|
| Sự Thật | Được xác minh từ hồ sơ công khai hoặc dữ liệu thị trường | Giá đóng cửa KRX ngày 13/7, FCF Oracle, khoản vay CoreWeave |
| Đồng Thuận | Ước tính thị trường tổng hợp | EPS và lợi nhuận ròng 2027–2028 |
| Ước Tính Môi Giới | Dự báo môi giới riêng lẻ | EPS SK Hynix của Korea Investment & Securities và BNK Investment & Securities |
| Kết Quả Mô Hình | Được suy ra từ các công thức và giả định được công bố | EPS và giá trị hiện tại có trọng số xác suất P1–P4 |
| Phán Đoán Chuyên Gia | Đánh giá phân tích phi thống kê | Xác suất kịch bản, PER hợp lý, tỷ suất lợi nhuận yêu cầu 11% |
| Không Xác Định | Không thể xác định chỉ từ nguồn công khai | Định giá cấp hợp đồng HBM, khối lượng theo từng khách hàng, năng suất sản xuất thực tế |

Các công thức cốt lõi như sau.

```text
Giá Trị Cuối Kỳ Theo Kịch Bản = EPS Theo Kịch Bản × PER Hợp Lý Theo Kịch Bản
EPS Có Trọng Số Xác Suất = Σ(Xác Suất Kịch Bản × EPS Theo Kịch Bản)
Giá Trị Cuối Kỳ Có Trọng Số Xác Suất = Σ(Xác Suất Kịch Bản × Giá Trị Cuối Kỳ Theo Kịch Bản)
Giá Trị Hiện Tại = Giá Trị Cuối Kỳ ÷ (1 + 11%)^Số Năm Còn Lại
HBM Need/Fleet = Kho lưu trữ nhu cầu HBM đã lắp đặt và hoạt động ÷ công suất cung cấp có thể phục vụ bởi đội thiết bị đã lắp đặt
```

Xác suất kịch bản không được suy ra từ phân phối tần suất lịch sử. Chúng là đánh giá có điều kiện phản ánh điều kiện nhu cầu, cung, hiệu quả và tài chính hiện đang quan sát được. Giá trị PER hợp lý tương tự không được quan sát cơ học từ thị trường mà là ước tính phân tích kết hợp độ bền lợi nhuận, mức độ tập trung kinh doanh, cấu trúc tài chính, và rủi ro dài hạn.

## 2. Giá Hiện Tại và Đồng Thuận Thị Trường

Giá đóng cửa KRX ngày 13/7 và ước tính đồng thuận được tổng hợp cùng ngày được sử dụng xuyên suốt.

| Hạng Mục | Samsung Electronics | SK Hynix |
|---|---:|---:|
| Giá Đóng Cửa KRX 2026-07-13 | 254,500원 | 1,845,000원 |
| EPS Đồng Thuận 2027 | 65,802원 | 444,359원 |
| EPS Đồng Thuận 2028 | 65,907원 | 433,625원 |
| Lợi Nhuận Ròng Đồng Thuận 2027 | 44.3조원 | 32.4조원 |
| Lợi Nhuận Ròng Đồng Thuận 2028 | 44.1조원 | 31.9조원 |
| Giá Hiện Tại / EPS Đồng Thuận 2027 | 3.87× | 4.15× |
| Giá Hiện Tại / EPS Đồng Thuận 2028 | 3.86× | 4.25× |

Nhìn bề ngoài, cả hai công ty trông có vẻ rẻ một cách đáng kể. Nhưng các bội số PER thấp này không có nghĩa là thị trường không biết về lợi nhuận 2027 — chúng nhiều khả năng là tín hiệu cho thấy thị trường nghi ngờ về độ bền của lợi nhuận sau 2028.

Sự phân tán trong các ước tính SK Hynix minh họa điều này một cách rõ ràng.

| Nguồn | EPS 2027 | EPS 2028 | Diễn Giải |
|---|---:|---:|---|
| Đồng Thuận Thị Trường | 444,359원 | 433,625원 | Bình thường hóa vừa phải năm 2028 |
| Korea Investment & Securities | 415,254원 | 495,696원 | Tăng trưởng lợi nhuận tiếp tục đến 2028 |
| BNK Investment & Securities | 214,642원 | 66,989원 | Vượt đỉnh nhanh sau 2027 |

Đối với cùng một công ty, ước tính EPS 2028 dao động từ 66,989원 đến 495,696원. Sự phân kỳ này không xuất phát từ dự báo nhu cầu 2026 mà từ các giả định khác nhau về <strong>giá bán trung bình HBM 2028, tốc độ mở rộng nguồn cung, và thời gian kéo dài của capex AI</strong>.

Tính lại PER hiện tại sử dụng EPS có trọng số xác suất của báo cáo này:

| Năm | Samsung Electronics | SK Hynix |
|---|---:|---:|
| 2027 | 4.19× | 4.69× |
| 2028 | 5.10× | 5.84× |

Áp dụng ngược PER hợp lý có trọng số xác suất vào giá cổ phiếu hiện tại, EPS ngụ ý mà thị trường đang định giá là khoảng 31,700원 đối với Samsung và khoảng 245,000원 đối với SK Hynix — thấp hơn khoảng 52% và 45% so với đồng thuận 2027 tương ứng. Thị trường không chiết khấu lợi nhuận 2027 theo nghĩa đen, mà chiết khấu thời gian tồn tại của lợi nhuận đó.

## 3. Những Gì Đã Thay Đổi trong Chu Kỳ Bộ Nhớ — và Những Gì Chưa Thay Đổi

### Những Gì Đã Thay Đổi

1. Máy chủ AI, HBM và SSD doanh nghiệp đã nâng tỷ trọng nhu cầu từ phân khúc doanh nghiệp và trung tâm dữ liệu trong tổng cơ cấu cầu.
2. HBM đòi hỏi quy trình xác nhận chất lượng từ khách hàng, đóng gói tiên tiến, nâng cao tỷ lệ yield theo từng giai đoạn và hợp đồng dài hạn, khiến tốc độ phản ứng cung trong ngắn hạn chậm hơn so với DRAM thông thường.
3. Khi HBM chiếm tỷ trọng ngày càng lớn trong wafer start, sản lượng DRAM thông thường từ các nhà máy cùng cơ sở giảm xuống, qua đó có thể hỗ trợ giá DRAM thông thường.
4. Việc các nhà cung cấp đám mây lớn và nhà khai thác trung tâm dữ liệu AI tài trợ trước đã kéo sớm các đơn đặt hàng bộ nhớ thực tế, đóng vai trò như một yếu tố tăng tốc.
5. Ngược lại, khi các vấn đề tín dụng phát sinh, nhu cầu không suy giảm từ từ — mà có thể giảm đột ngột thông qua đàm phán lại hợp đồng và hoãn đầu tư.

### Những Gì Chưa Thay Đổi

1. Giá cao cuối cùng sẽ kéo theo xây dựng nhà máy mới, cải thiện yield, chuyển đổi node quy trình và đối thủ cạnh tranh bổ sung công suất.
2. Giá và biên lợi nhuận HBM cao sẽ làm tăng động lực để nhà cung cấp thứ hai gia nhập thị trường và để khách hàng gây áp lực giảm chi phí.
3. Hợp đồng dài hạn không loại bỏ rủi ro giá — mà chuyển đổi nó thành rủi ro định giá khi gia hạn và rủi ro tín dụng của khách hàng.
4. Đồng thời áp dụng EPS đỉnh chu kỳ với PER cao là sai lầm lạc quan kép, khi cả lợi nhuận lẫn bội số đều được tính ở mức thuận lợi nhất.

Luận điểm rằng HBM đã biến bộ nhớ trở thành ngành kinh doanh tốt hơn DRAM truyền thống, và luận điểm rằng chu kỳ bộ nhớ đã bị xóa bỏ, là hai nhận định hoàn toàn khác nhau.

## 4. Mô Hình Cung-Cầu HBM và Điểm Uốn Năm 2028

Trong [Mô Hình Cung-Cầu HBM 2030 — Kiểm Chứng Chéo](/vi/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/), chúng tôi tái hiện kết quả `cầu 26,7EB, cung 10,6EB, thâm hụt 2,52×` của mô hình gốc trong các đơn vị nhất quán. Bản thân công thức không so sánh sai một luồng cầu với một lượng tồn kho cung. Vấn đề nằm ở chỗ các giả định dài hạn nhân nối tiếp nhau theo chuỗi.

Bao gồm:
- Tốc độ tăng trưởng tiêu thụ token hàng tháng
- Quy mô mô hình, độ dài ngữ cảnh và mở rộng trạng thái agent
- Tỷ lệ KV cache và memory residency
- Hiệu quả throughput, quantization và routing
- Vòng đời dịch vụ HBM và sự dịch chuyển khối lượng công việc suy luận sang các loại bộ nhớ khác
- Sản lượng sản xuất khả thi và yield đóng gói trên ba nhà sản xuất bộ nhớ lớn

Vì lý do này, mức thâm hụt 2,52× năm 2030 nên được xem là kịch bản stress tăng giá mạnh hơn là kịch bản cơ sở. Việc tái suy diễn các giả định trung tâm phù hợp với từng kịch bản P1–P4 cho kết quả sau:

| Kịch Bản | Hệ Số Token | Quy Mô Mô Hình | Hiệu Quả Throughput | Hiệu Quả KV | HBM Residency | Cầu | Need/Fleet |
|---|---:|---:|---:|---:|---:|---:|---:|
| P1 Thặng Dư Cầu Trật Tự | 20× | 4,0× | 12× | 5,0× | 65% | 16,1EB | 1,52× |
| P2 Căng Thẳng Tín Dụng Cục Bộ & Tái Tập Trung | 18× | 3,5× | 12× | 5,5× | 60% | 12,8EB | 1,21× |
| P3 Tăng Hiệu Quả & Mở Rộng Cung | 12× | 2,0× | 14× | 6,0× | 50% | 6,5EB | 0,62× |
| P4 Đứt Gãy Tín Dụng Hệ Thống | 8× | 2,0× | 14× | 7,0× | 45% | 2,6EB | 0,25× |

Để đảm bảo tính so sánh, công suất cung được giữ cố định ở mức 10,6EB. Wafer start HBM thực tế, cơ cấu sản phẩm, yield die tốt và công suất đóng gói là thông tin không công khai, do đó không thể xác nhận giá trị tuyệt đối.

Nhìn theo trục thời gian, nhận định được đơn giản hóa đáng kể.

| Giai Đoạn | Đánh Giá | Mức Độ Tin Cậy |
|---|---|---|
| 2026–2027 | Chuyển đổi HBM4 và nhu cầu AI vượt trước các bổ sung công suất nhà máy mới | Cao |
| 2028 | SK Hynix Yongin Line 1, Micron ID1/Tongluo và mở rộng HBM Samsung bắt đầu nới lỏng cung | Trung Bình-Cao |
| 2029–2030 | Thâm hụt còn lại có nhiều khả năng thu hẹp hơn là sâu thêm | Trung Bình |
| Thâm hụt 2,5× năm 2030 | Đòi hỏi nhiều giả định tăng giá đồng thời cùng thành lập | Thấp |

Do đó, quyết định đầu tư không phụ thuộc vào việc chu kỳ tăng trưởng 2027 có xảy ra hay không. Điểm mấu chốt là liệu nguồn cung bổ sung đưa vào hoạt động năm 2028 có vượt qua được quy trình xác nhận chất lượng của khách hàng hay không, và liệu thời điểm đó có trùng với các đợt cải thiện hiệu quả suy luận và thắt chặt tài chính trung tâm dữ liệu AI hay không.

## 5. Hợp Đồng Dài Hạn của SK Hynix và Đường Cong Lợi Nhuận

Báo cáo SK Hynix ngày 13 tháng 7 của Korea Investment & Securities cho rằng việc lỡ kỳ vọng đồng thuận Q2 không phải do nhu cầu sụp đổ mà do độ trễ về thời gian trong cách dịch chuyển cơ cấu sản phẩm HBM và định giá hợp đồng cung dài hạn phản ánh vào kết quả báo cáo.

| Chỉ Tiêu | 2026F | 2027F | 2028F |
|---|---:|---:|---:|
| Doanh Thu | 32,83조원 | 48,77조원 | 58,53조원 |
| Lợi Nhuận Hoạt Động | 24,51조원 | 37,45조원 | 44,70조원 |
| EPS | 292,068원 | 415,254원 | 495,696원 |
| ROE | 94,5% | 65,4% | 46,5% |

Các giả định HBM cũng mang tính tích cực cao.

| Chỉ Số HBM | 2026F | 2027F |
|---|---:|---:|
| Tăng Trưởng Bit | +23,0% | +31,2% |
| ASP | $1,60/Gb | $2,82/Gb |
| Tăng Trưởng ASP | -2,5% | +76,3% |
| Doanh Thu | 3,71조원 | 8,30조원 |
| Tăng Trưởng Doanh Thu | +28,0% | +123,6% |

Các điều chỉnh ước tính chính trong báo cáo bao gồm:

- Doanh số HBM4 bắt đầu từ Q3 2026, nhưng điểm uốn lợi nhuận lớn nhất được mô hình hóa vào Q4 khi ASP HBM tăng `+52% QoQ`.
- So với ước tính tháng 5, ASP DRAM thông thường (non-HBM) cho giai đoạn 2026–2027 được điều chỉnh giảm khoảng 16%.
- Doanh thu HBM 2026 được nâng lên 17%.
- Khối lượng vận chuyển HBM 2027 được giữ nguyên trong khi ASP bị cắt giảm 5%.
- Khối lượng vận chuyển và giá NAND được nâng lên.

Báo cáo này không phải là sự rút lại luận điểm tăng trưởng HBM dài hạn. Đây là một đợt điều chỉnh giảm độ co giãn giá DRAM thông thường trong ngắn hạn và đẩy lùi thời điểm kinh tế HBM4 phản ánh vào kết quả báo cáo.

### Tại Sao Không Nên Tin Vào Hợp Đồng Dài Hạn Theo Mệnh Giá

1. Mức giá sàn, giá trần, nghĩa vụ mua tối thiểu và điều khoản thanh toán trước ở cấp độ hợp đồng không được công bố công khai.
2. Các báo cáo nêu rằng hợp đồng "không có giá trần" tự bản thân không thể xác nhận giá tăng mỗi năm — cần phải biết liệu định giá có liên kết với tỷ giá giao ngay hay không và tần suất điều chỉnh như thế nào.
3. Hợp đồng dài hạn khóa chặt khối lượng và quan hệ khách hàng nhưng không loại bỏ rủi ro khách hàng đàm phán lại, vỡ nợ hoặc suy giảm tín dụng.
4. DRAM thông thường và NAND nằm ngoài các hợp đồng đó vẫn hoàn toàn phơi lộ trước chu kỳ giá hàng hóa.
5. Nếu yield HBM4 thấp, lô hàng và lợi nhuận gia tăng của SK Hynix vẫn có thể không đạt mục tiêu ngay cả khi thị trường vẫn trong tình trạng thiếu cung.

Lợi ích lớn nhất của hợp đồng dài hạn không phải là loại bỏ chu kỳ mà là <strong>kéo dài thời gian duy trì lợi nhuận và chuyển đổi hình thức rủi ro</strong>.

## 6. Cách Dòng Vốn Tài Trợ Hạ Tầng AI Chuyển Hóa Thành Đơn Hàng Bộ Nhớ

Nhu cầu bộ nhớ AI không chỉ đơn thuần được thúc đẩy bởi sức kéo công nghệ. Hoạt động tài trợ vốn của các nhà vận hành trung tâm dữ liệu tạo ra các đơn hàng tập trung vào giai đoạn đầu, và khi điều kiện tài chính thắt chặt, khoảng trống đơn hàng có thể xuất hiện một cách đột ngột.

```text
Kỳ vọng AI gia tăng
  -> Đầu tư vào trung tâm dữ liệu cloud/AI và mở rộng hợp đồng dài hạn
  -> Capex tập trung giai đoạn đầu vào GPU, HBM, điện năng và trung tâm dữ liệu
  -> Tài sản, doanh thu và giá trị doanh nghiệp tăng giá
  -> Tài trợ thêm bằng nợ và vốn cổ phần
  -> Chương trình capex quy mô lớn hơn

Chiều ngược lại
Chậm trễ trong thu tiền hoặc chi phí tái tài trợ tăng cao
  -> Đàm phán lại hợp đồng / trì hoãn mở rộng
  -> Khoảng trống đơn hàng bộ nhớ
  -> ASP và giá cổ phiếu sụt giảm
  -> Giá trị tài sản đảm bảo và điều kiện tài chính xấu đi
  -> Cắt giảm capex thêm
```

Các con số được xác nhận từ công bố thông tin đại chúng là rất đáng kể.

| Hạng mục | Giá trị xác nhận | Diễn giải |
|---|---:|---|
| Oracle FY2026 Free Cash Flow | -$23,7 tỷ | Capex AI quy mô lớn vượt khả năng tạo tiền mặt |
| Tài trợ nợ Oracle | $43 tỷ | Phụ thuộc nhiều vào nguồn vốn bên ngoài cho đầu tư AI |
| Tài trợ vốn cổ phần Oracle | $5 tỷ | Nợ đơn thuần không đủ bù đắp đầu tư |
| Oracle RPO | $638 tỷ | Hợp đồng dài hạn đảm bảo khả năng hiển thị doanh thu cao |
| Trả trước của khách hàng & Cung cấp GPU trực tiếp Oracle | $75 tỷ | Khách hàng cuối cùng chia sẻ rủi ro đầu tư |
| Tổng nợ CoreWeave (Cuối 2025) | $21,6 tỷ | Đòn bẩy tài chính cao trong trung tâm dữ liệu AI |
| CoreWeave DDTL 4.0 mới | $8,5 tỷ | Tài trợ thêm để tiếp tục mở rộng |
| Ngưỡng DSCR CoreWeave | Tối thiểu 1,15× | Xác minh tái tài trợ toàn diện bắt đầu chậm nhất sau ngày 30 tháng 6 năm 2027 |

Chi tiết các khoản vay cuối năm 2025 của CoreWeave bao gồm DDTL 2.0 khoảng $5,04 tỷ, DDTL 2.1 khoảng $2,74 tỷ, DDTL 1.0 khoảng $1,55 tỷ, DDTL 3.0 khoảng $0,34 tỷ và hợp đồng thuê tài chính thiết bị/phần mềm khoảng $4,17 tỷ. DDTL 4.0, được ký vào tháng 3 năm 2026, có tổng giá trị $8,5 tỷ.

Những con số này không hàm ý rằng nhu cầu AI là ảo. Các hợp đồng, GPU, hạ tầng điện năng và trung tâm dữ liệu đều có thực. Tuy nhiên, nếu dòng tiền không theo kịp chi phí tài trợ vào năm 2027–2028, các nhà vận hành yếu thế có khả năng phải bán tài sản để được các nhà cung cấp đám mây lớn thâu tóm.

Đây là lý do xác suất được gán cho <strong>P2 — áp lực cục bộ dẫn đến tái tập trung tài sản vào tay các hyperscaler</strong> — vượt hơn xác suất của P4 sụp đổ hệ thống. Trong P2, đơn hàng bộ nhớ không biến mất nhưng khoảng cách một hoặc nhiều quý là hoàn toàn có thể xảy ra.

## 7. Cây Xác Suất Có Điều Kiện P1–P4

Xác suất cuối cùng được xác định bằng cách sắp xếp theo trình tự `nhu cầu thực → xác minh tài chính → cung/hiệu quả → hấp thụ tài sản`, chứ không phải từ tần suất chu kỳ bộ nhớ lịch sử.

```text
Xác minh Thu tiền AI và Tái tài trợ 2028
  Vượt qua 50%
    ├─ P1 Vượt cầu bền vững 70%               = 35%
    └─ P3 Bình thường hóa hiệu quả/cung 30%    = 15%
  Áp lực 50%
    ├─ P2 Áp lực cục bộ/tái tập trung 80%      = 40%
    └─ P4 Đóng băng tín dụng hệ thống 20%      = 10%
```

Nhánh đầu 50/50 không phải là prior thống kê. Đây là điểm xuất phát trung lập phản ánh thực tế rằng nhu cầu thực và các hợp đồng đều mạnh nhưng xác minh tài chính vẫn chưa hoàn tất. Tính xác suất với độ chính xác đến từng điểm phần trăm từ dữ liệu hiện tại sẽ tạo ra độ chính xác giả tạo — các điều chỉnh chỉ được thực hiện theo bước 5 điểm phần trăm.

### Bằng chứng ủng hộ Xác minh Vượt qua vs. Áp lực Tài chính

| Bằng chứng ủng hộ Xác minh Vượt qua | Bằng chứng ủng hộ Áp lực Tài chính |
|---|---|
| Độ trễ trong lộ trình tăng sản lượng HBM đại trà đến hết 2027 | Oracle FY2026 FCF -$23,7 tỷ, tài trợ nợ $43 tỷ |
| Oracle RPO $638 tỷ, trả trước của khách hàng và cung cấp GPU trực tiếp $75 tỷ | Tổng nợ CoreWeave $21,6 tỷ, DDTL mới $8,5 tỷ |
| Hợp đồng dài hạn và trả trước HBM nâng cao khả năng hiển thị đơn hàng | Xác minh DSCR CoreWeave 1,15× sau giữa năm 2027 |
| Đầu tư thực tế vào trung tâm dữ liệu của các nhà cung cấp đám mây lớn | Phần bù rủi ro tăng cao đối với trái phiếu AI kỳ hạn dài |

Tỷ lệ phân chia 70/30 giữa P1 và P3 trên nhánh xác minh vượt qua phản ánh thực tế rằng qua năm 2027, các nút thắt cổ chai về chứng nhận, năng suất và đóng gói vẫn còn tồn tại, trong khi về phía bộ nhớ, MoE, MLA, nén KV, routing và offloading đều có thể mở rộng quy mô đồng thời từ năm 2028 trở đi.

Tỷ lệ phân chia 80/20 giữa P2 và P4 trên nhánh áp lực cũng rõ ràng. GPU và trung tâm dữ liệu không phải là tài sản biến mất — các hyperscaler với dòng tiền mạnh có thể mua lại và tái triển khai chúng. Bởi vì sự sụt giảm capex đồng thời, nhiều vi phạm điều khoản vay và suy giảm hợp đồng dài hạn HBM chưa cùng lúc xuất hiện, P4 được xem là rủi ro đuôi ở mức 10%.

### Sổ cái Bằng chứng

| Bằng chứng | P1 | P2 | P3 | P4 | Đánh giá |
|---|---:|---:|---:|---:|---|
| Thiếu cung HBM đến hết 2027 | ++ | + | - | -- | Tình trạng thiếu hụt tiếp diễn |
| Mở rộng cung ứng Top-3 bộ nhớ sau 2028 | - | 0 | ++ | 0 | Con đường độc lập của P3 |
| CXMT mở rộng DDR5/LPDDR cho khách hàng | - | - | ++ | 0 | Khống chế trần giá hàng hóa trước HBM |
| Tăng tốc NAND nhiều lớp YMTC và chấp nhận của khách hàng | - | - | ++ | 0 | Áp lực lên Samsung NAND và cấu trúc enterprise SSD trước |
| Chứng nhận khách hàng HBM/bộ nhớ máy chủ Trung Quốc | -- | - | ++ | 0 | Nếu xác nhận, dịch chuyển từ P1 sang P3 |
| Oracle RPO & GPU do khách hàng cung cấp | + | + | 0 | - | Nhu cầu có thực; đệm giảm lây lan |
| Oracle FCF âm & tài trợ quy mô lớn | - | ++ | 0 | + | Rủi ro áp lực tín dụng cục bộ |
| Nợ CoreWeave & xác minh DSCR | - | ++ | 0 | + | Điểm uốn tài chính 2027–2028 |
| Phần bù rủi ro trái phiếu AI kỳ hạn dài tăng | -- | ++ | 0 | + | Dịch chuyển 5pp từ P1 sang P2 |
| Cải thiện hiệu quả suy luận & offloading | - | 0 | ++ | 0 | Vẫn thiếu bằng chứng cấp độ sản xuất |
| Khả năng hấp thụ tài sản của hyperscaler | 0 | ++ | 0 | -- | Lý do P2 trội hơn P4 |

`++` và `--` chỉ biểu thị chiều hướng và không phải tỷ lệ xác suất thống kê.

### Lịch sử Điều chỉnh Xác suất

| Bước | P1 | P2 | P3 | P4 | Lý do |
|---|---:|---:|---:|---:|---|
| Khởi điểm | 40% | 35% | 15% | 10% | Thiếu cung vật lý chiếm ưu thế, rủi ro tài chính cục bộ, con đường cung/hiệu quả |
| Phản ánh suy yếu trái phiếu AI kỳ hạn dài | 35% | 40% | 15% | 10% | P1 sang P2 dịch 5pp; không có bằng chứng lây lan |
| Đánh giá lại capex hyperscaler | 35% | 40% | 15% | 10% | Tác động thực thi nhu cầu và tập trung tài sản bù trừ nhau |
| Đánh giá lại kịch bản dài hạn AI | 35% | 40% | 15% | 10% | 2027–2028 không thay đổi; chỉ xác suất P3 sau 2030 mở rộng |
| Đánh giá lại con đường cung Trung Quốc | 35% | 40% | 15% | 10% | Phản ánh rủi ro cung hàng hóa; thiếu bằng chứng chứng nhận khách hàng HBM |

### Phạm vi Không chắc chắn Xác suất và Quy tắc Điều chỉnh

| Con đường | Trung tâm | Phạm vi không chắc chắn | Tín hiệu mạnh có thể dịch chuyển ước tính trung tâm |
|---|---:|---:|---|
| P1 | 35% | 25–45% | Hai hoặc nhiều hyperscaler nâng hướng dẫn capex; chi phí tài trợ ổn định; hợp đồng dài hạn được củng cố |
| P2 | 40% | 30–50% | Một sự kiện áp lực nhà vận hành yếu thế với hyperscaler hấp thụ tài sản |
| P3 | 15% | 10–25% | Top-3 hoặc mở rộng cung Trung Quốc được xác nhận về khối lượng; mức tiêu thụ HBM trên mỗi token giảm |
| P4 | 10% | 5–15% | Nhiều nhà vận hành vỡ nợ, hai hoặc nhiều đợt cắt giảm capex và suy giảm hợp đồng dài hạn xảy ra đồng thời |

- Một bài báo đơn lẻ hoặc giai thoại chỉ đảm bảo điều chỉnh 0–2pp.
- Một tín hiệu mạnh đơn lẻ từ hồ sơ công ty hoặc báo cáo thu nhập đảm bảo điều chỉnh tối đa 5pp.
- Hai hoặc nhiều tín hiệu mạnh độc lập cùng chiều hướng đảm bảo dịch chuyển 5–10pp.
- Áp lực tín dụng cục bộ dịch chuyển xác suất từ P1 sang P2; bằng chứng lây lan dịch chuyển từ P2 sang P4; bằng chứng cung/hiệu quả dịch chuyển từ P1 sang P3.

## 8. Kịch Bản Cuối Cùng và Áp Lực Giá HBM

| Kịch bản | Xác suất | Trạng thái 2028 | Nhu cầu/Fleet 2030 | Áp lực giá HBM | Kết quả chính |
|---|---:|---|---:|---:|---|
| P1 Cầu vượt cung có trật tự | 35% | Nguồn cung căng hoặc cân bằng | 1,3–1,8× | Đi ngang đến -10% | Giá sàn hợp đồng giữ vững; lợi nhuận HBM ổn định ở mức cao |
| P2 Căng thẳng tín dụng cục bộ & Tái tập trung | 40% | Khoảng trống đơn hàng, dư thừa cung khiêm tốn | 0,9–1,3× | -15 đến -30% | Nhà khai thác yếu rút lui; hyperscaler tiếp nhận tài sản |
| P3 Cải thiện hiệu suất & Mở rộng cung | 15% | Dư thừa cung gia tăng | 0,6–0,9× | -20 đến -35% | Lượng token sử dụng tăng nhưng phần bù giá HBM bị nén |
| P4 Đóng băng tín dụng hệ thống | 10% | Cắt giảm capex và điều chỉnh tồn kho | 0,3–0,6× | -40 đến -55% | Đàm phán lại hợp đồng dài hạn, cắt giảm sản lượng, hủy capex, can thiệp chính sách |

Giữ nguyên tất cả các biến số khác, việc dịch chuyển 10 điểm phần trăm ra khỏi P2 sẽ làm thay đổi giá trị cuối 2028 như sau:

| Dịch chuyển xác suất | Thay đổi giá trị cuối Samsung | Thay đổi giá trị cuối SK Hynix | Ý nghĩa |
|---|---:|---:|---|
| 10pp từ P2 sang P1 | +21,800원 | +227,000원 | Xác suất thiếu cung kéo dài tăng lên |
| 10pp từ P2 sang P3 | -7,500원 | -70,000원 | Nền kinh tế AI tăng trưởng nhưng phần bù giá HBM bị nén |
| 10pp từ P2 sang P4 | -16,800원 | -132,000원 | Rủi ro căng thẳng cục bộ lan rộng thành rủi ro hệ thống |

SK Hynix nhạy cảm hơn với mọi dịch chuyển xác suất. Ngay cả khi sử dụng cùng xác suất trung tâm, biên độ sai số định giá và biến động giá cổ phiếu của SK Hynix đều lớn hơn do mức độ tập trung HBM cao hơn.

## 9. Mở Rộng Nguồn Cung Trung Quốc Là Biến Số Trong Mọi Kịch Bản, Không Phải Kịch Bản Riêng Biệt

Tăng trưởng công suất của CXMT và YMTC không phải là kịch bản thứ năm độc lập với P1–P4. Đây là biến số cung ứng làm thay đổi giá cả theo sản phẩm và thị phần trong mọi kịch bản.

| Giai đoạn tiến triển Trung Quốc | Thị trường bị ảnh hưởng trước | Samsung Electronics | SK Hynix | Ánh xạ kịch bản |
|---|---|---|---|---|
| CXMT mở rộng DDR4/DDR5/LPDDR nội địa | DRAM phổ thông | Áp lực ASP và danh mục sản phẩm | Tác động trực tiếp tương đối hạn chế | EPS bị cắt giảm trên tất cả kịch bản; xác suất không đổi |
| CXMT được công nhận bởi khách hàng PC toàn cầu | Client DDR5/LPDDR toàn cầu | Áp lực trần ASP và thị phần đồng thời | Rủi ro đối với mảng client | Rủi ro tăng của P3 |
| Trung Quốc thâm nhập RDIMM máy chủ phân khúc thấp | DRAM máy chủ tiêu chuẩn | Áp lực danh mục máy chủ một phần | DRAM ngoài máy chủ AI có nguy cơ | Xem xét lại tăng của P3 |
| YMTC tăng NAND nhiều lớp và được khách hàng chấp nhận | NAND tiêu dùng/SSD doanh nghiệp | Áp lực thị phần và biên NAND lớn nhất | Solidigm và SSD doanh nghiệp có nguy cơ | Giảm EPS và bội số P3 |
| Trung Quốc sản xuất đại trà HBM và được khách hàng AI công nhận | HBM | Bù đắp một phần từ việc bắt kịp HBM | Rủi ro phần bù khan hiếm lớn và thị phần | Dịch chuyển 5–10pp từ P1 sang P3 |
| Trung Quốc tăng tốc đồng thời với tốc độ capex AI toàn cầu chậm lại | Toàn bộ bộ nhớ | Áp lực kết hợp DRAM phổ thông/NAND/HBM | Áp lực kết hợp HBM/DRAM | Theo dõi lan rộng từ P3 sang P4 |

Trong giai đoạn 2026–2027, CXMT có khả năng kìm hãm trần giá client DDR5 và LPDDR nhiều hơn là trực tiếp làm suy yếu giá HBM. YMTC tương tự có thể thúc đẩy cạnh tranh giá trong NAND tiêu dùng và một số SSD doanh nghiệp trước.

Để Trung Quốc nổi lên như một mối đe dọa trực tiếp đối với HBM, chỉ sản xuất die DRAM là chưa đủ. Cần có đầy đủ: liên kết TSV, xếp chồng, tích hợp die nền, đóng gói tiên tiến, và nhiều lần công nhận sản xuất đại trà từ phía khách hàng AI.

Các tín hiệu sau đây phải được xác nhận trước khi mở rộng công suất Trung Quốc được tính toán một cách có ý nghĩa về mặt số lượng:

1. DDR5/LPDDR của CXMT được các nhà sản xuất PC toàn cầu sử dụng với số lượng lớn ở mức giá thấp hơn hơn 20% so với 3 nhà cung cấp bộ nhớ hàng đầu.
2. CXMT đạt được công nhận vượt ra ngoài PC tiêu dùng vào PC doanh nghiệp và server RDIMM.
3. NAND nhiều lớp của YMTC được xác nhận bằng khối lượng vận chuyển thực tế và đơn hàng từ khách hàng SSD doanh nghiệp — không chỉ là mục tiêu tuyên bố.
4. HBM Trung Quốc tiến từ công nhận mẫu thử sang công nhận sản xuất đại trà nhiều lần từ khách hàng chip tăng tốc AI.
5. Tăng trưởng cung và giảm giá DRAM/NAND phổ thông trong nhóm 3 nhà cung cấp hàng đầu được quan sát đồng thời trong hai hoặc nhiều quý liên tiếp.

## 10. Samsung Electronics: EPS và Giá Trị Hợp Lý Theo Kịch Bản

| Năm | Kịch bản | EPS | PER hợp lý | Giá trị cuối |
|---|---|---:|---:|---:|
| 2027 | P1 | 65,000원 | 8,5× | 552,500원 |
| 2027 | P2 | 62,000원 | 8,0× | 496,000원 |
| 2027 | P3 | 58,000원 | 7,5× | 435,000원 |
| 2027 | P4 | 45,000원 | 7,0× | 315,000원 |
| 2028 | P1 | 68,000원 | 8,5× | 578,000원 |
| 2028 | P2 | 45,000원 | 8,0× | 360,000원 |
| 2028 | P3 | 38,000원 | 7,5× | 285,000원 |
| 2028 | P4 | 24,000원 | 8,0× | 192,000원 |

PER nền trên 9× không được gán cho Samsung vì việc giảm lỗ mảng foundry chưa được xác nhận. Bội số 8,5× trong P1 chỉ có thể đạt được nếu phục hồi thị phần HBM, giá DRAM/NAND phổ thông và chuẩn hóa foundry cùng vận hành đồng thời.

Bội số 8,0× trong P4 được áp dụng để tránh lỗi chiết khấu kép khi nhân EPS đáy với PER cũng đang bị nén. Trong kịch bản suy thoái thực sự, cần xem xét đồng thời EPS chuẩn hóa, tiền mặt ròng và giá trị sổ sách.

## 11. SK Hynix: EPS và Giá Trị Hợp Lý Theo Kịch Bản

| Năm | Kịch bản | EPS | PER hợp lý | Giá trị cuối |
|---|---|---:|---:|---:|
| 2027 | P1 | 430,000원 | 9,0× | 3,870,000원 |
| 2027 | P2 | 405,000원 | 7,0× | 2,835,000원 |
| 2027 | P3 | 370,000원 | 6,0× | 2,220,000원 |
| 2027 | P4 | 250,000원 | 5,5× | 1,375,000원 |
| 2028 | P1 | 470,000원 | 9,0× | 4,230,000원 |
| 2028 | P2 | 280,000원 | 7,0× | 1,960,000원 |
| 2028 | P3 | 210,000원 | 6,0× | 1,260,000원 |
| 2028 | P4 | 80,000원 | 8,0× | 640,000원 |

Bội số 9× trong P1 giả định SK Hynix nắm giữ thị phần HBM, điều khoản hợp đồng dài hạn, ROE cao và được tái định giá có cấu trúc như một tài sản AI chiến lược. Duy trì bội số này đến 2028 đòi hỏi xác nhận bảo vệ thị phần HBM4E, tái định giá hợp đồng dài hạn và hoạt động trả cổ tức/mua lại cổ phiếu.

Giá mục tiêu 3,800,000원 của Korea Investment & Securities áp dụng bội số PBR 6,0× cho BPS dự phóng 12 tháng tới — vượt đỉnh dải lịch sử 5,0× được trích dẫn trong cùng báo cáo. Do đó, mục tiêu 3,800,000원 đòi hỏi không chỉ thực hiện được lợi nhuận mà còn phải có sự tái định giá cấu trúc của mảng kinh doanh bộ nhớ.

Trong P2 và P3, mức độ tập trung HBM chuyển từ lợi thế thành điểm dễ tổn thương. Khi ASP giảm, lợi nhuận và bội số định giá có thể bị nén đồng thời.

## 12. Kết Quả Bình Quân Gia Quyền Theo Xác Suất và So Sánh Điều Chỉnh Rủi Ro

| Năm | Công ty | EPS bình quân gia quyền | PER hỗn hợp hợp lý | Giá trị cuối bình quân gia quyền | PV chiết khấu 11%/năm | So với giá hiện tại |
|---|---|---:|---:|---:|---:|---:|
| 2027 | Samsung Electronics | 60,750원 | 8,04× | 488,525원 | 421,385원 | +65,6% |
| 2027 | SK Hynix | 393,000원 | 7,53× | 2,959,000원 | 2,552,333원 | +38,3% |
| 2028 | Samsung Electronics | 49,900원 | 8,18× | 408,250원 | 317,246원 | +24,7% |
| 2028 | SK Hynix | 316,000원 | 7,97× | 2,517,500원 | 1,956,316원 | +6,0% |

Bốn nhận xét rút ra từ các kết quả này:

1. Nhìn riêng qua lăng kính 2027, cả hai công ty đều có giá trị điều chỉnh rủi ro cao hơn giá hiện tại.
2. Một khi xác suất chuẩn hóa năm 2028 được chiết khấu, biên an toàn của Samsung rộng hơn.
3. Giá trị hiện tại năm 2028 của SK Hynix chỉ cao hơn 6% so với giá cổ phiếu hiện tại. Phần lớn kỳ vọng lợi nhuận phụ thuộc vào việc P1 được duy trì.
4. Bộ nhớ phổ thông, foundry và vị thế tiền mặt ròng của Samsung tạo ra vùng đệm giảm giá một phần trong P2 và P3.

Điều thị trường đã biết rõ là tình trạng thiếu cung HBM và giá bộ nhớ cao hơn. Điều có thể đang bị định giá sai theo hai chiều:

- Nếu việc Samsung bắt kịp HBM trùng khớp với sự phục hồi giá DRAM/NAND phổ thông, cả lợi nhuận lẫn bội số định giá đều có thể cải thiện cùng lúc.
- Nếu hợp đồng dài hạn và HBM4E của SK Hynix bảo vệ được giá sàn và thị phần ngay cả sau khi nguồn cung tăng thêm sau 2028, mức chiết khấu chuẩn hóa hiện tại có thể là quá mức.

Ngược lại, thị trường có thể đã đúng nếu cung ứng, hiệu suất và điều kiện tín dụng đều cải thiện đồng thời vào 2028, cắt ngắn lợi nhuận đỉnh chu kỳ.

## 13. Cách Nhìn Nhận Nhu Cầu AI Dài Hạn Sau Năm 2030

[AI 2040 Plan A](https://ai-2040.com/?choices=plan-a-root) trình bày lộ trình từ khoảng 20 triệu H100e vào năm 2026 lên 60 tỷ H100e vào năm 2034, với mức tiêu thụ điện năng cho tính toán AI đạt 5TW vào năm 2034. Tuy nhiên, chính tài liệu này mô tả đây là kịch bản chính sách, không phải dự báo ước tính tốt nhất, và lưu ý rằng một số biến số đã được điều chỉnh theo sát với câu chuyện dẫn dắt.

Do đó, các kịch bản dài hạn không được đưa trực tiếp vào ước tính EPS giai đoạn 2027–2028.

| Giai đoạn | P1 Cầu Vượt Cung | P2 Tái Tập Trung | P3 Tăng Trưởng Sản Lượng / Bình Thường Hóa Giá | P4 Thất Bại | Trạng thái |
|---|---:|---:|---:|---:|---|
| 2026–2028 | 35% | 40% | 15% | 10% | Xác suất phân tích hiện tại |
| Đường cơ sở có điều kiện hậu 2030 | 25% | 35% | 30% | 10% | Nhận định dài hạn; không phải xác suất thống kê |

Nếu AI và robot nâng cao hiệu quả thiết kế chip, xây dựng nhà máy và sản xuất, tổng nhu cầu bit bộ nhớ có thể tăng trong khi phần bù khan hiếm đặc thù của HBM thu hẹp lại. <strong>Do đó, quy mô thị trường HBM mở rộng và việc mở rộng PER dài hạn cần được đánh giá riêng biệt.</strong>

Khi nhu cầu bộ nhớ dài hạn tăng lên, không gian cơ hội mở rộng không chỉ cho HBM mà còn cho DRAM thông thường, NAND, SSD doanh nghiệp, bộ điều khiển, CXL, nguồn điện, làm mát và liên kết. Đây là lợi thế tương đối của Samsung với danh mục sản phẩm đa dạng hơn.

## 14. Những Điều Kiện Cần Hiện Thực Hóa Để Phân Tích Này Duy Trì Giá Trị

### Samsung Electronics

1. Việc khách hàng chứng nhận HBM4 và HBM4E phải chuyển hóa thành khối lượng sản xuất hàng loạt thực tế và thị phần doanh thu.
2. Phục hồi giá hợp đồng DRAM và NAND thông thường phải bù đắp được chi phí đầu tư HBM, tiền thưởng và dự phòng.
3. Thua lỗ mảng đúc chip phải thu hẹp và bắt đầu đóng góp có ý nghĩa vào lợi nhuận 2027–2028.
4. Tiền mặt ròng và năng lực hoàn trả cổ đông phải được duy trì bất chấp capex nặng nề.

### SK Hynix

1. Thị phần HBM4E và mức sàn giá hợp đồng dài hạn phải giữ vững ngay cả khi Samsung và Micron mở rộng cung.
2. Việc tái định giá HBM bắt đầu từ Q4 2026 phải hướng tới mức bình quân 2027 là $2,82/Gb.
3. Điểm yếu về năng suất TSV và xếp chồng phải được chứng minh là tạm thời và quy về chi phí chuyển đổi sản phẩm.
4. Dòng tiền tự do cao phải chảy vào hoàn trả cổ đông và chính sách vốn, không chỉ mở rộng công suất.

## 15. Tín Hiệu Rủi Ro và Chỉ Báo Dẫn Dắt

| Rủi ro | Chỉ báo dẫn dắt | Tác động đến Samsung | Tác động đến SK Hynix | Điều chỉnh phân tích |
|---|---|---|---|---|
| Đàm phán lại hợp đồng dài hạn HBM | Sàn giá, trả trước và mức mua tối thiểu suy yếu | Vừa phải | Rất lớn | P2/P4 tăng |
| Cắt giảm hướng dẫn capex của hyperscaler | Hai hoặc nhiều hơn hướng dẫn cắt giảm đồng thời | Lớn | Rất lớn | P2/P4 tăng |
| Sự kiện tái cấp vốn trung tâm dữ liệu AI | Điều khoản giao ước CoreWeave/chi phí tài chính, cấp vốn Oracle | Vừa phải | Lớn | P2 tăng; P4 tăng nếu lây lan |
| Mở rộng cung tăng tốc | Sản lượng HBM có khả năng sản xuất lớn của Samsung/Micron tăng | Tích cực cho bắt kịp HBM; tiêu cực cho định giá | Rất tiêu cực | P3 tăng |
| Cải thiện hiệu quả suy luận đột ngột | Bit HBM trên mỗi token giảm | Danh mục sản phẩm rộng cung cấp bộ đệm một phần | Tiêu cực | Bội số HBM giảm |
| Mở rộng cung hàng hóa Trung Quốc | Định giá CXMT/YMTC, thị phần, chứng nhận khách hàng toàn cầu | Tiêu cực hơn cho DRAM/NAND thông thường | Client DRAM và Solidigm chịu áp lực | Giảm EPS theo sản phẩm |
| Thách thức HBM từ Trung Quốc | TSV/xếp chồng/die nền/đóng gói/chứng nhận khách hàng | Bù đắp một phần giá trị bắt kịp HBM | Rất tiêu cực cho phần bù khan hiếm | Dịch chuyển P1 sang P3 |
| Thất bại bình thường hóa đúc chip | Tiếp tục thua lỗ, không cải thiện năng suất | Rủi ro riêng của Samsung | Tác động hạn chế | Giảm bội số P1 của Samsung |

### Tín Hiệu Tăng Giá

- Hợp đồng dài hạn HBM 2028 với khối lượng và giá cao hơn và đa dạng hóa khách hàng rộng hơn
- Ổn định sớm năng suất HBM4E và khối lượng sản xuất hàng loạt
- Xác nhận đồng thời thị phần HBM đang tăng của Samsung và thua lỗ đúc chip thu hẹp
- Doanh thu dịch vụ AI và dòng tiền tăng nhanh hơn hợp đồng tài nguyên tính toán
- Thời gian giao hàng và phân bổ HBM duy trì ngay cả khi mở rộng cung bị trì hoãn
- Kế hoạch hoàn trả cổ đông của SK Hynix trở nên cụ thể

### Tín Hiệu Giảm Giá

- Giảm ASP HBM và sụt giảm khối lượng vận chuyển xảy ra đồng thời
- Hai hoặc nhiều hyperscaler lớn hạ thấp tốc độ tăng trưởng capex
- Đàm phán lại, vi phạm hoặc suy giảm khoản trả trước hợp đồng dài hạn
- Tích lũy tồn kho bộ nhớ và giá hợp đồng thấp hơn giá giao ngay
- Mức tiêu thụ HBM trên mỗi token của dịch vụ AI thực tế giảm hơn 20% trong hai quý liên tiếp
- Tăng cung sản lượng Samsung/Micron trùng với sụt giảm phần bù HBM

Trên cơ sở hàng tháng, các chỉ báo cần theo dõi cùng nhau là: giá hợp đồng và khoản trả trước HBM4/4E, khối lượng và năng suất của 3 nhà sản xuất bộ nhớ hàng đầu, thời gian giao hàng đóng gói tiên tiến, capex và dòng tiền của hyperscaler, chi phí tài chính Oracle và CoreWeave, doanh thu ODM máy chủ Đài Loan, và giá hợp đồng và tồn kho DRAM/NAND.

## 16. Diễn Giải Đầu Tư Tương Đối

Hai cổ phiếu không phải là những cách tương đương để mua cùng một chu kỳ tăng bộ nhớ.

| Kịch bản | Samsung Electronics | SK Hynix |
|---|---|---|
| P1 Tăng cường | Bắt kịp HBM và thuận lợi bộ nhớ thông thường | Đòn bẩy lợi nhuận lớn nhất từ thị phần HBM và hợp đồng dài hạn |
| P2 Cảnh báo | Đa dạng hóa kinh doanh và tiền mặt ròng cung cấp phòng thủ một phần | Nhạy cảm hơn với khoảng cách đơn hàng và nén bội số |
| P3 Tăng cường | Danh mục sản phẩm bộ nhớ rộng và thực thi đúc chip cung cấp bộ đệm một phần | Phơi lộ trực tiếp trước nén phần bù HBM |
| P4 Cảnh báo | Sụt giảm tuyệt đối không thể tránh khỏi nhưng phòng thủ tương đối có thể thực hiện | Rủi ro lớn nhất về sụt giảm đồng thời lợi nhuận và bội số |

Từ góc độ điều chỉnh rủi ro, Samsung cung cấp lựa chọn rộng hơn và mang tính phòng thủ hơn. SK Hynix có đòn bẩy lợi nhuận lớn hơn trong P1, nhưng định giá của nó dịch chuyển nhanh hơn khi điều kiện cung, hiệu quả và tín dụng thay đổi.

Các cổ phiếu thiết bị và vật liệu cũng không nên được gom vào nhóm một cách tùy tiện. Các công ty thiết bị tiếp xúc với khoảng cách đơn hàng phải được tách biệt khỏi nhà cung cấp hàng tiêu hao và phụ tùng có doanh thu theo tỷ lệ sử dụng. Thiết bị có đơn đặt hàng đã được xác nhận và linh kiện/vật liệu có dòng doanh thu tái diễn phù hợp hơn với khung kịch bản này so với giỏ thuần túy theo chủ đề HBM.

## 17. Kết Luận

Đà tăng trưởng bộ nhớ đến năm 2027 có thể được duy trì là lộ trình trung tâm cho ước tính lợi nhuận. Nhưng bài kiểm tra thực sự của giá cổ phiếu hiện tại không phải là EPS 2027 — mà là thời gian kéo dài của lợi nhuận sau năm 2028. Lập luận rằng thâm hụt cung HBM kéo dài lâu hơn các chu kỳ trước, và lập luận rằng các công ty bộ nhớ xứng đáng được hưởng bội số khan hiếm nâng cao vĩnh viễn, không phải là cùng một lập luận.

Samsung Electronics nắm giữ đồng thời tiềm năng bắt kịp HBM, DRAM/NAND thông thường, hoạt động đúc chip và tiền mặt ròng, cung cấp lợi thế P1 và phòng thủ giảm giá tương đối qua P2–P4. Thị phần HBM và hợp đồng dài hạn của SK Hynix cung cấp đòn bẩy lợi nhuận cao nhất trong P1, nhưng nếu điều kiện cung, hiệu quả và tài chính bình thường hóa, lợi nhuận và bội số có thể nén lại cùng nhau.

Kết quả có trọng số xác suất hiện tại cho thấy: <strong>đến năm 2027, cả hai công ty đều cung cấp lợi thế tăng giá đáng kể; nhìn xuyên đến năm 2028, biên an toàn điều chỉnh rủi ro của Samsung rộng hơn.</strong> Để SK Hynix được định giá lại thêm, cần có xác nhận rằng năng suất HBM4E, điều khoản hợp đồng dài hạn 2028 và tài chính cơ sở hạ tầng AI tiếp tục hỗ trợ P1.

## Các Mục Chưa Thể Xác Nhận Từ Nguồn Công Khai

1. EPS theo phân khúc của Samsung Electronics cho 2027–2028 và độ nhạy bình thường hóa đúc chip
2. Trọng số khách hàng hợp đồng dài hạn SK Hynix, công thức tái định giá và điều khoản trả trước/mua tối thiểu
3. Đầu vào wafer dành riêng cho HBM, năng suất die tốt và xếp chồng, và khối lượng có thể sản xuất theo khách hàng của 3 nhà sản xuất bộ nhớ hàng đầu
4. Thành phần capex hyperscaler 2028 giữa dòng tiền nội bộ, trái phiếu doanh nghiệp và tài chính dự án
5. Lịch tái cấp vốn CoreWeave và Oracle và dư địa điều khoản giao ước
6. Thay đổi dung lượng, băng thông và tỷ lệ lưu trú bộ nhớ HBM4E theo thế hệ trên mỗi bộ tăng tốc
7. Khối lượng vận chuyển thực tế CXMT/YMTC, chứng nhận khách hàng toàn cầu và độ nhạy lợi nhuận theo sản phẩm

## Nguồn Tham Khảo Chính

- [Korea Investment & Securities, SK Hynix Xem Trước Kết Quả Q2/2026, 2026-07-13](https://vo.la/fd9udR9)
- [Korea Investment & Securities, "Khởi Đầu Bắt Đầu Từ Bây Giờ," 2026-05-20](https://vo.la/jBPy7zV)
- [Korea Invest Insights, Mô Hình Cung-Cầu HBM 2030 Kiểm Chứng Chéo](/vi/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/)
- [AI 2040, Phương Án A](https://ai-2040.com/?choices=plan-a-root)
- [AI 2040, Phụ Lục Điện Toán](https://ai-2040.com/supplements/compute-supplement)
- [AI 2040, Kinh Tế Học Của Phương Án A](https://ai-2040.com/supplements/economics-of-plan-a)
- [Oracle Kết Quả Tài Chính FY2026](https://www.oracle.com/news/announcement/q4fy26-earnings-release-2026-06-10/)
- [CoreWeave Báo Cáo Form 10-K Năm 2025](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm)
- [CoreWeave DDTL 4.0 Form 8-K](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000129/crwv-20260330.htm)

Xác suất kịch bản và giá trị hợp lý được trình bày trong báo cáo này là các ước tính phân tích dựa trên thông tin công khai và không cấu thành tư vấn đầu tư cá nhân hóa. Quyết định đầu tư thực tế cần tính riêng đến biến động giá, kỳ hạn đầu tư, thuế, rủi ro tỷ giá, và khả năng chịu đựng thua lỗ của từng cá nhân.
