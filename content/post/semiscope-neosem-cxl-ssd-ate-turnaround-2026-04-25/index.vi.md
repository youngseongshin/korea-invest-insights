---
title: "SemiScope: Neosem - Cổ phiếu thuần túy về thiết bị kiểm tra CXL và SSD Gen6 của Hàn Quốc tại điểm bùng phát chu kỳ đặt hàng 2026"
slug: semiscope-neosem-cxl-ssd-ate-turnaround-2026-04-25
date: 2026-04-25T19:20:00+09:00
description: "Neosem (253590 KQ) là công ty ATE của Hàn Quốc, có lợi thế cạnh tranh trực tiếp trong mảng thiết bị kiểm tra SSD PCIe Gen6, thiết bị kiểm tra bộ nhớ CXL 3.1, tự động hóa DIMM máy chủ, SOCAMM và tiềm năng burn-in HBM. Năm 2025 là một chu kỳ suy giảm mạnh, nhưng các đơn hàng cuối năm 2025 cho thấy khả năng phục hồi doanh thu trong năm 2026."
categories: ["Chuỗi cung ứng công nghệ Hàn Quốc", "Thiết bị bán dẫn"]
tags: ["Neosem", "253590", "SemiScope", "CXL", "Gen6 SSD", "PCIe 6.0", "ATE", "Thiết bị kiểm tra SSD", "Thiết bị kiểm tra bộ nhớ", "SOCAMM", "HBM Burn-in"]
series: ["semiscope-2026"]
---

> **Phân tích chuyên sâu SemiScope.** Neosem không phải là một rổ thiết bị bán dẫn đa dạng. Đây là cái tên ATE tập trung, đứng ngay tại giao điểm của SSD PCIe Gen6, mở rộng bộ nhớ CXL, tự động hóa DIMM máy chủ và những điểm nghẽn kiểm tra tiếp theo trong bộ nhớ trung tâm dữ liệu AI.

---

## TL;DR

1. **Neosem (253590 KQ) là công ty ATE, không phải công ty IP.** Sản phẩm của họ là thiết bị kiểm tra hậu xử lý bán dẫn: thiết bị kiểm tra SSD PCIe, thiết bị kiểm tra bộ nhớ CXL, thiết bị kiểm tra tự động hóa DIMM máy chủ và thiết bị burn-in. Nếu OpenEdges là lựa chọn IP thượng nguồn trong chuỗi CXL, thì Neosem là lựa chọn thiết bị hạ nguồn — được trả tiền khi các nhà sản xuất bộ nhớ đặt mua công cụ.
2. **Thế mạnh cốt lõi là kiểm tra trong các giai đoạn chuyển đổi giao diện.** Thiết bị kiểm tra SSD PCIe Gen5, thiết bị kiểm tra bộ nhớ CXL 1.1/2.0, và chu kỳ PCIe Gen6 / CXL 3.1 sắp tới đều có một điểm chung: khi một giao diện bộ nhớ tốc độ cao mới trở thành hiện thực, bài toán kiểm tra trở nên phức tạp hơn và giá trị nội dung thiết bị tăng lên.
3. **Năm 2025 rất tệ, nhưng đó chính xác là lý do tại sao cơ hội lại thú vị.** Doanh thu giảm 39,3% so với cùng kỳ xuống còn KRW 63,9 tỷ, lợi nhuận hoạt động giảm 75,3% xuống KRW 4,1 tỷ, và biên lợi nhuận hoạt động (OPM) co lại còn 6,4%. Việc tạm dừng capex bộ nhớ và chi phí R&D nặng nề xảy ra đồng thời. Nhưng buổi IR tháng 11 của ban lãnh đạo chỉ ra sự phục hồi đơn hàng mạnh mẽ từ cuối tháng 8, với các đơn hàng từ tháng 9 đến tháng 11 được báo cáo ở mức gần gấp đôi tổng lũy kế từ tháng 1 đến tháng 8.
4. **Chuỗi kích hoạt 2026-2027 dày đặc bất thường.** Demo thiết bị kiểm tra Gen6 SSD, giao hàng thiết bị kiểm tra sản xuất CXL 3.1, GEMINI3 cho SOCAMM, tiềm năng burn-in BX và mở rộng khách hàng nước ngoài tạo ra nhiều con đường để doanh thu phục hồi. Tín hiệu ngắn hạn rõ ràng nhất là liệu các đơn hàng cuối năm 2025 có chuyển hóa thành doanh thu Q1/Q2 năm 2026 hay không.
5. **Quan điểm đầu tư: phục hồi theo sự kiện cộng với beta chu kỳ.** Neosem chưa phải là một cổ phiếu tăng trưởng đều. Đây là cổ phiếu thiết bị có biến động mạnh, gắn liền với capex bộ nhớ và thời điểm của khách hàng. Nhưng những tham chiếu đi đầu trong CXL và tiềm năng cạnh tranh sạch hơn trong thiết bị kiểm tra SSD khiến đây là một trong những cách trực tiếp nhất trên sàn chứng khoán Hàn Quốc để đặt cược vào chu kỳ kiểm tra giao diện tiếp theo.

