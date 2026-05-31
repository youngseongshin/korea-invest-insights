---
title: "Trong bong bóng lợi nhuận, dự phóng bị cắt sau cùng: sự dồn vốn vào hạ tầng AI và giá trị của nghiên cứu chuyên sâu"
slug: "ai-infra-earnings-bubble-deep-dive-research-thesis-os-2026-05-31"
date: 2026-05-31T14:00:00+09:00
description: "BCA Research cho rằng bong bóng AI không phải bong bóng định giá mà là bong bóng lợi nhuận. Trong bong bóng lợi nhuận, giá cổ phiếu rơi từ rất lâu trước khi dự phóng lợi nhuận bị cắt. Vì vậy, đúng lúc dòng vốn đang dồn vào hạ tầng AI, việc đọc trực tiếp cấu trúc hệ thống và các chỉ báo dẫn dắt qua nghiên cứu chuyên sâu lại quan trọng hơn là chờ đợi đồng thuận. Ghi chú này trình bày phương pháp đó một cách điềm tĩnh, qua Thesis OS và công việc thực tế của blog chúng tôi."
categories: ["Korea Market", "Research Process"]
tags:
  - "AI 인프라"
  - "이익 버블"
  - "딥다이브 리서치"
  - "Thesis OS"
  - "반도체 사이클"
  - "컨센서스"
  - "선행지표"
  - "AI PCB"
  - "Research OS"
draft: false
---

> Đây là một ghi chú phương pháp luận. Với những bài viết làm nguyên liệu cho phân tích, nên đọc kèm theo: [luận điểm về đế/PCB AI (nút thắt chung của BOM hệ thống)](/vi/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/), [nhu cầu token của Goldman so với đỉnh ASP bộ nhớ của J.P. Morgan](/vi/post/goldman-token-demand-vs-jpm-memory-asp-peakout-korea-semiconductor-2026-05-31/), và [ghi chú công khai về Thesis OS](/vi/post/thesis-os-open-source-research-operating-system-2026-05-30/) giải thích cấu trúc vận hành toàn bộ công việc này.

## TL;DR

* Trong một báo cáo gần đây, BCA Research cho rằng <strong>bong bóng AI không phải bong bóng định giá mà là bong bóng lợi nhuận (earnings)</strong>. Không phải PER phình lên, mà chính lợi nhuận phình lên. Và như mọi bong bóng, sớm muộn nó cũng xẹp, dù BCA nói thêm rằng các thước đo nhu cầu AI của họ vẫn chưa cho thấy tín hiệu sắp xảy ra.
* Đặc trưng cốt lõi của bong bóng lợi nhuận là <strong>độ trễ</strong>. Theo cách diễn đạt của BCA, gần như trong mọi trường hợp "cổ phiếu bắt đầu rơi từ rất lâu trước khi dự phóng lợi nhuận bị cắt." Dự phóng đồng thuận là một tín hiệu trễ.
* Vì vậy, đúng vào giai đoạn dòng tiền dồn vào hạ tầng AI như thế này, điều quan trọng hơn là một <strong>nghiên cứu chuyên sâu đọc trực tiếp cấu trúc hệ thống và các chỉ báo dẫn dắt nhu cầu, thay vì chờ đợi EPS đồng thuận</strong>. Khi dự phóng đã bị cắt thì đã quá muộn.
* Ghi chú này trình bày, không hề phóng đại, nghiên cứu chuyên sâu đó thực sự quan sát những gì, và chúng tôi đã vận hành nó bằng một cấu trúc gọi là <strong>Thesis OS</strong> ra sao.

---

## 1. Gọi bong bóng AI là "bong bóng lợi nhuận" nghĩa là gì

Khi nói "bong bóng", người ta thường hình dung PER vọt lên — một bong bóng định giá, nơi giá tăng nhanh hơn lợi nhuận rất nhiều. BCA Research nhìn AI như một loại hơi khác. Đó là <strong>bong bóng lợi nhuận, nơi chính lợi nhuận phình lên chứ không phải giá</strong>.

