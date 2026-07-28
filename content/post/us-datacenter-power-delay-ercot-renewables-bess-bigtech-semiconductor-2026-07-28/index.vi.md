---
title: "Vì sao các trung tâm dữ liệu Mỹ đang chậm lại: Bài học từ ERCOT và lộ trình cho Big Tech cùng ngành bán dẫn"
slug: "us-datacenter-power-delay-ercot-renewables-bess-bigtech-semiconductor-2026-07-28"
date: 2026-07-28T21:45:00+09:00
description: "Phân tích kiểm chứng nguồn về các trì hoãn trung tâm dữ liệu tại Mỹ trên các khía cạnh đấu nối lưới điện, máy biến áp, tua-bin và sự phản đối tại địa phương; lý do ERCOT giảm rủi ro nhờ 40.3 GW điện mặt trời, 22.0 GW pin lưu trữ và 5.1 GW đáp ứng phụ tải; cùng ý nghĩa của nút thắt đối với cổ phiếu Big Tech, GPU, HBM, bộ nhớ và thiết bị điện."
categories: ["Phân tích độc quyền", "Triển vọng thị trường", "Phân tích công nghệ"]
tags:
  - "trung tâm dữ liệu Mỹ"
  - "hạ tầng AI"
  - "lưới điện"
  - "ERCOT"
  - "BESS"
  - "điện mặt trời"
  - "Big Tech"
  - "Nvidia"
  - "HBM"
  - "Samsung Electronics"
  - "SK hynix"
  - "thiết bị điện"
  - "Research OS"
draft: false
---

> Bối cảnh: Trong [bộ ba bài phân tích kết quả kinh doanh AI của Big Tech](/vi/post/big-tech-ai-earnings-capex-roi-memory-2028-fcf-2026-07-22/), câu hỏi then chốt của năm 2028 là liệu capex AI có thể chuyển hóa thành doanh thu và dòng tiền tự do hay không. [Xếp hạng doanh nghiệp hưởng lợi từ trung tâm dữ liệu tại Hàn Quốc](/vi/post/korea-ai-datacenter-beneficiaries-power-cooling-operator-flow-ranking-2026-07-23/) và [bản đồ nút thắt điện năng cho trung tâm dữ liệu AI](/vi/post/ai-datacenter-power-bottleneck-korea-value-chain-screen-2026-07-04/) của chúng tôi lập luận rằng các nhà cung cấp điện năng, làm mát và nguồn điện dự phòng kiếm tiền sớm hơn nhà vận hành. Báo cáo này áp dụng khuôn khổ đó cho Hoa Kỳ.

## TL;DR

- Trì hoãn trung tâm dữ liệu tại Mỹ là có thật, dù không có cơ sở dữ liệu quốc gia duy nhất nào có thể đưa ra tỷ lệ hủy bỏ mang tính kết luận. Allianz Research tóm lược rằng khoảng 12 GW công suất Mỹ dự kiến cho năm 2026 có thể bị trì hoãn hoặc hủy bỏ, trong khi chỉ khoảng 5 GW đang được xây dựng tích cực. NERC cũng xác nhận nhiều khu vực đã hạ dự báo phụ tải lớn do việc đấu nối và hoàn thành chậm hơn kỳ vọng.[^allianz][^nerc]
- Nút thắt có bốn lớp: <strong>đấu nối lưới điện, máy biến áp và máy cắt, thiết bị phát điện, cùng cấp phép địa phương và phân bổ chi phí</strong>. Cuối năm 2025, 1,312 GW phát điện và 749 GW lưu trữ đang chờ trong hàng đợi đấu nối tại Mỹ. Thời gian giao máy biến áp tăng áp cho máy phát đã vượt 160 tuần vào đầu năm 2026.[^lbl][^reuters-transformer]
- Cụm từ “hơn một nửa số bang của Mỹ đang chịu cảnh báo thiếu hụt” đã cường điệu hóa đánh giá chính thức. NERC nhận định mọi khu vực đều có đủ nguồn lực trong điều kiện đỉnh phụ tải mùa hè bình thường, nhưng xác định rủi ro tăng cao trong điều kiện cực đoan tại một số khu vực.[^nerc]
- ERCOT là bằng chứng mạnh mẽ cho luận điểm điện mặt trời kết hợp lưu trữ. NERC ghi nhận ERCOT có 40.3 GW điện mặt trời và 22.0 GW lưu trữ pin, với đóng góp đỉnh kỳ vọng lần lượt là 29.7 GW và 20.7 GW. Xác suất xảy ra Cảnh báo Khẩn cấp Năng lượng trong giờ có rủi ro cao nhất đã giảm từ 3.1% xuống 0.43%.[^nerc]
- Nhưng ERCOT không phải câu chuyện chỉ có điện mặt trời và pin. Kết quả của hệ thống này còn phản ánh 5.1 GW đáp ứng phụ tải, các phụ tải tính toán có thể cắt giảm, quy tắc thị trường nhanh hơn, và nền tảng sẵn có gồm phát điện khí đốt, hạt nhân và điện gió.
- Điện mặt trời cộng BESS là lựa chọn bổ sung nguồn cung nhanh nhất trong ba năm tới, không phải giải pháp hoàn chỉnh 24/7. Kiến trúc thực tế là <strong>điện mặt trời+BESS, PPA điện hạt nhân hoặc khí đốt hiện hữu, động cơ khí đốt hoặc pin nhiên liệu sau công tơ, và phụ tải tính toán linh hoạt</strong>.
- Với Big Tech, các trì hoãn giới hạn tăng trưởng ngắn hạn nhưng làm tăng giá trị khan hiếm của công suất đã được cấp điện. Với ngành bán dẫn, chúng vừa tạo rủi ro về thời điểm xuất hàng trong ngắn hạn, vừa có thể kéo dài chu kỳ nhu cầu 2027-2028.

