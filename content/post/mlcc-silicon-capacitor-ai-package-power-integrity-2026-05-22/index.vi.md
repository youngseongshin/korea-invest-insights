---
title: "Hiểu về MLCC và Tụ Silicon — Hợp Đồng ₩1,5 Nghìn Tỷ của Samsung Electro-Mechanics Tiết Lộ Điều Gì về Nút Thắt Nguồn Điện trong Gói Chip AI"
date: 2026-05-22
description: "MLCC là linh kiện gốm siêu nhỏ gọn có mặt trong hầu hết mọi thiết bị điện tử, đóng vai trò ổn định nguồn điện. Tụ silicon là linh kiện hiệu suất cao được đặt bên trong hoặc ngay cạnh các gói chip GPU AI và HBM để triệt tiêu biến động điện tức thời. Điểm mấu chốt không phải là tụ silicon thay thế MLCC, mà là chiến trường cho linh kiện thụ động đang mở rộng từ bề mặt PCB vào bên trong các gói chip bán dẫn AI. Hợp đồng cung ứng trị giá ₩1,5 nghìn tỷ của Samsung Electro-Mechanics là tín hiệu cho thấy các công ty MLCC và substrate có thể được tái phân loại thành mắt xích chuỗi cung ứng tính toàn vẹn nguồn điện trong gói chip AI. Tuy vậy, ba cổ phiếu MLCC cốt lõi đã tăng trung bình +35,6% trong tuần này và Samsung Electro-Mechanics hiện giao dịch ở mức P/E 73x dự phóng 2026. Một sự chuyển dịch ngành hấp dẫn và một mức giá vào lệnh hấp dẫn là hai chuyện hoàn toàn khác nhau."
categories: ["Stock-Analysis"]
tags:
  - "MLCC"
  - "Tụ Silicon"
  - "Samsung Electro-Mechanics"
  - "009150"
  - "Đóng Gói AI"
  - "Tính Toàn Vẹn Nguồn Điện"
  - "Chuỗi Giá Trị Bán Dẫn"
  - "Substrate"
slug: mlcc-silicon-capacitor-ai-package-power-integrity-2026-05-22
---

> 📚 Series liên quan
> [Hợp Đồng ₩1,5 Nghìn Tỷ Tụ Silicon Samsung Electro-Mechanics](/vi/post/samsung-electro-mechanics-silicon-capacitor-1p5tn-2026-05-21/) / [Samsung Electro-Mechanics — Thách Thức Hybrid](/vi/post/samsung-electro-mechanics-hybrid-challenger-2026-05-17/) / [Phân Tích Sâu Mảng MLCC & FC-BGA của Samsung Electro-Mechanics](/vi/post/samsung-electro-mechanics-mlcc-fcbga-ai-infrastructure-deep-dive-2026-05-15/) / [Hub Chuỗi Giá Trị Bán Dẫn](/vi/page/korea-semiconductor-equipment-ip-hub/) / [Hub Substrate & PCB AI](/vi/page/korea-ai-pcb-substrate-hub/)

<figure>
  <img src="/img/posts/mlcc-silicon-capacitor-ai-package-power-integrity-2026-05-22/MLCC_Concept.png" alt="Sơ đồ minh họa MLCC và tụ silicon" loading="lazy">
</figure>

*MLCC là một loại tụ điện — linh kiện gốm siêu nhỏ gọn có mặt trong hầu hết mọi thiết bị điện tử, đóng vai trò ổn định nguồn điện. Tụ silicon được đặt gần chip bán dẫn hơn MLCC, trong một số trường hợp là ngay bên trong gói chip, để triệt tiêu biến động điện tức thời trong GPU AI và HBM. Từ góc độ đầu tư, điều quan trọng là tín hiệu cho thấy "linh kiện thụ động" đang thăng cấp từ linh kiện hàng hóa đơn thuần thành thành phần then chốt trong gói chip AI và tính toàn vẹn nguồn điện.*

---

## Tóm Tắt Trọng Điểm

Tụ điện lưu trữ điện tích trong thời gian ngắn rồi giải phóng theo nhu cầu. Với người không có nền kỹ thuật, hãy hình dung nó như một **bể chứa nước, bộ giảm chấn, hoặc bộ lọc nhiễu cho mạch điện**. MLCC là phiên bản gốm đa lớp có sản lượng cao nhất trong dòng tụ điện. Samsung Electro-Mechanics mô tả MLCC đóng vai trò như một "con đập" — tích trữ điện và giải phóng theo lượng kiểm soát.[^samsung-mlcc]

