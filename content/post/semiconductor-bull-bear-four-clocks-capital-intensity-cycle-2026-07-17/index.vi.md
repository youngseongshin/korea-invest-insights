---
title: "Tranh luận thực sự trong ngành bán dẫn: bốn chiếc đồng hồ vật lý và một chiếc đồng hồ giá cổ phiếu"
slug: "semiconductor-bull-bear-four-clocks-capital-intensity-cycle-2026-07-17"
date: 2026-07-17T11:00:00+09:00
description: "Phe tăng giá và giảm giá ngành bán dẫn không còn tranh cãi về việc nhu cầu AI có tồn tại hay không. Câu hỏi thực sự là liệu nhu cầu có vượt nguồn cung và cải thiện hiệu suất, liệu độ trễ giữa giá, đơn hàng, xây dựng và tạo doanh thu có thu hẹp, và liệu doanh thu tăng thêm có vượt qua khấu hao và chi phí vốn để đến được dòng tiền cổ đông. Kịch bản trung tâm là tăng giá về nền tảng nhưng giảm giá về định giá."
categories: ["Exclusive Analysis", "Market-Outlook", "Tech-Analysis"]
tags: ["Bán dẫn", "Bộ nhớ", "HBM", "AI CAPEX", "TSMC", "Samsung Electronics", "SK Hynix", "Micron", "Đóng gói tiên tiến", "Cường độ vốn", "Định giá"]
valley_cashtags: ["삼성전자", "SK하이닉스"]
draft: false
---

> Bối cảnh
> Bài viết này là bản tổng hợp gộp các trục đã được phân tích riêng lẻ từ trước vào một khung duy nhất. Bằng chứng về cầu được bàn trong [Vì sao việc IBM lỡ kỳ vọng lợi nhuận lại là bằng chứng cho sức mạnh của bộ nhớ](/vi/post/ibm-ericsson-q2-memory-cost-evidence-semiconductor-sentiment-2026-07-14/), sự lan tỏa của cung trong [Khoảng trống nguồn cung lan ra ngoài HBM](/vi/post/memory-supply-gap-spillover-substrate-essd-legacy-hana-three-reports-2026-07-14/), quy mô cung-cầu trong [Nghiên cứu chuyên sâu cung-cầu HBM 2030](/vi/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/), khả năng chi trả trong [Ai trả tiền cho đồng thuận bán dẫn năm 2027](/vi/post/semiconductor-2027-earnings-hyperscaler-payability-memory-nvidia-2026-06-21/), và định giá trong [Kịch bản xấu nhất đã nằm trong giá](/vi/post/samsung-hynix-worst-case-eps-priced-in-consensus-dispersion-2026-07-10/). Các hub liên quan là [Hub HBM AI](/vi/page/korea-semiconductor-hbm-kospi-hub/) và [Hub Phân tích độc quyền](/vi/page/exclusive-analysis-hub/).

## TL;DR

* Phe tăng giá và phe giảm giá ngành bán dẫn không còn tranh cãi về việc "nhu cầu AI có tồn tại hay không" nữa. Đơn hàng chính thức, tình trạng thiếu hụt node tiên tiến và đóng gói tiên tiến của TSMC, giới hạn nguồn cung bộ nhớ của Dell và HPE, CAPEX của các hyperscaler đều nghiêng về phía <strong>nhu cầu AI thực sự mạnh</strong>.
* Tranh luận thực sự có ba điểm. Tăng trưởng cầu có nhanh hơn cải thiện cung và hiệu suất hay không. Độ trễ giữa giá, đơn hàng, xây dựng và thu tiền có thu hẹp lại hay không. Doanh thu tăng thêm có vượt qua khấu hao, chi phí tài chính và cạnh tranh để còn lại thành dòng tiền cổ đông hay không.
* Luận điểm tăng giá mạnh nhất là "khi AI trở thành lớp nền tảng mới của mọi hoạt động tính toán, nút thắt vật lý sẽ kéo dài hơn dự kiến, còn hợp đồng dài hạn và thế độc quyền nhóm tạo ra <strong>đáy</strong> lợi nhuận cao hơn trước".
* Luận điểm giảm giá mạnh nhất là "nhu cầu AI vẫn tiếp tục tăng, nhưng ngay <strong>thời điểm tốc độ tăng trưởng vượt qua đỉnh</strong>, cung, khấu hao và chi phí vốn cùng lúc đi lên, khiến giá, biên lợi nhuận, ROIC và multiple đều trở về mức bình thường".
* Con đường khả dĩ nhất hiện nay là sự pha trộn. <strong>Ngành có thể là bull trong khi giá cổ phiếu có thể là valuation bear</strong> (xác suất 55%). Dù kết quả kinh doanh 2026-2027 mạnh, giá cổ phiếu vẫn chiết khấu trước phản ứng cung và độ trễ thu hồi vốn của giai đoạn 2027-2028. \[Phạm vi phân tích\]

---

<div class="thesis-callout">
  <div class="thesis-callout__label">Luận điểm chính</div>
  <div class="thesis-callout__body">
    Ngành bán dẫn AI vẫn chưa sụp đổ. Nhưng scarcity cycle đang dịch chuyển sang capital-intensity cycle. Đợt tăng tiếp theo sẽ không bắt đầu từ công bố CAPEX, mà bắt đầu khi điện năng đấu nối, tỷ lệ vận hành và dòng tiền AI đuổi kịp khấu hao và chi phí vốn.
  </div>
</div>

---

## 1. Nguyên tắc phân tích: không trộn lẫn bốn câu hỏi

Tranh luận về ngành bán dẫn thường sai vì gộp bốn câu hỏi khác nhau vào chung một câu.

1. <strong>Ngành</strong>: nhu cầu tính toán AI và bộ nhớ có tăng trưởng dài hạn hay không.
2. <strong>Lợi nhuận doanh nghiệp</strong>: nhà cung cấp hiện tại có duy trì được giá và biên lợi nhuận cao từ nhu cầu đó hay không.
3. <strong>Giá cổ phiếu</strong>: giá hiện tại đã phản ánh trước bao nhiêu phần lợi nhuận và rủi ro tương lai.
4. <strong>Danh mục đầu tư</strong>: dù là doanh nghiệp tốt, có nên nắm giữ thêm ở mức độ tập trung và tiền mặt hiện tại hay không.

Sự thật "nhu cầu AI mạnh" trả lời được câu hỏi về ngành nhưng không trả lời được câu hỏi về giá cổ phiếu và danh mục. Ngược lại, sự thật "SOXX lao dốc mạnh" nói lên thời điểm của giá cổ phiếu nhưng không chứng minh ngay được sự sụp đổ của nhu cầu ngành.

Nếu không giữ vững sự phân biệt này, phe tăng giá sẽ mua một ngành tốt ở bất kỳ mức giá nào, còn phe giảm giá sẽ tuyên bố ngành đã kết thúc chỉ vì một phiên lao dốc.

<strong>Lưu ý về phạm vi</strong>: phạm vi trọng tâm của bài viết này là bộ nhớ, foundry node tiên tiến, đóng gói tiên tiến, AI fabless, mạng và thiết bị, vật liệu liên quan do AI dẫn dắt. Ô tô, công nghiệp, analog và node trưởng thành nói chung chỉ được đề cập ở phần kết nối với chuỗi cung ứng AI. Do đó không nên áp dụng đồng nhất phán đoán này cho toàn bộ các phân ngành chi tiết của bán dẫn.

---

## 2. Bốn chiếc đồng hồ vật lý và một chiếc đồng hồ giá cổ phiếu

Trên thị trường này có năm chiếc đồng hồ chạy với tốc độ khác nhau. Khung phân tích này là xương sống của bài viết.

| Đồng hồ | Đo lường điều gì | Ý nghĩa hiện tại |
|---|---|---|
| Đồng hồ giá | ASP hợp đồng bộ nhớ, cơ cấu sản phẩm, giá foundry và đóng gói | Phản ánh vào kết quả kinh doanh hiện tại nhanh nhất |
| Đồng hồ đầu tư | Đơn hàng GPU, wafer, thiết bị, fab, CAPEX | Đặt trước nguồn cung tương lai và ý chí của khách hàng |
| Đồng hồ xây dựng | Đấu nối điện, hoàn công trung tâm dữ liệu, lắp đặt rack, ramp fab | Chuyển hóa đầu tư đã công bố thành năng lực vận hành thực tế |
| Đồng hồ thu tiền | Doanh thu AI và cloud, lợi nhuận gộp, FCF | Thu hồi chi phí đầu tư, khấu hao, chi phí tài chính |
| Đồng hồ giá cổ phiếu | Khoảng cách 6-12 tháng phía trước bốn đồng hồ trên | Chuyển động sớm nhất và chiết khấu tốc độ thay đổi |

