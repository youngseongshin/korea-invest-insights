---
title: "Samsung và SK Hynix chiếm 90,8% ngành bán dẫn Hàn Quốc: Nơi dòng vốn ETF nhạy cảm hơn"
date: 2026-06-13T14:40:00+09:00
description: "Ghi chú chiến lược kết hợp dữ liệu vốn hóa thị trường bán dẫn Hàn Quốc và dữ liệu phân bổ ETF toàn diện. Điểm mấu chốt là phân tách tỷ lệ sở hữu ETF tuyệt đối, độ nhạy ETF điều chỉnh theo vốn hóa, và các ứng viên có khoảng cách ETF bị định giá thấp như TCK, Daeduck Electronics, Korea Circuit và Doosan Tesna."
categories: ["Cổ-phiếu-Hàn-Quốc", "Bán-dẫn", "Dòng-vốn-ETF"]
tags: ["bán dẫn Hàn Quốc", "dòng vốn ETF", "Samsung Electronics", "SK Hynix", "TCK", "Daeduck Electronics", "Korea Circuit", "Doosan Tesna", "Leeno Industrial", "DB HiTek"]
series: ["korea-rerating-2026", "korea-market-flow", "korea-semiconductor"]
slug: "korea-semiconductor-etf-exposure-marketcap-gap-strategy-2026-06-13"
draft: false
---

> Bối cảnh
> Bài viết này tiếp nối [Dòng tiền tái cơ cấu ETF chủ đề Hàn Quốc](/post/kr-theme-etf-rebalance-flow-semicap-cap-trim-2026-06-12/), [Dòng tiền ETF đang dẫn dắt thị trường Hàn Quốc](/post/korea-etf-flow-led-market-volatility-strategy-2026-06-13/), [Hub Bán dẫn / HBM Hàn Quốc](/page/korea-semiconductor-hbm-kospi-hub/), [Hub PCB AI và Substrate](/page/korea-ai-pcb-substrate-hub/), [Bài theo dõi cân bằng Sam-Ha-Ma](/post/sam-hama-parity-follow-up-ai-chip-memory-pe-map-2026-06-05/) và [Nút thắt capex trung tâm dữ liệu AI](/post/ai-datacenter-capex-5p3t-korea-power-substrate-storage-bottleneck-2026-06-05/).

## TL;DR

- Chuỗi giá trị bán dẫn của Hàn Quốc cực kỳ tập trung theo vốn hóa thị trường. Tính đến ngày 12 tháng 6 năm 2026, Samsung Electronics và SK Hynix chiếm khoảng **90,8%** trong rổ proxy vốn hóa thị trường 50 cổ phiếu bán dẫn hàng đầu Hàn Quốc.
- Xét theo sở hữu ETF tuyệt đối, **SK Hynix, Samsung Electronics, Samsung Electro-Mechanics và Hanmi Semiconductor** chiếm ưu thế. Nhưng khi điều chỉnh theo vốn hóa thị trường, **Leeno Industrial, DB HiTek, EO Technics, Wonik IPS, HPSP và ISC** lại có độ nhạy ETF cao hơn.
- Theo khung phân tích khoảng cách sở hữu ETF, danh sách theo dõi đầu tiên gồm **TCK, Daeduck Electronics, Korea Circuit và Doosan Tesna**. Simmtech, TES và TLB đã có mức độ phân bổ ETF đáng kể.
- Kết luận chiến lược: tách biệt **bộ nhớ vốn hóa lớn làm vị thế cốt lõi**, **các cổ phiếu dẫn đầu nhạy cảm với ETF làm giao dịch sự kiện/dòng tiền**, và **các ứng viên khoảng cách ETF chưa được sở hữu đủ làm danh sách theo dõi cho sản phẩm ETF tiếp theo / mở rộng chỉ số**.
- Đây không phải danh sách khuyến nghị mua. Đây là khung ưu tiên nghiên cứu. Trước khi sử dụng dòng tiền ETF làm tín hiệu giao dịch, nhà đầu tư vẫn cần xác nhận PCF/PDF từ tổ chức phát hành, phương pháp luận chỉ số, khớp lệnh phiên đóng cửa, và bằng chứng sức mạnh tương đối T+1 / T+3.

<div class="thesis-callout">
  <div class="thesis-callout__label">Điểm Cốt Lõi</div>
  <div class="thesis-callout__body">
    Dòng tiền ETF bán dẫn Hàn Quốc không phải về việc công ty nào lớn nhất. Vấn đề là <strong>cổ phiếu nào nhạy cảm nhất với dòng tiền ETF</strong> và <strong>cổ phiếu nào ETF chưa nắm giữ đủ</strong>. Samsung và SK Hynix chính là thị trường; alpha có khả năng đến từ độ nhạy và các khoảng cách sở hữu chưa được khai thác.
  </div>
</div>

## 1. Vấn đề đặt ra: Hai cổ phiếu thống trị toàn ngành

Ghi chú Alpha của Thesis OS đã định nghĩa mức độ tiếp xúc với ngành bán dẫn Hàn Quốc theo nghĩa rộng: thiết bị, bộ nhớ, fabless, OSAT, thiết bị sản xuất, vật liệu, linh kiện, đế mạch và đóng gói. Sau đó, hệ thống xếp hạng 50 công ty niêm yết hàng đầu của Hàn Quốc theo chỉ số thay thế vốn hóa thị trường.

Chỉ số này không phải vốn hóa thị trường chính thức của KRX. Nó sử dụng công thức từ cơ sở dữ liệu nội bộ:

```text
chỉ số thay thế vốn hóa = giá đóng cửa × cổ phiếu do nước ngoài nắm giữ ÷ tỷ lệ sở hữu nước ngoài
ước tính quy mô sở hữu ETF = NAV của ETF × tỷ trọng cấu thành
tỷ lệ tiếp xúc ETF / vốn hóa = ước tính quy mô sở hữu ETF ÷ chỉ số thay thế vốn hóa
```

Đây không phải phương pháp thay thế hoàn hảo cho vốn hóa thị trường chính thức của KRX. Tuy nhiên, khi áp dụng nhất quán cho cả 50 cổ phiếu hàng đầu, chỉ số này hữu ích để so sánh mức độ tập trung vốn.

| Hạng mục | Giá trị |
|---|---:|
| Chỉ số thay thế vốn hóa top-50 bán dẫn | khoảng KRW 3.766 nghìn tỷ |
| Chỉ số thay thế vốn hóa Samsung Electronics | KRW 1.885,58 nghìn tỷ |
| Chỉ số thay thế vốn hóa SK Hynix | KRW 1.532,41 nghìn tỷ |
| Tỷ trọng Samsung + SK Hynix trong rổ top-50 | khoảng 90,8% |

Ngành bán dẫn Hàn Quốc có vẻ đa dạng về số lượng cổ phiếu, nhưng xét theo vốn hóa, đây thực chất là **thị trường của Samsung Electronics và SK Hynix**. Điều này đặt ra hai câu hỏi riêng biệt:

1. Dòng tiền lớn nhất từ các ETF có vẫn đổ vào Samsung và SK Hynix?
2. Trong 9,2% còn lại, những cổ phiếu nào chịu rủi ro cao nhất từ các cú sốc dòng vốn ETF?

Bài viết này tập trung vào câu hỏi thứ hai.

## 2. Top 50 Vốn Hóa Thị Trường Ngành Bán Dẫn Hàn Quốc (Proxy)

Đơn vị: nghìn tỷ KRW. Vốn hóa thị trường là proxy từ cơ sở dữ liệu nội bộ, không phải số liệu chính thức của KRX.

| Hạng | Công ty | Mã | Phân khúc | Vốn hóa proxy |
|---:|---|---:|---|---:|
| 1 | Samsung Electronics | 005930 | Thiết bị / bộ nhớ | 1,885.58 |
| 2 | SK Hynix | 000660 | Thiết bị / bộ nhớ | 1,532.41 |
| 3 | Samsung Electro-Mechanics | 009150 | Đế / đóng gói | 128.02 |
| 4 | Hanmi Semiconductor | 042700 | Thiết bị / kiểm tra | 34.42 |
| 5 | LG Innotek | 011070 | Đế / linh kiện | 24.52 |
| 6 | Jusung Engineering | 036930 | Thiết bị | 10.73 |
| 7 | Wonik IPS | 240810 | Thiết bị | 9.00 |
| 8 | Isu Petasys | 007660 | Đế | 8.99 |
| 9 | Daeduck Electronics | 353200 | Đế | 8.17 |
| 10 | Leeno Industrial | 058470 | Socket kiểm tra | 7.97 |
| 11 | DB HiTek | 000990 | Xưởng đúc | 7.58 |
| 12 | EO Technics | 039030 | Thiết bị | 7.54 |
| 13 | SKC | 011790 | Vật liệu / composite | 6.96 |
| 14 | HPSP | 403870 | Thiết bị | 5.88 |
| 15 | FADU | 440110 | Fabless | 5.06 |
| 16 | PSK | 319660 | Thiết bị | 4.92 |
| 17 | ISC | 095340 | Socket kiểm tra | 4.88 |
| 18 | Simmtech | 222800 | Đế | 4.87 |
| 19 | Eugene Technology | 084370 | Thiết bị | 4.49 |
| 20 | Jeju Semiconductor | 080220 | Fabless | 3.53 |
| 21 | TES | 095610 | Thiết bị | 3.53 |
| 22 | Soulbrain | 357780 | Vật liệu | 3.43 |
| 23 | Doosan Tesna | 131970 | OSAT / kiểm tra | 3.38 |
| 24 | PSK Holdings | 031980 | Thiết bị | 3.29 |
| 25 | Hana Micron | 067310 | OSAT | 3.25 |
| 26 | TCK | 064760 | Vật liệu / linh kiện | 3.24 |
| 27 | Korea Circuit | 007810 | Đế | 3.22 |
| 28 | Hansol Chemical | 014680 | Vật liệu | 3.21 |
| 29 | Dongjin Semichem | 005290 | Vật liệu | 3.01 |
| 30 | TSE | 131290 | Kiểm tra | 2.99 |
| 31 | Techwing | 089030 | Thiết bị kiểm tra | 2.42 |
| 32 | VM | 089970 | Thiết bị | 2.40 |
| 33 | Park Systems | 140860 | Đo lường | 2.38 |
| 34 | RFHIC | 218410 | RF / liền kề bán dẫn hợp chất | 2.04 |
| 35 | GigaVis | 420770 | Thiết bị kiểm tra | 1.85 |
| 36 | KC Tech | 281820 | Thiết bị | 1.72 |
| 37 | Hana Materials | 166090 | Vật liệu / linh kiện | 1.45 |
| 38 | S&S Tech | 101490 | Mặt nạ trắng | 1.36 |
| 39 | Haesung DS | 195870 | Đóng gói / khung dẫn | 1.33 |
| 40 | YC | 232140 | Thiết bị kiểm tra | 1.31 |
| 41 | Komico | 183300 | Làm sạch / phủ | 1.31 |
| 42 | GST | 083450 | Thiết bị | 1.20 |
| 43 | SFA Semicon | 036540 | OSAT | 1.19 |
| 44 | Wonik QnC | 074600 | Thạch anh / vật liệu | 1.11 |
| 45 | TLB | 356860 | Đế | 0.98 |
| 46 | SEMCNS | 252990 | Linh kiện thẻ đầu dò | 0.98 |
| 47 | LX Semicon | 108320 | Fabless | 0.82 |
| 48 | DI | 003160 | Thiết bị kiểm tra | 0.80 |
| 49 | Protec | 053610 | Thiết bị | 0.80 |
| 50 | Dongwoon Anatech | 094170 | Fabless | 0.78 |