---

## Tại sao Neosem đáng chú ý

Thị trường bán dẫn thích nói về tính toán: GPU, bộ tăng tốc AI, stack HBM, bộ nhớ pool CXL và dung lượng SSD. Nhưng trước khi những thiết bị đó vào máy chủ, chúng phải được kiểm tra. Không phải lấy mẫu. Không phải kiểm tra điểm. Mà là kiểm tra ở quy mô sản xuất.

Đó là sân chơi của Neosem.

Neosem sản xuất thiết bị kiểm tra tự động, hay ATE, cho các thiết bị bộ nhớ và lưu trữ sau khi chế tạo và đóng gói. Các công cụ của họ được sử dụng để xác minh xem SSD, thiết bị bộ nhớ CXL, DIMM và các module liên quan có hoạt động đúng trước khi xuất xưởng hay không. Hệ thống càng quan trọng, mức độ chịu đựng lỗi tiềm ẩn càng thấp. Một thiết bị lưu trữ hay bộ nhớ lỗi trong máy chủ AI có thể gây ra bất ổn ở cấp độ hệ thống, và chi phí thất bại ngày càng tăng khi kiến trúc bộ nhớ trung tâm dữ liệu trở nên phức tạp hơn.

Điểm mạnh chiến lược của công ty không phải là kiểm tra tổng quát. Mà là kiểm tra xung quanh các giao diện tốc độ cao mới. PCIe 4.0 chuyển sang PCIe 5.0. PCIe 5.0 chuyển sang PCIe 6.0. CXL 1.1 chuyển sang CXL 2.0, và thị trường đang chuẩn bị cho CXL 3.1. Mỗi lần chuyển đổi làm tăng tốc độ, độ phức tạp giao thức, áp lực toàn vẹn tín hiệu, xử lý lỗi và gánh nặng xác nhận.

Đó là lý do Neosem thú vị. Họ đã xây dựng danh tiếng là người tiên phong thương mại hóa các thiết bị kiểm tra sản xuất cho các tiêu chuẩn giao diện mới. Họ đi sớm trong kiểm tra SSD dựa trên PCIe. Họ thương mại hóa thiết bị kiểm tra bộ nhớ CXL 1.1 và 2.0 và giao công cụ sản xuất cho Samsung Electronics. Và hiện nay họ đang cố gắng mở rộng vị thế tiên phong đó sang CXL 3.1 và thiết bị kiểm tra Gen6 SSD.

Cuộc tranh luận trọng tâm về cổ phiếu này đơn giản: liệu năm 2025 là sự suy giảm cấu trúc, hay chỉ là tạm dừng capex trước một chu kỳ đặt hàng mới?

Nhận định của tôi: 2025 là một chu kỳ suy giảm thực sự, không phải sai số làm tròn. Nhưng sự bùng phát chu kỳ đặt hàng cũng đủ thực để theo dõi chặt chẽ. Neosem là một trong những cổ phiếu Hàn Quốc được dẫn dắt bởi sự kiện rõ ràng nhất trong câu chuyện phục hồi kiểm tra giao diện 2026.

---

## Neosem thực sự bán gì

Sản phẩm của Neosem chia thành bốn nhóm thực tế.

| Dòng sản phẩm | Kiểm tra gì | Tại sao quan trọng |
|---|---|---|
| **Thiết bị kiểm tra SSD PCIe** | SSD doanh nghiệp và trung tâm dữ liệu sử dụng giao diện PCIe Gen4/Gen5 và Gen6 trong tương lai. | Máy chủ AI cần lưu trữ nhanh hơn và độ tin cậy cao hơn. Tốc độ giao diện tăng làm phức tạp việc kiểm tra. |
| **Thiết bị kiểm tra bộ nhớ CXL** | Thiết bị bộ nhớ CXL và các sản phẩm mở rộng bộ nhớ liên quan. | CXL kết nối CPU, bộ nhớ và bộ tăng tốc dưới kiến trúc bộ nhớ coherent. Xác nhận phải bao gồm hành vi giao thức, độ trễ và xử lý lỗi, không chỉ tín hiệu đơn giản. |
| **Tự động hóa DIMM máy chủ / GEMINI** | Module bộ nhớ máy chủ và quy trình kiểm tra kiểu buồng tự động. | Kiểm tra bộ nhớ máy chủ cần thông lượng, tự động hóa và độ tin cậy ở quy mô lớn. |
| **Thiết bị burn-in / dòng BX** | Linh kiện bộ nhớ dưới điều kiện stress, bao gồm các biến thể liên quan đến HBM trong tương lai. | Burn-in sàng lọc độ tin cậy dưới điều kiện stress nhiệt độ, điện áp và thời gian. Cơ hội HBM tồn tại nhưng Neosem chưa phải người dẫn đầu hiện tại. |