Khi đồng hồ giá và đồng hồ đầu tư đi trước còn đồng hồ xây dựng và đồng hồ thu tiền đi sau, <strong>kết quả kinh doanh tốt và CAPEX được nâng lên có thể ngược lại trở thành yếu tố bán ra.</strong> Vì thị trường nhìn vào công suất chưa vận hành, khấu hao, nợ vay và khoảng trống ROI trong tương lai nhiều hơn là lợi nhuận hiện tại.

Ngược lại, khi khoảng cách giữa bốn đồng hồ thu hẹp lại, đà tăng giá sẽ khởi động trở lại. Đó là khi số GW đã công bố chuyển hóa thành lượng điện đấu nối thực tế và tỷ lệ sử dụng GPU, khi tăng trưởng lợi nhuận gộp AI vượt qua khấu hao và chi phí lãi vay, và khi lượng mua trước của khách hàng được tiêu thụ bằng nhu cầu sử dụng thực tế chứ không phải nằm lại thành tồn kho.

Dùng khung này, các câu hỏi vốn tưởng như rời rạc sẽ được giải thích trong cùng một cấu trúc. Vì sao kết quả kinh doanh tốt mà giá cổ phiếu vẫn giảm. Vì sao CAPEX tăng mà giá cổ phiếu của khách hàng vẫn yếu. Vì sao đang thiếu cung mà cổ phiếu thiết bị lại giảm trước.

---

## 3. Tiền đề chung mà phe tăng giá và phe giảm giá đều thừa nhận

Phe tăng giá và phe giảm giá tinh vi nhìn chung đồng ý với những sự thật sau.

1. Nhu cầu huấn luyện và suy luận AI hiện tại là có thực.
2. Tồn tại nút thắt vật lý ở node tiên tiến, HBM, đóng gói tiên tiến, điện năng và mạng.
3. Kết quả kinh doanh chuỗi cung ứng giai đoạn 2026-2027 có khả năng cao sẽ mạnh.
4. Giá cổ phiếu luôn nhìn vào tốc độ thay đổi của ước tính lợi nhuận và giai đoạn cung tiếp theo trước khi nhìn vào kết quả kinh doanh tuyệt đối.
5. Không phải mọi loại bán dẫn đều hưởng lợi như nhau.
6. Một ngành tốt và một thời điểm mua tốt là hai việc khác nhau.

Do đó, điểm tranh cãi giữa hai bên không phải là sự tồn tại của nhu cầu, mà là <strong>thời gian duy trì và chất lượng của nhu cầu, tốc độ phản ứng của nguồn cung, khả năng sinh lời của doanh thu gia tăng, định giá và vị thế hiện tại</strong>.

---

# Phần I. Luận điểm tăng giá (Bull Case)

> <strong>Khi AI không còn là một tính năng phần mềm đơn lẻ mà trở thành lớp nền tảng mới của toàn bộ hoạt động tính toán, nhu cầu về khối lượng tính toán, dung lượng bộ nhớ, băng thông, mạng và điện năng cùng lúc phình to. Nguồn cung không thể theo kịp ngay vì lead time dài của việc xây fab, đóng gói, điện năng và chứng nhận khách hàng, còn nhà cung cấp trong thế độc quyền nhóm và hợp đồng dài hạn tạo ra đáy lợi nhuận cao hơn trước đây cùng thời gian duy trì dài hơn.</strong>

Cốt lõi của luận điểm tăng giá không phải là giá sẽ tăng tốc mãi mãi. Đây là lập luận rằng dù tốc độ tăng giá chậm lại, sự kết hợp giữa ASP cao hơn trước, cơ cấu sản phẩm cao cấp, khả năng nhìn thấy trước sản lượng và kỷ luật vốn vẫn có thể làm <strong>diện tích lợi nhuận</strong> mở rộng.

### 4. Nhu cầu đang được kiểm chứng bằng đơn hàng vật lý, không phải bằng phát biểu

Điều quan trọng nhất trong cuộc gọi 2Q26 của TSMC không phải là phát biểu lạc quan dài hạn, mà là <strong>thay đổi thực tế trong CAPEX và phân bổ công suất</strong>. \[Thực tế/Hạng B: đối chiếu tài liệu truyền đạt cuộc gọi kết quả kinh doanh với nhiều báo cáo nghiên cứu, đối chiếu trực tiếp với văn bản IR chính thức bị hạn chế một phần\]

- Nâng hướng dẫn tăng trưởng doanh thu FY2026 lên trên 40%
- Nâng CAPEX năm 2026 lên 60-64 tỷ USD
- Giải thích khoảng cách cung-cầu ở node tiên tiến dưới N3 và đóng gói tiên tiến là rất lớn
- Cho biết không đơn thuần cộng dồn đơn hàng khách hàng, mà xác nhận cả vị trí trung tâm dữ liệu, tiến độ xây dựng, khả năng đảm bảo điện năng và việc lắp đặt rack

Sự kết hợp này làm suy yếu luận điểm giảm giá yếu kiểu "đơn hàng ma" và "toàn bộ nhu cầu AI là đặt hàng trùng lặp". Quyết định mua thiết bị và xây fab của TSMC khó có thể xảy ra nếu thiếu tín hiệu nhu cầu dài hạn, khoản đặt cọc trước và lộ trình đồng phát triển từ khách hàng.

Việc Dell và HPE chỉ ra DRAM và NAND là ràng buộc hàng đầu trong nguồn cung máy chủ, và việc Teradyne xác nhận nhu cầu nửa cuối năm mạnh cho khâu kiểm tra HBM và DRAM, cũng đi theo cùng hướng. \[Thực tế/Hạng C-B: broker channel check\] Nhu cầu không chỉ nằm trên slide mà còn hiện diện trong lượng xuất xưởng máy chủ, phân bổ bộ nhớ, thiết bị kiểm tra và công suất đóng gói.

<strong>Diễn giải của phe tăng giá</strong>: bằng chứng quan trọng nhất của nhu cầu AI không phải là dự báo doanh thu, mà là việc nhà cung cấp đang đổ vào <strong>khoản vốn khó đảo ngược</strong>.

<strong>Điều kiện phản chứng</strong>: hyperscaler thực sự cắt giảm CAPEX. TSMC và các hãng bộ nhớ trì hoãn việc đưa thiết bị vào và ramp fab. Việc trì hoãn hợp đồng khách hàng và sụt giảm tỷ lệ vận hành xuất hiện đồng thời.

### 5. Nhu cầu lan từ một loại GPU duy nhất ra toàn bộ BOM máy chủ

Đầu tư AI ban đầu tập trung vào GPU và HBM, nhưng khi quy mô lớn lên, nút thắt dịch chuyển sang CPU, mạng, lưu trữ, quản lý điện năng, bo mạch nền và linh kiện thụ động.

- Agentic AI sử dụng đồng thời không chỉ GPU mà cả CPU, bộ nhớ, mạng và lưu trữ.
- Suy luận quy mô lớn làm tăng yêu cầu về KV cache và băng thông bộ nhớ.
- Khi mở rộng từ scale-up sang scale-out rồi scale-across, nhu cầu về switch tốc độ cao, quang học và kết nối coherent tăng lên.
- eSSD, IC quản lý điện năng, MLCC, ABF, CCL và PCB nhiều lớp cao cấp của trung tâm dữ liệu AI trở thành nút thắt đến sau.

Do đó, dù tốc độ tăng trưởng của riêng NVIDIA chậm lại, tổng thị trường mục tiêu của bán dẫn AI vẫn có thể mở rộng sang các linh kiện khác. ASIC tự phát triển cũng không phá vỡ hoàn toàn logic này. TPU và Trainium có thể làm giảm thị phần GPU, nhưng vẫn tiêu thụ node tiên tiến, HBM hoặc DRAM hiệu năng cao, đóng gói tiên tiến và mạng.

