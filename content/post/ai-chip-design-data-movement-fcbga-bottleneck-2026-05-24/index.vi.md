---
title: "Sau NVIDIA, Nút Thắt Cổ Chai Trong Chip AI Là Di Chuyển Dữ Liệu, HBM, FC-BGA Và Độ Ổn Định Nguồn Điện"
date: 2026-05-24T19:20:00+09:00
description: "Tổng hợp từ buổi phỏng vấn Reiner Pope của Dwarkesh Patel về thiết kế chip, thảo luận của All-In về NVIDIA và hạ tầng AI, cùng debate của 20VC về thị trường vốn liên quan đến Anthropic, Cerebras và SpaceX. Điểm mấu chốt: hạ tầng AI không còn chỉ là câu chuyện GPU nữa. Nhà đầu tư cần theo dõi di chuyển dữ liệu, HBM, substrate đóng gói, Ethernet và kết nối quang, độ ổn định nguồn điện và kiểm thử. Tại Hàn Quốc, chuỗi liên kết chạy từ bộ nhớ Samsung Electronics và SK Hynix đến FC-BGA và tụ silicon của Samsung Electro-Mechanics, rồi vào Daeduck, Isu Petasys, Simmtech, Korea Circuit, TLB và test socket."
categories: ["Market-Outlook"]
tags:
  - "NVIDIA"
  - "Marvell"
  - "Samsung Electro-Mechanics"
  - "Samsung Electronics"
  - "SK Hynix"
  - "HBM"
  - "FC-BGA"
  - "substrate AI"
  - "hạ tầng AI"
  - "chuỗi giá trị bán dẫn"
slug: ai-chip-design-data-movement-fcbga-bottleneck-2026-05-24
valley_cashtags:
  - NVIDIA
  - Marvell
  - 삼성전기
  - 삼성전자
  - SK하이닉스
  - 대덕전자
  - 이수페타시스
  - 심텍
  - 코리아써키트
  - 티엘비
draft: false
---

> Chuỗi bài liên quan
> [NVIDIA Q1 FY27 và chuỗi cung ứng hạ tầng AI Hàn Quốc](/post/nvidia-q1-fy27-korea-ai-infra-supply-chain-2026-05-21/) / [Xem trước kết quả kinh doanh Marvell và Broadcom](/post/marvell-broadcom-earnings-korea-ai-bottleneck-preview-2026-05-23/) / [Samsung Electro-Mechanics ký hợp đồng tụ silicon 1,5 nghìn tỷ KRW](/post/samsung-electro-mechanics-silicon-capacitor-1p5tn-2026-05-21/) / [Giải thích MLCC và tụ silicon](/post/mlcc-silicon-capacitor-ai-package-power-integrity-2026-05-22/) / [Luận điểm định giá lại Samsung Electronics](/post/samsung-electronics-tsmc-rerating-thesis-2026-05-16/) / [Hub PCB và substrate AI Hàn Quốc](/page/korea-ai-pcb-substrate-hub/)

## TL;DR

Quan trọng nhất trong ba video là buổi phỏng vấn Reiner Pope của Dwarkesh Patel. Nó không bắt đầu bằng các tiêu đề thị trường. Nó bắt đầu bằng những gì thực sự xảy ra bên trong chip: dòng điện chạy đâu, dữ liệu nằm ở đâu, và chip phải di chuyển dữ liệu đó bao nhiêu lần.[^dwarkesh]

Điểm mấu chốt rất đơn giản. Hiệu năng AI không chỉ phụ thuộc vào FLOPS. Nút thắt cổ chai thực sự là <strong>dữ liệu đến từ đâu, được lưu trữ ở đâu, và con đường giữa bộ nhớ và tính toán ngắn đến mức nào</strong>. Với khung nhìn đó, NVIDIA vẫn là trung tâm, nhưng luận điểm đầu tư lan rộng sang HBM, substrate đóng gói, FC-BGA, PCB nhiều lớp, Ethernet, kết nối quang, linh kiện ổn định nguồn và kiểm thử.

Với nhà đầu tư Hàn Quốc, hướng đọc rất rõ ràng. <strong>Samsung Electronics và SK Hynix là lõi bộ nhớ. Samsung Electro-Mechanics là nút FC-BGA và ổn định nguồn bằng tụ silicon. Daeduck, Isu Petasys, Simmtech, Korea Circuit và TLB là các cổ phiếu phân tán trong substrate và PCB.</strong> Đây không phải thị trường để đuổi theo khoảng gap thứ Hai. Điều then chốt là liệu khối lượng giao dịch và dòng tiền ngoại/tổ chức có duy trì đến buổi chiều hay không.

