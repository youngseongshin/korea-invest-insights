---
title: "HBM, HBF và HBC: Cách phân biệt ba công nghệ bộ nhớ AI"
slug: "hbm-hbf-hbc-ai-memory-comparison-2026-06-22"
date: 2026-06-22T10:00:00+09:00
description: "HBM, HBF và HBC không phải cùng loại bộ nhớ. Bài viết phân tích băng thông, dung lượng và chi phí suy luận như ba bức tường riêng biệt, so sánh mức độ trưởng thành một cách trung thực."
categories: ["Exclusive Analysis", "Tech-Analysis"]
tags: ["HBM", "HBF", "HBC", "Bộ nhớ AI", "Bán dẫn", "SK Hynix", "Samsung Electronics", "Micron", "Qualcomm", "NAND", "DRAM"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Bối cảnh
> Bài viết này là phần nền kỹ thuật của [Ai trả tiền cho đồng thuận bán dẫn năm 2027](/vi/post/semiconductor-2027-earnings-hyperscaler-payability-memory-nvidia-2026-06-21/), [IPO CXMT và rủi ro giá bộ nhớ](/vi/post/cxmt-ipo-memory-price-risk-hbm-client-dram-2026-06-21/), và [Vì sao siêu chu kỳ AI ngày càng kéo dài](/vi/post/ai-supercycle-extension-agent-demand-ipo-funding-memory-storage-2026-06-12/). Nếu các bài trước tập trung vào cầu, giá và định giá, thì bài này đi thẳng vào câu hỏi: <strong>ba công nghệ bộ nhớ AI về phía cung thực sự là gì, đã được kiểm chứng đến đâu, và quan hệ giữa chúng như thế nào</strong>. Các hub liên quan: [Hub HBM Hàn Quốc](/vi/page/korea-semiconductor-hbm-kospi-hub/) và [Hub Phân tích Độc quyền](/vi/page/exclusive-analysis-hub/).

## TL;DR

* HBM, HBF và HBC không phải cùng một loại bộ nhớ. <strong>HBM và HBF là linh kiện bộ nhớ</strong>, còn <strong>HBC là tên kiến trúc bộ tăng tốc của Qualcomm</strong>. Xếp cả ba trên cùng một hàng và so sánh đơn thuần bằng số TB/s là cách đọc sai chắc chắn xảy ra.
* Ba công nghệ nhắm vào ba bức tường khác nhau. <strong>HBM là bức tường băng thông</strong>, <strong>HBF là bức tường dung lượng</strong>, <strong>HBC là chi phí và điện năng cho suy luận</strong>.
* Khoảng cách trưởng thành là rất lớn. <strong>HBM đã vào sản xuất đại trà hoàn toàn (★★★★★)</strong>, <strong>HBF còn ở giai đoạn mô phỏng (★★, mục tiêu ra mẫu nửa cuối 2026)</strong>, <strong>HBC mới là bản vẽ thiết kế (★, mục tiêu lấy mẫu năm 2027)</strong>.
* Ba công nghệ là bổ trợ, không phải cạnh tranh. "Nhiệt độ" của dữ liệu quyết định vị trí phù hợp. Dữ liệu nóng (KV cache) thuộc về HBM, dữ liệu lạnh (trọng số mô hình cố định) thuộc về HBF, suy luận chi phí thấp thuộc về hướng HBC.
* Hiện tại không có công nghệ nào đe dọa được vị trí bộ nhớ làm việc của HBM. Đóng góp doanh thu có ý nghĩa từ HBF và HBC sớm nhất cũng phải đến năm 2027-2028. \[Suy luận\]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Luận điểm chính</div>
  <div class="thesis-callout__body">
    Trong cuộc chiến bộ nhớ AI, thứ duy nhất được kiểm chứng đến nay là HBM. HBF là lời hứa, HBC là bản vẽ. Cả ba không phải đối thủ cạnh tranh mà là những mảnh ghép bổ trợ lấp đầy các tầng khác nhau trong hệ thống phân cấp bộ nhớ.
  </div>
</div>

---

## 1. Nút thắt cổ chai của AI không phải là tính toán mà là bộ nhớ

Sức mạnh tính toán của GPU đã tăng khoảng 80 lần trong 10 năm qua, nhưng băng thông bộ nhớ chỉ tăng khoảng 17 lần. \[Thực tế: So sánh thông số kỹ thuật các thế hệ NVIDIA\] Khoảng cách đó chính là nút thắt cổ chai thực sự của các chip AI ngày nay. Chip AI đắt tiền ngày càng phải chờ đợi dữ liệu nhiều hơn, và tốc độ tạo từng token của LLM gần như phụ thuộc hoàn toàn vào khả năng vận chuyển dữ liệu của bộ nhớ.

Nút thắt này chia thành hai bức tường.

<strong>Bức tường băng thông:</strong> Không thể vận chuyển dữ liệu đủ nhanh. Giai đoạn giải mã (decode) khi suy luận LLM phải đọc các trọng số mô hình khổng lồ từ bộ nhớ cho mỗi token được tạo ra, khiến tốc độ luôn bị ràng buộc bởi tốc độ bộ nhớ.

<strong>Bức tường dung lượng:</strong> Không thể chứa đủ nhiều dữ liệu. Chỉ riêng KV cache sinh ra trong ngữ cảnh 128.000 token đã khoảng 343 GB, vượt qua dung lượng HBM 192 GB của GPU thế hệ mới nhất (B200). \[Thực tế: Tính toán từ thông số công khai\]

HBM, HBF và HBC là các công nghệ tấn công hai bức tường này theo những cách khác nhau. Và trong số ba thứ đó, một cái không phải là linh kiện bộ nhớ mà là kiến trúc bộ tăng tốc của một công ty. Bỏ qua sự phân biệt này thì việc so sánh sẽ sụp đổ hoàn toàn.

---

## 2. HBM: Công nghệ duy nhất được kiểm chứng, giải quyết bức tường băng thông

### Khái niệm

Ý tưởng của HBM (High Bandwidth Memory) rất súc tích. Xếp chồng 8-16 lớp chip DRAM theo chiều dọc và gắn ngay bên cạnh GPU, kết nối chúng bằng hàng nghìn điện cực siêu nhỏ (TSV) để mở rộng kênh truyền dữ liệu trao đổi cùng lúc lên tới 1.024-2.048 bit. Không phải vì một chân đơn lẻ nhanh hơn mà vì con đường truyền dữ liệu rộng cực độ mới nhanh. Nguyên lý tương tự như một con đường 2.048 làn xe có tổng lưu lượng lớn hơn nhiều so với một làn đơn dù nhanh hơn.

### Hiệu suất và mức độ kiểm chứng

Băng thông của một stack HBM3E là khoảng 1,2 TB/s, còn HBM4 đạt khoảng 2 TB/s. \[Thực tế: Thông số JEDEC\] Gấp 20-30 lần DDR5. Thực tế là tất cả các chip AI như NVIDIA H100, H200, B200, AMD MI300... đều tích hợp HBM.

<strong>Mức độ kiểm chứng ★★★★★:</strong> Trong ba công nghệ, chỉ có HBM đang ở trạng thái sản xuất đại trà hoàn toàn. Sau nhiều năm sản xuất quy mô lớn, tỷ lệ lợi suất và độ tin cậy đã được xác nhận. SK Hynix chiếm khoảng 57-62% thị phần và duy trì vị trí nhà cung cấp chính cho NVIDIA. \[Thực tế: IR doanh nghiệp và ước tính thị trường\]

### Lộ trình và các bên tham gia

Lộ trình tiếp nối từ HBM4 (sản xuất đại trà 2026, áp dụng logic base die) sang HBM4E (tùy chỉnh theo khách hàng), rồi đến HBM5 (mục tiêu 2029, 4 TB/s). Từ HBM4, SK Hynix sản xuất base die bằng tiến trình 12nm của TSMC, tạo ra cấu trúc mà công ty bộ nhớ và xưởng đúc cùng tham gia thiết kế. \[Thực tế: Thông báo của doanh nghiệp\] \[Suy luận: Con số 4 TB/s của HBM5 là mục tiêu lộ trình, chưa được đo lường thực tế\]

Các bên tham gia là thế độc quyền ba công ty SK Hynix, Samsung Electronics và Micron, với TSMC đóng vai trò nền tảng thông qua base die và interposer. Thị trường bộ nhớ AI là cấu trúc liên doanh giữa ba công ty bộ nhớ, TSMC và NVIDIA. \[Suy luận: Quy mô thị trường ước tính khoảng 35 tỷ USD năm 2025 và 45-58 tỷ USD năm 2026, độ lệch lớn giữa các nguồn\]

---

## 3. HBF: Tân binh nhắm vào bức tường dung lượng, vẫn còn là lời hứa

### Khái niệm

Ý tưởng của HBF (High Bandwidth Flash) khá thông minh. Mượn nguyên xi phương pháp xếp chồng và giao tiếp của HBM, nhưng thay thế DRAM đắt tiền bên trong bằng flash NAND giá rẻ. NAND có thể lưu nhiều bit trong một ô nhớ, dung lượng lớn hơn và chi phí mỗi GB thấp hơn nhiều. Tháng 8 năm 2025, SanDisk và SK Hynix đã thông báo hợp tác chuẩn hóa. SanDisk mô tả điều này là "bổ sung (augment) chứ không thay thế HBM." \[Thực tế: Thông báo chung của SanDisk và SK Hynix\]

SanDisk tuyên bố có thể chứa khoảng 512 GB trong một stack (gấp 8-16 lần HBM) với băng thông đạt khoảng 1,6 TB/s. \[Thực tế: Factsheet của SanDisk\]

### Đánh giá mức độ kiểm chứng một cách trung thực

Cần dừng lại ở đây.

<strong>Mức độ kiểm chứng ★★:</strong> HBF chưa vào sản xuất đại trà, thậm chí chưa có một benchmark độc lập nào từ chip thực tế. Con số 512 GB và 1,6 TB/s là từ mô phỏng nội bộ của SanDisk, và chú thích của factsheet cũng ghi rõ "kiểm tra và mô phỏng nội bộ, giả định mô hình cụ thể." \[Thực tế: Chú thích factsheet của SanDisk\] Mục tiêu ra mẫu thực vật đầu tiên là nửa cuối năm 2026, và việc áp dụng cho thiết bị suy luận là sau năm 2027. Còn phải vượt qua độ khó xếp chồng hơn 5.000 lớp khi ghép 16 lớp NAND 238 tầng với nhau.

### Điểm yếu của NAND xác định phạm vi sử dụng

HBF có hai hạn chế.

Thứ nhất, <strong>độ trễ:</strong> NAND đọc chậm hơn DRAM nên độ trễ của HBF dài hơn HBM khoảng 100 lần (HBF khoảng 10 µs so với HBM vài chục ns). \[Thực tế: Đặc tính vật liệu\]

Thứ hai, <strong>tuổi thọ ghi:</strong> NAND có giới hạn số lần ghi, không phù hợp cho các tác vụ cập nhật thường xuyên.

Hai điểm yếu này xác định phạm vi sử dụng của HBF: <strong>kho lưu trữ dung lượng lớn chứa trọng số mô hình</strong>, thứ hầu như không thay đổi và chỉ cần đọc. Trong phạm vi đó, hai điểm yếu gần như không thành vấn đề.

### Biến số quyết định: Việc áp dụng của NVIDIA

<strong>Hiện tại NVIDIA không tỏ ra quan tâm nhiều đến HBF.</strong> Có tín hiệu cho thấy họ muốn giải quyết vấn đề dung lượng theo hướng SSD tốc độ cao kết nối trực tiếp vào GPU (eSSD), trong khi khách hàng lớn tỏ ra quan tâm đến HBF chủ yếu là Google. \[Suy luận: Tổng hợp quan sát ngành và thông tin công khai\] Việc khách hàng lớn nhất có áp dụng hay không là ẩn số lớn nhất quyết định thành bại của HBF.

Các bên tham gia: SanDisk dẫn đầu, SK Hynix hợp tác, Samsung tham gia, trong khi Kioxia chọn con đường khác là eSSD. Các phe phái vẫn chưa được định hình rõ ràng.

---

## 4. HBC: Đây không phải bộ nhớ, đây là kiến trúc bộ tăng tốc của Qualcomm

### Làm rõ thuật ngữ trước tiên

"HBC" là một từ viết tắt có bẫy. Dù được đặt cạnh HBM và HBF, nhưng <strong>HBC là tên kiến trúc bộ tăng tốc AI của Qualcomm được công bố tại Ngày Nhà đầu tư tháng 6 năm 2026</strong> ("High Bandwidth Compute"). Đây không phải thuật ngữ tiêu chuẩn được nhiều công ty đồng thuận mà là thương hiệu của một công ty. \[Thực tế: Thông báo chính thức của Qualcomm\]

Từ viết tắt "HBC" tương tự xung đột với "High Bandwidth Cache (HBCC)" của AMD, và cũng bị nhầm lẫn với HBF. Cả ba là những khái niệm hoàn toàn khác nhau.

Do đó, so sánh "HBM vs HBF vs HBC" về bản chất là <strong>so sánh 2 linh kiện bộ nhớ với 1 thiết kế bộ tăng tốc</strong>. Không hiểu sự bất đối xứng này dễ rơi vào phương trình sai như "HBC có băng thông gấp 18 lần HBM" (vì đơn vị chuẩn khác nhau).

### Khái niệm và công nghệ

Vật liệu bộ nhớ mà HBC sử dụng không phải HBM mà là <strong>LPDDR</strong> (DRAM điện áp thấp dùng trong điện thoại thông minh). Ý tưởng là xếp chồng LPDDR giá rẻ này theo chiều 3D ngay trên chip logic tính toán, rút ngắn khoảng cách giữa tính toán và bộ nhớ xuống gần bằng 0. Cách tiếp cận này không cần interposer silicon đắt tiền, không cần HBM đắt tiền, nhằm giảm chi phí và điện năng suy luận.

Qualcomm đưa ra các con số như băng thông trên watt gấp 6 lần HBM, dung lượng trên watt gấp 200 lần SRAM. \[Thực tế: Thông báo của Qualcomm\] Tuy nhiên, các con số này là tuyên bố của chính Qualcomm được chuẩn hóa theo đơn vị card/rack, và dễ đọc sai nếu so sánh trực tiếp với số liệu đơn vị stack của HBM vì tiêu chuẩn khác nhau.

### Mức độ kiểm chứng và thực tế

<strong>Mức độ kiểm chứng ★:</strong> Chip AI250 của Qualcomm tích hợp HBC chưa tồn tại thực tế và mục tiêu lấy mẫu là giữa năm 2027. Tất cả số liệu hiệu suất được công bố đều là mục tiêu thiết kế. \[Thực tế: Thông báo của Qualcomm\] Nếu HBF ở giai đoạn mô phỏng thì HBC mới ở giai đoạn bản vẽ. Có tin đồn Microsoft và Meta đặt hàng bộ tăng tốc của Qualcomm nhưng chưa được xác nhận. \[Suy luận: Thông tin thứ cấp, chưa kiểm chứng\]

Cách đọc đúng về HBC không phải là "bộ nhớ cạnh tranh với HBM" mà là <strong>"chiến lược hệ thống của một công ty nhằm chạy suy luận rẻ hơn mà không dùng HBM."</strong> Nếu thành công, có thể ảnh hưởng đến một phần phân khúc suy luận chi phí thấp trong nhu cầu HBM, nhưng không phải bức tranh thay thế HBM toàn bộ. Các bên tham gia thực tế cũng chỉ là Qualcomm độc lập.

---

## 5. Bổ trợ không phải cạnh tranh: "Nhiệt độ" dữ liệu quyết định vị trí

Tiêu đề "HBF giết chết HBM", "HBC thay thế HBM" xuất hiện thường xuyên. Kết luận sau kiểm chứng là những cái đó đều bị phóng đại. Về bản chất, ba công nghệ có quan hệ bổ trợ.

Lý do không phải từ logic thị trường trừu tượng mà từ đặc tính vật lý của dữ liệu.

Dữ liệu được nạp vào bộ nhớ khi suy luận LLM có hai loại.

<strong>Trọng số mô hình (dữ liệu lạnh):</strong> Khi quá trình huấn luyện kết thúc, gần như không thay đổi và chỉ được đọc trong mỗi lần suy luận. Có thể lưu trong bộ nhớ chậm nhưng lớn và rẻ (HBF) mà không bị thiệt hại. Hạn chế tuổi thọ ghi của NAND cũng gần như không thành vấn đề với trọng số "chỉ đọc."

<strong>KV cache (dữ liệu nóng):</strong> Cập nhật liên tục trong quá trình hội thoại. Phải được lưu trong bộ nhớ nhanh nhất (HBM). Nếu thay bằng bộ nhớ chậm thì toàn bộ hệ thống sẽ chậm lại.

HBM và HBF chênh lệch độ trễ khoảng 100 lần, về mặt vật lý không thể cùng đứng ở vị trí "bộ nhớ làm việc." HBF không đẩy HBM ra mà là tầng bên dưới tiếp nhận những gì HBM không chứa được. HBC lại theo đuổi suy luận chi phí thấp trên một đường ray hoàn toàn khác.

Chip AI trong tương lai sẽ không phải là lựa chọn "HBM hay HBF" mà có khả năng cao sẽ đi theo <strong>hệ thống 3 tầng: HBM + HBF + SSD tốc độ cao</strong>. \[Suy luận: Phân tích lộ trình công nghệ\]

Tuy nhiên, sự cạnh tranh một phần là có thực. Cuộc cạnh tranh giải quyết vấn đề dung lượng bằng HBF hay eSSD vẫn còn mở. Trong thị trường suy luận chi phí thấp, chip tăng tốc HBC và chip tăng tốc HBM cũng có phần chồng lấp. Nếu HBF và HBC thành công trong việc mở ra con đường "dung lượng lớn với giá rẻ," sẽ có thêm động lực để khách hàng mua ít HBM đắt tiền hơn, tạo ra kịch bản xói mòn biên. Tuy nhiên, tất cả những cạnh tranh này đều là câu chuyện của sau năm 2027.

---

## 6. Các cột mốc cần theo dõi ngay bây giờ

Cả ba công nghệ đều có thời điểm chuyển từ "lời hứa" sang "thực tế" khác nhau.

<strong>HBM đang diễn ra.</strong> Tỷ lệ lợi suất sản xuất HBM4, sự mở rộng HBM tùy chỉnh theo khách hàng, và quá trình chuyển đổi sang hybrid bonding là những điểm quan sát tiếp theo. SK Hynix, Samsung, Micron và TSMC sẽ tiếp tục nắm giữ phần lớn giá trị bộ nhớ AI trong thời gian tới. \[Suy luận: Ước tính thị phần\]

<strong>Với HBF, có hai cột mốc quan trọng nhất.</strong> Thứ nhất, mẫu thực vật đầu tiên và benchmark độc lập vào nửa cuối năm 2026. Vì tất cả số liệu cho đến nay đều là mô phỏng, thời điểm ra mẫu thực là quyết định. Thứ hai, việc NVIDIA có áp dụng hay không. Nếu áp dụng, phe HBF sẽ được định hình nhanh chóng; nếu không, sẽ vẫn là phe thiểu số.

<strong>Với HBC, cột mốc đầu tiên là mẫu thực và xác minh độc lập từ AI250 của Qualcomm vào năm 2027.</strong> Việc xác nhận đơn hàng từ Microsoft và Meta cũng là thước đo mức độ mở rộng hệ sinh thái HBC.

---

## Kiểm tra thổi phồng

Có một số tuyên bố thường xuất hiện trong lĩnh vực này cần đề phòng.

<strong>"HBF/HBC thay thế HBM":</strong> Độ trễ và vai trò khác nhau, nên đây là quan hệ bổ trợ. Câu chuyện thay thế là phóng đại.

<strong>"Dung lượng gấp 16 lần, 4 TB VRAM, điện năng gấp 6 lần":</strong> Hầu hết là mô phỏng nội bộ của công ty hoặc mục tiêu thiết kế, không phải đo lường độc lập.

<strong>"HBM bị đe dọa năm 2026":</strong> Đóng góp doanh thu có ý nghĩa từ HBF và HBC sớm nhất cũng phải đến năm 2027-2028.

<strong>"HBC là bộ nhớ thế hệ tiếp theo":</strong> Lỗi phân loại. HBC không phải bộ nhớ mà là kiến trúc bộ tăng tốc của Qualcomm.

Thừa nhận tiềm năng nhưng tách biệt tiêu đề marketing khỏi thực tế đã được xác minh là điểm xuất phát của phân tích.

---

_Bài viết này là tài liệu phân tích kỹ thuật dựa trên các nguồn sơ cấp, thứ cấp và tam cấp công khai cùng thông báo doanh nghiệp. Đây không phải khuyến nghị đầu tư vào bất kỳ cổ phiếu hay sản phẩm cụ thể nào. Phần lớn số liệu hiệu suất của HBF và HBC là tuyên bố của công ty, mô phỏng hoặc mục tiêu, chưa được xác minh độc lập. Đây là lĩnh vực thay đổi nhanh, vì vậy nên cập nhật và xác nhận bằng nguồn sơ cấp mới nhất._

---

### Bài viết liên quan

- [Ai trả tiền cho đồng thuận bán dẫn năm 2027](/vi/post/semiconductor-2027-earnings-hyperscaler-payability-memory-nvidia-2026-06-21/)
- [IPO CXMT và rủi ro giá bộ nhớ](/vi/post/cxmt-ipo-memory-price-risk-hbm-client-dram-2026-06-21/)
- [Phân tích TechWing HBM Cube Prober](/vi/post/techwing-hbm-cube-prober-big3-conditional-buy-2026-06-21/)
- [Vì sao siêu chu kỳ AI ngày càng kéo dài](/vi/post/ai-supercycle-extension-agent-demand-ipo-funding-memory-storage-2026-06-12/)
- [Samsung và SK Hynix chiếm 90,8% ETF bán dẫn Hàn Quốc](/vi/post/korea-semiconductor-etf-exposure-marketcap-gap-strategy-2026-06-13/)