Tụ silicon cũng là một loại tụ điện. Khác với MLCC xếp chồng hàng trăm lớp gốm, tụ silicon hình thành các lớp điện môi và điện cực trên tấm wafer silicon. Theo tài liệu sản phẩm của Samsung Electro-Mechanics, nó có thể được mỏng hóa xuống dưới 100 micromet, nhúng bên trong gói chip, và hưởng lợi từ điện cảm ký sinh thấp — yếu tố thuận lợi cho việc ổn định nguồn điện.[^samsung-sicap-product]

Điểm cốt lõi **không phải là thay thế mà là sự dịch chuyển vị trí**. MLCC được gắn chủ yếu trên bề mặt PCB hoặc xung quanh chip. Tụ silicon có thể đặt bên trong gói chip, dưới substrate, hoặc ngay cạnh die. Vì GPU AI và HBM tiêu thụ dòng điện đột ngột với biên độ lớn, khoảng cách quan trọng không kém dung lượng thực tế — "tốc độ cung cấp điện" trở nên quan trọng ngang với "dung lượng tích trữ."

Hợp đồng cung ứng tụ silicon trị giá khoảng ₩1,5 nghìn tỷ được Samsung Electro-Mechanics công bố ngày 20 tháng 5 năm 2026 là bằng chứng quy mô lớn đầu tiên về sự dịch chuyển cấu trúc này. Hợp đồng có hiệu lực từ ngày 1 tháng 1 năm 2027 đến ngày 31 tháng 12 năm 2028. Công ty tuyên bố rằng sản phẩm được nhúng bên trong các gói chip bán dẫn hiệu suất cao — bao gồm GPU máy chủ AI và HBM — để nâng cao độ ổn định cung cấp nguồn điện.[^samsung-sicap-contract]

Tuy nhiên, nhận định đầu tư phải được giữ thật tỉnh táo. Trong tuần này (18–22 tháng 5), ba cổ phiếu MLCC cốt lõi tăng trung bình <strong>+35,6%</strong>, bỏ xa năm cổ phiếu substrate AI cốt lõi ở mức <strong>+14,0%</strong>. Samsung Electro-Mechanics tăng +32,7% trong tuần; Samwha Capacitor vọt lên +56,4%. Đà tăng theo chủ đề rõ nét, nhưng hiệu quả triển khai vốn mới đã giảm đi đáng kể.

Kết luận: **ý nghĩa của tụ silicon không phải là thay thế MLCC — mà là sự mở rộng chiến trường linh kiện thụ động từ bề mặt PCB vào bên trong các gói chip bán dẫn AI**. Dòng sản phẩm cao cấp của Samsung Electro-Mechanics và Murata có thể được tái phân loại thành tài sản chuỗi cung ứng hạ tầng AI. Nhưng một sự chuyển dịch ngành tốt và một mức giá vào lệnh tốt vẫn là hai câu hỏi hoàn toàn riêng biệt.

---

## 1. Mối Quan Hệ Giữa Tụ Điện và MLCC

Tụ điện lưu trữ điện tích và giải phóng nhanh chóng khi cần. Khi chip bán dẫn đột ngột đòi hỏi một lượng dòng điện lớn, tụ điện gần đó cung cấp ngay, ngăn điện áp sụt giảm. Ngược lại, khi điện áp tăng vọt, tụ điện hấp thụ bớt, ổn định mạch. Đó là lý do tụ điện đảm nhận các vai trò lưu trữ năng lượng, làm phẳng điện áp, lọc nhiễu và ổn định nguồn điện trong các mạch điện tử.

MLCC — **Multi-Layer Ceramic Capacitor** (Tụ Gốm Đa Lớp) — là tụ điện siêu nhỏ gọn được tạo ra bằng cách xếp chồng hàng trăm lớp gốm điện môi mỏng xen kẽ với các lớp điện cực kim loại. Samsung Electro-Mechanics đề cập đến năng lực sản xuất MLCC dung lượng cao với tới 600 lớp, đồng thời nhấn mạnh tầm quan trọng của MLCC ngày càng tăng cùng với sự mở rộng của 5G, điện tử tiêu dùng, xe tự lái và Internet of Things.[^samsung-mlcc]

