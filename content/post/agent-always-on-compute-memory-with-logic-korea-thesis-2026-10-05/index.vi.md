---
title: "Tính toán tiết kiệm, ký ức tích lũy: Vì sao bộ nhớ Hàn Quốc tích hợp logic trong kỷ nguyên tác nhân"
date: 2026-10-05T22:20:00+09:00
categories: ["Exclusive Analysis", "AI Infrastructure", "Korean-Equities"]
tags: ["Bộ nhớ", "Samsung Electronics", "SK hynix", "HBM", "HBM tùy chỉnh", "tác nhân", "KV cache", "SSD doanh nghiệp", "HBF", "CXL", "hợp đồng cung ứng dài hạn"]
slug: "agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05"
description: "Khi ngày càng nhiều tác nhân AI được giao trọn vẹn công việc, chi phí tính toán giảm còn ngữ cảnh và tri thức tích lũy. Bài viết tính toán luận điểm đầu tư vào bộ nhớ Hàn Quốc và mức độ duy trì lợi nhuận mà giá cổ phiếu hiện tại đòi hỏi, dựa trên sự phân hóa giữa xử lý theo lô và thời gian thực, nhu cầu CPU và mạng, HBM và SSD tích hợp logic, cùng hợp đồng dài hạn và tiền đặt cọc."
image: "cover.png"
draft: false
---

Ngay cả khi gửi cùng một câu hỏi cho cùng một mô hình AI, giá vẫn chênh lệch đáng kể tùy cách xử lý. Theo bảng giá của Anthropic, với Opus 5.5, xử lý theo lô có thể trả lời trong vòng một ngày có giá bằng một nửa mức niêm yết, còn chế độ tốc độ cao bảo đảm phản hồi nhanh có giá gấp đôi. Chi phí đọc lại ngữ cảnh đã đọc chỉ bằng một phần hai mươi mức niêm yết.[^anthropic-pricing]

Bảng giá này tóm lược hướng đi của hạ tầng AI. Việc không gấp được xử lý rẻ, việc cần gấp được xử lý đắt. Và thứ rẻ nhất không phải là tính toán mới, mà là lấy ra dùng lại những gì đã ghi nhớ.

<strong>Càng có nhiều tác nhân được giao trọn vẹn công việc, tính toán càng hiệu quả còn ngữ cảnh và tri thức càng tích lũy. Bộ nhớ và thiết bị lưu trữ chứa những dữ liệu tích lũy ấy đang chuyển từ sản phẩm tiêu chuẩn sang sản phẩm tích hợp logic. Trọng tâm đầu tư vào bộ nhớ Hàn Quốc nằm ở thời gian lợi nhuận duy trì được, hơn là quy mô lợi nhuận năm nay.</strong>

Các mắt xích cần kiểm chứng nối tiếp nhau: hạ tầng có chuyển sang điện toán luôn hoạt động hay không, tính toán có thực sự hiệu quả hơn không, dữ liệu nào tích lũy, việc đưa logic vào bộ nhớ có thể hiện thành doanh thu hay không, và giá trị đó có ở lại với doanh nghiệp Hàn Quốc hay không. Cuối bài, chúng tôi tính mức độ duy trì lợi nhuận mà giá cổ phiếu hiện tại của Samsung Electronics và SK hynix đòi hỏi.

Ngày phân tích là ngày 5 tháng 10 năm 2026. Giá cổ phiếu là giá đóng cửa ngày 2 tháng 10; ngày 5 tháng 10 không có giao dịch trong phiên thường lệ tại Hàn Quốc. Bài viết phân biệt thông tin do công ty công bố, dự báo của tổ chức nghiên cứu và giả định tính toán của tác giả. Bảng độ nhạy dưới đây là phép tính để kiểm chứng, không phải giá mục tiêu.

<link rel="stylesheet" href="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/thesis.css">

## Hạ tầng chuyển từ thiết bị trả lời lời gọi sang thiết bị duy trì mục tiêu

Chatbot chỉ tính toán khi có câu hỏi. Tác nhân được ủy thác thì khác. Khi người dùng giao một mục tiêu, tác nhân lập kế hoạch, dùng công cụ, kiểm tra kết quả và thử lại nếu cần. Công việc vẫn tiếp diễn ngay cả khi người dùng đóng màn hình.

Vì vậy, đơn vị đo tải cũng thay đổi. Trong thời đại chatbot, tải gần với số người dùng truy cập đồng thời. Trong thời đại tác nhân, tải gần bằng số người dùng nhân với số mục tiêu mỗi người giao và thời gian các mục tiêu đó còn hoạt động. Đây là điện toán luôn hoạt động hướng mục tiêu.

Dấu hiệu đã xuất hiện trong sản phẩm và bảng giá. Managed Agents của Anthropic tính riêng 0.08 đô la mỗi giờ trong thời gian phiên còn hoạt động, ngoài phí token. Tài liệu giải thích phiên duy trì trạng thái nên không áp dụng chiết khấu xử lý theo lô.[^anthropic-pricing][^managed-agents]

Tại sự kiện dành cho nhà phát triển tháng 5 năm 2026, Google giới thiệu tác nhân cá nhân chạy cả ngày trên máy ảo chuyên dụng. Trong cùng bài trình bày, công ty cho biết tổng token xử lý hằng tháng tăng từ khoảng 480 trillion token vào tháng 5 năm 2025 lên hơn 3.2 quadrillion token vào tháng 5 năm 2026, tức tăng khoảng 7 lần trong một năm. Đây là số liệu công ty công bố; tỷ trọng của tác nhân không được công bố riêng.[^google-io]

Thời lượng công việc cũng tăng. Trong phép đo tháng 1 năm 2026 của METR, độ dài nhiệm vụ mà Claude Opus 4.5 có thể hoàn thành với xác suất 50% tương đương 320 phút theo chuẩn con người; kể từ năm 2024, độ dài này tăng gấp đôi khoảng mỗi 89 ngày. METR cũng thừa nhận giới hạn do phần đuôi phân phối của các nhóm nhiệm vụ còn thiếu chắc chắn.[^metr]

Hình dưới đây thể hiện chuỗi lập luận của toàn bài. Mỗi mũi tên là một mắt xích cần kiểm chứng, không phải một sự thật đã được xác lập.

<figure class="kii-figure"><img src="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/chain.svg" alt="Chuỗi lập luận từ tác nhân được ủy thác đến điện toán luôn hoạt động, nâng cao hiệu quả tính toán và tích lũy trạng thái, bộ nhớ tích hợp logic, rồi đến tính bền vững của lợi nhuận"><figcaption>Sơ đồ khái niệm. Nhu cầu tăng lên và giá trị ở lại với nhà sản xuất bộ nhớ là hai mắt xích khác nhau. Trên điện thoại, có thể cuộn ngang để xem.</figcaption></figure>

## Giá xử lý việc gấp và không gấp chênh nhau tới bốn lần

Không phải mọi công việc chạy liên tục đều cần xử lý gấp. Không có lý do để dùng cùng một thiết bị cho việc sắp xếp tài liệu qua đêm và câu trả lời mà người dùng đang chờ. Các công ty mô hình đã phản ánh khác biệt này vào giá.

| Công ty và mô hình | Theo lô hoặc tốc độ thấp | Tiêu chuẩn | Tốc độ cao hoặc ưu tiên | Đọc ngữ cảnh trong bộ nhớ đệm |
|---|---:|---:|---:|---:|
| Anthropic Opus 5.5 | 0.5 lần | 1 lần | 2 lần | 0.05 lần |
| OpenAI gpt-6-astra | 0.5 lần | 1 lần | 2 lần | 0.1 lần |
| Google Gemini 3.1 Pro Preview | 0.5 lần | 1 lần | 1.8 lần | Phí lưu trữ riêng |