Điểm mấu chốt nằm ở khoảng cách sau tên thứ ba. Samsung Electro-Mechanics đã là cái tên độc lập có quy mô lớn, nhưng Hanmi nhỏ hơn đáng kể, và Leeno còn nhỏ hơn nhiều. Vì vậy, cùng một dòng vốn ETF sẽ có tiềm năng tác động giá lớn hơn đối với các cổ phiếu vốn hóa vừa trong nhóm thiết bị, đế bán dẫn, kiểm tra và vật liệu.

## 3. Quy Mô ETF Tuyệt Đối: Dòng Tiền Lớn Đã Tập Trung Vào Các Công Ty Dẫn Đầu

Tỷ lệ sở hữu ETF ước tính được tính bằng cách nhân trọng số thành phần ETF với NAV của ETF, sau đó cộng dồn toàn bộ dữ liệu ETF nội địa.

| Hạng | Công ty | Số ETF | Tổng trọng số | Trọng số ETF tối đa | Sở hữu ETF ước tính | ETF / vốn hóa thị trường |
|---:|---|---:|---:|---:|---:|---:|
| 1 | SK Hynix | 9 | 209,8% | 37,6% | KRW 8.249,9 tỷ | 0,54% |
| 2 | Samsung Electronics | 9 | 174,8% | 26,2% | KRW 6.205,9 tỷ | 0,33% |
| 3 | Samsung Electro-Mechanics | 4 | 76,2% | 37,9% | KRW 3.037,2 tỷ | 2,37% |
| 4 | Hanmi Semiconductor | 5 | 53,9% | 18,1% | KRW 2.134,6 tỷ | 6,20% |
| 5 | Leeno Industrial | 3 | 14,2% | 7,3% | KRW 772,3 tỷ | 9,70% |
| 6 | DB HiTek | 4 | 11,5% | 4,7% | KRW 699,7 tỷ | 9,23% |
| 7 | Wonik IPS | 2 | 11,1% | 6,7% | KRW 636,4 tỷ | 7,07% |
| 8 | EO Technics | 2 | 10,4% | 6,3% | KRW 596,5 tỷ | 7,91% |
| 9 | LG Innotek | 1 | 8,9% | 8,9% | KRW 524,8 tỷ | 2,14% |
| 10 | Isu Petasys | 3 | 15,8% | 9,1% | KRW 447,1 tỷ | 4,98% |

Xét về giá trị tuyệt đối, SK Hynix và Samsung chiếm ưu thế vượt trội. Tuy nhiên, tỷ lệ sở hữu ETF chỉ lần lượt ở mức 0,54% và 0,33% so với vốn hóa thị trường tương ứng. Đối với các cổ phiếu vốn hóa lớn này, dòng tiền ETF chỉ là một phần trong cả một cấu trúc dòng tiền phức tạp hơn nhiều, bao gồm: cổ phiếu tiền mặt khối ngoại, định chế tài chính nội địa, đòn bẩy nhà đầu tư cá nhân, dòng tiền hợp đồng tương lai/chương trình giao dịch và kỳ vọng lợi nhuận.

Ngược lại, tỷ lệ sở hữu ETF ước tính của Hanmi là 2,13 nghìn tỷ KRW, tương đương 6,20% vốn hóa thị trường. Leeno, DB HiTek, Wonik IPS và EO Technics có quy mô sở hữu ETF tuyệt đối nhỏ hơn, nhưng mức độ nhạy cảm so với vốn hóa thị trường lại cao hơn đáng kể.

## 4. Độ Nhạy Cảm Với Dòng Vốn ETF: Cổ Phiếu Bán Dẫn Vốn Hóa Trung Biến Động Mạnh Hơn

| Hạng | Công ty | Ước tính sở hữu ETF | ETF / vốn hóa thị trường |
|---:|---|---:|---:|
| 1 | Leeno Industrial | KRW 772,3 tỷ | 9,70% |
| 2 | DB HiTek | KRW 699,7 tỷ | 9,23% |
| 3 | EO Technics | KRW 596,5 tỷ | 7,91% |
| 4 | Wonik IPS | KRW 636,4 tỷ | 7,07% |
| 5 | HPSP | KRW 411,2 tỷ | 6,99% |
| 6 | ISC | KRW 306,5 tỷ | 6,29% |
| 7 | Hanmi Semiconductor | KRW 2.134,6 tỷ | 6,20% |
| 8 | Soulbrain | KRW 182,5 tỷ | 5,31% |
| 9 | Isu Petasys | KRW 447,1 tỷ | 4,98% |
| 10 | Samsung Electro-Mechanics | KRW 3.037,2 tỷ | 2,37% |

