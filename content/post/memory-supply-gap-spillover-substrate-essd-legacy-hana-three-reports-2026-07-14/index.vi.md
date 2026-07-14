---
title: "Khoảng trống nguồn cung lan ra ngoài HBM: đọc ba báo cáo Hana Securities như một câu chuyện"
slug: "memory-supply-gap-spillover-substrate-essd-legacy-hana-three-reports-2026-07-14"
date: 2026-07-14T16:00:00+09:00
description: "Ba báo cáo Hana Securities được tổng hợp thành một khung. Khoảng trống nguồn cung do ba ông lớn chuyển sang HBM và DDR5 đang lan sang đế đóng gói (Daeduck Electronics, Simmtech, Haesung DS), bộ điều khiển eSSD (ASICLAND, FADU) và bộ nhớ legacy (GigaDevice). Đây là bằng chứng cho thấy chu kỳ bùng nổ bộ nhớ đã mở rộng ra ngoài HBM. Tóm tắt báo cáo, không phải khuyến nghị đầu tư."
categories: ["Exclusive Analysis", "Tech-Analysis", "Market-Outlook"]
tags: ["Memory", "Package Substrate", "eSSD", "Legacy Memory", "Daeduck Electronics", "ASICLAND", "FADU", "GigaDevice", "CXMT", "SK Hynix", "Hana Securities"]
valley_cashtags: ["SK하이닉스", "대덕전자"]
draft: false
---

> Bối cảnh
> Bài viết này là phần tiếp theo của cấu trúc tập trung HBM và rủi ro DRAM legacy đã đề cập trong [SK Hynix cắt giảm lợi nhuận Q2 nhưng giữ nguyên giá mục tiêu](/vi/post/sk-hynix-2q-earnings-cut-mirae-kis-lta-target-price-2026-07-14/), [IPO của CXMT và rủi ro giá bộ nhớ](/vi/post/cxmt-ipo-memory-price-risk-hbm-client-dram-2026-06-21/). Nên đọc cùng [FADU 2Q26: có thể vượt kỳ vọng, nhưng chưa phải cú sốc lớn](/vi/post/fadu-2q26-earnings-preview-essd-controller-moderate-beat-2026-07-04/) cho trục FADU eSSD, và [Luận Điểm AI PCB và Substrate](/vi/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/) cho trục đế đóng gói. Các hub liên quan là [Hub AI HBM](/vi/page/korea-semiconductor-hbm-kospi-hub/) và [Hub phân tích độc quyền](/vi/page/exclusive-analysis-hub/).

## TL;DR

* Gộp ba báo cáo mà Hana Securities công bố trong hai tuần gần đây vào một khung duy nhất, ta thấy <strong>ba cảnh của cùng một câu chuyện</strong>. Khoảng trống nguồn cung do ba ông lớn dẫn đầu chuyển dịch sang HBM và DDR5 đang lan sang các chuỗi giá trị lân cận.
* <strong>Cảnh 1, đế đóng gói</strong>: việc DDR5, LPDDR5 mở rộng diện tích và tăng số lớp đang bào mòn năng lực sản xuất thực tế của đế đóng gói. Tín hiệu thiếu hụt nguồn cung là việc ký kết LTA (Daeduck Electronics, Simmtech, Haesung DS).
* <strong>Cảnh 2, bộ điều khiển eSSD</strong>: nhu cầu từ trung tâm dữ liệu AI khiến SSD doanh nghiệp tăng vọt, và SK Hynix đã chọn ASICLAND, một design house trong nước, làm đối tác cho bộ điều khiển Gen6. Bộ điều khiển Gen6 dành cho FADU được kỳ vọng sản xuất hàng loạt vào nửa cuối năm 2027.
* <strong>Cảnh 3, bộ nhớ legacy</strong>: GigaDevice của Trung Quốc đang lấp đầy khoảng trống DDR4 và SLC NAND mà nhóm dẫn đầu bỏ lại. Trong một năm gần đây, ASP của SLC NAND tăng khoảng 5 lần, ASP của DRAM legacy tăng khoảng 10 lần.
* <strong>Chu kỳ bùng nổ bộ nhớ đã mở rộng phạm vi ra ngoài HBM.</strong> Tuy nhiên cả ba trục đều có điểm cần xác minh. Với đế đóng gói là công bố LTA, giá bán và tỷ lệ vận hành; với eSSD là đơn hàng chính thức và thời điểm ghi nhận doanh thu của FADU; với legacy là tốc độ Trung Quốc lấp đầy khoảng trống. \[Phạm vi phân tích: tóm tắt báo cáo\]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Luận điểm chính</div>
  <div class="thesis-callout__body">
    Ba báo cáo đề cập đến ba cổ phiếu khác nhau nhưng hội tụ về một câu duy nhất. Khoảng trống nguồn cung do ba ông lớn dẫn đầu tập trung vào HBM và DDR5 đang lan sang đế đóng gói, bộ điều khiển eSSD và bộ nhớ legacy, mở rộng phạm vi của chu kỳ bùng nổ bộ nhớ ra ngoài HBM.
  </div>
