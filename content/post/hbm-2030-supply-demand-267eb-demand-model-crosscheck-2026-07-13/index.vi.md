---
title: "Nghiên cứu chuyên sâu cung-cầu HBM 2030: mổ xẻ mô hình cầu 26,7EB đối chiếu với lịch trình mở rộng công suất"
slug: "hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13"
date: 2026-07-13T11:00:00+09:00
description: "Chúng tôi tái hiện độc lập luận điểm cầu HBM 2030 là 26,7EB so với cung 10,6EB (thiếu hụt 2,5 lần) từ công thức công khai, rồi đối chiếu với dự báo token 24 lần của Goldman, phản chứng hiệu suất DeepSeek MLA và TurboQuant, và lịch trình công suất của Big 3. Phân tích cấu trúc, không phải khuyến nghị đầu tư."
categories: ["Exclusive Analysis", "Tech-Analysis", "Market-Outlook"]
tags: ["HBM", "Cung-cầu bộ nhớ", "AI Memory", "SK Hynix", "Samsung Electronics", "Micron", "KV Cache", "Hạ tầng AI", "Công suất bán dẫn"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Bối cảnh
> Nếu bài [So sánh công nghệ bộ nhớ HBM, HBF, HBC](/vi/post/hbm-hbf-hbc-ai-memory-comparison-2026-06-22/) đã bàn về bản chất công nghệ, thì bài này đào sâu vào <strong>cung và cầu gặp nhau như thế nào cho đến năm 2030</strong>. Nên đọc cùng với [Giá trị token AI và giá trị gia tăng của bộ nhớ](/vi/post/ai-token-value-memory-value-added-2026-07-09/), [Earnings call Big Tech cuối tháng 7 và luận điểm bộ nhớ](/vi/post/big-tech-july-earnings-call-memory-thesis-scenarios-2026-07-07/), [Ai trả tiền cho đồng thuận bán dẫn 2027](/vi/post/semiconductor-2027-earnings-hyperscaler-payability-memory-nvidia-2026-06-21/). Các hub liên quan là [Hub HBM AI](/vi/page/korea-semiconductor-hbm-kospi-hub/) và [Hub Phân tích độc quyền](/vi/page/exclusive-analysis-hub/).

## TL;DR

* Chúng tôi tái hiện độc lập bằng công thức công khai câu chuyện đang lan truyền trên thị trường: <strong>cầu HBM năm 2030 là 26,7EB, cung 10,6EB, thiếu hụt 2,5 lần</strong>. Phép tính tự nó tái hiện được. Vấn đề nằm ở việc con số đó đứng trên những giả định nào.
* 26,7EB không phải là lỗi so sánh nhầm giữa tồn kho và lưu lượng. Cả cầu lẫn cung đều được quy đổi và so sánh dưới dạng <strong>tồn kho HBM đang lắp đặt và vận hành (stock)</strong>. Tuy nhiên con số này chỉ đúng khi nhiều giả định tăng giá đồng thời xảy ra: token tăng 24 lần, footprint mô hình tăng 5 lần, ngữ cảnh (context) tăng 4 lần, tỷ lệ KV tồn lưu 70%.
* Chúng tôi đối chiếu qua ba lăng kính: (1) cấu trúc mô hình cầu, (2) căn cứ tăng giá của các giả định cầu và phản chứng hiệu suất công nghệ, (3) lịch trình mở rộng công suất của Big 3. Ba lăng kính hội tụ về <strong>một kết luận, không mâu thuẫn</strong>.
* Kết luận <strong>tách bạch hướng đi và độ lớn</strong>. `Tình trạng thắt chặt đến năm 2027` có độ tin cậy cao, `cung được cải thiện từ năm 2028` phù hợp với lịch trình mở rộng công suất chính thức, còn `thiếu hụt đúng 2,5 lần vào năm 2030` là kịch bản thiên về tăng giá.
* Bài viết này không đưa ra phán đoán mua hay nắm giữ đối với bất kỳ cổ phiếu cụ thể nào. Đây là phân tích mổ xẻ cấu trúc cung-cầu ngành. \[Phạm vi phân tích\]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Luận điểm chính</div>
  <div class="thesis-callout__body">
    Vấn đề thực sự của cung-cầu HBM không phải là "liệu năm 2030 có thiếu hụt 2,5 lần hay không", mà là "hướng thiếu hụt vững chắc, nhưng độ lớn nhạy cảm với giả định". Dữ liệu ủng hộ tình trạng thắt chặt năm 2027 và cải thiện cung năm 2028, còn con số 2,5 lần là kịch bản thiên về tăng giá, chỉ đúng khi nhiều giả định cầu cùng lúc khớp nhau.
  </div>
</div>

---

## 1. Xác định vấn đề: chúng ta đang kiểm chứng điều gì

Trên thị trường bộ nhớ AI đang lan truyền một câu chuyện mạnh mẽ. Cầu HBM năm 2030 là 26,7EB (exabyte), trong khi cung chỉ đạt 10,6EB, để lại <strong>khoảng thiếu hụt cấu trúc gấp 2,5 lần</strong>. Con số này xuất phát từ một mô hình phân tích độc lập (Memory Analyst) và lan rộng qua nhiều video YouTube và báo cáo.

Bài nghiên cứu chuyên sâu này trả lời bốn câu hỏi. \[Câu hỏi kiểm chứng\]

1. Công thức `26,7EB so với 10,6EB` có nhất quán về mặt nội tại không?
2. Các giả định về cầu có hợp lý dựa trên căn cứ công khai và cấu trúc mô hình không?
3. Nếu tính cả kế hoạch mở rộng công suất của Samsung Electronics, SK Hynix, Micron thì thiếu hụt năm 2030 còn tồn tại không?
4. Thị trường thực sự thanh khoản hóa con số này như thế nào?

Trước tiên, để không làm mờ kết luận, chúng tôi khẳng định rõ một điều. Bài viết này không định giá lại giá cổ phiếu hiện tại hay bội số hợp lý. Chỉ bàn về <strong>độ tin cậy của hướng đi và độ lớn của cung-cầu</strong>.

---

## 2. Lăng kính thứ nhất: mổ xẻ mô hình cầu 26,7EB

### 2.1 Đây là so sánh tồn kho với tồn kho (loại bỏ một hiểu lầm phổ biến)

Hiểu lầm đầu tiên cần loại bỏ là nhận định "cầu 26,7EB và cung 10,6EB là so sánh nhầm giữa tiêu thụ hàng năm và sản xuất hàng năm". Kết quả kiểm chứng cho thấy <strong>đây không phải là lỗi.</strong> Mô hình gốc so sánh hai loại tồn kho. \[Thực tế\]

- <strong>Need (nhu cầu)</strong>: tồn kho HBM cần được lắp đặt và bật hoạt động để xử lý khối lượng công việc suy luận AI trong năm đó
- <strong>Serving fleet (đội phục vụ)</strong>: tồn kho trong số HBM được sản xuất trong khoảng 5 năm gần nhất, được đưa vào suy luận, sau khi phản ánh hiệu suất lão hóa và vẫn chưa ngừng hoạt động

Tức là cả hai con số đều là tồn kho (stock), không phải lưu lượng (flow). Cấu trúc `fleet = sản lượng khoảng 5 năm gần nhất × tỷ trọng suy luận - ma sát` của mô hình gốc thể hiện rõ phép chuyển đổi này. Xét trên chiều stock-flow thì nhất quán. \[Suy luận\] Tuy nhiên tỷ lệ phân bổ suy luận, tuổi thọ 5 năm, hiệu suất theo từng thế hệ dùng để chuyển lưu lượng thành tồn kho không phải là chuẩn ngành được kiểm chứng độc lập, mà là <strong>giả định của mô hình</strong>.

### 2.2 Tái hiện nguyên vẹn công thức cầu 26,7EB

Chúng tôi đưa nguyên công thức đơn giản mà mô hình gốc công bố cùng các giá trị đầu vào base-case năm 2030 vào để tái hiện độc lập.

```text
traffic = 24  (2026 대비 24배, 월간 토큰 120 quadrillion)
replicaIndex = 24^0.90 / 11 = 1.5878

weights = 1.75 × 1.5878 × 5 / 1.75 = 7.939EB
contextBucket = 4 × 1.5 / 4 × 0.70 = 1.05
kv = 1.27 × 24^0.55 × 1.05 = 7.658EB
scratch = (7.939 + 7.658) × 0.15 = 2.340EB

need = (7.939 + 7.658 + 2.340) × 1.10 / 0.74 = 26.66EB ≈ 26.7EB
```

Nếu tách cầu theo từng thành phần, ta có bảng sau.

| Cấu thành cầu 2030 | EB | Tỷ trọng |
|---|---:|---:|
| Resident weights (trọng số thường trú) | 7,94 | 44,3% |
| KV cache | 7,66 | 42,7% |
| Scratch (bộ nhớ tác vụ tạm thời) | 2,34 | 13,0% |
| Tổng phụ (trước khi phản ánh redundancy, utilization) | 17,94 | 100,0% |
| Lượng lắp đặt cuối cùng cần thiết (×1,10 / 0,74) | 26,66 | - |

\[Thực tế\] Phép tính 26,7EB tái hiện được bằng công thức công khai. Điều quan trọng là trọng số thường trú và KV cache lần lượt chiếm 44% và 43%, tức phần lớn tổng cầu. Chính hai hạng mục này là mục tiêu trực tiếp của các cải thiện hiệu suất công nghệ sẽ được trình bày ở phần sau.

\[Chưa xác minh\] Tuy nhiên trong công cụ tính toán còn có một giá trị đầu vào riêng là `frontier/HBM-served share 70%`, nhưng công thức đơn giản được công bố không cho thấy rõ giá trị này được phản ánh vào trọng số như thế nào. Cho đến khi có audit ở cấp độ code, chúng tôi chưa công nhận 26,7EB là một mô hình độc lập hoàn chỉnh.

### 2.3 Đọc đúng tốc độ tăng trưởng

`CAGR 5 năm` thường được trích dẫn trước đây là một lỗi tính kỳ hạn. Từ 2026 đến 2030 có 5 điểm quan sát, nhưng <strong>số kỳ lãi kép chỉ là 4</strong>.

| Hạng mục | 2026 | 2030 | Bội số | CAGR 4 kỳ chính xác |
|---|---:|---:|---:|---:|
| Lượng HBM cần lắp đặt | 4,8EB | 26,7EB | 5,56 lần | <strong>53,6%</strong> |
| Serving fleet | 3,75EB | 10,6EB | 2,83 lần | <strong>29,7%</strong> |

Ngoài ra, lộ trình sản lượng HBM hàng năm của mô hình gốc, từ `2,8EB năm 2024 lên 7,6EB năm 2030`, có CAGR 6 kỳ là <strong>18,1%</strong>. `Serving fleet 10,6EB` không phải sản lượng hàng năm mà là tồn kho tích lũy và khấu hao từ sản lượng của nhiều năm, nên không được nhầm lẫn hai khái niệm này với nhau. \[Thực tế\]

Nếu cầu tăng 53,6%/năm còn tồn kho cung tăng 29,7%/năm, thì bản thân hướng nới rộng khoảng cách là hiển nhiên về mặt số học. Vấn đề là các giả định đầu vào của hai tốc độ tăng trưởng này vững chắc đến đâu.

---

## 3. Lăng kính thứ hai: mặt tăng giá và phản chứng của các giả định cầu

### 3.1 Căn cứ tăng giá đã xác nhận của cầu

Căn cứ cho việc cầu mạnh là có thật. \[Thực tế\]

- Goldman Sachs Research dự báo mức tiêu thụ token hàng tháng giai đoạn 2026-2030 sẽ tăng <strong>24 lần</strong>, đạt 120 quadrillion.
- Cùng tài liệu này dự báo số lượt truy vấn LLM hàng ngày sẽ tăng trưởng bình quân khoảng 40%/năm, đạt 11 tỷ lượt vào năm 2030.
- Dung lượng HBM trên mỗi accelerator đã liên tục tăng qua từng thế hệ NVIDIA.
- Micron đưa ra hướng dẫn rằng tính đến tháng 6/2026, cầu DRAM và NAND vượt xa cung, và tình trạng thắt chặt này sẽ <strong>kéo dài đến sau năm 2027</strong>.
- Micron cho biết đã ký 16 hợp đồng khách hàng chiến lược (SCA), trong đó doanh thu tích lũy tính theo giá sàn của 14 hợp đồng đạt khoảng 100 tỷ USD, cùng các cam kết đặt cọc tiền mặt và tài trợ liên quan trị giá 22 tỷ USD. Tuy nhiên HBM chỉ là một phần của các hợp đồng này, không phải toàn bộ đều là hợp đồng HBM.

### 3.2 Căn cứ đối lập tồn tại ngay trong cùng một nguồn

Điều thú vị là ngay trong chính tài liệu của Goldman, vốn được dùng làm căn cứ tăng giá, cũng tồn tại căn cứ đối lập. \[Thực tế\]

- Goldman dự báo tình trạng thiếu chip trong ngắn hạn, nhưng đồng thời khẳng định rằng <strong>khi năng lực sản xuất mới đi vào hoạt động, toàn ngành có thể bắt kịp trong khoảng 2 năm</strong>.
- Goldman giải thích rằng chi phí trên mỗi token suy luận giảm 60-70%/năm. Giá giảm làm tăng lượng sử dụng, nhưng đồng thời cũng giảm gánh nặng bộ nhớ vật lý của cùng một khối lượng công việc.
- Điểm mấu chốt là mức tăng 24 lần của Goldman không phải là dự báo cầu bit HBM, mà là dự báo <strong>lưu lượng token</strong>. Việc chuyển đổi `từ token sang phiên đồng thời, ngữ cảnh, KV và trọng số, tồn lưu HBM` hoàn toàn là các giả định mô hình riêng biệt.

\[Suy luận\] Do đó dự báo của Goldman ủng hộ việc sử dụng AI tăng lên, nhưng không trực tiếp ủng hộ `thiếu hụt HBM 2,5 lần vào năm 2030`. Sự phân biệt này thường bị bỏ qua khi câu chuyện tăng giá trích dẫn Goldman.

### 3.3 Phản chứng cấu trúc mô hình và hiệu suất

Trọng số và KV cache, hai yếu tố cốt lõi của công thức cầu, chính là mục tiêu trực tiếp của cải thiện công nghệ. \[Thực tế\]

- Ví dụ KV cache <strong>khoảng 504KB/token</strong> của mô hình gốc là trường hợp của <strong>Llama 3.1 405B</strong>. Đây không phải giá trị phổ quát cho mọi frontier model.
- Dòng DeepSeek-V3/R1 nâng cao đáng kể hiệu suất KV và tính toán nhờ Multi-head Latent Attention (MLA) và Mixture-of-Experts (MoE).
- TurboQuant của Google Research đưa ra kết quả giảm bộ nhớ KV <strong>tối thiểu 6 lần</strong> trên các benchmark công khai.

\[Suy luận\] Tuy nhiên TurboQuant là kết quả nghiên cứu áp dụng cho KV cache. Nó không giảm 6 lần cả trọng số, scratch, redundancy, và cũng chưa phải mức trung bình ngành đã được kiểm chứng về độ trễ, thông lượng, chất lượng trong môi trường sản xuất quy mô lớn.

Vì vậy kết luận trung thực là loại trừ cả hai thái cực. `504KB/token × toàn bộ khối lượng công việc tương lai` là ước tính quá cao, còn `nén KV 6 lần × toàn bộ HBM` là ước tính quá thấp. Cầu tương lai nằm giữa hai thái cực đó, và điều cốt yếu là <strong>cấu trúc trọng số và KV sẽ thay đổi ra sao</strong>.

---

## 4. Lăng kính thứ ba: đối chiếu chéo lịch trình mở rộng công suất của Big 3

### 4.1 Công suất fab và nguồn cung HBM hiệu dụng là hai khái niệm khác nhau

Sai lầm phổ biến khi xem xét nguồn cung là quy đổi ngay tin tức khởi công hoặc hoàn công fab thành HBM có thể bán được. Giữa hai khái niệm này có năm khoảng cách. \[Thực tế/Suy luận\]

1. <strong>Die intensity tăng</strong>: khi số die trên mỗi stack tăng từ 12 lớp lên 16 lớp, số die cần thiết cho cùng một số lượng stack tăng khoảng 33%. Dù wafer tăng, tốc độ tăng số stack có thể bán vẫn có thể thấp hơn mức đó.
2. <strong>HBM trade ratio</strong>: HBM tiêu tốn nhiều wafer và tài nguyên công nghệ hơn DRAM thông thường. Micron cũng khẳng định rằng tỷ lệ này tăng lên qua từng thế hệ, gây áp lực lên nguồn cung non-HBM.
3. <strong>Công đoạn sau, hiệu suất, chứng nhận</strong>: phải vượt qua toàn bộ good die, xếp chồng TSV, base die, advanced packaging, thông số nhiệt và điện, chứng nhận khách hàng thì mới trở thành nguồn cung hiệu dụng.
4. <strong>Độ trễ ramp</strong>: việc mở cleanroom hay first wafer khác với qualified volume có thể ghi nhận doanh thu.
5. <strong>Chi phí cơ hội giữa các sản phẩm</strong>: tăng sản lượng HBM có thể lấn chiếm wafer DRAM thông thường. Dù HBM tăng, không có gì đảm bảo giá DRAM toàn thể sẽ ổn định ngay lập tức.

### 4.2 Lịch trình mở rộng công suất chính thức

Đây là lịch trình của Big 3 và toàn ngành được xác nhận qua các tài liệu sơ cấp công khai.

| Doanh nghiệp / hạng mục | Nội dung xác nhận chính thức | Diễn giải đóng góp cung thực tế |
|---|---|---|
| SK Hynix M15X | Mục tiêu hoàn công tháng 11/2025, sản xuất DRAM và HBM thế hệ mới | Trục mở rộng công suất nhanh nhất giai đoạn 2026-27. Có thể ramp nhanh nhờ tận dụng hạ tầng hiện có |
| SK Hynix Yongin giai đoạn 1 | Đầu tư thiết bị 21,6 nghìn tỷ won, kế hoạch mở cleanroom đầu tiên sớm vào tháng 2/2027 | Bắt đầu lắp đặt năm 2027, khả năng mở rộng hiệu ứng cung từ năm 2028 trở đi |
| SK Hynix Yongin toàn bộ | Mục tiêu cleanroom đầu tiên của fab thứ 4 là năm 2033 | Giả định toàn bộ 4 fab Yongin đi vào cung ứng năm 2030 là sai |
| Samsung Electronics HBM4 | Bắt đầu sản xuất hàng loạt và xuất xưởng thương mại tháng 2/2026, dự kiến doanh thu HBM năm 2026 tăng hơn 3 lần | Việc Samsung quay lại vai trò second-source giai đoạn 2026-27 là biến số nới lỏng cung lớn nhất |
| Đầu tư dài hạn Samsung Electronics | Khoảng 2.100 nghìn tỷ won cho bán dẫn giai đoạn 2026-2040, khoảng 1.650 nghìn tỷ won cho Yongin và các khu hiện có, fab HBM tại Onyang, Cheonan | Định hướng mạnh nhưng là envelope đến năm 2040. Không thể quy đổi trực tiếp thành sản lượng cung năm 2030 |
| Micron ID1 | First wafer giữa năm 2027 | Xét đến chứng nhận khách hàng, doanh số có ý nghĩa rơi vào cuối 2027 đến 2028 |
| Micron ID2 | First wafer cuối năm 2028 | Đóng góp nới lỏng cung từ năm 2029 trở đi |
| Micron Tongluo và packaging | Tongluo có sản lượng xuất xưởng có ý nghĩa trong FY2028, mở rộng packaging HBM từ nửa đầu năm 2027 | Nới lỏng đồng thời nút thắt front-end và công đoạn sau |
| SEMI toàn ngành bộ nhớ | Công suất bộ nhớ 300mm dự báo từ 4,1 triệu WPM năm 2026 lên 4,2 triệu WPM năm 2027 | Mức tăng tổng công suất wafer chỉ khoảng 2,4%, khá chậm. Chuyển dịch mix HBM và tăng trưởng bit theo node quan trọng hơn |

### 4.3 Phán định về phía cung

- \[Thực tế\] Cả Big 3 đều đang tiến hành đầu tư quy mô lớn.
- \[Thực tế\] Năm 2027 là năm cleanroom và first wafer bắt đầu tăng lên, chứ không phải năm toàn bộ sản lượng chuyển thành qualified output.
- \[Suy luận\] Khả năng cao là nới lỏng cung sẽ hiện rõ từ năm 2028 và mạnh hơn trong giai đoạn 2029-30.
- \[Chưa xác minh\] Chỉ dựa vào tài liệu công khai thì không thể xác định serving fleet năm 2030 là 10,6EB hay 15EB. WPM chính xác, mix sản phẩm, hiệu suất, công suất packaging đều chưa được công bố.

---

## 5. Phân tích độ nhạy tổng hợp từ ba lăng kính

Chúng tôi tổng hợp hướng đi mà ba lăng kính chỉ ra vào một bảng độ nhạy duy nhất. Serving fleet phía cung được cố định ở mức 10,6EB, chỉ giả định cầu được tính toán lại độc lập bằng công thức công khai.

| Kịch bản | Giả định thay đổi | Cầu 2030 | Cầu/Cung | Phán định |
|---|---|---:|---:|---|
| Base mô hình gốc | Token 24 lần, mô hình 5 lần, hiệu suất KV 4 lần, tỷ lệ tồn lưu 70% | 26,7EB | 2,52 lần | Thiếu hụt mạnh |
| Giảm footprint mô hình | Hệ số mô hình từ 5 lần xuống 2 lần | 18,5EB | 1,75 lần | Thiếu hụt |
| Cải thiện hiệu suất KV | Hiệu suất KV từ 4 lần lên 6 lần | 22,3EB | 2,10 lần | Thiếu hụt |
| Giảm tỷ lệ tồn lưu HBM | Từ 70% xuống 50% | 22,9EB | 2,16 lần | Thiếu hụt |
| Tăng trưởng token giảm một nửa | Từ 24 lần xuống 12 lần | 16,2EB | 1,53 lần | Thiếu hụt |
| Bear tổng hợp | Token 12 lần, mô hình 2 lần, hiệu suất KV 6 lần, tỷ lệ tồn lưu 50%, throughput 14 lần | 6,5EB | 0,62 lần | Dư cung |
| Bull tổng hợp | Token 36 lần, mô hình 8 lần, hiệu suất KV 3 lần, tỷ lệ tồn lưu 80%, throughput 8 lần | 67,9EB | 6,41 lần | Thiếu hụt cực đoan |

Bear và bull tổng hợp không phải kịch bản chính thức của mô hình gốc, mà là stress test độc lập để xem xét hiệp phương sai (covariance) giữa các giả định.

Cách diễn giải bảng này chính là trái tim của bài nghiên cứu chuyên sâu này.

<strong>Thứ nhất, chỉ thay đổi một biến số duy nhất thì thiếu hụt không dễ dàng biến mất.</strong> Dù hạ hệ số mô hình từ 5 lần xuống 2 lần, hay giảm một nửa tăng trưởng token, thiếu hụt (1,5-1,75 lần) vẫn còn tồn tại. Đây là căn cứ để câu chuyện tăng giá nói rằng "lay chuyển giả định nào cũng vẫn thiếu hụt".

<strong>Thứ hai, nhưng các biến số không độc lập với nhau.</strong> Tăng trưởng token chậm lại, mô hình nhỏ hơn và MoE mở rộng, nén KV, offload HBM, cải thiện throughput đều <strong>di chuyển đồng thời khi hiệu suất công nghệ được cải thiện</strong>. Đây là lý do trong kịch bản bear tổng hợp, cầu giảm xuống 6,5EB và đảo ngược thành dư cung.

<strong>Thứ ba, do đó dù mang nhãn base-case, 2,5 lần trên thực tế cần được coi là kịch bản thiên về tăng giá.</strong> One-way sensitivity, tức chỉ đẩy một biến số đến cùng, không thể chứng minh độ vững chắc của con số 2,5 lần. Rủi ro thực sự nằm ở hiệp phương sai, tức việc các giả định cùng sụp đổ với nhau.

---

## 6. Góc nhìn thanh khoản thị trường: nên đọc con số 2,5 lần như thế nào

Không nên đọc `cầu 26,7EB, cung 10,6EB` theo nghĩa đen là 16,1EB đơn hàng không được đáp ứng. Thị trường thực tế thanh khoản hóa theo trình tự sau.

```text
잠재 AI 워크로드 증가
→ qualified HBM 병목
→ 가격 상승·장기계약·선급금
→ 고객별 allocation과 낮은 ROI 워크로드 지연
→ SLM·MoE·양자화·KV 재사용·offload 확대
→ 추가 capex와 second-source 인증
→ 실현 출하량과 청산 수요가 수렴
```

\[Suy luận\] Nói cách khác, nên hiểu chính xác rằng 2,5 lần không phải là dự báo chính xác về mức thiếu hụt sản lượng sẽ hiện thực hóa, mà là kịch bản thể hiện <strong>cường độ của quyền định giá và áp lực phân phối</strong>. Thiếu hụt lớn không có nghĩa là "16EB sẽ mãi mãi không được lấp đầy", mà có nghĩa là "khoảng cách đó chịu áp lực thanh khoản mạnh thông qua giá cả, hợp đồng, thay thế công nghệ".

Từ góc nhìn này, điểm cần quan sát thực sự trong phân tích cung-cầu không phải là bản thân con số EB, mà là những điều sau. \[Điểm theo dõi\]

1. Giá sàn (price floor) của các hợp đồng nhiều năm có được duy trì không
2. Premium ASP của HBM4/4E có được duy trì đủ lâu không
3. Việc tăng tỷ trọng HBM có khiến nguồn cung DRAM thông thường cũng trở nên thắt chặt không
4. Cải thiện hiệu suất và advanced packaging có giúp biên lợi nhuận của doanh thu gia tăng thuộc về bên cung hay không
5. Lợi nhuận và dòng tiền tích lũy được bao nhiêu trước khi nguồn cung mới năm 2028 đưa giá về bình thường

---

## 7. Triển vọng theo trục thời gian: Base / Bull / Bear

Khi đặt ba lăng kính và phân tích độ nhạy lên trục thời gian, kết quả được sắp xếp như sau.

| Giai đoạn | Base | Bull | Bear |
|---|---|---|---|
| 2026-2027 | Ramp HBM4 và cầu AI nhanh hơn nguồn cung greenfield mới. Thắt chặt tiếp diễn | Chứng nhận Samsung trễ, nút thắt packaging kéo dài, cầu token và ASIC vượt dự báo | Nguồn cung HBM4 lớn của Samsung và phân tán mix khách hàng nhanh hơn dự kiến |
| 2028 | SK Yongin giai đoạn 1, hiệu ứng Micron ID1, Tongluo, packaging bắt đầu. Mức thiếu hụt được nới lỏng | Hiệu ứng cung bị hạn chế do hiệu suất và chứng nhận ban đầu trễ | Công suất mới ổn định nhanh, hiệu suất KV và routing cải thiện đồng thời |
| 2029-2030 | Dù còn thiếu hụt, khả năng được nới lỏng cao hơn mở rộng. Quyền định giá kéo dài lâu hơn các chu kỳ trước | Footprint mô hình và tính đồng thời của agent lấn át cải thiện hiệu suất, hợp đồng dài hạn và premium khan hiếm tiếp diễn | Micron ID2, Samsung, SK ramp mở rộng đồng thời, hiệu suất và offload chồng lấn khiến premium HBM trở về bình thường |

### Phán định cuối cùng theo trục thời gian

- `Thắt chặt đến năm 2027`: <strong>xác suất cao</strong>
- `Cung cải thiện từ năm 2028`: <strong>xác suất trung bình khá</strong>
- `Thiếu hụt được nới lỏng giai đoạn 2029-30`: <strong>xác suất trung bình</strong>
- `Khoảng cách 2,5 lần mở rộng cả năm 2030`: <strong>xác suất thấp / kịch bản thiên về tăng giá</strong>

---

## 8. Cần theo dõi điều gì: các trigger đánh giá lại

Nếu xác định trước các tín hiệu để phân biệt câu chuyện cung-cầu đang mạnh lên hay yếu đi, sẽ không bị cuốn theo tin tức.

<strong>Tín hiệu cho thấy luận điểm tăng giá cung-cầu đang mạnh lên</strong>

1. Bên cung xác nhận chính thức tình trạng sold-out hoặc hợp đồng dài hạn, giá sàn ngay cả sau năm 2028
2. Hiệu suất HBM4/4E và công suất packaging cải thiện trong khi vẫn duy trì premium ASP và biên lợi nhuận
3. Dù Samsung và Micron mở rộng công suất, hướng dẫn về tình trạng thắt chặt ngành vẫn kéo dài sau năm 2028
4. Token thực tế, ngữ cảnh thường trú, tính đồng thời của khối lượng công việc agentic tiệm cận lộ trình tăng 24 lần

<strong>Tín hiệu cho thấy luận điểm tăng giá cung-cầu đang yếu đi</strong>

1. Việc giảm tổng hợp từ 6 lần trở lên đối với bộ nhớ KV và trọng số trở nên phổ biến trong môi trường sản xuất
2. Phần lớn suy luận gia tăng chuyển sang cấu trúc SLM, ASIC, offload nhẹ về bộ nhớ (memory-light)
3. Công suất mới của Samsung HBM4E và Micron được chứng nhận đại trà nhanh hơn dự kiến
4. Bên cung rút lại hướng dẫn `thắt chặt sau năm 2027` và giá sàn hợp đồng khách hàng suy yếu
5. Premium ASP HBM, giá hợp đồng, biên lợi nhuận DRAM giảm mang tính cấu trúc cùng với việc tăng cung

---

## Kết luận: hướng đi vững chắc, độ lớn cần khiêm tốn

Kết luận một dòng của bài nghiên cứu chuyên sâu này là như sau. <strong>`HBM thắt chặt đến năm 2027, cung cải thiện từ năm 2028` được dữ liệu và lịch trình chính thức ủng hộ, nhưng `thiếu hụt 2,5 lần vào năm 2030` là kịch bản thiên về tăng giá, chỉ đúng khi nhiều giả định cầu cùng lúc khớp nhau.</strong>

Con số 26,7EB được tái hiện một cách tinh vi, nhưng sự tinh vi đó không đồng nghĩa với chắc chắn. Đây là giá trị chỉ đúng khi token tăng 24 lần, mô hình tăng 5 lần, ngữ cảnh tăng 4 lần, tỷ lệ tồn lưu KV 70% <strong>đồng thời</strong> xảy ra, và khi hiệu suất công nghệ được cải thiện, các giả định này sẽ cùng sụp đổ. Ngược lại, nguồn cung chuyển thành qualified output chậm hơn nhiều so với tin tức về fab. Điểm mà hai lực này gặp nhau chính là bước ngoặt năm 2028.

Khung nhìn hữu ích khi xem xét cung-cầu không phải là tin vào một con số duy nhất, mà là <strong>tách bạch độ tin cậy của hướng đi và sự bất định của độ lớn</strong>. Hướng đi vững chắc. Độ lớn cần khiêm tốn.

---

_Bài viết này là tài liệu phân tích cấu trúc cung-cầu được tái hiện độc lập và đối chiếu chéo, tổng hợp từ các tài liệu sơ cấp công khai (Goldman Sachs, SK Hynix, Samsung Electronics, Micron, SEMI, Google Research, báo cáo kỹ thuật DeepSeek) và mô hình thứ cấp (Memory Analyst). Các cổ phiếu được đề cập chỉ là ví dụ minh họa cấu trúc ngành, không phải khuyến nghị đầu tư. Phần lớn các con số như 26,7EB, 10,6EB, 2,5 lần là giả định và kịch bản của mô hình, không phải dự báo chính thức của công ty. Đây là lĩnh vực thay đổi nhanh, nên khuyến nghị cập nhật và xác nhận bằng tài liệu sơ cấp mới nhất._

---

### Bài viết liên quan

- [HBM, HBF và HBC: Cách phân biệt ba công nghệ bộ nhớ AI](/vi/post/hbm-hbf-hbc-ai-memory-comparison-2026-06-22/)
- [Giá trị hiện tại và tương lai của token AI: phân tích giá trị gia tăng của doanh nghiệp bộ nhớ](/vi/post/ai-token-value-memory-value-added-2026-07-09/)
- [Các cuộc gọi kết quả cuối tháng 7 của Big Tech và bản đồ kịch bản cho luận điểm bộ nhớ](/vi/post/big-tech-july-earnings-call-memory-thesis-scenarios-2026-07-07/)
- [Ai trả tiền cho đồng thuận bán dẫn năm 2027: Samsung, Hynix, Micron, Nvidia nhìn từ khả năng chi trả của hyperscaler](/vi/post/semiconductor-2027-earnings-hyperscaler-payability-memory-nvidia-2026-06-21/)
- [Định giá Samsung và SK Hynix theo lợi nhuận 2028E: con số rẻ và bài kiểm tra chu kỳ](/vi/post/samsung-hynix-2028e-profit-valuation-cycle-scenarios-2026-07-09/)