Thương hiệu rõ ràng nhất hiện nay là kiểm tra SSD và module. Tài liệu KIRS cho thấy Thiết bị kiểm tra SSD cộng Thiết bị kiểm tra DIMM máy chủ chiếm 82,9% doanh thu nửa đầu năm 2025. Kiểm tra linh kiện bao gồm burn-in chiếm khoảng 10-15%, trong khi CXL không được công bố riêng.

Việc thiếu công bố CXL này quan trọng. Nhà đầu tư thường nói "Neosem là cổ phiếu thiết bị CXL", nhưng dòng doanh thu được báo cáo vẫn pha trộn SSD, DIMM, CXL và thiết bị liên quan. CXL có thể trở thành sản phẩm có hệ số định giá cao nhất, nhưng nền tảng tài chính hiện tại vẫn rộng hơn chỉ CXL.

---

## Tài chính 2025 - Một sự điều chỉnh mạnh

Các con số năm 2025 của Neosem không hề nhẹ nhàng.

| Chỉ tiêu | 2022 | 2023 | 2024 | 2025 | YoY 2025 |
|---|---:|---:|---:|---:|---:|
| Doanh thu | KRW 74,7 tỷ | KRW 100,9 tỷ | **KRW 105,2 tỷ** | **KRW 63,9 tỷ** | **-39,3%** |
| Lợi nhuận hoạt động | KRW 8,4 tỷ | KRW 8,1 tỷ | **KRW 16,5 tỷ** | **KRW 4,1 tỷ** | **-75,3%** |
| Biên lợi nhuận hoạt động | 11,2% | 8,0% | **15,7%** | **6,4%** | -9,3pp |
| Lợi nhuận ròng | KRW 10,0 tỷ | KRW 8,3 tỷ | KRW 19,2 tỷ | **KRW 4,8 tỷ** | -74,8% |

Đây là một đợt nén chu kỳ thiết bị điển hình. Doanh thu giảm khi các khách hàng bộ nhớ trì hoãn hoặc giảm capex thiết bị kiểm tra, trong khi chi phí R&D và phát triển sản phẩm không giảm theo. Công ty chi tiêu cho Gen6 SSD, CXL 3.1, tự động hóa SOCAMM và mở rộng burn-in trong khi khách hàng vẫn đang tiêu hóa công suất trước đó.

Đây là mặt nguy hiểm của mô hình. Các công ty thiết bị có đòn bẩy hoạt động theo cả hai chiều. Khi đơn hàng tăng tốc, biên lợi nhuận phục hồi nhanh chóng. Khi đơn hàng tạm dừng, chi phí kỹ thuật và hỗ trợ cố định nén chặt biên lợi nhuận cũng nhanh chóng không kém.

Điểm nhìn về phía trước là bình luận về đơn hàng. Trong buổi IR tháng 11 năm 2025, công ty cho biết đơn hàng bắt đầu tăng mạnh từ cuối tháng 8, với các đơn hàng từ tháng 9 đến tháng 11 được báo cáo ở mức khoảng gấp đôi tổng lũy kế từ tháng 1 đến tháng 8. Vì việc ghi nhận doanh thu thiết bị thường trễ so với đơn hàng khoảng sáu đến chín tháng, điều này cho thấy khả năng phục hồi doanh thu năm 2026 thay vì năm 2025.

Bài kiểm tra đầu tiên là Q1 và Q2 năm 2026. Nếu doanh thu hàng quý trở lại mức trên KRW 20 tỷ, thị trường có thể coi đợt phục hồi đơn hàng cuối năm 2025 là có thực. Nếu không, tham vọng "năm kỷ lục 2026" cần phải được chiết khấu mạnh.

---

## Lợi thế cạnh tranh - Tiên phong xác nhận giao diện

Lợi thế của Neosem không phải là không ai khác có thể làm thiết bị kiểm tra. Teradyne, Advantest, DI, Exicon và các nhà cung cấp thiết bị kiểm tra khác đều tồn tại. Lợi thế hẹp hơn: Neosem đã đi sớm trong việc chuyển hóa các tiêu chuẩn giao diện mới thành thiết bị kiểm tra bộ nhớ và SSD sẵn sàng cho sản xuất.