<strong>Diễn giải của phe tăng giá</strong>: đầu tư AI đang tiến hóa từ chu kỳ GPU thành <strong>chu kỳ BOM trung tâm dữ liệu AI</strong>. Vai trò dẫn đầu có thể đổi chủ, nhưng tổng nhu cầu silicon, bộ nhớ và đóng gói vẫn được duy trì.

<strong>Điều kiện phản chứng</strong>: cải thiện hiệu suất làm tăng thông lượng nhưng chi tiêu bằng USD cho máy chủ, bộ nhớ và mạng lại giảm, và hiện tượng này lặp lại ở nhiều khách hàng.

### 6. HBM là sản phẩm tự ăn mòn nguồn cung của chính nó

HBM đòi hỏi diện tích wafer lớn hơn, TSV và xếp chồng, đóng gói, kiểm tra và chứng nhận khách hàng. Khi tỷ trọng HBM tăng lên, lượng bit có thể sản xuất từ cùng một lượng wafer đưa vào sẽ giảm, đồng thời công suất DRAM thông dụng cũng bị hạn chế.

Điều này tạo ra hai hiệu ứng có lợi cho phe tăng giá. Thứ nhất, bản thân nguồn cung HBM khó có thể tăng nhanh. Thứ hai, việc chuyển đổi sang HBM làm giảm nguồn cung hiệu dụng của DRAM thông dụng, qua đó hỗ trợ đồng thời giá DRAM máy chủ và DRAM phổ thông.

Fab mới cũng không tạo ra nguồn cung ngay khi công bố. Cần lần lượt trải qua các bước điện năng, nước, cleanroom, lắp đặt thiết bị, ramp quy trình, yield và chứng nhận khách hàng. Vẫn tồn tại độ trễ cho đến khi cơ sở mới của SK Hynix Y1 và các cơ sở mới của Samsung Electronics, Micron đóng góp thành nguồn cung bit thực tế.

<strong>Diễn giải của phe tăng giá</strong>: sự khan hiếm trong chu kỳ này là <strong>tình trạng thiếu hụt phức hợp đòi hỏi đồng thời wafer tốt, xếp chồng yield cao, đóng gói đã được kiểm chứng và chứng nhận khách hàng</strong>. Vì vậy chỉ đổ tiền vào cũng không giải quyết được ngay.

<strong>Điều kiện phản chứng</strong>: yield HBM và năng suất đóng gói tăng nhanh hơn dự kiến, chứng nhận khách hàng của Samsung Electronics và Micron chuyển thành sản lượng quy mô lớn, khiến tốc độ tăng cung vượt qua tốc độ tăng cầu.

### 7. Thế độc quyền nhóm và hợp đồng dài hạn có thể làm giảm biên độ chu kỳ

Ngành bộ nhớ có ít nhà cung cấp hơn trước, và HBM đòi hỏi đồng phát triển và chứng nhận sâu theo từng khách hàng. LTA khiến nhà cung cấp phải từ bỏ một phần đà tăng vọt của giá giao ngay, nhưng đổi lại nâng cao khả năng nhìn thấy trước sản lượng, lock-in khách hàng và sự tin cậy trong đầu tư.

Các chu kỳ trước đây có cấu trúc là nhà cung cấp phản ứng với giá giao ngay bằng cách mở rộng công suất, khách hàng tích trữ tồn kho, rồi giá sụp đổ. Nếu hợp đồng dài hạn bao gồm sản lượng tối thiểu, công thức điều chỉnh giá và tính chất Take-or-Pay, thì <strong>dù đỉnh lợi nhuận thấp hơn, đáy và thời gian duy trì lợi nhuận vẫn có thể cao hơn.</strong>

Điều phe tăng giá đặt cược không phải là "giá sẽ tiếp tục tăng nhanh hơn nữa", mà là giả định "lợi nhuận cao sẽ duy trì lâu hơn".

<strong>Điều chưa xác minh cốt lõi</strong>: giá sàn, giá trần, sản lượng tối thiểu, điều khoản tái đàm phán và điều khoản hủy hợp đồng của LTA phần lớn không được công khai. Không nên nâng LTA lên thành sự bảo đảm lợi nhuận vô điều kiện. \[Chưa xác minh\]

### 8. Con hào của node tiên tiến nằm ở đường cong học tập, không phải ở thiết bị

Phát biểu của Chủ tịch TSMC C.C. Wei rằng "chọn foundry không phải như chọn mua sữa ở cửa hàng tiện lợi" mô tả chính xác chi phí chuyển đổi của node tiên tiến.

Khách hàng phải đồng hành nhiều năm cùng nhà cung cấp qua các bước chọn quy trình, thiết kế PDK và IP, chip thử nghiệm, tối ưu hóa chung, học tập yield, đảm bảo công suất cho đến sản xuất hàng loạt. Việc sở hữu cùng loại thiết bị ASML không khiến khách hàng lập tức chuyển đổi. Đóng gói tiên tiến cũng đòi hỏi giải quyết đồng thời substrate, nhiệt, điện năng, tính toàn vẹn tín hiệu và kiểm tra.

<strong>Diễn giải của phe tăng giá</strong>: bán dẫn node tiên tiến trông có vẻ như hàng hóa thông thường (commodity), nhưng không phải là sản phẩm hoàn toàn đồng nhất vì chi phí chuyển đổi của khách hàng và quá trình học tập chung. Dù nguồn cung tăng lên, lợi nhuận vượt trội của người dẫn đầu đã được kiểm chứng vẫn có thể duy trì lâu hơn dự kiến. Trong giai đoạn thiếu cung, khách hàng chọn <strong>nhà cung cấp giữ đúng tiến độ và yield</strong> thay vì nhà cung cấp rẻ nhất.

### 9. Thiếu điện năng và giấy phép có thể làm chậm nhu cầu nhưng không phá hủy nhu cầu

Việc chậm trễ đấu nối điện và xây dựng trung tâm dữ liệu là căn cứ cốt lõi của phe giảm giá. Nhưng phe tăng giá coi đây không phải là sự vắng mặt của nhu cầu, mà là <strong>backlog đang chờ đi vào vận hành</strong>.

Nhà vận hành đã đảm bảo được điện năng, mặt bằng, trạm biến áp và làm mát đang nắm giữ tài sản khan hiếm. Trong lúc nhu cầu vẫn được duy trì, việc chậm trễ xây dựng có thể biểu hiện dưới dạng dời thời hạn giao hàng và phần bù giá, hơn là hủy đơn hàng. Việc TSMC xác nhận vị trí trung tâm dữ liệu và khả năng đảm bảo điện năng của khách hàng là bằng chứng cho thấy ít nhất đồng hồ xây dựng của nhóm khách hàng hàng đầu chưa hoàn toàn dừng lại.

<strong>Điều kiện của phe tăng giá</strong>: các dự án bị trì hoãn không bị hủy mà lần lượt đi vào vận hành, và sau khi vận hành phải dẫn đến tỷ lệ sử dụng cao và doanh thu cloud tương ứng.

### 10. Trung Quốc đuổi kịp là rủi ro cho phân khúc phổ thông nhưng khó thay thế frontier trong ngắn hạn

IPO và huy động vốn quy mô lớn của CXMT là rủi ro nguồn cung DRAM phổ thông trong trung và dài hạn. Nhưng ở HBM, node tiên tiến và đóng gói tiên tiến vẫn tồn tại rào cản về yield, thiết bị, vật liệu, hệ sinh thái thiết kế và chứng nhận khách hàng.

Quy định của Mỹ đối với thiết bị bán sang Trung Quốc và các thảo luận về hạn chế mua hàng từ CXMT, YMTC có thể làm chậm việc mở rộng khách hàng toàn cầu của các doanh nghiệp Trung Quốc, đồng thời củng cố vị thế thị trường ex-China của các nhà cung cấp Hàn Quốc, Mỹ, Đài Loan.

<strong>Diễn giải của phe tăng giá</strong>: nguồn cung Trung Quốc là vấn đề của <strong>"giá trần DRAM phổ thông sau năm 2028"</strong> hơn là <strong>"sự sụp đổ của HBM ngay hôm nay"</strong>. Độ trễ về công nghệ và chứng nhận đủ dài để không làm suy yếu luận điểm tăng giá trong ngắn hạn.

### 11. Dữ liệu xuất khẩu thực tế xác nhận đà tăng trưởng mạnh