Nhóm này đã nhận được dòng vốn ETF đáng kể. Hàm ý mang tính hai chiều.

Thứ nhất, nếu việc tạo lập ETF bán dẫn tiếp tục hoặc các ETF chủ đề mở rộng, những cổ phiếu này có thể tiếp tục nhận thêm dòng vốn gia tăng.

Thứ hai, nếu xuất hiện tình trạng tất toán ETF hoặc tái cân bằng giới hạn vốn hóa, chính những cổ phiếu này có thể trở nên dễ bị tổn thương về mặt cơ học. Tỷ lệ sở hữu ETF cao không chỉ mang ý nghĩa tích cực. Điều đó đồng nghĩa với **khả năng tham gia tăng giá cao hơn khi dòng vốn hỗ trợ và rủi ro bán tháo cơ học cao hơn khi dòng vốn đảo chiều**.

## 5. Daeduck và Simmtech: Cơ Sở Dữ Liệu Chủ Đề Nội Địa Có Thể Đánh Giá Thấp Mức Độ Phơi Lộ

Phân tích đã kiểm tra lại Daeduck Electronics và Simmtech trên toàn bộ vũ trụ API ETF Naver gồm 1.137 ETF, bởi vì một cơ sở dữ liệu ETF chủ đề nội địa đơn thuần có thể đánh giá thấp mức độ phơi lộ của hai cổ phiếu này.

| Công ty | Số ETF | Số quản lý | Tổng tỷ trọng | Tỷ trọng ETF tối đa | Ước tính sở hữu ETF | ETF / vốn hóa thị trường |
|---|---:|---:|---:|---:|---:|---:|
| Daeduck Electronics | 16 | 10 | 81,78% | 15,39% | KRW 159,0 tỷ | 1,95% |
| Simmtech | 17 | 11 | 61,25% | 6,91% | KRW 188,5 tỷ | 3,87% |

Daeduck đã có mặt trong 16 ETF. Simmtech đã có mặt trong 17 ETF. Vậy cả hai đều không phải là tên ETF chưa được khám phá.

Tuy nhiên, chúng có sự khác biệt:

- Daeduck xuất hiện trong nhiều ETF, nhưng tỷ lệ sở hữu ETF so với vốn hóa thị trường chỉ ở mức 1,95%.
- Simmtech đã ở mức 3,87%, nghĩa là dòng tiền ETF đã được phản ánh nhiều hơn.
- Daeduck có thể hưởng lợi nếu các chủ đề AI substrate, FC-BGA, ASIC và networking trở nên rõ ràng hơn trong tên sản phẩm ETF và phương pháp luận xây dựng chỉ số.
- Simmtech đã được đại diện rộng rãi trong SOL AI Semiconductor Materials/Equipment, ACE AI Semiconductor TOP3+, RISE Non-Memory Semiconductor Active, KoAct KOSDAQ Active và KODEX AI Semiconductor Core Equipment.

### Daeduck Electronics: Các ETF Nắm Giữ Chính

| ETF | Quản lý | Tỷ trọng | NAV ETF | Ước tính nắm giữ |
|---|---|---:|---:|---:|
| KODEX AI Semiconductor Core Equipment | Samsung AM | 6,84% | KRW 473,7 tỷ | KRW 32,4 tỷ |
| ACE AI Semiconductor TOP3+ | KIM | 2,23% | KRW 1.296,9 tỷ | KRW 28,9 tỷ |
| RISE Non-Memory Semiconductor Active | KB AM | 5,76% | KRW 345,3 tỷ | KRW 19,9 tỷ |
| WON Semiconductor Value Chain Active | Woori AM | 4,36% | KRW 378,5 tỷ | KRW 16,5 tỷ |
| 1Q K Semiconductor TOP2+ | Hana AM | 6,06% | KRW 253,5 tỷ | KRW 15,4 tỷ |
| SOL Semiconductor Back-End | Shinhan AM | 15,39% | KRW 83,4 tỷ | KRW 12,8 tỷ |

### Simmtech: Các ETF Nắm Giữ Chính

| ETF | Quản lý | Tỷ trọng | NAV ETF | Ước tính nắm giữ |
|---|---|---:|---:|---:|
| SOL AI Semiconductor Materials/Equipment | Shinhan AM | 4,79% | KRW 1.221,7 tỷ | KRW 58,5 tỷ |
| ACE AI Semiconductor TOP3+ | KIM | 2,32% | KRW 1.296,9 tỷ | KRW 30,1 tỷ |
| RISE Non-Memory Semiconductor Active | KB AM | 6,91% | KRW 345,3 tỷ | KRW 23,9 tỷ |
| KoAct KOSDAQ Active | Samsung Active AM | 3,55% | KRW 652,8 tỷ | KRW 23,2 tỷ |
| KODEX AI Semiconductor Core Equipment | Samsung AM | 4,77% | KRW 473,7 tỷ | KRW 22,6 tỷ |
| TIME KOSDAQ Active | Timefolio | 2,62% | KRW 383,5 tỷ | KRW 10,0 tỷ |

Điều này thay đổi kết luận. Simmtech không phải là cổ phiếu bị ETF nắm giữ thiếu. Nó gần với một tên substrate đã được ETF nắm giữ đầy đủ. Daeduck thì khác: được đưa vào danh mục rộng rãi nhưng vẫn bị đánh giá thấp hơn so với vốn hóa thị trường.

## 6. Phân Loại Lại Khoảng Cách Sở Hữu ETF Thấp

