---
title: "Marvell Q1 FY2027 và Bán Dẫn Hàn Quốc: Nút Thắt Kết Nối, Substrate và Nguồn Điện Quan Trọng Hơn HBM"
date: 2026-05-28T10:20:00+09:00
description: "Kết quả Q1 FY2027 của Marvell không chỉ là EPS vượt kỳ vọng — mà cho thấy nút thắt của trung tâm dữ liệu AI đang lan rộng sang custom XPU, optical interconnect, scale-up networking, FCBGA, MLCC, tụ điện silicon và test socket. Read-through cho bán dẫn Hàn Quốc được phân tích theo thứ tự: Samsung Electro-Mechanics, Samsung Electronics, SK Hynix và ISC·Leeno·TSE."
categories: ["Market-Outlook"]
tags:
  - "Marvell"
  - "MRVL"
  - "마벨"
  - "한국 반도체"
  - "삼성전기"
  - "009150"
  - "삼성전자"
  - "005930"
  - "SK하이닉스"
  - "000660"
  - "ISC"
  - "리노공업"
  - "티에스이"
  - "FC-BGA"
  - "MLCC"
  - "실리콘 커패시터"
  - "HBM"
  - "AI ASIC"
  - "AI 인프라"
slug: marvell-q1-fy2027-korea-semiconductor-readthrough-2026-05-28
valley_cashtags:
  - Marvell
  - 삼성전기
  - 삼성전자
  - SK하이닉스
  - ISC
  - 리노공업
  - 티에스이
  - 대덕전자
  - 이수페타시스
  - 심텍
draft: false
---

> 📚 Bối cảnh bài viết tiếp theo
> Đây là bài tiếp theo của [Kiểm tra nút thắt bán dẫn Hàn Quốc trước kết quả Marvell·Broadcom](/post/marvell-broadcom-earnings-korea-ai-bottleneck-preview-2026-05-23/). Câu hỏi đặt ra trong bài preview là "Liệu chiến lược đặt cược đơn lẻ vào HBM có mở rộng sang AI ASIC, networking và ổn định hóa nguồn điện không?" — và bài này trả lời câu hỏi đó dựa trên kết quả Q1 FY2027 của Marvell. Các hub liên quan: [Hub AI HBM](/page/korea-semiconductor-hbm-kospi-hub/), [Hub Substrate·PCB AI](/page/korea-ai-pcb-substrate-hub/), [Hub Chuỗi giá trị bán dẫn Hàn Quốc](/page/korea-semiconductor-equipment-ip-hub/).

## TL;DR

Điểm mấu chốt của Marvell Q1 FY2027 không phải là EPS vượt kỳ vọng. Điểm mấu chốt là công ty đã nâng lộ trình tăng trưởng trung tâm dữ liệu AI cho FY2027–FY2028, và giải thích nguyên nhân thông qua <strong>custom XPU, optical interconnect, Ethernet switching, DCI, scale-up/scale-across networking và XPU attach</strong>.

Khi dịch sang bán dẫn Hàn Quốc, câu trả lời không đơn giản là "mua thêm HBM". HBM vẫn là dòng chính, nhưng alpha gia tăng mà kết quả lần này xác nhận là <strong>nút thắt về kết nối, substrate, tính toàn vẹn nguồn điện và kiểm thử xung quanh GPU</strong>.

Thứ tự ưu tiên như sau:

| Ưu tiên | Read-through Hàn Quốc | Cổ phiếu/Nhóm chính | Nhận định |
|---:|---|---|---|
| 1 | FCBGA + MLCC máy chủ AI + Tụ điện silicon | Samsung Electro-Mechanics | Trực tiếp nhất. Tuy nhiên đã được re-rating, cần xác nhận biên lợi nhuận SiCap·FCBGA |
| 2 | HBM4, SOCAMM2, eSSD, advanced packaging | Samsung Electronics, SK Hynix | Beta HBM duy trì. Alpha mới nằm ở memory attach và packaging ngoài HBM |
| 3 | Test socket·interface cho Custom ASIC/XPU | ISC, Leeno, TSE | Cấu trúc tốt nhưng đưa vào watchlist cho đến khi xác nhận doanh thu trực tiếp |
| 4 | PCB/MLB tốc độ cao cho AI networking | ISU Petasys, Daeduck Electronics, Simtech, v.v. | Cần chọn lọc. Không phải tất cả "AI PCB" đều hưởng lợi như nhau |