Cả ba công ty đều phân biệt giá của cùng một mô hình theo tốc độ phản hồi. Chênh lệch giữa bậc rẻ nhất và đắt nhất là 3.6 đến 4 lần. Google cũng tính phí theo thời gian lưu ngữ cảnh trong bộ nhớ đệm. Điều đó cho thấy việc lưu giữ ngữ cảnh đã trở thành một sản phẩm riêng.[^anthropic-pricing][^openai-pricing][^google-pricing]

<figure class="kii-figure"><img src="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/pricing.svg" alt="Biểu đồ cột hệ số giá xử lý theo lô, tốc độ cao và đọc bộ nhớ đệm so với giá đầu vào tiêu chuẩn của Anthropic Opus 5.5"><figcaption>Theo bảng giá chính thức của Anthropic, tra cứu ngày 5 tháng 10 năm 2026. Hệ số được tính với giá đầu vào tiêu chuẩn bằng 1. Đọc bộ nhớ đệm là giá đầu vào khi dùng lại ngữ cảnh đã xử lý.</figcaption></figure>

Sự phân hóa này quan trọng với nhà đầu tư vì mức sử dụng thiết bị. Thiết bị chỉ phục vụ nhu cầu thời gian thực có mức hoạt động chênh lệch lớn giữa ngày và đêm. Nếu nhận việc không gấp với giá rẻ vào giờ thấp điểm, cùng một thiết bị có thể chạy cả ngày. Điện toán luôn hoạt động không chỉ tăng tổng cầu mà còn giảm thời gian thiết bị nhàn rỗi.

## Công việc lặp lại chuyển sang mô hình nhỏ và mã lệnh

Nếu tác nhân thực hiện cùng loại công việc hàng chục nghìn lần mỗi ngày, không cần gọi mô hình lớn nhất mỗi lần. Các tác vụ lặp lại được chuyển sang hai hướng: mô hình nhỏ chuyên làm việc đó hoặc mã lệnh chạy không cần mô hình.

Bằng chứng cho hướng mô hình nhỏ nằm trong bảng giá. Theo bảng giá OpenAI, đầu vào của gpt-6-astra là 10 đô la cho mỗi 1 triệu token, còn gpt-6-luna là 0.10 đô la. Chênh lệch 100 lần trong cùng một công ty. Các nhà nghiên cứu NVIDIA ước tính trong bài báo năm 2025 rằng có thể thay 40 đến 70% lời gọi tác nhân bằng mô hình nhỏ chuyên biệt. Đây là ước tính của bài báo, không phải tỷ trọng đo thực tế.[^openai-pricing][^nvidia-slm]

Bằng chứng cho hướng mã lệnh nằm trong tài liệu sản phẩm. Tài liệu Agent Skills của Anthropic cho biết các tập lệnh trong skill được chạy trong shell và chỉ kết quả mới được đưa vào ngữ cảnh của mô hình. Bản thân mã tập lệnh không được đưa vào ngữ cảnh. Cấu trúc này biến quy trình mà mô hình phải suy luận mỗi lần thành mã cố định một lần.[^agent-skills]

Công ty tự động hóa web Skyvern công bố kết quả chạy lại bằng mã một tác vụ mà tác nhân đã thực hiện trước đó, không cần mô hình. Thời gian chạy giảm từ 279 giây xuống 120 giây, còn chi phí mỗi lần giảm từ 0.11 đô la xuống 0.04 đô la. Đây là phép đo riêng do một công ty công bố.[^skyvern]

Ở đây có một điểm phân biệt quan trọng. Lượng tính toán cho mỗi công việc giảm. Nhưng mã đã cố định, trọng số của mô hình chuyên biệt và nhật ký thực thi vẫn phải được lưu ở đâu đó. Hiệu quả được cải thiện bằng cách dùng ít tính toán hơn nhưng dùng nhiều dữ liệu đã lưu hơn.

## GPU không thể tự mình hoàn thành công việc

Một tác vụ của tác nhân gồm nhiều giai đoạn. GPU đảm nhiệm giai đoạn suy nghĩ. CPU đảm nhiệm việc chạy công cụ, xử lý tệp và thực thi mã trong môi trường cách ly. Mạng đảm nhiệm việc chuyển dữ liệu giữa các giai đoạn.

Phát biểu về nhu cầu CPU từ nhiều công ty trong năm nay cùng chỉ về một hướng. CEO Amazon Andy Jassy nói trong buổi công bố kết quả tháng 7 rằng phần lớn việc tác nhân dùng công cụ chạy trên CPU, không phải bộ tăng tốc AI. CEO AMD Lisa Su dự báo vào tháng 8 rằng thị trường CPU máy chủ sẽ đạt 220 tỷ đô la vào năm 2030, trong đó tác nhân và môi trường thực thi cách ly sẽ là phần lớn nhất. Cả hai đều là diễn giải và dự báo của lãnh đạo doanh nghiệp.[^amzn-call][^amd-call]

Cũng có tín hiệu thực tế. TrendForce đưa tin vào tháng 4 rằng giá CPU máy chủ tăng 10 đến 20% kể từ tháng 3 và thời gian giao hàng tăng từ 1 đến 2 tuần lên 8 đến 12 tuần. Đây là tin thứ cấp dẫn các phương tiện truyền thông Đài Loan và Nhật Bản. NVIDIA đã xuất xưởng CPU Vera 88 lõi, nêu rõ tác vụ thực thi cách ly cho tác nhân là mục đích sử dụng.[^tf-cpu][^nvda-vera]

Mạng cũng gồm nhiều loại. Kết nối trong rack ghép các chip, Ethernet kết nối các rack, còn CXL mở rộng bộ nhớ. Trong buổi công bố kết quả tháng 9, Broadcom cho biết doanh thu mạng AI cao hơn 2.5 lần so với một năm trước và nhu cầu laser cho truyền thông quang học vượt xa nguồn cung.[^avgo-call]

Bộ xử lý dữ liệu cũng trở thành một hạng mục riêng. Tháng 3, NVIDIA công bố thiết kế dựa trên BlueField-4 để quản lý dữ liệu ngữ cảnh trước thiết bị lưu trữ và cho biết sản phẩm đối tác sẽ ra mắt trong nửa cuối năm 2026. Tính đến ngày 5 tháng 10 năm 2026, chưa tìm thấy tài liệu xác nhận sản phẩm đã xuất xưởng và đi vào hoạt động.[^nvda-stx]

Kết luận ở đây không phải GPU trở nên kém quan trọng. GPU, CPU, bộ xử lý dữ liệu và nhiều loại mạng cùng trở nên cần thiết. Bộ nhớ gắn với tất cả các thiết bị này.

## Có thể dùng lại tính toán, còn ngữ cảnh và tri thức thì tích lũy

Có thể tóm tắt mạch lập luận đến đây trong một câu: hạ tầng tác nhân tăng dung lượng bộ nhớ để tránh tính toán cùng một thứ hai lần.

Khi đọc ngữ cảnh dài, mô hình ngôn ngữ tạo ra các kết quả tính toán trung gian. Chúng được gọi là KV cache. Nếu lưu bộ nhớ đệm, mô hình không phải tính toán lại từ đầu khi đọc cùng ngữ cảnh lần nữa. Đây là lý do đọc ngữ cảnh trong bộ nhớ đệm chỉ có giá bằng một phần hai mươi mức niêm yết trong bảng giá mở đầu.