| Trục lợi thế | Đánh giá | Lý do |
|---|---|---|
| **Vị thế thiết bị kiểm tra SSD PCIe** | Cao | Advantest được báo cáo đã rút khỏi mảng kiểm tra SSD vào tháng 1 năm 2025, củng cố vị thế của Neosem trong thiết bị kiểm tra SSD PCIe Gen5. |
| **Tham chiếu sản xuất CXL** | Cao | Neosem có tham chiếu thương mại trong thiết bị kiểm tra sản xuất CXL 1.1 và 2.0 được cung cấp cho Samsung Electronics. |
| **Lịch sử xác nhận khách hàng** | Trung bình-cao | Dữ liệu xác nhận theo thiết bị, firmware, lịch sử debug và tích hợp dây chuyền khách hàng tạo ra ma sát chuyển đổi. |
| **Thông lượng / tự động hóa** | Trung bình | GEMINI mang lại khả năng tiếp xúc tự động hóa DIMM máy chủ, nhưng khả năng lãnh đạo thông lượng phải được chứng minh lại theo từng thế hệ. |
| **Khả năng cạnh tranh chi phí** | Trung bình | Các nhà cung cấp thiết bị Hàn Quốc có thể cạnh tranh về chi phí, nhưng các nhà cung cấp ATE toàn cầu có quy mô và chiều sâu hỗ trợ. |

Tài sản quan trọng nhất là lịch sử xác nhận. Trong kiểm tra giao diện tốc độ cao, công cụ không chỉ cần tạo tín hiệu. Nó cần hiểu hành vi thiết bị, các mẫu kiểm tra, chế độ lỗi, thời gian giao thức, các trường hợp biên firmware và quy trình sản xuất đặc thù của từng khách hàng. Một khi nhà sản xuất bộ nhớ đã debug một thế hệ thiết bị mới trên một nền tảng thiết bị kiểm tra nhất định, việc chuyển đổi không hề dễ dàng.

Điều này đặc biệt quan trọng trong CXL. Thiết bị bộ nhớ CXL không chỉ là một DIMM nhanh hơn. Nó phải hoạt động dưới ngữ nghĩa bộ nhớ, cache coherency, ràng buộc độ trễ và xử lý lỗi ở cấp hệ thống. Một thiết bị kiểm tra sản xuất phải xác nhận hành vi nằm gần kiến trúc hệ thống hơn so với kiểm tra bộ nhớ truyền thống.

Tuy nhiên, lợi thế này không vĩnh viễn. CXL 3.1 có thể dẫn đến nguồn cung kép. Samsung, SK Hynix và Micron không thích phụ thuộc vào một nhà cung cấp duy nhất nếu danh mục trở nên lớn. Exicon, DI và các nhà cung cấp thiết bị kiểm tra toàn cầu có thể đẩy mạnh hơn vào cùng cơ hội này. Lợi thế tiên phong của Neosem quan trọng nhất nếu nó chuyển hóa thành chiến thắng sản xuất lặp lại trước khi đối thủ bắt kịp.

---

## Bản đồ khách hàng - Samsung, SK Hynix, Micron và câu hỏi xuất khẩu

Khách hàng có thể xác nhận công khai bao gồm Samsung Electronics, SK Hynix và Micron. Thách thức là doanh thu theo từng khách hàng không được công bố đầy đủ, và doanh thu CXL cụ thể không được tách riêng.

| Loại | Khách hàng / khu vực | Sản phẩm | Trạng thái | Độ tin cậy |
|---|---|---|---|---|
| Sản xuất hiện tại | Samsung Electronics memory | Thiết bị kiểm tra bộ nhớ sản xuất CXL 1.1 / 2.0 và trạm debug | Tham chiếu giao hàng sản xuất được báo cáo | Cao |
| Sản xuất hiện tại | Samsung Electronics memory | Thiết bị kiểm tra DIMM DDR5 | Nguồn cung sản xuất được bên bán trích dẫn | Cao |
| Sản xuất hiện tại | SK Hynix | Thiết bị burn-in BX | Tham chiếu đặt hàng và ghi nhận doanh thu được bên bán trích dẫn | Cao |
| Sản xuất hiện tại | Micron | Thiết bị kiểm tra SSD | Lịch sử cung cấp sản xuất và tham chiếu giải thưởng nhà cung cấp 2023 | Cao |
| Đang triển khai | Samsung Electronics | Thiết bị kiểm tra bộ nhớ sản xuất CXL 3.1 | Một số giao hàng nửa đầu 2026 được bình luận thị trường kỳ vọng | Trung bình-cao |
| Đang triển khai | Samsung Electronics | Thiết bị kiểm tra Gen6 SSD | Demo đang thử nghiệm, mục tiêu sản xuất 2027 | Trung bình |
| Đang triển khai | Samsung / SK hoặc hệ sinh thái bộ nhớ rộng hơn | Biến thể burn-in BX tập trung HBM | Công ty đã thảo luận về cân nhắc phát triển, nhưng thực thi chưa rõ | Thấp-trung bình |
| Đang triển khai | Hệ sinh thái bộ nhớ NVIDIA / nhà sản xuất bộ nhớ | GEMINI3 cho SOCAMM | Phát triển cho đơn hàng 2026 có thể, nhưng danh tính khách hàng cuối chưa rõ | Thấp-trung bình |
| Tiềm năng | Khách hàng mới nước ngoài | Công cụ kiểm tra burn-in và SSD/CXL | Ban lãnh đạo muốn mở rộng xuất khẩu và đạt cột mốc xuất khẩu US$100M vào 2027 | Thấp-trung bình |

