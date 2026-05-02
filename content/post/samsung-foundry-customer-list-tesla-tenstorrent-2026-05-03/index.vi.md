---
title: "Danh Sách Khách Hàng Samsung Foundry 2026 — Ai Đang Dùng Samsung Foundry? Tesla, Tenstorrent, Qualcomm, Google, Ambarella và Toàn Bộ Các Đối Tác Đã Được Xác Nhận"
slug: samsung-foundry-customer-list-tesla-tenstorrent-2026-05-03
date: 2026-05-03T11:00:00+09:00
description: "Khách hàng của Samsung Foundry năm 2026 — được xác nhận qua các buổi báo cáo kết quả kinh doanh, công bố từ phía khách hàng và thông tin chuỗi cung ứng — bao gồm Tesla (HW5/thế hệ kế tiếp của Dojo tại SF2), Tenstorrent (Wormhole/Blackhole tại SF4X), Qualcomm (một số dòng modem và Snapdragon), Google (các thế hệ TPU tiếp theo và Pixel SoC tại SF4LPP/SF3), Ambarella (CV3-AD ADAS), và chính bộ phận System LSI của Samsung (Exynos). Nhìn thẳng vào thực tế: Samsung Foundry vẫn là cái tên đáng tin cậy ở vị trí số 2 sau TSMC tại các node tiên tiến, với danh sách khách hàng nghiêng mạnh về chip tăng tốc AI, SoC ô tô/ADAS, và những khách hàng sẵn sàng chấp nhận rủi ro hiệu suất để đổi lấy năng lực sản xuất hoặc lý do chuỗi cung ứng chủ quyền."
categories: ["Sector-Deep-Dive", "Korea Market", "AI Infrastructure"]
tags:
  - "Samsung Foundry"
  - "005930"
  - "Samsung Electronics"
  - "Tesla"
  - "Tenstorrent"
  - "Qualcomm"
  - "Google"
  - "Ambarella"
  - "TSMC"
  - "chip AI"
  - "xưởng đúc chip"
  - "bán dẫn"
  - "SF2"
  - "SF3"
  - "SF4"
  - "cổ phiếu Hàn Quốc"
---

> 🔗 **Bài liên quan**: [Thị phần HBM của SK hynix](/post/sk-hynix-hbm-market-share-ai-memory-demand-2026/) · [OpenEdges Technology — IP trung tâm dữ liệu LPDDR6/5X](/post/openedges-lpddr-datacenter-ip-alpha-thesis-2026-04-30/) · [Big Tech Q1/2026 → Samsung Electronics vs Samsung Electro-Mechanics](/post/bigtech-1q26-samsung-electronics-vs-electro-mechanics-2026-04-30/)

*Bài viết này trả lời thẳng câu hỏi — "Ai đang dùng Samsung Foundry năm 2026?" — rồi lý giải tại sao mỗi khách hàng chọn Samsung, họ đang dùng node nào, và cơ cấu khách hàng đó nói lên điều gì về vị thế của Samsung Foundry so với TSMC.*

---

## TL;DR

**Câu trả lời ngắn gọn.** Danh sách khách hàng đã được xác nhận của Samsung Foundry năm 2026, xếp theo mức độ ảnh hưởng kinh tế, bao gồm:

- **Tesla** — khách hàng nhiều thế hệ (HW3 → chuẩn bị HW4), với SoC xe tự lái thế hệ tiếp theo và các chip tăng tốc liên quan đến Dojo trên các node tiên tiến của Samsung (SF4 / SF3 / SF2 được ghi nhận trên báo chí chuyên ngành).
- **Tenstorrent** — dòng chip tăng tốc AI Wormhole và Blackhole trên các node tiên tiến của Samsung Foundry, bao gồm SF4X chuẩn 4nm. Công ty ASIC do Jim Keller dẫn dắt này là đối tác công khai của Samsung Foundry.
- **Qualcomm** — chia sản xuất giữa Samsung Foundry và TSMC; một số modem (5G/6G) và các biến thể Snapdragon SoC nhất định theo lịch sử đã được sản xuất tại các node tiên tiến của Samsung.
- **Google** — Pixel Tensor SoC (dòng G3/G4) trên các node chuẩn 4nm của Samsung; một phần sản xuất liên quan đến TPU theo lịch sử cũng dùng năng lực Samsung, dù TSMC nổi bật hơn ở các thế hệ TPU mới nhất.
- **Ambarella** — SoC ô tô ADAS CV3-AD trên node chuẩn 5nm của Samsung.
- **Samsung System LSI** — Exynos 2400 / Exynos Auto / logic image sensor, khối lượng công việc nội bộ làm nền tảng cho năng lực Samsung Foundry.
- **Các công việc chip AI liền kề NVIDIA và startup** — một số chip tăng tốc và chip mạng theo lịch sử đã dùng năng lực Samsung.
- **Fabless Hàn Quốc và Nhật Bản** — Rebellions, FuriosaAI (Renegade thế hệ tiếp theo), các khách hàng tầm DB HiTek, và các công ty AI ASIC châu Á đang sử dụng dây chuyền sản xuất 4 / 5 / 8 / 12nm của Samsung Foundry.