Phân cấp rất rõ ràng:

```text
Tụ điện = toàn bộ danh mục linh kiện ổn định điện
MLCC = biến thể gốm đa lớp phổ thông trong danh mục đó
Tụ silicon = biến thể hiệu suất cao trên nền wafer silicon, tối ưu cho vị trí đặt cực gần chip
```

Cả MLCC lẫn tụ silicon đều là tụ điện. Chúng khác nhau ở vị trí triển khai và yêu cầu hiệu suất mà chúng được thiết kế để đáp ứng.

---

## 2. So Sánh Tụ Điện Thông Thường / MLCC / Tụ Silicon

| | Tụ Điện Thông Thường | MLCC | Tụ Silicon |
|---|---|---|---|
| Danh mục | Họ linh kiện rộng | Một loại tụ điện | Một loại tụ điện |
| Hình dung đơn giản | Bể chứa nước của mạch điện | Bể chứa nước gốm siêu nhỏ gọn | Bể chứa nước cực gần, nhúng ngay cạnh hoặc bên trong chip |
| Vật liệu chính | Gốm, điện phân nhôm, tantalum, màng, silicon, v.v. | Gốm điện môi + điện cực kim loại bên trong | Cấu trúc trên nền wafer silicon |
| Vai trò chính | Lưu trữ năng lượng, làm phẳng điện áp, lọc nhiễu | Lọc nhiễu tần số cao, ổn định nguồn quanh chip, thu nhỏ kích thước | Triệt tiêu biến động nguồn tức thời trong GPU AI, HBM và chip hiệu suất cao |
| Vị trí điển hình | Tầng nguồn, bo mạch, mô-đun, động cơ, biến tần | Chủ yếu trên PCB, quanh chip, quanh mô-đun | Bên trong gói chip, trong substrate, ngay cạnh die |
| Ưu điểm | Đa dạng lựa chọn cho nhiều ứng dụng | Nhỏ gọn, chi phí thấp, sản xuất hàng loạt | Cực mỏng; đặt sát die; thuận lợi cho ổn định nguồn |
| Hạn chế | Hiệu năng biến động lớn theo từng loại | Hạn chế trong ổn định nguồn gói chip tốc độ cực cao, cực gần | Phức tạp sản xuất và chi phí cao; thị trường khả dụng hiện tại tập trung vào chip hiệu suất cao |
| Động lực tăng trưởng chính | Ô tô, lưới điện, công nghiệp, máy chủ AI | Ô tô, máy chủ AI, smartphone, 5G, IoT | GPU AI, HBM, điện toán hiệu suất cao, chip di động cao cấp |

Chỉ cần nhìn qua danh mục sản phẩm tụ điện của TDK cũng thấy rõ sự đa dạng của danh mục: MLCC nhỏ, tụ gốm điện áp cao, tụ màng, tụ điện phân nhôm, và tụ nguồn đều nằm dưới cùng một "ô" tụ điện.[^tdk-capacitors] Nói "tụ điện triển vọng" là quá chung chung. Từ góc độ đầu tư, điều quan trọng là loại tụ nào, ở vị trí nào, cho ứng dụng nào.

---

## 3. Phạm Vi Ứng Dụng

### 3.1 Tụ Điện Thông Thường

Tụ điện thông thường xuất hiện trong hầu hết mọi mạch điện, từ điện tử tiêu dùng đến hạ tầng điện lực.

| Ứng dụng | Loại Tụ Chính | Vai Trò |
|---|---|---|
| Smartphone, PC | MLCC, tantalum, polymer | Ổn định nguồn quanh vi xử lý ứng dụng, bộ nhớ và PMIC |
| Máy chủ, máy chủ AI | MLCC, polymer, tụ silicon | Triệt tiêu biến động nguồn trong CPU, GPU và HBM |
| Điện tử ô tô | MLCC, màng, điện phân nhôm, tantalum | Ổn định ECU, ADAS, biến tần, bộ sạc và BMS |
| Hệ thống điện xe EV | Màng, MLCC điện áp cao, điện phân nhôm | DC link điện áp cao, sạc, chuyển đổi nguồn |
| Công nghiệp, lưới điện | Màng, điện phân nhôm | Hiệu chỉnh hệ số công suất, truyền động động cơ, lưu trữ năng lượng |
| Viễn thông, tần số cao | Gốm, tụ silicon | Lọc tần số cao, phối hợp trở kháng |

