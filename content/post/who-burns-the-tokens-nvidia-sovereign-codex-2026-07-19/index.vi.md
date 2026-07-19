---
title: "Ai đốt hết số token đó? Bản đồ khách hàng NVIDIA, AI chủ quyền và 9 triệu người dùng Codex bắt đầu trả lời"
slug: "who-burns-the-tokens-nvidia-sovereign-codex-2026-07-19"
date: 2026-07-19T19:00:00+09:00
description: "Câu hỏi dai dẳng nhất trong tranh luận CAPEX AI là ai sẽ thực sự dùng hết hạ tầng đó. Trên sổ sách NVIDIA, doanh thu ngoài hyperscale đã đạt điểm cân bằng với hyperscale và tốc độ tăng trưởng theo quý đã đảo chiều. Doanh thu AI chủ quyền tăng gấp ba trong một năm, nhóm bán dẫn Meritz phản bác góc nhìn hẹp của thị trường bằng thị trường DRAM máy chủ đang căng trở lại, và Codex thêm ba triệu người dùng trong ba ngày. Chúng tôi kiểm chứng chéo bằng chứng phía cầu và ý nghĩa cho kịch bản 45/35/20."
categories: ["Exclusive Analysis", "Market-Outlook", "Tech-Analysis"]
tags: ["NVIDIA", "AI chủ quyền", "Codex", "Bộ nhớ AI", "DRAM máy chủ", "HBM", "Samsung Electronics", "SK Hynix", "CAPEX AI", "AI tác tử", "Research OS"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Bối cảnh: Bài viết trước [Nhu cầu bộ nhớ AI có vượt kỳ vọng không?](/vi/post/ai-memory-demand-exceed-expectations-supply-map-2026-07-18/) đã xác suất hóa cầu thành kịch bản cơ sở 45%, vượt trội 35%, dưới kỳ vọng 20%, còn [Hai tháng phát ngôn của Chủ tịch SK Hynix Chey Tae-won](/vi/post/chey-tae-won-mental-model-sk-hynix-q-margin-signal-2026-07-19/) đã đọc lời nói và hành động của người đứng đầu cao nhất bên cung. Mắt xích yếu còn lại là cầu cuối cùng. GPU và HBM được lắp đặt nhiều đến vậy, thì rốt cuộc ai sẽ đốt hết số token đó? Bài viết này ghi lại một tuần mà câu hỏi đó bắt đầu có con số đi kèm.

## TL;DR

- Tỷ trọng hyperscale trong doanh thu trung tâm dữ liệu của NVIDIA vẫn quanh mức 50% suốt bảy quý liên tiếp. Tỷ trọng chưa sụp đổ. Điều thay đổi là cơ cấu. Trong quý 2-4/2026, <strong>doanh thu ngoài hyperscale (ACIE) đạt 37 tỷ USD, gần như cân bằng với 38 tỷ USD của hyperscale</strong>, còn tốc độ tăng trưởng theo quý đã đảo chiều thành 31% so với 12%. Ở lần công bố tiếp theo, chính tỷ trọng có thể đảo chiều lần đầu tiên.
- Cùng giai đoạn đó, tốc độ tăng trưởng doanh thu trung tâm dữ liệu so với cùng kỳ năm trước đã tái tăng tốc từ +56% lên +66%, +75%, rồi +92%. Tỷ trọng được giữ nguyên trong khi toàn bộ tốc độ lại nhanh lên có nghĩa là <strong>phần tăng trưởng gia tăng đang được dẫn dắt bởi nhóm khách hàng ngoài hyperscale</strong>. Chính NVIDIA đã ghi trong tài liệu công bố rằng tăng trưởng do nhóm khách hàng còn lại dẫn dắt.
- Doanh thu AI chủ quyền trong cả năm tài chính 2026 vượt 30 tỷ USD, gấp ba lần năm trước, và ở quý gần nhất cũng tăng hơn 80% so với cùng kỳ. Đây là nhóm khách hàng mà thị trường đã bỏ lỡ vì chỉ nhìn vào miệng của các hyperscaler.
- Nhóm bán dẫn của Meritz Securities trong báo cáo công bố Chủ nhật đã chỉ ra việc mua sắm chủ quyền đang bước vào giai đoạn thực chất và tình trạng thiếu cung DRAM máy chủ tái diễn nghiêm trọng từ giữa tháng 7. Dự báo giá hợp đồng DRAM máy chủ quý 3 tăng +13-18% của TrendForce, lời chứng thực về thời gian giao hàng hơn 40 tuần của Inventec (Đài Loan), và phát biểu của Micron rằng chỉ đáp ứng được 50-66% nhu cầu của khách hàng chính, đều xác nhận chéo điều này từ bên ngoài.
- Ở phía cầu cuối cùng cũng đã có con số. Codex của OpenAI tăng từ 1 triệu vào tháng 2 lên 5 triệu vào cuối tháng 5, rồi từ 6 triệu vào ngày 12/7 (ngay sau khi GPT-5.6 ra mắt) lên 9 triệu vào khoảng ngày 15/7, tức <strong>thêm 3 triệu người dùng chỉ trong ba ngày</strong>. Đây là giai đoạn đơn vị đo cầu chuyển từ số người dùng đăng ký sang thời gian thực thi của agent.
- Kết luận không phải là vội vàng nâng xác suất. Trước khi bàn đến dư cung, đây là lúc cần kiểm chứng lại xem <strong>liệu chúng ta có đang vẽ đường cầu quá thận trọng hay không</strong>, và phán định đó sẽ do mùa báo cáo kết quả kinh doanh quanh ngày 30/7 và công bố của NVIDIA cuối tháng 8 đưa ra.

<div class="thesis-callout">
<div class="thesis-callout__label">Luận điểm chính</div>

Thị trường đã nghi ngờ tính bền vững của CAPEX AI trong khi chỉ nhìn vào miệng của bốn Big Tech. Trong lúc đó, trên sổ sách của NVIDIA, doanh thu ngoài hyperscale đã đạt điểm cân bằng với hyperscale, doanh thu chủ quyền tăng gấp ba trong một năm, và Codex thêm 3 triệu người dùng chỉ trong ba ngày. Trong khi giá cổ phiếu phản ánh trước nỗi sợ dư cung, thì nền tảng cầu lại đang tích lũy bằng chứng thực đo theo chiều ngược lại. Sự bất đối xứng này chính là bản chất của đợt điều chỉnh lần này.

</div>

## 1. Một tuần như thế nào: giữa giá sàn và báo cáo

Trước tiên, hãy xác nhận bối cảnh sân khấu. Vào thứ Năm ngày 16/7, thị trường Mỹ chứng kiến chỉ số bán dẫn Philadelphia (SOX) lao dốc khoảng 4%, rơi vào vùng thị trường giá xuống (bear market) hơn 20% so với đỉnh, còn Nasdaq giảm 1,47%. Sang thứ Sáu ngày 17/7, Nasdaq giảm thêm 1,40%, khiến mức giảm trong tuần lên tới 2,90%. [Thực tế: dữ liệu thị trường] Cùng ngày tại Tokyo, cổ phiếu Kioxia chạm giá sàn ngay sau khi mở cửa, lao dốc 16,1%. Giá cổ phiếu đã xuống dưới một nửa so với đỉnh ngày 22/6, và khoảng 30 nghìn tỷ JPY vốn hóa thị trường đã bốc hơi. Nguyên nhân trực tiếp là phán quyết bồi thường bằng sáng chế khoảng 229 triệu USD cho Viasat mà bồi thẩm đoàn Mỹ đã công nhận, nhưng bản chất là làn sóng giảm đòn bẩy (deleveraging) trên toàn bộ đà tăng AI, thể hiện qua việc TSMC -7,29%, ADR SK Hynix -13,69%, và SanDisk -12,63% cùng lao dốc trong phiên đó. [Thực tế: báo Nikkei, Hankyung]

Thị trường Hàn Quốc đã tránh được ngày thứ Sáu này, vì 17/7 là ngày nghỉ lễ Chế Hiến (Jeheonjeol), được tái chỉ định thành ngày nghỉ lần đầu tiên sau 18 năm. Nhưng ngay trước đó, thị trường đã trải qua các đợt lao dốc mạnh: ngày 13/7 SK Hynix -15,37%, Samsung Electronics -10,70%, và ngày 16/7 SK Hynix -12,34%, Samsung Electronics -9,47%. [Thực tế: dữ liệu sàn giao dịch] Câu chuyện mà thị trường đang đưa vào giá là rõ ràng. Nguồn cung đang tăng, Trung Quốc đang đuổi kịp, lợi nhuận năm 2027 đang bị hạ dự báo, và không ai biết khi nào CAPEX của Big Tech sẽ hạ nhiệt.

Trong bối cảnh này, vào Chủ nhật, các báo cáo của các nhà phân tích Kim Sun-woo, Yang Seung-su và Kim Dong-kwan thuộc nhóm bán dẫn Meritz Securities đã lần lượt được công bố. Thời điểm phát hành cho thấy rõ họ ý thức trực diện về đợt lao dốc ngày thứ Sáu và sự cố Kioxia. Nội dung cốt lõi đi theo hướng ngược lại. Hiện tại nhu cầu bộ nhớ không chỉ đến từ các hyperscaler, việc mua sắm của khối chủ quyền bao gồm cả Trung Đông đang bước vào giai đoạn thực chất, và tình trạng thiếu cung DRAM máy chủ đang tái diễn nghiêm trọng từ giữa tháng 7. Đây là sự phản bác nhắm vào góc nhìn coi việc nới lỏng thiếu hụt năm 2028 là điều hiển nhiên mà không tính đến nhu cầu này. [Thực tế: tóm tắt báo cáo Meritz Securities, 19/7/2026]

Thay vì để đây là một cuộc tranh cãi bằng lời, chúng tôi tách lập luận này thành ba mảnh có thể kiểm chứng và đối chiếu từng phần với bằng chứng thực đo: cơ cấu khách hàng của NVIDIA, hoạt động mua sắm của khối chủ quyền, và mức sử dụng cuối cùng.

## 2. Bản đồ khách hàng NVIDIA: tỷ trọng vẫn 50%, tăng trưởng đến từ bên ngoài

Trước tiên, hãy xác nhận chính xác mệnh đề cho rằng tỷ trọng của các hyperscaler đang thu nhỏ lại. Khi đặt các câu công bố theo từng quý của NVIDIA theo chuỗi thời gian, bức tranh như sau.

| Quý tài chính | Giai đoạn | Doanh thu DC | So với cùng kỳ | Tỷ trọng CSP lớn/hyperscale (theo công bố) |
|---|---|---|---|---|
| FY25 Q3 | 8-10/2024 | 30,77 tỷ USD | +112% | khoảng 50% |
| FY25 Q4 | 11/2024-1/2025 | 35,58 tỷ USD | +93% | khoảng 50% |
| FY26 Q1 | 2-4/2025 | 39,11 tỷ USD | +73% | hơi dưới 50% |
| FY26 Q2 | 5-7/2025 | 41,10 tỷ USD | +56% | khoảng 50% |
| FY26 Q3 | 8-10/2025 | 51,22 tỷ USD | +66% | không công bố |
| FY26 Q4 | 11/2025-1/2026 | 62,31 tỷ USD | +75% | hơi trên 50%, tăng trưởng do nhóm khách hàng còn lại dẫn dắt |
| FY27 Q1 | 2-4/2026 | 75,2 tỷ USD | +92% | Hyperscale 38 tỷ USD (khoảng 50%) so với ACIE 37 tỷ USD |

[Thực tế: bình luận CFO NVIDIA, hội nghị kết quả kinh doanh]

Hai điều hiện ra cùng lúc. Thứ nhất, <strong>bản thân con số tỷ trọng chưa từng rời khỏi dải 50% suốt bảy quý liên tiếp</strong>. Câu chuyện cho rằng các hyperscaler đã bị đẩy lùi không phải là bằng chứng thực đo. Thứ hai, dù vậy hướng đi của cơ cấu đã thay đổi rõ rệt. Công bố FY26 Q4 nêu rõ tăng trưởng do nhóm khách hàng còn lại dẫn dắt và doanh thu đã đa dạng hóa, còn từ FY27 Q1, NVIDIA bắt đầu công bố trung tâm dữ liệu tách thành hyperscale và ACIE (AI cloud, công nghiệp, doanh nghiệp). Ngay trong quý đầu tiên đó, ACIE đạt 37 tỷ USD, gần bám sát 38 tỷ USD của hyperscale, còn tốc độ tăng trưởng theo quý đã đảo chiều thành <strong>ACIE +31% so với hyperscale +12%</strong>. Doanh thu AI cloud bên trong ACIE đã vượt gấp ba lần so với cùng kỳ năm trước. CEO Jensen Huang khẳng định trong hội nghị rằng về dài hạn, nhóm thứ hai này sẽ tăng trưởng nhanh hơn. [Thực tế: hội nghị kết quả kinh doanh]

Chồng thêm sự tái tăng tốc của tốc độ tăng trưởng lên đây thì bức tranh sẽ hoàn chỉnh. Tốc độ tăng trưởng doanh thu trung tâm dữ liệu so với cùng kỳ đã chạm đáy ở mức +56% tại FY26 Q2, rồi leo trở lại lên +66%, +75%, và +92%. Việc tỷ trọng được giữ nguyên trong khi toàn bộ tốc độ tăng trưởng lại nhanh lên, về mặt số học có nghĩa là <strong>hơn một nửa phần tăng trưởng gia tăng đang được tạo ra bởi nhóm ngoài hyperscale</strong>. [Suy luận: tính toán số học từ công bố] Chỉ cần xu hướng này tiếp diễn thêm một quý nữa, công bố FY27 Q2 vào cuối tháng 8 sẽ ghi nhận con số ACIE vượt qua hyperscale lần đầu tiên. Kể từ khoảnh khắc đó, chính khung phán đoán tính bền vững của nhu cầu AI chỉ bằng cách nhìn vào hướng dẫn CAPEX của bốn Big Tech sẽ trở nên lỗi thời.

Cần làm rõ một điểm dễ nhầm lẫn. Độ tập trung khách hàng trực tiếp trong báo cáo 10-Q (khách hàng A 22%, khách hàng B 14%) thực ra lại tăng lên, nhưng đây là chỉ số ở tầng phân phối tổng hợp các đối tác bo mạch, OEM và các đơn mua trực tiếp quy mô lớn, nên thuộc một tầng khác với sự đa dạng hóa của người dùng cuối. [Thực tế: 10-K] Hai hiện tượng, phân phối tập trung và cầu cuối cùng mở rộng, cùng tồn tại song song.

## 3. AI chủ quyền: nhóm khách hàng mà thị trường bỏ lỡ vì chỉ nhìn vào miệng

Khối lượng lớn nhất trong nhu cầu ngoài hyperscale chính là khối chủ quyền. CFO của NVIDIA cho biết doanh thu AI chủ quyền trong FY2026 đã <strong>vượt mốc 30 tỷ USD</strong>, hơn gấp ba lần năm trước. Canada, Pháp, Hà Lan, Singapore và Anh dẫn đầu, còn ở FY27 Q1 doanh thu chủ quyền cũng tăng hơn 80% so với cùng kỳ, và hạ tầng của NVIDIA hiện đã được lắp đặt tại khoảng 40 quốc gia với tổng GDP lên tới 50 nghìn tỷ USD. [Thực tế: hội nghị kết quả kinh doanh NVIDIA]

Thực thể vật lý cũng đã hình thành. HUMAIN của Ả Rập Saudi đã chốt kế hoạch triển khai tối đa 600.000 GPU NVIDIA trong 3 năm, và đã nhận lô hàng đầu 18.000 GB300. Stargate UAE của UAE đang xây dựng giai đoạn 1 công suất 200MW của cụm 1GW, với mục tiêu vận hành trong quý 3 năm nay, riêng giai đoạn 1 sẽ có tối đa 35.000 GB300, còn đơn vị vận hành G42 đã nhận được giấy phép xuất khẩu của Mỹ vào giữa tháng 7. EU đang triển khai chương trình AI Gigafactory trị giá 20 tỷ EUR, Ấn Độ đặt mục tiêu 100.000 GPU công cộng vào cuối năm, còn SoftBank của Nhật Bản đặt mục tiêu thương mại hóa dịch vụ đám mây GPU chủ quyền vào tháng 10. [Thực tế: công bố của từng công ty, từng quốc gia]

Điều này kết nối với bộ nhớ như thế nào? Đã có hai con đường được công khai. Chương trình Stargate toàn cầu của OpenAI đã ký kết thư ý định (LOI) với Samsung Electronics và SK Hynix vào tháng 10/2025, với quy mô <strong>tối đa 900.000 wafer DRAM mỗi tháng</strong>, tương đương khoảng 40% năng lực sản xuất DRAM toàn cầu. Giới hạn của việc đây chỉ là thư ý định không có tính ràng buộc vẫn còn nguyên. [Thực tế: báo chí, LOI] Và SK Hynix vào tháng 6 năm nay đã chính thức hóa quan hệ đối tác HBM4 nhiều năm với NVIDIA, kéo dài xuyên suốt thế hệ Vera Rubin kế tiếp. [Thực tế: công bố của NVIDIA] Ở phía các quỹ đầu tư quốc gia, liên tục có các báo cáo về sự hợp tác giữa nguồn vốn UAE (Mubadala, MGX, G42, Kazna) và phía SK Hynix.

Cũng có một khoảng trống cần để lại một cách trung thực. Không có công bố mới nào trong tháng 6-7 xác nhận việc chủ thể chủ quyền trực tiếp mua khối lượng lớn DRAM từ Samsung Electronics hay SK Hynix. [Chưa xác minh: hợp đồng trực tiếp chưa công bố] Vì nhu cầu bộ nhớ của khối chủ quyền đi qua các OEM máy chủ và nhà cung cấp hệ thống, nên trong công bố khách hàng của các hãng bộ nhớ, nó bị trộn lẫn với hyperscaler. [Suy luận: cấu trúc phân phối] Không nhìn thấy khác với không tồn tại. Vì không có kịch bản nào mà 600.000 GPU đã được xác định lại không đi kèm bộ nhớ, nên vấn đề không nằm ở việc có tồn tại hay không, mà ở mức độ hiển thị trong công bố về quy mô và thời điểm.

## 4. DRAM máy chủ căng trở lại: lập luận của Meritz và bằng chứng thực đo bên ngoài

Tình trạng thiếu cung DRAM máy chủ tái diễn nghiêm trọng từ giữa tháng 7 mà nhóm Meritz chỉ ra không phải là lập luận đơn phương của riêng công ty chứng khoán này. Bốn bằng chứng thực đo từ bên ngoài đều chỉ cùng một hướng.

| Bằng chứng thực đo | Nội dung | Nguồn, thời điểm |
|---|---|---|
| Dự báo giá hợp đồng | Giá hợp đồng DRAM máy chủ quý 3 dự báo tăng +13-18%. Không thể tăng đối với CSP Mỹ bị ràng buộc bởi hợp đồng dài hạn (LTA), nên mức tăng tập trung vào khách hàng phi-LTA | TrendForce, 9/7 |
| Tốc độ tăng cung | Tốc độ tăng cung bit RDIMM ở mức 15-20%/năm, không theo kịp tốc độ tăng xuất xưởng CPU. CSP tích trữ tồn kho trước vì dự đoán thiếu hụt năm 2027. Module dịch chuyển xuống từ 96/128GB về 32/64GB | TrendForce, 9/7 |
| Thời gian giao hàng | Thời gian giao hàng DRAM máy chủ vượt 40 tuần, giá tăng khoảng 90% so với cuối năm 2025, thời hạn hiệu lực báo giá rút ngắn còn 1-30 ngày | Phát biểu của Inventec, 16/7 |
| Lời chứng thực nhà cung cấp | Chỉ có thể đáp ứng 50-66% nhu cầu của khách hàng chính, HBM đã bán hết đến hết năm 2027, tình trạng thiếu cung kéo dài đến sau năm 2027 | Hội nghị kết quả kinh doanh Micron, tháng 7 |

[Thực tế: từng nguồn]

Mức giá tuyệt đối cũng đã phát ra tín hiệu bất thường. Giá giao dịch cố định của DRAM PC phổ thông (DDR4 8Gb) đạt 21 USD vào tháng 6, mức cao kỷ lục kể từ khi bắt đầu thống kê, còn giá giao ngay cao hơn giá cố định tới 72%. Cũng có báo cáo cho biết Samsung Electronics đã thông báo cho khách hàng Trung Quốc rằng sẽ tăng giá DRAM tối đa 20% trong quý 3. [Thực tế: báo chí ngành] Trong giai đoạn giá hợp đồng đang tăng, sự kết hợp mức phí bảo hiểm giao ngay vượt 70% cho thấy có nhu cầu thực sự tồn tại bên ngoài kênh hợp đồng, sẵn sàng trả giá cao để có ngay hàng gấp. Không phải các hyperscaler bị ràng buộc bởi LTA, mà chính nhóm bên ngoài đó, tức khối chủ quyền, doanh nghiệp và đám mây hạng hai, mới là bên trả mức giá đắt đỏ. Câu nói của TrendForce rằng mức tăng tập trung vào khách hàng phi-LTA và câu nói của Meritz rằng việc mua sắm chủ quyền đang bước vào giai đoạn thực chất là hai cách diễn đạt của cùng một hiện tượng. [Suy luận: diễn giải chéo]

Nhà phân tích Kim Sun-woo tiến thêm một bước nữa ở đây. Ông cho rằng thị trường đang bị mắc kẹt trong khung nhìn hẹp về hợp đồng dài hạn mang tính hy sinh và việc hạ dự báo lợi nhuận năm 2027, dẫn đến hiểu lầm, và dự báo rằng sự hiểu lầm này sẽ nhanh chóng được xóa bỏ khi các sự kiện như thực hiện sớm việc hoàn trả cổ đông và các quan hệ đối tác bao gồm đầu tư cổ phần từ Big Tech lần lượt diễn ra. [Thực tế: lập luận trong báo cáo] Đây không phải là sự thật đã được kiểm chứng mà là dự báo của công ty chứng khoán, nên tiêu chí chấm điểm là liệu nó có được xác nhận bằng các sự kiện thực tế trong mùa báo cáo kết quả kinh doanh tuần này hay không. Tuy nhiên, hướng đi này nhất quán với động thái huy động vốn niêm yết Nasdaq và các quan hệ đối tác của Chủ tịch SK Hynix Chey Tae-won đã đề cập trong bài viết trước, cũng như hợp đồng nhiều năm giữa SK Hynix và NVIDIA.

## 5. Codex 9 triệu: những con số về cầu cuối cùng bắt đầu xuất hiện

Điểm bị công kích nhiều nhất trong tranh luận CAPEX AI không phải là hạ tầng, mà là phần cuối của nó. Bằng chứng cho thấy mức sử dụng cuối cùng đang tăng tương xứng với tốc độ xây dựng trung tâm dữ liệu vẫn còn yếu. Ở mắt xích yếu này, những con số đáng chú ý đã bắt đầu xuất hiện.

| Thời điểm | Số người dùng | Ghi chú |
|---|---|---|
| Tháng 2/2026 | 1 triệu | Người dùng hoạt động riêng của Codex |
| 8/4 | 3 triệu | Hoạt động hàng tuần, tuyên bố đặt lại giới hạn sử dụng mỗi mốc 1 triệu người |
| 21/4 | 4 triệu | Thêm 1 triệu chỉ trong 2 tuần |
| Cuối tháng 5 - đầu tháng 6 | Vượt 5 triệu | Gấp 6 lần so với tháng 2 |
| 9/7 | GPT-5.6 ra mắt chính thức | 3 phiên bản Sol, Terra, Luna; Codex tích hợp với ChatGPT desktop |
| 12/7 | 6 triệu | Từ đây chỉ số là gộp Codex + ChatGPT Work |
| Khoảng 15/7 | 9 triệu | Tăng 3 triệu chỉ trong ba ngày |

[Thực tế: phát biểu công khai của ban lãnh đạo OpenAI, báo chí]

Cần nêu hai lưu ý để đảm bảo công bằng. Con số sau ngày 9/7 không còn là riêng Codex mà là chỉ số gộp với ChatGPT Work, nên khó so sánh liên tục một cách nghiêm ngặt với giai đoạn trước đó. Và theo ngoại suy bên ngoài dựa trên việc kéo dài nguyên tốc độ tăng trưởng cuối tháng 5, thời điểm đạt 10 triệu người dùng được tính là tháng 10, nhưng thực tế đã đạt 9 triệu vào giữa tháng 7. Cũng cần nói rõ đường ngoại suy này không phải là dự báo chính thức của OpenAI. [Thực tế: xác minh nguồn ngoại suy] Ngay cả khi tính đến việc thay đổi định nghĩa chỉ số, sự thật vẫn còn đó là một cú tăng tốc rút ngắn đường dự kiến khoảng ba tháng đã được thực đo chỉ trong ba ngày ngay sau khi GPT-5.6 ra mắt.

Lý do Codex quan trọng không phải là độ lớn của con số mà là bản chất của cầu. Codex là sản phẩm chuyển đổi thời gian làm việc của con người thành thời gian suy luận. Con người không cần kết nối lâu hơn nhưng agent vẫn có thể làm việc lâu hơn, và khi một người chạy song song nhiều tác vụ, <strong>khối lượng công việc tăng nhanh hơn số người dùng</strong>. Từ giai đoạn này, đơn vị đo cầu không còn là số người dùng hoạt động hàng tháng mà là tổng thời gian thực thi của agent. Đây chính xác là cấu trúc giống với việc bài viết trước đã viết lại giới hạn trên của mô hình cầu bộ nhớ AI thành số khối lượng công việc nhân với bộ nhớ trên mỗi khối lượng công việc nhân với tần suất thực thi.

Cuộc tranh luận về hiệu quả cũng bị đảo ngược ở đây. Chính OpenAI cho biết GPT-5.6 Sol cải thiện hiệu quả token hơn 54% so với thế hệ trước. Việc người dùng và mức sử dụng bùng nổ ngay sau khi mô hình có chi phí trên mỗi token thấp hơn ra mắt là một trường hợp thực đo của giả thuyết Jevons, trong đó ở lĩnh vực agent lập trình, cải thiện hiệu quả không làm giảm nhu cầu tính toán mà <strong>mở rộng phạm vi công việc có thể giao cho AI</strong>. [Suy luận: hiệu ứng Jevons] Điều cần nhìn không phải là tốc độ giảm giá token, mà là khối lượng công việc mà việc giảm giá đó vừa mở ra.

## 6. Vậy điều này chuyển hóa thành gì cho bộ nhớ

Cũng cần sự tiết chế. Không thể giải thích toàn bộ chu kỳ bộ nhớ chỉ bằng một con số 9 triệu người dùng Codex. Để số người dùng chuyển hóa thành nhu cầu bit bộ nhớ, nó phải đi qua bốn hệ số chuyển đổi: khối lượng thực thi đồng thời, độ dài ngữ cảnh, dung lượng bộ nhớ trang bị trên mỗi bộ tăng tốc, và tốc độ tăng cung. [Suy luận: mô hình cầu] Chỉ cần một trong số này yếu đi, chỉ số gây chú ý và cầu thực sự sẽ tách rời nhau.

Tuy nhiên, khi đối chiếu các biến số tăng đã dựng lên làm luận cứ cho kịch bản vượt trội 35% trong bài viết kịch bản cầu trước đó với bằng chứng thực đo tuần này, có thể thấy chúng thẳng hàng với nhau.

- Sự mở rộng nền tảng cầu bộ tăng tốc đã có bằng chứng thực đo qua việc đảo chiều tốc độ tăng trưởng ACIE và doanh thu chủ quyền tăng gấp ba.
- Suy luận thường trực của agent đã có con số đầu tiên qua mức tăng 3 triệu trong ba ngày của Codex và sự chuyển đổi đơn vị chỉ số.
- Sự lan tỏa ra ngoài HBM đã hiện diện trong giá qua dự báo giá hợp đồng DRAM máy chủ +13-18%, thời gian giao hàng 40 tuần, và mức phí bảo hiểm giao ngay 72%.
- Giả thuyết mức sử dụng thắng hiệu quả đã có bằng chứng thực đo phản trực giác là mức sử dụng bùng nổ ngay sau khi hiệu quả token cải thiện 54%.

Ý nghĩa đối với câu chuyện nới lỏng nguồn cung năm 2028 cũng phân nhánh từ đây. Công thức của phe nới lỏng phần lớn đặt việc tăng trưởng CAPEX của hyperscaler chững lại làm giới hạn trên cho tốc độ tăng trưởng cầu. Nhưng nếu một nửa cầu gia tăng bắt đầu đến từ bên ngoài nhóm đó, thì chính giả định về giới hạn trên này cần được tính toán lại. Đây chính xác là điểm mà sự phản bác của Meritz nhắm tới. Chúng tôi không thay đổi xác suất ngay lập tức. Chúng tôi giữ nguyên khung xác suất cơ sở 45%, vượt trội 35%, dưới kỳ vọng 20%, nhưng ghi nhận sự thật rằng luận cứ cho phía vượt trội đã bắt đầu có bằng chứng thực đo ở ba nhánh. Việc cập nhật xác suất sẽ được thực hiện khi bảng phán định dưới đây được lấp đầy. [Suy luận: vận hành kịch bản]

## 7. Kiểm tra phản biện

Luận cứ càng có vẻ mạnh, chúng tôi càng cần dựng lên phía đối lập.

- <strong>Chất lượng của cầu ngoài hyperscale.</strong> ACIE bao gồm cả neocloud. Đơn hàng của các đám mây hạng hai vốn dễ tổn thương về chi phí vốn là loại cầu bị hủy đầu tiên khi lãi suất và môi trường huy động vốn thắt chặt. Việc tốc độ tăng trưởng đảo chiều không đảm bảo cả độ bền của cầu.
- <strong>Biến động chính trị của khối chủ quyền.</strong> Các dự án cấp quốc gia bị lung lay bởi bầu cử, ngân sách và quy định xuất khẩu. Chương trình Gigafactory của EU đã hai lần bị lùi thời hạn gọi thầu, còn khối lượng ở Trung Đông phụ thuộc vào một công tắc duy nhất là giấy phép xuất khẩu của Mỹ.
- <strong>Bẫy chỉ số.</strong> Con số 9 triệu của Codex là con số ngay sau khi định nghĩa chỉ số thay đổi thành chỉ số gộp, và tiêu chí xác định trạng thái hoạt động cũng chưa được công bố. Hướng tăng trưởng là thực đo, nhưng độ lớn vẫn chưa tách khỏi yếu tố marketing.
- <strong>Sự tự hủy hoại của việc giá tăng vọt.</strong> Tình trạng DRAM máy chủ căng trở lại vừa là luận cứ tăng giá, vừa là rủi ro ăn mòn ngân sách CNTT như trường hợp của IBM, tạo ra khoảng trống cầu sau đợt mua trước. Chính Chủ tịch Chey đã cảnh báo về việc giá tăng quá nóng sẽ phá hủy nhu cầu.
- <strong>Phân biệt giữa dự báo và thực đo.</strong> Dự báo sự kiện của Meritz (thực hiện sớm việc hoàn trả cổ đông, quan hệ đối tác đầu tư cổ phần từ Big Tech) vẫn còn là dự báo. Nếu không thành hiện thực, góc nhìn hẹp của thị trường sẽ hóa ra là đúng.

## 8. Bảng phán định: điều gì sẽ chốt câu trả lời

- Liệu mức tăng giá hợp đồng quý 3 trong hội nghị kết quả kinh doanh của Samsung Electronics và SK Hynix quanh ngày 30/7 có xác nhận dải +13-18% của TrendForce hay không, và liệu có xuất hiện đề cập đến khách hàng phi-LTA cùng khối lượng chủ quyền hay không.
- Liệu việc thực hiện sớm hoàn trả cổ đông của SK Hynix và các quan hệ đối tác dạng đầu tư cổ phần có xuất hiện dưới dạng công bố thực tế hay không. Đây là hạng mục chấm điểm trực tiếp cho dự báo của Meritz.
- Liệu ACIE có vượt qua hyperscale lần đầu tiên trong công bố FY27 Q2 của NVIDIA vào cuối tháng 8 hay không. Nếu vượt qua, sự mở rộng nền tảng cầu sẽ không còn là câu chuyện mà trở thành con số công bố chính thức.
- Liệu hợp đồng bộ nhớ trực tiếp từ khối chủ quyền hoặc các đơn hàng lớn qua OEM máy chủ có được nâng lên cấp độ công bố hay không. Việc thư ý định Stargate có chuyển đổi thành hợp đồng có tính ràng buộc hay không là ứng viên đầu tiên.
- Liệu chỉ số sử dụng của Codex và các agent cạnh tranh có bắt đầu được công bố theo tiêu chí thời gian thực thi cùng với việc vượt mốc 10 triệu hay không.

Yếu tố phán định vẫn không đổi. Nếu giá hợp đồng DRAM quay đầu giảm, toàn bộ câu chuyện cầu này sẽ bị thị trường bác bỏ; nếu giá được duy trì, đường cầu vốn được vẽ quá thận trọng sẽ phải được vẽ lại.

---

Các cổ phiếu được đề cập trong bài là ví dụ minh họa cho phân tích, không phải khuyến nghị mua hay bán cổ phiếu cụ thể. Trách nhiệm đối với quyết định đầu tư và kết quả của nó thuộc về nhà đầu tư. Báo cáo của Meritz Securities được trích dẫn sau khi tái cấu trúc lại nội dung cốt lõi, trách nhiệm về số liệu chi tiết và dự báo trong văn bản gốc thuộc về công ty chứng khoán đó. Số người dùng Codex đã đổi định nghĩa thành chỉ số gộp với ChatGPT Work kể từ sau ngày 9/7 nên khó so sánh nghiêm ngặt với giai đoạn trước đó, và đường ngoại suy đạt 10 triệu vào tháng 10 không phải là dự báo chính thức của OpenAI. Việc mua trực tiếp bộ nhớ của các chủ thể chủ quyền chưa được xác nhận qua công bố, và khối lượng liên quan đến Stargate vẫn đang ở giai đoạn thư ý định không có tính ràng buộc. Dữ liệu giá cổ phiếu, chỉ số và giá cả dựa trên tài liệu công khai tính đến ngày 17/7/2026 và chưa phản ánh biến động sau thời điểm đó.

### Bài viết liên quan

- [Nhu cầu bộ nhớ AI có vượt kỳ vọng không? Đọc xác suất tăng trưởng vượt trội qua kịch bản cầu và bản đồ cung](/vi/post/ai-memory-demand-exceed-expectations-supply-map-2026-07-18/)
- [Hai tháng phát ngôn của Chủ tịch SK Hynix Chey Tae-won: công ty mạnh lên, đỉnh biên lợi nhuận đã qua](/vi/post/chey-tae-won-mental-model-sk-hynix-q-margin-signal-2026-07-19/)
- [Tranh luận thực sự trong ngành bán dẫn: bốn chiếc đồng hồ vật lý và một chiếc đồng hồ giá cổ phiếu](/vi/post/semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17/)
- [Bán dẫn có mang tính chu kỳ không và giá hợp lý là bao nhiêu? Định giá Samsung, SK Hynix và Micron bằng FCFE và lợi nhuận chuẩn hóa](/vi/post/memory-fair-value-fcfe-terminal-samsung-hynix-micron-2026-07-17/)