Theo số liệu tạm tính ngày 1-10/7/2026 của Tổng cục Hải quan, xuất khẩu bán dẫn đạt mức mạnh 11,2 tỷ USD. Trong xuất khẩu DRAM/HBM từ Hàn Quốc sang Đài Loan tháng 6, chỉ báo HBM proxy đã điều chỉnh theo baseline (baseline-adjusted HBM proxy) cũng duy trì tín hiệu constructive. \[Thực tế/Hạng A-B: số liệu chính thức của Tổng cục Hải quan, proxy ở mức medium\]

Dữ liệu này không chứng minh trực tiếp doanh thu HBM theo từng công ty, nhưng ít nhất phản bác lại lập luận rằng đà xuất khẩu bán dẫn Hàn Quốc đã đột ngột suy yếu.

<strong>Lưu ý</strong>: số liệu tạm tính 10 ngày chỉ là cảnh báo sớm. Không nên nâng cấp thành luận điểm dài hạn trước khi xác nhận được sự quy thuộc theo mặt hàng, công ty và hiệu ứng nền cuối tháng.

### 12. Multiple thấp có thể đã phản ánh một phần sự bình thường hóa lợi nhuận

Cổ phiếu bộ nhớ là ngành nhận P/E thấp ngay tại đỉnh lợi nhuận. Vì vậy bản thân P/E thấp không phải là bằng chứng cho thấy cổ phiếu đang rẻ. Nhưng nếu thị trường đang chiết khấu quá mức tính bền vững của lợi nhuận năm 2027, trong khi đáy lợi nhuận thực tế cao hơn trước đây, giá cổ phiếu vẫn có thể tăng nhờ <strong>bình thường hóa multiple</strong> dù EPS không tăng thêm.

Tính bất đối xứng mà phe tăng giá đặt cược không phải là "giá phải tiếp tục tăng tốc thì cổ phiếu mới lên". Đó là việc nếu giá hợp đồng ổn định ở mức cao, LTA và cơ cấu sản phẩm cao cấp duy trì được FCF, và kỷ luật của nhà cung cấp được xác nhận, thị trường có thể trao cho cổ phiếu không phải peak multiple mà là <strong>durable earnings multiple</strong>.

---

# Phần II. Luận điểm giảm giá (Bear Case)

> <strong>Nhu cầu AI sẽ không biến mất. Nhưng khi tốc độ tăng trưởng nhu cầu vượt qua đỉnh, nếu tình trạng mua trước trở về bình thường, nguồn cung mới, khấu hao và chi phí vốn của khách hàng xuất hiện đồng thời, biên lợi nhuận gia tăng của nhà cung cấp và multiple của giá cổ phiếu sẽ cùng bị nén lại. Ngành vẫn tăng trưởng nhưng cổ đông có thể trải qua tỷ suất sinh lời thấp.</strong>

Cốt lõi của luận điểm giảm giá không phải là doanh thu sụp đổ, mà là <strong>khả năng sinh lời của doanh thu gia tăng suy giảm</strong>. Dù tin tốt liên tục xuất hiện, nếu mức độ nâng EPS thu hẹp lại và định giá hạ thấp, giá cổ phiếu sẽ giảm trước.

### 13. Giá cổ phiếu luôn nhìn vào tốc độ thay đổi trước khi nhìn vào kết quả kinh doanh tuyệt đối

Đỉnh 4Q26 trong tài liệu của Morgan Stanley nên được đọc chính xác hơn là <strong>đỉnh của tốc độ tăng theo năm của giá hợp đồng</strong>, chứ không phải đỉnh của mức giá bộ nhớ tuyệt đối. \[Hạng C/thấp-trung bình: chưa xác minh trực tiếp định nghĩa giá và giả định gốc\] Dù giá tiếp tục tăng và EPS tiếp tục tăng, nếu biên độ tăng thu hẹp lại, giá cổ phiếu vẫn có thể quay đầu trước.

Cổ phiếu bán dẫn nhạy cảm với đạo hàm bậc hai hơn là đạo hàm bậc một.

- Doanh thu tăng: có thể đã là sự thật ai cũng biết.
- EPS tăng: có thể đã được phản ánh vào đồng thuận.
- Mức độ nâng EPS chậm lại: là thông tin mới và tiêu cực với giá cổ phiếu.

Sự suy yếu của cổ phiếu bán dẫn trong tháng 7/2026 không khẳng định chắc chắn sự sụp đổ của ngành, nhưng việc giá cổ phiếu không phản ứng dù TSMC công bố kết quả kinh doanh tốt và bình luận tích cực về nhu cầu AI cho thấy <strong>lợi ích cận biên của kỳ vọng đã biến mất</strong>.

### 14. Rush order và giới hạn nguồn cung có thể đang kéo nhu cầu tương lai về hiện tại

Giới hạn nguồn cung DRAM và NAND của Dell, HPE cùng với Rush order của các OEM máy chủ là bằng chứng cho sự mạnh mẽ của nhu cầu hiện tại. \[Hạng C-B: tài liệu truyền đạt của BofA\] Nhưng đồng thời đây cũng có thể là tín hiệu cuối chu kỳ, khi khách hàng lo sợ thiếu hàng và giá tăng nên đẩy sớm đơn hàng.

Cisco đã có các phản ứng sau trước việc giá thành bộ nhớ tăng. \[Hạng C-B: tài liệu truyền đạt của JPM\]

- Cam kết mua trước bộ nhớ
- Tăng giá sản phẩm
- Giảm lượng bộ nhớ lắp trong switch
- Ngừng một số giao dịch máy chủ

Đây là <strong>hành động ban đầu của sự phá hủy nhu cầu</strong>, quan trọng hơn nhiều so với việc chỉ tích trữ tồn kho đơn thuần. Trong [trường hợp của IBM](/vi/post/ibm-ericsson-q2-memory-cost-evidence-semiconductor-sentiment-2026-07-14/), một số hợp đồng phần mềm và hệ thống cũng bị trì hoãn khi khách hàng chuyển ngân sách sang mua trước máy chủ, lưu trữ và bộ nhớ. \[Thực tế/Hạng A: IBM 8-K\]

Nếu lượng xuất xưởng hiện tại là tiêu thụ cuối cùng, đơn hàng sẽ được duy trì ngay cả sau khi nguồn cung trở lại bình thường. Ngược lại, nếu đó là mua trước, sẽ xuất hiện khoảng trống đơn hàng trong thời gian tiêu thụ hết tồn kho.

### 15. Giá tăng quá cao sẽ tự phá hủy nhu cầu của chính nó

Giá bộ nhớ tăng có lợi cho kết quả kinh doanh của nhà cung cấp nhưng lại đẩy BOM và giá sản phẩm của khách hàng lên cao. Khách hàng PC, smartphone và máy chủ phổ thông nhạy cảm với giá có thể hạ thông số kỹ thuật hoặc trì hoãn việc mua hàng.

Tài liệu cuộc gọi của TSMC giải thích rằng giá linh kiện tăng đang tạo gánh nặng cho thị trường cuối nhạy cảm về giá và người tiêu dùng. Dù nhu cầu ở nhóm cao cấp nhất của trung tâm dữ liệu AI vẫn mạnh, nếu nhu cầu CNTT phổ thông yếu đi, sự phân cực bên trong ngành sẽ càng trầm trọng.

Rủi ro mà phe giảm giá nhìn thấy không phải là "nhu cầu HBM biến mất". Đó là việc mức giá cao của HBM và DRAM máy chủ đang thúc đẩy khách hàng <strong>thiết kế thay thế, tối ưu hóa bộ nhớ, điều chỉnh thời điểm mua hàng và làm co lại nhu cầu sản phẩm phổ thông</strong>.

### 16. Khi tình trạng thiếu hụt mạnh nhất cũng là lúc phản ứng cung lớn nhất

Việc TSMC nâng CAPEX, ba hãng bộ nhớ mở rộng công suất, công suất đóng gói tiên tiến và kiểm tra được mở rộng vừa là bằng chứng của nhu cầu hiện tại, vừa là <strong>hạt giống của nguồn cung tương lai</strong>.

Giai đoạn 2027-2028 có thể xuất hiện đồng thời các yếu tố sau.

- Lượng wafer đưa vào của fab mới tăng lên
- Yield HBM và năng suất xếp chồng cải thiện
- Nút thắt đóng gói tiên tiến được nới lỏng
- Thị phần HBM4 của Samsung Electronics và Micron tăng lên
- Nguồn cung DRAM phổ thông của CXMT mở rộng