Tín hiệu khách hàng quan trọng nhất là Micron và sức hút nước ngoài rộng hơn. Nếu Neosem vẫn gắn chặt với thời điểm của Samsung, cổ phiếu là một proxy beta cao cho capex bộ nhớ Samsung. Nếu tỷ trọng doanh thu nước ngoài mở rộng có ý nghĩa, hệ số định giá có thể được nâng lên.

Tham chiếu của ban lãnh đạo về mục tiêu đạt cột mốc xuất khẩu US$100M vào 2027 hữu ích như một chỉ dấu tham vọng, nhưng tôi sẽ coi đó là điểm kiểm tra thực thi chứ không phải giả định cơ sở. Chỉ số có thể quan sát được là tỷ trọng doanh thu nước ngoài trong các báo cáo hàng quý và hàng năm.

---

## Ma trận tác động xu hướng

| Xu hướng | Tác động | Hàm ý đầu tư |
|---|---|---|
| **Capex máy chủ AI và PCIe 6.0 / Gen6 SSD** | Thuận lợi mạnh | SSD trung tâm dữ liệu nhanh hơn cần phạm vi kiểm tra mới. Nếu Advantest vẫn không có trong thiết bị kiểm tra SSD, vị thế cạnh tranh của Neosem có thể đặc biệt sạch. |
| **Pool bộ nhớ CXL và mở rộng** | Thuận lợi mạnh | CXL 3.1 đưa danh mục gần hơn đến triển khai quy mô lớn. Tham chiếu CXL 1.1/2.0 của Neosem là tài sản tiên phong thực sự. |
| **Ứng dụng NVIDIA SOCAMM** | Thuận lợi | GEMINI3 có thể mở ra danh mục tự động hóa mới nếu SOCAMM trở thành tiêu chuẩn khối lượng thực sự. Thời điểm và quy mô thị trường vẫn chưa rõ. |
| **Nhu cầu kiểm tra gói HBM** | Trung lập đến thuận lợi | Burn-in BX có tiềm năng, nhưng TechWing và Advantest nằm trung tâm hơn trong kiểm tra HBM hiện nay. Neosem không phải người dẫn đầu rõ ràng trong kiểm tra HBM. |
| **Tích hợp burn-in và kiểm tra mật độ cao** | Thuận lợi với cạnh tranh | BX bao gồm chức năng kiểm tra tần số thấp, nhưng định vị CLT của Exicon và sức mạnh burn-in của DI làm tăng áp lực cạnh tranh. |
| **Phục hồi capex bộ nhớ Samsung** | Thuận lợi | Samsung là khách hàng chủ chốt và thời điểm CXL/Gen6 quan trọng trực tiếp. |
| **Chu kỳ capex SK Hynix** | Trung lập đến thuận lợi nhẹ | Neosem có tiếp xúc burn-in, nhưng khả năng lãnh đạo kiểm tra HBM cụ thể có vẻ ở nơi khác hiện tại. |
| **Kiểm soát xuất khẩu Mỹ-Trung** | Trung lập đến bất lợi nhẹ | Tiếp xúc Trung Quốc trực tiếp có vẻ hạn chế, nhưng phân bổ capex của các nhà sản xuất bộ nhớ có thể thay đổi theo địa chính trị. |
| **Nội địa hóa ATE Hàn Quốc** | Thuận lợi | Các nhà sản xuất bộ nhớ trong nước được hưởng lợi từ lựa chọn thiết bị địa phương trong các danh mục kiểm tra chiến lược quan trọng. |