### 3.2 MLCC

Ứng dụng cốt lõi của MLCC là **ổn định nguồn xung quanh chip**. Chúng xuất hiện trong smartphone, ô tô, máy chủ, thiết bị mạng, thiết bị gia dụng và máy móc công nghiệp. Khi thiết bị thu nhỏ, bán dẫn chuyển mạch nhanh hơn, và số lượng cảm biến cùng mô-đun truyền thông tăng lên, số điểm cần ổn định điện áp cũng tăng theo tỷ lệ.

Tầm quan trọng của MLCC trong máy chủ AI cũng đang tăng. TDK nhận định rằng nhu cầu AI và đám mây thúc đẩy tích hợp cao hơn và hiệu suất cao hơn trong máy chủ trung tâm dữ liệu — làm tăng mật độ nguồn mỗi rack và mỗi máy chủ, biến hiệu suất và kích thước của linh kiện thụ động thành ràng buộc thiết kế thực sự.[^tdk-capacitors] Đó là lý do luận điểm đầu tư MLCC đã mở rộng ra ngoài câu chuyện phục hồi chu kỳ smartphone đơn thuần, vươn tới ổn định nguồn máy chủ AI.

### 3.3 Tụ Silicon

Ứng dụng cốt lõi của tụ silicon là **ổn định nguồn bên trong gói chip**. Samsung Electro-Mechanics mô tả tụ silicon là thiết bị siêu nhỏ gọn, hiệu suất cao xây dựng trên wafer silicon, được nhúng bên trong các gói chip bán dẫn hiệu suất cao — bao gồm GPU máy chủ AI và HBM — để nâng cao độ ổn định cung cấp nguồn điện.[^samsung-sicap-contract]

Tài liệu sản phẩm của công ty củng cố thêm: tụ silicon hình thành điện môi và điện cực bên trong trên silicon, có thể được mỏng hóa xuống dưới 100 micromet qua gia công wafer, và rất phù hợp để nhúng bên trong gói chip. Điện cảm ký sinh thấp là lợi thế then chốt cho ổn định nguồn.[^samsung-sicap-product]

Để giải mã các thuật ngữ chuyên môn:

```text
Điện cảm ký sinh = yếu tố gây trở ngại làm chậm phản hồi tức thời của dòng điện
Điện trở ký sinh = yếu tố gây tổn thất năng lượng khi dòng điện đi qua
Tính toàn vẹn nguồn điện = khả năng cung cấp điện áp và dòng điện ổn định, không gợn sóng cho chip đúng lúc cần
```

Chip bán dẫn AI tiêu thụ điện theo từng đợt đột ngột và lớn. Tụ điện đặt xa die phản hồi quá chậm. Giải pháp là đưa tụ điện lại ngay cạnh chip — hoặc bên trong gói chip. Luận điểm đầu tư cho tụ silicon không phải là "dung lượng cao hơn" mà là **phản hồi nhanh hơn nhờ vị trí gần hơn**.

---

## 4. Nhà Cung Cấp Chính và Tệp Khách Hàng

### 4.1 Nhà Cung Cấp MLCC Chính

| Khu vực | Công ty tiêu biểu | Thế mạnh |
|---|---|---|
| Nhật Bản | Murata, TDK, Taiyo Yuden | Dẫn đầu MLCC siêu nhỏ, độ tin cậy cao, chuẩn ô tô |
| Hàn Quốc | Samsung Electro-Mechanics | MLCC giá trị cao cho IT, ô tô và máy chủ AI; mở rộng sang tụ silicon |
| Đài Loan / Trung Hoa đại lục | Yageo, Walsin | Linh kiện thụ động phổ thông, công nghiệp và phân khúc trung-thấp |
| Mỹ / liên kết Nhật | KYOCERA AVX, KEMET/Yageo, Vishay | Tụ đặc chủng, dòng sản phẩm ô tô, công nghiệp và tần số cao |