Khi nút thắt được tháo gỡ, lượng xuất xưởng toàn ngành tăng lên nhưng scarcity premium của những người chiến thắng hiện tại lại giảm xuống. Dù SK Hynix bán được nhiều sản lượng hơn, phần bù giá HBM và biên lợi nhuận gia tăng vẫn có thể giảm.

<strong>Việc tháo gỡ nút thắt là tin tốt cho khách hàng và toàn ngành, nhưng có thể là tin xấu cho lợi nhuận vượt trội của nhà cung cấp hiện tại.</strong>

### 17. Nút thắt CAPEX AI đang dịch chuyển từ chip sang chi phí vốn

Con số CAPEX hợp nhất năm 2027 của Alphabet, Meta, Amazon theo Citi là 801 tỷ USD, đây không phải là hướng dẫn của công ty mà là ước tính mang tính tấn công của nhà phân tích. \[Hạng C-B\] Con số này quan trọng không phải vì quy mô, mà vì hàm ý của mô hình rằng <strong>FCF của cả ba công ty sẽ chuyển sang âm trong giai đoạn 2027-2028</strong>.

Theo tài liệu chính thức FY2026, Oracle có các số liệu sau. \[Thực tế/Hạng A: SEC 10-K\]

| Hạng mục | Số tiền |
|---|---:|
| CAPEX | 55,7 tỷ USD |
| Dòng tiền từ hoạt động kinh doanh (OCF) | 32,0 tỷ USD |
| FCF đơn giản | khoảng -23,7 tỷ USD |
| Tổng nợ vay | 129,5 tỷ USD |

Dù có nhu cầu AI, khả năng đầu tư của khách hàng không phải là vô hạn. CAPEX vượt quá dòng tiền phải phụ thuộc vào trái phiếu doanh nghiệp, thuê tài chính, tài trợ dự án và tăng vốn. Nếu lãi suất, chênh lệch tín dụng và giá cổ phiếu cùng lúc trở nên bất lợi, các kế hoạch từ năm 2027 trở đi có thể bị điều chỉnh trước tiên.

Take-or-Pay và RPO cũng không phải là tấm khiên an toàn hoàn hảo. Chúng vừa đảm bảo doanh thu cho khách hàng, vừa làm tăng nghĩa vụ xây dựng cơ sở vật chất và gánh nặng huy động vốn của nhà cung cấp.

<strong>Điều chỉnh quan trọng</strong>: nút thắt chi phí vốn không phải là sự sụp đổ nhu cầu đã được xác định ở hiện tại. Vì TSMC và các hyperscaler vẫn đang nâng CAPEX, nên cần phân loại đây là <strong>rủi ro tương lai</strong>.

### 18. Tăng trưởng lượng sử dụng AI và tăng trưởng doanh thu bán dẫn tính bằng USD không phải là một

Lượng tử hóa (quantization), sparsity, tái sử dụng cache, speculative decoding, gộp bộ nhớ CXL và tối ưu hóa phần mềm đang làm giảm chi phí phần cứng cần thiết cho "mỗi đơn vị trí tuệ".

Nếu tổng lượng sử dụng tăng nhanh hơn cải thiện hiệu suất, nhu cầu bán dẫn sẽ tiếp tục tăng trưởng. Nhưng nếu tốc độ của hai bên trở nên tương đương nhau, dù lượng token và suy luận bùng nổ, <strong>tốc độ tăng trưởng doanh thu tính bằng USD của các hãng chip vẫn có thể chậm lại</strong>.

ASIC tự phát triển là rủi ro thị phần trực tiếp đối với NVIDIA và các bộ tăng tốc phổ thông. Đối với bộ nhớ, tác động ít trực tiếp hơn, nhưng việc tối ưu hóa tầng bộ nhớ và băng thông theo từng khách hàng vẫn có thể làm giảm lượng HBM lắp đặt hoặc độ co giãn giá.

### 19. Quá trình thu tiền của AI có thể không theo kịp khấu hao và chi phí tài chính

GPU và trung tâm dữ liệu tạo ra doanh thu <strong>sau khi vận hành</strong>, chứ không phải tại thời điểm đặt hàng. Nếu việc đấu nối điện và lắp đặt rack bị trì hoãn, vốn sẽ được đổ vào trước còn doanh thu đến sau.

Đồng hồ thu tiền càng chậm, các chi phí sau sẽ càng tích lũy.

- Khấu hao fab, máy chủ, thiết bị điện mới
- Lãi trái phiếu doanh nghiệp, thuê tài chính, tài trợ dự án
- Rủi ro lỗi thời kinh tế và tổn thất của GPU đời cũ
- Suy yếu quyền đàm phán do tập trung khách hàng
- Vòng quay tài sản thấp của công suất chưa vận hành

CoreWeave là trường hợp cho thấy dù nhu cầu AI mạnh, chi phí vốn vẫn có thể bào mòn giá trị cổ đông. \[Thực tế/Hạng A: SEC\]

| Hạng mục | 1Q26 |
|---|---:|
| Doanh thu | 2,078 tỷ USD |
| Chi phí đầu tư (capex) | 7,695 tỷ USD |
| Chi phí lãi vay ròng | 536 triệu USD |
| Tỷ trọng doanh thu từ hai khách hàng lớn nhất | 65% |

Dù RPO lớn cũng không loại bỏ được chi phí huy động vốn cao và nghĩa vụ xây dựng cơ sở vật chất. Hiện chưa có bằng chứng cho thấy sự yếu ớt này lây lan ra toàn bộ hyperscaler. Nhưng nếu các neocloud có đòn bẩy cao và các doanh nghiệp ngoại vi như Oracle lung lay trước, nhu cầu biên của đơn hàng bán dẫn có thể suy yếu theo.

### 20. Nguồn vốn Trung Quốc có thể làm suy yếu kỷ luật cung trong giai đoạn xuống chu kỳ

IPO quy mô lớn của CXMT không phải là sự kiện tạo ra năng lực cạnh tranh HBM ngay lập tức. Ý nghĩa quan trọng hơn là việc <strong>CXMT đã đảm bảo được nguồn vốn để tiếp tục phát triển công nghệ và mở rộng công suất ngay cả trong giai đoạn ngành đi xuống</strong>.

Nhà cung cấp theo kinh tế thị trường sẽ cắt giảm CAPEX khi giá và khả năng sinh lời giảm xuống. Nhưng nhà cung cấp ưu tiên mục tiêu chính sách và nội địa hóa có thể chọn mở rộng thị phần ngay cả khi khả năng sinh lời thấp. Nếu CXMT thay thế DRAM phổ thông ở thị trường nội địa Trung Quốc, các nhà cung cấp toàn cầu có thể phân bổ nhiều sản lượng hơn ra thị trường ngoài Trung Quốc, và điều này sẽ đè giá trần xuống.

### 21. Doanh thu tăng nhưng biên lợi nhuận gia tăng vẫn có thể quay đầu

Trong giai đoạn đi lên, giá, tỷ lệ vận hành và tỷ trọng HBM đồng thời kéo biên lợi nhuận lên. Trong giai đoạn đi xuống, chính đòn bẩy đó vận hành theo chiều ngược lại.

- Khấu hao của fab và thiết bị mới tăng lên
- Chi phí ramp ban đầu của N2 và fab hải ngoại
- Phần bù giá thu hẹp do yield HBM cải thiện và cạnh tranh gia tăng
- Khách hàng hạ thông số kỹ thuật và kháng cự giá
- Nguồn cung DRAM, NAND phổ thông tăng lên
- Scarcity rent thu hẹp do nút thắt đóng gói và kiểm tra được tháo gỡ

Câu hỏi mạnh nhất của phe giảm giá không phải là "doanh thu có tăng hay không", mà là <strong>"một đồng doanh thu tăng thêm có tạo ra lợi nhuận hoạt động tương đương như trước hay không"</strong>. Khi biên lợi nhuận hoạt động gia tăng vượt qua đỉnh, dù EPS vẫn tăng, giá cổ phiếu vẫn có thể bị de-rating.

### 22. Sự thay đổi vai trò dẫn dắt của thị trường cho thấy điều chỉnh kỳ vọng đặc thù của ngành bán dẫn

