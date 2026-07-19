---
title: "Mở Rộng Sản Xuất NVIDIA Vera CPU và Simmtech: SoCAMM2 Là Về Đơn Vị Module, Không Phải Bit"
slug: "nvidia-vera-cpu-socamm2-simmtech-module-unit-thesis-2026-07-19"
date: 2026-07-19T18:05:00+09:00
description: "Khi NVIDIA mở rộng Vera CPU sang NVL72 và máy chủ độc lập, chúng tôi xác minh liệu giảm dung lượng SoCAMM2 có phủ định với Simmtech. Kết nối các tài liệu chính thức của NVIDIA, TrendForce, SK Hynix và Simmtech cùng với giá cổ phiếu ngày 16 tháng 7, cung-cầu và sự đồng thuận để thiết lập logic đầu tư dựa trên đơn vị module và điều kiện vào cửa."
categories: ["Phân tích độc quyền", "Phân tích công nghệ", "Cổ phiếu"]
tags:
  - "Simmtech"
  - "NVIDIA"
  - "Vera CPU"
  - "Vera Rubin"
  - "SoCAMM2"
  - "LPDDR5X"
  - "Máy chủ AI"
  - "Bảng mạch Module Bộ nhớ"
  - "Cơ sở hạ tầng bán dẫn"
  - "Cung và cầu"
series: ["exclusive-analysis", "ai-hbm-2026"]
valley_cashtags:
  - 심텍
draft: false
---

Một NVL72 NVIDIA Vera Rubin chứa 36 CPU Vera và 54TB bộ nhớ LPDDR5X. Đó là 1,5TB trên mỗi CPU. Tuy nhiên, vào tháng Sáu, TrendForce báo cáo rằng NVIDIA sẽ giảm một nửa dung lượng của các module Vera SoCAMM thế hệ tiếp theo trong khi tăng tổng số lô hàng module và sản xuất CPU Vera.

Nhìn bề ngoài, giảm dung lượng bộ nhớ có vẻ tiêu cực với các nhà cung cấp thành phần. Khi đo nhu cầu PCB thuần túy theo bit, nó là. Tuy nhiên, những gì Simmtech sản xuất không phải là chip DRAM mà là PCB cho các module SoCAMM. Khối lượng của Simmtech nhạy cảm hơn với số lượng CPU được sản xuất và số lượng module hơn là tổng dung lượng bộ nhớ. Ngay cả khi thiếu LPDDR buộc giảm dung lượng trên mỗi CPU, nếu NVIDIA vận chuyển nhiều CPU Vera và module hơn, nhu cầu PCB có thể không giảm.

Nhìn vào các tài liệu chính thức, nghiên cứu ngành, ước tính của nhà phân tích và giá cổ phiếu thực tế cũng như dữ liệu cung-cầu cho thấy logic kinh doanh vẫn nguyên vẹn, nhưng đáy giá chưa được xác nhận.

> Ngữ Cảnh Kết Nối
> Bài viết này là tiếp nối của [Luận án đầu tư cơ sở hạ tầng và PCB AI: Hệ thống BOM như một tắc nghẽn chung](/post/ai-pcb-thesis-system-bom-common-bottleneck-2026-05-05/), [Hệ sinh thái PCB AI Hàn Quốc: mười công ty](/post/korea-ai-pcb-ecosystem-ten-companies-2026-05-05/), [Xác minh bảng vật liệu Vera Rubin VR200](/post/vera-rubin-vr200-bom-memory-pcb-mlcc-korea-alpha-2026-05-21/), và [Khoảng trống cung cấp bộ nhớ tràn ra ngoài HBM](/post/memory-supply-gap-spillover-substrate-essd-legacy-hana-three-reports-2026-07-14/). Các bài viết liên quan có thể được tìm thấy trong [trung tâm cơ sở hạ tầng và PCB AI](/page/korea-ai-pcb-substrate-hub/), [trung tâm HBM AI](/page/korea-semiconductor-hbm-kospi-hub/), và [trung tâm phân tích độc quyền](/page/exclusive-analysis-hub/).

## TL;DR