<div class="thesis-callout">
  <div class="thesis-callout__label">Kết luận chính</div>
  <div class="thesis-callout__body">
    Nút thắt AI đã chuyển từ chip sang điện năng. Bài học từ ERCOT không phải là “chỉ cần năng lượng tái tạo”, mà là danh mục gồm bổ sung nguồn lực nhanh, pin, đấu nối linh hoạt, đáp ứng phụ tải và nguồn phát điện ổn định. Tác động lên cổ phiếu diễn ra theo ba đồng hồ khác nhau: trần tăng trưởng ngắn hạn đối với Big Tech, lắp đặt bán dẫn bị dời sang 2027-2028, và đơn hàng trực tiếp dành cho nhà cung cấp thiết bị điện cùng lưu trữ.
  </div>
</div>

## 0. Trước hết cần thống nhất định nghĩa

“Công suất” trung tâm dữ liệu có thể là phụ tải CNTT, tổng công suất điện của cơ sở, hoặc quy mô cuối cùng đã công bố của cả khuôn viên. “Hàng đợi” đấu nối có thể chỉ các dự án phát điện hoặc các phụ tải lớn. Trộn lẫn các khái niệm này tạo ra những con số ấn tượng nhưng gây hiểu lầm.

| Nhận định phổ biến | Kiểm tra bằng chứng | Giả định sử dụng |
|---|---|---|
| Công suất trung tâm dữ liệu hiện tại của Mỹ là 50 GW | Ước tính khác nhau theo phạm vi | Wood Mackenzie ước tính hiện tại khoảng 24 GW và đạt 110 GW vào năm 2030.[^reuters-transformer] |
| 30-50% dự án năm 2026 bị trì hoãn | Ước tính ngành, không phải điều tra dân số chính thức | Sử dụng chiều hướng, không dùng ước lượng điểm giả tạo. Allianz nói 12 GW được lên kế hoạch so với khoảng 5 GW đang xây dựng.[^allianz] |
| Một nửa số bang Mỹ đối mặt cảnh báo thiếu hụt | Mạnh hơn ngôn ngữ của NERC | Mọi khu vực đều đủ nguồn lực trong điều kiện bình thường; một số khu vực đối mặt rủi ro thời tiết cực đoan tăng cao.[^nerc] |
| ERCOT đã vượt 90 GW | Hơn 92 GW là một dự báo | Dự báo mùa hè của ERCOT vượt 92 GW; các số liệu quy hoạch đã điều chỉnh theo đáp ứng phụ tải của NERC thấp hơn.[^kera][^nerc] |
| ERCOT có 35 GW điện mặt trời và 12 GW BESS | Đúng về xu hướng nhưng đã cũ | NERC ghi nhận 40.3 GW điện mặt trời và 22.0 GW BESS cho năm 2026.[^nerc] |
| Hàng đợi Mỹ là 2.6 TW | Phụ thuộc vào thời điểm và phạm vi | Hàng đợi phát điện và lưu trữ đang hoạt động vào cuối năm 2025 đạt tổng cộng 2.061 TW. Đây không phải bản thân hàng đợi phụ tải trung tâm dữ liệu.[^lbl] |

## 1. Mức độ trì hoãn lớn đến đâu?

Không có cơ sở dữ liệu dự án trung tâm dữ liệu toàn diện tại Mỹ. Một khuôn viên đơn lẻ có thể có công suất cuối cùng được công bố, công suất tòa nhà đầu tiên nhỏ hơn, và nhiều mốc cấp điện theo từng giai đoạn. “Trì hoãn”, “hủy bỏ”, “tạm dừng” và “giữ đất nhưng chưa có điện” không phải là một.

Tuy vậy, ba tín hiệu độc lập cùng khớp nhau:

1. Allianz Research cho biết khoảng 12 GW công suất Mỹ dự kiến cho năm 2026 có thể bị trì hoãn hoặc hủy bỏ, trong khi chỉ khoảng 5 GW đang được xây dựng tích cực.[^allianz]
2. NERC cho biết một số khu vực đánh giá đã điều chỉnh giảm dự báo phụ tải lớn vì việc đấu nối và hoàn thành chậm hơn dự kiến trước đó.[^nerc]
3. Data Center Watch, được các báo cáo truyền thông trích dẫn, đã đếm được 75 dự án trị giá khoảng $130 billion bị chặn hoặc trì hoãn trong quý đầu năm 2026.[^dcwatch]

Kết luận có thể bảo vệ không phải là chính xác một nửa sẽ biến mất. Mà là công suất AI được công bố đang tăng nhanh hơn việc cung cấp điện và xây dựng, đẩy một phần đáng kể nguồn cung năm 2026 sang năm 2027 và xa hơn.

## 2. Nút thắt bốn lớp

| Lớp | Thước đo đã xác minh | Tại sao quan trọng |
|---|---:|---|
| Đấu nối phát điện và lưu trữ | 2,061 GW đang hoạt động cuối năm 2025; thời gian trung vị đến vận hành vượt năm năm đối với các dự án hoàn thành năm 2025 | Phụ tải mới không thể mở rộng nếu thiếu nguồn cung và truyền tải. |
| Đấu nối phụ tải lớn | 36-48 tháng tại các vùng tăng trưởng trung tâm dữ liệu của PJM | Vỏ công trình hoàn thiện không thể tạo doanh thu nếu không có ngày cấp điện. |
| Máy biến áp và máy cắt | Máy biến áp tăng áp vượt 160 tuần; máy cắt điện áp cao khoảng 125 tuần | Một linh kiện thiếu có thể làm đình trệ toàn bộ trạm biến áp. |
| Cấp phép, biểu giá và phản đối địa phương | 75 dự án và $130 billion bị trì hoãn hoặc chặn trong Q1 2026 | Nước, tiếng ồn, đất đai và chuyển dịch chi phí có thể ngăn xây dựng. |

Hàng đợi phát điện và lưu trữ bao gồm khoảng 8,200 dự án. Chỉ 13% công suất đã nộp đơn từ năm 2000 đến 2020 đi vào vận hành thương mại tính đến cuối năm 2025.[^lbl] Do đó, quy mô hàng đợi không đồng nghĩa với nguồn cung tương lai.

Thiết bị là ràng buộc vật lý cấp bách hơn. Reuters đưa tin thời gian giao máy biến áp tăng áp cho máy phát vượt 160 tuần trong quý đầu năm 2026, và máy cắt điện áp cao đạt 125 tuần. Các công ty điện lực hiện đặt hàng trước nhiều năm và đôi khi trả trước để giữ suất sản xuất.[^reuters-transformer]

Tua-bin khí đốt cũng không phải là phương án thay thế tức thì. Mitsubishi Power cho biết đơn hàng kéo dài đến năm 2030 và thời gian dẫn lắp đặt đã lên năm năm hoặc hơn.[^gas-turbine]

## 3. Nút thắt đã chuyển từ rack sang trạm biến áp

Chuỗi tạo doanh thu là:

```text
Nhu cầu AI và hợp đồng khách hàng
→ thỏa thuận đất đai và điện năng
→ phê duyệt phát điện, truyền tải và trạm biến áp
→ giao máy biến áp, thiết bị đóng cắt và máy cắt
→ hoàn thành công trình, làm mát và nguồn điện dự phòng
→ lắp đặt GPU, mạng và bộ nhớ
→ chạy thử nghiệm
→ kích hoạt khối lượng công việc của khách hàng
→ ghi nhận doanh thu cloud và AI
```

Các lệnh của FERC vào tháng 6 năm 2026 gửi tới sáu đơn vị vận hành lưới điện khu vực xác nhận việc tích hợp phụ tải lớn đã trở thành một vấn đề chính sách cấp quốc gia.[^ferc]

Nhưng “thiếu phát điện” chỉ là một dạng thất bại. Một khu vực có thể có nhà máy điện nhưng không có truyền tải. Có thể có truyền tải nhưng không có máy biến áp. Có thể có thiết bị nhưng không có thỏa thuận về bên chịu chi phí. Và một phụ tải cứng nhắc 24/7 đòi hỏi hạ tầng nhiều hơn phụ tải có thể chuyển các tác vụ huấn luyện theo thời gian hoặc địa điểm.

## 4. ERCOT đã làm gì khác biệt

### 4-1. Điện mặt trời và pin tạo đóng góp có thể đo lường

Đánh giá năm 2026 của NERC ghi nhận ERCOT có 40.3 GW điện mặt trời và 22.0 GW lưu trữ pin. Đóng góp đỉnh kỳ vọng là 29.7 GW và 20.7 GW.

| Nguồn lực ERCOT | Công suất danh định | Đóng góp đỉnh kỳ vọng | Tỷ lệ đóng góp |
|---|---:|---:|---:|
| Điện gió | 40.6 GW | 9.45 GW | 23% |
| Điện mặt trời | 40.3 GW | 29.68 GW | 74% |
| BESS | 22.0 GW | 20.69 GW | 94% |