Tính đến ngày 16/7/2026, SOXX đã giảm khoảng 19% so với đỉnh tháng 6, và hiệu suất tương đối so với SPY trong 20 phiên giao dịch gần nhất cũng xấu đi đáng kể. Trong khi xu hướng ngắn hạn của QQQ và chỉ số bán dẫn bị tổn hại, Dow Jones và S&P500 tính theo trọng số bằng nhau lại tương đối mạnh. \[Hạng B+: đối chiếu Yahoo/TradingView\]

Đây gần với một đợt <strong>luân chuyển dòng tiền có chọn lọc</strong>, khi tiền dịch chuyển từ các vị thế quá đông ở công nghệ và bán dẫn sang tài chính, y tế, năng lượng và cổ phiếu giá trị, hơn là một sự sụp đổ toàn diện của toàn bộ thị trường chứng khoán Mỹ.

Đây không phải là bằng chứng cho thấy ngành đã sụp đổ, mà là <strong>bằng chứng cho thấy thị trường không còn sẵn sàng mua câu chuyện ngành tốt ở bất kỳ mức giá nào nữa</strong>. Khi cổ phiếu bán dẫn không tăng dù có tin tốt còn các ngành khác lại mạnh lên, chi phí cơ hội của việc nắm giữ cổ phiếu bán dẫn sẽ tăng lên.

### 23. Mức độ tập trung là rủi ro tách biệt với luận điểm tăng giá

Dù cốt lõi ngành bán dẫn đúng về dài hạn, nếu mức độ tiếp xúc tập trung vào bộ nhớ và hạ tầng AI, chỉ một yếu tố chung cũng có thể làm rung chuyển toàn bộ danh mục.

- Samsung Electronics, SK Hynix, Micron là các cổ phiếu khác nhau nhưng cùng gắn với <strong>yếu tố chung là giá DRAM và CAPEX AI</strong>.
- Quang học và linh kiện, thiết bị, vật liệu cũng phản ứng đồng thời với CAPEX của hyperscaler và trạng thái risk-on/risk-off.
- Khi thiếu tiền mặt, nhà đầu tư buộc phải hành động thay vì phán đoán khi thị trường lao dốc mạnh.

Do đó cần tách bạch nguyên tắc "nắm giữ lâu dài một doanh nghiệp tốt" với vấn đề "nắm giữ quá mức các cổ phiếu có tương quan cao với nhau". <strong>Luận điểm tăng giá dài hạn không biện minh cho mức độ tập trung.</strong>

---

## 24. Cùng một bằng chứng, phe tăng giá và phe giảm giá đọc khác nhau như thế nào

Bảng này là phần thực dụng nhất của bài viết. Hai bên đọc cùng một tin tức theo hướng hoàn toàn ngược nhau, và cột cuối cùng chính là biến số phân định thực sự.

| Bằng chứng | Diễn giải phe tăng giá | Diễn giải phe giảm giá | Biến số phân định thực sự |
|---|---|---|---|
| CAPEX TSMC 60-64 tỷ USD | Kiểm chứng vật lý cho nhu cầu AI dài hạn | Cung và khấu hao tăng trong giai đoạn 2027-2028 | Tỷ lệ vận hành, giá, ROIC gia tăng |
| Rush order DRAM máy chủ | Thiếu hụt và nhu cầu thực sự mạnh | Kéo nhu cầu tương lai về hiện tại | Tồn kho khách hàng, kênh phân phối và tái đặt hàng |
| Cải thiện yield HBM | Mở rộng xuất xưởng và giảm giá thành | Thu hẹp phần bù giá và scarcity rent | Cải thiện giá thành có nhanh hơn giảm giá bán hay không |
| Mở rộng LTA | Tăng khả năng nhìn thấy sản lượng, nâng đáy lợi nhuận | Giới hạn giá trần, chuyển rủi ro tín dụng sang khách hàng | Sản lượng tối thiểu, công thức giá, điều khoản hủy hợp đồng |
| Mở rộng ASIC tự phát triển | Mở rộng TAM silicon AI ra ngoài GPU | Giảm thị phần và ASP của bộ tăng tốc phổ thông | Tổng tiêu thụ HBM, wafer, đóng gói |
| Trì hoãn điện năng và xây dựng | Giá trị của nhu cầu chờ đợi và tài sản khan hiếm | Trì hoãn doanh thu, công suất chưa vận hành, lãi vay tích lũy | Tỷ lệ hủy, lượng điện đấu nối thực tế, tỷ lệ vận hành |
| IPO của CXMT | Khó thay thế HBM trong ngắn hạn | Tiếp tục mở rộng phân khúc phổ thông ngay cả trong downcycle | Lượng wafer đưa vào, yield DDR5, chứng nhận khách hàng |
| RPO và Take-or-Pay cao | Khả năng nhìn thấy doanh thu dài hạn | Huy động vốn, nghĩa vụ xây dựng và tập trung khách hàng | Biên lợi nhuận hợp đồng, tài sản đảm bảo, điều khoản hủy và tín dụng |
| Lượng sử dụng AI bùng nổ | Tăng trưởng cấu trúc của tổng nhu cầu bán dẫn | Độ co giãn doanh thu USD chậm lại nhờ cải thiện hiệu suất | Tốc độ tăng lượng sử dụng so với tốc độ giảm chi phí/token |
| P/E bộ nhớ thấp | Lo ngại về đỉnh đã được phản ánh | Không rẻ vì mẫu số là EPS đỉnh (peak EPS) | Đáy lợi nhuận và thời gian duy trì FCF |
| SOXX lao dốc mạnh | Sự tách rời tạm thời giữa ngành và giá cổ phiếu | Lợi ích cận biên của tin tốt đã biến mất | EPS revision và khả năng giành lại đường MA50 |

---

## 25. Bản đồ Bull / Bear theo chuỗi giá trị

| Chuỗi giá trị | Logic phe tăng giá | Logic phe giảm giá | Quan sát cốt lõi |
|---|---|---|---|
| Dẫn đầu HBM | Chứng nhận khách hàng, khoảng cách công nghệ, cơ cấu sản phẩm cao, thiếu cung | Tập trung khách hàng, đối thủ đuổi kịp, bình thường hóa phần bù giá | Yield, giá, thị phần HBM4 và sản lượng theo từng khách hàng |
| DRAM, NAND phổ thông | HBM crowding-out, nhu cầu máy chủ và eSSD, thế độc quyền nhóm | Mua trước trở về bình thường, CXMT, mở rộng công suất, độ co giãn giá | Biên độ tăng giá hợp đồng, tồn kho, bit shipment |
| Foundry node tiên tiến | Hưởng lợi từ cả ASIC AI, CPU, GPU, chi phí chuyển đổi cao | Khấu hao N2 và fab hải ngoại, quyền đàm phán của khách hàng tự thiết kế | Tỷ lệ vận hành, ASP wafer, biên lợi nhuận theo từng node |
| Đóng gói tiên tiến, OSAT | Thiếu hụt nhóm CoWoS, mở rộng chiplet và gói lớn | Nút thắt được nới lỏng sau khi mở rộng công suất, khách hàng tự làm nội bộ | Backlog đơn hàng, lượng thiết bị đưa vào, giá trị mỗi gói |
| AI fabless | Tăng trưởng compute AI và chu kỳ sản phẩm | ASIC tự phát triển, tập trung khách hàng, thất bại thiết kế | Design win, con hào phần mềm, chuyển đổi doanh thu |
| Quang học, mạng | Băng thông scale-out/across tăng vọt | Thay đổi tiêu chuẩn, tự làm nội bộ, cạnh tranh, điều chỉnh tồn kho | Tốc độ cổng, ASP, sản xuất hàng loạt theo từng khách hàng |
| Thiết bị, kiểm tra | Hưởng lợi cấp hai từ CAPEX bộ nhớ và foundry | Đơn hàng pull-in, khoảng trống CAPEX, book-to-bill đạt đỉnh | Backlog đơn hàng, tỷ lệ hủy, CAPEX khách hàng |
| Vật liệu, substrate | Thông số cao, độ tinh khiết cao, thời gian kiểm định, mở rộng BOM | Khách hàng đa nguồn cung, mở rộng công suất, biến động nguyên liệu | Tỷ trọng doanh thu hướng AI, chuyển giá, qualification |
| Neocloud | Compute là hàng hóa độc lập, khan hiếm điện năng và mặt bằng | Đòn bẩy tài chính, giá trị còn lại của GPU, tập trung khách hàng | Lãi vay/EBITDA, tỷ lệ vận hành, FCF sau CAPEX |
| Hyperscaler | Tăng trưởng doanh thu AI, quảng cáo, cloud, khả năng tiếp cận vốn | CAPEX, khấu hao, FCF bị bào mòn | Lợi nhuận gộp AI, FCF, nợ vay và thuê tài chính |

