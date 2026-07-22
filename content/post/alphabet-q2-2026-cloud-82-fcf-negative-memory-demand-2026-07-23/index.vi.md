---
title: "Quý 2 của Alphabet: Cloud +82% khép lại tranh luận về cầu, FCF âm mở ra tranh luận về tiền mặt"
slug: "alphabet-q2-2026-cloud-82-fcf-negative-memory-demand-2026-07-23"
date: 2026-07-23T11:00:00+09:00
description: "Quý 2 của Alphabet hạ mạnh xác suất vách đá nhu cầu AI sau 2028: Cloud tăng 82%, backlog đạt 514 tỷ USD, khách hàng hiện hữu dùng vượt cam kết hơn 50%. Cùng bản báo cáo đó là FCF quý âm lần đầu trong lịch sử, hướng dẫn CAPEX 2026 nâng lên tối đa 205 tỷ USD, và việc thuê compute từ SpaceX khoảng 920 triệu USD mỗi tháng vì thiếu công suất. Chúng tôi đọc điểm kết của tranh luận cầu và điểm khởi đầu của tranh luận tiền mặt, dịch sang HBM, DRAM máy chủ và eSSD, và chuẩn bị bảng chấm điểm Microsoft, Amazon cuối tháng 7."
categories: ["Exclusive Analysis", "Company-Analysis", "Market-Outlook"]
tags: ["Alphabet", "Google Cloud", "CAPEX AI", "TPU", "HBM", "DRAM máy chủ", "Bộ nhớ AI", "FCF", "Backlog", "Lợi nhuận Big Tech", "Research OS"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Bối cảnh: Bài viết trước [Ai đốt hết số token đó?](/vi/post/who-burns-the-tokens-nvidia-sovereign-codex-2026-07-19/) đã viết rằng mắt xích yếu cuối cùng trong tranh luận CAPEX AI, tức cầu cuối cùng, đã bắt đầu có con số đi kèm, và để việc phán định lại cho mùa báo cáo kết quả kinh doanh quanh ngày 30/7. Bảng điểm đầu tiên đã đến sớm hơn dự kiến. Alphabet công bố kết quả kinh doanh quý 2 vào rạng sáng 23/7 giờ Hàn Quốc. Bài viết này tổng hợp hai ghi chú phân tích mổ xẻ cùng một kết quả kinh doanh từ hai góc độ khác nhau thành một bài duy nhất. Nói trước kết luận, tranh luận về phía cầu về cơ bản đã kết thúc, và sân khấu tranh luận đã chuyển sang dòng tiền và lợi nhuận trên vốn.

## TL;DR

- Doanh thu Google Cloud đạt 24,8 tỷ USD, <strong>+82%</strong> (đồng thuận +64%), đánh dấu năm quý liên tiếp tăng tốc theo chuỗi 32% → 34% → 48% → 63% → 82%. Backlog tăng ròng 52 tỷ USD, từ 462 tỷ USD lên <strong>514 tỷ USD</strong>, ngay cả khi lượng doanh thu được ghi nhận cũng đang lớn dần.
- Chất lượng của cầu còn quan trọng hơn. Khách hàng Cloud hiện hữu đang chi tiêu vượt mức cam kết ban đầu trung bình <strong>hơn 50%</strong>, còn lưu lượng API mô hình Gemini tăng lên 22 tỷ token/phút từ 16 tỷ, tăng 37,5% chỉ trong một quý. Vì nguồn cung không đủ, từ tháng 6 Alphabet đã bắt đầu trả <strong>khoảng 920 triệu USD mỗi tháng cho SpaceX</strong> để thuê compute AI. Đây là cảnh tượng chưa từng có khi một hyperscaler trở thành bên mua ròng compute.
- Ở mặt sau của cùng kết quả kinh doanh đó, FCF theo quý ghi nhận <strong>-5,9 tỷ USD, lần đầu tiên âm trong lịch sử</strong>. CAPEX 44,9 tỷ USD đã vượt qua OCF 39,1 tỷ USD, và hướng dẫn CAPEX 2026 được nâng lại từ 180-190 tỷ USD lên <strong>195-205 tỷ USD</strong>, đồng thời báo hiệu mức tăng lớn trong năm 2027.
- Phán đoán chia làm ba. Khả năng xảy ra vách đá nhu cầu AI sau năm 2028 đã thấp hơn. Điểm đảo chiều FCF của Alphabet bị đẩy lùi từ năm 2027 sang giai đoạn 2028-2029. Với bộ nhớ, sức mạnh nhu cầu về khối lượng được tái xác nhận, nhưng tính bền vững của giá và biên lợi nhuận đỉnh vẫn là vấn đề riêng biệt.
- Chúng tôi giữ nguyên xác suất kịch bản cầu cơ sở 45%, vượt trội 35%, dưới kỳ vọng 20%. Tuy nhiên, đã có thêm một nhánh bằng chứng thực đo củng cố cho kịch bản vượt trội 35%, còn tiền đề cốt lõi của kịch bản dưới kỳ vọng 20%, tức việc CAPEX Big Tech giảm tốc sớm, đã yếu đi sau bản in kết quả kinh doanh này. Lần chấm điểm tiếp theo là Microsoft (rạng sáng 30/7 giờ Hàn Quốc) và Amazon (31/7).

<div class="thesis-callout">
<div class="thesis-callout__label">Luận điểm chính</div>

Cloud +82% và FCF theo quý lần đầu tiên âm trong lịch sử là hai mặt của cùng một kết quả kinh doanh. Trước câu hỏi liệu cầu có thực hay không, Alphabet đã trả lời bằng mức sử dụng vượt cam kết và hành động thuê cả server của người khác với giá cao hơn. Đổi lại, hóa đơn để đón nhận nhu cầu đó đã đến sớm hơn dự kiến. Tiêu chí chấm điểm của thị trường giờ đã chuyển từ sự tồn tại của cầu sang lợi nhuận tiền mặt sau khấu hao, và với nhà đầu tư bộ nhớ, kết quả kinh doanh này là viện binh cho khối lượng chứ không phải bảo chứng cho biên lợi nhuận.

</div>

## 1. Trước tiên là các con số: điều gì đã được công bố

| Hạng mục | Thực tế Q2/26 | Cơ sở so sánh | Phán định |
|---|---|---|---|
| Doanh thu toàn công ty | 119,8 tỷ USD, +24% | Đồng thuận khoảng 116,9 tỷ USD | Vượt |
| Doanh thu Google Cloud | 24,8 tỷ USD, +82% | Đồng thuận 22,4 tỷ USD, +64% | Vượt mạnh |
| Lợi nhuận hoạt động Cloud | 8,8 tỷ USD (biên 35,6%) | Năm trước 2,8 tỷ USD (biên 20,7%) | Cải thiện |
| Doanh thu Tìm kiếm | 63,3 tỷ USD, +17% | Đồng thuận 63,4 tỷ USD | Phù hợp |
| Lợi nhuận hoạt động toàn công ty | 40,8 tỷ USD, +30% (biên 34,0%) | Biên thấp hơn đồng thuận | Trái chiều |
| EPS điều chỉnh | Khoảng 2,85 USD | Đồng thuận khoảng 2,89 USD | Thấp hơn nhẹ |
| Dòng tiền hoạt động (OCF) | 39,1 tỷ USD | CAPEX 44,9 tỷ USD | Đảo chiều |
| FCF theo quý | -5,9 tỷ USD | Quý trước 10,1 tỷ USD | Lần đầu âm trong lịch sử |
| Backlog Cloud | 514 tỷ USD | Quý trước 462 tỷ USD | +52 tỷ USD |
| Hướng dẫn CAPEX 2026 | 195-205 tỷ USD | Trước đó 180-190 tỷ USD | Nâng lại |

[Thực tế: công bố và earnings call của Alphabet]

Các con số GAAP có ảo giác quang học. EPS GAAP công bố là 9,11 USD, lợi nhuận ròng 112,1 tỷ USD, +298% so với cùng kỳ, nhưng trong đó có khoảng 99 tỷ USD lãi đánh giá lại (trước thuế, tương đương khoảng 6,26 USD/cổ phiếu sau thuế) từ các cổ phần chưa niêm yết tại Anthropic và SpaceX. Sau khi loại bỏ khoản mục không liên quan đến hoạt động kinh doanh này, EPS thực chất khoảng 2,85 USD, thấp hơn nhẹ so với kỳ vọng thị trường. Doanh thu và Cloud thắng lớn, nhưng chất lượng lợi nhuận không mạnh bằng con số bề mặt. [Thực tế: tính toán lại từ công bố]

## 2. Tranh luận về cầu: vì sao có thể coi là đã kết thúc

Bài viết trước đã chỉ ra mắt xích yếu của cầu cuối cùng, lấy con số 3 triệu người dùng Codex thêm trong ba ngày làm bằng chứng thực đo đầu tiên. Bản in kết quả kinh doanh của Alphabet đã chồng thêm bốn nhánh bằng chứng thực đo lên trên đó.

<strong>Mức sử dụng đang vượt trước hợp đồng.</strong> Lưu lượng API mô hình Gemini tăng từ 16 tỷ token/phút lên 22 tỷ token/phút, tăng 37,5% chỉ trong một quý, còn số nhà phát triển hàng tháng đã vượt 9 triệu người. Khách hàng Cloud hiện hữu đang chi tiêu trung bình hơn 50% so với cam kết ban đầu, và mức vượt này còn lớn hơn quý trước. Tốc độ thu hút khách hàng mới gấp đôi năm trước, khối lượng giao dịch marketplace gấp bảy lần. [Thực tế: thư CEO, earnings call] Giả thuyết cho rằng cầu chỉ dựa vào hợp đồng dài hạn của một số ít phòng thí nghiệm tiên phong không tương thích với dữ liệu cho thấy mức tiêu thụ thực tế sau hợp đồng đã vượt cam kết.

<strong>Nơi phát sinh cầu đã mở rộng.</strong> Bên cạnh cầu phát triển mô hình như tiền huấn luyện quy mô lớn cho Gemini 4, năm nhánh đã được trình bày đồng thời: suy luận doanh nghiệp trong tài chính, dược phẩm, bán lẻ, viễn thông, sản xuất; khối lượng công việc BigQuery và bảo mật; các dịch vụ tiêu dùng như AI Mode trong Tìm kiếm và app Gemini; và cả doanh số bán ngoài hệ thống TPU cung cấp trực tiếp cho trung tâm dữ liệu của khách hàng. Khoảng 90% doanh nghiệp Fortune 100 dùng Gemini Enterprise, có 500 khách hàng cloud xử lý trên 1 nghìn tỷ token mỗi năm, và hơn 2.000 khách hàng xử lý trên 100 tỷ token. [Thực tế: thư CEO]

<strong>Nguồn cung vẫn đang giới hạn tốc độ tăng trưởng.</strong> CFO khẳng định môi trường vẫn bị hạn chế về nguồn cung. Alphabet đang thuê công suất trung tâm dữ liệu bên thứ ba với giá cao để bù đắp phần thiếu hụt ngắn hạn, và giải thích rằng việc chấp nhận khoảng 6 tháng kém hiệu quả là xứng đáng để giữ được khách hàng lớn. Nối tiếp mạch đó là tin lớn nhất của cuộc gọi lần này. Từ tháng 6, Alphabet đã ký hợp đồng thuê compute AI từ SpaceX với giá khoảng 920 triệu USD mỗi tháng, quy đổi theo năm khoảng 11 tỷ USD. [Thực tế: earnings call, báo chí] Việc công ty tính toán nhanh nhạy nhất thế giới lại đi thuê server của người khác với giá cao hơn là bằng chứng hành vi đối lập trực diện với giả thuyết cầu bị thổi phồng.

<strong>Backlog vẫn tăng ngay cả khi đang được ghi nhận.</strong> Doanh thu Cloud quý 2 tăng khoảng 23,8% so với quý trước, cho thấy các hợp đồng lớn đang chuyển hóa nhanh thành doanh thu, nhưng số dư backlog vẫn tăng thêm 52 tỷ USD. Backlog hiện tại gấp khoảng 5,2 lần doanh thu Cloud quy đổi theo năm của quý 2, và công ty cho biết hơn một nửa sẽ được ghi nhận trong vòng 24 tháng. [Thực tế: công bố, earnings call] Đây là bằng chứng mạnh cho tầm nhìn đến năm 2027. Tuy nhiên, độ tập trung khách hàng và số tiền ghi nhận theo từng năm từ 2028 trở đi chưa được công bố. [Chưa xác minh: chi tiết backlog chưa công bố]

Lập luận phản bác về hiệu quả hóa cũng mất sức trong quý này. Chi phí trên mỗi phản hồi của AI Mode đã giảm xuống mức thấp nhất kể từ khi ra mắt, nhưng số người dùng và khối lượng truy vấn lại tăng nhanh hơn. AI Mode có 1 tỷ người dùng hàng tháng, app Gemini có 950 triệu MAU. Mối quan hệ mà mức sử dụng tăng nhanh hơn mức giảm chi phí trên mỗi đơn vị đã được xác nhận ngay cả ở quy mô của Alphabet, cùng hướng với mô hình Jevons đã thấy ở Codex. [Suy luận: quan hệ hiệu quả-mức sử dụng]

## 3. Tranh luận về tiền mặt: hóa đơn đến sớm hơn dự kiến

Ở phía đối diện với cầu, điều mà kết quả kinh doanh lần này đã xác định chắc chắn là quy mô và thời hạn của chi tiêu.

CAPEX quý 2 đạt 44,9 tỷ USD, gấp đôi năm trước, vượt qua OCF 39,1 tỷ USD, và cường độ vốn theo quý (CAPEX/OCF) khoảng 115%. Phần số học cũng nặng nề không kém. CAPEX nửa đầu năm khoảng 80,6 tỷ USD, nên để chạm mức trần hướng dẫn cả năm 205 tỷ USD, nửa cuối năm cần chi trung bình mỗi quý 57,2-62,2 tỷ USD, tức nhiều hơn quý 2 khoảng 27-38%. Khả năng FCF phục hồi đáng kể trong nửa cuối 2026 và năm 2027 là thấp. [Suy luận: tính toán riêng]

Đầu mối cho năm 2027 cũng đã xuất hiện. CFO giữ nguyên dự báo CAPEX 2027 sẽ tăng mạnh, còn đồng thuận thị trường khoảng 257 tỷ USD. Lộ trình từ 205 tỷ USD lên 257 tỷ USD tương ứng mức tăng khoảng +25%. Đây là lộ trình giảm tốc từ khoảng +76% năm nay xuống +25% năm sau, chứ chưa phải kịch bản tái tăng tốc lên mức 300 tỷ USD. [Thực tế: earnings call, đồng thuận] Sự phân biệt này quan trọng. Nếu là lộ trình giảm tốc, khung logic của điểm đảo chiều FCF vẫn còn nguyên; nếu tái tăng tốc, chính khung logic đó sẽ sụp đổ.

Nếu tính trước độ nhạy cho năm 2028, tiêu chí phán định sẽ trở nên rõ ràng hơn. Điểm xuất phát là OCF lũy kế 12 tháng hiện tại, 185,7 tỷ USD.

| Giả định CAPEX 2028 | OCF cần để FCF = 0 | CAGR OCF cần thiết | OCF cần để FCF đạt 50 tỷ USD | Tốc độ tăng cần thiết |
|---|---|---|---|---|
| 200 tỷ USD | 200 tỷ USD | Khoảng 3,8% | 250 tỷ USD | Khoảng 16,0% |
| 230 tỷ USD | 230 tỷ USD | Khoảng 11,3% | 280 tỷ USD | Khoảng 22,8% |
| 250 tỷ USD | 250 tỷ USD | Khoảng 16,0% | 300 tỷ USD | Khoảng 27,1% |

[Suy luận: độ nhạy tự tính, không phải hướng dẫn của công ty]

Nếu CAPEX ổn định quanh mức 200 tỷ USD vào năm 2028, việc FCF phục hồi không khó. Nếu tiếp tục tăng lên 230-250 tỷ USD, OCF gộp của Cloud và Tìm kiếm phải tăng hơn 20%/năm thì mới quay lại mức FCF trước đây. Nếu Cloud +82% và biên 35,6% được duy trì trong một thời gian, đây không phải con số bất khả thi, nhưng khấu hao, chi phí điện, tiền thuê ngoài, và cơ cấu bán phần cứng TPU biên thấp hơn đang đè theo hướng ngược lại.

Sự chuyển đổi trong cơ chế phân bổ vốn cũng đã chính thức hóa trong quý này. Alphabet là công ty có 242,5 tỷ USD tiền mặt và chứng khoán khả mại, OCF 12 tháng 185,7 tỷ USD, nên khả năng thanh toán tự thân không phải là điều đáng tranh cãi. Tuy nhiên, trong quý 2 công ty đã huy động khoảng 30,5 tỷ USD cổ phiếu phổ thông, khoảng 19,1 tỷ USD cổ phiếu ưu đãi chuyển đổi, và khoảng 21,1 tỷ USD nợ ròng, đồng thời không mua lại cổ phiếu quỹ. Nợ đã tăng từ khoảng 16 tỷ USD lên khoảng 100 tỷ USD chỉ trong 12 tháng. [Thực tế: công bố] Từ một công ty từng dùng OCF để trang trải cả CAPEX lẫn mua lại cổ phiếu, Alphabet đã chuyển thành công ty dừng mua lại để dồn cho CAPEX, thậm chí huy động cả nợ lẫn vốn cổ phần. Đây không phải tín hiệu rủi ro thanh khoản mà là tín hiệu cho thấy cơ chế phân bổ vốn đã thay đổi, và điều an ủi từ góc nhìn tín dụng là trọng lượng huy động đang nghiêng về phía cổ đông hơn là thị trường trái phiếu.

## 4. Chấm điểm ba câu hỏi

Trước kết quả kinh doanh này, việc chấm điểm ba câu hỏi cho ra kết quả như sau.

<strong>Cầu AI có duy trì sau năm 2028 không. Khả năng xảy ra vách đá đã thấp hơn.</strong> Cầu đang lan tỏa từ huấn luyện sang suy luận, dữ liệu, bảo mật và công việc doanh nghiệp; mức tiêu thụ thực tế vượt cam kết; mức sử dụng tăng nhanh hơn cải thiện hiệu quả; phần lớn doanh thu bán ngoài TPU dự kiến ghi nhận vào năm 2027; và nguồn cung vẫn thiếu đến mức năm 2027 vẫn phải tăng mạnh CAPEX. Nhìn nhận chính xác là năm 2028 không phải thời điểm cầu kết thúc, mà là thời điểm năng lực cung mới chính thức vận hành và bước lên bàn kiểm chứng.

<strong>FCF của Alphabet có đảo chiều không. Có thể, nhưng thời điểm bị đẩy lùi.</strong> Điểm giao cắt FCF theo quý đã đến sớm hơn dự kiến ban đầu (đầu năm 2027), nhưng dù đặt OCF 2027 lạc quan ở mức 230-240 tỷ USD, với CAPEX 257 tỷ USD thì FCF cả năm vẫn ở mức 0 trở xuống. Việc quay lại có lãi chỉ thành lập vào năm 2028, và chỉ khi tốc độ tăng CAPEX 2028 giảm xuống mức một chữ số. Sự tái tăng tốc mạnh của FCF là kịch bản có điều kiện cho giai đoạn 2028-2029.

<strong>Điều này có dẫn đến việc mua bộ nhớ liên tục không. Tích cực mạnh về khối lượng, trung lập về giá và biên lợi nhuận.</strong> Mổ xẻ ở phần tiếp theo.

## 5. Dịch sang bộ nhớ: viện binh cho khối lượng, không phải bảo chứng cho biên lợi nhuận

Khoảng 60% CAPEX hạ tầng kỹ thuật quý 2 dành cho máy chủ, 40% cho trung tâm dữ liệu và mạng. Đầu tư máy chủ bao gồm cả TPU, GPU, CPU, HBM, DRAM máy chủ, SSD và chất bán dẫn mạng. [Thực tế: earnings call]

Các hạng mục hỗ trợ cầu HBM khá rõ ràng. Đó là thế hệ TPU mới và việc đưa vào NVIDIA Vera Rubin, tiền huấn luyện quy mô lớn cho Gemini 4, khối lượng suy luận doanh nghiệp tăng, kiến trúc mạng thế hệ mới kết nối 1 triệu bộ gia tốc, và doanh số bán ngoài hệ thống TPU sẽ được ghi nhận đầy đủ từ năm 2027. Điều quan trọng là dù TPU tự phát triển thay thế một phần GPU NVIDIA, cầu HBM không biến mất mà chỉ chuyển kênh mua từ chuỗi cung ứng GPU sang chuỗi cung ứng hệ thống TPU. Nếu cộng thêm cả việc thuê compute từ bên thứ ba, kênh cầu của HBM và DRAM máy chủ đã mở rộng thành ba nhánh: trung tâm dữ liệu tự có, TPU bán ngoài, và compute đi thuê. [Suy luận: phân rã kênh cầu]

Luận cứ cho DRAM máy chủ và eSSD cũng dày thêm sau bản in này. AI agent không chỉ dùng bộ gia tốc mà còn chạy tiền xử lý, quản lý trạng thái, bảo mật và điều phối trên server CPU. Alphabet đã nhấn mạnh cùng lúc cả CPU Axion lẫn khối lượng công việc dữ liệu và bảo mật đang tăng. Con số 500 khách hàng xử lý trên 1 nghìn tỷ token mỗi năm cho thấy nhu cầu lưu trữ dẫn đến log, checkpoint, chỉ mục tìm kiếm và cơ sở dữ liệu vector không chỉ giới hạn ở huấn luyện. [Thực tế: thư CEO] Nền tảng phía cầu của việc DRAM máy chủ tái siết chặt (giá hợp đồng quý 3 dự báo +13-18%, thời gian giao hàng 40 tuần) đã thấy ở bài viết trước, nay được tái xác nhận qua kết quả kinh doanh Big Tech.

Dù vậy, không nên chỉ dựa vào kết quả kinh doanh này để nâng ước tính lợi nhuận 2028 của các công ty bộ nhớ. Khi mua sắm thiết bị tăng vọt, năng lực cung bộ nhớ cũng sẽ tăng trong giai đoạn 2027-2029. Việc mở rộng chip tự phát triển làm giảm quyền định giá của NVIDIA trong hệ thống, chi phí suy luận trên mỗi phản hồi đang giảm nhanh, và khi Alphabet bắt đầu siết chặt hiệu quả CAPEX, áp lực giảm giá linh kiện sẽ truyền xuống dọc theo chuỗi cung ứng. Giá cao của HBM4 và HBM thế hệ tiếp theo bao gồm cả phần bù khan hiếm đầu thế hệ và phần bù hiệu suất, nên không phải giá trị vĩnh viễn. Tổng hợp lại như sau.

| Hạng mục | Phán đoán trước kết quả kinh doanh | Phán đoán sau kết quả kinh doanh |
|---|---|---|
| Cầu bit AI accelerator, HBM | Cao | Rất cao |
| Cầu DRAM máy chủ, eSSD | Khá cao | Cao |
| Đóng gói tiên tiến, mạng | Cao | Rất cao |
| Vách đá cầu năm 2028 | Khả năng thấp | Khả năng thấp hơn nữa |
| Tính bền vững của ASP bộ nhớ | Không chắc chắn | Không chắc chắn |
| Duy trì biên lợi nhuận đỉnh bộ nhớ | Thấp | Thấp |
| Big Tech phục hồi FCF sớm | Trung bình | Thấp hơn |
| Lợi nhuận trên vốn gia tăng của CAPEX | Chưa được chứng minh | Chứng minh một phần, tiếp tục kiểm chứng |

[Suy luận: phán đoán tổng hợp]

Rủi ro của bán dẫn năm 2028 không phải là hủy đơn hàng mà là việc ASP và biên lợi nhuận trở về mức bình thường. Điều này phù hợp với kịch bản cầu 45/35/20. Bản in lần này đã chồng thêm một bằng chứng thực đo cho luận cứ vượt trội 35%, đồng thời làm yếu đi tiền đề CAPEX Big Tech giảm tốc sớm vốn là nền tảng của kịch bản dưới kỳ vọng 20%. Bản thân xác suất sẽ được cập nhật sau khi xác nhận thêm cả Microsoft và Amazon. Từ góc nhìn Samsung Electronics và SK Hynix, đây là bản in giúp cải thiện nền tảng cầu cho cuộc đàm phán giá HBM hướng tới năm 2027 sẽ bắt đầu từ quý 4.

## 6. Phản ứng giá cổ phiếu, và sự khác biệt phán đoán giữa hai ghi chú

Phản ứng thị trường tóm gọn tính chất của giai đoạn này. Ngay sau công bố, cổ phiếu mở đầu phiên ngoài giờ giảm khoảng 2%, có lúc phục hồi lên gần tham chiếu, rồi bị đẩy lùi khi CAPEX được nâng lên trong cuộc gọi, khiến mức giảm nới rộng lên khoảng 3-5%. Tính đến sáng 23/7 giờ Hàn Quốc, giá cổ phiếu quanh mức 342 USD, thấp hơn khoảng 1,5% so với giá đóng cửa phiên trước khoảng 347 USD. [Thực tế: dữ liệu thị trường] Quy luật của năm 2026, rằng chính CAPEX chứ không phải việc vượt kỳ vọng lợi nhuận mới quyết định phản ứng trong một thị trường nơi vượt kỳ vọng đã trở thành mặc định, lại lặp lại lần thứ năm. Đọc theo chiều ngược lại, việc mức giảm chỉ dừng ở mức này trước mức tăng trưởng +82% cũng là tín hiệu cho thấy chừng nào tăng trưởng còn được chứng minh, thị trường vẫn sẽ tiêu hóa được chi tiêu.

Hai ghi chú làm chất liệu tổng hợp đã đưa ra kết luận khác nhau từ cùng một sự thật. Một ghi chú chọn tạm hoãn theo tiêu chí chứng minh cấu trúc. Cách diễn đạt chính xác không phải là lợi nhuận trên vốn đã được chứng minh, mà là khả năng được chứng minh đang cao nhất, và ghi chú này bảo lưu việc đưa ra mục tiêu giá trước FCF âm, việc huy động vốn, và cảnh báo tăng CAPEX năm 2027. Ghi chú còn lại giữ khuyến nghị mua theo giá vào lệnh. Ghi chú này đưa ra mục tiêu 12 tháng 430 USD, dựa trên giả định mức điều chỉnh 15% so với đỉnh, áp dụng hệ số 28-29 lần cho EPS 2027 khoảng 15 USD (loại trừ lãi đánh giá lại), kèm điều kiện rút lại là sẽ tính lại nếu CAPEX 2027 được lượng hóa gần mức 300 tỷ USD. [Thực tế: kết luận của hai ghi chú]

Sự khác biệt giữa hai phán đoán không nằm ở nhận thức sự thật mà ở thời gian biểu và tiêu chí. Góc nhìn cấu trúc đặt gánh nặng chứng minh lên công ty cho đến khi lợi nhuận tiền mặt sau khấu hao được xác nhận bằng con số cụ thể, còn góc nhìn định giá tính toán xem rủi ro đó đã được phản ánh bao nhiêu vào mức giá đã điều chỉnh. Theo nguyên tắc của blog này, chúng tôi không khuyến nghị một hướng cụ thể mà trình bày song song cả hai khung, nhưng mẫu số chung là rõ ràng. Dù theo hướng nào, biến số phán định tiếp theo không phải là cầu mà là tiền mặt.

## 7. Bảng phán định: hai tuần tới sẽ quyết định

Dưới đây là tổng hợp những ô đã được lấp đầy và những ô mới mở ra sau kết quả kinh doanh lần này.

- Phần bình luận CAPEX Big Tech thuộc về Alphabet đã được xác định là nâng lên. Điều còn lại là hướng dẫn FY27 đầu tiên của Microsoft (cuộc gọi rạng sáng 30/7 giờ Hàn Quốc) và tốc độ tăng trưởng AWS của Amazon (rạng sáng 31/7). Nếu Alphabet đã kết thúc tranh luận về cầu, thì hai công ty này sẽ phân định tranh luận về biên lợi nhuận và FCF.
- Việc tốc độ tăng trưởng Cloud có duy trì trên 50% trong 2-4 quý tới hay không, và biên lợi nhuận có trụ trên 30% hay không, là chỉ báo xác nhận cho kịch bản thượng. Nếu sau khi hạn chế cung được nới lỏng mà tốc độ tăng trưởng tụt xuống dưới 30%, cần tính lại khả năng cầu bị ước tính quá mức.
- Cần theo dõi liệu backlog có tiếp tục tăng ròng sau khi ghi nhận doanh thu hay không. Tổ hợp backlog giảm hoặc chỉ có thời hạn hợp đồng kéo dài tăng lên là tín hiệu chất lượng hợp đồng suy giảm.
- Quý mà tốc độ tăng OCF theo cơ sở 12 tháng vượt qua tốc độ tăng CAPEX chính là điểm khởi đầu của đảo chiều FCF. Ngược lại, nếu CAPEX 2028 vượt 250 tỷ USD trong khi OCF không theo kịp, sẽ được phán định là tổn hại FCF mang tính cấu trúc.
- Việc có tiếp tục phát hành cổ phiếu hoặc huy động nợ quy mô lớn hay không, việc thuê ngoài kiểu SpaceX có thu hẹp trong giai đoạn 2027-2028 hay không, và việc bán ngoài TPU có dẫn đến tiêu dùng Cloud lặp lại hay không, là các hạng mục xác nhận phía hiệu quả vốn.
- Yếu tố phân định phía bộ nhớ không đổi. Đó là giá hợp đồng DRAM, và việc xác nhận giá hợp đồng quý 3 trong các cuộc gọi của Samsung Electronics và SK Hynix quanh ngày 30/7.

---

Các cổ phiếu được nhắc đến trong bài là ví dụ minh họa cho phân tích, không phải khuyến nghị mua hay bán một cổ phiếu cụ thể nào. Trách nhiệm đối với quyết định đầu tư và kết quả của nó thuộc về nhà đầu tư. Alphabet chưa đưa ra hướng dẫn CAPEX năm 2028 và doanh thu Cloud; tỷ trọng theo khách hàng, số tiền ghi nhận theo năm và điều kiện hủy của backlog 514 tỷ USD chưa được công bố; khối lượng mua cùng tỷ trọng theo nhà cung cấp của HBM, DRAM, NAND cũng không thuộc diện công bố. Độ nhạy FCF năm 2028 và phần số học CAPEX nửa cuối năm là ước tính riêng lấy công bố hiện tại làm điểm xuất phát, không phải dự báo của công ty. Quy mô trước thuế của lãi đánh giá lại cổ phần chưa niêm yết và tác động sau thuế trên mỗi cổ phiếu có thể có chênh lệch làm tròn do được tính lại từ công bố gốc. Mục tiêu giá 430 USD là tính toán của một trong hai ghi chú nguồn được tổng hợp, không phải mục tiêu giá của blog này. Giá cổ phiếu và diễn biến thị trường được tính đến sáng ngày 23/7/2026 theo giờ Hàn Quốc (KST).

### Bài viết liên quan

- [Ai đốt hết số token đó? Bản đồ khách hàng NVIDIA, AI chủ quyền và 9 triệu người dùng Codex bắt đầu trả lời](/vi/post/who-burns-the-tokens-nvidia-sovereign-codex-2026-07-19/)
- [Nhu cầu bộ nhớ AI có vượt kỳ vọng không? Đọc xác suất tăng trưởng vượt trội qua kịch bản cầu và bản đồ cung](/vi/post/ai-memory-demand-exceed-expectations-supply-map-2026-07-18/)
- [Hai tháng phát ngôn của Chủ tịch SK Hynix Chey Tae-won: công ty mạnh lên, đỉnh biên lợi nhuận đã qua](/vi/post/chey-tae-won-mental-model-sk-hynix-q-margin-signal-2026-07-19/)
- [Tranh luận thực sự trong ngành bán dẫn: bốn chiếc đồng hồ vật lý và một chiếc đồng hồ giá cổ phiếu](/vi/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/)