Đây không phải mô thức mới. Các doanh nghiệp xây nhà và ngân hàng đã làm đúng như vậy ngay trước khủng hoảng tài chính. PER của họ trông thấp, nhưng chỉ vì lợi nhuận không bền vững thổi phồng mẫu số (E) và làm hệ số trông rẻ. Những ngành dao động mạnh theo chu kỳ thịnh-suy — tài nguyên thiên nhiên, hàng không, vận tải biển, và bán dẫn ngày nay — dễ tổn thương trước loại bong bóng lợi nhuận này.

Ngay lúc này, đường doanh thu bán dẫn đang giống bức tranh đó.

![Doanh số bán dẫn toàn cầu vẽ nên một đường parabol — tái dựng dựa trên số liệu tổng hợp hằng năm công khai của WSTS](global-semiconductor-sales-parabolic.png)

<small>Nguồn: tái dựng gần đúng dựa trên số liệu tổng hợp hằng năm công khai của WSTS, với 2025-2026 là ước tính. Mang tính minh họa, không phải lời khuyên đầu tư. Hình dạng của dữ liệu gốc cùng mạch với biểu đồ "doanh số bán dẫn parabol" trình bày trong báo cáo của BCA Research (2026-05-28).</small>

Đường doanh thu trở nên parabol vừa là tin tốt vừa là lời cảnh báo. Khi lợi nhuận tăng nhanh, PER trông thấp. Nhưng nếu lợi nhuận đó là sản phẩm của chu kỳ, thì chính việc hệ số trông rẻ có thể trở thành cái bẫy. Lời cảnh báo xưa cũ của các ngành chu kỳ áp dụng ở đây: <strong>"khoảnh khắc nguy hiểm nhất là khi lợi nhuận đạt đỉnh."</strong>

Đừng hiểu lầm. Cả BCA lẫn chúng tôi đều không nói "nó xẹp ngay bây giờ". BCA đánh giá các thước đo nhu cầu AI của họ — tỷ lệ chấp nhận, chi tiêu cho token, lượt tải công cụ lập trình bằng AI, giá GPU và bộ nhớ — phần lớn vẫn ở mức yên tâm. Điểm mấu chốt không phải thời điểm, mà là <strong>bong bóng này vận hành theo cách nào</strong>.

---

## 2. Cái bẫy thật sự của bong bóng lợi nhuận là "độ trễ"

Điều khiến bong bóng lợi nhuận nguy hiểm không phải là nó vỡ, mà là <strong>thứ tự nó vỡ</strong>.

Điểm cốt lõi BCA chỉ ra là: giới phân tích Phố Wall đoán kém về thời điểm bong bóng lợi nhuận xẹp. Và gần như trong mọi trường hợp, <strong>"cổ phiếu bắt đầu rơi từ rất lâu trước khi dự phóng lợi nhuận bị cắt"</strong> (BCA Research, 2026-05-28).

Đây là ý nghĩa thực tế của câu đó, được vẽ ra.

![Trong bong bóng lợi nhuận, giá cổ phiếu rơi trước khi dự phóng bị cắt — sơ đồ khái niệm](earnings-bubble-price-leads-estimate-cuts.png)

<small>Đây là sơ đồ khái niệm, không phải dữ liệu thật. Nó đơn giản hóa cấu trúc độ trễ mà BCA mô tả, trong đó giá đi trước và dự phóng đi sau.</small>

Đường đỏ (giá cổ phiếu) quay đầu giảm trước. Đường xanh chấm (dự phóng lợi nhuận đồng thuận) chỉ bị cắt rất lâu sau đó. Dải xám ở giữa chính là độ trễ. Nếu bạn theo nguyên tắc "tôi sẽ bán khi giới phân tích hạ giá mục tiêu hoặc dự phóng", bạn sẽ luôn hành động muộn đúng bằng độ trễ đó.

Từ đó rút ra kết luận. <strong>Dự phóng đồng thuận là một tín hiệu trễ.</strong> Cổ phiếu không trông đắt nhất khi lợi nhuận đạt đỉnh, và đến lúc dự phóng bị cắt thì giá đã rơi rồi. Nên nếu chỉ nhìn dự phóng, bạn sẽ bỏ lỡ cả đỉnh bong bóng lẫn điểm uốn của nó.

---

## 3. Vì vậy cần nghiên cứu chuyên sâu — nó quan sát những gì