Tệp khách hàng MLCC cực kỳ rộng: OEM smartphone, nhà sản xuất PC và máy chủ, OEM ô tô, nhà cung ứng Tier-1, nhà sản xuất thiết bị viễn thông và công ty mô-đun bán dẫn. Trong đầu tư MLCC, **cơ cấu nhu cầu theo thị trường đầu cuối và tỷ trọng sản phẩm giá trị cao** quan trọng hơn việc phụ thuộc vào bất kỳ khách hàng đơn lẻ nào.

### 4.2 Nhà Cung Cấp Tụ Silicon Chính

| | Công ty tiêu biểu | Định vị |
|---|---|---|
| Murata | Dẫn đầu về tụ silicon và thiết bị thụ động tích hợp | Tụ silicon cho di động hiệu suất cao, viễn thông và điện toán hiệu suất cao |
| Samsung Electro-Mechanics | Tân binh quy mô lớn | Đảm bảo hợp đồng cung ứng khoảng ₩1,5 nghìn tỷ giao hàng 2027–2028 |
| KYOCERA AVX và các công ty khác | Tụ MOS đặc chủng | Dòng sản phẩm tần số cao, vi sóng và công nghiệp đặc thù |
| Hệ sinh thái đóng gói nâng cao | Lựa chọn nội bộ hoặc đồng thiết kế | Liên kết với công nghệ interposer và tính toàn vẹn nguồn trong gói chip |

Chiều cạnh khách hàng rất quan trọng. MLCC có tệp khách hàng rộng và có thể thay thế. Tụ silicon, ngược lại, phải được thiết kế vào gói chip ngay từ đầu. Chúng yêu cầu đủ tiêu chuẩn của khách hàng, tích hợp vào kiến trúc gói chip và xác nhận tính toàn vẹn nguồn. Một khi đã được thiết kế vào, rất khó thay thế — chi phí chuyển đổi cao.

Đối tác hợp đồng của Samsung Electro-Mechanics chỉ được tiết lộ chính thức là "tập đoàn toàn cầu lớn." Do đó, việc xác định khách hàng là NVIDIA, AMD, Broadcom, Google, Meta, Microsoft, Amazon hay bất kỳ công ty cụ thể nào khác là không chính xác. Điều đó vẫn chưa được xác nhận.

---

## 5. Ý Nghĩa Thực Sự của Tụ Silicon

### 5.1 Ý Nghĩa Kỹ Thuật — Nút Thắt Nguồn Điện Dịch Chuyển Vào Bên Trong Gói Chip

Khi GPU AI và HBM tăng cường độ tính toán và tốc độ di chuyển dữ liệu, nhu cầu dòng điện tức thời đã tăng đáng kể. Vấn đề là nguồn điện đến từ xa bị làm chậm bởi các yếu tố ký sinh trong dây dẫn nguồn, substrate và gói chip — làm giảm khả năng phản hồi biến động. Giải pháp là đưa tụ điện lại ngay gần die.

MLCC thông thường nằm chủ yếu trên PCB hoặc quanh rìa gói chip. Tụ silicon có thể đặt bên trong gói chip hoặc ngay cạnh die. Với tụ điện có cùng dung lượng, **vị trí quyết định hiệu suất**.

### 5.2 Ý Nghĩa Kinh Doanh — Linh Kiện Thụ Động Được Định Giá Lại Thành Linh Kiện Đóng Gói AI

MLCC truyền thống được định giá như linh kiện chu kỳ. Khi nhu cầu smartphone và PC yếu đi, điều chỉnh hàng tồn kho tiếp diễn, và sản phẩm phổ thông phải đối mặt với cạnh tranh giá. Tụ silicon, ngược lại, là linh kiện phức tạp cao được nhúng bên trong gói chip GPU AI và HBM. Chúng yêu cầu đủ tiêu chuẩn khách hàng, tích hợp vào thiết kế gói chip và xác nhận tính toàn vẹn nguồn.

Với Samsung Electro-Mechanics, hợp đồng này mang ý nghĩa chiến lược vượt xa con số doanh thu. Công ty chính thức tuyên bố đã tận dụng năng lực quy trình chính xác tích lũy được từ mảng kinh doanh MLCC và substrate gói chip để gia nhập chuỗi cung ứng cốt lõi bán dẫn AI.[^samsung-sicap-contract]