Texas đã lập kỷ lục sản lượng điện mặt trời 29.3 GW và kỷ lục xả pin 7.2 GW vào mùa hè năm 2025. Với 8.78 GW BESS được bổ sung trong năm 2025 và thêm 2.68 GW đến tháng 3 năm 2026, xác suất mô hình hóa xảy ra Cảnh báo Khẩn cấp Năng lượng trong giờ có rủi ro cao nhất giảm từ 3.1% xuống 0.43%.[^nerc]

Pin không cấp điện cho toàn bộ bang trong nhiều ngày. Chúng chuyển điện mặt trời giữa trưa sang buổi tối, phản ứng với mất cân bằng đột ngột và ổn định tần số.

### 4-2. Nguồn cung chỉ là một nửa câu trả lời

ERCOT có 5.1 GW đáp ứng phụ tải sẵn sàng cho mùa hè 2026, tăng 54.9% so với cùng kỳ. NERC cho biết có thêm phụ tải tính toán có thể được cắt giảm trong tình trạng khẩn cấp, làm giảm dự báo nhu cầu nội bộ ròng của hệ thống 3.7 GW.[^nerc]

```text
Điện mặt trời phục vụ nhu cầu ban ngày
→ pin bù cho giai đoạn tăng phụ tải buổi tối
→ khí đốt, hạt nhân và gió hỗ trợ nguồn cung ổn định và ban đêm
→ phụ tải tính toán lớn cắt giảm khi hệ thống căng thẳng
→ tín hiệu thị trường và quy tắc đấu nối nhanh thu hút nguồn lực
```

Rủi ro thấp hơn của ERCOT phản ánh mức tăng 12% nguồn lực dự kiến, nhiều BESS hơn, nhiều đáp ứng phụ tải hơn và phụ tải lớn linh hoạt. Đây không phải câu chuyện của một công nghệ duy nhất.

### 4-3. Các điểm yếu còn lại

- Giờ rủi ro cao nhất là 9 giờ tối, sau khi sản lượng điện mặt trời giảm.
- Miền Tây Texas vẫn đối mặt các hạn chế truyền tải.
- Việc ngắt đồng thời các phụ tải điện tử lớn có thể làm mất ổn định tần số và điện áp.
- Con số 92 GW là dự báo mùa hè, không phải kỷ lục thực tế.
- Công suất pin tính bằng GW nói rất ít về khả năng vượt qua các sự kiện nhiều ngày ít gió hoặc ít nắng nếu không có dữ liệu thời lượng năng lượng tính bằng GWh.

## 5. Điện mặt trời cộng BESS có phải giải pháp nhanh nhất?

Đối với nguồn điện bổ sung trong ba năm tới, có. Đối với nguồn cung hoàn chỉnh 24/7, không.

| Lựa chọn | Tốc độ đến điện lần đầu | Độ ổn định 24/7 | Ràng buộc chính | Vai trò tốt nhất |
|---|---|---|---|---|
| Solar+BESS | Nhanh | Trung bình | Đất đai, máy biến áp, thời lượng, ban đêm | Điện bổ sung nhanh và hỗ trợ giờ cao điểm |
| Động cơ khí đốt hoặc tua-bin nhỏ tại chỗ | Trung bình | Cao | Đường ống khí, giấy phép không khí, chi phí nhiên liệu | Điện cầu nối và vượt qua hàng đợi |
| Pin nhiên liệu+BESS | Trung bình | Cao | Nguồn cung nhiên liệu, chi phí thiết bị, dịch vụ | Nguồn cung mô-đun sau công tơ |
| PPA điện hạt nhân hoặc khí đốt hiện hữu | Nhanh đến trung bình | Cao | Truyền tải và cấu trúc hợp đồng | Nguồn cung ổn định |
| Nhà máy khí chu trình hỗn hợp mới | Chậm | Cao | Thời gian giao tua-bin, đường ống, giấy phép | Nguồn cung dài hạn quy mô lớn |
| Truyền tải mới | Rất chậm | Cao | Giấy phép, đất đai, phân bổ chi phí | Giải pháp cấu trúc |
| SMR hoặc điện hạt nhân mới | Rất chậm | Cao | Cấp phép, chi phí xây dựng, tiến độ | Điện ổn định trong thập niên 2030 |
| Phụ tải tính toán linh hoạt | Nhanh nhất | Không phải nguồn cung | SLA và phần mềm | Đấu nối nhanh hơn với cùng một lưới điện |

S&P Global đã mô hình hóa một trung tâm dữ liệu 627 MW và nhận thấy thiết kế điện mặt trời cộng lưu trữ có chi phí cao hơn hơn hai lần so với nhà máy chu trình hỗn hợp, trong khi vẫn không bảo đảm điện qua các giai đoạn nhiều ngày ít nắng.[^spp-solar-gas] Điều đó không phủ nhận solar+BESS. Nó xác định vai trò của giải pháp này là công suất bổ sung nhanh và công suất giờ cao điểm, thay vì giải pháp độc lập quanh năm.