Màn hình khoảng cách tập trung bao gồm TLB, Korea Circuit, Doosan Tesna, TES, TCK, Daeduck và Simmtech.

| Công ty | Vốn hóa thị trường ước tính | Số lượng ETF | Sở hữu ETF ước tính | ETF / vốn hóa | Thay đổi ETF tích cực gần đây | Diễn giải |
|---|---:|---:|---:|---:|---:|---|
| TCK | KRW 3,24 nghìn tỷ | 5 | KRW 14,4 tỷ | 0,44% | +0,39%p | Khoảng cách sở hữu ETF thấp nhất — cơ hội lớn nhất |
| Daeduck Electronics | KRW 8,17 nghìn tỷ | 16 | KRW 159,0 tỷ | 1,95% | +0,09%p | Ứng viên mở rộng ETF substrate AI |
| Doosan Tesna | KRW 3,38 nghìn tỷ | 6 | KRW 53,6 tỷ | 1,58% | -1,27%p | Cần chất xúc tác ETF OSAT/kiểm thử |
| Korea Circuit | KRW 3,22 nghìn tỷ | 5 | KRW 73,2 tỷ | 2,27% | +0,59%p | Ứng viên tăng tỷ trọng âm thầm |
| Simmtech | KRW 4,87 nghìn tỷ | 17 | KRW 188,5 tỷ | 3,87% | +2,00%p | Dòng vốn ETF đã ở mức đáng kể |
| TES | KRW 3,53 nghìn tỷ | 14 | KRW 126,6 tỷ | 3,59% | -0,63%p | Nhiều ETF đưa vào danh mục, một số gần đây đã cắt giảm |
| TLB | KRW 0,98 nghìn tỷ | 7 | KRW 34,2 tỷ | 3,47% | -0,60%p | Độ tinh khiết SOCAMM cao, nhưng mức độ tiếp xúc ETF đã tồn tại |

Là một khung chiến lược, mô hình này trở thành phễu bốn nhóm:

| Nhóm | Tên công ty | Diễn giải |
|---|---|---|
| Chuyển sang nghiên cứu sâu hơn | TCK, Daeduck Electronics, Korea Circuit | Khoảng cách sở hữu ETF thấp kết hợp khả năng mở rộng chủ đề |
| Theo dõi / cần chất xúc tác | Doosan Tesna | Sở hữu thấp, nhưng thay đổi ETF tích cực gần đây còn yếu |
| ETF đã phản ánh đầy đủ | Simmtech, TES, TLB | Đã được đưa vào danh mục rộng rãi và nhạy cảm với ETF |
| Các cổ phiếu dẫn dắt nhạy cảm với dòng vốn | Leeno, DB HiTek, EO Technics, Wonik IPS, HPSP, ISC, Hanmi | Đã tiếp xúc với dòng vốn ETF; hồ sơ giao dịch theo sự kiện/dòng vốn |

## 7. Thẻ Ý Tưởng: TCK

**Khả năng Hành động:** Tiến hành nghiên cứu sâu hơn. Đây không phải tín hiệu mua ngay lập tức; cần mở rộng sản phẩm ETF và xác nhận dòng vốn.

**Điểm Khác Biệt Cốt Lõi:** TCK có vốn hóa thị trường ủy quyền 3,24 nghìn tỷ KRW, nhưng chỉ có khoảng 14,4 tỷ KRW sở hữu ETF ước tính, tương đương 0,44% vốn hóa thị trường. Đây là tỷ lệ rất thấp đối với một cái tên đại diện trong mảng vật liệu / vật tư tiêu hao bán dẫn.

**Tại Sao Là Bây Giờ:** Nếu các ETF bán dẫn mở rộng từ bộ nhớ và thiết bị sang vật liệu / vật tư tiêu hao, TCK là một trong những ứng viên bị sở hữu thấp rõ ràng nhất. Thay đổi ETF chủ động gần đây cũng tích cực ở mức +0,39%p.

**Rủi Ro Đầu Tiên:** Khoảng cách này có thể kéo dài nếu các ETF vật liệu / vật tư tiêu hao không tăng quy mô, hoặc nếu TCK không vượt qua các bộ lọc thanh khoản, phương pháp luận hoặc nhãn chủ đề.

**Điều Kiện Để Trở Thành Cơ Hội Đầu Tư:** Bằng chứng PCF/PDF từ nhà phát hành về việc đưa vào danh mục hoặc tăng tỷ trọng, cộng với xác nhận dòng vốn nước ngoài / tổ chức.

**Điều Có Thể Phủ Nhận Luận Điểm:** Nếu đà tăng trưởng hoạt động hoặc biên lợi nhuận suy yếu trong khi khoảng cách ETF vẫn chưa được lấp đầy, lập luận "ETF cuối cùng sẽ mua vào" là chưa đủ.

**Quy Trình Tiếp Theo:** Lập bản đồ vũ trụ ETF vật liệu / vật tư tiêu hao bán dẫn, phương pháp luận chỉ số, các ràng buộc thanh khoản và tỷ lệ cổ phiếu tự do lưu hành.

## 8. Thẻ Ý Tưởng: Daeduck Electronics

**Khả năng hành động:** Tiến hành nghiên cứu chuyên sâu hơn. Ứng viên mở rộng ETF nền tảng AI.

**Lợi thế khác biệt:** Daeduck hiện đã có mặt trong 16 ETF, nhưng tỷ lệ sở hữu ETF ước tính chỉ chiếm 1,95% so với vốn hóa thị trường tham chiếu. Cổ phiếu xuất hiện rộng rãi, nhưng chưa được nắm giữ nhiều.