Sự phân biệt quan trọng nhất là giữa "ứng dụng CXL" và "thời điểm doanh thu CXL". Dự báo thị trường CXL có thể trông rất lớn. Nhưng Neosem chỉ kiếm tiền khi các nhà sản xuất bộ nhớ đặt mua thiết bị kiểm tra sản xuất, không phải khi ngành công nghiệp công bố biểu đồ TAM. Trình tự là: hoàn thiện tiêu chuẩn, phát triển thiết bị, đủ điều kiện khách hàng, công cụ thử nghiệm, công cụ sản xuất, rồi mới đến doanh thu.

---

## Các tác nhân kích hoạt nhảy vọt

### Tác nhân 1 - Ứng dụng sản xuất thiết bị kiểm tra Gen6 SSD

Đây là tác nhân chất lượng cao nhất vì Neosem đã có nền tảng thiết bị kiểm tra SSD mạnh.

Định nghĩa rõ ràng: thiết bị kiểm tra SSD PCIe 6.0 / Gen6 chuyển từ demo và công cụ R&D sang dây chuyền sản xuất tại Samsung Electronics, Micron hoặc cả hai. Lộ trình SSD Gen6 loại PM1763 của Samsung và quỹ đạo chứng nhận SSD Gen6 của Micron là động lực khách hàng cơ bản.

Các chỉ số dẫn đầu:

- R&D hoặc ứng dụng thiết bị thử nghiệm trong nửa đầu 2026;
- đơn hàng sản xuất nửa cuối 2026;
- ghi nhận doanh thu 2027;
- bằng chứng Neosem vẫn là nhà cung cấp chính hoặc duy nhất.

Nếu động lực nhà cung cấp duy nhất Gen5 kéo dài sang Gen6, tiềm năng tăng giá có thể có ý nghĩa. Kịch bản thị phần toàn cầu trên 50% trong thiết bị kiểm tra SSD không phải không thể nếu đối thủ vẫn vắng mặt hoặc đến muộn. Rủi ro là Teradyne hoặc nhà cung cấp ATE khác mở rộng mạnh vào PCIe 6.0, hoặc Advantest quay trở lại bất chấp việc rút lui được báo cáo.

### Tác nhân 2 - Chu kỳ thiết bị kiểm tra sản xuất CXL 3.1

CXL 3.1 là tác nhân có sức hút câu chuyện mạnh hơn.

Neosem đã có tham chiếu sản xuất CXL 1.1 và CXL 2.0. Câu hỏi tiếp theo là liệu lịch sử đó có chuyển hóa thành thị phần thiết bị kiểm tra sản xuất CXL 3.1 khi Samsung, SK Hynix và cuối cùng là Micron mở rộng quy mô sản phẩm bộ nhớ CXL hay không.

Các chỉ số dẫn đầu:

- giao hàng thiết bị kiểm tra sản xuất CXL 3.1 đầu tiên trong nửa đầu 2026;
- khách hàng được công bố, số lượng công cụ hoặc quy mô hợp đồng;
- bằng chứng CXL 3.1 không giới hạn ở mẫu kỹ thuật;
- đơn hàng lặp lại trong cuối 2026 và 2027.

Kịch bản lạc quan là thiết bị kiểm tra CXL mang ASP cao hơn thiết bị kiểm tra SSD thông thường vì chúng phải xác nhận hành vi giao thức, ngữ nghĩa bộ nhớ, độ trễ và xử lý lỗi. Một chu kỳ sản xuất có thể cộng thêm hàng trăm tỷ won trong cơ hội tích lũy trong nhiều năm nếu mở rộng bộ nhớ CXL trở thành danh mục trung tâm dữ liệu thực sự.

Rủi ro là nguồn cung kép. Samsung và các nhà sản xuất bộ nhớ khác có thể chia CXL 3.1 giữa Neosem và các đối thủ như Exicon hoặc DI. Nếu điều đó xảy ra, câu chuyện CXL vẫn tích cực, nhưng câu chuyện độc quyền mờ dần.

### Tác nhân 3 - Gia nhập burn-in BX tập trung HBM

Đây là tác nhân bất định nhất.

HBM4 và HBM4E sẽ tăng nhu cầu sàng lọc độ tin cậy, đặc biệt khi chiều cao stack tăng và độ phức tạp liên kết tăng lên. Thiết bị burn-in BX của Neosem có con đường khái niệm vào các biến thể HBM cụ thể, và công ty đã thảo luận về khả năng phát triển tập trung HBM.

Nhưng hiện nay, tôi sẽ không đặt cược Neosem là người dẫn đầu kiểm tra HBM. Hệ sinh thái cube prober của TechWing và nền tảng kiểm tra bộ nhớ của Advantest nằm trung tâm hơn trong cuộc trò chuyện kiểm tra HBM hiện tại. Một số báo cáo cũng cho thấy thiết bị tương tự của các nhà cung cấp khác đang trải qua quy trình đủ điều kiện của Samsung.