</div>

---

## Khung xuyên suốt: một khoảng trống, ba nhánh lan tỏa

Đọc riêng lẻ, ba báo cáo là ba câu chuyện cổ phiếu không liên quan đến nhau. Nhưng khi đặt chồng lên nhau, đó là ba kết quả tách ra từ cùng một nguyên nhân.

<strong>Nguyên nhân</strong>: ba ông lớn dẫn đầu (Samsung Electronics, SK Hynix, Micron) tập trung nguồn wafer và nguồn lực công đoạn sau vốn có hạn vào HBM và DDR5. Hệ quả là các linh kiện lân cận và sản phẩm legacy rơi vào khoảng trống nguồn cung.

<strong>Lan tỏa</strong>: khoảng trống đó lan theo ba hướng.

| Cảnh | Vị trí khoảng trống nguồn cung | Trục hưởng lợi | Tín hiệu thiếu hụt, tăng trưởng |
|---|---|---|---|
| 1 | Đế đóng gói bộ nhớ | Daeduck Electronics, Simmtech, Haesung DS | Ký kết LTA, tăng giá bán |
| 2 | Bộ điều khiển eSSD | ASICLAND, FADU | SK Hynix chọn Gen6, hợp đồng sản xuất hàng loạt |
| 3 | DRAM legacy, SLC NAND | GigaDevice (Trung Quốc) | ASP tăng vọt, kết quả kinh doanh bất ngờ |

Bên dưới là phần trình bày từng cảnh cùng số liệu gốc trong báo cáo.

---

## Cảnh 1: đế đóng gói, công suất bị bào mòn âm thầm

Báo cáo đầu tiên là `Khuyến nghị mua ngành đế đóng gói bộ nhớ` của chuyên viên phân tích Kim Min-kyung, Hana Securities (ngày 3/7/2026). \[Thực tế: báo cáo Hana Securities\]

### Luận điểm: lo ngại giảm giá bán là thừa, thực chất là thiếu cung

Tin Meta cho thuê ngoài tài nguyên tính toán làm dấy lên lo ngại bong bóng AI, cộng với tin tức báo chí về khả năng giảm giá bán đế trong nửa cuối năm, đã khiến Daeduck Electronics, Simmtech, Haesung DS điều chỉnh giá cổ phiếu mạnh. Nhận định của báo cáo là <strong>đợt điều chỉnh này thực ra là cơ hội mua</strong>, vì các IDM bộ nhớ đang ghi nhận biên lợi nhuận hoạt động cao không có động lực để giảm giá bán.

Logic cốt lõi là <strong>sự bào mòn năng lực sản xuất thực tế</strong>.