Bộ nhớ đệm không nhỏ. Trong tài liệu kỹ thuật phát hành tháng 6, IBM ước tính KV cache cho một yêu cầu chiếm khoảng 3 đến 10GB ở mô hình cỡ trung và 40 đến 80GB ở mô hình lớn. Công ty báo cáo rằng tái sử dụng bộ nhớ đệm giảm thời gian từ đầu vào 130,000 token đến phản hồi đầu tiên xuống còn một phần năm mươi sáu. Đây là phép đo nội bộ của một công ty.[^ibm-kv]

NVIDIA đã xác định một tầng mới để lưu bộ nhớ đệm này. Bên dưới HBM trong GPU, bộ nhớ máy chủ và SSD trong máy chủ là một tầng lưu trữ flash kết nối qua Ethernet, mang tên CMX. NVIDIA cũng đưa ra phần mềm quyết định bộ nhớ đệm nên nằm ở tầng nào.[^nvda-cmx][^nvda-dynamo]

Các công ty bộ nhớ cũng đề cập điều tương tự trong báo cáo kết quả. Micron cho biết ngày 30 tháng 9 doanh thu SSD trung tâm dữ liệu trong quý gần 10 tỷ đô la, cao hơn 10 lần so với một năm trước. Công ty nêu lưu trữ ngữ cảnh, tức đưa KV cache xuống tầng lưu trữ, là một trong các nguyên nhân.[^mu-remarks]

SK hynix cho biết trong buổi công bố kết quả tháng 7 rằng doanh thu SSD doanh nghiệp tăng gấp đôi so với quý trước, đồng thời nêu lưu trữ KV cache và lưu trữ đặt gần GPU là các ứng dụng mới. Samsung Electronics dự báo SSD máy chủ sẽ chiếm hơn 60% doanh thu NAND năm 2026. Hai phát biểu này được xác nhận qua bản ghi cuộc gọi do một phương tiện truyền thông đăng lại.[^skh-call][^sec-call]

CEO Western Digital, một công ty ổ cứng, diễn đạt sự khác biệt này trong tháng 8: chu kỳ tính toán có thể được dùng lại, còn dữ liệu tích lũy theo lãi kép. Tác nhân lưu lại nhật ký ở từng bước, và các nhật ký đó trở thành nguyên liệu cho công việc tiếp theo.[^wdc-call]

Tuy nhiên, cần phân biệt tốc độ tăng với quy mô giá trị. Bộ nhớ của một tác nhân cá nhân không lớn nếu xét theo dung lượng. Giá trị tăng lên nếu toàn bộ dịch vụ suy luận chuyển sang thiết kế đưa bộ nhớ đệm xuống flash. Quá trình chuyển đổi này vẫn ở giai đoạn đầu.

## Bộ nhớ chuyển từ sản phẩm tiêu chuẩn sang sản phẩm tích hợp logic

Khi dữ liệu tích lũy nhiều hơn, yêu cầu của khách hàng đối với bộ nhớ cũng thay đổi. Khách hàng trước đây chỉ hỏi dung lượng nay hỏi có thể lấy dữ liệu đúng lúc không, tiêu thụ bao nhiêu điện và tương thích với chip của họ đến đâu. Để đáp ứng, logic cần được tích hợp vào bộ nhớ.

Trong bản cáo bạch niêm yết tại Mỹ tháng 7, SK hynix trực tiếp nêu sự chuyển đổi này. Công ty viết rằng trước đây các nhà sản xuất bộ nhớ cung cấp linh kiện phổ thông, nhưng trong thời đại AI, bộ nhớ đóng vai trò cốt lõi trong tối ưu hóa hiệu năng; tầm nhìn của công ty là nhà sáng tạo bộ nhớ AI toàn diện. Đây là cách công ty tự định vị, cần phân biệt với sự thật đã được chứng minh bằng kết quả kinh doanh.[^skh-424b4]

Ví dụ tiên tiến nhất là đế của HBM. HBM là sản phẩm xếp chồng nhiều lớp chip bộ nhớ; đế là chip ở dưới cùng xử lý tín hiệu và điện năng. Các thế hệ trước được sản xuất bằng quy trình bộ nhớ. Từ HBM4, đế được sản xuất bằng quy trình logic. Samsung Electronics dùng quy trình 4 nanomet của chính mình. Năm 2024, SK hynix công bố hợp tác sản xuất đế HBM4 bằng quy trình logic của TSMC.[^sec-hbm4][^skh-tsmc]

Bước tiếp theo là HBM tùy chỉnh, đưa logic của khách hàng vào đế. Ngày 26 tháng 8, NVIDIA công bố NVHBM, tích hợp mạch điều khiển bộ nhớ của mình vào đế HBM. NVIDIA tuyên bố sản phẩm tăng băng thông 30% và giảm điện năng 15% so với HBM4E tiêu chuẩn. Ngày 30 tháng 9, Micron cho biết sẽ cùng NVIDIA phát triển sản phẩm này.[^nvda-nvhbm][^mu-remarks]

Tại hội nghị bán dẫn Hot Chips tháng 8, Samsung Electronics trình bày cả các bước tiếp theo: chuyển mạch điều khiển, đưa phần tử tính toán vào đế để chia sẻ một phần phép tính của bộ xử lý, rồi xếp trực tiếp bộ nhớ lên trên chip tính toán. Công ty không nêu lịch ra mắt.[^sec-hotchips]

Các sản phẩm cùng hướng cũng xuất hiện ở thiết bị lưu trữ và những loại bộ nhớ khác. Tuy nhiên, mức độ hoàn thiện rất khác nhau giữa các sản phẩm.

| Sản phẩm | Logic tích hợp | Giai đoạn hiện tại |
|---|---|---|
| Đế HBM4 | Điều khiển tín hiệu và điện năng bằng quy trình logic | Sản xuất hàng loạt, đã có doanh thu |
| SOCAMM2 | Mô-đun bộ nhớ tiết kiệm điện cho máy chủ | Sản xuất hàng loạt, doanh số tăng |
| SSD doanh nghiệp | Chip điều khiển và firmware, thiết kế lưu ngữ cảnh | Sản xuất hàng loạt, doanh thu tăng mạnh |
| HBM tùy chỉnh, NVHBM | Mạch điều khiển bộ nhớ của khách hàng | Đang phát triển, dự kiến áp dụng cho GPU thế hệ tiếp theo |
| Mô-đun bộ nhớ CXL | Mạch giám sát để phân loại dữ liệu thường dùng | Có tin Samsung đặt mục tiêu sản xuất hàng loạt vào cuối năm 2026, có thể trễ |
| HBF | Giao diện băng thông cao đặt NAND gần chip tính toán | Công bố quy cách kỹ thuật đầu tiên tháng 8 năm 2026, chưa có sản phẩm |
| PIM, HBM tích hợp phần tử tính toán | Mạch tính toán bên trong bộ nhớ | Mẫu thử và lộ trình |

Các sản phẩm được ghi là sản xuất hàng loạt đã được xác nhận trong tài liệu kết quả kinh doanh năm nay. Tài liệu kết quả quý II của Samsung Electronics ghi nhu cầu đế HBM tăng là một yếu tố ảnh hưởng đến kết quả kinh doanh mảng đúc chip. HBM tùy chỉnh và các sản phẩm bên dưới vẫn chưa được xác nhận qua doanh thu. SK hynix cho biết sẽ giữ cách kết nối hiện tại đến HBM4E; tại sự kiện ngành tháng 9, CXL được đánh giá là tầng bổ trợ chứ không thay thế HBM.[^sec-ir][^skh-q2][^tf-cxl][^hbf-ocp][^sec-fms][^skh-hybrid][^tf-cxl-doubt]