---

## 1. Tại Sao Buổi Phỏng Vấn Reiner Pope Quan Trọng

Sai lầm phổ biến trong đầu tư bán dẫn AI là đọc hiệu năng chip theo kiểu "nhiều FLOPS hơn đồng nghĩa chip tốt hơn." Giải thích của Reiner Pope phá vỡ khung tư duy đó từ nền tảng.

Phần lớn tính toán AI là phép nhân ma trận lặp đi lặp lại: nhân nhiều số, cộng lại, rồi làm lại. Làm cho đơn vị số học nhanh hơn là quan trọng, nhưng ở cấp độ chip, câu hỏi lớn hơn thường là <strong>những con số đó đến từ đâu</strong>.

Một chip AI có nhiều tầng lưu trữ và di chuyển.

| Vị trí | Mô tả dễ hiểu | Hàm ý đầu tư |
|---|---|---|
| Register và SRAM | Bàn làm việc bên trong chip | Rất nhanh, nhưng diện tích tốn kém |
| HBM | Kho tốc độ cao cạnh GPU | Nút thắt băng thông; SK Hynix và Samsung Electronics |
| Substrate đóng gói / interposer | Nền kết nối chip và bộ nhớ | FC-BGA, ABF, substrate tiên tiến |
| Bo mạch server và mạng | Đường xá trong và ngoài rack | PCB nhiều lớp, Ethernet, kết nối quang |
| Nguồn điện data center | Điện cho toàn hệ thống | Biến áp, phân phối, làm mát, tổng chi phí vận hành |

Nếu đơn vị số học phải chờ dữ liệu, chip bị sử dụng kém hiệu quả. Vậy câu hỏi thực sự về chip AI không chỉ là "có thể thêm nhiều tính toán hơn không?" Mà là <strong>"có thể di chuyển ít dữ liệu hơn, giữ nó gần hơn, và nuôi chip mà không lãng phí điện không?"</strong>

Đó là lý do tại sao HBM, FC-BGA, tụ silicon và PCB tốc độ cao cùng thuộc một cuộc thảo luận. Tất cả đều giải quyết cùng một vấn đề vật lý: <strong>giữ cho chip AI được cung cấp dữ liệu và nguồn điện ổn định</strong>.

---

## 2. Tại Sao Tính Toán Độ Chính Xác Thấp Dẫn Đến Substrate Và Nguồn Điện

Luận điểm của Reiner Pope về độ chính xác thấp không chỉ đơn giản là FP8 hay FP4 tăng gấp đôi tốc độ. Độ chính xác thấp hơn còn thay đổi diện tích, số lượng dây và nguồn điện. Ít bit hơn đồng nghĩa mạch nhỏ hơn, chuyển mạch ít hơn và năng lượng tiêu thụ mỗi phép tính thấp hơn.

Điều này quan trọng với nhà đầu tư vì độ chính xác thấp không chỉ là tính năng của GPU NVIDIA. Nếu nhiều tính toán hơn được nhồi vào cùng một ngân sách điện năng, toàn bộ hệ thống phải tiến hóa.

| Bước chuyển công nghệ | Yêu cầu hệ thống | Liên kết chuỗi cung ứng Hàn Quốc |
|---|---|---|
| Áp dụng FP8 và FP4 | Nhiều tính toán hơn trong cùng ngân sách điện | HBM4, DRAM server, SOCAMM |
| Thiết kế kiểu Tensor Core / systolic-array | Ít di chuyển dữ liệu hơn bên trong chip | HBM và kết nối đóng gói |
| GPU và ASIC lớn hơn | Die và định dạng đóng gói lớn hơn | FC-BGA, ABF, substrate tiên tiến |
| Mở rộng quy mô rack | Băng thông chip-to-chip và rack-to-rack nhiều hơn | PCB nhiều lớp, Ethernet, kết nối quang |
| Mật độ điện cao hơn | Phản ứng nhanh hơn với biến động dòng điện và nhiễu điện áp | MLCC, tụ silicon |