Kiến trúc thực tế được triển khai theo giai đoạn:

1. <strong>Cấp điện ban đầu:</strong> điện mặt trời, BESS, động cơ tại chỗ hoặc pin nhiên liệu, dịch vụ lưới một phần và khối lượng công việc theo lô linh hoạt.
2. <strong>Ổn định:</strong> PPA dài hạn với điện hạt nhân, khí đốt hoặc thủy điện hiện hữu; nâng cấp trạm biến áp và truyền tải; lưu trữ thời lượng dài hơn.
3. <strong>Nguồn cung cấu trúc:</strong> phát điện chu trình hỗn hợp mới, truyền tải, khởi động lại điện hạt nhân, địa nhiệt, lưu trữ thời lượng dài và cuối cùng là điện hạt nhân tiên tiến.

## 6. Quy tắc và phần mềm quan trọng ngang thiết bị

Các lệnh tháng 6 của FERC yêu cầu PJM, MISO, SPP, CAISO, ISO-NE và NYISO giải trình hoặc cải cách biểu giá dành cho phụ tải lớn. Các lựa chọn bao gồm phát điện đồng vị trí, dịch vụ truyền tải linh hoạt, phát điện sau công tơ và dịch vụ tạm thời từ các máy phát điện lân cận.[^ferc]

Tài sản mới nổi là điện toán có thể cắt giảm.

| Khối lượng công việc | Độ linh hoạt điện năng | Lý do |
|---|---:|---|
| Suy luận thời gian thực | Thấp | Chi phí độ trễ và gián đoạn cao. |
| Cloud doanh nghiệp | Thấp đến trung bình | Phải bảo vệ SLA khách hàng. |
| Huấn luyện giữa các điểm kiểm tra | Trung bình | Có thể tạm dừng và khởi động lại ngắn hạn. |
| Huấn luyện theo lô và tiền xử lý | Cao | Công việc có thể chuyển đổi theo thời gian và khu vực. |
| Đào tiền mã hóa | Rất cao | Cắt giảm tương đối đơn giản. |

Không phải mọi nhu cầu AI đều linh hoạt. Nhưng nếu một phần khuôn viên có thể cắt giảm, lưới điện không còn phải xây mọi nâng cấp cho đỉnh xấu nhất xảy ra đồng thời hoàn toàn trước lần cấp điện đầu tiên.

## 7. Tác động lên cổ phiếu Big Tech

### 7-1. Kênh tiêu cực: nhu cầu đã ký hợp đồng chuyển thành doanh thu chậm hơn

```text
Trì hoãn cấp điện
→ trì hoãn kích hoạt trung tâm dữ liệu
→ công suất dịch vụ GPU vẫn bị giới hạn
→ backlog và RPO chuyển đổi chậm hơn
→ tăng trưởng cloud ngắn hạn bị chặn trần
→ khấu hao có thể bắt đầu trước khi mức sử dụng tối ưu
```

Nếu đất đai, tòa nhà và tiền đặt cọc thiết bị đã được thanh toán trước khi điện đến, dòng tiền tự do sẽ chịu áp lực. Vì vậy, câu hỏi FCF năm 2028 không chỉ là capex. Đó là công suất đã cấp điện và mức sử dụng.

### 7-2. Kênh tích cực: giá trị khan hiếm của công suất đang hoạt động

Khi nguồn cung tăng chậm hơn nhu cầu, công suất GPU đã được cấp điện trở nên giá trị hơn:

- Chiết khấu có thể giảm.
- Cam kết dài hạn và trả trước có thể tăng.
- Mức sử dụng cao hấp thụ khấu hao.
- Nhà vận hành có nguồn điện bảo đảm và đa dạng hóa địa lý sẽ gia tăng thị phần.

Trì hoãn trung tâm dữ liệu không tiêu cực như nhau với mọi hyperscaler. Chúng gây hại cho các công ty có kế hoạch lớn nhưng chưa có điện, trong khi củng cố sức mạnh định giá của các công ty có công suất đã cấp điện.

### 7-3. Bảng điểm Big Tech mới

| Chỉ số | Tín hiệu tích cực | Tín hiệu tiêu cực |
|---|---|---|
| Điện năng đã cấp | MW/GW và ngày cụ thể | Chỉ nêu quy mô khuôn viên cuối cùng |
| Nguồn cung điện | PPA đa khu vực, điện tại chỗ, hợp đồng lưới | Một công ty điện lực và một ngày xa xôi |
| Hợp đồng khách hàng | Cam kết dài hạn, trả trước, mức sử dụng tối thiểu | Mối quan tâm không ràng buộc |
| Phân kỳ capex | Đầu tư phù hợp với tiến độ cấp điện | Tòa nhà và chip chờ điện |
| Tính linh hoạt | Khối lượng công việc dịch chuyển theo thời gian và khu vực | Mọi phụ tải được coi là nhu cầu cứng nhắc 24/7 |
| Dòng tiền | Doanh thu và sử dụng vượt khấu hao | Khấu hao và lãi vay tăng trước |