**Nhận định thực tế.** Samsung Foundry năm 2026 **không** ngang hàng với TSMC ở mặt trận tiên tiến nhất — TSMC vẫn giành được phần lớn công việc chip AI tiên tiến khối lượng cao (NVIDIA, AMD, Apple silicon). Điều Samsung Foundry **thực sự là** năm 2026: một cái tên đáng tin cậy ở vị trí số 2, với danh sách khách hàng nghiêng mạnh về (a) chip tăng tốc AI cần năng lực sản xuất ngoài TSMC, (b) SoC ô tô / ADAS, (c) khách hàng sẵn sàng trả thêm chi phí rủi ro hiệu suất để đổi lấy năng lực, chuỗi cung ứng chủ quyền, hoặc giá tốt hơn. Cơ cấu khách hàng này đúng với những gì bạn kỳ vọng từ một "xưởng đúc thách thức có năng lực node tiên tiến thực sự nhưng còn câu hỏi tồn đọng về hiệu suất."

---

## 1. Tại Sao "Ai Dùng Samsung Foundry?" Là Câu Hỏi Đúng Đắn

Vị thế của Samsung Foundry là chủ đề bị báo chí chuyên ngành đưa tin mâu thuẫn nhiều hơn gần như bất kỳ chủ đề nào khác trong ngành bán dẫn. Tuần này headline là "Samsung giành Tesla / Qualcomm / Google" — tuần sau lại là "Samsung mất [X] vào tay TSMC."

Để cắt bỏ tiếng ồn, cần đặt một câu hỏi khác. Không phải "Samsung Foundry có đang thắng không?" — câu hỏi đó không có câu trả lời rõ ràng vì phụ thuộc vào góc nhìn bạn chọn. Thay vào đó: **ai thực sự đang dùng Samsung Foundry năm 2026, và cơ cấu khách hàng đó nói lên điều gì?**

Cơ cấu khách hàng là thước đo trung thực duy nhất về vị thế của một xưởng đúc, bởi vì:

1. **Phân bổ năng lực sản xuất có thể quan sát được.** Các công bố từ khách hàng, tham chiếu trong buổi báo cáo kết quả, và thông tin chuỗi cung ứng từ báo chí chuyên ngành tiết lộ ai đang thực sự in wafer tại fab nào.
2. **Cơ cấu khách hàng phản ánh các đánh đổi về hiệu suất, năng lực và giá.** Một xưởng đúc giành được khách hàng ở node tiên tiến hoặc là đã giải quyết được vấn đề hiệu suất, hoặc có lợi thế năng lực mà TSMC không thể đáp ứng, hoặc đang định giá tích cực. Cơ cấu khách hàng cho bạn biết đâu là lý do thực.
3. **Cơ cấu khách hàng dự báo mức sử dụng 2027–2028.** Danh sách khách hàng của Samsung Foundry năm 2026 phần lớn quyết định sản lượng sản xuất năm 2027. Những khách hàng thấy được hôm nay *chính là* doanh thu hai năm tới.

---

## 2. Cơ Cấu Khách Hàng Đã Xác Nhận — Ai, Ở Đâu, và Tại Sao

### 2.1 Tesla — Mỏ Neo Nhiều Thế Hệ