Vì vậy, tác nhân phải cụ thể:

- thông báo chính thức về biến thể BX dành riêng cho HBM;
- gia nhập đủ điều kiện tại Samsung hoặc SK Hynix;
- đơn hàng sản xuất gắn với HBM4 hoặc HBM4E.

Cho đến lúc đó, HBM là tiềm năng, không phải luận điểm cốt lõi.

### Tác nhân 4 - GEMINI3 và SOCAMM

SOCAMM, hay Small Outline Compression Attached Memory Module, là dạng module bộ nhớ mới tiềm năng gắn với yêu cầu hệ sinh thái NVIDIA và các nền tảng tính toán AI nhỏ gọn. Nếu SOCAMM trở thành tiêu chuẩn khối lượng lớn, nhu cầu tự động hóa và kiểm tra module có thể tạo ra một danh mục mới cho GEMINI3 của Neosem.

Các chỉ số dẫn đầu:

- các nhà sản xuất bộ nhớ thông báo capex liên quan đến SOCAMM;
- thông số nền tảng NVIDIA đủ ổn định cho sản xuất khối lượng lớn;
- Neosem trình diễn GEMINI3 hoặc đặt hàng sớm;
- đóng góp doanh thu được tách riêng hoặc thảo luận trong hồ sơ.

Rủi ro là tiêu chuẩn hóa. Nếu SOCAMM vẫn hẹp, độc quyền hoặc khối lượng thấp, GEMINI3 có thể là sản phẩm hữu ích nhưng không phải sản phẩm thay đổi cuộc chơi cho công ty.

---

## Bản đồ rủi ro

| Rủi ro | Tại sao quan trọng | Cần theo dõi gì |
|---|---|---|
| **Tập trung khách hàng** | Doanh thu thiết bị có thể biến động theo một vài quyết định của nhà sản xuất bộ nhớ. | Thời điểm đặt hàng Samsung và Micron, tỷ trọng doanh thu nước ngoài, tình trạng tồn đơn. |
| **Phụ thuộc chu kỳ capex** | Năm 2025 cho thấy doanh thu và biên lợi nhuận có thể giảm nhanh như thế nào khi khách hàng tạm dừng chi tiêu. | Chuyển hóa doanh thu Q1 và Q2 năm 2026 từ đơn hàng cuối năm 2025. |
| **Cạnh tranh CXL 3.1** | Tham chiếu tiên phong có thể không đảm bảo vị thế nhà cung cấp duy nhất. | Chiến thắng thiết bị kiểm tra CXL của Exicon, DI và các nhà cung cấp toàn cầu. |
| **Rủi ro không theo kịp HBM** | Neosem có thể bỏ lỡ chu kỳ con kiểm tra HBM phong phú nhất nếu vẫn đến muộn. | Tin tức phát triển và đủ điều kiện BX dành riêng cho HBM. |
| **Áp lực chi phí R&D** | Gen6 SSD, CXL 3.1, BX và GEMINI3 đều đòi hỏi chi tiêu trước khi có doanh thu. | Phục hồi OPM so với chi phí kỹ thuật tiếp tục. |
| **Độ tin cậy dự báo** | Dự báo bên bán năm 2025 cao hơn nhiều so với kết quả thực tế. | Hướng dẫn ban lãnh đạo so với công bố đơn hàng và doanh thu ghi nhận. |

Điểm cuối cùng quan trọng. Một dự báo bên bán vào tháng 1 năm 2025 được báo cáo kỳ vọng doanh thu 2025 khoảng KRW 131,5 tỷ, tăng 28%. Doanh thu sơ bộ thực tế năm 2025 là KRW 63,9 tỷ, giảm 39%. Sai lệch này không chỉ là lỗi mô hình; đó là lời nhắc nhở rằng cổ phiếu thiết bị có thể chuyển từ "kỷ lục năm tới" sang "trì hoãn capex" rất nhanh.

Với năm 2026, tôi sẽ dùng sự lạc quan của ban lãnh đạo như một giả thuyết, không phải kết luận.

---

## Năm điểm kiểm tra trong hai quý tới