- Công suất đế đóng gói bộ nhớ đã đình trệ kể từ đợt mở rộng quy mô lớn năm 2020-2022.
- Nhưng khi đó sản phẩm chủ lực là DDR4, LPDDR4, còn hiện tại sản phẩm chủ lực là DDR5, LPDDR5/5X.
- Việc bộ nhớ nâng cao hiệu năng và die tăng kích thước khiến đế phải <strong>mở rộng diện tích, tăng số lớp</strong>, làm giảm số lượng đế có thể sản xuất trên cùng một công suất.
- Các hãng đế đóng gói hàng đầu như Unimicron, Samsung Electro-Mechanics tập trung mở rộng năng lực sản xuất FCBGA, sản phẩm biên lợi nhuận cao, khiến lo ngại về cân đối cung cầu đế BT toàn cầu càng lớn hơn.

Đã có một đợt tăng giá bán đế vào tháng 4/2026. Đây là phản ánh giá nguyên vật liệu như vàng, đồng tăng, nhưng báo cáo suy đoán rằng đợt tăng giá cũng phản ánh một phần lo ngại cung cầu nửa cuối năm. Nửa cuối năm còn có nguồn cung bộ nhớ thông thường cho NVIDIA Rubin và việc các hãng bộ nhớ Trung Quốc mở rộng xuất xưởng DDR5, nên nhu cầu đế sẽ còn tăng thêm. \[Suy luận: ước tính của báo cáo\]

### Điểm cần xác minh: tín hiệu thiếu hụt nguồn cung là LTA

Công cụ quan sát hữu ích nhất mà báo cáo đưa ra là <strong>việc ký kết LTA (hợp đồng cung ứng dài hạn)</strong>. Tháng 3/2020, Simmtech đã ký hợp đồng bán hàng, cung ứng đơn lẻ với Micron; trong ngành đế đóng gói vốn có thời hạn giao hàng ngắn, một hợp đồng quy mô lớn hơn 100 tỷ won là điều bất thường. Kể từ công bố đó, tình trạng thiếu cung thực tế trở nên trầm trọng hơn và thị trường bước vào chu kỳ tăng giá toàn diện. \[Thực tế: tiền lệ\]

Vì vậy hàm ý thực chiến của trục này rất rõ ràng. Thay vì mua cổ phiếu hưởng lợi trước, hãy kiểm tra trước <strong>công bố hợp đồng cung ứng, giá bán, tỷ lệ vận hành</strong>. Nếu xuất hiện công bố LTA, có thể đọc đó là tín hiệu bước vào chu kỳ tương tự năm 2020.

---

## Cảnh 2: bộ điều khiển eSSD, SK Hynix đã chọn xong đối tác

Báo cáo thứ hai là `ASICLAND: đối tác eSSD mà Hynix đã chọn` của chuyên viên phân tích Kwon Tae-woo, Hana Securities (ngày 8/7/2026). \[Thực tế: báo cáo Hana Securities\]

### Công ty và hợp đồng

ASICLAND (445090) là design house thành lập năm 2016, là công ty duy nhất trong nước sở hữu đồng thời tư cách thành viên TSMC VCA (Value Chain Alliance) và đối tác thiết kế toàn diện (Total Design Partner) của Arm. Hoạt động kinh doanh chia làm hai mảng: ASIC phi bộ nhớ (AI, HPC…) và bộ nhớ (eSSD, eMMC…), với hơn 80% nhân sự là kỹ sư.

Sự kiện then chốt là hợp đồng với SK Hynix.

- Ngày 29/6, công ty công bố hợp đồng hỗ trợ thiết kế và tape-out bộ điều khiển eSSD thế hệ mới với SK Hynix.
- Quy mô 31,9 tỷ won (43,7% doanh thu năm 2025), thời hạn từ 27/5/2025 đến 31/12/2027.
- Tape-out theo chuẩn PCIe Gen6, tiến trình 5nm, đã hoàn tất vào ngày 1/7.
- Kịch bản cơ sở là bắt đầu sản xuất hàng loạt năm 2028, nhưng lịch trình kiểm định được đặt thận trọng nên vẫn có khả năng đến sớm hơn.
- Điểm mấu chốt là đây không dừng ở khâu phát triển mà là <strong>cấu trúc hợp đồng nối thẳng sang sản xuất hàng loạt</strong>.