**Tình trạng.** Tesla là khách hàng của Samsung Foundry qua nhiều thế hệ sản phẩm. Chip FSD Hardware 3 (HW3) được sản xuất trên node 14nm của Samsung. Chip Hardware 4 (HW4) chuyển sang node chuẩn 7nm. Hardware 5 / SoC xe tự lái thế hệ tiếp theo được báo chí chuyên ngành liên hệ với SF4 và các node trên lộ trình (SF3 / SF2), với việc sử dụng năng lực Samsung tiếp tục xuyên suốt 2026 và xa hơn.

**Tại sao chọn Samsung.** Tesla nhất quán vận hành chiến lược mua wafer từ hai nhà cung cấp — TSMC cho sản xuất GPU/chip AI cấp Dojo, Samsung cho SoC FSD/HW. Cam kết với Samsung nhiều khả năng phản ánh tổ hợp: (a) năng lực sản xuất mà TSMC không thể đáp ứng theo khối lượng Tesla cần, (b) đòn bẩy giá mà Tesla khai thác được từ vị thế thách thức của Samsung, và (c) tính liên tục của nền tảng FSD đã được xây dựng trong mối quan hệ từ HW3.

**Ý nghĩa với Samsung.** Tesla là cái tên gần nhất với "khách hàng biểu trưng" mà Samsung Foundry có — một tên tuổi Mỹ niêm yết đại chúng mà xe của họ phụ thuộc vào silicon do Samsung sản xuất. Mất Tesla vào tay TSMC sẽ là tín hiệu tiêu cực nặng nề nhất có thể; giữ được Tesla qua HW5 là một trong những tín hiệu tích cực mạnh nhất.

### 2.2 Tenstorrent — Cược Công Khai Của Jim Keller Vào Samsung

**Tình trạng.** Chip tăng tốc AI Wormhole và thế hệ tiếp theo Blackhole của Tenstorrent được công bố công khai là sản xuất tại Samsung Foundry. CEO Tenstorrent Jim Keller đã có nhiều buổi phỏng vấn công khai thảo luận về quan hệ đối tác với Samsung Foundry, với công ty chuyển công việc sản xuất node tiên tiến sang SF4X chuẩn 4nm của Samsung.

**Tại sao chọn Samsung.** Định vị của Tenstorrent là "startup chip tăng tốc AI đặt cược chống lại hệ sinh thái NVIDIA/CUDA." Chọn Samsung thay vì TSMC cho sản xuất node tiên tiến nhất quán với định vị ngược chiều đó. Năng lực sản xuất của Samsung và mô hình hợp tác linh hoạt hơn so với khung ưu tiên khách hàng cấp 1 của TSMC được cho là các yếu tố quan trọng.

**Ý nghĩa với Samsung.** Tenstorrent là sự chứng thực công khai nhất về chip tăng tốc AI mà Samsung Foundry có. Khi lượng xuất hàng Tenstorrent mở rộng, tỷ trọng doanh thu Samsung Foundry từ chip tăng tốc AI ngoài NVIDIA tăng lên. Đây là sự đa dạng hóa có ý nghĩa thoát khỏi thế "Samsung Foundry = khối lượng công việc nội bộ Samsung System LSI."

### 2.3 Qualcomm — Chia Nguồn Giữa Samsung và TSMC

**Tình trạng.** Các Snapdragon SoC hàng đầu của Qualcomm theo lịch sử được chia giữa Samsung Foundry và TSMC qua các thế hệ. Snapdragon 8 Gen 1 là thắng lợi đáng chú ý của Samsung ở node chuẩn 4nm; các flagship tiếp theo (Snapdragon 8 Gen 2, Gen 3, Snapdragon 8 Elite) chuyển chủ yếu sang TSMC. Tuy nhiên, Qualcomm vẫn tiếp tục sản xuất một số modem và các biến thể Snapdragon tầm thấp hơn tại Samsung Foundry.

**Tại sao chọn Samsung.** Chia nguồn bảo vệ Qualcomm khỏi tình trạng thiếu hụt năng lực TSMC và đòn bẩy giá. Mối quan hệ với Samsung cho Qualcomm vị thế đàm phán đáng tin cậy với TSMC. Đối với Samsung Foundry, mối quan hệ Qualcomm — dù ở khối lượng dưới flagship — là khách hàng tham chiếu quan trọng phát tín hiệu "các node của Samsung đạt chuẩn sản xuất thương mại."