Nếu dự phóng đi sau, phải nhìn gì để đi trước? Nghiên cứu chuyên sâu không nhìn EPS tiêu đề, mà nhìn <strong>cấu trúc và các chỉ báo dẫn dắt</strong> tạo ra EPS đó. Cụ thể là bốn điều.

<strong>① Đọc cấu trúc hệ thống.</strong> Câu chuyện tuyến tính — "sau GPU là bộ nhớ, rồi đến đế" — dễ giao dịch nhưng chỉ đúng một nửa. Hạ tầng AI thực tế là một hệ thống cấp rack, trong đó GPU, CPU, DPU, NIC, ASIC chuyển mạch, mô-đun bộ nhớ và bo nguồn cùng tăng theo. Như chúng tôi trình bày trong [luận điểm về đế/PCB AI](/vi/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/), đế và PCB không phải điểm dừng cuối của một vòng luân chuyển, mà là mẫu số chung của toàn bộ danh mục vật liệu (BOM) hệ thống. Hiểu cấu trúc sẽ thấy được đâu là nút thắt thật sự.

<strong>② Tách các biến số.</strong> Cùng một nhu cầu AI, Goldman theo dõi lượng sử dụng token (Q) và chi phí trên mỗi token (C), còn J.P. Morgan theo dõi tốc độ tăng của giá bộ nhớ (P). Khi [tách hai dự báo thành P, Q và C](/vi/post/goldman-token-demand-vs-jpm-memory-asp-peakout-korea-semiconductor-2026-05-31/), rõ ràng hai quan điểm trông như xung đột thật ra đang nói về các biến số khác nhau và có thể cùng đúng. Gộp tất cả vào một con số tiêu đề chính là điều che lấp chuyện này.

<strong>③ Trực tiếp theo dõi các chỉ báo dẫn dắt.</strong> Thay vì chờ EPS đồng thuận bị cắt, hãy quan sát thứ chuyển động trước — giá và lượng hợp đồng dài hạn HBM, giá hợp đồng DRAM máy chủ, chi tiêu cho token, giá giao ngay GPU và bộ nhớ, tỷ lệ chấp nhận. Những thứ này đổi hướng trước dự phóng.

<strong>④ Tách sự thật, suy luận và phỏng đoán.</strong> "Sự thật đã được xác nhận chính thức", "suy luận hợp lý" và "phỏng đoán đơn thuần" không nằm chung một ô. Những gì chưa kiểm chứng — tên khách hàng, có được lựa chọn hay không, điều khoản hợp đồng — được ghi rõ là suy luận hoặc phỏng đoán. Thiếu sự tách bạch đó, bạn bị cuốn theo một câu chuyện hấp dẫn và mua phỏng đoán như thể là sự thật.

Bốn điều này không chờ dự phóng bị cắt. Nhờ vậy chúng ít chịu thiệt vì độ trễ.

---

## 4. Thesis OS — cấu trúc vận hành nghiên cứu chuyên sâu này thành một hệ thống

Làm tốt bốn điều trên một hai lần thì không khó. Cái khó là làm chúng <strong>mỗi lần, với cùng một kỷ luật</strong>. Vì vậy chúng tôi giao công việc này cho một cấu trúc chứ không phải cho tâm trạng của một người trong ngày hôm đó. Cấu trúc ấy là [Thesis OS](/vi/post/thesis-os-open-source-research-operating-system-2026-05-30/).

Thesis OS chia thành ba vai trò.

| Vai trò | Làm gì |
|---|---|
| <strong>Alpha (알파)</strong> | Thu thập bằng chứng — dữ liệu thị trường, bộ lọc, trình thu thập, quy trình kiểm chứng dữ kiện |
| <strong>Lattice (격자)</strong> | Phán đoán — dệt bằng chứng thành luận điểm, lập dự phóng, kiểm tra bằng lập luận ngược |
| <strong>Arki (아키)</strong> | Quản trị — giữ toàn bộ nhất quán bằng schema, luồng công việc và kiểm tra tình trạng |

Điểm mấu chốt không phải tự động hóa hào nhoáng, mà là <strong>khả năng lặp lại của kỷ luật</strong>. Tách bằng chứng (Alpha) khỏi phán đoán (Lattice) làm giảm khả năng một câu chuyện hay đi trước bằng chứng. Có quản trị (Arki), bạn tách sự thật, suy luận và phỏng đoán theo cùng một chuẩn mỗi lần và tiếp tục theo dõi các chỉ báo dẫn dắt. Thesis OS là mã nguồn mở, nên độc giả quan tâm có thể trực tiếp xem xét chính cấu trúc đó.