**Tại sao là lúc này:** Nếu nền tảng AI, FC-BGA, ASIC và mạng kết nối được thể hiện rõ ràng hơn trong nhãn sản phẩm ETF và cấu trúc chỉ số, tỷ trọng của Daeduck có thể tăng lên. Công ty có quy mô nhỏ hơn nhiều so với Samsung Electro-Mechanics và phản ánh ETF kém hơn Simmtech.

**Bác bỏ đầu tiên:** Không nên phóng đại góc nhìn "chưa được khám phá". Cổ phiếu này đã hiện diện ở hơn mười nhà quản lý và 16 ETF.

**Điều kiện để trở nên đáng đầu tư:** Tỷ trọng cao hơn trong các chỉ số nền tảng AI / FC-BGA, sức mạnh tương đối vượt đường 20 ngày, và xác nhận dòng vốn nước ngoài / tổ chức.

**Rủi ro tiêu diệt luận điểm:** Nếu khả năng tạo ra giá trị từ nền tảng AI vẫn tập trung vào Samsung Electro-Mechanics và Daeduck không thể hiện đóng góp thu nhập từ FC-BGA / substrate tốc độ cao.

**Bước tiếp theo:** So sánh Daeduck, Simmtech, Korea Circuit và TLB theo tỷ trọng ETF, sức mạnh tương đối và điều chỉnh ước tính lợi nhuận.

## 9. Thẻ Ý Tưởng: Korea Circuit

**Khả năng hành động:** Chuyển sang nghiên cứu sâu hơn / danh sách theo dõi.

**Lợi thế Chênh lệch:** Korea Circuit có vốn hóa thị trường ước tính KRW 3,22 nghìn tỷ, quy mô sở hữu ETF ước tính KRW 73,2 tỷ và tỷ lệ ETF / vốn hóa là 2,27%. Cổ phiếu này chưa hoàn toàn bị bỏ qua, nhưng mức độ phản ánh vẫn thấp hơn so với Simmtech, TES và TLB.

**Tại Sao Ngay Lúc Này:** Có khả năng xảy ra xúc tác kép SOCAMM + FC-BGA, và biến động ETF chủ động gần đây là +0,59%p. Từ khóa cốt lõi là "tăng tỷ trọng âm thầm."

**Lý Do Từ Chối Ban Đầu:** Mức độ tiếp xúc trực tiếp với chủ đề có thể kém rõ ràng hơn so với Simmtech hoặc TLB, và dòng chảy ETF đơn thuần là chưa đủ nếu thiếu bằng chứng về doanh thu từ nền tảng / module AI.

**Điều Kiện Để Có Thể Đầu Tư:** Tỷ trọng ETF chủ động tiếp tục tăng kèm theo dòng tiền thực tế từ tổ chức hoặc nhà đầu tư nước ngoài.

**Điều Có Thể Phá Vỡ Luận Điểm:** Nếu SOCAMM / FC-BGA vẫn chỉ là câu chuyện giá mà không có bằng chứng về doanh thu, biên lợi nhuận hay đơn hàng thực tế.

**Bước Tiếp Theo:** Theo dõi danh sách ETF của Korea Circuit, biến động ETF chủ động và dòng vốn tương đối so với Simmtech và TLB.

## 10. Thẻ Ý Tưởng: Doosan Tesna

**Khả năng hành động:** Theo dõi / cần tín hiệu kích hoạt.

**Lợi thế khác biệt:** Doosan Tesna có vốn hóa thị trường đại diện là 3,38 nghìn tỷ KRW và ước tính chỉ có 53,6 tỷ KRW sở hữu bởi ETF, tương đương 1,58% vốn hóa. Đối với một ứng viên OSAT / kiểm định, tỷ lệ đại diện trong ETF vẫn còn thấp.

**Tại sao Ngay Lúc Này:** Nếu nhu cầu back-end AI và kiểm định mở rộng từ substrate và socket sang OSAT / kiểm định, Doosan Tesna có thể trở thành ứng viên được đưa vào ETF tiếp theo hoặc tăng trọng số.

**Lý Do Bác Bỏ Ban Đầu:** Thay đổi ETF chủ động gần đây là -1,27%p, khá yếu. Việc bị sở hữu thiếu không tự động đồng nghĩa với khả năng hành động.

**Điều Kiện Để Trở Thành Khoản Đầu Tư Khả Thi:** Phục hồi trọng số ETF trong lĩnh vực OSAT / kiểm định, nâng cấp đồng thuận, và sự quay trở lại của các tổ chức với dòng tiền thực.

**Điều Có Thể Phá Vỡ Luận Điểm:** Nếu nhu cầu kiểm định được định giá chủ yếu vào Leeno, ISC và TSE trong khi Doosan Tesna không thể hiện đòn bẩy biên lợi nhuận hay công suất sử dụng.

**Quy Trình Tiếp Theo:** So sánh Doosan Tesna, Hana Micron, SFA Semicon, Leeno và ISC theo sở hữu ETF, đòn bẩy hoạt động và dòng vốn.

## 11. Cách Xử lý Các Cổ phiếu Đã Có Dòng Vốn ETF

Leeno, DB HiTek, EO Technics, Wonik IPS, HPSP, ISC và Hanmi không phải là các cổ phiếu bị ETF nắm giữ thấp hơn giá trị. Đây là những cổ phiếu dẫn dắt thị trường nhạy cảm với dòng vốn ETF.