Đối với bản thân Marvell, nhận định là <strong>HOLD / Buy watch</strong>. Giá tham chiếu $198,70, mục tiêu 12 tháng $225 tương ứng upside khoảng +13%. Lộ trình tăng trưởng mạnh nhưng định giá đã phản ánh kỳ vọng cao. Về phía Hàn Quốc, điều quan trọng hơn Marvell là <strong>nút thắt mà Marvell xác nhận sẽ lan sang đâu</strong>.

---

## 1. Điều Thực Sự Cần Chú Ý Trong Kết Quả Marvell

Marvell công bố kết quả Q1 FY2027 sau giờ giao dịch tại Mỹ ngày 27 tháng 5 năm 2026. Các con số chính thức như sau. ([Marvell][1])

| Chỉ tiêu | Q1 FY2027 | Diễn giải |
|---|---:|---|
| Doanh thu | <strong>$2,418B</strong> | +28% so với cùng kỳ, vượt điểm giữa guidance +$18M |
| GAAP EPS | <strong>$0,04</strong> | Thấp do tác động kế toán từ việc mua lại Celestial AI·XConn |
| Non-GAAP EPS | <strong>$0,80</strong> | Sát consensus |
| GAAP gross margin | <strong>52,1%</strong> | Cải thiện so với cùng kỳ |
| Non-GAAP gross margin | <strong>58,9%</strong> | Duy trì cuối vùng 58% dù AI mix tăng |
| Dòng tiền hoạt động | <strong>$638,8M</strong> | Dòng tiền hoạt động kỷ lục |
| Guidance doanh thu Q2 | <strong>$2,70B ±5%</strong> | Biên độ $2,565B–$2,835B |
| Guidance Non-GAAP EPS Q2 | <strong>$0,93 ±$0,05</strong> | Baseline lợi nhuận quý tới |

Kết quả bản thân gần với "beat nhẹ / EPS sát kỳ vọng". Tuy nhiên, điều quan trọng đối với cổ phiếu và read-through bán dẫn Hàn Quốc không phải là vài cent trong Q1, mà là <strong>lộ trình doanh thu FY2027–FY2028 mà ban lãnh đạo đề cập</strong>.

Theo transcript từ bên thứ ba, ban lãnh đạo đặt mục tiêu doanh thu FY2027 khoảng $11,5B và FY2028 khoảng $16,5B, đồng thời nâng dự báo tăng trưởng interconnect FY2027 từ khoảng 50% lên hơn 70%. Dù đây không phải transcript IR chính thức, định hướng nhất quán với nội dung trong thông cáo chính thức của công ty. Thông cáo chính thức của Marvell cũng nêu rõ các động lực tăng trưởng gồm 800G·1,6T optics, 51,2T Ethernet switches, scale-up optical cho NPO/CPO, DCI modules, custom XPU và XPU-attach. ([Marvell][1], [StockAnalysis transcript][2])

Tóm lại trong một câu:

> Marvell xác nhận bằng con số rằng capex trung tâm dữ liệu AI đang chuyển dịch từ mua GPU sang xây dựng cơ sở hạ tầng kết nối cluster.

---

## 2. Điểm Cốt Lõi Là Cấu Trúc Kết Nối, Không Phải SOCAMM

Sai lầm diễn giải nguy hiểm nhất khi nhà đầu tư Hàn Quốc đọc cuộc gọi lần này là chỉ nhìn qua lăng kính "theme SOCAMM". SOCAMM quan trọng, nhưng không phải trọng tâm của cuộc gọi Marvell.

Trọng tâm theo thứ tự:

| Trụ cột chính của Marvell | Tại sao quan trọng | Dịch sang bán dẫn Hàn Quốc |
|---|---|---|
| Custom XPU / custom ASIC | Tín hiệu hyperscaler tăng silicon AI nội bộ ngoài GPU NVIDIA | Đa dạng hóa khách hàng HBM, substrate đóng gói, test socket |
| Optical interconnect | 800G/1,6T, DCI, scale-up optics là nút thắt mở rộng AI cluster | PCB tốc độ cao·quang học cần chọn lọc; FCBGA·ổn định hóa điện SEMCO mang tính cấu trúc |
| Ethernet switching | Roadmap 51,2T, 100T, 200T tăng dollar content trong silicon AI networking | FCBGA cho network ASIC, bo mạch tốc độ cao, kiểm tra·kiểm thử |
| XPU attach | CXL, NIC, memory attach, inference KV cache kết nối | SOCAMM2·eSSD·server DRAM Samsung Electronics, các tùy chọn memory IP như OpenEdges |
| NVLink Fusion | Con đường để custom silicon cùng tồn tại trong hệ sinh thái NVIDIA | Mở rộng chuỗi cung ứng thay vì nhị phân "NVIDIA vs ASIC" |

Thông báo hợp tác NVIDIA–Marvell cũng đi cùng hướng. NVIDIA đầu tư 2 tỷ USD vào Marvell, và Marvell cung cấp custom XPU tương thích NVLink Fusion cùng scale-up networking. Hai công ty cũng hợp tác trong silicon photonics và AI-RAN. ([Marvell NVIDIA][3])

Ý nghĩa rất đơn giản:

> Trung tâm dữ liệu AI không phải là một hộp GPU — mà là hệ thống trong đó GPU, custom XPU, HBM, optical, switch, retimer, CXL, NIC, FCBGA và MLCC vận hành như một thể thống nhất.

Do đó, đầu tư bán dẫn Hàn Quốc cần chuyển từ "chỉ nhìn vào cổ phiếu bộ nhớ lớn" sang "nút thắt nào dưới lớp bộ nhớ đang chuyển thành con số thực?".

---

## 3. Read-through Bán Dẫn Hàn Quốc Ưu tiên 1: Samsung Electro-Mechanics

Khi dịch kết quả Marvell sang cổ phiếu Hàn Quốc một cách rõ ràng nhất, đó là Samsung Electro-Mechanics (SEMCO). Có ba lý do.

Thứ nhất, custom XPU, Ethernet switch, optical interconnect và XPU attach mà Marvell nhấn mạnh đều đòi hỏi package và substrate tốc độ cao, mật độ cao. Điều này kết nối với nhu cầu FC-BGA.

Thứ hai, máy chủ AI sử dụng dòng điện lớn ở điện áp thấp trong thời gian ngắn. Để giảm dao động điện áp xung quanh package GPU·HBM·XPU, cần các linh kiện ổn định hóa nguồn như MLCC và tụ điện silicon.

Thứ ba, Samsung Electro-Mechanics đã sở hữu cả hai lớp này. Công ty công bố trong kết quả Q1 2026 rằng doanh thu Package Solution đạt 725 tỷ KRW, tăng 45% so với cùng kỳ và 12% so với quý trước, đồng thời đề cập đến việc mở rộng cung cấp substrate cao cấp cho AI accelerator, server CPU và mạng lưới. ([Samsung Electro-Mechanics Q1][4])

Ngoài ra, Samsung Electro-Mechanics đã ký hợp đồng cung cấp tụ điện silicon (SiCap) trị giá 1,557 nghìn tỷ KRW với một tập đoàn lớn toàn cầu. Thời hạn hợp đồng từ ngày 1 tháng 1 năm 2027 đến ngày 31 tháng 12 năm 2028. Linh kiện này được mô tả là dùng để tăng cường ổn định nguồn điện bên trong package GPU·HBM cho máy chủ AI. ([Samsung Electro-Mechanics SiCap][5])

Luận điểm đầu tư cho Samsung Electro-Mechanics nay đã thay đổi như sau:

| Khung cũ | Khung hiện tại |
|---|---|
| Cổ phiếu chu kỳ MLCC·module camera smartphone | Nền tảng tính toàn vẹn nguồn điện AI package + FCBGA |
| Phục hồi nhu cầu di động | Nhu cầu AI accelerator·server CPU·network ASIC |
| Chu kỳ MLCC phổ thông | MLCC/SiCap mix dung lượng cao·điện trở thấp·siêu mỏng·độ tin cậy cao |
| So sánh với một trong Ibiden/Murata | So sánh hybrid MLCC + FCBGA + SiCap |