**Ý nghĩa với Samsung.** Khối lượng Qualcomm tại Samsung Foundry không phải là công việc Snapdragon flagship gây chú ý; đó là công việc sản xuất ổn định lấp đầy năng lực tầm trung. Cần theo dõi xem Snapdragon 8 Gen 5 hoặc flagship tương lai có quay lại Samsung Foundry không — điều đó sẽ là tín hiệu tích cực lớn.

### 2.4 Google — Pixel Tensor SoC và Một Phần Công Việc TPU

**Tình trạng.** Pixel Tensor SoC của Google (G1, G2, G3, G4) được sản xuất tại Samsung Foundry, tận dụng IP thiết kế phái sinh Exynos của Samsung System LSI và sản xuất chuẩn 5nm/4nm. Một phần sản xuất TPU (các thế hệ cũ hơn, năng lực bổ sung) theo lịch sử dùng Samsung; các thế hệ TPU mới nhất chủ yếu ở TSMC.

**Tại sao chọn Samsung.** Dòng thiết kế Pixel Tensor xuất phát từ IP của Samsung System LSI khiến Samsung Foundry là đối tác sản xuất tự nhiên. Với công việc TPU, Samsung đóng vai trò bổ sung năng lực thay vì là đối tác chính.

**Ý nghĩa với Samsung.** Khối lượng Google Pixel không lớn theo nghĩa tuyệt đối trong ngành foundry, nhưng mối quan hệ này có tiếng tăm cao và tạo ra nhu cầu kéo cho node chuẩn 4nm của Samsung. Yếu tố biến động lớn hơn là liệu TPU thế hệ tiếp theo có bao giờ quay lại Samsung một cách có ý nghĩa không.

### 2.5 Ambarella — SoC Ô Tô ADAS

**Tình trạng.** Dòng CV3-AD của Ambarella — chip tăng tốc AI ô tô hàng đầu của công ty cho ADAS và ứng dụng lái xe tự động — được sản xuất trên node chuẩn 5nm của Samsung Foundry. Ambarella đã công bố công khai Samsung Foundry là đối tác 5nm của mình.

**Tại sao chọn Samsung.** Khách hàng ô tô coi trọng (a) tính liên tục cung cấp — cam kết của Samsung với sản xuất cấp ô tô dài hạn, (b) năng lực sản xuất — năng lực 5nm ô tô của TSMC đang bị đăng ký quá tải bởi Apple/AMD/NVIDIA, (c) chứng nhận hệ thống chất lượng cấp ô tô của Samsung.

**Ý nghĩa với Samsung.** Ambarella là khách hàng tham chiếu "5nm ô tô" rõ ràng nhất mà Samsung có. Khi ADAS / L2+ / L3 tự động hóa mở rộng trên toàn cầu, sức kéo khách hàng lên năng lực node tiên tiến cấp ô tô của Samsung ngày càng tăng.

### 2.6 Samsung System LSI — Mỏ Neo Khối Lượng Nội Bộ

**Tình trạng.** Bộ phận System LSI của chính Samsung — SoC di động Exynos, Exynos Auto cho ô tô, logic image sensor, IC modem — là khách hàng nội bộ lớn nhất của Samsung Foundry. Exynos 2400 (dòng Galaxy S24), Exynos Auto V920 (hợp tác Hyundai Pleos / Kia), và logic image sensor đều sử dụng các node tiên tiến của Samsung Foundry.

**Tại sao chọn Samsung.** Nội bộ — theo định nghĩa.

**Ý nghĩa với Samsung.** Đây là sàn đỡ. Dù tất cả khách hàng bên ngoài biến mất ngày mai, Samsung System LSI vẫn duy trì các fab node tiên tiến của Samsung Foundry hoạt động. Khối lượng công việc nội bộ cũng là nguồn phát triển IP, học hỏi cải thiện hiệu suất, và trưởng thành quy trình của Samsung Foundry. Cách đọc trung thực: các thắng lợi từ khách hàng bên ngoài quan trọng như **phần tăng trưởng thêm trên nền** khối lượng nội bộ.

### 2.7 Tầng Fabless Hàn Quốc và Châu Á

**Tình trạng.** Một đuôi dài các khách hàng fabless Hàn Quốc và châu Á dùng Samsung Foundry ở các node 4 / 5 / 8 / 12 / 14nm. Các khách hàng đã được xác nhận và thảo luận công khai bao gồm:

- **Rebellions** — startup chip tăng tốc AI Hàn Quốc (REBEL-Quad / chip tăng tốc thế hệ tiếp theo trên node tiên tiến Samsung).
- **FuriosaAI** — chip Renegade trên 5nm Samsung Foundry; thế hệ tiếp theo đang phát triển.
- **DeepX** — startup AI biên Hàn Quốc, Samsung Foundry.
- **OpenEdges Technology** — IP hệ thống con bộ nhớ Hàn Quốc (LPDDR6/5X PHY/Controller đã được silicon-proven trên Samsung SF5A; đang phát triển trên Samsung 4nm).
- **Nhiều fabless Nhật Bản** — khối lượng công việc ô tô, image sensor và AI.

**Tại sao chọn Samsung.** Gần về địa lý, hỗ trợ IR/kỹ thuật bằng tiếng Hàn, hệ sinh thái đối tác Samsung SAFE IP (Cadence, Synopsys, OpenEdges là đối tác Sub-License), và mức giá phù hợp với các khách hàng không ở cấp 1.

**Ý nghĩa với Samsung.** Tầng này ít hào nhoáng nhưng bền vững. Đây là tầng giúp việc sử dụng quy trình khối lượng lớn của Samsung Foundry ở các node 4 / 5 / 8nm khả thi. Đây cũng là tầng hưởng lợi trực tiếp nhất từ làn sóng startup AI ASIC xuất phát từ Hàn Quốc hoặc châu Á.

### 2.8 Nhóm "Từng Là Khách Hàng"

Để chính xác, một số tên lớn **không còn** là khách hàng chính của Samsung Foundry dù từng được báo chí chuyên ngành nhắc đến:

- **NVIDIA** — GPU Ampere A8000 / GA100 từng một phần dùng Samsung 8nm, nhưng thị trường nhanh chóng chuyển sang TSMC cho Hopper, Blackwell và Rubin. Hiện tại NVIDIA gần như hoàn toàn ở TSMC.
- **Apple** — Không còn là khách hàng Samsung Foundry có ý nghĩa cho silicon iPhone/Mac tiên tiến kể từ thời A9. Toàn bộ Apple silicon hiện tại là TSMC.
- **AMD** — CPU/GPU tiên tiến của AMD là TSMC; một số công việc AMD cũ dùng GlobalFoundries; Samsung không phải đối tác node tiên tiến hiện tại của AMD ở quy mô đáng kể.

Dịch chuyển khách hàng là thực tế. Cơ cấu Samsung Foundry năm 2026 khác biệt về cấu trúc so với năm 2020.

---

## 3. Cơ Cấu Khách Hàng Cho Bạn Biết Điều Gì

### 3.1 Nhận Dạng Mẫu Trong Cơ Cấu Khách Hàng

Đọc danh sách đã xác nhận năm 2026 như một bức tranh tổng thể, bốn mẫu nổi lên:

| Mẫu | Điều này cho thấy về Samsung Foundry |
| --- | --- |
| **Tỷ trọng chip tăng tốc AI cao (Tenstorrent, Tesla, Rebellions, FuriosaAI, Ambarella)** | Vị thế thách thức là có thật. Samsung là xưởng đúc "chip tăng tốc AI không đến TSMC." |
| **Tỷ trọng ô tô/ADAS mạnh (Tesla, Ambarella, Samsung Auto, Hyundai Pleos)** | Ô tô là lợi thế cấu trúc nơi cam kết dài hạn, năng lực và hệ thống chất lượng của Samsung vượt trội địa vị cấp 2 ô tô của TSMC. |
| **Samsung System LSI nội bộ là sàn đỡ** | Sàn sử dụng fab độc lập với thắng lợi khách hàng bên ngoài. |
| **Di động tầm trung (Qualcomm dưới flagship, Google Pixel, fabless Hàn Quốc/châu Á)** | Samsung cạnh tranh tốt ở "điểm ngọt khối lượng sản xuất" 4 / 5 / 8 / 12nm hơn là tại mặt trận tiên tiến nhất. |

### 3.2 Điều *Chưa* Có Trong Danh Sách (và Tại Sao Điều Đó Quan Trọng)

Cũng mang thông tin không kém: ai **không** có trong danh sách khách hàng Samsung Foundry tính đến 2026.