Việc SK Hynix chọn design house cho bộ điều khiển eSSD đã đi từ công ty A trong nước ở Gen4, GUC của Đài Loan ở Gen5, và nay đến <strong>ASICLAND ở Gen6</strong>. \[Thực tế: báo cáo\]

### Nhu cầu và kết quả kinh doanh

Nhu cầu eSSD từ trung tâm dữ liệu AI là trục tăng trưởng đã được xác nhận. Doanh thu cộng gộp của 5 hãng SSD doanh nghiệp hàng đầu toàn cầu trong 1Q26 đạt 18,46 tỷ USD, tăng 86,1% so với quý trước, mức cao nhất từ trước đến nay (TrendForce). Năm 2026 được dự báo là năm SSD doanh nghiệp vươn lên thành ứng dụng lớn nhất của NAND. \[Thực tế: TrendForce\]

Lộ trình sản xuất hàng loạt của ASICLAND cũng đang được kích hoạt tuần tự.

- Bộ điều khiển thẻ eMMC đã phát sinh doanh thu sản xuất hàng loạt, dự kiến mở rộng lên quy mô từ 40-50 tỷ won trở lên mỗi năm
- <strong>Bộ điều khiển Gen6 dành cho FADU, tiến trình 6nm, được kỳ vọng sản xuất hàng loạt vào nửa cuối năm 2027</strong>
- Dự án phát triển Gen7 kế tiếp có khả năng ký hợp đồng trong năm nay

Doanh thu 1Q26 đạt 54 tỷ won (+242,4% so với cùng kỳ năm trước), lỗ hoạt động thu hẹp còn 3 tỷ won. Khi hợp đồng lần này được phản ánh, hướng dẫn doanh thu năm 2026 được nâng từ 160 tỷ won lên 180 tỷ won, dự kiến chuyển sang có lãi cả năm. \[Thực tế: báo cáo\]

### Điểm cần xác minh: hợp đồng của ASICLAND không đồng nghĩa với doanh thu của FADU

Có một điểm cần tách bạch ở đây. Báo cáo đề cập <strong>bộ điều khiển Gen6 dành cho FADU sản xuất hàng loạt vào nửa cuối năm 2027</strong>, điều này liên quan trực tiếp đến vị thế hiện tại của FADU. Nhưng không có gì đảm bảo rằng hợp đồng của ASICLAND sẽ chuyển hóa thành nhu cầu khách hàng và doanh thu của FADU. ASICLAND là design house thiết kế bộ điều khiển, còn FADU là công ty bán SSD chứa bộ điều khiển đó. Vị trí của hai công ty trong chuỗi giá trị khác nhau. \[Suy luận: phân tách theo chuỗi giá trị\]

Vì vậy khi nhìn vào FADU, cần kiểm tra riêng <strong>đơn hàng chính thức và lịch trình ghi nhận doanh thu của FADU</strong>, chứ không phải công bố hợp đồng của ASICLAND. Hướng đi đã rõ, nhưng doanh thu là một sự kiện riêng biệt.

---

## Cảnh 3: bộ nhớ legacy, Trung Quốc lấp chỗ trống mà nhóm dẫn đầu bỏ lại

Báo cáo thứ ba là `GigaDevice: doanh nghiệp bộ nhớ legacy đang tăng trưởng nhờ khoảng trống nguồn cung toàn cầu` của chuyên viên phân tích Baek Seung-hye, Hana Securities (ngày 14/7/2026). \[Thực tế: báo cáo Hana Securities\]

### Công ty: cùng một cội rễ với CXMT