Tuy nhiên kết luận này khác với "mua ở bất kỳ giá nào". Samsung Electro-Mechanics đã phản ánh đáng kể hợp đồng SiCap, vốn hóa 100 nghìn tỷ KRW và việc re-rating cơ sở hạ tầng AI. Do đó, biến số xác nhận tiếp theo không phải là đà tăng giá mà là <strong>tỷ suất lợi nhuận gộp, OPM Package Solution, tỷ lệ lợi nhuận sản xuất SiCap và đa dạng hóa khách hàng bổ sung</strong>.

---

## 4. Samsung Electronics·SK Hynix: Duy trì Beta HBM, Alpha Mới Nằm Ở Ngoại Vi HBM

Kết quả Marvell không tiêu cực với HBM — thực ra ngược lại. Dù custom XPU và scale-up networking tăng, dollar content bộ nhớ không giảm. Khi các mô hình AI chuyển sang agentic AI, reasoning và mixture-of-experts, yêu cầu di chuyển dữ liệu và bộ nhớ càng tăng.

Tuy nhiên từ góc độ đầu tư, "HBM tốt" đã là thesis trung tâm. Thông tin mới mà cuộc gọi Marvell cung cấp là:

1. Cơ sở khách hàng HBM mở rộng từ cấu trúc GPU NVIDIA đơn lẻ sang custom XPU của hyperscaler.
2. XPU attach kết nối với CXL, NIC, memory attach và KV cache, ảnh hưởng đến server DRAM·SOCAMM·eSSD.
3. Khi AI cluster lớn hơn, giá trị của packaging·substrate·ổn định hóa điện kết nối bộ nhớ và chip tính toán tăng lên.

Samsung Electronics có nhiều lựa chọn phức hợp ở điểm này. HBM4, HBM4E, SOCAMM2, SSD PM1763, foundry và advanced packaging đều nằm trong cùng một AI infrastructure stack. Samsung Electronics đã trình bày HBM4E, SOCAMM2, SSD PM1763 và nhiều sản phẩm khác tại GTC 2026 như danh mục AI infrastructure hợp tác với NVIDIA. ([Samsung Semiconductor][6])

SK Hynix vẫn là pure beta HBM mạnh nhất. Tuy nhiên nếu chỉ xét kết quả Marvell, alpha mới lớn hơn ở <strong>Samsung Electro-Mechanics, test socket và substrate tốc độ cao tăng trưởng song hành với HBM</strong> so với SK Hynix. SK Hynix là dòng chính nhưng đã là vị trí được thị trường chú ý nhiều nhất.

---

## 5. Test Socket: Người Hưởng Lợi Thầm Lặng Từ Sự Lan Rộng Custom ASIC

Lý do custom revenue quan trọng trong cuộc gọi Marvell không chỉ là khối lượng chip đơn giản. Điểm mấu chốt là <strong>SKU và chu kỳ qualification</strong>.

Nếu AI accelerator chuẩn hóa vào một GPU NVIDIA duy nhất, nhu cầu linh kiện kiểm thử cũng tương đối có thể dự đoán. Ngược lại, nếu custom XPU theo hyperscaler, XPU attach, CXL, NIC, switch ASIC và DPU tăng lên, điều kiện kiểm thử và thiết kế socket sẽ phân mảnh hơn.

Trong trường hợp này, test socket và linh kiện interface có thể cải thiện đồng thời ba yếu tố:

| Biến số | Hướng | Lý do |
|---|---|---|
| Số lượng | Tăng | Tăng SKU custom ASIC, network ASIC, memory attach |
| ASP | Tăng | Độ khó kiểm thử tăng với pin count cao·tín hiệu tốc độ cao·công suất cao |
| Chu kỳ thay thế | Mang tính cấu trúc | Lặp lại thay thế thế hệ và qualification theo khách hàng |

Tại Hàn Quốc, ISC, Leeno và TSE nằm trong watchlist. Tuy nhiên ở đây cần hạ mức độ tự tin. Việc xác định liệu các nhà cung cấp test socket Hàn Quốc có tham gia trực tiếp vào chuỗi custom XPU của Marvell hoặc hyperscaler cụ thể hay không là khó khẳng định chỉ từ tài liệu công khai. Do đó hiện tại đây là <strong>"khả năng hưởng lợi"</strong>, không phải <strong>"xác nhận mapping khách hàng"</strong>.