- **Không có nhà siêu máy tính AI mặt trận tiên tiến** — NVIDIA, AMD, Apple silicon, Microsoft Maia (TSMC), Meta MTIA (TSMC) đều ở TSMC. Nỗ lực chuẩn 2nm (SF2) của Samsung còn bất định về hiệu suất và khách hàng đến 2027.
- **Không có Snapdragon flagship nào trên SF3 / SF2 được ghi nhận.** Cho đến khi điều đó thay đổi, khoảng cách khối lượng flagship di động của Samsung vẫn còn đó.

Những vắng mặt này *không phải* thất bại. Đây là khoảng cách mà các node SF2 và SF1.4 của Samsung phải thu hẹp trong 2027–2028 để chuyển từ "cái tên số 2 đáng tin cậy" sang "ngang bằng thương mại với TSMC."

### 3.3 Cách Đọc Của Xưởng Đúc Thách Thức

Rút gọn thành một câu: **Samsung Foundry năm 2026 đang giành được những khách hàng cần năng lực, muốn tránh tập trung vào TSMC, hoặc coi trọng cam kết dài hạn cấp ô tô — và chưa giành được khối lượng chip tăng tốc AI siêu máy tính mặt trận tiên tiến.**

Đó chính xác là hồ sơ khách hàng của một cái tên số 2 đáng tin cậy trong thế độc quyền đôi, với tiềm năng thách thức bền vững trên các node tiếp theo.

---

## 4. Hàm Ý Cho Cổ Phiếu Samsung Electronics

Đây không phải bài khuyến nghị đầu tư, nhưng cơ cấu khách hàng có hàm ý trực tiếp đến cách đọc Samsung Electronics (KS: 005930):

1. **Samsung Foundry không phải dòng doanh thu mặt trận tiên tiến.** Tăng trưởng bộ nhớ AI tiên tiến của Samsung Electronics đến từ DS Memory (mở rộng khách hàng HBM4 sang NVIDIA, DRAM máy chủ AI), không phải từ thắng lợi khách hàng bên ngoài của Samsung Foundry. Nhầm lẫn hai cái này dẫn đến đọc sai.
2. **Thắng lợi khách hàng Samsung Foundry bền vững, không bùng nổ.** Tesla, Tenstorrent, Ambarella, Google Pixel và tầng fabless Hàn Quốc/châu Á tích lũy đều đặn. Chúng không tạo ra một quý duy nhất tái định giá cổ phiếu.
3. **Điểm uốn chuẩn 2nm (SF2) là biến động thực sự.** Liệu Samsung Foundry có giành được ít nhất một khách hàng AI lớn bên ngoài tại SF2 trong 2027–2028 hay không là kết quả nhị phân ảnh hưởng vật chất đến quỹ đạo doanh thu Samsung Foundry và toàn bộ hồ sơ biên lợi nhuận mảng foundry của Samsung.
4. **Tầng AI ASIC Hàn Quốc / châu Á trở nên có ý nghĩa khi nhiều khách hàng đồng thời mở rộng.** Một thắng lợi Rebellions hay FuriosaAI đơn lẻ còn nhỏ. Năm đến mười startup chip tăng tốc AI Hàn Quốc / châu Á đồng thời mở rộng trên năng lực 4 / 5nm của Samsung trở nên có ý nghĩa vật chất.

---

## 5. FAQ

**H: Samsung Foundry có phải là Samsung Electronics không?**
Đ: Samsung Foundry là bộ phận sản xuất chip theo hợp đồng của Samsung Electronics (KOSPI: 005930). Nó nằm trong bộ phận DS (Device Solutions) của Samsung cùng với Memory và System LSI. Đây không phải là pháp nhân niêm yết riêng biệt.

**H: Samsung Foundry có niêm yết đại chúng không?**
Đ: Không riêng biệt. Để có tỷ trọng, bạn mua Samsung Electronics (005930). Doanh thu và lợi nhuận hoạt động Samsung Foundry được báo cáo như một phần của mảng DS Foundry trong báo cáo tài chính hợp nhất Samsung Electronics.