<figure class="kii-figure"><img src="/post-assets/agent-always-on-compute-memory-with-logic-korea-thesis-2026-10-05/maturity.svg" alt="Sơ đồ chia sản phẩm bộ nhớ tích hợp logic thành ba giai đoạn: đã có doanh thu, phát triển và mẫu thử, lộ trình"><figcaption>Phân loại giai đoạn dựa trên công bố và tài liệu kết quả của công ty. Càng về bên trái càng được xác nhận trong kết quả năm nay; càng về bên phải, lịch trình càng chưa rõ. Tính đến ngày 5 tháng 10 năm 2026.</figcaption></figure>

Vì vậy, nói bộ nhớ tích hợp logic là đúng về hướng đi, nhưng phạm vi hiện vẫn hẹp. Các sản phẩm đã xác nhận doanh thu hiện nay là HBM4, mô-đun máy chủ và SSD doanh nghiệp. DRAM và NAND phổ thông vẫn cạnh tranh theo quy cách và giá.

## Giả thuyết bộ nhớ trở thành trung tâm điện toán mới chỉ được xác nhận về hướng đi

Giả thuyết xa hơn là cấu trúc điện toán sẽ thay đổi. Máy tính hiện nay lấy thiết bị tính toán làm trung tâm, còn bộ nhớ cung cấp dữ liệu. Nếu dữ liệu tăng nhanh hơn năng lực tính toán, chi phí di chuyển dữ liệu sẽ cao hơn chi phí tính toán. Khi đó, tính toán ngay tại nơi có dữ liệu sẽ hợp lý hơn.

Nhiều nỗ lực theo hướng này đang xuất hiện. Bước cuối trong lộ trình của Samsung Electronics xếp trực tiếp bộ nhớ lên chip tính toán. Qualcomm cho biết sẽ tích hợp tính toán và bộ nhớ theo cấu trúc ba chiều trong sản phẩm năm 2027. SK hynix và Sandisk cùng Google, Tenstorrent xây dựng quy cách đặt NAND ngay cạnh chip tính toán.[^sec-hotchips][^qcom-hbc][^hbf-ocp]

CEO Sandisk gọi AI trong buổi công bố kết quả tháng 8 là một bài toán về cơ bản lấy bộ nhớ làm trung tâm và cần nhiều lưu trữ. Cần cân nhắc rằng đây là phát biểu của CEO một công ty bộ nhớ.[^sndk-call]

Đánh giá về giả thuyết này cần rõ ràng. Năm 2026, điện toán lấy bộ nhớ làm trung tâm là một quyền chọn, không phải luận cứ đầu tư. Chưa có kiểm chứng hiệu năng độc lập, lịch sản xuất hàng loạt hay xác nhận khách hàng chấp nhận. Đây không phải chất liệu để giải thích giá cổ phiếu hiện tại. Tuy nhiên, nếu hướng đi này đúng, lợi ích lớn nhất sẽ thuộc về doanh nghiệp cùng sở hữu bộ nhớ, quy trình logic và công nghệ xếp chồng.

## Luận điểm đầu tư bộ nhớ Hàn Quốc chuyển từ quy mô sang thời gian duy trì lợi nhuận

Giờ chuyển sang các doanh nghiệp Hàn Quốc. Lợi nhuận năm nay đã lớn. Lợi nhuận hoạt động quý II của mảng bán dẫn Samsung Electronics là KRW 89.2 trillion, tương đương 70% doanh thu. Lợi nhuận hoạt động quý II của SK hynix là KRW 60.5 trillion, tương đương 76% doanh thu.[^sec-ir][^skh-q2]

Tuy nhiên, thị trường không định giá cao mức lợi nhuận này. Tính theo giá đóng cửa ngày 2 tháng 10, Samsung Electronics được giao dịch ở mức 5.85 lần lợi nhuận dự kiến năm 2026, còn SK hynix ở mức 5.25 lần. Lợi nhuận dự kiến là mức bình quân do Naver Finance tổng hợp từ các công ty chứng khoán.[^naver-sec][^naver-skh]

Có thể hiểu mức định giá thấp là dấu hiệu thị trường vẫn xem bộ nhớ là ngành chu kỳ. Mối lo là lợi nhuận hiện nay đến từ thiếu hụt nguồn cung và sẽ giảm mạnh như trước khi việc mở rộng công suất hoàn tất. Đây là cách diễn giải, nhưng có cơ sở. Chính SK hynix đã nêu tình trạng dư cung lặp lại của ngành bộ nhớ trong phần rủi ro của bản cáo bạch.[^skh-424b4]

Đây là điểm bộ nhớ tích hợp logic trở nên quan trọng với đầu tư. Sự thay đổi này không làm lợi nhuận năm nay tăng thêm. Điều cốt lõi là nó có thể tạo lý do để lợi nhuận không giảm sâu như trước sau khi nguồn cung bình thường hóa. Lý do đó nằm ở chi phí chuyển đổi và cấu trúc hợp đồng.

Thứ nhất, khách hàng khó đổi nhà cung cấp hơn. Đế được thiết kế phù hợp với chip của khách hàng không dễ thay bằng sản phẩm của công ty khác. Thời gian thiết kế, kiểm chứng và chứng nhận tạo ra chi phí chuyển đổi. Quy mô chi phí chuyển đổi thực tế và việc nó có được phản ánh vào giá hay không vẫn là giả thuyết chưa được xác nhận.

Thứ hai là cấu trúc hợp đồng. Micron cho biết ngày 30 tháng 9 đã ký 26 hợp đồng với khách hàng chiến lược. Đây là cấu trúc trong đó khách hàng phải thanh toán dù không mua lượng hàng đã cam kết trong nhiều năm; các cam kết tài chính của khách hàng lên tới 32 tỷ đô la, phần lớn là tiền đặt cọc. Micron cho biết sẽ tăng đầu tư thiết bị dựa trên mức độ chắc chắn này.[^mu-remarks]

Hai công ty Hàn Quốc cũng đi theo hướng tương tự. SK hynix cho biết trong quý II đã hoàn tất đàm phán hợp đồng cung ứng dài hạn với khoảng 10 khách hàng, và giải thích trong cuộc gọi kết quả rằng các cơ chế tài chính như tiền đặt cọc được đưa vào. Samsung Electronics cho biết dự định phân bổ 60 đến 70% công suất theo hợp đồng dài hạn, với thời hạn cơ bản 5 năm và gia hạn hằng năm. Giá và điều kiện hủy của từng hợp đồng chưa được công bố.[^skh-q2][^skh-lta][^sec-lta]

Một ngành mà khách hàng đặt tiền trước và cam kết khối lượng sẽ vận hành khác ngành mua bán hàng tiêu chuẩn trên thị trường giao ngay. Tuy nhiên, hợp đồng dài hạn có hai mặt. TrendForce cho biết do cơ chế giá trong hợp đồng dài hạn, mức tăng giá DRAM máy chủ của một số nhà cung cấp thấp hơn bình quân thị trường. Họ đổi phần đỉnh trong chu kỳ tăng lấy một mức sàn trong chu kỳ giảm.[^tf-memory]