GigaDevice (603986) là doanh nghiệp dẫn đầu thị phần tại Trung Quốc ở các mảng DRAM legacy, SLC NAND Flash, NOR Flash và MCU. Đây là một công ty bộ nhớ khác do ông Zhu Yiming, nhà sáng lập CXMT (Changxin Memory), thành lập năm 2005; hiện ông Zhu kiêm nhiệm chức chủ tịch hội đồng quản trị của cả hai công ty. GigaDevice đầu tư cổ phần thiểu số 1,8% vào CXMT, còn CXMT gia công DRAM cho GigaDevice theo hợp đồng, tạo thành quan hệ hợp tác giữa hai bên. \[Thực tế: báo cáo\]

Sự phân công vai trò rất rõ ràng. <strong>CXMT tập trung vào DRAM thông dụng từ DDR5/LPDDR5 trở lên và HBM, còn GigaDevice phụ trách bộ nhớ đặc chủng như NOR Flash, SLC NAND, DRAM legacy từ DDR4/LPDDR4 trở xuống, và MCU</strong>. Nói cách khác, trong lúc CXMT đuổi theo nhóm dẫn đầu để đi lên, GigaDevice hấp thụ khoảng trống legacy ở phía dưới.

### Kết quả kinh doanh: bất ngờ do khoảng trống tạo ra

Kết quả kinh doanh sơ bộ 2Q26 thể hiện cấu trúc này bằng con số cụ thể.

- Doanh thu sơ bộ 7,3 tỷ NDT, tăng 226% so với cùng kỳ năm trước, vượt 46% so với dự báo đồng thuận
- Lợi nhuận ròng thuộc về cổ đông công ty mẹ 5,4 tỷ NDT, tăng 1.496% so với cùng kỳ năm trước, vượt 77% so với dự báo đồng thuận

Nguyên nhân của kết quả khả quan là ASP sản phẩm chủ lực tăng và thị phần mở rộng. Khi các hãng bộ nhớ hàng đầu toàn cầu tăng tỷ trọng sản xuất tập trung vào HBM, DDR5 và 3D NAND, cung cầu DRAM và NAND legacy trở nên eo hẹp; <strong>trong một năm gần đây, ASP của SLC NAND tại GigaDevice tăng khoảng 5 lần, ASP của DRAM legacy tăng khoảng 10 lần</strong>. \[Thực tế: báo cáo\]

### Chất xúc tác nửa cuối năm và điểm cần xác minh

Động lực tăng trong nửa cuối năm đến từ hai yếu tố. Thứ nhất, việc Kioxia và Micron cắt giảm sản xuất hàng loạt NAND legacy khiến đà tăng giá SLC NAND tiếp diễn. Nhờ hợp tác với CXMT, GigaDevice là một trong số ít doanh nghiệp có thể mở rộng năng lực sản xuất DDR4 trong 2-3 năm tới. Mục tiêu là nâng thị phần NOR Flash toàn cầu từ khoảng 20% hiện nay lên 25% trong 3-5 năm. Thứ hai là xuất xưởng số lượng lớn DRAM 3D tùy biến. Các loại DRAM tùy biến liên quan đến AI như cockpit thông minh ô tô, AI PC, robot được dự báo sẽ đóng góp vào doanh thu từ nửa cuối năm 2026. \[Suy luận: triển vọng theo báo cáo\]

Ý nghĩa kép của báo cáo này chính là điểm cần xác minh. Đà tăng trưởng vượt bậc của GigaDevice vừa là <strong>bằng chứng cho thấy phạm vi của chu kỳ bùng nổ bộ nhớ đã mở rộng, vừa là dữ liệu để xác nhận tốc độ các doanh nghiệp Trung Quốc lấp đầy khoảng trống</strong>. Tốc độ Trung Quốc lấp chỗ trống mà nhóm dẫn đầu bỏ lại nhanh đến đâu cũng ảnh hưởng đến trần giá legacy của các doanh nghiệp bộ nhớ Hàn Quốc. Đây là mạch logic tương tự luận điểm về trần giá DRAM client đã đề cập trong [IPO của CXMT và rủi ro giá bộ nhớ](/vi/post/cxmt-ipo-memory-price-risk-hbm-client-dram-2026-06-21/).

---