Các chỉ số cần xác nhận trong kết quả hàng quý: doanh thu logic AI/HPC, số khách hàng mới, mix socket cao cấp và phòng thủ OPM.

---

## 6. PCB Thông Thường Không Phải Đối Tượng Mua Không Phân Biệt

Kết quả Marvell tích cực cho AI networking và optical interconnect. Tuy nhiên kết luận "AI networking tốt → tất cả PCB đều tốt" là nguy hiểm.

Lợi ích tập trung vào các công ty đáp ứng các điều kiện sau, không phải PCB thông thường:

1. Phải xử lý được vật liệu tổn hao thấp cho tín hiệu tốc độ cao.
2. Phải có exposure vào MLB nhiều lớp hoặc substrate đóng gói cao cấp.
3. Phải được chứng nhận bởi khách hàng máy chủ AI·thiết bị mạng.
4. Tăng ASP·số lớp·diện tích phải được xác nhận, không chỉ tăng khối lượng.

Việc GPU và XPU tăng không có nghĩa số lượng substrate tăng theo cùng tỷ lệ. Trong cấu trúc mà nhiều chip được đóng gói dày đặc hơn trong một package và bo mạch hiệu năng cao, <strong>diện tích substrate, số lớp, độ khó vật liệu và tỷ lệ lợi nhuận sản xuất</strong> quan trọng hơn số lượng.

Do đó việc gộp ISU Petasys, Daeduck Electronics, Simtech, TLB và Korea Circuit vào cùng một rổ là không chính xác. Read-through thực tế từ kết quả Marvell gần hơn với "chọn lọc những công ty có substrate nhiều lớp cho mạng lưới và vật liệu đáp ứng tín hiệu tốc độ cao".

---

## 7. Định Giá Bản Thân MRVL: Công Ty Tốt Và Giá Tốt Là Hai Chuyện Khác

Nhận định về bản thân Marvell là HOLD / Buy watch.

| Chỉ tiêu | Nội dung |
|---|---:|
| Giá tham chiếu | $198,70, giá đóng cửa phiên thường ngày 27-05-2026 |
| Mục tiêu 12 tháng | $225 |
| Upside | \~+13,2% |
| Khung định giá | FY2028E EV/Sales |
| Nhận định cốt lõi | Lộ trình tăng trưởng được nâng lên nhưng định giá cũng đã cao |

Công thức base case:

```text
Giá mục tiêu = (Doanh thu FY2028E × Mục tiêu EV/Sales - Nợ ròng) ÷ Số cổ phiếu pha loãng
```

Giả định: doanh thu FY2028E $16,5B, mục tiêu EV/Sales 12,5x, nợ ròng \~$1,117B, cổ phiếu pha loãng 915M. Kết quả cho giá mục tiêu \~$224, làm tròn là $225.

Để Marvell được re-rating như Broadcom, cần ba điều:

1. Custom silicon revenue phải được xác nhận là chương trình lặp lại, không phải sự kiện khách hàng đơn lẻ.
2. Non-GAAP gross margin phải được bảo vệ trong vùng 58–59% dù interconnect và switching tăng trưởng.
3. Khoản trả trước để đảm bảo chuỗi cung ứng phải chuyển thành doanh thu ramp thực tế và FCF.

Tóm lại, công ty đã trở thành công ty tốt — nhưng liệu đây có phải mức giá vào lệnh tốt hay không là câu hỏi khác.

---

## 8. Các Điểm Kiểm Tra Tiếp Theo

| Điểm kiểm tra | Tín hiệu mạnh | Tín hiệu yếu |
|---|---|---|
| Doanh thu Q2 FY2027 | Tiếp cận hoặc vượt mức trên $2,835B | Dưới điểm giữa $2,70B |
| Doanh thu Data Center | Tăng trưởng high-teens trở lên so với quý trước | Tăng trưởng tuần tự chậm lại |
| Non-GAAP GM | Trên 59,25% hoặc bảo vệ biên trên | Dưới 58,25% |
| Interconnect | Duy trì·nâng dự báo FY2027 +70% trở lên | Ramp 800G/1,6T chậm lại |
| Custom XPU | Tăng trưởng 2x trở lên FY2028·tầm nhìn FY2029 $10B+ | Chậm trễ ramp theo khách hàng |
| Scale-up switching | Sản xuất hàng loạt với khách hàng tier-1 được cụ thể hóa | Nhiều engagement nhưng không có doanh thu |
| Read-through Hàn Quốc | Xác nhận số liệu Package Solution·SiCap·FCBGA của Samsung Electro-Mechanics | Theme mạnh nhưng không có biên lợi nhuận·đơn hàng |