## Samsung Electronics và SK hynix đối mặt cùng thay đổi từ những vị thế khác nhau

Hai công ty có điểm mạnh và điểm yếu khác nhau trước cùng một thay đổi là bộ nhớ tích hợp logic.

| Hạng mục | Samsung Electronics | SK hynix |
|---|---|---|
| Biên lợi nhuận hoạt động bán dẫn quý II | 70% | 76% |
| Đế HBM4 | Quy trình 4 nanomet nội bộ | Quy trình TSMC |
| Giá trị logic thuộc về ai, phân tích của bài viết | Có thể giữ lại trong nội bộ qua kết quả mảng đúc chip | Là chi phí trả cho bên ngoài |
| Độ rộng sản phẩm | HBM, mô-đun máy chủ, SSD, đúc chip, đóng gói | HBM, mô-đun máy chủ, SSD, dẫn dắt quy cách HBF |
| Hợp đồng dài hạn | Kế hoạch phân bổ 60 đến 70% công suất | Đã hoàn tất đàm phán với khoảng 10 khách hàng |
| Hoàn vốn cho cổ đông | Kế hoạch cổ tức tiền mặt khoảng KRW 30 trillion trong quý III | Nghị quyết hủy cổ phiếu quỹ KRW 40 trillion |
| Giá so với lợi nhuận dự kiến năm 2026 | 5.85 lần | 5.25 lần |

Điểm mạnh của SK hynix là khả năng sinh lời và quan hệ khách hàng hiện tại. Biên lợi nhuận hoạt động cao hơn, và công ty đã hoàn tất đàm phán hợp đồng cung ứng dài hạn với khoảng 10 khách hàng. Điểm yếu là giá trị logic được trả ra bên ngoài. Theo tin TrendForce dẫn phương tiện truyền thông Hàn Quốc, giá thành đế HBM4 do TSMC sản xuất cao gấp 3 đến 4 lần chip bộ nhớ. Đây không phải con số được công ty xác nhận.[^tf-basedie]

Điểm mạnh của Samsung Electronics là cấu trúc giữ giá trị logic trong công ty. Samsung Electronics tự giới thiệu là công ty duy nhất có đồng thời bộ nhớ, thiết kế logic, đúc chip và đóng gói.[^sec-fms] Điểm yếu là cấu trúc này chưa được chứng minh đầy đủ bằng lợi nhuận. Không được tính hai lần doanh thu đế do nội bộ sản xuất như thể đó là khoản tiền kiếm từ khách hàng bên ngoài. Cần xác nhận bằng chi phí hợp nhất và dòng tiền.

Hoàn vốn cho cổ đông là con đường lợi nhuận đến với cổ đông. Tháng 8, SK hynix thông qua việc mua lại và hủy toàn bộ cổ phiếu quỹ trị giá KRW 40 trillion, đồng thời nâng mục tiêu hoàn vốn dòng tiền tự do lên trên 50%. Samsung Electronics dự kiến chi khoảng KRW 30 trillion cổ tức tiền mặt trong quý III và sẽ xác nhận tại cuộc họp hội đồng quản trị cuối tháng 10. Cả hai thông tin đều được xác nhận qua báo chí; chưa đối chiếu bản công bố chính thức.[^skh-return][^sec-return]

Đánh giá của tôi như sau. Càng tiến sâu vào xu hướng tích hợp logic vào bộ nhớ, doanh nghiệp tự sản xuất logic càng có lợi thế cấu trúc. Xét kết quả và vị thế khách hàng hiện nay, SK hynix đang dẫn trước. Ở giai đoạn đầu, năng lực thực thi của SK hynix có lợi thế; khi HBM tùy chỉnh và các bước tiếp theo phát triển mạnh, cấu trúc tích hợp của Samsung Electronics có khả năng tạo ra giá trị lớn hơn. Điểm chuyển tiếp sẽ là lúc đế do Samsung Foundry sản xuất được chế tạo hàng loạt theo thiết kế của khách hàng bên ngoài.

## Giá hiện tại giả định chỉ còn lại hơn một nửa lợi nhuận năm nay

Có thể đơn giản hóa giá cổ phiếu thành lợi nhuận bền vững mà thị trường tin tưởng nhân với hệ số định giá. Giả sử thị trường định giá công ty bộ nhớ ở mức 10 lần, phép tính ngược cho thấy mức lợi nhuận mà giá hiện tại đòi hỏi.

Giá đóng cửa Samsung Electronics ngày 2 tháng 10 là KRW 276,000. Với hệ số 10 lần, lợi nhuận trên mỗi cổ phiếu mà giá đòi hỏi là KRW 27,600, bằng 58.5% mức KRW 47,142 dự kiến năm 2026. Giá đóng cửa SK hynix là KRW 1,842,000; theo cùng phép tính, lợi nhuận trên mỗi cổ phiếu cần có là KRW 184,200, bằng 52.5% mức dự kiến KRW 350,576.[^naver-sec][^naver-skh]

Nói cách khác, giá hiện tại phù hợp với giả định chỉ hơn một nửa lợi nhuận năm 2026 sẽ còn duy trì trong tương lai. Điều đó không có nghĩa đây là suy nghĩ chính xác của thị trường. Có nhiều tổ hợp giữa hệ số định giá và lợi nhuận. Tuy vậy, câu hỏi trở nên rõ ràng: sản phẩm tích hợp logic và hợp đồng dài hạn có thể giữ lợi nhuận sau khi bình thường hóa cao hơn một nửa lợi nhuận năm nay không?

Bảng dưới đây thay đổi tỷ lệ lợi nhuận năm 2026 còn duy trì và hệ số định giá. Con số trong ngoặc là mức thay đổi so với giá đóng cửa ngày 2 tháng 10. Tỷ lệ duy trì và hệ số đều là giả định tính toán của bài viết, không gán xác suất. Không bao gồm cổ tức.

Samsung Electronics, giá cơ sở KRW 276,000

| Tỷ lệ lợi nhuận dự kiến năm 2026 còn duy trì | 8 lần | 10 lần | 12 lần |
|---|---:|---:|---:|
| 40% | 151,000KRW (-45.3%) | 189,000KRW (-31.7%) | 226,000KRW (-18.0%) |
| 55% | 207,000KRW (-24.8%) | 259,000KRW (-6.1%) | 311,000KRW (+12.7%) |
| 70% | 264,000KRW (-4.3%) | 330,000KRW (+19.6%) | 396,000KRW (+43.5%) |

SK hynix, giá cơ sở KRW 1,842,000

| Tỷ lệ lợi nhuận dự kiến năm 2026 còn duy trì | 8 lần | 10 lần | 12 lần |
|---|---:|---:|---:|
| 40% | 1,122,000KRW (-39.1%) | 1,402,000KRW (-23.9%) | 1,683,000KRW (-8.6%) |
| 55% | 1,543,000KRW (-16.3%) | 1,928,000KRW (+4.7%) | 2,314,000KRW (+25.6%) |
| 70% | 1,963,000KRW (+6.6%) | 2,454,000KRW (+33.2%) | 2,945,000KRW (+59.9%) |

Hai đầu của bảng làm rõ vấn đề. Nếu chỉ còn 40% lợi nhuận, giá cổ phiếu vẫn thấp hơn hiện nay dù hệ số tăng lên 12 lần. Câu chuyện ngành tích cực không thể bù cho lợi nhuận giảm. Ngược lại, nếu thị trường tin rằng 70% lợi nhuận còn lại, giá cổ phiếu cao hơn 20 đến 33% ngay cả khi hệ số vẫn là 10 lần.