* Thông số kỹ thuật chính thức của NVIDIA cho thấy Vera Rubin NVL72 sử dụng 36 CPU Vera và 54TB LPDDR5X. Các giá để máy chủ Vera CPU độc lập hỗ trợ tối đa 4 nút trên mỗi khay 1U, mở rộng đến tối đa 256 CPU trên mỗi giá. Sự tiến hóa của Vera từ một CPU hỗ trợ trong các giá GPU sang một nền tảng máy chủ độc lập được xác nhận.
* Giảm dung lượng SoCAMM được báo cáo của TrendForce là một phản ứng đối với thiếu hụt cung cấp LPDDR, không phải yêu cầu giảm tốc. NVIDIA dự định giảm dung lượng trên mỗi module trong khi tăng tổng số lô hàng module và sản xuất CPU Vera.
* Simmtech liệt kê PCB SoCAMM trên trang sản phẩm chính thức của mình. Tuy nhiên, cung cấp đồng thời từ ba nhà cung cấp bộ nhớ và thị phần cao là ước tính của nhà phân tích, không phải tiết lộ của công ty. Doanh thu và thị phần khách hàng cụ thể thực tế vẫn chưa được công bố.
* Vào ngày 16 tháng 7, Simmtech đóng cửa ở mức 107.400 KRW, giảm 11,68% trong một ngày duy nhất. Trong 20 ngày giao dịch, các tổ chức mua ròng 236,2 tỷ KRW, và tiền thực (hưu trí, quỹ tương hỗ, bảo hiểm) mua 186,4 tỷ KRW, trong khi nhà đầu tư nước ngoài bán 161,1 tỷ KRW và chương trình bán 185,9 tỷ KRW. Áp lực mua của các tổ chức trung hạn va chạm với áp lực bán ngắn hạn.
* PER 2026E của 27,1x không rẻ. Áp dụng EPS kỳ vọng 2027E là 6.655 KRW cho lợi suất 16,1x, nhưng chỉ khi doanh thu SoCAMM và lợi nhuận ròng mở rộng như kế hoạch.
* Phán quyết là **Mua có điều kiện**. Một phương pháp an toàn hơn xác nhận hỗ trợ gần 104.000 KRW với việc giảm bán nước ngoài và chương trình, hoặc phục hồi qua 113.800 KRW trên khối lượng tăng.

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Phán quyết của Bài Viết Này</div>
  <div class="thesis-callout__body">
    Kết nối trực tiếp giảm dung lượng SoCAMM2 với sự suy giảm nhu cầu PCB Simmtech sử dụng đơn vị sai. Công thức doanh thu của Simmtech tiếp cận CPU Vera × module trên mỗi CPU × PCB trên mỗi module × thị phần Simmtech nhiều hơn số lượng bit DRAM. Tuy nhiên, hai mục cuối cùng trong công thức này chưa được xác nhận bởi các tiết lộ công ty.
  </div>
</div>

---

## 1. Những Con Số Để Loại Bỏ và Những Con Số Để Giữ Lại

Quy mô thị trường CPU máy chủ năm 2030 là 170 tỷ đô la, tỷ lệ CPU-to-GPU 1:1 và thiếu hụt DRAM năm 2027 xuất hiện trong phân tích đính kèm đã được phản ánh trong các tuyên bố chính thức từ nhiều công ty môi giới và các bài thuyết trình của công ty. Chúng hữu ích để hiểu hướng của ngành nhưng không phải là nguồn lợi nhuận vượt mức cụ thể cho Simmtech.

Bốn con số quan trọng hơn khi đánh giá Simmtech:

| Mục | Tại Sao Nó Quan Trọng |
|---|---|
| CPU Vera được vận chuyển | Xác định cơ sở được cài đặt cho nền tảng SoCAMM |
| Module SoCAMM trên mỗi CPU | Biến khối lượng trực tiếp cho các PCB module Simmtech |
| Thị phần cung cấp khách hàng cụ thể của Simmtech | Xác định phần của Simmtech trong tăng trưởng ngành |
| Giá và chi phí PCB module | Xác định tốc độ mà tăng trưởng doanh thu chuyển đổi thành lợi nhuận hoạt động |

Sử dụng giả định từ 5 đến 6 triệu CPU Vera và 8 module trên mỗi CPU cho kết quả 40 đến 48 triệu module hàng năm. Với 5,5 triệu đơn vị, đó là 44 triệu module. Tuy nhiên, phép tính này không phải là kế hoạch vận chuyển chính thức của NVIDIA. Đó là một kịch bản dẫn xuất từ các ước tính vận chuyển CPU của nhà phân tích và ngành cũng như cấu hình hệ thống được công bố công khai.

Do đó, hình 44 triệu đơn vị không nên được sử dụng trực tiếp làm dự báo doanh thu. Nó chỉ là một ví dụ để đánh giá độ lớn của đơn hàng.

## 2. Các Tài Liệu Chính Thức của NVIDIA Xác Nhận Đường Mở Rộng của Vera

### 2.1 NVL72 Chứa 36 CPU Vera

[Trang chính thức Vera Rubin NVL72](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/) của NVIDIA trình bày cấu hình sau:

| Mục | Thông Số Kỹ Thuật Chính Thức |
|---|---:|
| Rubin GPU | 72 |
| CPU Vera | 36 |
| Bộ Nhớ CPU | LPDDR5X 54TB |
| Bộ Nhớ trên mỗi CPU Vera | 1,5TB |
| Lõi CPU Vera | 88 |

Cấu trúc không đơn giản là một CPU cho mỗi GPU. Trong NVL72, một CPU Vera hỗ trợ hai GPU. Tuy nhiên, một giá 72-GPU duy nhất yêu cầu 36 CPU. Điều này cho thấy rằng lớp CPU và LPDDR đã tăng lên thành các thành phần chính trong cấu trúc chi phí hệ thống AI.

### 2.2 Vera Bán Ngoài Các Giá GPU

Thay đổi quan trọng hơn là hệ thống CPU Vera độc lập. [Blog kỹ thuật của NVIDIA](https://developer.nvidia.com/blog/?p=114004) giải thích rằng các giá CPU Vera có thể chứa tối đa 4 nút trên mỗi khay 1U và mở rộng quy mô thành 256 CPU Vera trên mỗi giá. Các hệ thống socket đơn và song song hỗ trợ tối đa 1,5TB LPDDR5X trên mỗi socket.

NVIDIA thông báo rằng Cisco, Dell, HPE, Lenovo và Supermicro có kế hoạch khởi chạy các hệ thống dựa trên Vera trong nửa sau năm 2026. Nếu lịch trình giữ, các nguồn nhu cầu Vera mở rộng ngoài các khối lượng lắp ráp NVL72.

```text
Các Nguồn Nhu Cầu Vera

Lớp CPU trong Vera Rubin NVL72
+ Máy chủ CPU Vera độc lập
+ Giá CPU cho suy luận và tác nhân
+ Hệ thống socket đơn và song song từ các OEM lớn
```

Đó là lý do tại sao logic đầu tư của Simmtech không phụ thuộc vào sản lượng lắp ráp giá GPU một mình. Sự mở rộng của các hệ thống CPU độc lập mở rộng cơ sở nhu cầu cho các module SoCAMM và PCB.

## 3. Giảm Dung Lượng SoCAMM Có Nghĩa Là Gì?

[Phân tích của TrendForce vào ngày 10 tháng 6 năm 2026](https://www.trendforce.com/presscenter/news/20260610-13090.html) phát hiện ra rằng chỉ khoảng 60% yêu cầu LPDRAM năm 2027 của NVIDIA có thể được đáp ứng bằng các phân bổ dành riêng. Để giải quyết thiếu hụt cung cấp, NVIDIA được báo cáo đã chọn các điều chỉnh sau:

1. Giảm dung lượng bộ nhớ của mỗi module SoCAMM cho Vera.
2. Tăng tổng số lô hàng module.
3. Sản xuất nhiều CPU Vera hơn với cùng một cung cấp LPDRAM.
4. Tăng độ thâm nhập thị trường của các giá CPU Vera độc lập.

Trong cấu trúc này, hai loại nhu cầu có thể chuyển động theo hướng khác nhau.

| Đơn Vị Nhu Cầu | Tác Động của Giảm Dung Lượng |
|---|---|
| Bit DRAM và GB | Dung lượng được cài đặt trên mỗi CPU có thể giảm |
| Module SoCAMM | Có thể tăng nếu tăng trưởng vận chuyển CPU vượt quá giảm dung lượng |
| PCB Module | Tỷ lệ thuận với module, vì vậy có thể tăng |
| Socket, kết nối, kiểm tra module | Tăng với số lượng module |

Biểu thị điều này theo thuật ngữ Simmtech cho công thức sau:

```text
Khối Lượng PCB SoCAMM Simmtech
= Vận Chuyển CPU Vera
× Module SoCAMM trên mỗi CPU
× PCB trên mỗi module
× Thị phần cung cấp Simmtech
```

Ngược lại, doanh thu SoCAMM của nhà cung cấp bộ nhớ xấp xỉ số lượng CPU × GB được cài đặt trên mỗi CPU × giá trên mỗi GB. Tin tức tương tự có thể có những tác động khác nhau đối với các nhà cung cấp DRAM và nhà cung cấp PCB module.

### Sự Không Khớp Giữa Thông Số Kỹ Thuật Chính Thức và Báo Cáo của TrendForce

Trang chính thức hiện tại của NVIDIA hiển thị tối đa 1,5TB LPDDR5X trên mỗi CPU Vera. TrendForce báo cáo giảm dung lượng module thế hệ tiếp theo. Với cả hai tài liệu tồn tại đồng thời, chưa chắc chắn trường hợp nào áp dụng:

* Trang của NVIDIA tiếp tục hiển thị cấu hình tối đa hoặc thiết kế hiện có
* Giảm dung lượng chỉ áp dụng cho khách hàng cụ thể hoặc cấu hình sản phẩm
* Thông số kỹ thuật sản xuất cuối cùng chưa được hoàn thiện

Sự không nhất quán này không phải là tiếng ồn bị che giấu mà là mục để xác minh để đánh giá đầu tư. Dung lượng thực tế trên mỗi module, module trên mỗi CPU và cấu hình khách hàng cụ thể của các hệ thống sản xuất phải được xác minh thông qua các sản phẩm được khởi chạy và tiết lộ của công ty.

## 4. Simmtech Cung Cấp Gì trong SoCAMM2?

### 4.1 Những Gì Công Ty Chính Thức Xác Nhận

[Trang sản phẩm chính thức của Simmtech](https://www.simmtech.com/product/board06.aspx) phân loại PCB SoCAMM là một sản phẩm module bộ nhớ thế hệ tiếp theo cho AI. Các thông số kỹ thuật chính được trình bày bởi công ty như sau:

| Mục | Mô Tả Chính Thức của Simmtech |
|---|---|
| Bộ Nhớ Cơ Bản | LPDDR |
| Ứng Dụng | Module bộ nhớ thế hệ tiếp theo cho AI |
| Số Lớp | 10–12 lớp |
| Yêu Cầu Chính | Hằng số điện môi thấp và tổn hao, hệ số giãn nở nhiệt thấp, kiểm soát trở kháng |
| Xử Lý Bề Mặt | Selective ENIG |

Xác nhận rằng PCB SoCAMM xuất hiện trên danh sách sản phẩm của Simmtech được thiết lập. Công ty cũng sản xuất các PCB module bộ nhớ chung và các cơ sở package bộ nhớ. Khi nhu cầu LPDDR máy chủ AI phát triển trong cả module và package, công ty có nền tảng sản phẩm để phản ứng.

### 4.2 Những Gì Chỉ Được Xác Nhận Bởi Ước Tính Nhà Phân Tích

Tuyên bố rằng Simmtech tham gia sản xuất SoCAMM2 từ Samsung Electronics, SK Hynix và Micron đồng thời và giữ thị phần cao không phải là tiết lộ của công ty. Đó là một phân tích và ước tính thị trường trong [báo cáo môi giới được đăng trên trang chủ của Simmtech](https://www.simmtech.com/upload/media/file/639179687810021917.pdf).

Do đó, những biểu thức này phải được phân biệt:

| Biểu Thức | Mức Độ Bằng Chứng |
|---|---|
| Simmtech sở hữu sản phẩm PCB SoCAMM | Xác nhận chính thức của công ty |
| Simmtech tham gia sản xuất SoCAMM2 từ ba nhà cung cấp bộ nhớ | Ước tính nhà phân tích |
| Simmtech giữ thị phần cung cấp #1 | Ước tính nhà phân tích |
| Doanh thu và thị phần khách hàng cụ thể | Chưa được công bố |
| Thời gian chính xác của đóng góp SoCAMM đối với lợi nhuận Simmtech | Chưa được công bố |

Sự phân biệt này là cần thiết vì xác định khách hàng và khối lượng sản xuất thúc đẩy kinh tế của kinh doanh cơ sở hạ tầng. Khả năng sản xuất một sản phẩm và duy trì thị phần cao cho doanh thu lặp lại được tách ra bằng các giai đoạn xác định khách hàng, năng suất, giá đơn vị và tỷ lệ sử dụng.

### 4.3 Sản Xuất Hàng Loạt của SK Hynix Xác Nhận Thực Tế Nền Tảng

Theo [thông báo chính thức của SK Hynix](https://news.skhynix.com/mass-production-socamm2-192gb/), công ty bắt đầu sản xuất hàng loạt SoCAMM2 192GB sử dụng LPDDR5X 1cnm vào tháng 4 năm 2026. Sản phẩm hướng tới nền tảng NVIDIA Vera Rubin.

Điều này cho thấy rằng SoCAMM2 không phải là một dự án nghiên cứu dài hạn mà đã vào sản xuất hàng loạt thực tế. Tuy nhiên, sản xuất module hàng loạt của SK Hynix không tự động chứng minh khối lượng cung cấp khách hàng cụ thể của Simmtech. Simmtech chứng minh doanh thu SoCAMM, hỗn hợp bảng lớp cao và cải thiện tỷ lệ sử dụng trong kết quả quý thứ hai và thứ ba là cần thiết riêng biệt.

## 5. Kết Quả Đang Phục Hồi Nhưng Vẫn Ở Giai Đoạn Chứng Minh Kỳ Vọng

Simmtech ghi nhận doanh thu năm 2025 toàn năm là 1,41 nghìn tỷ KRW và lợi nhuận hoạt động 11,9 tỷ KRW, với lỗ ròng 164,2 tỷ KRW. Trong quý 1 năm 2026, doanh thu hợp nhất phục hồi lên khoảng 422,4 tỷ KRW và lợi nhuận hoạt động lên khoảng 13,7 tỷ KRW. Sự đồng thuận quý 2 kỳ vọng tốc độ phục hồi nhanh hơn.

| Mục | Thực Tế Quý 1/2026 | Đồng Thuận Quý 2/2026 | Thay Đổi Tuần Tự |
|---|---:|---:|---:|
| Doanh Thu | \~422,4 tỷ KRW | 466,9 tỷ KRW | \~+10,5% |
| Lợi Nhuận Hoạt Động | \~13,7 tỷ KRW | 47,3 tỷ KRW | \~+245% |
| Biên Lợi Nhuận Hoạt Động | \~3,2% | \~10,1% | +6,9 điểm phần trăm |

Kết quả quý 1 thực tế từ [báo cáo quý của Simmtech](https://kind.krx.co.kr/external/2026/05/14/000890/20260514001959/11013.htm); ước tính quý 2 từ đồng thuận Naver và WiseReport được thu thập bởi cơ sở dữ liệu địa phương của Research OS vào ngày 16 tháng 7.

Tăng trưởng lợi nhuận hoạt động vượt xa tăng trưởng doanh thu. Điều này chỉ ra nhu cầu tăng đồng thời hỗn hợp sản phẩm lợi nhuận cao, sử dụng nhà máy và hấp thụ chi phí cố định. Ngay cả khi khối lượng SoCAMM tăng, biên lợi nhuận có thể giảm dưới kỳ vọng do chi phí vật liệu thô và mạ vàng, năng suất ban đầu và đàm phán giá cụ thể với khách hàng.

### Đường Lợi Nhuận Do Đồng Thuận Hàng Năm Yêu Cầu

| Năm | Doanh Thu | Lợi Nhuận Hoạt Động | Thu Nhập Ròng | EPS | PER 2026E (Đóng cửa ngày 16 tháng 7) |
|---|---:|---:|---:|---:|---:|
| 2026E | 1.932 nghìn tỷ KRW | 189,6 tỷ KRW | 149,3 tỷ KRW | 3.968 KRW | 27,1x |
| 2027E | 2.289 nghìn tỷ KRW | Không có đồng thuận tổng hợp | 251,0 tỷ KRW | 6.655 KRW | 16,1x |
| 2028E | 2.566 nghìn tỷ KRW | Không có đồng thuận tổng hợp | 322,8 tỷ KRW | 8.588 KRW | 12,5x |

Để giá cổ phiếu hiện tại trông rẻ, thu nhập năm 2027 và 2028 phải thực sự hình thành. PER 2026E hiện tại là 27,1x và PBR là 5,64x phản ánh đáng kể phục hồi sớm. Mục tiêu giá trung bình là 171.250 KRW cao hơn giá hiện tại 59,5%, nhưng khi các mục tiêu tăng nhanh chóng, chúng rất khó sử dụng làm biên an toàn.

## 6. Giá Cổ Phiếu Ngày 16 Tháng 7: Sốc Giảm Nhưng Phục Hồi Xu Hướng Chưa Được Xác Nhận

Simmtech đóng cửa ở mức 107.400 KRW vào ngày 16 tháng 7, giảm 11,68% vào ngày hôm đó với mức thấp trong ngày là 103.700 KRW. Đây là 34,6% thấp hơn mức cao ngày 1 tháng 7 là 164.200 KRW.

| Thời Kỳ và Chỉ Báo | Giá Trị |
|---|---:|
| Lợi Suất 1 ngày | -11,68% |
| 5 ngày | -8,91% |
| 10 ngày | -13,87% |
| 20 ngày | -15,76% |
| 60 ngày | +40,94% |
| 120 ngày | +109,77% |
| so với MA 5 ngày | -5,42% |
| so với MA 20 ngày | -12,28% |
| so với MA 60 ngày | -4,48% |
| so với MA 120 ngày | +27,39% |
| RSI14 | 44,4 |

RSI đã thoát khỏi lãnh thổ quá mua. Tuy nhiên, giá vẫn dưới các đường trung bình động 5 ngày, 20 ngày và 60 ngày. Vì nó cao hơn 27% so với dòng 120 ngày, toàn bộ lợi suất từ lông chuyển động dài hạn chưa biến mất. Cả "suy giảm sắc nét có nghĩa là rẻ" và "xu hướng đã phục hồi" chưa thể được xác nhận.

Trên cơ sở giao dịch, mức thấp ngày 14 tháng 7 là 99.600 KRW và mức thấp ngày 16 tháng 7 là 103.700 KRW đại diện cho vùng hỗ trợ đầu tiên. Mức 113.800 KRW xác nhận liệu hỗ trợ ngắn hạn bị phá vỡ có phục hồi; 121.600 đến 124.000 KRW là một vùng kháng cự nơi đóng cửa ngày 15 tháng 7 và trung bình động 20 ngày trùng lặp.

## 7. Cung và Cầu: Các Tổ Chức Mua Nhưng Nhà Đầu Tư Nước Ngoài và Chương Trình Vẫn Bán

Các số tiền mua ròng tích lũy cho đến ngày 16 tháng 7 từ cơ sở dữ liệu địa phương Kiwoom của Research OS như sau. Các đơn vị tính bằng tỷ KRW.

| Thời Kỳ | Nước Ngoài | Tổ Chức | Cá Nhân | Tiền Thực | Chương Trình |
|---|---:|---:|---:|---:|---:|
| 1 ngày | -9,83 | -5,88 | +15,57 | -5,91 | -11,55 |
| 5 ngày | -25,79 | +6,02 | +18,95 | +7,98 | -28,71 |
| 10 ngày | -93,39 | +80,32 | +11,79 | +75,77 | -40,78 |
| 20 ngày | -161,09 | +236,21 | -84,25 | +186,44 | -185,94 |

Tiền thực là tổng các quỹ hưu trí, quỹ tương hỗ và bảo hiểm. Bảng này tiết lộ hai điều đồng thời.

Thứ nhất, trên cơ sở 20 ngày, mua của các tổ chức và tiền thực là đáng kể. Trong quá trình điều chỉnh sau đỉnh, vốn dài hạn hướng nội bộ hấp thụ khối lượng.

Thứ hai, bán của nhà đầu tư nước ngoài và chương trình đã tiếp tục ở cùng một quy mô. Khi ngã giá ngày 16 tháng 7, nhà đầu tư nước ngoài và các tổ chức bán cùng nhau trong khi các cá nhân hấp thụ 15,57 tỷ KRW. Thật khó để đánh giá đáy được xác nhận chỉ bằng mua của các tổ chức.

Thị phần giao dịch bán khống cũng tăng lên 21,2% vào ngày 16 tháng 7. Trung bình 20 ngày là 9,3%. Kho hàng hoàn lại bán khống là khoảng 5,48 triệu cổ phiếu hoặc 14,6% của cổ phiếu được phát hành, nhưng không phải tất cả kho hàng hoàn lại bán khống là kho hàng bán khống. Con số này chỉ nên được tham khảo như một tham chiếu cho khối lượng bán có sẵn.

## 8. Simmtech Được Xem Xét Lại Thông Qua P × Q × C

### P: Giá Đơn Vị của PCB SoCAMM Lớp Cao

PCB SoCAMM yêu cầu 10–12 lớp, tổn hao điện môi thấp, giãn nở nhiệt thấp và kiểm soát trở kháng chính xác. Độ khó sản xuất cao hơn so với PCB module bộ nhớ chung có thể giúp cải thiện hỗn hợp sản phẩm. Tuy nhiên, giá đơn vị và cấu trúc tăng giá cụ thể của khách hàng không được công bố.

### Q: Số Lượng CPU Vera và Module SoCAMM

Q là biến lợi suất tăng lên lớn nhất. Ngoài sản xuất hàng loạt NVL72, các giá CPU Vera độc lập và máy chủ OEM lớn dự kiến cho nửa sau năm 2026. Nếu NVIDIA tuân theo báo cáo của TrendForce trong việc giảm dung lượng trên mỗi module trong khi tăng số lô hàng module, Q của Simmtech có thể phát triển nhanh hơn số lượng bit DRAM.

### C: Vật Liệu Thô, Mạ Vàng, Năng Suất, Sử Dụng

Mục xác định liệu tăng trưởng doanh thu có chuyển đổi thành lợi nhuận hoạt động. PCB nhạy cảm với giá vàng và đồng, vật liệu BT, chi phí mạ và năng suất ban đầu. Để đạt được biên lợi nhuận hoạt động 10,1% được đồng thuận cho Q2, tăng sản phẩm lợi nhuận cao và chuyển chi phí phải được xác nhận cùng nhau.

## 9. Ba Kịch Bản

| Kịch Bản | Điều Kiện | Giải Thích Thu Nhập và Giá |
|---|---|---|
| Tăng Giá | Vera Rubin và máy chủ CPU độc lập vận chuyển theo lịch trình; tổng số module SoCAMM tăng; Simmtech duy trì thị phần nhà cung cấp bộ nhớ ba | EPS 2027E là 6.655 KRW hoặc cao hơn trở nên khả thi và biện minh cho PER dẫn đầu là \~16x |
| Cơ Sở | Vận chuyển Vera phát triển nhưng thiếu hụt LPDDR và các ramp khách hàng cụ thể không khớp; thị phần và biên lợi nhuận Simmtech vẫn ở mức đồng thuận | Tăng trưởng kinh doanh vẫn có giá trị nhưng cổ phiếu có thể dao động rộng dựa trên thu nhập và cung-cầu |
| Giảm Giá | Vera hoặc SoCAMM sản xuất hàng loạt bị trì hoãn; giảm dung lượng trên mỗi module không dẫn đến tăng số lượng module; thị phần hoặc năng suất Simmtech kém diễn biến | PER 2026E là 27x trở thành gánh nặng và xác suất tái bước vào mức thấp tháng 7 tăng |

Trong các kịch bản này, biến quan trọng nhất không phải là thị trường CPU máy chủ 170 tỷ đô la. Đó là khối lượng vận chuyển thực tế của Simmtech, doanh thu khách hàng cụ thể, hỗn hợp bảng lớp cao và biên lợi nhuận hoạt động. Ngay cả khi các con số ngành lớn chứng minh đúng, nếu phần dành cho công ty là nhỏ, cổ phiếu sẽ gặp khó khăn.

## 10. Phán Quyết Đầu Tư và Chuỗi Xác Minh

### Phán Quyết: Mua Có Điều Kiện

Logic kinh doanh đã trở nên rõ ràng hơn. Các tài liệu chính thức của NVIDIA xác nhận sự mở rộng máy chủ độc lập của Vera, và báo cáo của TrendForce cho thấy giảm dung lượng là một phản ứng đối với thiếu hụt cung cấp, không phải suy giảm nhu cầu. Simmtech chính thức sở hữu sản phẩm PCB SoCAMM.

Tuy nhiên, cổ phiếu vẫn chịu áp lực từ bán của nhà đầu tư nước ngoài và chương trình, và nó không rẻ trên cơ sở thu nhập 2026. Do đó, tốt hơn là xem xét hai đường vào.

| Đường | Điều Kiện Xác Minh |
|---|---|
| Xác Nhận Hỗ Trợ | Giữ mức thấp giữa 103.700–106.000 KRW và xác nhận việc làm dịu bán của nhà đầu tư nước ngoài và chương trình |
| Xác Nhận Xu Hướng | Phục hồi qua 113.800 KRW trên khối lượng tăng với các tổ chức hoặc nhà đầu tư nước ngoài chuyển sang mua ròng |

Phục hồi qua 121.600–124.000 KRW sẽ đảo ngược đáng kể tổn thương xu hướng gần đây. Ngược lại, phá vỡ dưới 99.600 KRW trên cơ sở đóng cửa mà không phục hồi sẽ yêu cầu đánh giá lại giả thuyết giá.

### Những Động Lực

* Đạt được doanh thu 466,9 tỷ KRW và lợi nhuận hoạt động 47,3 tỷ KRW trong thu nhập 2Q26
* Bình luận của công ty về doanh thu SoCAMM, hỗn hợp bảng lớp cao và tỷ lệ sử dụng
* Khởi chạy thực tế của máy chủ dựa trên Vera từ OEM trong nửa sau năm 2026
* Thông số kỹ thuật sản xuất cuối cùng của NVIDIA và sự mở rộng vận chuyển giá CPU Vera độc lập
* Cập nhật sản xuất hàng loạt và xác định khách hàng từ SK Hynix, Samsung Electronics và Micron cho SoCAMM2

### Điều Kiện Vô Hiệu Hóa

* Lặp lại các đơn hàng không tuân theo khối lượng SoCAMM ban đầu
* Giảm dung lượng trên mỗi module không chuyển thành tăng tổng số lô hàng module
* Thị phần thị trường khách hàng cụ thể của Simmtech xác nhận dưới ước tính nhà phân tích
* Lợi nhuận hoạt động Q2 hiện vật bỏ lỡ sự đồng thuận với gánh nặng vật liệu thô và năng suất tái diễn
* Vera Rubin hoặc khởi chạy hệ thống CPU Vera độc lập bị trì hoãn đáng kể
* 99.600 KRW phá vỡ dưới hỗ trợ với mở rộng đồng thời bán của nhà đầu tư nước ngoài và chương trình

## 11. Kết Luận Cuối Cùng

Mở rộng cung cấp CPU Vera củng cố luận án đầu tư SoCAMM2 của Simmtech. Đặc biệt, đường dẫn giảm dung lượng module do thiếu hụt LPDDR trong khi tăng tổng số lô hàng module và vận chuyển CPU rất khó có thể được đặc trưng là bất lợi cho các nhà cung cấp cơ sở hạ tầng. Nhà cung cấp DRAM bán bit và GB; Simmtech bán PCB đi vào mỗi module. Đây là những đơn vị khác nhau.

Tuy nhiên, nhiều mục vẫn chưa được xác nhận. Khối lượng vận chuyển Vera, module cuối cùng trên mỗi CPU, thị phần thực tế khách hàng cụ thể của Simmtech, doanh thu SoCAMM và biên lợi nhuận bảng lớp cao không thể được hoàn thiện bằng tài liệu công khai một mình. Tính toán như 44 triệu module là một kịch bản hữu ích nhưng không phải là hướng dẫn chính thức.

Giá cổ phiếu hiện tại đã giảm gần 35% từ đỉnh, nhưng không có bằng chứng rằng bán của nhà đầu tư nước ngoài và chương trình đã kết thúc. Do đó, ý tưởng này nên được xem như "một ứng cử viên mua có điều kiện yêu cầu xác nhận của cả thu nhập và cung-cầu" chứ không phải "một cổ phiếu tăng trưởng đã giảm sắc nét". Thu nhập hoạt động Q2 và bình luận doanh thu SoCAMM là xác minh đầu tiên, và vận chuyển máy chủ Vera độc lập nửa sau năm 2026 đại diện cho xác minh thứ hai.

---

## Bằng Chứng và Hạn Chế

### Những Sự Thật Được Xác Nhận

* Thông số kỹ thuật chính thức của NVIDIA trình bày 36 CPU Vera và 54TB LPDDR5X trong NVL72.
* NVIDIA tiết lộ các hệ thống CPU độc lập chứa tối đa 256 CPU Vera trên mỗi giá và kế hoạch khởi chạy OEM cho nửa sau năm 2026.
* TrendForce báo cáo điều chỉnh để giảm dung lượng trên mỗi module trong khi tăng tổng số lô hàng module và sản xuất CPU Vera do thiếu hụt LPDRAM.
* SK Hynix thông báo sản xuất hàng loạt SoCAMM2 192GB cho Vera Rubin.
* Simmtech liệt kê PCB SoCAMM trên danh sách sản phẩm chính thức của mình.
* Đóng cửa ngày 16 tháng 7 của Simmtech, cung-cầu và đồng thuận đã được xác minh lại từ cơ sở dữ liệu địa phương.

### Ước Tính

* Tính toán hàng năm 40 đến 48 triệu module sử dụng giả định 5 đến 6 triệu CPU Vera và 8 module trên mỗi CPU
* Tuyên bố rằng Simmtech cung cấp đồng thời cho ba nhà cung cấp bộ nhớ và duy trì thị phần cao
* Độ lớn của tác động giảm dung lượng đối với doanh thu và lợi nhuận Simmtech sau khi tăng số lượng module

### Mục Không Được Xác Nhận Bởi Tài Liệu Công Khai

* Hướng dẫn vận chuyển CPU Vera chính thức năm 2027 của NVIDIA
* Hệ thống sản xuất cuối cùng module trên mỗi CPU và dung lượng trên mỗi module
* Doanh thu SoCAMM khách hàng cụ thể của Simmtech, thị phần, giá đơn vị và biên lợi nhuận
* Ngày thông báo kết quả Q2 và hướng dẫn doanh thu SoCAMM của công ty
* Phạm vi chính xác của ứng dụng cho giảm dung lượng được báo cáo của TrendForce và thông số kỹ thuật 1,5TB chính thức của NVIDIA

Phân tích thông tin dựa trên tài liệu công khai và dữ liệu thị trường địa phương; không phải lời khuyên đầu tư phản ánh dòng thời gian, giá hoặc khoan dung rủi ro của nhà đầu tư cá nhân.

*Từ chối trách nhiệm: Chỉ dành cho mục đích nghiên cứu và thông tin. Không phải lời khuyên đầu tư. Các tên được trích dẫn chỉ để minh họa phân tích; độc giả nên tự thực hiện do diligence của họ và tham khảo các cố vấn được cấp phép trước bất kỳ quyết định đầu tư nào.*