### 5.3 Ý Nghĩa Đầu Tư — Có Thể Được Tái Phân Loại Thành Cổ Phiếu "Linh Kiện Máy Chủ AI"

Thị trường từ trước đến nay nhìn nhận Samsung Electro-Mechanics như công ty MLCC, mô-đun camera và substrate. Nếu doanh thu tụ silicon tăng lên mức sản xuất đại trà, cách phân loại đó sẽ thay đổi một phần.

| Nhận Định Thị Trường Trước Đây | Nhận Định Có Thể Có Sau Tụ Silicon |
|---|---|
| Cổ phiếu linh kiện smartphone | Cổ phiếu linh kiện máy chủ AI |
| Cổ phiếu chu kỳ MLCC | Cổ phiếu linh kiện tính toàn vẹn nguồn giá trị cao |
| Câu chuyện tăng trưởng MLCC ô tô | Tân binh chuỗi cung ứng đóng gói GPU AI / HBM |
| Phơi lộ với linh kiện thụ động phổ thông | Phơi lộ với linh kiện phức tạp cao trong gói chip |

Tuy nhiên, rủi ro phóng đại vẫn còn. Tụ silicon sẽ không thay thế toàn bộ thị trường MLCC. Tăng trưởng sẽ đến trước tiên ở phần bên trong gói chip AI, điện toán hiệu suất cao, chip di động cao cấp, và một số ứng dụng viễn thông và công nghiệp đòi hỏi hiệu suất cực cao. Phần lớn nhu cầu ổn định nguồn trong smartphone phổ thông, ô tô và thiết bị gia dụng có khả năng vẫn là lãnh địa của MLCC trong tương lai gần.

---

## 6. Diễn Biến Thị Trường Tuần Này — MLCC Bỏ Xa Substrate AI

Tuần này (18–22 tháng 5 năm 2026), thị trường định giá lại mạnh mẽ nhóm cổ phiếu MLCC. Ba cổ phiếu MLCC cốt lõi tăng trung bình <strong>+35,6%</strong>; năm cổ phiếu substrate AI cốt lõi tăng trung bình <strong>+14,0%</strong>.

### 6.1 Rổ Ba Cổ Phiếu MLCC Cốt Lõi

| Tên | Tăng/giảm tuần | 20D | 60D | P/E 2026E | Ngoại | Tổ chức | Ngoại + Tổ chức | Chương trình |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Samwha Capacitor | **+56,4%** | +56,0% | +68,0% | 40,8x | -₩5,88B | +₩16,09B | +₩10,21B | N/A |
| Samsung Electro-Mechanics | **+32,7%** | +65,0% | +200,5% | 73,2x | -₩292,90B | +₩111,79B | -₩181,11B | +₩170,96B |
| Amotech | +17,6% | -18,4% | +55,2% | 18,9x | +₩4,91B | -₩0,87B | +₩4,05B | +₩5,10B |

Samsung Electro-Mechanics ghi nhận ba phiên tăng liên tiếp: +7,5% ngày 20 tháng 5, +13,5% ngày 21 tháng 5, và +11,3% ngày 22 tháng 5. Samwha Capacitor còn mạnh hơn: +23,0% ngày 20 tháng 5, +29,9% ngày 22 tháng 5. Đây ít là một đợt tăng thuần túy dựa trên lợi nhuận mà nhiều hơn là **sự định giá lại linh kiện tính toàn vẹn nguồn AI khởi phát từ Samsung Electro-Mechanics và lan rộng ra cả hệ sinh thái MLCC**.

### 6.2 Rổ Năm Cổ Phiếu Substrate AI Cốt Lõi

| Tên | Tăng/giảm tuần | 20D | 60D | P/E 2026E | Ngoại | Tổ chức | Ngoại + Tổ chức | Chương trình |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Simtech | **+31,4%** | +52,2% | +146,8% | 38,7x | -₩24,58B | +₩61,81B | +₩37,22B | -₩5,35B |
| TLB | +18,0% | +44,4% | +89,2% | 25,3x | -₩7,80B | +₩15,30B | +₩7,50B | -₩3,98B |
| Daeduck Electronics | +11,4% | +49,5% | +132,8% | 38,9x | -₩2,93B | +₩29,05B | +₩26,12B | +₩5,28B |
| Korea Circuit | +10,7% | +5,6% | +66,7% | 25,5x | -₩2,71B | -₩0,58B | -₩3,29B | +₩0,44B |
| ISU Petasys | -1,5% | -21,9% | +12,7% | 35,6x | -₩119,17B | -₩0,74B | -₩119,90B | -₩125,28B |