Cần chú ý đến số liệu của SK hynix. Lợi nhuận ròng quý II là KRW 93.9 trillion, cao hơn lợi nhuận hoạt động KRW 60.5 trillion. Chưa xác định được nguyên nhân. Nếu khoản lợi nhuận đó đến từ các hạng mục ngoài hoạt động kinh doanh, lợi nhuận trên mỗi cổ phiếu dự kiến cả năm có thể bao gồm lợi nhuận không lặp lại; khi đó cần giả định tỷ lệ duy trì thấp hơn.[^skh-q2]

Chìa khóa tái định giá là tỷ lệ lợi nhuận còn duy trì, không phải hệ số định giá. Bộ nhớ tích hợp logic và hợp đồng dài hạn có thể giúp nâng tỷ lệ đó. Liệu chúng có làm được hay không sẽ rõ trong năm 2027 và 2028, khi nguồn cung tăng.

## Phản biện mạnh nhất là giá trị logic thuộc về bên thiết kế

Lập luận này có những phản biện mạnh. Tôi nêu các phản biện đáng kể nhất trước.

Thứ nhất là bên nắm giữ giá trị. Trong NVHBM, NVIDIA thiết kế mạch điều khiển được tích hợp vào đế. NVIDIA cho biết nhiều công ty bộ nhớ sẽ cung cấp cùng một quy cách. Micron thuê xưởng đúc bên ngoài sản xuất đế đó. Trong cấu trúc này, giá trị thiết kế thuộc về NVIDIA, giá trị sản xuất thuộc về xưởng đúc, còn các công ty bộ nhớ có thể lại cạnh tranh trên cùng một quy cách.[^nvda-nvhbm][^mu-foundry]

Điều tương tự xảy ra ở thiết bị lưu trữ. Trong thiết kế lưu ngữ cảnh của NVIDIA, phần tính toán quản lý dữ liệu nằm trong bộ xử lý dữ liệu NVIDIA, không nằm trong SSD. Phần mềm quyết định bộ nhớ đệm nằm ở tầng nào cũng thuộc NVIDIA. Nơi dữ liệu tích lũy và nơi khiến khách hàng khó rời bỏ có thể khác nhau.[^nvda-cmx][^nvda-dynamo]

Phản biện này làm lung lay lập luận của bài viết nhiều nhất. Việc logic được đưa vào bộ nhớ và việc công ty bộ nhớ sở hữu logic đó là hai chuyện khác nhau. Đây cũng là lý do bài viết nhấn mạnh cấu trúc tích hợp của Samsung Electronics. Công ty bộ nhớ không tự sản xuất được logic có thể bị đẩy vào vị trí hẹp hơn khi sản phẩm ngày càng phức tạp.

Thứ hai là sự thích ứng của nhu cầu. Khi bộ nhớ đắt lên, khách hàng tìm cách dùng ít hơn. Ngày 29 tháng 9, TrendForce cho biết các nhà sản xuất GPU và chip tùy chỉnh đang xem xét giảm dung lượng HBM trên mỗi thiết bị và ưu tiên đánh giá cấu hình 8 lớp trong năm 2027. Các nhà nghiên cứu Google công bố tháng 3 phương pháp nén giảm lượng bộ nhớ KV cache xuống dưới một phần sáu. Tài liệu Anthropic cho biết độ chính xác giảm khi ngữ cảnh dài hơn và cung cấp chức năng chuyển các cuộc hội thoại cũ thành bản tóm tắt.[^tf-hbm][^turboquant][^anthropic-context]

Chưa có câu trả lời liệu tốc độ tích lũy có nhanh hơn công nghệ tiết giảm hay không. Micron cũng thừa nhận tốc độ tăng bộ nhớ trong mỗi máy chủ đã phần nào giảm do giá.[^mu-remarks]

Thứ ba là nguồn cung và vốn. Ngày 30 tháng 7, TrendForce dự báo nguồn cung NAND sẽ dịu lại trong nửa cuối năm 2027 và tạo áp lực giảm giá. Theo tin TrendForce, thị phần doanh thu DRAM quý II của CXMT Trung Quốc tăng lên 9.5%. Trong bài phát biểu ngày 10 tháng 9, Tổng giám đốc Ngân hàng Thanh toán Quốc tế cảnh báo đầu tư thiết bị của các công ty công nghệ lớn đang vượt quá dòng tiền. Nếu tiền của khách hàng cạn, cam kết trong hợp đồng dài hạn cũng sẽ bị thử thách.[^tf-supply][^tf-china][^bis]

Ngược lại, Micron cho rằng cân đối cung cầu năm 2027 và 2028 sẽ căng hơn năm 2026. Việc dự báo của tổ chức nghiên cứu và nhà cung cấp khác nhau chính là lý do không nên kết luận chắc chắn về năm 2027.[^mu-remarks]

Tiền đề về nhu cầu cũng cần được kiểm tra. Điểm xuất phát của bài viết là mọi người sẽ tiếp tục giao việc cho tác nhân. Trong dữ liệu sử dụng riêng công bố tháng 2, Anthropic cho biết các tác vụ kéo dài liên tục hơn 45 phút chỉ nằm trong nhóm 0.1% cao nhất. Phần lớn công việc ngắn hơn nhiều. Nếu việc ủy thác không trở thành thói quen hoặc người dùng không giao quyền, tốc độ phát triển điện toán luôn hoạt động sẽ chậm hơn giả định của bài viết.[^anthropic-autonomy]

## Quý tới cần kiểm tra căn cứ duy trì lợi nhuận, không phải giá

Có thể kiểm tra lập luận này qua các số liệu sắp công bố. Dưới đây là các hạng mục cần theo dõi và điều kiện có thể làm thay đổi đánh giá.

| Hạng mục cần kiểm tra | Tín hiệu củng cố lập luận | Tín hiệu làm lập luận yếu đi |
|---|---|---|
| Kết quả quý III, tháng 10 | Khối lượng HBM4 và SSD doanh nghiệp tăng, cơ cấu sản phẩm cải thiện | Phần lớn tăng trưởng lợi nhuận chỉ do giá hàng phổ thông tăng |
| Hợp đồng dài hạn | Công bố tiền đặt cọc và điều kiện mua tối thiểu, gia hạn hợp đồng | Từ bỏ lợi nhuận do trần giá, tiếp tục không công bố điều kiện |
| HBM tùy chỉnh | Đế Samsung Foundry sản xuất hàng loạt cho khách hàng bên ngoài | Ba nhà sản xuất cạnh tranh giá trên một quy cách |
| Lưu trữ ngữ cảnh | Sản phẩm đối tác CMX xuất xưởng, hợp đồng máy chủ lưu trữ chuyên dụng | Công nghệ nén phổ biến, giao hàng chậm |
| Nguồn cung năm 2027 | Giá hợp đồng tiếp tục tăng, khách hàng nâng kế hoạch đầu tư | Giá NAND giảm, lượng HBM trên mỗi thiết bị thu hẹp |

Theo tin báo chí, kết quả sơ bộ quý III của Samsung Electronics sẽ được công bố ngày 8 tháng 10. Mức bình quân lợi nhuận hoạt động do FnGuide tổng hợp là KRW 108.1 trillion. SK hynix dự kiến công bố vào cuối tháng 10, với mức bình quân lợi nhuận hoạt động KRW 77.2 trillion. Cả hai đều theo tin ngày 5 tháng 10; chưa xác nhận thông báo lịch chính thức của công ty.[^consensus]