Câu hỏi trong cuộc gọi kết quả kinh doanh tiếp theo nên là: bao nhiêu gigawatt có thể bật lên, khi nào, và gắn với bao nhiêu doanh thu khách hàng?

## 8. Tác động lên cổ phiếu bán dẫn

### 8-1. Rủi ro ngắn hạn: khoảng cách giữa đặt hàng và lắp đặt

Các hyperscaler có thể nhận GPU và HBM trước khi điện sẵn sàng, tạo ra tồn kho tại khách hàng, hoặc trì hoãn giao hàng để khớp với thời điểm cấp điện, tạo ra các khoảng trống xuất hàng theo quý.

Các dấu hiệu cảnh báo gồm:

- Số ngày tồn kho GPU và máy chủ tại khách hàng tăng
- Giảm tiền trả trước và lịch giao hàng kéo dài hơn
- Nhiều đề cập hơn về việc “chờ điện”
- Lượng xuất hàng của server ODM tăng nhanh hơn công suất cloud đang hoạt động
- Hợp đồng HBM còn nguyên nhưng ngày giao hàng theo quý bị lùi

“Nhu cầu bị hoãn” không tự động là tín hiệu tích cực.

### 8-2. Cơ hội trung hạn: đuôi chu kỳ dài hơn

Nếu dự án bị dời thay vì biến mất, đường cong nhu cầu có thể phẳng hơn và kéo dài hơn.

```text
Công suất trung tâm dữ liệu năm 2026 bị trượt tiến độ
→ lắp đặt GPU và HBM chuyển sang 2027-2028
→ tăng trưởng xuất hàng năm 2026 chậm lại
→ các lắp đặt bị hoãn chồng lên nhu cầu thay thế và mở rộng
→ đỉnh có thể thấp hơn, nhưng chu kỳ kéo dài hơn
```

Điều này cần ba điều kiện:

1. Nhu cầu AI cuối cùng không suy yếu.
2. Năng lực tài chính và tín dụng của hyperscaler vẫn vững.
3. Giải pháp điện đang được xây dựng thay vì chỉ được công bố.

Các trì hoãn lặp lại cùng việc AI kiếm tiền yếu hơn sẽ biến trì hoãn thành hủy bỏ.

### 8-3. Hiệu năng trên mỗi watt trở nên giá trị hơn

| Lớp bán dẫn | Tác động của khan hiếm điện |
|---|---|
| GPU và AI ASIC | Hiệu năng trên mỗi watt trở thành tiêu chí mua hàng mạnh hơn. |
| HBM | Giảm năng lượng truyền dữ liệu và tăng mức sử dụng accelerator làm gia tăng giá trị. |
| Server DRAM | Tổng chi phí sở hữu, bao gồm điện và làm mát, quan trọng hơn. |
| Enterprise SSD | Lưu trữ công suất thấp, thông lượng cao giảm thời gian GPU nhàn rỗi. |
| Mạng | Fabric nhanh hơn có giá cao hơn nhờ giảm thời gian cụm máy nhàn rỗi. |
| Bán dẫn công suất và đế nền | Phân phối và chuyển đổi điện áp cao trở thành phần lớn hơn trong giá trị hệ thống. |

Với SK hynix, kênh tích cực là lợi thế hiệu năng trên mỗi watt của HBM và server DRAM giá trị cao. Samsung Electronics kết hợp khả năng phục hồi HBM với danh mục rộng hơn về DRAM công suất thấp và enterprise SSD. Nhưng nếu trì hoãn cấp điện tạo tồn kho máy chủ và tồn kho phía khách hàng, mức độ tiếp xúc hàng hóa rộng hơn cũng có thể làm tăng độ nhạy.

## 9. Đánh giá cổ phiếu theo nhóm

| Nhóm | 0-6 tháng tới | 1-3 năm tới | Đánh giá |
|---|---|---|---|
| Hyperscaler | Giới hạn công suất kìm hãm tăng trưởng; công suất đang hoạt động giữ sức mạnh định giá | Tiếp cận điện trở thành hào kinh tế | Phân hóa giữa các công ty rộng hơn |
| GPU và AI ASIC | Rủi ro thời điểm xuất hàng theo quý | Hiệu năng trên mỗi watt và nhu cầu bị hoãn | Tích cực trung hạn, biến động ngắn hạn |
| HBM và bộ nhớ máy chủ | Nhịp độ giao hàng và tồn kho khách hàng quan trọng | Khả năng kéo dài chu kỳ | Tích cực có điều kiện |
| Thiết bị điện | Backlog và định giá vẫn mạnh | Mở rộng công suất có thể tạo cạnh tranh về sau | Hưởng lợi trực tiếp, định giá là yếu tố quan trọng |
| BESS | Nhu cầu giờ cao điểm và sau công tơ | Giá trị thời lượng dài hơn và phần mềm | Bên hưởng lợi mang tính cấu trúc |
| Tua-bin và động cơ | Đơn hàng mạnh, giao hàng chậm | Ràng buộc về đường ống và cấp phép | Backlog mạnh, doanh thu bị trì hoãn |
| Hạt nhân và địa nhiệt | Đóng góp ngắn hạn hạn chế | Phần bù giá cho điện ổn định | Thời gian dài |