Rổ substrate AI không tăng đồng đều. Simtech, TLB và Daeduck Electronics tăng mạnh, nhưng ISU Petasys kết thúc tuần ở mức -1,5% trong bối cảnh bán tháo mạnh từ nước ngoài và chương trình. Trong nhóm substrate AI, thị trường tuần này dường như ưu tiên **SoCAMM, mô-đun bộ nhớ và phơi lộ FC-CSP hơn là các bo mạch mạng nhiều lớp**.

### 6.3 Dẫn Đầu Giá Thuộc MLCC; Chất Lượng Dòng Tiền Ưu tiên Một Số Cái Tên Substrate AI

| Rổ | Ngoại | Tổ chức | Ngoại + Tổ chức | Cá nhân | Chương trình |
|---|---:|---:|---:|---:|---:|
| MLCC cốt lõi (3 cổ phiếu) | -₩293,86B | +₩127,01B | -₩166,85B | +₩159,40B | +₩176,05B |
| Substrate AI cốt lõi (5 cổ phiếu) | -₩157,19B | +₩104,84B | -₩52,35B | +₩52,05B | -₩128,89B |
| Substrate AI trừ ISU Petasys | -₩38,02B | +₩105,57B | +₩67,55B | -₩65,47B | -₩3,60B |

Về giá, MLCC áp đảo. Về chất lượng dòng tiền, **rổ substrate AI loại trừ ISU Petasys** cho thấy bức tranh sạch hơn. Simtech, TLB và Daeduck cho thấy rõ ràng tích lũy của tổ chức với cá nhân bán hoặc trung tính — cấu hình mang tính xây dựng hơn. Trong nhóm MLCC, ₩292,9 tỷ bán ròng của khối ngoại tại Samsung Electro-Mechanics không thể bỏ qua. Giá cổ phiếu mạnh, nhưng đây trông giống định giá lại dẫn dắt bởi tổ chức, chương trình và cá nhân hơn là tích lũy dẫn dắt bởi khối ngoại.

---

## 7. Đánh Giá Đầu Tư

| Tên | Nhận Định |
|---|---|
| MLCC | Đà giá mạnh nhất. Có rủi ro quá nhiệt và áp lực bán từ khối ngoại. |
| Substrate AI | Lợi nhuận tuyệt đối thấp hơn, nhưng dòng tiền tổ chức và liên kết lợi nhuận ổn định hơn. |
| Samsung Electro-Mechanics | Dẫn đầu xuyên danh mục về MLCC, FC-BGA và tụ silicon. Nắm giữ có thể biện minh; đuổi theo không nên. |
| Samwha Capacitor | Cường độ mở rộng chủ đề cao nhất. +56% trong một tuần khiến vào lệnh mới cực kỳ khó. |
| Daeduck Electronics | Nắm giữ substrate AI cốt lõi. Chiết khấu định giá so với Samsung Electro-Mechanics là đáng kể. |
| Simtech / TLB | Dẫn đầu đợt mở rộng substrate AI tuần này. Tuần tới, theo dõi giai đoạn tích lũy sau tăng nóng trước khi vào lại. |
| ISU Petasys | Tụt hậu tương đối trong nhóm substrate AI. Ưu tiên thấp hơn cho đến khi dòng tiền ngoại phục hồi. |

Tuần này là tuần **sự chú ý mở rộng từ substrate AI sang MLCC**. Luận điểm substrate AI không bị bác bỏ. Thay vào đó, thị trường đang phân loại tinh hơn "nút thắt tiếp theo sau bộ nhớ" — kéo dài định giá lại sang các linh kiện tính toàn vẹn nguồn máy chủ AI.

Về thực tế:

```text
Nắm giữ: Samsung Electro-Mechanics, Daeduck Electronics
Không đuổi theo: Samsung Electro-Mechanics, Samwha Capacitor
Theo dõi khi điều chỉnh: Simtech, TLB
Chờ dòng tiền phục hồi: ISU Petasys
Xác nhận chính cần có: Liệu tăng giá MLCC và doanh thu máy chủ AI có nâng kỳ vọng lợi nhuận Q2–Q3 không
```