| Điều kiện | Hành động |
|---|---|
| ETF tạo mới kết hợp mua ròng từ khối ngoại / tổ chức | Có thể áp dụng chiến lược theo xu hướng |
| Tín hiệu tái cân bằng mạnh nhưng giá tăng đột biến một ngày rồi khối lượng giảm dần | Không đuổi theo; xác nhận tại T+1 / T+3 |
| ETF hoàn mua lại hoặc cắt giảm tỷ trọng cùng với khối ngoại bán ra | Rủi ro ngắn hạn tăng cao |
| Giá giữ vững dù chịu áp lực từ ETF | Xác nhận nhu cầu thực tế mạnh hơn |

Hanmi đặc biệt quan trọng. Ước tính tỷ lệ sở hữu của ETF là lớn, nhưng luận điểm đầu tư thực sự của cổ phiếu này không phải là dòng vốn ETF. Đó là mảng bonder TC cho HBM, đa dạng hóa khách hàng HBM4 và các thông báo đơn hàng thực tế. Dòng vốn ETF có thể tác động lên giá; nhưng đó không phải là luận điểm đầu tư cốt lõi.

## 12. Khung Thực Thi: Ba Rổ Đầu Tư

### 12.1 Tiếp Xúc Cốt Lõi Với Bán Dẫn

**Samsung Electronics và SK Hynix**

Với hai cổ phiếu này, dòng tiền thị trường Hàn Quốc, giao dịch cổ phiếu tiền mặt nước ngoài, tính bền vững lợi nhuận HBM và PER tương đối so với Micron quan trọng hơn độ nhạy ETF. Đừng xem các bộ lọc cắt giảm tỷ trọng ETF là tín hiệu bán. Tuy nhiên, do lĩnh vực này quá tập trung, nhà đầu tư cần theo dõi beta tổng danh mục khi biến động gia tăng.

### 12.2 Cổ Phiếu Dẫn Đầu Nhạy Cảm Với Dòng Tiền ETF

**Leeno, DB HiTek, EO Technics, Wonik IPS, HPSP, ISC và Hanmi**

Các cổ phiếu này đã có dòng tiền ETF. Chúng có thể tăng nhanh khi xuất hiện sự kiện phù hợp, nhưng cũng nhạy cảm hơn với đợt rút vốn ETF và tái cân bằng tỷ trọng. Thời điểm vào lệnh và xác nhận tín hiệu quan trọng hơn là chỉ dựa vào nhãn hiệu đơn thuần.

### 12.3 Ứng Cử Viên Có Khoảng Cách Tỷ Trọng ETF Thấp

**TCK, Daeduck Electronics, Korea Circuit và Doosan Tesna**

Đây là các ứng cử viên cho làn sóng gắn nhãn sản phẩm ETF tiếp theo hoặc mở rộng chỉ số. Tuy nhiên, "ETF chưa nắm giữ đủ" là chưa đủ điều kiện. Khoảng cách tỷ trọng phải đi kèm với bằng chứng hoạt động kinh doanh.

| Công ty | Bằng Chứng Cần Thiết |
|---|---|
| TCK | Nhu cầu vật liệu / tiêu hao, mức độ sử dụng của khách hàng, phục hồi biên lợi nhuận |
| Daeduck Electronics | Đế AI, FC-BGA, đóng góp doanh thu từ ASIC / mạng |
| Korea Circuit | Đơn hàng lặp lại SOCAMM + FC-BGA và khả năng sinh lời |
| Doosan Tesna | Tăng trưởng khối lượng OSAT / kiểm thử và đòn bẩy hoạt động |

## 13. Điều Kiện Thất Bại

1. Dữ liệu bề mặt ETF của Naver khác biệt đáng kể so với dữ liệu thành phần PCF/PDF của nhà phát hành.
2. Các ứng viên bị nắm giữ thiếu không đáp ứng phương pháp chỉ số thực tế hoặc tiêu chí thanh khoản để được đưa vào / tăng tỷ trọng.
3. AUM của ETF không tăng trưởng, và các ETF theo chủ đề chứng kiến dòng tiền rút ra.
4. Tín hiệu tái cân bằng đã được phản ánh vào giá, và sức mạnh tương đối T+1 / T+3 suy yếu.
5. Các ứng viên có khoảng cách bị nắm giữ thiếu không cung cấp được bằng chứng hoạt động kinh doanh.
6. Dòng tiền vào Samsung và SK Hynix đảo chiều, gây ra làn sóng rút vốn khỏi ETF bán dẫn diện rộng.

Điều kiện thất bại quan trọng nhất là số ba. Tái cân bằng ETF là **thay đổi tỷ trọng nội bộ**, không đồng nghĩa với việc tạo lập ETF mới. Nếu dòng tiền rời khỏi ETF, các ứng viên mua nội bộ có thể không đạt kỳ vọng.

## 14. Nhận Định Cuối Cùng

Sai lầm dễ mắc nhất trong phân tích ETF bán dẫn Hàn Quốc là chỉ nhìn vào những cái tên lớn nhất. SK Hynix và Samsung có tỷ trọng nắm giữ ETF tuyệt đối lớn nhất, nhưng độ nhạy được điều chỉnh theo vốn hóa thị trường của họ lại thấp. Leeno, DB HiTek, EO Technics, Wonik IPS, HPSP và ISC nhạy cảm hơn với dòng chảy ETF.