Thiết bị điện là bên hưởng lợi trực tiếp rõ ràng nhất vì máy biến áp, máy cắt, thiết bị đóng cắt, cáp và pin giải quyết các nguyên nhân của trì hoãn. Nhưng backlog dài không tự động đồng nghĩa với cổ phiếu rẻ. Mở rộng sản xuất, chi phí đầu vào, tiền đặt cọc và cạnh tranh sau năm 2028 vẫn quan trọng.

Mức độ tiếp xúc của doanh nghiệp niêm yết Hàn Quốc vẫn gồm:

- Lưới điện và phân phối: LS ELECTRIC, HD Hyundai Electric, Hyosung Heavy Industries
- Cáp: Iljin Electric, Gaon Cable
- BESS và chất lượng điện: LG Energy Solution, Samsung SDI, Vinatech
- Làm mát: LG Electronics, GST
- Điện ổn định: Doosan Enerbility, SK Gas, GNC Energy

Xem [xếp hạng doanh nghiệp hưởng lợi ngày 23 tháng 7](/vi/post/korea-ai-datacenter-beneficiaries-power-cooling-operator-flow-ranking-2026-07-23/) để lựa chọn cổ phiếu dựa trên giá và dòng tiền. Báo cáo này tập trung vào thời gian kéo dài của nút thắt tại Mỹ.

## 10. Bảng điều khiển hàng tháng

| Chỉ báo | Diễn giải tích cực | Diễn giải tiêu cực |
|---|---|---|
| MW cấp điện lần đầu cho trung tâm dữ liệu | Kế hoạch trở thành công suất hoạt động | Quy mô cuối cùng tăng trong khi ngày tháng tiếp tục trượt |
| Thời gian giao máy biến áp lớn | Nút thắt và sức mạnh định giá duy trì | Thời gian giao sụp đổ do hủy dự án |
| Phê duyệt phụ tải lớn tại ERCOT và PJM | Cung cấp điện nhanh hơn | Tiến độ nghiên cứu lại kéo dài |
| Triển khai BESS và thời lượng | Phủ tốt hơn nhu cầu đỉnh buổi tối | GW cao nhưng GWh không đủ |
| Đăng ký đáp ứng phụ tải | Nhiều phụ tải hơn kết nối với cùng một lưới | Lo ngại SLA làm giảm tham gia |
| Mức sử dụng Big Tech và chuyển đổi RPO | Điện và khách hàng đến cùng lúc | RPO tăng nhưng chuyển đổi chậm |
| Tồn kho GPU và HBM tại khách hàng | Nhu cầu bị hoãn vẫn lành mạnh | Chip tích tụ vì thiếu điện |
| Tăng trưởng cloud so với khấu hao | Doanh thu vượt cơ sở chi phí | Khấu hao vượt tăng trưởng |

## 11. Red team

Luận điểm tích cực thất bại nếu:

1. Trì hoãn phản ánh nhu cầu AI yếu hơn thay vì thời điểm điện năng.
2. Backlog cloud và tiền trả trước của khách hàng giảm.
3. Tồn kho GPU và HBM tăng lên, các sản lượng đã ký hợp đồng bị hủy.
4. Mở rộng sản xuất máy biến áp và BESS tạo sụp đổ giá năm 2028.
5. Phản đối địa phương đồng thời chặn truyền tải, phát điện tại chỗ và năng lượng tái tạo.

Luận điểm tiêu cực thất bại nếu:

1. Quy tắc phụ tải linh hoạt và phát điện đồng vị trí nhanh chóng được tiêu chuẩn hóa.
2. Hợp đồng cắt giảm kiểu ERCOT lan sang PJM và MISO.
3. Điện mặt trời lai ghép, lưu trữ, động cơ và pin nhiên liệu cấp điện cho các khuôn viên lớn trong vòng hai năm.
4. Hyperscaler công bố hợp đồng khách hàng dài hạn song song với các ngày điện ổn định.
5. Hợp đồng HBM và tiền trả trước vẫn nguyên vẹn dù lịch giao hàng thay đổi.

## 12. Quan điểm cuối cùng

Các trung tâm dữ liệu Mỹ không chỉ chậm lại vì đất nước thiếu năng lượng. Những thể chế và thiết bị cần để kết nối, biến đổi, cắt giảm và phân bổ chi phí điện năng đang di chuyển chậm hơn nhu cầu AI.