---

## 8. Kết Luận Một Dòng

MLCC là "bể chứa nước gốm siêu nhỏ gọn" của ngành điện tử. Tụ silicon là "bộ ổn định nguồn cực gần" được nhúng bên trong các gói chip GPU AI và HBM. Tụ silicon không thay thế MLCC. Chiến trường của linh kiện thụ động đang mở rộng từ bề mặt PCB vào bên trong các gói chip bán dẫn AI.

Ý nghĩa thực sự của hợp đồng ₩1,5 nghìn tỷ của Samsung Electro-Mechanics không phải là "bán thêm một loại tụ điện nữa." Đó là tín hiệu rằng **một nhà sản xuất linh kiện thụ động đã gia nhập chuỗi cung ứng linh kiện then chốt bên trong các gói chip bán dẫn AI**. Sự chuyển dịch này có thể tái phân loại các dòng sản phẩm cao cấp của Samsung Electro-Mechanics và Murata thành tài sản chuỗi giá trị hạ tầng AI.

Tuy nhiên, thị trường đã phản ứng nhanh. Ba cổ phiếu MLCC cốt lõi tăng trung bình +35,6% trong tuần; Samsung Electro-Mechanics tăng +200,5% trong 60 ngày và giao dịch ở P/E 73,2x dự phóng 2026. Công ty xuất sắc và sự chuyển dịch ngành là có thực. Liệu mức giá hôm nay có phải là điểm vào mới tốt hay không là câu hỏi hoàn toàn riêng biệt. Chất xúc tác tiếp theo cần theo dõi không phải là diễn biến giá mà là **điều chỉnh lợi nhuận Q2–Q3, công bố doanh thu máy chủ AI phân tách, các đơn hàng tụ silicon tiếp theo và sự phục hồi dòng tiền ngoại**.

---

*Bài viết này chỉ phục vụ mục đích nghiên cứu và bình luận, không cấu thành lời khuyên đầu tư. Mô tả kỹ thuật về tụ điện, MLCC và tụ silicon dựa trên tài liệu chính thức của Samsung Electro-Mechanics, TDK, Murata và các nguồn kỹ thuật công khai khác. Hợp đồng cung ứng tụ silicon của Samsung Electro-Mechanics (khoảng ₩1,5 nghìn tỷ, từ ngày 1 tháng 1 năm 2027 đến ngày 31 tháng 12 năm 2028) phản ánh thông báo chính thức của công ty. Khách hàng chưa được tiết lộ công khai; không có GPU, ASIC hay công ty đám mây cụ thể nào được xác định là đối tác. Dữ liệu giá, dòng tiền và định giá cho giai đoạn 18–22 tháng 5 năm 2026 lấy từ cơ sở dữ liệu cục bộ Research OS của người dùng và có thể khác với dữ liệu chính thức của sàn hoặc nhà môi giới. P/E 2026E, số liệu dòng tiền ngoại/tổ chức/chương trình và bình quân rổ cho nhóm ba cổ phiếu MLCC cốt lõi và năm cổ phiếu substrate AI cốt lõi phản ánh phân loại của nhà phân tích. Phân tích có thể sai. Ngày tham chiếu dữ liệu: 22 tháng 5 năm 2026, giờ KST.*

[^samsung-mlcc]: [Samsung Electro-Mechanics, Mô Tả Sản Phẩm MLCC](https://samsungsem.com/kr/product/passive-component/mlcc.do)
[^samsung-sicap-product]: [Samsung Electro-Mechanics, Mô Tả Sản Phẩm Tụ Silicon](https://www.samsungsem.com/global/product/passive-component/silicon-capacitor.do)
[^samsung-sicap-contract]: [Samsung Electro-Mechanics, Thông Báo Hợp Đồng Cung Ứng Tụ Silicon Trị Giá ₩1,5 Nghìn Tỷ](https://samsungsem.com/global/newsroom/news/view.do?id=10310)
[^tdk-capacitors]: [TDK, Danh Mục Sản Phẩm Tụ Điện và Tài Liệu Ứng Dụng Hệ Thống Nguồn Máy Chủ AI](https://product.tdk.com/en/products/capacitor/index.html)

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