Vậy giá trị bán dẫn AI không kết thúc ở nhà cung cấp GPU. NVIDIA neo giữ hệ thống. Marvell và Broadcom nằm trong chip AI tùy chỉnh, kết nối, Ethernet và kết nối quang. Bộ nhớ, substrate và linh kiện ổn định nguồn của Hàn Quốc gắn kết bên dưới.

---

## 3. Con Số Của NVIDIA Mạnh. Câu Hỏi Thị Trường Đã Thay Đổi

NVIDIA công bố doanh thu Q1 FY27 là <strong>$81,6 tỷ</strong>, doanh thu Data Center là <strong>$75,2 tỷ</strong>, và hướng dẫn doanh thu Q2 là <strong>$91,0 tỷ ±2%</strong>. Theo số liệu chính thức, nhu cầu hạ tầng AI chưa hạ nhiệt.[^nvidia]

Nhưng thị trường không còn chỉ hỏi "NVIDIA có tốt không?" Điều đó đã được biết rồi. Những câu hỏi mới là:

1. Capex này có quay trở lại thành doanh thu và dòng tiền tự do cho khách hàng đám mây không?
2. Các nút thắt nguồn điện và làm mát data center có thể giải quyết không?
3. Các công ty mô hình có thể tiếp tục trả hóa đơn token cao không?
4. Làn sóng phản đối AI và quy định có làm chậm triển khai không?

Tập All-In thuộc về nhóm này. Anthropic, Karpathy, SpaceX, thu nhập NVIDIA và quy định AI đều là một phần của vấn đề lớn hơn: <strong>AI chưa kết thúc, nhưng giờ phải chứng minh hiệu quả sử dụng vốn</strong>.[^allin]

Bằng ngôn ngữ thị trường:

| Khung 2023-2025 | Khung từ 2026 trở đi |
|---|---|
| GPU khan hiếm | Di chuyển dữ liệu và nguồn điện cấp rack khan hiếm |
| HBM khan hiếm | HBM + substrate + ổn định nguồn + mạng cùng khan hiếm |
| Mô hình AI cải thiện | Sử dụng AI phải chuyển đổi thành doanh thu và dòng tiền |
| Mua NVIDIA | Theo dõi các nút thắt bên dưới NVIDIA |

---

## 4. Marvell Và Broadcom: Kết Nối Trở Thành Bài Kiểm Tra Tiếp Theo

Marvell và Broadcom là các sự kiện thu nhập tiếp theo cần theo dõi trong khung này. Cả hai đều không đơn giản là "đối thủ cạnh tranh NVIDIA." Khi data center AI mở rộng quy mô, cả hai gắn vào <strong>kết nối, chuyển mạch, tín hiệu quang và silicon AI tùy chỉnh</strong>.

Với Marvell, câu hỏi cốt lõi là liệu silicon AI tùy chỉnh và kết nối quang có đang tăng tốc thành doanh thu thực tế không. Với Broadcom, câu hỏi cốt lõi là liệu ASIC AI và mạng Ethernet AI có đang mở rộng cùng nhau không. Nếu cả hai công ty đều có tín hiệu tích cực, luận điểm đọc sang Hàn Quốc sẽ lan rộng hơn ra ngoài HBM thuần túy.

| Tín hiệu từ Mỹ | Luận điểm đọc sang Hàn Quốc |
|---|---|
| Nhu cầu chip AI tùy chỉnh | HBM, substrate đóng gói, kiểm thử |
| Tăng trưởng Ethernet AI và switch | Isu Petasys, PCB tốc độ cao, vật liệu tổn thất thấp |
| Kết nối quang và silicon photonics | Tiếp xúc quang học có chọn lọc; lợi ích gián tiếp substrate và nguồn |
| Mở rộng quy mô rack | Thiết bị điện, làm mát, chi phí vận hành data center |
| Đóng gói lớn hơn | FC-BGA Samsung Electro-Mechanics, Daeduck, Korea Circuit |

Cách đọc đúng không phải "Broadcom / Marvell tốt nghĩa là tất cả bán dẫn Hàn Quốc đều tốt." Mà là: <strong>tăng trưởng chip AI mang lại lợi ích cho các nhà cung cấp nút thắt nuôi, kết nối, ổn định và kiểm thử những chip đó.</strong>

---

## 5. Tin Từ AT&S Xác Nhận Điều Gì