**H: Samsung Foundry hiện sản xuất trên các node quy trình nào?**
Đ: Tính đến 2026, Samsung Foundry đang sản xuất trên các node chuẩn 14 / 8 / 7 / 5 / 4 / 3nm. Node GAA (gate-all-around) chuẩn 3nm đã trong sản xuất từ 2022, với quá trình cải thiện hiệu suất và tăng lượng khách hàng tiếp tục. Chuẩn 2nm (SF2) là mục tiêu node lớn tiếp theo.

**H: Khách hàng lớn nhất của Samsung Foundry là ai?**
Đ: Nội bộ — Samsung System LSI (Exynos, image sensor, modem) là khối lượng công việc nội bộ đơn lẻ lớn nhất. Trong số khách hàng bên ngoài, Tesla và Qualcomm theo lịch sử là những tên có khối lượng cao nhất; Tenstorrent và Google Pixel cũng đáng kể.

**H: Samsung Foundry có sản xuất chip NVIDIA không?**
Đ: Không ở thế hệ hiện tại 2026. Chip tăng tốc AI mặt trận tiên tiến của NVIDIA (Hopper, Blackwell, Rubin) ở TSMC. Samsung từng sản xuất GPU Ampere thế hệ cũ của NVIDIA ở 8nm, nhưng NVIDIA đã chuyển sang TSMC cho các thế hệ tiếp theo.

**H: Samsung Foundry có cạnh tranh với TSMC không?**
Đ: Có — Samsung được coi rộng rãi là cái tên thách thức số 2 của TSMC tại các node tiên tiến. TSMC giữ cơ sở khách hàng siêu máy tính AI mặt trận tiên tiến; Samsung cạnh tranh hiệu quả trong các mảng ô tô, startup chip tăng tốc AI, di động tầm trung và fabless Hàn Quốc/châu Á.

**H: Samsung Foundry có đang mất khách hàng vào tay TSMC không?**
Đ: Dịch chuyển khách hàng diễn ra hai chiều. Samsung mất khối lượng mặt trận tiên tiến Apple / NVIDIA / AMD đáng kể trong giai đoạn 2018–2024. Đổi lại, họ giành được Tesla liên tục nhiều thế hệ, Tenstorrent, Ambarella và cơ sở khách hàng fabless Hàn Quốc / châu Á đang tăng. Cơ cấu khách hàng năm 2026 khác biệt về cấu trúc so với 2020.

**H: Node SF2 là gì?**
Đ: SF2 là quy trình chuẩn 2nm của Samsung Foundry, trên lộ trình đã công bố của công ty cho đợt tăng sản xuất cuối 2025/2026. Liệu Samsung có giành được khách hàng bên ngoài lớn tại SF2 — đặc biệt là bất kỳ chip tăng tốc AI mặt trận tiên tiến nào — hay không là điểm uốn được theo dõi nhiều nhất 2026–2027 cho vị thế Samsung Foundry.

---

## 6. Khung Kết Luận

Điều duy nhất hữu ích nhất bạn có thể làm với câu hỏi "Ai dùng Samsung Foundry?" là **để câu trả lời thay đổi cách bạn nhìn nhận bản thân Samsung Foundry**. Đọc như một danh sách tên, cơ cấu khách hàng năm 2026 nói "Samsung Foundry là một xưởng đúc nghiêm túc với những khách hàng nghiêm túc." Đọc như một *mẫu* — chip tăng tốc AI + ô tô + fabless Hàn Quốc / châu Á + Samsung System LSI nội bộ — danh sách đó nói "Samsung Foundry là cái tên thách thức đáng tin cậy của TSMC, với cơ cấu khách hàng đúng với vị trí số 2 trong một thế độc quyền đôi."

Cả hai cách đọc đều đúng. Cái nào quan trọng hơn với quyết định của bạn phụ thuộc vào việc bạn đặt câu hỏi này cho mục đích mua sắm, phân bổ vốn cổ phần, hay để hiểu bản đồ bán dẫn toàn cầu. Với cả ba mục đích, câu trả lời hữu ích hơn nhiều so với những gì tiếng ồn truyền thông gợi ý.

---

## Phụ Lục — Phân Tầng Bằng Chứng

### [Thực tế]