Nhưng độ nhạy cao cũng đồng nghĩa với rủi ro rút vốn cao hơn. Alpha tiếp theo không đơn giản nằm ở những cổ phiếu nhạy cảm nhất với ETF. Nó nằm ở nơi **tỷ lệ sở hữu ETF thấp hơn kỳ vọng, chủ đề vận hành và xu hướng dòng vốn** cùng hội tụ.

Ưu tiên hiện tại:

| Thứ hạng | Ứng viên | Nhận định |
|---:|---|---|
| 1 | TCK | Khoảng cách ETF sở hữu thiếu mạnh nhất; theo dõi mở rộng ETF vật liệu / tiêu hao |
| 2 | Daeduck Electronics | Ứng viên mở rộng ETF substrate AI; được đưa vào rộng rãi nhưng tỷ lệ sở hữu điều chỉnh theo vốn hóa vẫn thấp |
| 3 | Korea Circuit | Ứng viên tăng tỷ trọng thầm lặng; xác nhận xúc tác kép SOCAMM + FC-BGA |
| 4 | Doosan Tesna | Ứng viên OSAT / kiểm tra sở hữu thiếu; cần chất xúc tác sau thay đổi ETF chủ động gần đây yếu |
| 5 | Leeno / DB HiTek / EO Technics / Wonik IPS / HPSP / ISC | Các cổ phiếu dẫn đầu nhạy cảm ETF; phù hợp hơn khi định khung là giao dịch theo sự kiện / dòng vốn hơn là khoảng cách sở hữu thiếu |

Kết luận một dòng:

> Trong thị trường mà Samsung Electronics và SK Hynix chiếm 90,8% chỉ số đại diện vốn hóa bán dẫn, alpha ETF đến từ việc tách biệt **độ nhạy ETF điều chỉnh theo vốn hóa thị trường** khỏi **khoảng cách ETF sở hữu thiếu**.

## Bảng Chứng Cứ

| Mục | Chi tiết |
|---|---|
| Ghi chú nghiên cứu nguồn | `Thesis OS source research note` |
| Proxy giá / vốn hóa thị trường | `full_results_20260613_061000.csv` |
| Ngày cập nhật giá | 2026-06-12 |
| DB ETF chủ đề nội địa | `theme_etf_rebalance_flow.db` |
| DB dòng tiền ETF chủ động | `active_etf_flow.db` |
| API thành phần ETF đầy đủ | `https://m.stock.naver.com/api/stocks/etf`, `https://m.stock.naver.com/api/etf/{ETF_CODE}/basic` |
| Quét ETF toàn diện | Đã quét 1.137 ETF, thành công 1.137, thất bại 0 |
| API trực tiếp KRX | Các endpoint JSON/PDF tại `data.krx.co.kr` trả về `LOGOUT` |
| Dữ liệu thô hỗ trợ | `/tmp/daeduck_simmtech_all_naver_etf_20260612.csv`, `/tmp/semicap_gap_targets_all_naver_etf_20260612.csv` |

## Sự Thật / Suy Luận / Suy Đoán / Bị Chặn

### [Sự Thật]

- Rổ đại diện vốn hóa thị trường top-50 bán dẫn Hàn Quốc đạt tổng cộng khoảng 3.766 nghìn tỷ KRW.
- Samsung Electronics và SK Hynix chiếm khoảng 90,8% rổ đó.
- Dựa trên quét toàn bộ API ETF Naver, Daeduck Electronics được đưa vào 16 ETF và Simmtech được đưa vào 17 ETF.
- Ước tính sở hữu ETF là 159,0 tỷ KRW đối với Daeduck và 188,5 tỷ KRW đối với Simmtech.
- Trong số bảy ứng viên khoảng cách trọng tâm, TCK có tỷ lệ sở hữu ETF thấp nhất: 14,4 tỷ KRW, tương đương 0,44% vốn hóa thị trường.

### [Suy Luận]

- Xét về sở hữu ETF tuyệt đối, SK Hynix, Samsung Electronics, Samsung Electro-Mechanics và Hanmi là những bên hưởng lợi lớn nhất.
- Xét về độ nhạy tái cân bằng, Leeno, DB HiTek, EO Technics, Wonik IPS, HPSP và ISC quan trọng hơn.
- Daeduck và Simmtech có thể bị đánh giá thấp trong dữ liệu ETF chủ đề nội địa; quét ETF đầy đủ cho thấy cả hai đã được đưa vào rộng rãi.
- Từ góc độ khoảng cách ETF sở hữu thấp, TCK, Daeduck, Doosan Tesna và Korea Circuit thú vị hơn Simmtech.

### [Suy Đoán]

- Nếu các chủ đề FC-BGA, ASIC và mạng AI trở nên rõ ràng hơn trong nhãn ETF và phương pháp chỉ số, tỷ trọng của Daeduck có thể tăng.
- Nếu các chủ đề SOCAMM / LPDDR tiếp tục duy trì, TLB và Korea Circuit có thể nhận được mức tăng thêm trong danh mục / mở rộng tỷ trọng sau Simmtech.
- Nếu các ETF vật liệu / vật tư bán dẫn mở rộng, TCK là ứng viên sở hữu thấp trực tiếp nhất.

### [Bị Chặn]

- Các điểm cuối PDF / JSON ETF trực tiếp của KRX trả về `LOGOUT`.
- Vốn hóa thị trường là proxy nội địa, không phải vốn hóa thị trường KRX chính thức.
- Kiểm tra chéo PCF/PDF của tổ chức phát hành chưa được hoàn thành cho mọi ETF. Các ứng viên chủ chốt cần xác minh riêng lẻ.