Biến số xác nhận cho từng cổ phiếu Hàn Quốc đơn giản hơn:

| Cổ phiếu/Nhóm | Cần xác nhận |
|---|---|
| Samsung Electro-Mechanics | Tăng trưởng Package Solution, doanh thu FCBGA cho AI network, tỷ lệ lợi nhuận·biên SiCap sản xuất hàng loạt, hợp đồng dài hạn bổ sung |
| Samsung Electronics | Chứng nhận khách hàng HBM4, xuất hàng thực tế SOCAMM2, giá·khối lượng eSSD, khách hàng foundry/packaging |
| SK Hynix | Ramp HBM4, đa dạng hóa khách hàng, khả năng dư cung năm 2027 |
| ISC·Leeno·TSE | Doanh thu test socket AI logic, khách hàng mới, mix cao cấp, OPM |
| PCB/MLB | Chứng nhận khách hàng AI network, tăng ASP, vật liệu tổn hao thấp·tăng số lớp |

---

## 9. Điều Kiện Vô Hiệu Hóa Thesis

Các điều kiện làm suy yếu thesis này rõ ràng như sau:

1. Doanh thu Q2 Marvell dưới điểm giữa $2,70B và tăng trưởng Data Center chậm lại.
2. Non-GAAP gross margin giảm xuống dưới 58,25%, xác nhận custom/interconnect mix gây pha loãng biên.
3. Dự báo doanh thu FY2028 $16,5B bị hạ xuống.
4. Custom XPU và XPU attach bị ràng buộc bởi sự chậm trễ lịch trình của khách hàng cụ thể.
5. SiCap của Samsung Electro-Mechanics được xác nhận là doanh thu biên thấp hoặc tốc độ tăng trưởng FCBGA chậm lại.
6. Kết quả của nhà cung cấp test socket không cho thấy doanh thu logic AI/HPC tăng.
7. Lead time HBM rút ngắn và xuất hiện tín hiệu dư cung năm 2027.

---

## Diễn Giải Cuối Cùng

Marvell Q1 FY2027 không phải là tín hiệu "chỉ mua HBM" đối với bán dẫn Hàn Quốc. Thông điệp chính xác hơn là:

> Khi AI cluster càng lớn, nút thắt chuyển từ GPU xuống kết nối, substrate, ổn định hóa nguồn điện và kiểm thử.

Từ góc độ này, cổ phiếu Hàn Quốc trực tiếp nhất là Samsung Electro-Mechanics. SEMCO có MLCC, FC-BGA và tụ điện silicon đều nằm trong cùng nút thắt AI package. Samsung Electronics và SK Hynix tiếp tục quan trọng là dòng chính HBM, nhưng alpha mới mà kết quả Marvell tạo ra lớn hơn ở ngoại vi HBM. ISC·Leeno·TSE là ứng viên hưởng lợi thứ cấp từ sự lan rộng custom ASIC, nhưng watchlist là đúng cho đến khi xác nhận doanh thu trực tiếp.

Kết luận không phải là mua không phân biệt. Dù thesis tốt, nếu không được xác nhận bằng con số thì chỉ kết thúc như một theme. Sau quý này, điều cần theo dõi trong bán dẫn Hàn Quốc không phải là giá cổ phiếu mà là <strong>doanh thu Package Solution, biên SiCap, doanh thu kiểm thử AI logic và ASP substrate tốc độ cao</strong>.

---

## Fact / Inference / Speculation / Blocked

### [Fact]