Ngày 21/5/2026, AT&S thông báo mở rộng công suất substrate IC cao cấp dùng trong AI tại cơ sở Trùng Khánh, Trung Quốc. Khoản đầu tư ở mức chục triệu euro cao và được hậu thuẫn bởi các thỏa thuận khách hàng dài hạn. AT&S kỳ vọng tác động EBIT dương chục triệu euro cao trong năm tài chính 2026/27.[^ats-capacity]

Điểm mấu chốt không phải tên khách hàng. Điểm mấu chốt là <strong>công suất substrate AI hiện đang được mở rộng theo các thỏa thuận dài hạn</strong>.

AT&S cũng định vị substrate lõi kính vào tháng 4 như nền tảng thế hệ tiếp theo cho AI, điện toán hiệu năng cao, truyền thông tốc độ cao và photonics. Khi các gói đóng gói trở nên lớn hơn và phức tạp hơn, độ ổn định kích thước, chất lượng tín hiệu, hiệu quả nguồn và di chuyển dữ liệu trở thành các yếu tố giới hạn.[^ats-glass]

Điều này thẳng hàng với buổi phỏng vấn Reiner Pope. Nếu nút thắt AI là di chuyển dữ liệu, substrate và đóng gói tiên tiến không còn là linh kiện thụ động nữa. Chúng trở thành hạ tầng hiệu năng.

---

## 6. Dịch Chuyển Sang Nhóm Cổ Phiếu Hàn Quốc

### 6.1 Samsung Electronics và SK Hynix: Lõi Bộ Nhớ

Giảm chi phí di chuyển dữ liệu đòi hỏi HBM và DRAM server. Dù bộ tăng tốc là GPU hay ASIC tùy chỉnh, silicon AI hiệu năng cao đều tiêu thụ băng thông bộ nhớ.

SK Hynix là cổ phiếu tiếp xúc HBM rõ ràng nhất. Samsung Electronics là lựa chọn rộng hơn: phục hồi HBM, HBM4, DRAM server, SOCAMM, eSSD và quyền chọn foundry. Nhưng Samsung vẫn cần bằng chứng thực thi: chứng nhận khách hàng, yield và chiến thắng silicon AI cụ thể.

### 6.2 Samsung Electro-Mechanics: FC-BGA Cộng Tụ Silicon

Samsung Electro-Mechanics là một trong những nút thắt bậc hai rõ ràng nhất của Hàn Quốc trong khung này.

Thứ nhất, FC-BGA là substrate đóng gói kết nối chip hiệu năng cao với bo mạch. GPU lớn hơn, CPU, chip AI tùy chỉnh và switch ASIC đều cần substrate tiên tiến.

Thứ hai, tụ silicon ổn định nguồn điện bên trong gói đóng gói AI GPU / HBM. Samsung Electro-Mechanics đã thông báo hợp đồng cung cấp tụ silicon trị giá khoảng 1,5 nghìn tỷ KRW với một khách hàng toàn cầu lớn vào tháng 5/2026, và mô tả sản phẩm là linh kiện cải thiện độ ổn định nguồn bên trong các gói đóng gói bán dẫn hiệu năng cao như GPU server AI và HBM.[^semco-sicap]

Điểm mấu chốt không phải "nhiều nội dung MLCC hơn." Điểm mấu chốt là Samsung Electro-Mechanics có thể được phân loại lại thành <strong>công ty substrate có linh kiện ổn định nguồn trong gói đóng gói</strong>.

### 6.3 Daeduck, Isu Petasys, Simmtech, Korea Circuit và TLB

Những cái tên này không nên bị gộp chung quá lỏng lẻo.

| Nhóm | Cần theo dõi gì | Rủi ro |
|---|---|---|
| Daeduck Electronics | FC-BGA, substrate đóng gói, substrate chip AI | Bằng chứng khách hàng, yield, tỷ lệ sử dụng |
| Isu Petasys | PCB mạng nhiều lớp cao | Xác nhận dòng tiền sau đà tăng mạnh |
| Simmtech / TLB | Module bộ nhớ, SoCAMM, PCB server | Tỷ lệ doanh thu AI và bằng chứng biên lợi nhuận |
| Korea Circuit | Quyền chọn SoCAMM và FC-BGA | Thời điểm chứng nhận và doanh thu thực tế |

