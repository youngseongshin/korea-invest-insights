---
title: "Bán dẫn có mang tính chu kỳ không và giá hợp lý là bao nhiêu? Định giá Samsung, SK Hynix và Micron bằng FCFE và lợi nhuận chuẩn hóa"
slug: "memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17"
date: 2026-07-17T20:00:00+09:00
description: "Samsung ở mức 3,9 lần và SK Hynix 4,3 lần theo đồng thuận 2028 có nghĩa thị trường nghi ngờ thời gian duy trì của lợi nhuận đó, chứ không phải sự tồn tại của nó. Bài viết lần lượt giải quyết: bán dẫn có chu kỳ không, hệ số nào phù hợp với EPS nào, tranh luận hiện tại lay động EPS 2028 hay chỉ hệ số, vì sao 2029 không quá xa, và dòng tiền 2026-2028 thực sự đi đâu, rồi tính giá hợp lý gia quyền xác suất bằng FCFE cộng giá trị cuối kỳ chuẩn hóa."
categories: ["Exclusive Analysis", "Valuation", "Tech-Analysis"]
tags: ["Samsung Electronics", "SK Hynix", "Micron", "Bộ nhớ", "HBM", "Định giá", "FCFE", "Chu kỳ", "Lợi nhuận chuẩn hóa", "Giá hợp lý"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Bối cảnh
> Bài viết này là phần tiếp theo của [Đâu là điểm tranh cãi thực sự giữa phe tăng giá và phe giảm giá bán dẫn](/vi/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/), bài đã kết luận rằng "ngành thì bull nhưng giá cổ phiếu thì valuation bear", và đây là phần tính định lượng <strong>vậy giá bao nhiêu mới là hợp lý</strong>. Nếu [Định giá lợi nhuận 2028E của Samsung Electronics và SK Hynix](/vi/post/samsung-hynix-2028e-profit-valuation-cycle-scenarios-2026-07-09/) đã bàn về "những con số trông có vẻ rẻ", thì bài này tính ra giá hợp lý bằng FCFE và giá trị cuối kỳ chuẩn hóa. Nên đọc cùng với [Kịch bản xấu nhất đã được phản ánh vào giá](/vi/post/samsung-hynix-worst-case-eps-priced-in-consensus-dispersion-2026-07-10/) và [SK Hynix hạ lợi nhuận quý 2](/vi/post/sk-hynix-2q-earnings-cut-mirae-kis-lta-target-price-2026-07-14/). Các hub liên quan là [Hub AI HBM](/vi/page/korea-semiconductor-hbm-kospi-hub/) và [Hub Exclusive Analysis](/vi/page/exclusive-analysis-hub/).

## TL;DR

* Lấy giá đóng cửa KRX ngày 17/7 (Samsung Electronics 255.000 KRW, SK Hynix 1.842.000 KRW) chia cho EPS đồng thuận 2028 tính đến ngày 16/7, PER lần lượt là <strong>3,9 lần và 4,3 lần</strong>. Thị trường không cho rằng lợi nhuận năm 2028 sẽ biến mất, mà đang phản ánh vào giá <strong>khả năng lợi nhuận đó không kéo dài lâu</strong>.
* Bán dẫn không thể gộp thành một ngành duy nhất. Bộ nhớ vẫn mang tính chu kỳ, còn HBM không phải sản phẩm xóa bỏ chu kỳ mà là sản phẩm <strong>kéo dài thời gian duy trì và làm giảm độ co giãn của nguồn cung</strong>.
* Tranh luận hiện tại bề ngoài lay động hệ số trước. Nhưng vì ý nghĩa kinh tế của việc hệ số giảm chính là phản ánh trước sự chuẩn hóa EPS sau năm 2028, nên không thể tách hoàn toàn vấn đề hệ số khỏi vấn đề EPS.
* Câu hỏi "lấy mốc năm 2028 hay mốc năm 2029" sai ngay từ tiền đề. Giá cổ phiếu là <strong>giá trị hiện tại của dòng tiền thuộc về cổ đông phát sinh vĩnh viễn kể từ năm 2026</strong>. Cách gắn PER thấp cho EPS 2028 và cách gắn PER bình thường cho EPS chuẩn hóa 2029 sẽ cho cùng một đáp số nếu giả định nhất quán.
* Giá hợp lý gia quyền xác suất tính bằng FCFE và giá trị cuối kỳ chuẩn hóa là <strong>Samsung Electronics 385.000 KRW (+51%), SK Hynix 1.950.000 KRW (+6%), Micron 1.140 USD (+34%)</strong>. Mức độ hấp dẫn đã điều chỉnh rủi ro xếp theo thứ tự Samsung Electronics, Micron, SK Hynix. \[Suy luận: tự tính toán\]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Luận điểm chính</div>
  <div class="thesis-callout__body">
    Tiền đề cho rằng giá cổ phiếu phải chọn một trong hai, EPS năm 2028 hoặc EPS năm 2029, tự nó đã không chính xác. Cách đúng là cộng FCFE giai đoạn 2026-2028 với giá trị cuối kỳ chuẩn hóa năm 2029, và khi tính theo cách này, biên an toàn của ba cổ phiếu nới rộng dần theo thứ tự Samsung Electronics, Micron, SK Hynix.
  </div>
</div>

---

## 1. Bán dẫn có mang tính chu kỳ không

Không có một câu trả lời duy nhất. Cường độ chu kỳ khác nhau theo từng phân khúc.

| Lĩnh vực | Tính chất chu kỳ | Lý do |
|---|---|---|
| DRAM, NAND phổ thông | Rất mạnh | Tính đồng nhất sản phẩm, tồn kho, biến động trong mở rộng công suất và ASP |
| HBM | Trung bình đến mạnh | Chứng nhận, xếp lớp, LTA là rào cản gia nhập, nhưng biên lợi nhuận cao lại kích thích mở rộng công suất và đa nguồn cung |
| Foundry, thiết bị | Trung bình đến mạnh | CAPEX của khách hàng và chu kỳ chuyển đổi công nghệ sản xuất |
| Fabless, nền tảng | Chênh lệch lớn theo từng sản phẩm | Có hào kinh tế nhưng vẫn phơi nhiễm với chuyển thế hệ sản phẩm và CAPEX của khách hàng |

Cách diễn đạt chính xác nhất là <strong>"ngành tăng trưởng về cấu trúc nhưng giá và lợi nhuận vận động theo chu kỳ"</strong>.

Mức độ phơi nhiễm khác nhau theo từng cổ phiếu. SK Hynix có độ phơi nhiễm thuần túy nhất với bộ nhớ và HBM. Samsung Electronics có độ nhạy lợi nhuận lớn trong giai đoạn bộ nhớ bùng nổ, nhưng mảng di động, màn hình, foundry và tiền mặt giúp đệm bớt một phần rủi ro giảm giá.

### Bản thân công ty nói gì

Nhận định này không phải cách diễn giải của người quan sát mà dựa trên <strong>tài liệu chính thức của công ty</strong>. \[Thực tế: hồ sơ SEC\]

Trong hồ sơ F-1 nộp tại Mỹ, SK Hynix quy định ngành bộ nhớ là <strong>highly cyclical</strong>. Trong báo cáo 10-Q, Micron nêu rõ rằng HBM đòi hỏi nhiều wafer và diện tích phòng sạch hơn để sản xuất cùng một lượng bit so với DRAM phổ thông, nhưng <strong>nếu nhu cầu HBM suy yếu và công suất đó quay trở lại sản xuất DRAM phổ thông, nguồn cung DRAM có thể tăng vọt</strong>.

Ghép hai điều này lại, ta có kết luận. HBM chỉ làm chậm phản ứng nguồn cung chứ không loại bỏ chu kỳ. \[Suy luận: tổng hợp từ hai hồ sơ\]

---

## 2. Hệ số hợp lý là bao nhiêu

Muốn bàn về PER hợp lý, trước tiên phải xác định <strong>áp dụng cho EPS nào</strong>. Cùng là 8 lần, nếu gắn vào lợi nhuận đỉnh chu kỳ thì đắt, còn gắn vào lợi nhuận chuẩn hóa thì hợp lý.

| Lợi nhuận áp dụng | Samsung Electronics | SK Hynix | Diễn giải |
|---|---:|---:|---|
| EPS đỉnh chu kỳ 2027-2028 | 5,5-7,5 lần | 5-7 lần | Chiết khấu cho quá trình chuẩn hóa lợi nhuận sau đó |
| EPS chuẩn hóa | 8-10 lần | 7-9 lần | Áp dụng cho lợi nhuận bình quân 3-5 năm |
| Xác nhận cao nguyên cấu trúc | 9-11 lần | 8-10 lần | Chỉ cho phép khi lợi nhuận vẫn được bảo vệ sau năm 2029 |

Mức trên 9 lần của Samsung Electronics cần được xác nhận đồng thời bằng sự phục hồi thị phần HBM và thu hẹp lỗ mảng foundry. Mức 8-10 lần của SK Hynix cần thị phần HBM4E, tái định giá LTA, hoàn trả cổ đông và khả năng bảo vệ biên lợi nhuận sau khi nguồn cung tăng.

Vì vậy, <strong>việc áp thẳng 9-12 lần lên đồng thuận 2028 là một kịch bản tăng giá mạnh, dùng đồng thời lợi nhuận đỉnh chu kỳ và hệ số mang tính cấu trúc</strong>. Ở doanh nghiệp mang tính chu kỳ, PER thường thấp nhất tại đỉnh chu kỳ, còn tại đáy suy thoái thì cao nhất, hoặc thậm chí không tính được. Terminal value phải được tính bằng lợi nhuận chuẩn hóa, không phải đỉnh hay đáy chu kỳ. \[Thực tế: phương pháp luận định giá doanh nghiệp chu kỳ của McKinsey\]

---

## 3. Tranh luận hiện tại đang lay động EPS, hay chỉ lay động hệ số

Tách theo từng tranh luận thì câu trả lời sẽ khác nhau.

| Tranh luận | Tác động trước mắt | Điều kiện để ảnh hưởng cả đến EPS |
|---|---|---|
| Giải chấp đòn bẩy ở một cổ phiếu đơn lẻ | Hệ số, cung cầu | Không có, vì đây là yếu tố kỹ thuật |
| Lo ngại lãi suất, trái phiếu AI, ROI | Hệ số là chính | Từ 2 Big Tech trở lên hạ CAPEX |
| Sức ép giảm giá từ người mua | Hệ số cộng rủi ro EPS | Giá hợp đồng giảm và đơn hàng giảm cùng lúc |
| Ba hãng bộ nhớ mở rộng công suất | EPS 2028, hệ số | Sản lượng đạt chuẩn thực tế và nguồn cung bit tăng |
| CXMT, YMTC | Hệ số dài hạn là chính | Chứng nhận toàn cầu, xuất xưởng quy mô lớn, sức ép giá |
| Nút thắt LTA, đóng gói HBM | Bảo vệ cả EPS lẫn hệ số | Duy trì giá sàn và sản lượng theo hợp đồng |

### Con số của giới phân tích vẫn chưa nhúc nhích

Theo WiseReport nội địa, EPS 2028 của Samsung Electronics giữ nguyên ở mức 65.907 KRW vào cả ngày 13/7 lẫn 16/7. Của SK Hynix giảm từ 433.625 KRW xuống 427.332 KRW, tương đương <strong>1,5%</strong>. \[Thực tế: đồng thuận WiseReport\]

Nói cách khác, con số của giới phân tích gần như không đổi, còn <strong>giá cổ phiếu đã di chuyển trước</strong>.

### Nhưng cũng không chỉ hạ mỗi hệ số

Nếu giải ngược PER chuẩn hóa 8 lần, ta sẽ ra mức EPS mà thị trường đang chấp nhận.

| Cổ phiếu | EPS giải ngược từ 8 lần | Đồng thuận 2028 | Chênh lệch |
|---|---:|---:|---:|
| Samsung Electronics | 31.875 KRW | 65.907 KRW | -52% |
| SK Hynix | 230.250 KRW | 427.332 KRW | -46% |

Thị trường đang phản ánh pha trộn hai trường hợp sau.

1. EPS 2028 gần với đồng thuận, nhưng giảm nhanh kể từ năm 2029.
2. Bản thân EPS 2028 đã bị hạ thấp do mở rộng nguồn cung và sức ép giảm giá từ người mua.

Dữ liệu xác nhận được đến hiện tại <strong>gần với trường hợp 1 hơn</strong>. Vì việc hủy CAPEX, giá hợp đồng giảm, tồn kho tăng và đàm phán lại LTA vẫn chưa được xác nhận cùng lúc. Tuy vậy, mở rộng công suất và sức ép từ người mua là những biến số thực tế có thể đẩy tình huống sang trường hợp 2. \[Suy luận: diễn giải dữ liệu\]

Đợt điều chỉnh hiện tại chưa phải là giai đoạn thị trường hạ dự báo lợi nhuận, mà là <strong>sự đánh giá lại thời gian duy trì của lợi nhuận</strong>. Tuy nhiên, bản chất của mối lo mà thị trường thể hiện qua hệ số chính là EPS sau năm 2028, và nếu giá hợp đồng, tồn kho, CAPEX xấu đi, tình huống sẽ chuyển thành giai đoạn hạ EPS 2028.

---

## 4. Lấy mốc năm 2028 hay mốc năm 2029

Tiền đề của câu hỏi này ngay từ đầu đã không chính xác. Giá cổ phiếu không được xác định bởi một trong hai mốc đó. Nó là <strong>giá trị hiện tại của dòng tiền thuộc về cổ đông phát sinh vĩnh viễn kể từ năm 2026</strong>.

```text
Giá trị hiện tại
= Giá trị hiện tại của FCFE giai đoạn 2026-2028
+ Giá trị hiện tại của giá trị cuối kỳ cuối năm 2028

Giá trị cuối kỳ cuối năm 2028 ≈ EPS chuẩn hóa năm 2029 × PER chuẩn hóa
```

Cách dùng EPS 2028 không phải là bỏ qua giai đoạn sau năm 2029. Đó là cách <strong>nén rủi ro suy giảm sau năm 2029 vào trong mức PER thấp gắn cho EPS 2028</strong>. Nếu dùng trực tiếp EPS chuẩn hóa 2029, ta có thể gắn một mức PER bình thường hơn. Nếu giả định nhất quán, kết quả của hai cách phải tương tự nhau.

Đây thực chất chỉ là hai cách diễn đạt cùng một điều, nhưng nhiều khi người ta vẫn tranh cãi xem cách nào mới đúng.

---

## 5. Năm 2029 có phải là tương lai quá xa

Ba năm không phải là khoảng cách xa trong định giá cổ phiếu. Với tỷ suất sinh lời yêu cầu 11%, 1 đồng của năm 2029 hiện có giá trị hiện tại khoảng 0,73 đồng.

```text
1/(1,11)^3 = 0,731
```

Dù nhà đầu tư bán cổ phiếu sau 1 năm, <strong>người mua tại thời điểm đó vẫn nhìn vào dòng tiền từ sau năm 2029</strong>. Vì giá bán cuối cùng lại do dòng tiền tương lai quyết định, nên dù kỳ đầu tư ngắn cũng không thể tránh khỏi lợi nhuận dài hạn. Mô hình FCFE của Damodaran cũng tính giá trị cổ phiếu bằng tổng FCFE trong giai đoạn dự phóng rõ ràng cộng với giá trị cuối kỳ sau đó. \[Thực tế: mô hình FCFE của NYU Stern\]

---

## 6. Dòng tiền giai đoạn 2026-2028 có được tính đến không

Có được tính đến. Nhưng <strong>EPS và dòng tiền thực sự về tay cổ đông là hai thứ khác nhau</strong>.

Tổng hợp đồng thuận WiseReport ngày 16/7 cho kết quả sau. \[Thực tế: tổng hợp đồng thuận\]

| Cổ phiếu | EPS 2026E | EPS 2027E | EPS 2028E | EPS lũy kế 3 năm | So với giá hiện tại |
|---|---:|---:|---:|---:|---:|
| Samsung Electronics | 46.664 KRW | 65.802 KRW | 65.907 KRW | 178.373 KRW | 70% |
| SK Hynix | 314.787 KRW | 438.114 KRW | 427.332 KRW | 1.180.233 KRW | 64% |

Nếu đồng thuận trở thành hiện thực, lợi nhuận lũy kế 3 năm tương đương 64-70% giá hiện tại, một quy mô không thể bỏ qua.

Vấn đề là lợi nhuận kế toán không đồng nghĩa với tiền mặt về tay cổ đông.

```text
FCFE = Lợi nhuận ròng - CAPEX ròng - Tăng vốn lưu động + Vay ròng
```

Các hãng bộ nhớ tăng mạnh đầu tư vào fab, EUV, đóng gói trong giai đoạn bùng nổ. Nếu dùng 60 trong 100 đơn vị lợi nhuận ròng để mở rộng công suất, phần tiền mặt về tay cổ đông ngay lập tức chỉ còn 40. 60 đơn vị còn lại không hẳn biến mất, nhưng <strong>chỉ trở thành giá trị khi thiết bị mới tạo ra lợi nhuận vượt chi phí vốn</strong>.

Lợi nhuận giai đoạn 2026-2028 được phản ánh vào giá cổ phiếu thông qua cổ tức, mua lại cổ phiếu quỹ, tăng tiền mặt ròng, giảm nợ, tăng giá trị sổ sách và mở rộng công suất có hiệu suất sinh lời cao. Ngược lại, nếu dư cung xuất hiện ngay sau khi mở rộng công suất, tiền mặt sẽ biến thành thiết bị và kéo cả ROE tương lai đi xuống. Đây là lý do thị trường không định giá lợi nhuận ròng thời kỳ bùng nổ theo tỷ lệ 1 đồng ăn 1 đồng.

### Hai kịch bản mà giá hiện tại đang phản ánh

Giá hiện tại tương đương 3,9 lần đồng thuận 2028 với Samsung Electronics và 4,3 lần với SK Hynix. Thị trường đang pha trộn hai yếu tố sau.

1. Phần lớn lợi nhuận giai đoạn 2026-2028 được tái đầu tư vào mở rộng công suất.
2. ASP và biên lợi nhuận chuẩn hóa trở lại kể từ năm 2029.

Vì vậy, biến số quyết định không phải là "EPS 2029 có giảm hay không" mà là <strong>mức độ giảm</strong> và <strong>tỷ lệ lợi nhuận giai đoạn 2026-2028 thực sự còn lại dưới dạng FCFE, tiền mặt ròng</strong>.

| Kịch bản 2029 | Cách đánh giá |
|---|---|
| EPS giảm 10-20%, sau đó ổn định | FCFE tường minh cộng PER chuẩn hóa 8-10 lần |
| EPS giảm 30-50%, sau đó phục hồi | FCFE tường minh cộng EPS chuẩn hóa 7-9 lần |
| EPS giảm trên 50%, dư cung kéo dài | PBR chuẩn hóa, tiền mặt ròng, giá trị cắt giảm sản lượng thay vì PER |

McKinsey cũng cho rằng doanh nghiệp mang tính chu kỳ cần gia quyền xác suất giữa kịch bản chu kỳ bình thường và kịch bản thay đổi cấu trúc, đồng thời tính giá trị cuối kỳ bằng dòng tiền chuẩn hóa chứ không phải đỉnh hay đáy chu kỳ. \[Thực tế: phương pháp luận McKinsey\]

---

## 7. Tính chi tiết thì giá hợp lý là bao nhiêu

Đưa khung phân tích trên vào số liệu thực tế. Giá hợp lý gia quyền xác suất tính đến ngày 17/7/2026 như sau. \[Suy luận: tự tính toán, giả định được nêu rõ bên dưới\]

### Phương pháp tính

```text
Giá hợp lý = FCF còn lại 2026 + FCF 2027 + FCF 2028 + Giá trị cuối kỳ cuối năm 2028
Giá trị cuối kỳ = EPS chuẩn hóa 2029 × PER hợp lý
```

- <strong>Tỷ lệ chiết khấu</strong>: Samsung Electronics 10,5%, SK Hynix 11,5%, Micron 10,5%
- <strong>Xác suất</strong>: nhu cầu vượt cung 30%, đơn hàng trống, tái tập trung 40%, nguồn cung bình thường hóa 20%, đoản mạch tín dụng 10%
- <strong>PER cuối kỳ</strong>: Samsung Electronics 7,5-8,5 lần, SK Hynix 6-9 lần, Micron 7-9,5 lần
- <strong>Xử lý pha suy giảm chu kỳ</strong>: phản ánh 45-90% phần lợi nhuận sụt giảm vào FCF, áp dụng đồng thời CAPEX cố định và khả năng cắt giảm

### Kết quả

| Cổ phiếu | Giá hiện tại | Giá hợp lý gia quyền xác suất | Dư địa tăng | Khoảng biến động theo độ nhạy |
|---|---:|---:|---:|---:|
| Samsung Electronics | 255.000 KRW | <strong>385.000 KRW</strong> | +51% | 316.000-461.000 KRW |
| SK Hynix | 1.842.000 KRW | <strong>1.950.000 KRW</strong> | +6% | 1.480.000-2.480.000 KRW |
| Micron | 853,20 USD | <strong>1.140 USD</strong> | +34% | 905-1.410 USD |

Khoảng biến động theo độ nhạy là kết quả khi dịch chuyển đồng thời xác suất nhu cầu vượt cung và bình thường hóa nguồn cung 10 điểm phần trăm, tỷ lệ chiết khấu ±1,5 điểm phần trăm, và PER cuối kỳ ±1 lần.

### Giá trị hiện tại theo từng kịch bản

| Kịch bản | Xác suất | Samsung Electronics | SK Hynix | Micron |
|---|---:|---:|---:|---:|
| Nhu cầu vượt cung tiếp diễn | 30% | 548.000 KRW | 3.415.000 KRW | 1.735 USD |
| Đơn hàng trống, tái tập trung | 40% | 347.000 KRW | 1.581.000 KRW | 1.086 USD |
| Nguồn cung, hiệu suất bình thường hóa | 20% | 283.000 KRW | 1.064.000 KRW | 674 USD |
| Đoản mạch tín dụng hệ thống | 10% | 241.000 KRW | 732.000 KRW | 505 USD |

Bảng này cho thấy sự khác biệt về tính chất giữa ba cổ phiếu. <strong>Samsung Electronics vẫn cao hơn giá hiện tại ngay cả trong kịch bản nguồn cung bình thường hóa (283.000 KRW).</strong> Trong khi đó, <strong>SK Hynix đã thấp hơn giá hiện tại ngay từ kịch bản thứ hai (1.581.000 KRW).</strong> Điều này có nghĩa lợi nhuận kỳ vọng hiện tại của SK Hynix phụ thuộc lớn nhất vào việc nhu cầu vượt cung tiếp diễn.

---

## 8. Sự khác biệt mà FCF tạo ra

Dù lợi nhuận năm 2029 chững lại, dòng tiền tạo ra trong 3 năm trước đó không biến mất. Quy mô của lớp đệm này khác nhau theo từng cổ phiếu.

| Cổ phiếu | FCF 2026F | FCF 2027F | FCF 2028F | Tỷ trọng FCF 3 năm trong giá trị gia quyền xác suất |
|---|---:|---:|---:|---:|
| Samsung Electronics | 158,2 nghìn tỷ KRW | 385,0 nghìn tỷ KRW | 412,7 nghìn tỷ KRW | <strong>26%</strong> |
| SK Hynix | 74,7 nghìn tỷ KRW | 177,4 nghìn tỷ KRW | 172,0 nghìn tỷ KRW | 17% |
| Micron | 50,6 tỷ USD | 124,3 tỷ USD | 145,9 tỷ USD | 18% |

\[Thực tế: báo cáo Samsung Securities (Samsung Electronics), tổng hợp báo cáo Korea Investment & Securities (SK Hynix), ước tính FactSet (Micron)\]

<strong>26% giá trị gia quyền xác suất của Samsung Electronics đến từ FCF giai đoạn 2026-2028.</strong> Nói cách khác, ngay cả khi kịch bản sau năm 2029 xấu đi, tỷ trọng dòng tiền đã chắc chắn có được vẫn là lớn nhất. SK Hynix thấp nhất với 17%, nghĩa là phần lớn giá trị phụ thuộc vào giá trị cuối kỳ sau năm 2029.

---

## 9. Thứ tự ưu tiên cuối cùng

<strong>Hạng 1, Samsung Electronics</strong>: Biên an toàn lớn nhất. Giá hiện tại gần với giá trị theo kịch bản bear khắc nghiệt nhất. Tiền mặt ròng và đa dạng hóa mảng kinh doanh đệm cho phần rủi ro giảm giá của giá trị cuối kỳ, và tỷ trọng FCF 3 năm 26% là lớp đệm bổ sung.

<strong>Hạng 2, Micron</strong>: Hấp dẫn theo giá hợp lý trung tâm nhưng nhạy cảm với nguồn cung mới năm 2028. Cũng cần nhìn vào việc giá hợp lý của Morningstar, một mốc neo bear bên ngoài, ở mức 850 USD, tương tự giá hiện tại. \[Thực tế: Morningstar\]

<strong>Hạng 3, SK Hynix</strong>: Động lực kinh doanh mạnh nhất nhưng biên an toàn về giá mỏng nhất. Đánh giá mới cần xác nhận giá và hiệu suất HBM4E cùng LTA 2028.

Do đó, ở mức giá hiện tại, <strong>mức độ hấp dẫn đã điều chỉnh rủi ro xếp theo thứ tự Samsung Electronics, Micron, SK Hynix</strong>. Phát hiện cốt lõi của phép tính này là thứ tự chất lượng kinh doanh (SK Hynix mạnh nhất nhờ độ phơi nhiễm thuần túy với HBM) lại ngược với thứ tự hấp dẫn về giá. \[Suy luận: đánh giá tổng hợp\]

---

## 10. Tổng hợp cách đánh giá theo từng cổ phiếu

- <strong>Samsung Electronics</strong>: Cộng riêng FCFE giai đoạn 2026-2028, áp dụng 8-10 lần cho EPS chuẩn hóa 2029 rồi chiết khấu. Tiền mặt ròng và đa dạng hóa mảng kinh doanh đệm cho phần rủi ro giảm giá của giá trị cuối kỳ.
- <strong>SK Hynix</strong>: Cộng FCFE giai đoạn 2026-2028 nhưng phản ánh cả mở rộng công suất lẫn pha loãng, áp dụng 7-9 lần cho EPS chuẩn hóa 2029. Chỉ cho phép mức trên khi cao nguyên HBM được xác nhận.

Cách chỉ định giá đồng thuận 2028 bằng 4 lần cũng không hoàn chỉnh, và cách áp máy móc 9-12 lần cũng vậy. Cách đúng là <strong>cộng FCFE giai đoạn 2026-2028 với giá trị cuối kỳ chuẩn hóa 2029 rồi tổng hợp theo từng kịch bản</strong>.

---

## Kết luận

Tóm tắt câu trả lời cho từng câu hỏi theo từng dòng như sau.

Bán dẫn có mang tính chu kỳ không. Bộ nhớ thì có. HBM không xóa bỏ chu kỳ mà chỉ kéo dài nó, và điều này được chính SK Hynix nói trong F-1 và Micron nói trong 10-Q.

Hệ số hợp lý là bao nhiêu. Trước tiên phải xác định gắn vào EPS nào. Ở đỉnh chu kỳ là 5-7 lần, ở mức chuẩn hóa là 7-10 lần.

Tranh luận hiện tại đang lay động điều gì. Bề ngoài là hệ số, nhưng điều mà hệ số đó thể hiện chính là EPS sau năm 2028. Con số của giới phân tích cho đến nay mới chỉ dịch chuyển khoảng 1,5%, còn giá cổ phiếu đã đi trước.

Lấy mốc 2028 hay 2029. Không phải cả hai. Cộng FCFE giai đoạn 2026-2028 với giá trị cuối kỳ chuẩn hóa năm 2029.

Năm 2029 có phải tương lai xa không. 1 đồng của 3 năm sau hiện có giá trị 0,73 đồng. Dù bán sau 1 năm, người mua vào thời điểm đó vẫn nhìn vào năm 2029.

Dòng tiền giai đoạn 2026-2028 có được phản ánh không. Có, nhưng không phải nguyên vẹn như EPS. Phải trừ đi phần chi ra để mở rộng công suất, và thiết bị đó phải sinh lời vượt chi phí vốn thì mới trở thành giá trị.

Vậy giá bao nhiêu. Samsung Electronics 385.000 KRW, SK Hynix 1.950.000 KRW, Micron 1.140 USD. Cổ phiếu có động lực kinh doanh mạnh nhất và cổ phiếu có biên an toàn giá lớn nhất là hai cổ phiếu khác nhau.

---

_Bài viết này là tài liệu phân tích do tác giả tự tính toán dựa trên giá KIS KRX (17/7/2026), đồng thuận WiseReport (16/7/2026), hồ sơ SEC (F-1 của SK Hynix, 10-Q của Micron), ước tính FCF của các công ty chứng khoán, và phương pháp luận định giá công khai của McKinsey, NYU Stern. Giá hợp lý gia quyền xác suất, xác suất kịch bản, PER cuối kỳ và tỷ lệ chiết khấu đều là ước tính dựa trên giả định tại thời điểm viết bài, không phải hướng dẫn của công ty hay đồng thuận thị trường. Các thay đổi trong ước tính của giới phân tích sau đợt giảm mạnh ngày 17/7 chưa được phản ánh. EPS lũy kế là tổng lợi nhuận kế toán, không phải ước tính FCFE. Các cổ phiếu được đề cập chỉ là ví dụ minh họa phương pháp luận định giá, không phải khuyến nghị mua bán một cổ phiếu cụ thể nào. Quyết định đầu tư và trách nhiệm thuộc về nhà đầu tư._

---

### Bài viết liên quan

- [Đâu là điểm tranh cãi thực sự giữa phe tăng giá và phe giảm giá bán dẫn: bốn chiếc đồng hồ thực và một chiếc đồng hồ giá cổ phiếu](/vi/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/)
- [Định giá lợi nhuận 2028E của Samsung Electronics và SK Hynix: con số trông có vẻ rẻ và kiểm chứng chu kỳ](/vi/post/samsung-hynix-2028e-profit-valuation-cycle-scenarios-2026-07-09/)
- [Samsung Electronics và SK Hynix có thực sự bị bán quá đà theo đồng thuận năm 2027 hay không](/vi/post/samsung-hynix-worst-case-eps-priced-in-consensus-dispersion-2026-07-10/)
- [SK Hynix hạ lợi nhuận quý 2, vì sao giá mục tiêu vẫn được giữ nguyên](/vi/post/sk-hynix-2q-earnings-cut-mirae-kis-lta-target-price-2026-07-14/)
- [Lý do IBM trượt lợi nhuận lại là bằng chứng cho sức mạnh của bộ nhớ](/vi/post/ibm-ericsson-q2-memory-cost-evidence-semiconductor-sentiment-2026-07-14/)
