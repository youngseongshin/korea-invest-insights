---
title: "Sau Astra: Transformer Vòng Lặp Thay Đổi Kinh Tế Hạ Tầng AI Như Thế Nào"
slug: "astra-loop-transformers-inference-economics-2026-09-08"
date: 2026-09-08T18:00:00+09:00
description: "Từ bài viết của CEO Lablup Jeongkyu Shin, chúng tôi phân tích nghiên cứu Huginn, Ouro và MoR để tách biệt hiệu quả tham số khỏi chi phí tính toán, bộ nhớ và triển khai."
categories: ["Tech-Analysis", "Exclusive Analysis"]
tags: ["AI", "Transformer Vòng Lặp", "Astra", "HBM", "Suy Luận", "Lablup"]
draft: false
---

Liệu một mô hình nhỏ có thể giải quyết các bài toán phức tạp hơn bằng cách đi qua cùng một mạng nơ-ron nhiều lần không? CEO Lablup Jeongkyu Shin đặt lại câu hỏi này trong [bài viết Facebook về transformer vòng lặp sau Astra](https://www.facebook.com/jeongkyu.shin/posts/pfbid02jm4iibHsgU11P7gY8e4SZKtKYNNdtHF6wdTQK2EdyDeTMEwxiDvHnHyhyAKphLml). Đằng sau câu hỏi kiến trúc là quyết định hạ tầng: mua bao nhiêu bộ tăng tốc, bao nhiêu bộ nhớ, và vận hành chúng như thế nào.

Nghiên cứu công khai cho thấy một mô hình có thể cải thiện khả năng giải quyết vấn đề trong khi giữ nguyên trọng số lưu trữ, bằng cách thực thi lặp đi lặp lại một khối tính toán dùng chung. Nhưng lặp lại tiêu tốn thời gian và năng lượng. Mô hình nhỏ hơn không tự động đồng nghĩa với dịch vụ rẻ hơn.

Đây là phân tích độc lập được gợi ý từ bài viết của Shin, bổ sung bằng các bài báo gốc và thẻ mô hình. Chúng tôi tách biệt cách bài viết diễn giải Astra khỏi các sự kiện được xác lập công khai, và coi các hàm ý ngành là phân tích có điều kiện. Các nguồn được kiểm tra vào ngày 8 tháng 9 năm 2026.

## Kết quả của Astra không tiết lộ kiến trúc của nó

Thông báo ngày 3 tháng 9 của OpenAI xác nhận việc ra mắt GPT-6 Astra và các cải tiến về năng lực. Tuy nhiên, [thông báo](https://openai.com/index/gpt-6-astra/) và [thẻ hệ thống](https://deploymentsafety.openai.com/gpt-6-astra) được xem xét ở đây không tiết lộ kiến trúc transformer vòng lặp, số lần đệ quy, hay tổng số tham số và số tham số hoạt động.

Do đó, chúng tôi không coi mối liên hệ giữa Astra và thiết kế kiểu Huginn là sự thật đã được xác lập. Các tuyên bố về kích thước 10T/1T trong bài viết và trích dẫn AGI cũng bị loại khỏi tiền đề của phân tích này. Hiệu suất tốt hơn đơn thuần không thể xác định kiến trúc nội bộ.

Vẫn có lý do chính đáng để xem xét tính đệ quy. Các mô hình công khai đã cho thấy những nỗ lực tách biệt dung lượng tham số lưu trữ và tính toán suy luận. Sự phát triển đó có thể được đánh giá mà không cần dựa vào thiết kế chưa được tiết lộ của một mô hình tiên tiến.

## Lưu trữ nhiều hơn và tính toán lâu hơn là hai lựa chọn khác nhau

Tham số là các trọng số số học được điều chỉnh trong quá trình huấn luyện. Mở rộng một mô hình thường làm tăng lượng dữ liệu được lưu trữ. Mixture of Experts (MoE) chọn một số module chuyên gia cho mỗi đầu vào, nhằm thực thi ít tính toán hơn so với tổng dung lượng mô hình.

MoE không xuất phát chỉ từ Switch Transformer. [Bài báo MoE có cổng thưa năm 2017](https://arxiv.org/abs/1701.06538) xuất hiện trước [Switch Transformer năm 2021](https://arxiv.org/abs/2101.03961), vốn đơn giản hóa định tuyến và huấn luyện ở quy mô lớn. Tổng số tham số lớn hơn cũng không nhất thiết đồng nghĩa với nhiều lớp hơn.

Chain-of-thought (CoT) tạo ra các token trung gian mở rộng ngữ cảnh cho tính toán sau. Một mô hình vòng lặp đưa trạng thái nội bộ qua một khối với trọng số dùng chung thêm một lần nữa. Tính toán trung gian không nhất thiết phải chuyển đổi thành một từ ở mỗi bước. Các cách tiếp cận này cũng có thể được kết hợp.

So sánh những gì mỗi cách tiếp cận bổ sung làm rõ sự đánh đổi.

| Cách tiếp cận | Điều gì tăng lên | Chi phí tiềm ẩn |
|---|---|---|
| Mô hình lớn hơn | Trọng số hoặc dung lượng chuyên gia | Lưu trữ, tính toán hoạt động, giao tiếp |
| Chain-of-thought | Token lý luận trung gian | Thời gian tạo, ngữ cảnh và cache |
| Độ sâu đệ quy | Các lượt qua một khối dùng chung | Tính toán lặp lại, độ trễ, quản lý trạng thái |

Đây là so sánh khái niệm. Kinh tế thực tế đòi hỏi đo lường ở cùng độ chính xác, độ dài đầu vào và điều kiện phần cứng.

## Nghiên cứu về "suy nghĩ trước khi nói" sử dụng các cơ chế khác nhau

[Pause tokens](https://arxiv.org/abs/2310.02226) cung cấp thêm tính toán trước khi trả lời. [Quiet-STaR](https://arxiv.org/abs/2403.09629) học cách tạo ra các lý luận trung gian giúp dự đoán các token tiếp theo. Tên của nó không nên được hiểu là bằng chứng rằng nó sử dụng lý luận trạng thái liên tục phi ngôn ngữ.

[Coconut](https://arxiv.org/abs/2412.06769) đưa trạng thái ẩn cuối cùng trở lại như một đầu vào mà không chuyển đổi nó thành một từ. Nó khám phá việc duy trì các khả năng trong một biểu diễn nội bộ trước khi cam kết với ngôn ngữ. Đây không phải là bằng chứng về ý thức con người hay dòng suy nghĩ tự chủ chạy liên tục.

Nghiên cứu về độ sâu đệ quy bao gồm [Universal Transformer năm 2018](https://arxiv.org/abs/1807.03819), lặp lại một phép biến đổi và có thể phân bổ tính toán khác nhau theo từng vị trí. Khó khăn là huấn luyện sự lặp lại có ích: một khối dùng chung phải xử lý các trạng thái từ nhiều giai đoạn khác nhau, và mỗi lượt qua tiếp theo phải cải thiện kết quả. Xung đột vai trò giữa các lớp là một trực giác hữu ích, không phải giải thích phổ quát cho mọi thất bại.

## Sao chép lớp khác với việc chia sẻ cùng một trọng số

[SOLAR 10.7B](https://arxiv.org/abs/2312.15166) của Upstage đã giới thiệu depth up-scaling (DUS): sao chép các lớp hiện có, xóa một số lớp, kết nối chúng thành một mô hình sâu hơn, rồi tiếp tục huấn luyện. Các bản sao bắt đầu giống hệt nhau có thể phát triển thành các trọng số khác nhau. Mô hình kết quả lưu trữ nhiều tham số hơn.

Một mô hình đệ quy tiếp tục chia sẻ cùng một trọng số. DUS tái sử dụng huấn luyện trước để xây dựng mô hình sâu hơn; vòng lặp tăng độ sâu thực thi mà không mở rộng tương ứng các trọng số được lưu trữ. Coi cả hai là cùng một kỹ thuật tiết kiệm bộ nhớ sẽ dẫn đến mô hình chi phí sai.

## Đọc các con số Huginn và Ouro cùng với điều kiện so sánh của chúng

Nghiên cứu [Huginn](https://arxiv.org/abs/2502.05171) của Geiping và cộng sự tách biệt xử lý đầu vào, lõi đệ quy và xử lý đầu ra. Lõi tinh chỉnh trạng thái nội bộ thông qua thực thi lặp đi lặp lại. Các tác giả đã huấn luyện một mô hình 3,5B tham số trên 800B token và báo cáo hiệu suất nhiệm vụ lý luận được cải thiện khi tính toán đệ quy tăng lên.

Con số 50B trong phần tóm tắt cần được đọc cẩn thận. Nó mô tả các cải thiện lên đến tải tính toán tương đương 50B tham số. Nó không đảm bảo chất lượng của mô hình 50B trên mọi nhiệm vụ, cũng không đảm bảo chất lượng đó đạt được với cùng chi phí. Một tập trọng số nhỏ sử dụng nhiều tính toán hơn là một kết quả nghiên cứu; kinh tế dịch vụ đòi hỏi đo lường riêng biệt.

[Ouro](https://arxiv.org/abs/2510.25741), từ ByteDance và các cộng tác viên, được phát hành vào tháng 10 năm 2025. Bài báo đề cập đến một họ các mô hình 1,4B và 2,6B, và báo cáo so sánh với các mô hình lên đến 12B trên nhiều benchmark. Tuy nhiên, [thẻ mô hình Ouro-1.4B chính thức](https://huggingface.co/ByteDance/Ouro-1.4B) mô tả mô hình cụ thể đó là tương đương với các mô hình thông thường 3–4B. Nói rằng 1,4B luôn thay thế 12B sẽ phóng đại quá mức kết quả so sánh.

Số lượng tham số nên được đọc cùng với dữ liệu huấn luyện, số lần đệ quy và các nhiệm vụ đánh giá. Hiệu quả suy luận rõ ràng cũng có thể là kết quả của đầu tư huấn luyện trước đáng kể.

## Ít trọng số lưu trữ hơn không loại bỏ nút thắt cổ chai bộ nhớ

Hãy xem xét một phép tính minh họa. Lưu trữ 3,5B tham số ở 2 byte mỗi tham số đòi hỏi khoảng 7GB cho trọng số. Việc sử dụng lặp đi lặp lại các trọng số đó không nhân yêu cầu lưu trữ theo số lần đệ quy. Đây là số học, không phải phép đo tổng mức sử dụng bộ nhớ GPU của Huginn.

Tổng bộ nhớ suy luận còn bao gồm KV cache dùng để tái sử dụng ngữ cảnh trước, các trạng thái trung gian và không gian làm việc thực thi. [Hướng dẫn tối ưu hóa suy luận của NVIDIA](https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/) phân biệt trọng số và KV cache là hai thành phần bộ nhớ chính. Ngữ cảnh dài hơn và nhiều yêu cầu đồng thời hơn làm tăng áp lực cache. Liệu cache có thể được chia sẻ giữa các bước đệ quy hay không phụ thuộc vào thiết kế.

Tái sử dụng trọng số cũng khác với việc giảm di chuyển dữ liệu. Nếu trọng số không thể ở lại trong bộ nhớ on-chip nhanh, một lượt qua khác có thể cần đọc lại chúng từ HBM. Lặp lại có thể làm tăng nhu cầu băng thông song song với tính toán. Nếu không xem xét hệ thống phân cấp bộ nhớ và cách triển khai cụ thể, không thể tuyên bố rằng vòng lặp là lý do HBM trở nên không cần thiết.

## Phần mềm phải hiện thực hóa khoản tiết kiệm từ thoát sớm

[Mixture-of-Recursions (MoR)](https://arxiv.org/abs/2507.10524) thay đổi độ sâu đệ quy theo từng token và quản lý tính toán cùng bộ nhớ đệm xung quanh các token còn hoạt động ở một độ sâu nhất định. Mục tiêu là hướng tính toán đến các token khó hơn thay vì lãng phí vào những token dễ.

Triển khai thực tế làm điều này phức tạp hơn. Các yêu cầu đệ quy khác nhau giữa các request có thể làm giảm hiệu quả batching. Các bộ lên lịch cần cho phép công việc khác sử dụng tài nguyên được giải phóng bởi hoàn thành sớm. Đây là thách thức vận hành được dự đoán trước, không phải kết quả đo lường cho một sản phẩm thương mại cụ thể.

Thẻ mô hình Ouro cung cấp một ví dụ cụ thể. Mô hình hỗ trợ thoát sớm, nhưng thẻ nêu rõ rằng vLLM không hỗ trợ tính năng này và thay vào đó thực thi toàn bộ số lần đệ quy được cấu hình. Một khả năng kiến trúc không tự động được triển khai trong engine phục vụ.

Điều này đặt ra các câu hỏi cụ thể cho các công ty phần mềm hạ tầng AI như Lablup: liệu nền tảng có thể batch các công việc với độ sâu đệ quy khác nhau, tái sử dụng cache, và giảm thời gian hoàn thành cùng chi phí năng lượng ở cùng chất lượng không? Đây là những câu hỏi để đánh giá cơ hội, không phải tuyên bố rằng Lablup đã hỗ trợ các tính năng đó hay đã chứng minh tăng trưởng doanh thu từ chúng.

## Bán dẫn Hàn Quốc đối mặt với cả tiết kiệm tài nguyên lẫn mở rộng sử dụng

Sau đây là các kịch bản có điều kiện cho việc áp dụng mô hình vòng lặp rộng rãi hơn, không phải dự báo thu nhập.

| Điều kiện | Tác động ngành có thể xảy ra | Bằng chứng cần thiết |
|---|---|---|
| Ít trọng số và ít cache hơn ở cùng chất lượng | Áp lực bộ nhớ thấp hơn mỗi request | Bộ nhớ đo lường ở cùng ngữ cảnh và mức đồng thời |
| Nhiều đệ quy hơn cho các bài toán khó | Nhu cầu thời gian tăng tốc và năng lượng cao hơn | Thời gian GPU và năng lượng trên mỗi nhiệm vụ thành công |
| Chi phí thấp hơn mở rộng sử dụng | Nhu cầu hạ tầng tổng hợp ổn định hoặc tăng | Sử dụng thực tế của khách hàng và kế hoạch mua sắm |
| Đệ quy và quản lý cache làm giảm hiệu quả batching | Thương mại hóa bị trì hoãn | Thông lượng ở cùng mục tiêu độ trễ |

Đối với các nhà cung cấp bộ nhớ như Samsung Electronics và SK hynix, nhu cầu tổng hợp phụ thuộc vào cả tài nguyên mỗi request lẫn tổng số request. Hiệu quả có thể kích thích áp dụng, nhưng tăng trưởng đó không thể được giả định là vượt quá phần tiết kiệm. Phân tích này một mình không đủ để điều chỉnh dự báo nhu cầu HBM hay thu nhập công ty.

So sánh hữu ích hơn là chi phí hoàn thành một nhiệm vụ thành công. Điểm benchmark cao vẫn có thể tốn kém nếu việc lặp lại mất quá nhiều thời gian hoặc phải thử lại thường xuyên. Ngược lại, tính toán thêm có thể giảm tổng chi phí nếu nó cải thiện đủ tỷ lệ thành công ngay lần đầu.

## Bài kiểm tra tiếp theo là chi phí nhiệm vụ, không phải số lượng tham số

Kiểm chứng trường hợp công nghiệp đòi hỏi so sánh tổng bộ nhớ, thời gian hoàn thành, năng lượng và thông lượng đồng thời ở cùng độ chính xác. Độ trễ đuôi quan trọng không kém giá trị trung bình, ngay cả với các câu hỏi dễ. Nếu nhiều đệ quy hơn không còn cải thiện chất lượng, hoặc tổn thất batching vượt quá tiết kiệm tài nguyên, luận điểm thương mại hóa trở nên yếu hơn.

Tiết lộ kiến trúc thêm có thể xác lập xem Astra có thuộc dòng nghiên cứu này hay không. Trong khi đó, một thay đổi có thể kiểm chứng vẫn còn đó: lập kế hoạch hạ tầng phải xem xét thời gian tính toán cho mỗi bài toán và khi nào nên dừng lại, cùng với kích thước của mô hình được lưu trữ. Biến sự linh hoạt đó thành chi phí thực tế thấp hơn là bài kiểm tra chung của cả phần cứng lẫn phần mềm.