## Tổng hợp: chu kỳ bùng nổ đã mở rộng, và ba nút xác nhận

Đọc chồng ba báo cáo lên nhau, kết luận chỉ có một. <strong>Chu kỳ bùng nổ bộ nhớ giờ không còn là câu chuyện riêng của HBM.</strong> Ba ông lớn dẫn đầu càng tập trung nguồn lực vào HBM và DDR5, khoảng trống nguồn cung càng xuất hiện ở bên cạnh và bên dưới, và khoảng trống đó tạo ra những đối tượng hưởng lợi riêng. Đế đóng gói, bộ điều khiển eSSD và bộ nhớ legacy mỗi thứ đi theo chu kỳ của riêng mình.

Tuy nhiên cả ba trục đều có <strong>nút xác nhận nằm giữa câu chuyện và doanh thu thực tế</strong>.

| Trục | Câu chuyện | Nút xác nhận cần bấm |
|---|---|---|
| Đế đóng gói | Diện tích lớn, số lớp cao bào mòn công suất thực tế | Công bố LTA, giá bán, tỷ lệ vận hành |
| Bộ điều khiển eSSD | SK Hynix chọn Gen6, chuyển sang sản xuất hàng loạt | Đơn hàng chính thức và lịch trình ghi nhận doanh thu của FADU |
| Bộ nhớ legacy | Trung Quốc hấp thụ khoảng trống của nhóm dẫn đầu, ASP tăng vọt | Tốc độ Trung Quốc lấp đầy khoảng trống |

Nói cách khác, ba báo cáo này không phải là <strong>tín hiệu bảo mua cổ phiếu hưởng lợi trước</strong>, mà là <strong>tấm bản đồ cho biết cần kiểm tra điều gì để nhận diện thời điểm bước vào chu kỳ</strong>. Có xuất hiện công bố LTA hay không, doanh thu của FADU có thực sự được ghi nhận hay không, việc Trung Quốc mở rộng công suất legacy có kéo giá đi xuống trở lại hay không. Ba nút này cho biết điểm mà câu chuyện chuyển hóa thành sự thật.

---

_Bài viết này tổng hợp nội dung chi tiết của ba báo cáo công khai từ Hana Securities (ngày 3/7/2026 về đế đóng gói bộ nhớ, ngày 8/7/2026 về ASICLAND, ngày 14/7/2026 về GigaDevice) thành một khung phân tích duy nhất. Mục tiêu và triển vọng được trích dẫn là quan điểm của công ty chứng khoán đó; các cổ phiếu được đề cập là ví dụ minh họa cấu trúc ngành, không phải khuyến nghị mua hoặc bán một cổ phiếu cụ thể. Số liệu và triển vọng trong báo cáo tính đến thời điểm công bố và có thể thay đổi sau đó. Quyết định đầu tư và trách nhiệm thuộc về nhà đầu tư._

---

### Bài viết liên quan

- [SK Hynix cắt giảm lợi nhuận Q2 nhưng giữ nguyên giá mục tiêu: tổng hợp báo cáo Mirae Asset và KIS](/vi/post/sk-hynix-2q-earnings-cut-mirae-kis-lta-target-price-2026-07-14/)
- [IPO của CXMT và rủi ro giá bộ nhớ: HBM không phải nơi gãy đầu tiên](/vi/post/cxmt-ipo-memory-price-risk-hbm-client-dram-2026-06-21/)
- [FADU 2Q26: có thể vượt kỳ vọng, nhưng chưa phải cú sốc lớn](/vi/post/fadu-2q26-earnings-preview-essd-controller-moderate-beat-2026-07-04/)
- [Luận Điểm AI PCB và Substrate: Nhu Cầu GPU, CPU, NIC và CCL Là Một Nút Thắt Cổ Chai Chung Của Toàn Hệ Thống](/vi/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/)
- [Nghiên cứu chuyên sâu cung-cầu HBM 2030: mổ xẻ mô hình cầu 26,7EB đối chiếu với lịch trình mở rộng công suất](/vi/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/)