<strong>Chất lượng tương đối</strong>: trục có chất lượng cao nhất là các nhà dẫn đầu đã được kiểm chứng về HBM, node tiên tiến, đóng gói tiên tiến. Tuy nhiên kỳ vọng đã cao nên timing risk lớn. Trục nhạy cảm với chu kỳ kinh tế cao là DRAM, NAND phổ thông và thiết bị, kiểm tra. Trục có rủi ro tài chính lớn là neocloud có đòn bẩy cao và trung tâm dữ liệu tập trung khách hàng. Trục có tính optionality lớn là sự phục hồi của foundry Samsung và các design win mới về quang học, vật liệu, những trục này nên được coi là quyền chọn miễn phí cho đến khi có đơn hàng thực tế.

---

## 26. Những lập luận yếu cần loại bỏ

Đây là những lập luận cả hai phía đều thường xuyên sử dụng nhưng không vượt qua được kiểm chứng.

<strong>Lập luận tăng giá yếu</strong>

| Lập luận | Vì sao sai |
|---|---|
| "AI mới 4 tuổi nên bộ nhớ chắc chắn sẽ tăng" | Nhu cầu cuối dài hạn và lợi nhuận vượt trội của nhà cung cấp hiện tại không phải là một |
| "CAPEX tăng thì mọi loại bán dẫn đều tăng" | CAPEX bao gồm cả đất, nhà xưởng, điện năng, thuê tài chính, và việc nắm bắt giá trị khác nhau theo từng sản phẩm, khách hàng |
| "P/E thấp thì chắc chắn rẻ" | Nếu mẫu số là peak EPS thì P/E thấp vẫn có thể là bình thường |
| "Có LTA nên giá và sản lượng được đảm bảo" | Cần kiểm tra điều khoản hợp đồng và tín dụng của khách hàng |
| "CXMT công nghệ kém nên có thể bỏ qua" | Rủi ro ngắn hạn với HBM thấp nhưng vẫn quan trọng với giá trần DRAM phổ thông |
| "Công ty tốt thì giá và tỷ trọng không quan trọng" | Dù chất lượng cao, rủi ro de-rating và mức độ tập trung vẫn còn đó |

<strong>Lập luận giảm giá yếu</strong>

| Lập luận | Vì sao sai |
|---|---|
| "Nhu cầu AI là giả" | Mâu thuẫn với đơn hàng chính thức, CAPEX và tình trạng thiếu cung |
| "Đỉnh 4Q26 nghĩa là giá sắp giảm" | Đỉnh của mức giá và đỉnh của tốc độ tăng giá là hai việc khác nhau |
| "CXMT sắp thay thế HBM" | Bỏ qua thời gian cần thiết cho yield, đóng gói, chứng nhận khách hàng |
| "ASIC tự phát triển sẽ xóa sổ nhu cầu bộ nhớ" | ASIC cũng tiêu thụ node tiên tiến và bộ nhớ, mạng hiệu năng cao |
| "Dead cross xác nhận ngành đã kết thúc" | Chỉ báo kỹ thuật đi sau, cần nhìn cùng lúc với xu hướng dài hạn và EPS |
| "RPO và Take-or-Pay hoàn toàn là ảo tưởng" | Khả năng nhìn thấy hợp đồng thực tế vẫn tồn tại, vấn đề nằm ở biên lợi nhuận và cấu trúc huy động vốn |

---

## 27. Kịch bản tổng hợp

Các xác suất dưới đây không phải là tần suất lịch sử mà là ước tính phán đoán tại thời điểm ngày 17/7/2026. \[Suy luận: ước tính kịch bản\]

| Xác suất | Kịch bản | Ngành | Lợi nhuận | Giá cổ phiếu | Điều kiện cốt lõi |
|---:|---|---|---|---|---|
| 25% | Tái khởi động tăng giá cấu trúc / bear trap | Nhu cầu AI và nút thắt tiếp diễn | Duy trì nâng EPS và biên lợi nhuận cao | SOXX phục hồi về 565-590 rồi tiếp tục xu hướng | Tỷ lệ vận hành, doanh thu AI, FCF bắt kịp CAPEX |
| <strong>55%</strong> | <strong>Fundamental Bull / Valuation Bear</strong> | Nhu cầu tăng trưởng | Lợi nhuận cao nhưng mức độ nâng chậm lại | Điều chỉnh dài, đi ngang, luân chuyển vai trò dẫn dắt | Phản ứng cung và khấu hao giới hạn multiple |
| 20% | Hard cycle bear | Đơn hàng trì hoãn, nhu cầu chậm lại | Giá và EPS hạ xuống | Phá đáy cũ và giảm rủi ro toàn diện | Tồn kho mua trước + CAPEX phanh lại + cung tăng |

Xác suất cao nhất là <strong>sự pha trộn giữa ngành bull và giá cổ phiếu valuation bear</strong>. Trong trường hợp này, tổn thất của nhà đầu tư đến từ <strong>thời gian và chi phí cơ hội</strong> nhiều hơn là từ sự sụp đổ lợi nhuận.

---

## 28. Cổng chuyển đổi: điều gì xuất hiện thì cần thay đổi phán đoán

Một chỉ báo đơn lẻ là không đủ. Chỉ thay đổi hướng phán đoán khi <strong>từ hai trục khác nhau trở lên</strong> được xác nhận.

<strong>Bull củng cố (từ hai trục trở lên)</strong>

1. Hyperscaler nâng CAPEX đồng thời với lợi nhuận gộp AI, cloud cùng tăng
2. Cải thiện điện năng đấu nối, tỷ lệ vận hành trung tâm dữ liệu, tỷ lệ sử dụng GPU
3. Giá HBM, DRAM và 12MF EPS của Samsung Electronics, SK Hynix, Micron tiếp tục được nâng lên
4. SOXX phục hồi về 565-590 và sức mạnh tương đối so với SPY đảo chiều

<strong>Valuation Bear duy trì</strong>

- Kết quả kinh doanh tốt nhưng mức độ nâng EPS chậm lại
- Mức giá DRAM vẫn cao nhưng tốc độ tăng chậm lại
- CAPEX được duy trì nhưng FCF và biên lợi nhuận suy yếu
- SOXX đi ngang trong vùng 470-565 và các ngành khác có ưu thế tương đối

<strong>Hard Bear nâng cấp (từ hai trục trở lên)</strong>

1. Hyperscaler cắt CAPEX, trì hoãn hợp đồng, tỷ lệ vận hành giảm
2. Tồn kho khách hàng, kênh phân phối tăng và biên độ tăng giá hợp đồng DRAM chậm lại
3. Ba hãng bộ nhớ chuyển sang hạ 12MF EPS
4. SOXX phá vỡ 520 rồi thất bại khi giành lại 565, lan rộng ra toàn thị trường

<strong>Bear suy yếu</strong>

- Sau Rush order, tồn kho không tích tụ mà được tiêu thụ bằng nhu cầu sử dụng thực tế
- Giá, yield và sản lượng HBM4 được duy trì, sự gia nhập của đối thủ được hấp thụ bởi tăng trưởng thị trường
- Tăng trưởng doanh thu và dòng tiền AI vượt qua khấu hao và chi phí lãi vay
- Chênh lệch tín dụng trái phiếu doanh nghiệp và mức độ tín nhiệm ổn định trong khi CAPEX được duy trì

---

## 29. Sổ cái bằng chứng: tin theo hạng nào cho từng luận điểm

Phần này công khai độ tin cậy của phân tích theo từng nguồn tư liệu. Nguyên tắc là không tạo ra sự tin tưởng cao từ tư liệu có hạng thấp.