Cụm từ "tiếp xúc server AI" là chưa đủ. Bằng chứng nhà đầu tư cần là <strong>cung cấp trực tiếp, ASP tăng, thỏa thuận dài hạn và khả năng phục hồi biên lợi nhuận</strong>.

---

## 7. 20VC Cho Thấy Gì Về Nhiệt Độ Thị Trường Vốn

Tập 20VC thảo luận về Anthropic, Karpathy gia nhập Anthropic, Cerebras, SpaceX và chi phí token AI.[^twentyvc] Phần này ít liên quan đến vật lý bán dẫn hơn, và nhiều hơn về nhiệt độ thị trường vốn.

Tín hiệu tích cực là nhà đầu tư vẫn sẵn sàng tài trợ cho câu chuyện hạ tầng AI và phần cứng AI. Tài trợ cho lab mô hình, khẩu vị IPO phần cứng AI và kỳ vọng IPO mega-tech vẫn còn sống.

Tín hiệu tiêu cực là rủi ro tập trung. Quá nhiều vốn đang tập hợp xung quanh một số ít công ty AI và hạ tầng mega. Chi tiêu mô hình AI tư nhân cuối cùng phải vượt qua sự giám sát của thị trường đại chúng, ngân sách capex big-tech hoặc doanh thu thực sự.

Vậy bài học từ 20VC không phải "mua tiếp xúc AI tư nhân." Mà là: <strong>khẩu vị rủi ro AI vẫn còn sống, nhưng thị trường sẽ ngày càng đòi hỏi bằng chứng kiếm tiền và dòng tiền.</strong>

---

## 8. Danh Sách Kiểm Tra Thực Tế

Với thị trường Hàn Quốc tuần tới, câu hỏi không chỉ là liệu Samsung Electronics và SK Hynix có tăng không. Tín hiệu tốt hơn là liệu tiền có chảy xuống theo chuỗi hay không.

| Thứ tự | Điểm kiểm tra | Ý nghĩa |
|---:|---|---|
| 1 | Samsung Electronics và SK Hynix giữ trên khối lượng | Lõi bộ nhớ được xác nhận |
| 2 | Samsung Electro-Mechanics và Daeduck giữ sau khi mở cửa | Định giá lại FC-BGA và ổn định nguồn |
| 3 | Isu Petasys, Simmtech, TLB và Korea Circuit tham gia | Phân tán PCB và SoCAMM |
| 4 | Dòng tiền ngoại và tổ chức giữ đến buổi chiều | Tiền thật, không chỉ là giao dịch theo chủ đề |
| 5 | Thiết bị điện và hạ tầng data center tham gia | Phân tán nút thắt hạ tầng AI đầy đủ |

Kỷ luật vào lệnh quan trọng.

| Điều kiện | Đọc |
|---|---|
| Gap tăng khi mở cửa với khối lượng yếu | Không đuổi theo |
| Giữ buổi chiều với mua ngoại / tổ chức | Mở rộng danh sách theo dõi |
| Nhóm PCB tăng trong khi bộ nhớ mega yếu | Nhiều khả năng mang tính chủ đề |
| Trình tự bộ nhớ → substrate → thiết bị điện | Tín hiệu phân tán nút thắt |
| Nhãn "AI" không có doanh thu hay đơn hàng | Tránh |

---

## 9. Kết Luận

Ba video kết hợp thành một câu:

<strong>Thương vụ AI chưa kết thúc. Nó đang chuyển xuống theo chuỗi.</strong>

2023-2025 là giai đoạn GPU và HBM. Từ 2026 trở đi, các tầng tiếp theo là di chuyển dữ liệu, đóng gói, FC-BGA, Ethernet và kết nối quang, ổn định nguồn, kiểm thử và chi phí vận hành data center. NVIDIA vẫn là trung tâm. Nhưng câu hỏi của nhà đầu tư bây giờ là: "nút thắt Hàn Quốc nào biến tăng trưởng doanh thu của NVIDIA thành thu nhập của chính mình?"

Thứ tự hiện tại là:

1. <strong>Lõi bộ nhớ:</strong> Samsung Electronics, SK Hynix
2. <strong>Đóng gói và ổn định nguồn:</strong> Samsung Electro-Mechanics, Daeduck Electronics
3. <strong>PCB tốc độ cao và module:</strong> Isu Petasys, Simmtech, Korea Circuit, TLB
4. <strong>Kiểm thử và socket:</strong> ISC, LEENO Industrial, TSE
5. <strong>Điện và vận hành data center:</strong> thiết bị điện và hạ tầng làm mát