- Doanh thu Marvell Q1 FY2027 là $2,418B, tăng +28% so với cùng kỳ; guidance doanh thu Q2 là $2,70B ±5%. ([Marvell][1])
- Non-GAAP gross margin Q1 Marvell là 58,9%; guidance non-GAAP gross margin Q2 là 58,25–59,25%. ([Marvell][1])
- Marvell đề cập các động lực tăng trưởng gồm 800G/1,6T scale-out optics, 51,2T Ethernet switches, scale-up optical, DCI modules, custom XPU và XPU-attach. ([Marvell][1])
- NVIDIA đầu tư 2 tỷ USD vào Marvell; Marvell thông báo cung cấp custom XPU tương thích NVLink Fusion và scale-up networking. ([Marvell NVIDIA][3])
- Doanh thu Package Solution Q1 2026 của Samsung Electro-Mechanics đạt 725 tỷ KRW, tăng 45% so với cùng kỳ và 12% so với quý trước. ([Samsung Electro-Mechanics Q1][4])
- Samsung Electro-Mechanics đã ký hợp đồng cung cấp tụ điện silicon trị giá 1,557 nghìn tỷ KRW, thời hạn từ 1 tháng 1 năm 2027 đến 31 tháng 12 năm 2028. ([Samsung Electro-Mechanics SiCap][5])

### [Inference]

- Hợp lý khi dịch các trục tăng trưởng của Marvell sang Hàn Quốc theo thứ tự: FCBGA/MLCC/SiCap của Samsung Electro-Mechanics, memory attach của Samsung Electronics·SK Hynix, test socket và substrate tốc độ cao.
- HBM vẫn là dòng chính, nhưng alpha gia tăng mà kết quả lần này cho thấy lớn hơn ở lớp kết nối·đóng gói·ổn định hóa điện·kiểm thử so với cổ phiếu bộ nhớ lớn.
- Việc re-rating Samsung Electro-Mechanics nên được nhìn nhận là chuyển đổi sang nền tảng passive/substrate AI infra, không phải phục hồi MLCC.

### [Speculation]

- Khách hàng SiCap của Samsung Electro-Mechanics được thị trường suy đoán là kết nối với hyperscaler Bắc Mỹ hoặc chuỗi cung ứng AI accelerator cụ thể, nhưng đối tác hợp đồng chưa được công bố.
- Việc các nhà cung cấp test socket Hàn Quốc tham gia trực tiếp vào chương trình custom XPU của Marvell hoặc khách hàng của Marvell không thể xác định chỉ từ tài liệu công khai.
- AI-RAN có thể tạo ra cơ hội bán dẫn RF·mạng lưới Hàn Quốc trong dài hạn, nhưng còn quá sớm để coi là động lực kết quả ngắn hạn năm 2026.

### [Blocked]

- Việc cung cấp trực tiếp của các công ty Hàn Quốc cho từng chương trình custom XPU·optical·switch của Marvell.
- Tên khách hàng, biên lợi nhuận theo sản phẩm và tốc độ ramp hàng tháng của hợp đồng SiCap Samsung Electro-Mechanics.
- Tỷ trọng doanh thu theo khách hàng AI logic của ISC·Leeno·TSE.
- NTM PER, EV/EBITDA và tỷ lệ điều chỉnh EPS consensus thời gian thực hiện tại của cổ phiếu PCB/substrate Hàn Quốc năm 2026.

---

## Sources

[1]: https://investor.marvell.com/news-events/press-releases/detail/1023/marvell-technology-inc-reports-first-quarter-of-fiscal-year-2027-financial-results "Marvell Technology, Inc. Reports First Quarter of Fiscal Year 2027 Financial Results"
[2]: https://stockanalysis.com/stocks/mrvl/transcripts/583849-q1-2027/ "Marvell Technology Q1 2027 Earnings Call Transcript & Audio"
[3]: https://investor.marvell.com/news-events/press-releases/detail/1019/nvidia-ai-ecosystem-expands-as-marvell-joins-forces-through-nvlink-fusion "NVIDIA AI Ecosystem Expands as Marvell Joins Forces Through NVLink Fusion"
[4]: https://m.samsungsem.com/global/newsroom/news/view.do?id=10266 "Samsung Electro-Mechanics Announces Q1 2026 Business Performance"
[5]: https://samsungsem.com/global/newsroom/news/view.do?id=10310 "Samsung Electro-Mechanics Signs 1.5 Trillion KRW Silicon Capacitor Supply Contract"
[6]: https://semiconductor.samsung.com/news-events/news/samsung-unveils-hbm4e-showcasing-comprehensive-ai-solutions-nvidia-partnership-and-vision-at-nvidia-gtc-2026/ "Samsung Unveils HBM4E at NVIDIA GTC 2026"

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