Cần xem nội dung hơn là con số. Ngay cả khi lợi nhuận hoạt động vượt bình quân, nếu chỉ do giá hàng phổ thông tăng thì không liên quan đến lập luận của bài viết. Ngược lại, dù lợi nhuận hoạt động thấp hơn bình quân, căn cứ duy trì lợi nhuận sẽ mạnh hơn nếu khối lượng HBM4 và chất lượng hợp đồng dài hạn cải thiện.

Cũng cần nêu điều kiện để thay đổi đánh giá. Nếu HBM tùy chỉnh trở thành một quy cách duy nhất khiến ba công ty bộ nhớ cạnh tranh trên cùng sản phẩm, đồng thời giá hợp đồng năm 2027 bắt đầu giảm, cần hạ mức đánh giá luận điểm này một bậc. Khi đó, bộ nhớ Hàn Quốc sẽ vẫn được xem là ngành chu kỳ dù sản xuất các sản phẩm tinh vi hơn.

<strong>Tác nhân dùng bộ nhớ để tiết kiệm tính toán. Logic được tích hợp vào sản phẩm chứa ký ức ấy, và một số khách hàng bắt đầu đặt tiền trước. Việc bộ nhớ Hàn Quốc được tái định giá phụ thuộc vào khả năng duy trì lợi nhuận sau khi nguồn cung tăng; giá hiện tại vẫn chỉ phản ánh hơn một nửa lợi nhuận năm nay.</strong>

## Ranh giới nguồn và phép tính

Đã đối chiếu công bố của công ty, hồ sơ công khai và tài liệu của tổ chức nghiên cứu vào ngày 5 tháng 10 năm 2026. Các phát biểu được xác nhận qua phương tiện truyền thông đăng lại bản ghi cuộc gọi được ghi chú trong chú thích. Số liệu hiệu năng do công ty công bố chưa được kiểm chứng độc lập. Tỷ lệ lợi nhuận còn duy trì và hệ số định giá trong bảng độ nhạy là giả định tính toán, không phải dự báo. Lợi nhuận trên mỗi cổ phiếu dự kiến sử dụng nguyên số liệu tổng hợp của Naver Finance; chưa xác minh được dự báo năm 2027.