Điện mặt trời cộng BESS là phản ứng bổ sung nhanh nhất. ERCOT chứng minh điều đó với 40.3 GW điện mặt trời, 22.0 GW lưu trữ pin, 50.4 GW tổng đóng góp đỉnh kỳ vọng và xác suất cảnh báo khẩn cấp được mô hình hóa là 0.43%. Nhưng bằng chứng đó cũng nhấn mạnh 5.1 GW đáp ứng phụ tải và phụ tải tính toán có thể cắt giảm.

Hàm ý đối với cổ phiếu cần được tách biệt theo thời gian:

- <strong>Big Tech, ngắn hạn:</strong> việc cung cấp điện giới hạn tăng trưởng cloud, trong khi công suất đã cấp điện hưởng giá trị khan hiếm.
- <strong>Big Tech, trung hạn:</strong> điện năng, mức sử dụng và hợp đồng khách hàng quyết định liệu dòng tiền tự do năm 2028 có phục hồi hay không.
- <strong>Bán dẫn, ngắn hạn:</strong> điều chỉnh giao hàng và tồn kho khách hàng tạo biến động.
- <strong>Bán dẫn, trung hạn:</strong> nếu trì hoãn không trở thành hủy bỏ, nhu cầu GPU và HBM có thể lan sang 2027-2028 và kéo dài chu kỳ.
- <strong>Bên hưởng lợi trực tiếp:</strong> máy biến áp, máy cắt, thiết bị đóng cắt, cáp, pin và phát điện tại chỗ giải quyết nguyên nhân vật lý của trì hoãn.

Sự phân biệt mang tính quyết định là giữa các dự án có ngày cấp điện chắc chắn và các thông báo chưa có điện, cũng như giữa nhu cầu bị hoãn được hậu thuẫn bởi hợp đồng khách hàng và nhu cầu biến mất.

> [Sự thật] Các nguồn công khai xác minh chỉ báo trì hoãn, phân loại rủi ro của NERC, nguồn lực ERCOT, hàng đợi đấu nối và thời gian giao thiết bị.  
> [Suy luận] Các lập luận về kéo dài chu kỳ và định giá khan hiếm đòi hỏi hợp đồng khách hàng cùng nhu cầu AI cuối cùng phải duy trì.  
> [Bị chặn] Ngày cấp điện ở cấp độ dự án, hiệu quả kinh tế của điện sau công tơ và lịch lắp đặt GPU chính xác phần lớn vẫn là thông tin riêng tư.

Các nghiên cứu liên quan được tập hợp tại [trung tâm Phân tích độc quyền](/vi/page/exclusive-analysis-hub/) và [trung tâm AI HBM](/vi/page/korea-semiconductor-hbm-kospi-hub/).

[^allianz]: [Allianz Research, Thinking fast, building slow: AI and the energy supply crunch](https://www.allianz.com/content/dam/onemarketing/azcom/Allianz_com/economic-research/publications/specials/en/2026/may/2026-05-12-ai-energy-AZ.pdf), May 12, 2026.
[^nerc]: [NERC, 2026 Summer Reliability Assessment](https://www.nerc.com/globalassets/our-work/assessments/nerc_sra_2026.pdf), May 2026.
[^lbl]: [Lawrence Berkeley National Laboratory, Queued Up: 2026 Edition](https://emp.lbl.gov/queues), July 2026.
[^reuters-transformer]: [Reuters, US power companies scramble to secure equipment as surging data center demand strains supplies](https://www.investing.com/news/stock-market-news/us-power-companies-scramble-to-secure-equipment-as-surging-data-center-demand-strains-supplies-4783319), July 9, 2026.
[^dcwatch]: [Tom's Hardware report citing Data Center Watch](https://www.tomshardware.com/tech-industry/artificial-intelligence/more-than-75-data-center-build-outs-worth-usd130-billion-have-been-successfully-blocked-in-the-first-four-months-of-2026-bipartisan-opposition-mounts-nationwide-over-fears-of-soaring-power-and-water-costs), June 13, 2026.
[^gas-turbine]: [S&P Global, Mitsubishi Power gas turbine orders stretch to 2030](https://www.spglobal.com/energy/en/news-research/latest-news/energy-transition/070326-interview-mitsubishi-power-gas-turbine-orders-stretch-to-2030-amid-ai-security-demand), July 3, 2026.
[^kera]: [KERA News, ERCOT predicts record summer energy demand](https://www.keranews.org/energy-environment/2026-06-04/ercot-predicts-record-summer-energy-demand), June 4, 2026.
[^ferc]: [FERC, FERC Launches Aggressive Targeted Action to Speed Large Load Integration](https://www.ferc.gov/news-events/news/ferc-launches-aggressive-targeted-action-speed-large-load-integration), June 18, 2026.
[^spp-solar-gas]: [S&P Global Market Intelligence, Data center power: Combined-cycle plant outperforms solar plus battery](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/03/data-center-power-combined-cycle-plant-outperforms-solar-plus-battery), March 2026.

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
