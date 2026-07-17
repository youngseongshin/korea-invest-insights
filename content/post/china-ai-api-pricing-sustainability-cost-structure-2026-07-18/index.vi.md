---
title: "Giá API AI Trung Quốc có bền vững không? Kiểm chứng cấu trúc chi phí qua công bố thông tin"
slug: "china-ai-api-pricing-sustainability-cost-structure-2026-07-18"
date: 2026-07-18T11:00:00+09:00
description: "Đầu ra của DeepSeek V4-Pro rẻ hơn GPT-5.6 Sol tới 34 lần. Đây là mức giá bền vững hay là con đường đi tới người thắng lấy tất cả như xe điện? Công bố thông tin tại Hong Kong của Zhipu và MiniMax cho câu trả lời tách bạch: API trả phí cao cấp đã bắt đầu vượt chi phí suy luận biên, nhưng cả hai đều chưa thu hồi được chi phí toàn phần bao gồm chi phí huấn luyện."
categories: ["Exclusive Analysis", "AI Infrastructure", "Tech-Analysis"]
tags: ["AI Trung Quốc", "DeepSeek", "Zhipu", "MiniMax", "Alibaba", "Huawei", "Giá API", "Cấu trúc chi phí", "HBM", "Samsung Electronics", "SK Hynix"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Bối cảnh
> Bài viết này là phần tiếp theo của [Sự hội tụ của các mô hình mở Trung Quốc thực sự thay đổi điều gì](/vi/post/china-open-model-convergence-value-chain-redistribution-2026-07-17/). Nếu bài trước đã bàn về <strong>hàm ý chuỗi giá trị</strong> của sự hội tụ hiệu năng, thì bài này kiểm chứng bằng công bố thông tin tại Hong Kong xem liệu mức giá API rẻ đó có <strong>bền vững về mặt cấu trúc chi phí</strong> hay không. Nên đọc cùng với [Kimi K3 Tái Định Hình Đường Cong Giá AI](/vi/post/kimi-k3-linear-api-pricing-semiconductor-big-tech-impact-2026-07-17/) và [Tranh luận thực sự trong ngành bán dẫn](/vi/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/). Các hub liên quan là [Hub AI HBM](/vi/page/korea-semiconductor-hbm-kospi-hub/) và [Hub Exclusive Analysis](/vi/page/exclusive-analysis-hub/).

## TL;DR

* Giá API AI Trung Quốc hiện nay là <strong>sự pha trộn giữa chi phí đã giảm về mặt cấu trúc và cạnh tranh chiến lược chấp nhận lỗ</strong>. Rất khó để mọi mức giá siêu rẻ này vừa được duy trì lâu dài, vừa quay trở lại ngang bằng mức giá tiên phong của Mỹ.
* Công bố thông tin tại Hong Kong cho câu trả lời tách bạch. Tỷ suất lợi nhuận gộp API của Zhipu cải thiện lên <strong>18,9%</strong> (so với 3,3% năm trước), tức <strong>đã bắt đầu vượt chi phí suy luận biên</strong>. Nhưng tổng lợi nhuận gộp chỉ bằng <strong>9,3%</strong> chi phí R&D, nghĩa là <strong>chưa thu hồi được chi phí toàn phần</strong>.
* Lợi thế chi phí của Trung Quốc là có thật, nhưng không nằm ở chip Huawei hay điện giá rẻ. Thứ tự đóng góp là <strong>cấu trúc mô hình và giảm tham số kích hoạt > xử lý theo lô, cache, lượng tử hóa > tỷ lệ sử dụng GPU đám mây > biên lợi nhuận mục tiêu thấp > điện năng và NPU nội địa</strong>.
* Ngay cả khi ước tính hào phóng hiệu ứng điện năng, nó cũng chỉ chiếm <strong>khoảng 2%</strong> giá compute. Việc Qwen 3.5 Flash có cùng một mức giá tại Bắc Kinh, Frankfurt và Virginia củng cố cho nhận định này.
* Khác với xe điện, mô hình AI có <strong>chi phí chuyển đổi thấp</strong>. Nếu có hiện tượng thắng lấy tất cả, nó sẽ xảy ra ở tầng đám mây và phân phối chứ không phải ở tầng mô hình. Con đường khả dĩ nhất là <strong>thế độc quyền nhóm giá rẻ (60%)</strong>. \[Phạm vi phân tích\]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Luận điểm chính</div>
  <div class="thesis-callout__body">
    Giá API Trung Quốc thấp không phải vì đó đã là mức giá bình thường có thể tự đứng vững, mà vì cải thiện hiệu suất suy luận và nguồn vốn huy động khổng lồ cùng nhau nâng đỡ nó. Điều này gây áp lực lên biên lợi nhuận API của các hãng mô hình phương Tây, nhưng không đồng nghĩa với việc tổng nhu cầu bán dẫn giảm, vì vốn huy động được lại tiếp tục đổ vào huấn luyện và hạ tầng điện toán.
  </div>
</div>

---

## 1. Rẻ đến mức nào

Đây là giá trên mỗi 1 triệu token, tính đến tháng 7 năm 2026. \[Thực tế: bảng giá chính thức của từng hãng\]

| Mô hình | Đầu vào | Đầu ra |
|---|---:|---:|
| DeepSeek V4 Flash | 0,14 USD | 0,28 USD |
| DeepSeek V4 Pro | 0,435 USD | 0,87 USD |
| Gemini 3.5 Flash | 1,50 USD | 9 USD |
| GPT-5.6 Sol | 5 USD | 30 USD |

DeepSeek V4-Pro rẻ hơn GPT-5.6 Sol khoảng <strong>11 lần</strong> ở đầu vào và khoảng <strong>34 lần</strong> ở đầu ra. Dĩ nhiên điều này không có nghĩa là hiệu năng, độ trễ, SLA, bảo mật và mức độ hỗ trợ công cụ hoàn toàn tương đương nhau.

### Ngay trong nội bộ Trung Quốc, chênh lệch giá cũng rất lớn

- Qwen 3.7 Max: đầu vào RMB 12, đầu ra RMB 36, hiện đang giảm giá 50%
- Doubao Seed 2.1 Pro: đầu vào RMB 6, đầu ra RMB 30
- DeepSeek V4-Pro: mạnh tay hơn hẳn cả các đối thủ Trung Quốc

Vì vậy <strong>không nên coi giá của DeepSeek là mức giá bình thường đại diện cho toàn bộ Trung Quốc</strong>. \[Suy luận: diễn giải phân tán giá\]

---

## 2. Phần bền vững: chi phí biên

DeepSeek V4-Pro là cấu trúc MoE chỉ <strong>kích hoạt 49 tỷ tham số</strong> trong tổng số 1,6 nghìn tỷ tham số. Kết hợp tỷ lệ vận hành cao, xử lý theo lô và cache có thể hạ đáng kể chi phí tính toán thực tế trên mỗi token. Giá cache hit cho đầu vào lặp lại chỉ <strong>0,003625 USD</strong> trên mỗi 1 triệu token. \[Thực tế: tài liệu chính thức DeepSeek\]

Vì vậy, với các loại lưu lượng sau, mức giá hiện tại có thể bền vững xét theo chi phí biên.

- Xử lý theo lô
- Cache hit
- Lưu lượng không cam kết độ trễ
- Sử dụng khối lượng lớn có thể duy trì tỷ lệ vận hành cao

---

## 3. Phần khó bền vững: chi phí toàn phần

Chỉ riêng mức giá công khai hiện tại thì khó có thể thu hồi được chi phí huấn luyện mô hình, R&D, các thử nghiệm thất bại, công suất nhàn rỗi, và SLA cho bảo mật, kinh doanh, doanh nghiệp.

Việc bình thường hóa giá cũng đã bắt đầu. \[Thực tế: động thái và tin tức của từng hãng\]

- DeepSeek hạ giá V4 75%, sau đó <strong>tăng gấp đôi giá vào giờ cao điểm</strong>
- Alibaba cũng <strong>tăng giá tối đa 34%</strong> đối với một số dịch vụ AI
- Thông lượng chuyên dụng cho doanh nghiệp và dịch vụ độ trễ thấp áp dụng mức giá cao hơn API công khai

Đây là bằng chứng cho thấy mức giá siêu rẻ không thể duy trì ở mọi khung giờ và mọi nhóm khách hàng.

| Dịch vụ | Mức độ bền vững |
|---|---|
| Lưu lượng cache, theo lô, không ưu tiên | Cao |
| Giờ cao điểm, độ trễ thấp, độ đồng thời cao | Thấp |
| Bảo mật, SLA cho doanh nghiệp | Định hình mức phí riêng, cao hơn |
| Thu hồi chi phí toàn phần của mảng kinh doanh API độc lập | Khó với mức giá hiện tại |

---

## 4. Kiểm chứng bằng công bố thông tin: Zhipu và MiniMax

Từ đây trở đi là phần cốt lõi của bài viết. Thay vì suy đoán, ta có thể kiểm chứng bằng <strong>công bố thông tin của các công ty niêm yết tại Hong Kong</strong>.

| Năm 2025 | Zhipu (02513) | MiniMax (00100) |
|---|---:|---:|
| Doanh thu | RMB 724 triệu | 79,04 triệu USD |
| Tỷ trọng doanh thu API, nền tảng | 26,3% | 32,8% |
| Tỷ suất lợi nhuận gộp API hoặc toàn công ty | API 18,9% | Toàn công ty 25,4% |
| Tỷ suất lợi nhuận gộp năm trước | API 3,3% | Toàn công ty 12,2% |
| R&D / Doanh thu | 439% | 320% |
| Lỗ ròng điều chỉnh / Doanh thu | 439% | 317% |
| Lợi nhuận gộp / R&D | <strong>9,3%</strong> | <strong>7,9%</strong> |

\[Thực tế: kết quả kinh doanh 2025 của Zhipu, báo cáo thường niên 2025 của MiniMax\]

### Zhipu: đã xác nhận thu hồi được chi phí biên

Doanh thu API và nền tảng mở tăng từ RMB 48,48 triệu lên <strong>190,4 triệu, tương đương tăng 293%</strong>, tỷ suất lợi nhuận gộp cũng tăng từ 3,3% lên 18,9%. Công ty giải thích nguyên nhân là hiệu suất suy luận, kinh tế quy mô và tăng giá.

Có một sự thật quan trọng hơn. Tính đến tháng 3 năm 2026, dù đã <strong>tăng giá API 83% so với cuối năm trước, nhu cầu vẫn vượt cung</strong>. Giá chính thức hiện tại của GLM-5 là RMB 4 cho đầu vào, RMB 18/triệu token cho đầu ra. Có vẻ như API cao cấp đã thoát khỏi cấu trúc bán phá giá dưới chi phí suy luận trực tiếp. \[Suy luận: hàm ý của việc tăng giá và nhu cầu vượt cung\]

### MiniMax: khả năng cao nhưng chưa xác định

Công ty không công bố riêng tỷ suất lợi nhuận gộp của mảng API. Tỷ suất lợi nhuận gộp toàn công ty cải thiện từ 12,2% lên <strong>25,4%</strong>, công ty cho biết nguyên nhân là hiệu suất mô hình, hệ thống và tối ưu hóa phân bổ hạ tầng.

Giá M2.5 hiện tại là 0,30 USD cho đầu vào, 1,20 USD/triệu token cho đầu ra, còn bản tốc độ cao là 0,60/2,40 USD. Tuy nhiên vì M2.5 ra mắt năm 2026 trong khi báo cáo lãi lỗ công bố chỉ tính đến năm 2025, nên <strong>tỷ lệ chi phí riêng của mảng API theo mức giá hiện tại vẫn chưa được kiểm chứng</strong>. \[Chưa xác minh\]

### Cả hai công ty đều chưa thu hồi được chi phí toàn phần

Tổng lợi nhuận gộp RMB 297 triệu của Zhipu chỉ bằng <strong>9,3%</strong> chi phí R&D RMB 3,18 tỷ. MiniMax cũng chỉ trang trải được <strong>7,9%</strong> chi phí R&D 253 triệu USD bằng lợi nhuận gộp 20,08 triệu USD, trong khi dòng tiền hoạt động kinh doanh chảy ra tới 280 triệu USD.

Dịch vụ mà MiniMax mua từ Alibaba Group năm 2025 lên tới <strong>75,88 triệu USD, tương đương 96% doanh thu</strong>. Đây là con số gộp cả cloud dùng cho huấn luyện lẫn cloud dùng cho dịch vụ nên không thể coi thẳng là chi phí API, nhưng nó là bằng chứng cho mức độ phụ thuộc cao vào hạ tầng điện toán bên ngoài. Alibaba nắm giữ 17,06% cổ phần của MiniMax.

Điểm quan trọng là công bố thông tin nêu rõ các giao dịch với bên liên quan được thực hiện <strong>theo đúng mức giá và điều kiện công khai áp dụng cho khách hàng thông thường</strong>. Có thể thừa nhận việc đảm bảo công suất và thuận lợi tích hợp nhờ quan hệ chiến lược, nhưng <strong>không có căn cứ để khẳng định có trợ giá ngầm</strong>. \[Suy luận: diễn giải văn bản công bố thông tin\]

Ngay cả sau khi niêm yết, Zhipu đã huy động ròng HK$31,375 tỷ, còn MiniMax huy động ròng tổng cộng HK$15,957 tỷ qua cổ phiếu mới và trái phiếu chuyển đổi. Phần lớn vốn huy động được đổ vào R&D và hạ tầng điện toán. Bản thân việc huy động vốn không phải là bằng chứng cho thua lỗ ở mảng API, nhưng <strong>cuộc đua mô hình tiên phong hiện chưa ở giai đoạn có thể duy trì chỉ bằng dòng tiền nội bộ</strong>. \[Thực tế: công bố thông tin\]

### Phán quyết

1. Tính bền vững chi phí biên của API trả phí cao cấp: Zhipu <strong>đã xác nhận</strong>, MiniMax khả năng cao nhưng chưa xác định
2. Tính bền vững của chi phí toàn phần bao gồm cả chi phí huấn luyện: cả hai công ty đều <strong>chưa đạt được</strong>
3. Khả năng duy trì cuộc chiến giá: <strong>cao</strong>. Vốn huy động từ thị trường vốn có thể giúp duy trì mức giá lỗ trong thời gian dài
4. Cấu trúc thị trường: thay vì thắng lấy tất cả, khả năng cao hơn là <strong>độc quyền nhóm theo từng phân khúc</strong>, như Zhipu ở doanh nghiệp Trung Quốc và on-premise, MiniMax ở thị trường nước ngoài, người tiêu dùng và đa phương thức

---

## 5. Phân rã lợi thế chi phí: đâu mới là lý do thực sự

Lợi thế chi phí phục vụ API của Trung Quốc là có thật. Nhưng cốt lõi không phải là điện giá rẻ hay chip Huawei đơn lẻ, mà là tổ hợp sau.

```text
Tham số kích hoạt nhỏ, lượng tử hóa
+ Tỷ lệ xử lý theo lô cao, tận dụng cache
+ Tỷ lệ sử dụng GPU của các đám mây quy mô lớn như Alibaba
+ Biên lợi nhuận mục tiêu thấp
+ Điện năng giá rẻ ở miền Tây Trung Quốc
```

| Yếu tố | Lợi thế chi phí | Đánh giá |
|---|---:|---|
| Cấu trúc mô hình, lượng tử hóa, caching | Rất lớn | Cốt lõi của năng lực cạnh tranh giá API Trung Quốc |
| Quy mô đám mây, tỷ lệ vận hành | Lớn | Hào bảo vệ chắc chắn nhất của Alibaba |
| Biên lợi nhuận mục tiêu thấp | Lớn | Lý do giá rẻ, nhưng là điểm yếu về khả năng sinh lời dài hạn |
| Huawei Ascend | Trung bình, có điều kiện | Có lợi với khối lượng công việc đã tối ưu hóa, tính đa dụng thấp |
| Điện năng miền Tây Trung Quốc | Trung bình | Hiệu quả với suy luận theo lô, hạn chế với API thời gian thực toàn cầu |
| Trợ cấp chính phủ, tài trợ chính sách | Tồn tại | Có lợi cho phát triển ngành nhưng số tiền cụ thể theo từng dịch vụ không minh bạch |

---

## 6. Điện năng có thực sự là yếu tố quyết định?

Điện năng Trung Quốc rẻ là sự thật. Giá điện đến nơi tại trung tâm dữ liệu Trung Vệ, Ninh Hạ tính đến năm 2026 là <strong>0,36 RMB/kWh</strong>, tương đương khoảng 45% mức giá miền Đông Trung Quốc. Mức trung bình giá điện công nghiệp của Mỹ năm 2025 là <strong>8,62 cent/kWh</strong>, quy đổi theo tỷ giá giả định 7,2 RMB/USD thì tương đương khoảng 0,62 RMB/kWh. Trung Vệ rẻ hơn khoảng <strong>42%</strong>. \[Thực tế: tài liệu chính quyền địa phương Trung Quốc, EIA Mỹ\]

Nhưng chỉ riêng điện năng không thể khiến giá API rẻ hơn 5 lần hay 10 lần. Nếu <strong>ước tính hào phóng</strong> hiệu ứng điện năng, giả định tải IT 1kW mỗi card, PUE 1,1, thì kết quả như sau.

```text
Trung Vệ:        1kW × 1,1 × 0,36 RMB = 0,40 RMB/giờ
Trung bình Mỹ:   1kW × 1,1 × 0,62 RMB = 0,68 RMB/giờ
Chênh lệch:                            khoảng 0,29 RMB/giờ
```

Vì giá L20 on-demand mà Alibaba đưa ra là 14,4 RMB/giờ, nên ngay cả với giả định cận trên này, chênh lệch điện năng cũng chỉ chiếm <strong>khoảng 2%</strong> giá compute. \[Suy luận: tự tính toán\]

Điều này có nghĩa là điện năng quan trọng, nhưng không phải là thủ phạm chính gây ra chênh lệch giá API.

### Bằng chứng phản bác mang tính quyết định

Lợi thế điện năng miền Tây phù hợp với suy luận theo lô và huấn luyện, nhưng API độ trễ thấp phải được đặt tại các region miền Đông hoặc nước ngoài gần người dùng. Và giá Qwen 3.5 Flash của Alibaba <strong>giống hệt nhau không chỉ ở Bắc Kinh mà cả ở Frankfurt và Virginia, với đầu vào 0,029 USD, đầu ra 0,287 USD/triệu token</strong>. \[Thực tế: bảng giá Alibaba Model Studio\]

Đây là bằng chứng trực tiếp nhất cho thấy API giá rẻ không chỉ là kết quả của điện năng Trung Quốc. \[Suy luận: hàm ý của việc giá đồng nhất theo region\]

---

## 7. Hào bảo vệ thực sự của Alibaba là tỷ lệ sử dụng

Alibaba Cloud mạnh hơn ở <strong>năng lực khiến GPU không bao giờ nghỉ</strong>, chứ không phải ở điện năng. \[Thực tế: tài liệu chính thức Alibaba\]

- Suy luận theo lô: <strong>giảm giá 50%</strong> so với giá niêm yết
- L20 spot instance: từ mức on-demand 14,4 RMB xuống thường quanh 2,88 RMB, tiết kiệm khoảng <strong>80%</strong>
- GPU nhàn rỗi: đơn giá hoạt động 0,000018 USD/CU so với đơn giá nhàn rỗi 0,000007 USD/CU
- Kết hợp on-demand, spot và tự động mở rộng quy mô để ứng phó lưu lượng đỉnh

Tuy nhiên spot có rủi ro bị thu hồi nên không thể chuyển toàn bộ API thời gian thực có SLA nghiêm ngặt sang chạy spot. Đây là cấu trúc đặt nhu cầu cơ bản vào on-demand hoặc tài nguyên chuyên dụng, chỉ xử lý phần nhu cầu co giãn bằng spot. \[Suy luận: giới hạn vận hành\]

---

## 8. Huawei Ascend có chắc chắn rẻ hơn không?

Nói chính xác, Ascend không phải GPU mà là <strong>NPU</strong>.

Huawei đưa ra các tuyên bố sau về CloudMatrix 384. \[Thực tế: tài liệu chính thức Huawei\]

- Thông lượng suy luận quy đổi trên một card đơn: 2.300 tokens/s
- Khoảng <strong>4 lần</strong> so với hệ thống phi siêu node trước đây
- Cải thiện MFU trên 50%
- Hiệu năng suy luận trung bình trên mỗi card gấp <strong>3-4 lần</strong> so với H20

Đây là cách bù đắp điểm yếu của từng chip cấu hình thấp bằng thiết kế hệ thống, thông qua gộp tài nguyên và song song hóa chuyên gia MoE.

### Nhưng không thể lập tức suy ra chi phí thấp

- Huawei <strong>chưa công bố TCO được kiểm chứng độc lập theo cùng một mô hình, cùng độ trễ, cùng điện năng</strong>. \[Chưa xác minh\]
- CloudMatrix là cấu trúc gộp nhiều NPU và mạng lại để nâng thông lượng, nên <strong>thông lượng trên mỗi card và tổng chi phí cả cụm là hai chuyện khác nhau</strong>.
- Một nghiên cứu thực địa năm 2026 về Ascend 910 cho thấy để suy luận ổn định cần 12 bản vá mã nguồn, vô hiệu hóa một số tính năng thông lượng cao, và các cơ chế ứng phó sự cố lặp lại. Dù giá phần cứng rẻ, <strong>chi phí kỹ thuật và vận hành vẫn có thể tăng lên</strong>. \[Thực tế: nghiên cứu thực địa Ascend\]

### Phán quyết có điều kiện

| Điều kiện | Phán quyết |
|---|---|
| Mô hình được tối ưu hóa sâu cho Ascend như Qwen, DeepSeek, GLM | Có thể cạnh tranh về chi phí |
| Di chuyển nguyên trạng mô hình dựa trên CUDA | Lợi thế chi phí chưa chắc chắn |
| Suy luận theo lô quy mô lớn trong nội địa Trung Quốc | Có lợi |
| Dịch vụ thời gian thực cho doanh nghiệp toàn cầu | Chưa xác nhận nếu tính cả chi phí phần mềm và SLA |

---

## 9. Khác gì so với xe điện

Điểm giống nhau là ngành chiến lược, đầu tư quy mô lớn, trợ cấp cho doanh nghiệp lớn, giành thị phần bằng cách hạ giá.

Điểm khác biệt là <strong>chi phí chuyển đổi của mô hình AI thấp hơn nhiều</strong>. Chuẩn API tương tự nhau, khách hàng có thể vừa định tuyến đồng thời nhiều mô hình, vừa tự vận hành mô hình mã nguồn mở. Nếu một hãng tăng giá, các mô hình cạnh tranh và việc tự host sẽ tạo ra trần giá.

Ngược lại, các nền tảng kết hợp cả cloud, dữ liệu, bảo mật, thanh toán, quảng cáo và công cụ làm việc có chi phí chuyển đổi cao. <strong>Nếu hiện tượng thắng lấy tất cả xuất hiện, nó sẽ ở tầng phân phối và đám mây chứ không phải tầng mô hình</strong>. \[Suy luận: cấu trúc chi phí chuyển đổi\]

Cấu trúc khả dĩ nhất là như sau.

- Alibaba: cloud, thương mại điện tử, khách hàng doanh nghiệp
- ByteDance: lưu lượng người tiêu dùng, quảng cáo, nội dung
- Tencent: WeChat, dịch vụ doanh nghiệp
- Huawei, Baidu: hạ tầng nội địa và khách hàng khu vực công, doanh nghiệp
- 1-2 hãng mô hình độc lập như DeepSeek: cung cấp mức giá chuẩn về công nghệ

---

## 10. Con đường dự kiến

| Kịch bản | Xác suất phán đoán | Kết quả |
|---|---:|---|
| Thế độc quyền nhóm giá rẻ | <strong>60%</strong> | Thu gọn còn 3-5 hãng, API cơ bản giữ giá rẻ, tăng giá giờ cao điểm và SLA |
| Hàng hóa hóa hoàn toàn | 25% | Mã nguồn mở, MoE, chip tự phát triển dẫn dắt đà giảm giá tiếp theo |
| Bình thường hóa mạnh | 15% | Giá tăng 2-5 lần do áp lực chip, điện năng, huy động vốn |

\[Suy luận: ước tính kịch bản\]

Ngay cả khi giá tăng 5 lần, giá đầu ra của DeepSeek V4-Pro cũng chỉ khoảng <strong>4,35 USD</strong>, vẫn thấp hơn các mô hình tiên phong của Mỹ. <strong>Mức giá hiện tại có thể chưa phải đáy, nhưng xu hướng giá rẻ hóa khó có thể đảo ngược.</strong>

---

## 11. Hàm ý với bán dẫn

API giá rẻ làm tăng lượng sử dụng suy luận, có lợi cho nhu cầu DRAM server, NAND, mạng và điện năng. Ngược lại, nó làm giảm lượng tính toán trên mỗi token và cường độ trang bị HBM, gây áp lực lên hiệu quả kinh tế trên mỗi đơn vị của GPU cao cấp và HBM.

| Đối tượng | Đánh giá |
|---|---|
| Samsung Electronics | Tỷ trọng DRAM, NAND phổ thông cao nên được đệm đỡ tương đối |
| SK Hynix | Cảnh báo dài hạn cho phần bù khan hiếm của HBM |
| NVIDIA | Áp lực lên đơn giá GPU cao cấp, nhưng tổng lượng suy luận tăng là yếu tố phòng thủ |
| Alibaba, Tencent | Hưởng lợi từ mở rộng hệ sinh thái cloud, phân phối nhiều hơn là từ biên lợi nhuận API |

Điều cốt lõi là <strong>tốc độ tăng tổng lượng sử dụng token</strong>, chứ không phải tốc độ giảm giá API. Nếu lượng sử dụng tăng nhanh hơn tốc độ giảm giá, hiệu ứng Jevons sẽ thắng thế; nếu không, hệ số nhân sẽ giảm bắt đầu từ GPU cao cấp và HBM. \[Suy luận: phán đoán xu hướng\]

---

## 12. Kiểm chứng quyết định nằm ở công bố thông tin nửa đầu năm 2026

- <strong>Tỷ suất lợi nhuận gộp API của Zhipu</strong> có tăng lên trên 25-30% sau đợt tăng giá 83% hay không
- <strong>MiniMax có công bố tỷ lệ chi phí API</strong> hay không
- <strong>Tốc độ tăng doanh thu có tiếp tục vượt tốc độ tăng chi phí điện toán</strong> hay không
- Khoảng cách giữa mức phí giờ cao điểm, SLA và mức phí API công khai có trở nên cố định hay không
- Huawei có công bố TCO được kiểm chứng độc lập theo cùng điều kiện hay không

Năm yếu tố này sẽ phân định giữa "chi phí bền vững" và "giá cả được chống đỡ bằng vốn".

---

## Kết luận

Giá API Trung Quốc thấp <strong>không phải vì đó đã là mức giá bình thường có thể tự đứng vững</strong>. Đó là vì cải thiện hiệu suất suy luận và nguồn vốn huy động khổng lồ cùng nhau nâng đỡ nó.

Trung Quốc có lợi thế chi phí mang tính cấu trúc trong việc phục vụ mô hình nội địa, theo lô và đã được tối ưu hóa. Nhưng mức giá API cực thấp đang quan sát được hiện nay không thể chỉ giải thích bằng chip Huawei và điện giá rẻ. Lợi thế chi phí lớn nhất, theo thứ tự, là quy mô mô hình và giảm tham số kích hoạt, xử lý theo lô, caching, lượng tử hóa, tỷ lệ sử dụng GPU đám mây, biên lợi nhuận mục tiêu thấp, còn điện năng và NPU nội địa xếp sau.

Trên góc độ đầu tư, việc API giá rẻ của Trung Quốc không có nghĩa ngay lập tức là "AI Trung Quốc đã xác lập được hào bảo vệ chi phí áp đảo". Cách diễn giải chính xác hơn là <strong>khi dịch vụ suy luận nhanh chóng bị hàng hóa hóa, biên lợi nhuận của các hãng mô hình sẽ giảm xuống, và khả năng giá trị dịch chuyển sang hạ tầng cloud, điện năng, bán dẫn sẽ tăng lên</strong>.

Điều này gây áp lực lên biên lợi nhuận API của các hãng mô hình phương Tây, nhưng vì vốn huy động được lại tiếp tục đổ vào huấn luyện và hạ tầng điện toán, nên <strong>không đồng nghĩa với việc tổng nhu cầu bán dẫn giảm</strong>.

---

_Bài viết này là tài liệu phân tích tổng hợp từ công bố thông tin niêm yết tại Hong Kong (kết quả kinh doanh 2025 và phát hành cổ phiếu mới của Zhipu 02513, báo cáo thường niên 2025 và huy động vốn của MiniMax 00100), bảng giá chính thức của từng hãng (DeepSeek, OpenAI, Google, Alibaba Model Studio, Volcano Engine, Zhipu BigModel, MiniMax Platform), tài liệu chính thức của Huawei và các nghiên cứu liên quan đến CloudMatrix, tài liệu điện năng của chính quyền địa phương Trung Quốc, và thống kê EIA của Mỹ. Tỷ lệ chi phí riêng của mảng API của MiniMax và TCO được kiểm chứng độc lập theo cùng điều kiện của Huawei chưa được công bố; xác suất kịch bản và tính toán điện năng là ước tính dựa trên giả định tại thời điểm viết bài. Các cổ phiếu được đề cập là ví dụ minh họa cho cấu trúc chi phí, không phải khuyến nghị mua bán một cổ phiếu cụ thể nào. Giá cả và số liệu công bố có thể thay đổi sau thời điểm công bố. Quyết định đầu tư và trách nhiệm thuộc về nhà đầu tư._

---

### Bài viết liên quan

- [Sự hội tụ của các mô hình mở Trung Quốc thực sự thay đổi điều gì: tái phân bổ chuỗi giá trị, không phải sụp đổ nhu cầu](/vi/post/china-open-model-convergence-value-chain-redistribution-2026-07-17/)
- [Kimi K3 Tái Định Hình Đường Cong Giá AI: Từ Kimi Linear đến HBM và Chiến Lược Big Tech](/vi/post/kimi-k3-linear-api-pricing-semiconductor-big-tech-impact-2026-07-17/)
- [Tranh luận thực sự trong ngành bán dẫn: bốn chiếc đồng hồ vật lý và một chiếc đồng hồ giá cổ phiếu](/vi/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/)
- [Bán dẫn có mang tính chu kỳ không và giá hợp lý là bao nhiêu? Định giá Samsung, SK Hynix và Micron bằng FCFE và lợi nhuận chuẩn hóa](/vi/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/)
- [Giá trị hiện tại và tương lai của token AI: phân tích giá trị gia tăng của doanh nghiệp bộ nhớ](/vi/post/ai-token-value-memory-value-added-2026-07-09/)