Câu đầu tư quan trọng nhất là: <strong>cạnh tranh hiệu năng AI là cạnh tranh chi phí di chuyển dữ liệu, và chi phí đó dịch chuyển thành HBM, đóng gói, substrate, mạng và nguồn điện.</strong>

Nếu sự phân tán đó được xác nhận bởi khối lượng giao dịch và dòng tiền ngoại / tổ chức, FC-BGA và PCB tốc độ cao nên được coi là nút thắt hạ tầng AI, không chỉ là một chủ đề khác.

---

## Phân Loại Bằng Chứng

### [Sự Thật]

- Buổi phỏng vấn Reiner Pope của Dwarkesh Patel giải thích thiết kế chip AI qua các phép toán MAC, di chuyển dữ liệu, số học độ chính xác thấp, cấu trúc Tensor Core / systolic-array và tổng chi phí vận hành.[^dwarkesh]
- NVIDIA công bố doanh thu Q1 FY27 là $81,6 tỷ, doanh thu Data Center là $75,2 tỷ, và hướng dẫn doanh thu Q2 là $91,0 tỷ ±2%.[^nvidia]
- AT&S thông báo ngày 21/5/2026 sẽ mở rộng công suất substrate IC AI cao cấp dựa trên các thỏa thuận khách hàng dài hạn.[^ats-capacity]
- Samsung Electro-Mechanics thông báo hợp đồng cung cấp tụ silicon trị giá khoảng 1,5 nghìn tỷ KRW và mô tả tụ silicon là linh kiện ổn định nguồn cho gói đóng gói GPU server AI và HBM.[^semco-sicap]

### [Suy Luận]

- Nút thắt chip AI đang chuyển từ đơn vị số học sang di chuyển dữ liệu và ổn định nguồn.
- Kết quả mạnh của NVIDIA có thể chảy qua sang Hàn Quốc không chỉ qua HBM, mà còn qua FC-BGA, PCB tốc độ cao, tụ silicon và test socket.
- Thu nhập Marvell và Broadcom là các điểm kiểm tra then chốt để xem "chip AI tùy chỉnh + nút thắt kết nối" có đang chuyển thành con số thực không.

### [Chưa Xác Nhận]

- Tên khách hàng chính của AT&S và cơ cấu sản phẩm chính xác.
- Liệu các công ty substrate và PCB Hàn Quốc cụ thể có trực tiếp cung cấp cho chương trình NVIDIA, Marvell hay Broadcom không.
- Khách hàng tụ silicon của Samsung Electro-Mechanics, biên lợi nhuận sản phẩm và vị trí gói đóng gói chính xác.
- Xác nhận chính thức của một số con số định giá và tài trợ công ty tư nhân được thảo luận trong All-In và 20VC.

[^dwarkesh]: Dwarkesh Patel, "Chip design from the bottom up / Reiner Pope," YouTube, 2026-05-22. https://www.youtube.com/watch?v=oIk3R-sMX5o
[^allin]: All-In Podcast, "SpaceX's $2T case, Nvidia's shock selloff, America turns on AI," YouTube, 2026-05-22. https://www.youtube.com/watch?v=HGbA6ze0_3M
[^twentyvc]: 20VC, "Andrej Karpathy joins Anthropic / Cerebras / SpaceX," YouTube, 2026-05-21. https://www.youtube.com/watch?v=z94zlbVn048
[^nvidia]: NVIDIA Investor Relations, "NVIDIA Announces Financial Results for First Quarter Fiscal 2027," 2026-05-20. https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027
[^ats-capacity]: I-Connect007, "AT&S Expands Capacity for AI Substrates," 2026-05-21. https://iconnect007.com/article/150109/ats-expands-capacity-for-ai-substrates/150106/pcb
[^ats-glass]: AT&S, "AT&S advances glass core substrates for AI, high-performance computing and photonics," 2026-04-22. https://ats.net/en/press/ats-advances-glass-core-substrates-for-ai-high-performance-computing-and-photonics/
[^semco-sicap]: Samsung Electro-Mechanics, "Samsung Electro-Mechanics Signs 1.5 Trillion KRW Silicon Capacitor Supply Contract with Global Large-Scale Company," 2026-05-20. https://samsungsem.com/global/newsroom/news/view.do?id=10310

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