---

## 5. Công việc của blog chúng tôi — một cách điềm tĩnh

Chúng tôi viết điều này như một bản ghi chép, không phải để khoe. Bằng chứng trung thực nhất là phương pháp này thực sự đã cho ra những bài viết nào.

* <strong>Lập bản đồ cấu trúc hệ thống</strong>: [luận điểm về đế/PCB AI](/vi/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/) — nhìn AI như một hệ thống cấp rack và định nghĩa lại đế là nút thắt chung.
* <strong>Tách biến số</strong>: [Goldman vs. J.P. Morgan](/vi/post/goldman-token-demand-vs-jpm-memory-asp-peakout-korea-semiconductor-2026-05-31/) — phân rã hai dự báo tưởng đối nghịch thành P, Q và C.
* <strong>Đọc xuyên kết quả (read-through)</strong>: [Marvell Q1 FY2027](/vi/post/marvell-q1-fy2027-korea-semiconductor-readthrough-2026-05-28/), [Dell Q1 FY2027](/vi/post/dell-q1-fy2027-earnings-korea-ai-server-margin-readthrough-2026-05-29/) — dịch kết quả của Mỹ thành nút thắt linh kiện và vật liệu của Hàn Quốc.
* <strong>Theo dõi cấu trúc chi phí</strong>: [hợp đồng tương lai token AI và chi phí trên mỗi token](/vi/post/ai-token-futures-cost-per-token-korea-semiconductor-thesis-2026-05-30/) — trục dịch chuyển từ cuộc đua hiệu năng sang cuộc đua chi phí.

Điểm chung của các bài này là không vội vã đi đến kết luận "mua/bán". Thay vào đó, chúng vẽ cấu trúc, tách biến số, đưa ra các chỉ báo dẫn dắt, và đặt cổ phiếu không như khuyến nghị mà như điểm quan sát. Mục tiêu là trao cho độc giả nguyên liệu để tự phán đoán. Chúng tôi không tuyên bố có thể đoán trúng đỉnh thị trường hay thời điểm bong bóng vỡ. Như BCA kết luận, ngay cả giới phân tích cũng làm điều đó không giỏi. Điều chúng tôi cố làm khiêm tốn hơn: <strong>hiểu cấu trúc trước khi dự phóng bị cắt, và buộc mình nhìn các tín hiệu dẫn dắt thay vì các tín hiệu trễ</strong>.

---

## 6. Kết lại

Trong giai đoạn dòng vốn dồn vào hạ tầng AI nhiều đến vậy, thái độ nguy hiểm nhất là chờ đồng thuận đổi chiều giúp mình. Trong bong bóng lợi nhuận, tín hiệu đó luôn đến muộn. Giá cổ phiếu chuyển động trước khi dự phóng bị cắt.

Vì vậy nghiên cứu chuyên sâu không phải một dự báo hào nhoáng, mà là <strong>sự chuẩn bị để bớt muộn</strong>. Hiểu hệ thống, tách biến số, trực tiếp nhìn các chỉ báo dẫn dắt, và phân biệt sự thật với phỏng đoán. Để lặp lại công việc đó không một lần mà mỗi lần với cùng một kỷ luật, chúng tôi dùng một cấu trúc gọi là [Thesis OS](/vi/post/thesis-os-open-source-research-operating-system-2026-05-30/). Nếu bạn quan tâm, chúng tôi khích lệ bạn nhìn không chỉ các kết luận mà cả cấu trúc và quá trình đằng sau chúng.

<small>Bài viết này trích dẫn ngắn gọn, có ghi nguồn, luận điểm cốt lõi đã công bố trong báo cáo "Earnings Bubbles Are Still Bubbles" của BCA Research (Global Investment Strategy, 2026-05-28), và các biểu đồ do chúng tôi tự thực hiện dựa trên dữ liệu và khái niệm công khai. Đây không phải khuyến nghị mua hay bán bất kỳ chứng khoán cụ thể nào; quyết định đầu tư và trách nhiệm thuộc về chính nhà đầu tư.</small>