[^anthropic-pricing]: [Anthropic official pricing](https://platform.claude.com/docs/en/about-claude/pricing), accessed 2026-10-05. Opus 5.5 standard input $4, batch $2, fast $8, and cached reads $0.20 per million tokens. Includes the Managed Agents session fee.

[^managed-agents]: [Claude Managed Agents overview documentation](https://platform.claude.com/docs/en/managed-agents/overview), accessed 2026-10-05. Documentation for a beta product.

[^google-io]: [Summary of Sundar Pichai's Google I/O 2026 keynote](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/), 2026-05. Company-reported figures.

[^metr]: [METR Time Horizon 1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1/), 2026-01-29. Time horizon at a 50% success rate.

[^openai-pricing]: [OpenAI API pricing](https://developers.openai.com/api/docs/pricing), accessed 2026-10-05. gpt-6-astra standard $10, Flex $5, Fast $20, and cached input $1. gpt-6-luna input $0.10.

[^google-pricing]: [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing), updated 2026-10-01. Gemini 3.1 Pro Preview standard $2, batch $1, Priority $3.60, plus an hourly cache-storage fee.

[^nvidia-slm]: [Small Language Models are the Future of Agentic AI](https://arxiv.org/abs/2506.02153), submitted by NVIDIA researchers on 2025-06-02. The paper presents a view; 40–70% is an estimate.

[^agent-skills]: [Anthropic Agent Skills overview documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), accessed 2026-10-05.

[^skyvern]: [Code-replay measurements on the Skyvern blog](https://www.skyvern.com/blog/asking-ai-to-build-scrapers-should-be-easy-right/), published 2025-10-17, updated 2026-08-24. Company's own measurements.

[^amzn-call]: [Republished transcript of Amazon's Q2 2026 earnings call](https://www.investing.com/news/transcripts/earnings-call-transcript-amazon-tops-q2-2026-estimates-as-aws-growth-accelerates-93CH-4826442), 2026-07-30. Management statement.

[^amd-call]: [Republished transcript of AMD's Q2 2026 earnings call](https://www.fool.com/earnings/call-transcripts/2026/08/11/amd-amd-q2-2026-earnings-call-transcript/), call on 2026-08-04. Market size is a company forecast.

[^tf-cpu]: [TrendForce report on server CPU prices](https://www.trendforce.com/news/2026/04/22/news-server-cpu-prices-up-as-much-as-20-since-march-intel-may-raise-prices-another-8-10-in-2h26/), 2026-04-22. Cites Taiwanese and Japanese media.

[^nvda-vera]: [NVIDIA announcement on Vera CPU shipments](https://blogs.nvidia.com/blog/vera-cpu-delivery/), 2026-05-18.

[^avgo-call]: [Republished transcript of Broadcom's FY2026 Q3 earnings call](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/), call on 2026-09-02. Management statement.

[^nvda-stx]: [NVIDIA announcement of BlueField-4 STX storage architecture](https://nvidianews.nvidia.com/news/nvidia-launches-bluefield-4-stx-storage-architecture-with-broad-industry-adoption), 2026-03-16. Performance figures are company claims.

[^ibm-kv]: [IBM Redbooks KV cache technical document](https://www.redbooks.ibm.com/docs/MD260021/MD260021.html), published 2026-06-05. Company measurements and estimates.

[^nvda-cmx]: [NVIDIA CMX product description](https://www.nvidia.com/en-us/data-center/ai-storage/cmx/), accessed 2026-10-05. Publication date not shown.

[^nvda-dynamo]: [NVIDIA Dynamo KV cache tiering documentation](https://docs.nvidia.com/dynamo/v1.1.0/user-guides/kv-cache-offloading), accessed 2026-10-05. The document does not provide performance figures.

[^mu-remarks]: [Micron FY2026 Q4 prepared remarks](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf), 2026-09-30. Data center SSD revenue is described in the original as "nearly $10 billion." Strategic customer agreements, deposits, NVHBM, and supply-demand outlook were cross-checked in this document.

[^skh-call]: [Republished transcript of SK hynix's Q2 2026 earnings call](https://www.investing.com/news/transcripts/earnings-call-transcript-sk-hynix-posts-record-q2-2026-results-as-shares-fall-93CH-4818480), July 2026 call. Not the company's official transcript.

[^sec-call]: [Republished transcript of Samsung Electronics' Q2 2026 earnings call](https://www.investing.com/news/transcripts/earnings-call-transcript-samsung-electronics-posts-record-q2-2026-profit-as-ai-demand-surges-93CH-4822292), July 2026 call. Not the company's official transcript.

[^wdc-call]: [Summary of Western Digital FY2026 Q4 earnings call](https://finance.biggo.com/news/US_WDC_2026-08-05), 2026-08-05. Statement checked in a secondary summary.

[^skh-424b4]: [SK hynix US listing prospectus, SEC 424B4](https://www.sec.gov/Archives/edgar/data/0002120882/000119312526299963/d32785d424b4.htm), 2026-07-09. Strategy section, Custom HBM definition, and risk factors checked against the original.

[^sec-hbm4]: [Samsung Electronics announcement of HBM4 volume shipments](https://news.samsungsemiconductor.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing/), 2026-02-12. Process and performance are company descriptions.

[^skh-tsmc]: [SK hynix and TSMC announcement of HBM4 collaboration](https://www.prnewswire.com/news-releases/sk-hynix-partners-with-tsmc-to-strengthen-hbm-technological-leadership-302120755.html), 2024-04-18. Announcement of development direction at the time.

[^tf-basedie]: [TrendForce report on SK hynix HBM4E base dies](https://www.trendforce.com/news/2026/08/31/news-sk-hynix-reportedly-weighs-intel-for-hbm4e-base-dies-amid-tsmc-cost-pressure-and-supply-diversification/), 2026-08-31. Cites Korean media; not confirmed by the company.

[^nvda-nvhbm]: [NVIDIA announcement of NVHBM](https://blogs.nvidia.com/blog/nvlink-fusion-nvhbm-custom-high-bandwidth-memory/), 2026-08-26. Bandwidth and power figures are company claims.

[^sec-hotchips]: [ServeTheHome summary of Samsung Electronics' Hot Chips 2026 presentation](https://www.servethehome.com/samsung-evolving-hbm-base-die-at-hot-chips-2026/), 2026-08-23. Roadmap is a company presentation; no schedule was provided.

[^sec-ir]: [Samsung Electronics Q2 2026 earnings presentation](https://images.samsung.com/kdp/ir/events/2026/2026_2Q_conference_kor.pdf), 2026-07-30. Semiconductor revenue KRW 127.5 trillion, operating profit KRW 89.2 trillion. Cites HBM base die demand as a factor in foundry performance.

[^skh-q2]: [SK hynix Q2 2026 earnings release](https://news.skhynix.com/en/q2-2026-business-results/), 2026-07-29. Revenue KRW 79.3 trillion, operating profit KRW 60.5 trillion, net income KRW 93.9 trillion, long-term supply agreements, and SOCAMM2.

[^tf-cxl]: [TrendForce report on Samsung and SK hynix CXL 3.2](https://www.trendforce.com/news/2026/07/21/news-samsung-reportedly-targets-2026-cxl-3-2-mass-production-sk-hynix-advances-new-ai-memory-architecture/), 2026-07-21. Secondary reporting.

[^hbf-ocp]: [Sandisk and SK hynix release the first HBF OCP specification](https://www.storagenewsletter.com/2026/08/05/fms-2026-sandisk-and-sk-hynix-advance-global-standardization-of-high-bandwidth-flash-with-release-of-first-ocp-technical-specification/), 2026-08-05.

[^sec-fms]: [StorageReview summary of Samsung Electronics' FMS 2026 presentation](https://www.storagereview.com/news/samsung-outlines-3d-memory-roadmap-for-ai-infrastructure-at-fms-2026), 2026-08-04. Low-power memory with PIM was shown; volume-production timing was not confirmed.

[^skh-hybrid]: [Tom's Hardware report on SK hynix's Hot Chips 2026 presentation](https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-says-hybrid-bonding-wont-be-ready-for-hbm4e-as-ai-memory-runs-into-a-775-micron-ceiling), 2026-08-24.

[^tf-cxl-doubt]: [TrendForce report from the AI Infrastructure Summit](https://www.trendforce.com/news/2026/09/18/news-openai-intel-reportedly-downplay-cxl-as-hbm-replacement-citing-use-case-and-data-transfer-limits/), 2026-09-18. Secondary reporting.

[^qcom-hbc]: [Qualcomm announcement of data center roadmap](https://www.qualcomm.com/news/releases/2026/06/qualcomm-unveils-comprehensive-data-center-roadmap-for-the-agent), 2026-06. Performance figures are company claims and have not been independently verified.

[^sndk-call]: [Republished transcript of Sandisk FY2026 Q4 earnings call](https://www.fool.com/earnings/call-transcripts/2026/08/12/sandisk-sndk-q4-2026-earnings-call-transcript/), call on 2026-08-05.

[^naver-sec]: [Naver Finance Samsung Electronics daily prices](https://m.stock.naver.com/api/stock/005930/price?pageSize=5&page=1) and [annual financial estimates](https://m.stock.naver.com/api/stock/005930/finance/annual), accessed 2026-10-05. October 2 close KRW 276,000; estimated 2026 EPS KRW 47,142.

[^naver-skh]: [Naver Finance SK hynix daily prices](https://m.stock.naver.com/api/stock/000660/price?pageSize=5&page=1) and [annual financial estimates](https://m.stock.naver.com/api/stock/000660/finance/annual), accessed 2026-10-05. October 2 close KRW 1,842,000; estimated 2026 EPS KRW 350,576.

[^skh-lta]: [NewsPim report on SK hynix's Q2 earnings call](https://www.newspim.com/news/view/20260729000198), 2026-07-29. Deposit statement checked in media reporting.

[^sec-lta]: [The Elec transcript of Samsung Electronics' Q2 earnings call](https://www.thelec.kr/news/articleView.html?idxno=60316), 2026-07-30. Long-term contract share and structure are management plans.

[^tf-memory]: [TrendForce forecast for memory contract prices in Q4 2026](https://www.trendforce.com/presscenter/news/20260930-13258.html), 2026-09-30. Forecast, not realized pricing.

[^skh-return]: [ZDNet Korea report on SK hynix share cancellation](https://zdnet.co.kr/view/?no=20260819161157), 2026-08-19. Original filing not cross-checked.

[^sec-return]: [Report on Samsung Electronics' 2026 shareholder returns](https://v.daum.net/v/20260821172850433), 2026-08-21. Plan, not an amount already paid.

[^mu-foundry]: [The Elec report on Micron outsourcing base-die production](https://www.thelec.net/news/articleView.html?idxno=14372), 2026-10-02. Micron's prepared remarks do not name the foundry.

[^tf-hbm]: [TrendForce outlook for HBM in 2027](https://www.trendforce.com/presscenter/news/20260929-13255.html), 2026-09-29. Research-firm forecast.

[^turboquant]: [Google Research introduction to TurboQuant](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/), 2026-03-24. Research result; scope of commercial deployment not confirmed.

[^anthropic-context]: [Anthropic context-window documentation](https://platform.claude.com/docs/en/build-with-claude/context-windows) and [compaction documentation](https://platform.claude.com/docs/en/build-with-claude/compaction), accessed 2026-10-05.

[^anthropic-autonomy]: [Anthropic research on measuring agent autonomy](https://www.anthropic.com/research/measuring-agent-autonomy), 2026-02-18. 99.9th percentile in company usage data.

[^tf-supply]: [TrendForce memory supply-demand outlook for 2026–2027](https://www.trendforce.com/presscenter/news/20260730-13158.html), 2026-07-30. Research-firm forecast.

[^tf-china]: [TrendForce report on CXMT and YMTC capacity expansion](https://www.trendforce.com/news/2026/09/24/news-cxmt-ymtc-ramp-memory-capacity-but-chinas-ai-cloud-boom-could-soak-up-new-supply-through-2027/), 2026-09-24. Secondary reporting.

[^bis]: [BIS General Manager's speech](https://www.bis.org/speeches/20260910-artificial-intelligence-growth-and-financial-stability-challenges-central-banks), 2026-09-10.

[^consensus]: [MoneyToday report on third-quarter earnings forecasts](https://www.mt.co.kr/amp/stock/2026/10/05/2026100217315021825), 2026-10-05. Cites FnGuide consensus.

*Miễn trừ trách nhiệm: Tài liệu phục vụ nghiên cứu và cung cấp thông tin. Mã cổ phiếu, hệ số và kịch bản là ví dụ phân tích; độc giả cần tự xem xét trước khi quyết định đầu tư.*
