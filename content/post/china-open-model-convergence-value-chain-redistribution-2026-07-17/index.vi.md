---
title: "Sự hội tụ của các mô hình mở Trung Quốc thực sự thay đổi điều gì: tái phân bổ chuỗi giá trị, không phải sụp đổ nhu cầu"
slug: "china-open-model-convergence-value-chain-redistribution-2026-07-17"
date: 2026-07-17T22:00:00+09:00
description: "Các mô hình mở Trung Quốc đang hội tụ về hiệu năng tiên phong của Mỹ trong khi được phục vụ trên hạ tầng suy luận nội địa Trung Quốc. Đây là tái phân bổ chuỗi giá trị chứ không phải sụp đổ nhu cầu AI. Giá trị độc quyền của API mô hình và GPU tiên tiến giảm xuống, trong khi suy luận rẻ hơn làm tăng lượng token và có thể nâng giá trị của bộ nhớ, lưu trữ, mạng, điện năng và phân phối đám mây."
categories: ["Exclusive Analysis", "AI Infrastructure", "Market-Outlook"]
tags: ["Mô hình mở Trung Quốc", "DeepSeek", "Kimi K3", "Qwen", "CXMT", "HBM", "Samsung Electronics", "SK Hynix", "Micron", "NVIDIA", "Chính sách AI"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Bối cảnh
> Bài viết này là phần tiếp theo của [Kimi K3 Tái Định Hình Đường Cong Giá AI](/vi/post/kimi-k3-linear-api-pricing-semiconductor-big-tech-impact-2026-07-17/). Nếu bài trước đã kiểm chứng giá cả và cấu trúc của <strong>một mô hình</strong>, thì bài này mở rộng góc nhìn sang việc <strong>toàn bộ hệ sinh thái mô hình mở Trung Quốc</strong> đang tái phân bổ chuỗi giá trị bán dẫn và Big Tech như thế nào, cũng như chính sách Mỹ và xung đột Mỹ Trung đang thay đổi cách diễn giải đó ra sao. Nên đọc cùng với [Tranh luận thực sự trong ngành bán dẫn](/vi/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/), [Bán dẫn có mang tính chu kỳ không và giá hợp lý là bao nhiêu?](/vi/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/), và [IPO của CXMT và rủi ro giá bộ nhớ](/vi/post/cxmt-ipo-memory-price-risk-hbm-client-dram-2026-06-21/). Các hub liên quan là [Hub AI HBM](/vi/page/korea-semiconductor-hbm-kospi-hub/) và [Hub Exclusive Analysis](/vi/page/exclusive-analysis-hub/).

## TL;DR

* Sự hội tụ về hiệu năng của các mô hình mở Trung Quốc gần với <strong>tái phân bổ chuỗi giá trị hơn là sụp đổ nhu cầu AI</strong>. Giá trị độc quyền của API mô hình và GPU tiên tiến nhất giảm xuống, trong khi suy luận rẻ hơn làm tăng mức sử dụng, có thể nâng giá trị của bộ nhớ, lưu trữ, mạng, điện năng và phân phối đám mây.
* Ưu tiên tương đối chia theo hướng sau. Trong bộ nhớ Hàn Quốc là <strong>Samsung Electronics > SK Hynix</strong>; trong bán dẫn Mỹ là <strong>Micron, SanDisk > NVIDIA</strong>; trong Big Tech là <strong>Meta, Amazon > Google, Microsoft > các hãng mô hình thuần túy</strong>. \[Suy luận: phán đoán tương đối\]
* Mô hình mở Trung Quốc đã chứng minh được <strong>chi phí tính toán và bộ nhớ trên mỗi đơn vị trí tuệ giảm xuống</strong>. Nhưng chưa chứng minh được <strong>tổng chi tiêu silicon giảm</strong>. TSMC thậm chí đã nâng CAPEX năm 2026 từ 52-56 tỷ USD lên 60-64 tỷ USD.
* Trong HBM, CXMT cách 3 hãng dẫn đầu <strong>1,5-2 thế hệ</strong> về sản phẩm và 2-3 năm về thương mại hóa. Vì vậy mối đe dọa năm 2028 không phải là cú sốc nguồn cung ở hiện tại, mà là <strong>một quyền chọn có điều kiện</strong>.
* <strong>Sự lan tỏa công nghệ</strong> của mô hình Trung Quốc và <strong>sự lan tỏa doanh thu</strong> của các hãng API Trung Quốc là hai chuyện khác nhau. Con đường thực tế nhất là tái host mô hình Trung Quốc lên AWS, Azure hoặc VPC doanh nghiệp rồi bán qua hệ thống bảo mật và hợp đồng của phương Tây. \[Phạm vi phân tích\]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Luận điểm chính</div>
  <div class="thesis-callout__body">
    Mô hình Trung Quốc có thể làm lung lay giá của mô hình Mỹ, nhưng không lập tức phá vỡ nhu cầu đối với AWS, Azure, chip Mỹ hay bộ nhớ Hàn Quốc. Thiệt hại trực tiếp rơi vào biên lợi nhuận của API mô hình đóng. Thứ tồn tại lâu nhất là hạ tầng dựa trên mức sử dụng: lớp phân phối và bảo mật đám mây, cùng với bộ nhớ, mạng và điện năng.
  </div>
</div>

---

## 1. Xác nhận sự thật trước

Hướng đi của hệ sinh thái là có thật, nhưng <strong>không phải phần cứng huấn luyện của mọi mô hình mới đều đã được công bố</strong>. Sự phân biệt này quan trọng.

DeepSeek-V3 được huấn luyện bằng <strong>2.048 GPU NVIDIA H800</strong> và 2,788 triệu giờ GPU. \[Thực tế: báo cáo kỹ thuật DeepSeek V3\] H800 là dòng bị hạn chế xuất khẩu, nhưng không phải GPU tiêu dùng giá rẻ. Ngược lại, Kimi K3 đã công bố 2,8 nghìn tỷ tham số, cửa sổ ngữ cảnh 1 triệu token và hiệu suất mở rộng cao hơn K2 tới 2,5 lần, nhưng <strong>báo cáo kỹ thuật đầy đủ và phần cứng huấn luyện dự kiến công bố vào ngày 27 tháng 7</strong>. \[Thực tế: thông báo chính thức của Kimi\]

Vì vậy nhận định "Kimi K3 cũng được huấn luyện bằng GPU NVIDIA giá rẻ" hiện chưa thể khẳng định. \[Chưa xác minh\]

### Cải thiện hiệu suất là có thật

DeepSeek V4-Pro chỉ <strong>kích hoạt 49 tỷ</strong> trong tổng số 1,6 nghìn tỷ tham số. Ở ngưỡng 1 triệu token, lượng FLOPs trên mỗi token so với V3.2 chỉ còn <strong>27%</strong>, KV cache chỉ còn <strong>10%</strong>. \[Thực tế: model card DeepSeek V4\] Đây là bằng chứng trực tiếp cho thấy mức sử dụng GPU và HBM trên mỗi token có thể giảm mạnh trong khi hiệu năng vẫn được giữ nguyên.

### Nhưng chiều ngược lại cũng là sự thật

Huawei CloudMatrix384 ghép 384 chip Ascend 910C để phục vụ DeepSeek-R1. Theo tổng hợp của JPMAM, CloudMatrix dùng 49TB HBM và 599kW điện, trong khi hệ thống so sánh là GB300 NVL72 chỉ dùng lần lượt 21TB và 145kW. \[Thực tế: bài báo CloudMatrix, tài liệu so sánh của JPMAM\]

Đây không phải là phép so sánh hiệu năng hoàn toàn tương đương, nhưng hướng đi rất rõ ràng: Trung Quốc đang bù đắp cho con chip đơn lẻ yếu hơn bằng <strong>nhiều chip hơn, nhiều bộ nhớ hơn và nhiều điện năng hơn</strong>. Một con chip riêng lẻ giá rẻ hơn không nhất thiết đồng nghĩa với việc dùng ít silicon, mạng và điện năng hơn nói chung. \[Suy luận: diễn giải cấu trúc\]

---

## 2. Phương trình cốt lõi: cần nhìn vào đâu

Câu trả lời cho cuộc tranh luận này không nằm ở điểm benchmark, mà nằm ở hai phương trình.

```text
Tổng nhu cầu tính toán = Tổng số token × Lượng tính toán trên mỗi token

Tổng nhu cầu bộ nhớ = Tổng số token × Lượng bộ nhớ sử dụng trên mỗi token
                     + Dung lượng lưu trữ mô hình, KV, dữ liệu tìm kiếm
```

Nếu mô hình mở hạ giá token 70% và tăng mức sử dụng lên 5 lần thì dù hiệu suất được cải thiện, <strong>tổng nhu cầu vẫn tăng</strong>. Ngược lại, nếu mức sử dụng chỉ tăng gấp đôi trong khi HBM trên mỗi token giảm 70%, thì <strong>nhu cầu HBM sẽ giảm</strong>.

Vì vậy chỉ số cần theo dõi từ nay về sau được rút gọn thành một câu hỏi duy nhất. <strong>Tốc độ tăng token vượt tốc độ giảm bộ nhớ trên mỗi token bao nhiêu.</strong>

### Phán định tính đến hiện tại

Tổng chi tiêu được quyết định bởi phương trình sau.

```text
Tổng chi tiêu silicon = Số lần huấn luyện × Chi phí mỗi lần
                       + Số token suy luận × Chi phí mỗi token
```

TSMC đã nâng CAPEX năm 2026 từ 52-56 tỷ USD lên <strong>60-64 tỷ USD</strong> trong cuộc gọi 2Q26. Microsoft cũng nâng thông lượng suy luận lên 40%, nhưng lượng token sử dụng của khách hàng lớn vẫn <strong>tăng 30%</strong> so với quý trước (QoQ), đồng thời duy trì CAPEX năm 2026 khoảng 190 tỷ USD. \[Thực tế: cuộc gọi 2Q26 của TSMC, cuộc gọi FY26 Q3 của Microsoft\]

<strong>Tính đến hiện tại, mức tăng sử dụng đang thắng cải thiện hiệu suất.</strong> \[Suy luận: tổng hợp dữ liệu\]

---

## 3. Tác động đến bán dẫn: chia theo từng cổ phiếu

| Cổ phiếu / Nhóm | Tác động đến giá cổ phiếu | Diễn giải chính |
|---|---|---|
| Samsung Electronics | Tích cực | Hưởng lợi rộng nhất vì không chỉ HBM mà cả DRAM server, NAND, eSSD và bộ nhớ phổ thông đều được hưởng lợi |
| SK Hynix | Từ hỗn hợp đến tích cực | Token tăng là tin tốt, nhưng nén MoE và KV làm giảm HBM trên mỗi token, gây áp lực lên hệ số nhân khan hiếm |
| Micron | Tích cực | Có độ phơi nhiễm tổng hợp DRAM, HBM, NAND trong chuỗi cung ứng Mỹ; hưởng lợi broad-memory tương tự Samsung |
| SanDisk | Tích cực | Triển khai cục bộ, trọng số mô hình, RAG và cache tăng lên đều chuyển hóa thành nhu cầu eSSD và NAND |
| NVIDIA | Tiêu cực ngắn hạn, hỗn hợp dài hạn | Thị phần Trung Quốc và giá trị độc quyền của GPU cao cấp nhất giảm; tổng lượng token tăng và lô hàng H200 bù đắp phần sản lượng |
| AMD | Tích cực tương đối | Mô hình mở giúp việc di chuyển giữa các loại phần cứng khác nhau dễ dàng hơn; ROCm và thị phần serving thực tế là yếu tố quyết định |
| Broadcom / Marvell / Arista | Tích cực trung hạn | Nhu cầu custom ASIC, Ethernet, quang học và SerDes ở phương Tây mở rộng |
| TSMC | Từ trung lập đến tích cực | Nhu cầu chip huấn luyện từ NVIDIA, AMD, ASIC vẫn duy trì, nhưng suy luận tại Trung Quốc dịch chuyển sang Ascend và SMIC |

### Vì sao Samsung có ưu thế tương đối hơn Hynix

Cùng là 3 hãng bộ nhớ, nhưng <strong>hướng đi của Samsung Electronics và SK Hynix lại khác nhau</strong>. Suy luận giá rẻ và sự lan rộng của mô hình mở không chỉ làm tăng HBM mà còn làm tăng tổng lượng DRAM server, NAND và bộ nhớ phổ thông. Samsung Electronics, với độ phơi nhiễm rộng hơn, sẽ nhận được nhiều hơn từ sự lan rộng này.

Ngược lại, MoE và nén KV làm giảm <strong>HBM trên mỗi token</strong>. Hynix, với độ phơi nhiễm HBM tập trung, vừa nhận lợi ích từ token tăng vừa chịu áp lực từ HBM trên mỗi token giảm cùng một lúc. Đây là cấu trúc mà <strong>hệ số nhân khan hiếm</strong>, chứ không phải nhu cầu tuyệt đối, chịu áp lực trước tiên. \[Suy luận: phân tích cấu trúc phơi nhiễm\]

Tuy nhiên Samsung Electronics cũng có rủi ro ở chiều ngược lại: đây là hãng chịu phơi nhiễm đầu tiên trước việc CXMT tăng sản lượng DRAM phổ thông.

### NVIDIA và H200

Gần đây Mỹ đã bắt đầu xuất khẩu một lượng H200 hạn chế sang Trung Quốc, nhưng khối lượng vẫn còn nhỏ. Điều này tích cực cho doanh thu ngắn hạn của NVIDIA, nhưng chưa đủ để đảo ngược xu hướng chuyển dịch sang hạ tầng nội địa lấy Huawei làm trung tâm. \[Thực tế: báo Reuters tháng 7/2026\] \[Suy luận: đánh giá tác động\]

---

## 4. Tác động đến Big Tech

| Công ty | Đánh giá | Lý do |
|---|---|---|
| Meta | Tích cực nhất | Chiến lược hệ sinh thái mở được kiểm chứng, thu hồi giá trị AI qua quảng cáo và đề xuất nội dung nhiều hơn là qua API |
| Amazon | Tích cực | Dù mô hình nào thắng, AWS vẫn bán được suy luận, lưu trữ và mạng |
| Google | Từ hỗn hợp đến tích cực | TPU và cloud được hưởng lợi, nhưng phần bù giá của API Gemini chịu áp lực |
| Microsoft | Hỗn hợp | Mức sử dụng Azure tăng, nhưng chi phí thuê mô hình OpenAI và tỷ lệ thu hồi CAPEX bị áp lực |
| Apple | Tích cực | Mô hình mở, kích thước nhỏ và giá rẻ giúp hạ chi phí on-device và Private Cloud |
| OpenAI, Anthropic | Tiêu cực | Khoảng cách hiệu năng và phần bù giá API bị thu hẹp, gây áp lực lên định giá cao và khả năng gọi vốn |

<strong>Khác với hiểu lầm phổ biến, Meta không phải là bên chịu thiệt hại lớn nhất.</strong> Meta kiếm tiền từ quảng cáo và đề xuất nội dung nhiều hơn là bán mô hình, đồng thời tận dụng mô hình mở để cắt giảm chi phí, nên có khả năng hưởng lợi tương đối. Gánh nặng thay vào đó nằm ở phía CAPEX và khấu hao. \[Suy luận: phân tích mô hình kinh doanh\]

### Bài học từ cú sốc DeepSeek năm 2025

Trong cú sốc DeepSeek năm 2025, NVIDIA đã mất <strong>17%, khoảng 593 tỷ USD</strong> vốn hóa thị trường chỉ trong một ngày. Phản ứng đầu tiên là bán tháo trên diện rộng toàn bộ hạ tầng GPU, điện năng và trung tâm dữ liệu, nhưng sau đó đã phục hồi một phần. \[Thực tế: tin tức thị trường năm 2025\]

Lần này nhiều khả năng <strong>giá cổ phiếu ngắn hạn sẽ phản ứng với nỗi sợ hiệu suất, còn kết quả kinh doanh trung hạn sẽ phản ứng với mức tăng sử dụng</strong>. \[Suy luận: mẫu hình quá khứ\]

---

## 5. Phán định các luận điểm về mô hình mở Trung Quốc

Lần lượt phán định các luận điểm đến từ cả phe tăng giá lẫn phe giảm giá như sau.

| Luận điểm | Phán định |
|---|---|
| GPU cao cấp nhất là điều kiện bắt buộc để đạt hiệu năng tiên phong | Đã suy yếu nhưng chưa bị bác bỏ hoàn toàn |
| Trí tuệ AI là tài nguyên khan hiếm | Phần lớn đã sụp đổ ở cấp độ giá mô hình thô và giá token |
| Quy mô vốn là hào bảo vệ | Hào bảo vệ tiền huấn luyện đã suy yếu, dịch chuyển sang triển khai, dữ liệu, điện năng và phân phối |
| Chi phí biên của mã nguồn mở bằng 0 | Chỉ giá trọng số mô hình tiệm cận 0, chi phí suy luận vẫn tiếp tục phát sinh |
| Huấn luyện 1 tỷ USD đã vượt qua khoản đầu tư 100 tỷ USD | Luận điểm không chính xác vì so sánh hai phạm vi chi phí khác nhau |

Mục cuối cùng là luận điểm bị lạm dụng sai nhiều nhất. Chi phí huấn luyện và tổng đầu tư hạ tầng không phải là hai phạm trù có thể so sánh trực tiếp với nhau.

---

## 6. HBM của CXMT hiện đã tiến đến đâu

Đây là phần bị thổi phồng thường xuyên nhất khi bàn về mối đe dọa Trung Quốc. Chia nhỏ theo từng mốc kiểm định thì thực chất sẽ lộ rõ.

| Mốc kiểm định | Phán định hiện tại | Căn cứ đánh giá |
|---|---|---|
| Công nghệ chế tạo tế bào DRAM | Đã thương mại hóa, cải thiện nhanh | Đang bán DDR5, LPDDR5X; Apple cũng đang thử nghiệm DRAM cho các sản phẩm dành cho thị trường Trung Quốc |
| Xếp chồng TSV | HBM2 sản lượng nhỏ, HBM3 giai đoạn đầu | Có tin sản xuất HBM2 nhưng chưa công bố sản lượng và yield |
| Đóng gói và base die | Đang xây dựng | Hệ sinh thái nội địa Trung Quốc đang hình thành, nhưng thiếu dữ liệu về yield sản xuất hàng loạt, nhiệt và độ tin cậy |
| Chứng nhận khách hàng | Chưa xác nhận với HBM | Hợp đồng với Tencent và thử nghiệm của Apple chỉ là bằng chứng năng lực DRAM thông thường, không phải HBM |
| Khoảng cách với nhóm dẫn đầu | 1,5-2 thế hệ | 3 hãng dẫn đầu đang ramp HBM4, còn CXMT thậm chí chưa qua kiểm chứng sản xuất hàng loạt HBM3 |

Tính đến ngày 17 tháng 7 năm 2026, danh mục sản phẩm công bố chính thức của CXMT chỉ gồm DDR5, LPDDR5/5X, DDR4, LPDDR4X, và <strong>không có HBM</strong>. TrendForce cũng xếp HBM3 của CXMT vào giai đoạn kiểm chứng ban đầu, đánh giá rằng rào cản công nghệ và điều kiện bắt buộc dùng thiết bị nội địa đang làm chậm quá trình sản xuất hàng loạt. \[Thực tế: tài liệu chính thức của CXMT, TrendForce\]

Ước tính công suất cũng không thống nhất. Con số đình trệ quanh mức 240.000 tấm/tháng và dự báo cuối năm đạt 350.000 tấm mâu thuẫn với nhau; do 350.000 tấm là mô hình ước tính tư nhân chứ không phải guidance của công ty, nên khó dùng như một con số đã được xác định. \[Chưa xác minh\]

### Cần sửa lại giả thuyết về DRAM legacy như sau

- <strong>Giai đoạn 2026-2027</strong>: khoản đầu tư HBM của CXMT sẽ <strong>làm chậm lại</strong> việc nới lỏng nguồn cung DRAM legacy sản xuất tại Trung Quốc.
- <strong>Năm 2028</strong>: nếu HBM3/3E đạt được chứng nhận từ khách hàng bộ tăng tốc Trung Quốc và có sản lượng đáng kể, có thể bắt đầu thay thế thị trường HBM thế hệ cũ trong nội địa Trung Quốc trước tiên.
- <strong>Từ năm 2029 trở đi</strong>: phải theo kịp cả HBM4, base die và yield đóng gói thì mới trực tiếp gây áp lực lên thị trường dẫn đầu toàn cầu và biên lợi nhuận của Hynix.

Nói cách khác, thay vì cho rằng "vì CXMT nên DRAM legacy sẽ thiếu hụt ngay lập tức", nhận định <strong>"CXMT không nới lỏng nguồn cung DRAM legacy được nhiều như kỳ vọng"</strong> hợp lý hơn. \[Suy luận: phán đoán theo từng giai đoạn\]

---

## 7. Chính sách Mỹ thay đổi cách diễn giải này như thế nào

Mỹ đang xem AI là <strong>hạ tầng cốt lõi của khối đồng minh</strong> hơn là một công nghệ thương mại thuần túy. Đây là lý do vì sao chỉ phân tích công nghệ thuần túy không thể đưa ra câu trả lời đầy đủ.

AI Action Plan và Sắc lệnh hành pháp 14320 của Mỹ nêu rõ mục tiêu xuất khẩu <strong>bộ công nghệ AI sản xuất tại Mỹ (AI stack)</strong>, bao gồm phần cứng, đám mây, mạng, mô hình và ứng dụng, cho các nước đồng minh, đồng thời giảm sự phụ thuộc công nghệ vào các nước đối địch. Dù mô hình Trung Quốc vượt trội về hiệu năng và giá cả, bộ công nghệ Mỹ vẫn giữ lợi thế về mặt chính sách trong mua sắm chính phủ và các ngành công nghiệp cốt lõi của các nước đồng minh. \[Thực tế: AI Action Plan của Nhà Trắng, EO 14320\]

### Nhưng đây không phải là sự tách rời hoàn toàn

Vào tháng 1 năm 2026, BIS của Mỹ đã chuyển sang xét duyệt từng trường hợp đối với việc xuất khẩu H200 và MI325X sang Trung Quốc, dựa trên danh sách khách hàng được phê duyệt và các điều kiện bảo mật. Đây là một sự thỏa hiệp nhằm vừa giữ Trung Quốc ở lại một phần trong hệ sinh thái chip Mỹ, vừa duy trì quyền kiểm soát. \[Thực tế: BIS 13/01/2026\]

Việc doanh nghiệp tư nhân Mỹ sử dụng mô hình Trung Quốc cũng chưa bị cấm toàn diện. Dự luật `No DeepSeek on Government Devices Act` vẫn chỉ đang ở giai đoạn đề xuất. Tuy nhiên chính phủ Úc đã chỉ thị loại bỏ DeepSeek khỏi hệ thống chính phủ, còn cơ quan bảo vệ dữ liệu cá nhân của Italy đã hạn chế việc xử lý dữ liệu người dùng. \[Thực tế: các biện pháp chính thức của từng quốc gia\]

<strong>Nhiều khả năng lệnh cấm trên thực tế từ bộ phận mua sắm và bảo mật sẽ vận hành trước cả luật pháp chính thức.</strong> \[Suy luận: thứ tự vận hành chính sách\]

---

## 8. Doanh nghiệp phương Tây có thể dùng API mô hình Trung Quốc không

Khả năng lan tỏa hoàn toàn khác nhau tùy theo từng con đường tiếp cận. Bảng dưới đây chính là câu trả lời cho câu hỏi này.

| Phương thức áp dụng | Khả năng lan tỏa | Nhận định |
|---|---|---|
| Gọi trực tiếp API được host tại Trung Quốc đại lục | Thấp | Rủi ro dữ liệu, thẩm quyền pháp lý, mua sắm |
| API của Qwen tại Mỹ, EU, Nhật Bản, Singapore | Trung bình | Có thể nội địa hóa dữ liệu nhưng rủi ro từ nhà cung cấp Trung Quốc vẫn còn |
| Mô hình Trung Quốc được AWS, Azure tái host | Từ trung bình khá đến cao | Chủ thể kiểm soát hợp đồng, bảo mật, dữ liệu là đám mây phương Tây |
| Open-weight trên VPC doanh nghiệp hoặc on-premise | Cao | Không cần gửi dữ liệu tới máy chủ Trung Quốc |
| Chính phủ, quốc phòng, hạ tầng cốt lõi | Rất thấp | Có thể hạn chế mua sắm cả theo phả hệ (lineage) của mô hình |

Con đường thực tế nhất là như sau.

```text
Phát triển mô hình Trung Quốc
→ Tái host lên AWS, Azure hoặc VPC doanh nghiệp
→ Bán qua hệ thống bảo mật, hợp đồng, kiểm toán của phương Tây
```

Nói cách khác, <strong>sự lan tỏa công nghệ của mô hình Trung Quốc và sự lan tỏa doanh thu của các hãng API Trung Quốc là hai chuyện tách biệt</strong>. \[Suy luận: phân tích con đường\]

### Giới hạn của API trực tiếp

Chính sách bảo mật của DeepSeek nêu rõ hãng <strong>thu thập, xử lý và lưu trữ trực tiếp tại Trung Quốc</strong> dữ liệu cá nhân bao gồm cả dữ liệu đầu vào, và có thể sử dụng dữ liệu đó để cải thiện dịch vụ và mô hình. \[Thực tế: DeepSeek Privacy Policy\] Đây là điều kiện chí mạng đối với các doanh nghiệp xử lý mã nguồn, thông tin khách hàng, dữ liệu y tế hoặc tài chính, hay công nghệ bị kiểm soát xuất khẩu.

Qwen có phần khác biệt. Alibaba Cloud Model Studio cung cấp các khu vực (region) tại Mỹ, Đức, Nhật Bản, Singapore, có thể giới hạn dữ liệu và suy luận trong một khu vực địa lý cụ thể, đồng thời khẳng định không dùng dữ liệu khách hàng để huấn luyện mô hình. \[Thực tế: chính sách khu vực và bảo mật của Alibaba Cloud\] Vì vậy việc áp dụng API trực tiếp có thể tăng lên ở các ngành không bị quản lý chặt và tại Đông Nam Á, Trung Đông, Mỹ Latinh.

Tuy nhiên việc nội địa hóa dữ liệu và chứng nhận SOC 2 <strong>không loại bỏ được rủi ro gián đoạn dịch vụ, chế tài hoặc rủi ro mua sắm phát sinh từ xung đột Mỹ Trung</strong>. \[Suy luận: rủi ro tồn dư\]

---

## 9. Điều chỉnh luận điểm: điều gì thay đổi, điều gì còn nguyên

<strong>Thứ nhất, logic sụp đổ của hyperscaler Mỹ đang suy yếu.</strong> AWS và Azure trực tiếp host DeepSeek, đồng thời cung cấp cô lập dữ liệu, SLA và đánh giá bảo mật. Đám mây Mỹ có thể hấp thụ đổi mới về chi phí của mô hình Trung Quốc và biến nó thành doanh thu. \[Thực tế: thông báo chính thức của AWS và Azure\]

<strong>Thứ hai, áp lực giá đến với API mô hình đóng trước tiên.</strong> Đây là gánh nặng cho giá token và biên lợi nhuận của OpenAI, Anthropic, Google, nhưng lượng suy luận và mức sử dụng AWS, Azure vẫn có thể tăng lên. Điều này tương đối có lợi cho chiến lược mô hình mở của Meta.

<strong>Thứ ba, sự tách rời Mỹ Trung hỗ trợ cho tổng đầu tư hạ tầng.</strong> Cả hai phe đều <strong>xây dựng trùng lặp</strong> bộ tăng tốc, bộ nhớ, mạng và lưới điện. Điều này làm giảm khả năng cải thiện hiệu suất sẽ dẫn thẳng tới việc giảm tổng chi tiêu silicon toàn cầu.

<strong>Thứ tư, phần bù giá HBM của SK Hynix có thể được duy trì lâu hơn trong khối đồng minh.</strong> HBM của CXMT nhiều khả năng sẽ thâm nhập vào bộ tăng tốc và trung tâm dữ liệu Trung Quốc trước tiên. Việc các CSP phương Tây áp dụng đòi hỏi thêm chứng nhận về chính sách và chuỗi cung ứng, ngoài chứng nhận kỹ thuật. Dù vậy, kiểm soát xuất khẩu lại đang thúc đẩy Trung Quốc đầu tư tự chủ nhanh hơn, nên đây là rủi ro cho thị phần của Hynix tại Trung Quốc từ năm 2028 trở đi.

<strong>Thứ năm, Samsung Electronics là một hàng rào phòng hộ tương đối.</strong> Suy luận giá rẻ và sự lan rộng của mô hình mở có thể làm tăng tổng lượng DRAM server, NAND và bộ nhớ phổ thông, chứ không chỉ HBM. Ở chiều ngược lại có rủi ro là hãng chịu phơi nhiễm đầu tiên trước việc CXMT tăng sản lượng DRAM phổ thông.

---

## 10. Thứ tự thiệt hại và hưởng lợi

1. <strong>Thiệt hại lớn nhất</strong>: lợi nhuận vượt trội của API mô hình đóng, các hãng cho thuê GPU dùng đòn bẩy cao
2. <strong>Rủi ro trung bình</strong>: các hãng đầu tư trước quy mô lớn và tập trung khách hàng như Oracle
3. <strong>Meta</strong>: không phải bên chịu thiệt hại lớn nhất. Có khả năng hưởng lợi tương đối nhờ tận dụng mô hình mở để cắt giảm chi phí. Gánh nặng nằm ở CAPEX và khấu hao
4. <strong>NVIDIA</strong>: hệ số nhân và cơ cấu sản phẩm chịu áp lực trước cả EPS ngắn hạn. Việc bị thay thế tại thị trường Trung Quốc là một rủi ro, nhưng hào bảo vệ về CUDA, mạng, hiệu suất điện năng và thời gian phát triển vẫn còn nguyên
5. <strong>Bộ nhớ</strong>: kịch bản cơ sở không phải là nhu cầu tuyệt đối HBM giảm, mà là <strong>phần bù khan hiếm của HBM thu hẹp, cộng với mở rộng theo tầng sang DDR/CXL/eSSD</strong>

---

## 11. Cập nhật kịch bản

Việc điều chỉnh tạm thời các xác suất đã dùng trong [Bán dẫn có mang tính chu kỳ không và giá hợp lý là bao nhiêu?](/vi/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/) là hợp lý.

| Kịch bản | Trước đó | Sau điều chỉnh |
|---|---:|---:|
| Nhu cầu vượt cung kéo dài | 30% | 30% |
| Tái tập trung tài sản | 40% | 40% |
| Bình thường hóa cung và hiệu suất | 20% | <strong>25%</strong> |
| Đứt gãy nhu cầu hệ thống | 10% | <strong>5%</strong> |

Hiệu năng của mô hình Trung Quốc <strong>làm giảm khả năng bản thân nhu cầu AI biến mất</strong> (kịch bản đứt gãy giảm từ 10% xuống 5%). Đổi lại, cải thiện hiệu suất và phần cứng sản xuất tại Trung Quốc làm giảm phần bù khan hiếm của NVIDIA và HBM (kịch bản bình thường hóa tăng từ 20% lên 25%).

Kịch bản theo trục thời gian vẫn có thể giữ nguyên: mức sử dụng thắng hiệu suất đến năm 2027 với xác suất 70%, cơ cấu và giá bình thường hóa từ năm 2028 trở đi với xác suất 25%, tổng CAPEX co lại với xác suất 5%. Tuy nhiên <strong>động lực của kịch bản 70% sẽ chuyển từ một hệ sinh thái toàn cầu duy nhất sang đầu tư kép giữa khối Mỹ và khối Trung Quốc.</strong> \[Suy luận: tái điều chỉnh kịch bản\]

---

## 12. Xác nhận điều gì thì sẽ thay đổi phán đoán

- <strong>Báo cáo kỹ thuật Kimi K3 (27 tháng 7)</strong>: nếu phần cứng huấn luyện được công bố, tính đúng sai của mệnh đề "huấn luyện mô hình tiên phong bằng GPU giá rẻ" sẽ được phân định
- <strong>Tốc độ tăng token so với tốc độ giảm bộ nhớ trên mỗi token</strong>: chênh lệch giữa hai giá trị này chính là câu trả lời thực sự cho cuộc tranh luận này
- <strong>Chứng nhận sản xuất hàng loạt HBM3E của CXMT và sản lượng đóng gói thực tế</strong>: nếu được xác nhận, cần hạ đồng thời cả EPS 2028 và hệ số nhân của Hynix
- <strong>Giá HBM và mức tải giảm tốc</strong>: tín hiệu đầu tiên cho thấy phần bù khan hiếm đang thu hẹp
- <strong>Các CSP phương Tây mở rộng tái host mô hình Trung Quốc</strong>: bằng chứng cho thấy giá trị phân phối đám mây đang tăng lên
- <strong>Việc thực thi thực tế các quy định mua sắm và bảo mật của Mỹ</strong>: phạm vi của lệnh cấm trên thực tế, vốn vận hành trước cả luật pháp

Hiện tại <strong>chưa phải giai đoạn để trộn lẫn rủi ro tận cùng (terminal risk) với kết quả kinh doanh của kỳ hiện tại</strong>. Khi chứng nhận sản xuất hàng loạt HBM3E của CXMT được xác nhận, khi đó mới cần điều chỉnh triển vọng của Hynix từ năm 2028 trở đi. \[Suy luận: thứ tự phán đoán\]

---

## Kết luận

Quay lại câu hỏi ban đầu, câu trả lời là như sau.

Việc các mô hình mở Trung Quốc hội tụ về hiệu năng tiên phong của Mỹ là một sự thật, và việc chi phí trên mỗi đơn vị trí tuệ giảm mạnh cũng là một sự thật. Nhưng điều đó không có nghĩa là tổng chi tiêu silicon đang giảm. Việc TSMC nâng CAPEX và token của Microsoft tăng 30% chính là câu trả lời tính đến hiện tại.

Chính sách Mỹ làm thay đổi đáng kể cách diễn giải này. Sự tách rời Mỹ Trung tạo ra <strong>đầu tư trùng lặp</strong> ở cả hai phe, qua đó hỗ trợ tổng nhu cầu hạ tầng, đồng thời trong khối đồng minh, chính sách này bảo vệ vị thế của bộ công nghệ Mỹ và bộ nhớ Hàn Quốc.

Việc doanh nghiệp phương Tây áp dụng API mô hình Trung Quốc cần được nhìn nhận bằng cách <strong>tách biệt mô hình khỏi nhà cung cấp dịch vụ</strong>. Công nghệ lan tỏa dưới dạng open-weight, nhưng chủ thể bán nó nhiều khả năng sẽ là AWS, Azure và VPC doanh nghiệp, chứ không phải bản thân các hãng API Trung Quốc.

Vì vậy kết luận là tái phân bổ. Thứ sụp đổ là lợi nhuận vượt trội của API mô hình đóng. Thứ tồn tại lại là hạ tầng dựa trên mức sử dụng.

---

_Bài viết này tổng hợp phân tích từ các bài báo khoa học công khai (DeepSeek V3/V4, Huawei CloudMatrix384), thông báo chính thức của doanh nghiệp (Kimi, cuộc gọi 2Q26 của TSMC, cuộc gọi FY26 Q3 của Microsoft, CXMT, Alibaba Cloud, DeepSeek Privacy Policy), tài liệu chính phủ Mỹ (AI Action Plan, EO 14320, BIS), các biện pháp quản lý của từng quốc gia, và nghiên cứu thị trường (TrendForce, JPMAM). Phần cứng huấn luyện của Kimi K3 vẫn chưa được xác minh cho tới khi báo cáo kỹ thuật công bố vào ngày 27 tháng 7, còn ước tính công suất của CXMT và xác suất kịch bản là ước tính của tác giả tại thời điểm viết bài, không phải guidance của công ty. Các cổ phiếu được đề cập chỉ là ví dụ minh họa cấu trúc chuỗi giá trị, không phải khuyến nghị mua bán một cổ phiếu cụ thể nào. Quyết định đầu tư và trách nhiệm thuộc về nhà đầu tư._

---

### Bài viết liên quan

- [Kimi K3 Tái Định Hình Đường Cong Giá AI: Từ Kimi Linear đến HBM và Chiến Lược Big Tech](/vi/post/kimi-k3-linear-api-pricing-semiconductor-big-tech-impact-2026-07-17/)
- [Bán dẫn có mang tính chu kỳ không và giá hợp lý là bao nhiêu? Định giá Samsung, SK Hynix và Micron bằng FCFE và lợi nhuận chuẩn hóa](/vi/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/)
- [Tranh luận thực sự trong ngành bán dẫn: bốn chiếc đồng hồ vật lý và một chiếc đồng hồ giá cổ phiếu](/vi/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/)
- [IPO của CXMT và rủi ro giá bộ nhớ: HBM không phải nơi gãy đầu tiên](/vi/post/cxmt-ipo-memory-price-risk-hbm-client-dram-2026-06-21/)
- [Nghiên cứu chuyên sâu cung-cầu HBM 2030: mổ xẻ mô hình cầu 26,7EB đối chiếu với lịch trình mở rộng công suất](/vi/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/)