1. **Phục hồi doanh thu Q1 năm 2026.** Nếu đợt phục hồi đơn hàng cuối năm 2025 là thực, doanh thu sẽ bắt đầu phục hồi. Kết quả doanh thu hàng quý trên KRW 20 tỷ sẽ là tín hiệu quan trọng.
2. **Giao hàng thiết bị kiểm tra sản xuất CXL 3.1.** Một chuyến hàng sản xuất CXL 3.1 liên quan đến Samsung trong nửa đầu 2026 sẽ xác nhận câu chuyện chuyển đổi CXL.
3. **Khả năng nhìn thấy đơn hàng thiết bị kiểm tra Gen6 SSD.** Theo dõi thời điểm đơn hàng sản xuất Gen6 SSD của Samsung trong nửa cuối 2026 và liệu Neosem có vẫn là nhà cung cấp chính.
4. **Quyết định BX dành riêng cho HBM.** Thông báo phát triển hoặc đủ điều kiện HBM chính thức sẽ thêm một chiều tiềm năng mới; im lặng giữ HBM bên ngoài luận điểm cốt lõi.
5. **Tỷ trọng xuất khẩu và sức hút Micron.** Bằng chứng tăng trưởng doanh thu nước ngoài là sự khác biệt giữa một proxy chu kỳ Samsung và một thương hiệu thiết bị kiểm tra toàn cầu hơn.

---

## Khung định giá

Tôi sẽ định giá Neosem ít giống một compounder chất lượng mượt mà hơn và nhiều giống một quyền chọn chu kỳ-và-sự kiện hơn.

| Kịch bản | Điều phải xảy ra | Hàm ý cho nhà đầu tư |
|---|---|---|
| **Trường hợp xấu** | Đơn hàng cuối 2025 không chuyển hóa, CXL 3.1 bị trì hoãn hoặc nguồn cung kép nặng nề, đơn hàng Gen6 SSD trễ, R&D giữ biên lợi nhuận gần mức một chữ số trung. | Năm 2025 không phải là đáy tạm thời; cổ phiếu vẫn là cổ phiếu thiết bị vốn nhỏ biến động. |
| **Trường hợp cơ sở** | Doanh thu Q1/Q2 năm 2026 phục hồi, giao hàng thử nghiệm CXL 3.1 diễn ra, Gen6 SSD vẫn đúng hướng cho 2027, biên lợi nhuận xây dựng lại về mức hai chữ số thấp. | Neosem có thể được định giá lại là câu chuyện phục hồi kiểm tra giao diện đáng tin cậy. |
| **Trường hợp lạc quan** | Động lực nhà cung cấp duy nhất thiết bị kiểm tra Gen6 SSD kéo dài, đơn hàng sản xuất CXL 3.1 mở rộng quy mô, thị phần Micron/nước ngoài tăng, và một trong SOCAMM hoặc burn-in HBM trở nên đáng kể. | Doanh thu có thể vượt đỉnh trước và thị trường có thể định giá một nền tảng kiểm tra bộ nhớ AI đa sản phẩm. |

Độ nhạy cảm chính là thời điểm. Một đơn hàng thiết bị trễ sáu tháng có thể biến câu chuyện kỷ lục năm thành thất vọng khác. Đó là lý do cổ phiếu cần được theo dõi qua chuyển hóa đơn hàng, không chỉ thông báo sản phẩm.

---

## Ghi chú cuối - Góc nhìn người phân bổ vốn

Neosem là một công cụ rất khác so với OpenEdges. OpenEdges là quyền chọn tiền bản quyền IP dài hạn. Neosem là quyền chọn chu kỳ thiết bị gần hơn gắn với đơn hàng công cụ sản xuất. Cả hai đều gần câu chuyện kiến trúc bộ nhớ CXL và AI, nhưng thời điểm dòng tiền khác nhau.

Sự khác biệt về thời điểm đó là lý do Neosem đáng chú ý ngay bây giờ. Báo cáo thu nhập năm 2025 đã hấp thụ một chu kỳ suy giảm mạnh. Công ty cho biết đơn hàng tăng từ cuối tháng 8. Nếu những đơn hàng đó trở thành doanh thu trong năm 2026, cổ phiếu có thể chuyển từ "hướng dẫn 2025 thất bại" sang "người dẫn đầu chu kỳ kiểm tra giao diện tiếp theo."

Quan điểm của tôi là xây dựng nhưng có điều kiện. Neosem xứng đáng có trong danh sách theo dõi SemiScope như là cổ phiếu ATE niêm yết Hàn Quốc rõ ràng nhất về Gen6 SSD và CXL 3.1. Nhưng tôi sẽ không để câu chuyện CXL vượt quá bằng chứng. Những xác nhận cứng đơn giản: phục hồi doanh thu Q1 năm 2026, giao hàng sản xuất CXL 3.1, khả năng nhìn thấy đơn hàng Gen6 SSD và mở rộng khách hàng nước ngoài.

Nếu tất cả những điều đó cùng xuất hiện, Neosem không chỉ là một giao dịch phục hồi. Đây trở thành người hưởng lợi tiên phong đáng tin cậy của chu kỳ kiểm tra bộ nhớ trung tâm dữ liệu AI tiếp theo.

---

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