- Samsung Foundry là bộ phận sản xuất chip theo hợp đồng của Samsung Electronics (KOSPI: 005930), nằm trong bộ phận DS (Device Solutions) cùng với Memory và System LSI.
- Tesla là khách hàng nhiều thế hệ của Samsung Foundry (HW3 ở 14nm, HW4 ở chuẩn 7nm, tiếp tục hợp tác trên các thế hệ tiếp theo).
- Chip tăng tốc Wormhole và Blackhole của Tenstorrent được sản xuất trên các node tiên tiến Samsung Foundry bao gồm SF4X.
- Qualcomm đã chia nguồn giữa Samsung Foundry và TSMC, với Snapdragon 8 Gen 1 được ghi nhận là sản xuất trên 4nm Samsung.
- Pixel Tensor SoC của Google (G1–G4) được sản xuất tại Samsung Foundry.
- Dòng ADAS CV3-AD của Ambarella ở node chuẩn 5nm của Samsung.
- Samsung System LSI (Exynos, logic image sensor, modem) là khối lượng công việc nội bộ tại Samsung Foundry.
- Các khách hàng fabless Hàn Quốc bao gồm Rebellions, FuriosaAI (Renegade), DeepX và OpenEdges Technology sử dụng các node 4 / 5 / 8 / 12nm của Samsung Foundry.
- Các thế hệ Hopper / Blackwell / Rubin của NVIDIA ở TSMC, không phải Samsung.
- Apple silicon ở TSMC, không phải Samsung, kể từ thời A9.

### [Suy luận]

- Mối quan hệ Tesla qua HW5 là tín hiệu tính liên tục khách hàng bên ngoài được theo dõi nhiều nhất của Samsung Foundry.
- Quan hệ đối tác Tenstorrent đại diện cho sự chứng thực chip tăng tốc AI ngoài NVIDIA rõ ràng nhất của Samsung Foundry.
- Tập trung cơ cấu khách hàng vào chip tăng tốc AI, ô tô và fabless Hàn Quốc/châu Á phản ánh vị thế thách thức của Samsung — năng lực sản xuất, giá trị chia nguồn và linh hoạt giá — thay vì ngang bằng hiệu suất mặt trận tiên tiến với TSMC.
- Danh sách khách hàng bên ngoài của node SF2 (2nm) sẽ là đầu vào lớn nhất duy nhất vào cách Samsung Foundry được định vị lại trong thế độc quyền đôi foundry toàn cầu qua 2027–2028.

### [Suy đoán]

- Snapdragon flagship quay lại Samsung Foundry tại SF3 hoặc SF2 sẽ là tín hiệu tái định giá tích cực lớn cho mảng foundry của Samsung.
- Cam kết Tesla tiếp tục qua HW5 và xa hơn sẽ neo giữ doanh thu node tiên tiến cấp ô tô của Samsung ở quy mô có ý nghĩa qua 2028.
- Thắng lợi Samsung Foundry trên ít nhất một chip tăng tốc siêu máy tính AI bên ngoài tại SF2 sẽ dịch chuyển đáng kể khung "số 2 đáng tin cậy" hiện tại sang "cạnh tranh thương mại ở mặt trận tiên tiến."

### [Chưa xác định]

- Đóng góp khối lượng wafer từng khách hàng vào doanh thu DS Foundry hàng quý của Samsung Foundry.
- Đường cong hiệu suất và tốc độ học hỏi từng node của Samsung Foundry.
- Điều khoản giá cấp 1 bí mật có thể so sánh trực tiếp TSMC và Samsung Foundry tại cùng một node.
- Danh sách đầy đủ khách hàng bên ngoài cho các design start SF2 của Samsung Foundry.

---

**Tuyên bố miễn trừ trách nhiệm**: Bài viết này là bình luận nghiên cứu, không phải tư vấn đầu tư. Mô tả cơ cấu khách hàng dựa trên tham chiếu khách hàng được công bố công khai, bình luận trong buổi báo cáo kết quả và thông tin chuỗi cung ứng từ báo chí chuyên ngành; phân bổ khối lượng wafer cụ thể không được công bố công khai. Danh sách khách hàng Samsung Foundry thay đổi liên tục. Các mã cổ phiếu được nêu chỉ mang tính minh họa cho khung phân tích, không phải khuyến nghị. Hãy tự thực hiện thẩm định và tham khảo cố vấn được cấp phép trước bất kỳ quyết định đầu tư nào.

*Disclaimer: For research and information purposes only. Not investment advice. Names cited are for analytical illustration; readers should perform their own due diligence and consult licensed advisors before any investment decision.*