| Luận điểm | Nguồn | Hạng | Độ tin cậy | Giới hạn |
|---|---|---|---|---|
| TSMC nâng tăng trưởng FY26, CAPEX 60-64 tỷ USD | Tài liệu cuộc gọi 2Q26, đối chiếu nhiều báo cáo nghiên cứu | B | medium-high | Tiếp cận trực tiếp văn bản IR chính thức bị hạn chế một phần |
| Giới hạn bộ nhớ của Dell, HPE, phản ứng của Cisco | Tài liệu quiet-period của JPM | C/B | medium | broker channel check, không phải công bố chính thức của công ty |
| Rush order DRAM máy chủ | Tài liệu của BofA | C/B | medium | Tiếp cận công khai văn bản gốc báo cáo bị hạn chế |
| CAPEX, OCF, nợ vay của Oracle | SEC 10-K (FY2026) | <strong>A</strong> | high | Trường hợp dễ tổn thương hơn so với hyperscaler dồi dào tiền mặt |
| Mua trước và trì hoãn hợp đồng của khách hàng IBM | SEC 8-K (14/7/2026) | <strong>A</strong> | high | Không thể tổng quát hóa trường hợp riêng của IBM cho toàn ngành CNTT |
| Doanh thu, CAPEX, lãi vay, tập trung khách hàng của CoreWeave | Hồ sơ SEC (1Q26) | <strong>A</strong> | high | Trường hợp dễ tổn thương của neocloud, cấu trúc khác Big Tech |
| CAPEX 801 tỷ USD của 3 công ty năm 2027 theo Citi | Citi mega-cap preview | C/B | medium | Ước tính mang tính tấn công, không phải hướng dẫn của công ty |
| Đỉnh tốc độ tăng giá bộ nhớ 4Q26 | Biểu đồ, trích dẫn gián tiếp từ Morgan Stanley | C | low-medium | Chưa kiểm chứng định nghĩa giá và giả định gốc |
| Huy động vốn và dư địa mở rộng cung của CXMT | Đối chiếu thông báo phát hành và kết quả đặt mua | B | medium-high | Có độ trễ đến khi có công suất, yield, chứng nhận khách hàng thực tế |
| Xuất khẩu bán dẫn Hàn Quốc và HBM proxy | Số liệu tạm tính 1-10/7 của Tổng cục Hải quan | A/B | Tổng số high, proxy medium | Không thể quy thuộc HBM theo từng công ty |
| SOXX giảm khoảng -19% so với đỉnh | Đối chiếu Yahoo/TradingView | B+ | high | Không phải giá trị gốc chính thức từ sàn giao dịch |

<strong>Chưa xác minh (Blocked)</strong>: điều kiện kinh tế chi tiết của LTA, giá, sản lượng, yield HBM4 theo từng khách hàng, lượng wafer mới thực tế của CXMT, khả năng sinh lời khối lượng công việc AI của từng hyperscaler riêng lẻ.

---

## 30. Những điều cần xác nhận tiếp theo

<strong>Kết quả kinh doanh, công bố thông tin</strong>

1. Alphabet, Meta, Amazon: cần nhìn <strong>lợi nhuận gộp AI, khấu hao, FCF, nợ vay và thuê tài chính mới</strong> hơn là CAPEX
2. SK Hynix, Samsung Electronics, Micron: xuất xưởng, yield, giá HBM4, tăng trưởng bit DRAM phổ thông, cấu trúc LTA, revision EPS FY2027
3. TSMC: pha loãng biên lợi nhuận từ N2 và fab hải ngoại, công suất đóng gói tiên tiến, kiểm chứng đơn hàng khách hàng và tỷ lệ vận hành thực tế
4. CXMT: phân bổ vốn huy động từ IPO, đặt hàng thiết bị fab mới, yield DDR5, chứng nhận khách hàng, lịch trình HBM

<strong>Dữ liệu hàng tháng, hàng tuần</strong>

1. Biên độ tăng giá hợp đồng DRAM và tồn kho khách hàng, kênh phân phối
2. Số liệu chính thức cuối tháng của xuất khẩu bán dẫn Hàn Quốc và HBM proxy
3. Delta revision 12MF EPS của ba hãng bộ nhớ
4. Vùng 520, 565, 590 của SOXX và sức mạnh tương đối so với SPY
5. Chênh lệch trái phiếu doanh nghiệp của hyperscaler và chi phí huy động vốn của neocloud

---

## Kết luận: từ scarcity cycle sang capital-intensity cycle

Căn cứ mạnh nhất của phe tăng giá ngành bán dẫn là nhu cầu AI có thực, nhu cầu đó đang lan ra thành nút thắt vật lý ở bộ nhớ, node tiên tiến, đóng gói và mạng, còn giá trị thời gian của nguồn cung và chứng nhận khách hàng tạo ra rào cản gia nhập.

Căn cứ mạnh nhất của phe giảm giá ngành bán dẫn là nhu cầu thực đó đã đẩy giá và CAPEX tăng vọt, và ở giai đoạn tiếp theo, việc mua trước trở về bình thường, phản ứng cung, khấu hao và chi phí vốn có thể đồng thời đè nén biên lợi nhuận và multiple.

Khi gộp cả hai lại, kết luận hội tụ về một điểm. <strong>Ngành bán dẫn AI vẫn chưa sụp đổ. Nhưng scarcity cycle đang dịch chuyển sang capital-intensity cycle.</strong> Đợt tăng tiếp theo sẽ không bắt đầu từ công bố CAPEX, mà bắt đầu khi điện năng đấu nối, tỷ lệ vận hành và dòng tiền AI đuổi kịp khấu hao và chi phí vốn.

Vì vậy thái độ hợp lý nhất lúc này là không từ bỏ luận điểm ngành dài hạn, nhưng <strong>quản lý riêng biệt thời điểm mua bán cổ phiếu và mức độ tập trung danh mục</strong>. Không đổi hướng chỉ vì một tín hiệu duy nhất, mà chỉ hành động khi có từ hai trục khác nhau trở lên được xác nhận. Theo xác suất hiện tại, con đường trung tâm là <strong>Fundamental Bull / Valuation Bear</strong>, nơi tăng trưởng cấu trúc của ngành cùng tồn tại với đợt điều chỉnh định giá kéo dài của giá cổ phiếu.

---

_Bài viết này tổng hợp công bố thông tin chính thức (SEC, Tổng cục Hải quan), dữ liệu thị trường và tài liệu kịch bản của các broker, để triển khai luận điểm tăng giá và luận điểm giảm giá ngành bán dẫn dưới hình thức mạnh nhất của mỗi bên, sau đó hội tụ về các biến số có thể quan sát được. Hạng độ tin cậy theo từng tư liệu đã được nêu rõ trong bài viết. Số liệu từ cuộc gọi của TSMC là giá trị đối chiếu chéo với khả năng tiếp cận trực tiếp văn bản IR chính thức bị hạn chế một phần, còn ước tính CAPEX của Citi và thời điểm đỉnh của Morgan Stanley không phải là hướng dẫn của công ty. Xác suất kịch bản là ước tính phán đoán tại thời điểm viết bài, không phải tần suất lịch sử. Các cổ phiếu được đề cập chỉ là ví dụ minh họa cấu trúc ngành, không phải khuyến nghị mua bán một cổ phiếu cụ thể nào. Phán đoán đầu tư và trách nhiệm thuộc về chính nhà đầu tư._

---

### Bài viết liên quan

- [Vì sao việc IBM lỡ kỳ vọng lợi nhuận lại là bằng chứng cho sức mạnh của bộ nhớ: đọc IBM và Ericsson để hiểu tâm lý ngành bán dẫn](/vi/post/ibm-ericsson-q2-memory-cost-evidence-semiconductor-sentiment-2026-07-14/)
- [Khoảng trống nguồn cung lan ra ngoài HBM: đọc ba báo cáo Hana Securities như một câu chuyện](/vi/post/memory-supply-gap-spillover-substrate-essd-legacy-hana-three-reports-2026-07-14/)
- [Nghiên cứu chuyên sâu cung-cầu HBM 2030: mổ xẻ mô hình cầu 26,7EB đối chiếu với lịch trình mở rộng công suất](/vi/post/hbm-2030-supply-demand-267eb-demand-model-crosscheck-2026-07-13/)
- [Ai trả tiền cho đồng thuận bán dẫn năm 2027: Samsung, Hynix, Micron, Nvidia nhìn từ khả năng chi trả của hyperscaler](/vi/post/semiconductor-2027-earnings-hyperscaler-payability-memory-nvidia-2026-06-21/)
- [Samsung Electronics và SK Hynix có thực sự bị bán quá mức so với đồng thuận 2027? Kịch bản xấu nhất đã nằm trong giá](/vi/post/samsung-hynix-worst-case-eps-priced-in-consensus-dispersion-2026-07-10/)
