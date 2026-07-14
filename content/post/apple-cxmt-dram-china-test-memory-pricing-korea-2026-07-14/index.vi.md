---
title: "Apple Có Thực Sự Dùng CXMT Không? Kiểm Thử Bộ Nhớ Chỉ Dành Cho Trung Quốc và Rủi Ro Giá Đối Với Các Nhà Sản Xuất DRAM Hàn Quốc"
date: 2026-07-14T22:10:00+09:00
description: "Kiểm chứng thông tin về các bài kiểm thử DRAM CXMT của Apple trên các khía cạnh công nghệ, chi phí, quy định và rủi ro chuỗi cung ứng. Con đường khả thi nhất là sử dụng hạn chế trên các thiết bị tiêu chuẩn bán tại Trung Quốc, trong khi đòn bẩy đàm phán có thể quan trọng hơn sản lượng trực tiếp."
categories: ["Phân Tích Độc Quyền", "Bán Dẫn", "Kiểm Chứng Thông Tin"]
tags: ["Apple", "CXMT", "LPDDR5X", "DRAM Di Động", "Samsung Electronics", "SK Hynix", "Micron", "HBM", "Kiểm Soát Bán Dẫn Mỹ-Trung"]
series: ["exclusive-analysis", "ai-hbm-2026"]
slug: "apple-cxmt-dram-china-test-memory-pricing-korea-2026-07-14"
valley_cashtags: ["Samsung Electronics", "SK Hynix", "Apple", "Micron"]
draft: false
---

Theo các báo cáo, Apple đang kiểm thử DRAM do ChangXin Memory Technologies, hay CXMT, sản xuất cho các thiết bị bán tại Trung Quốc. Chưa có hợp đồng cung ứng nào được công bố. Hai thực tế này cần được đọc cùng nhau: CXMT đã bước vào quy trình chứng nhận của Apple, nhưng chưa trở thành nhà cung cấp bộ nhớ chính cho iPhone hay Mac trên toàn cầu.

> Bối cảnh: Đây là bài viết tiếp nối [IPO của CXMT và rủi ro giá bộ nhớ](/post/cxmt-ipo-memory-price-risk-hbm-client-dram-2026-06-21/). Báo cáo đó lập luận rằng năng lực sản xuất của CXMT có khả năng kìm hãm giá client DRAM và LPDDR trước khi tác động đến HBM. Bài viết này phân tích cách một nhà mua lớn như Apple có thể khai thác nguồn cung mới nổi đó. Các tuyển tập liên quan gồm [AI HBM Hub](/page/korea-semiconductor-hbm-kospi-hub/) và [Exclusive Analysis Hub](/page/exclusive-analysis-hub/).

## TL;DR

* Apple có thể sẽ chứng nhận CXMT như một nhà cung cấp thương mại. Bước đầu tiên khả thi nhất là sản lượng hạn chế trên các thiết bị tiêu chuẩn bán tại Trung Quốc. Khả năng chuyển nhanh sang các sản phẩm flagship toàn cầu vẫn còn thấp.
* Thông số kỹ thuật LPDDR5X công khai của CXMT đủ điều kiện để bắt đầu chứng nhận. Các sản phẩm 8.533Mbps và 9.600Mbps đã vào sản xuất hàng loạt, trong khi phiên bản 10.667Mbps vẫn còn trong giai đoạn lấy mẫu khách hàng. Mức tiêu thụ điện, nhiệt độ, độ dày gói, tỷ lệ lỗi, độ tin cậy dài hạn và năng suất sản lượng lớn đạt chuẩn Apple vẫn chưa được công bố.
* Mức chiết khấu giá bán trung bình được báo cáo từ 5% đến 10% chưa giải quyết được bài toán kinh tế. Ước tính đó áp dụng cho toàn bộ danh mục DRAM hỗn hợp của CXMT, không phải báo giá LPDDR5X riêng dành cho Apple. Chi phí danh sách vật liệu kép, tách biệt tồn kho, chứng nhận và rủi ro thay thế theo quy định làm giảm khoản tiết kiệm thực tế.
* Đòn bẩy đàm phán có thể quan trọng hơn sản lượng trực tiếp. Một nhà cung cấp thứ tư có khả năng thực hiện đơn đặt hàng thương mại có thể tạo áp lực lên Samsung, SK Hynix và Micron trên toàn bộ sổ thu mua DRAM lớn hơn nhiều của Apple.
* Áp lực cạnh tranh ngắn hạn của CXMT tập trung vào DRAM di động và client, không phải HBM tiên tiến. Coi báo cáo này là tiêu cực toàn diện cho mọi cổ phiếu bộ nhớ là bỏ qua cơ cấu sản phẩm.
* Đánh giá theo sự kiện là Theo Dõi đối với SK Hynix, Chờ Đợi đối với Samsung Electronics và Chờ Đợi đối với Apple. Bằng chứng hiện tại hỗ trợ kiểm thử và vận động hành lang, không phải hợp đồng, sản phẩm, sản lượng hay thời hạn đã được công bố.

## 1. Những Gì Được Xác Nhận và Những Gì Chưa

### 1.1 Kiểm Thử Được Báo Cáo; Hợp Đồng Thì Chưa

Financial Times đưa tin Apple đang kiểm thử DRAM của CXMT cho các thiết bị bán tại Trung Quốc. Các báo cáo trước đó cho biết Apple đã yêu cầu làm rõ về mặt pháp lý từ chính phủ Mỹ. Apple, Nhà Trắng và CXMT đều không phản hồi yêu cầu bình luận của Reuters vào thời điểm đó.

| Câu hỏi | Đánh giá tính đến ngày 14/7/2026 | Mức độ bằng chứng |
|---|---|---|
| Apple có đang kiểm thử DRAM CXMT không? | Được báo cáo cho các thiết bị thị trường Trung Quốc | Báo cáo thứ cấp đáng tin cậy |
| Hợp đồng cung ứng đã được ký chưa? | Chưa xác nhận | Chặn |
| Sản phẩm nào liên quan? | Không xác định được iPhone, iPad hay Mac | Chặn |
| Chip có được sử dụng ngoài Trung Quốc không? | Không có bằng chứng hỗ trợ | Không suy luận |
| Chính phủ Mỹ có chấp thuận việc sử dụng không? | Theo báo cáo, sự rõ ràng về pháp lý đã được yêu cầu | Không có quyết định chính thức |
| Phân bổ cho các nhà cung cấp hiện tại có bị giảm không? | Chưa xác nhận | Chặn |

Cách diễn đạt chính xác là Apple đang chứng nhận CXMT như một nhà cung cấp tiềm năng, không phải Apple đã chính thức áp dụng nó. [Tin tức Reuters](https://www.marketscreener.com/news/apple-seeks-approval-to-buy-chips-from-blacklisted-chinese-company-ft-reports-ce7f5fd9d08df72d), [tóm tắt báo cáo kiểm thử](https://www.macrumors.com/2026/07/08/apple-begins-testing-controversial-chinese-memory/)

### 1.2 CXMT Không Còn Là Nhà Sản Xuất Thử Nghiệm

Counterpoint Research ước tính thị phần doanh thu DRAM toàn cầu của CXMT ở mức khoảng 8% trong Q1/26, xếp thứ tư sau Samsung, SK Hynix và Micron. Các con số thị phần khác nhau tùy theo mẫu số là doanh thu, lô bit hay đầu vào wafer, nhưng xu hướng rõ ràng: CXMT không còn là nhà cung cấp nhỏ ở quy mô phòng thí nghiệm nữa. [Counterpoint Research](https://counterpointresearch.com/en/insights/global-dram-revenue-surges-to-near-dollar-100-billion-mark-in-q1-2026)

Quy mô không chứng minh được độ trưởng thành đạt chuẩn Apple. Cung cấp DRAM thông dụng cho các khách hàng Trung Quốc lớn không thiết lập được mức tiêu thụ điện, độ tin cậy và năng suất cần thiết trong các thiết bị cao cấp của Apple.

## 2. Hiệu Suất: Chứng Nhận Khó Hơn Đạt Tốc Độ Tiêu Đề

CXMT cho biết danh mục LPDDR5X của họ bao gồm các die 12Gb và 16Gb, gói 12GB, 16GB và 24GB, và tốc độ dữ liệu lên đến 10.667Mbps. Các sản phẩm 8.533Mbps và 9.600Mbps đã vào sản xuất hàng loạt vào tháng 5/2025; phiên bản 10.667Mbps vẫn còn trong giai đoạn lấy mẫu khách hàng. [Thông báo của CXMT](https://www.cxmt.com/en/news/info_19.html)

| Hạng mục | Tình trạng đã xác nhận | Diễn giải đầu tư |
|---|---|---|
| Mật độ die | 12Gb và 16Gb | Đáp ứng yêu cầu di động và PC cấp cơ bản |
| Dung lượng gói | 12GB, 16GB và 24GB | Hỗ trợ các cấu hình thiết bị tiêu chuẩn |
| Tốc độ dữ liệu | 8.533, 9.600 và 10.667Mbps | Linh kiện tốc độ cao nhất vẫn còn trong giai đoạn lấy mẫu |
| Tiêu thụ điện | CXMT tuyên bố tiết kiệm 30% so với LPDDR5 của họ | Không phải so sánh tương đương với ba nhà sản xuất lớn |
| Chứng nhận Apple | Chưa tiết lộ | Không thể xác nhận việc áp dụng thương mại |
| Năng suất sản lượng lớn | Chưa tiết lộ | Không thể xác nhận cung cấp hàng chục triệu đơn vị |

Thông số kỹ thuật công khai bác bỏ luận điểm rằng DRAM Trung Quốc tự động quá chậm cho Apple. Các điểm tắc nghẽn thực sự là tiêu thụ điện năng ở chế độ chờ và làm mới, độ ổn định nhiệt, độ dày gói, tỷ lệ lỗi, biến động giữa các lô, độ tin cậy dài hạn, năng suất sản lượng lớn và tích hợp với bộ xử lý và firmware quản lý nguồn điện của Apple.

CXMT đã giành được chỗ trong quy trình chứng nhận. Bằng chứng công khai chưa cho thấy họ có thể duy trì chất lượng đạt chuẩn Apple ở quy mô lớn.

## 3. Giá: Chiết Khấu 5% đến 10% Không Giải Quyết Được Bài Toán Kinh Tế

SemiAnalysis ước tính rằng giá bán trung bình DRAM tổng hợp của CXMT trong Q1/26 thấp hơn khoảng 5% đến 10% so với bộ ba hiện tại, trong khi chi phí mỗi bit DDR5 của họ có thể cao hơn 30%. Đây là ước tính sản phẩm hỗn hợp trên toàn công ty, không phải báo giá LPDDR5X riêng cho Apple. [SemiAnalysis](https://newsletter.semianalysis.com/p/chinas-cxmt-is-set-to-challenge-dram)

| Chi phí bổ sung | Gánh nặng đối với Apple |
|---|---|
| Tách biệt chuỗi cung ứng Trung Quốc và toàn cầu | Số bộ phận, kế hoạch lắp ráp và logistics riêng biệt |
| Tồn kho kép | Không khớp nhu cầu theo khu vực và vòng quay chậm hơn |
| Kỹ thuật chứng nhận | Xác nhận bộ xử lý, firmware và nhiệt lặp lại |
| Rủi ro thay thế theo quy định | Chuyển đổi nhà cung cấp khẩn cấp và tái chứng nhận |
| Lỗi chất lượng | Bảo hành, thu hồi và thiệt hại thương hiệu |

Mức chiết khấu danh nghĩa thu hẹp lại sau các chi phí này. Giá của CXMT cũng không nên được hiểu là bằng chứng về năng lực dẫn đầu chi phí có cấu trúc. Hỗ trợ nhà nước, yêu cầu biên lợi nhuận thấp hơn, cơ cấu sản phẩm và chiến lược thị trường trong nước có thể đóng góp vào điều này.

## 4. Đòn Bẩy Đàm Phán Có Thể Quan Trọng Hơn Sản Lượng

Lợi ích kinh tế của Apple không chỉ giới hạn ở mức chiết khấu trên chip mua từ CXMT. Chứng nhận một nhà cung cấp thứ tư có khả năng thực hiện đơn đặt hàng thương mại thực sự có thể ảnh hưởng đến giá của toàn bộ sổ thu mua DRAM của Apple.

```text
Duy trì chứng nhận CXMT
→ cho phép một đơn đặt hàng sản xuất nhỏ
→ chứng minh năng lực chuyển đổi đáng tin cậy
→ hạn chế tăng giá hợp đồng từ bộ ba hiện tại
```

Hiệu ứng này có thể xuất hiện trước khi CXMT giành được thị phần đáng kể. Một phân bổ nhỏ loại bỏ giả định của các nhà cung cấp hiện tại rằng Apple không có lựa chọn nào khác.

Chỉ mẫu thôi là không đủ. Lựa chọn này chỉ trở nên đáng tin cậy khi CXMT có thể cung cấp sản lượng thương mại tối thiểu vào một sản phẩm đang xuất xưởng. Nếu không có hợp đồng và sẵn sàng chuyển đổi, các nhà cung cấp hiện tại có ít lý do để thay đổi giá của họ.

## 5. Quy Định: Khả Năng Mua Hợp Pháp và An Ninh Cung Ứng Nhiều Năm Là Khác Nhau

### 5.1 Chỉ Định Section 1260H Không Tự Động Cấm Các Giao Dịch Thương Mại Thông Thường

Bộ Quốc phòng Mỹ đã đưa CXMT vào danh sách Section 1260H về các công ty quân sự Trung Quốc ngày 8/6/2026. Việc phân loại này tạo ra rủi ro hợp đồng chính phủ và an ninh quốc gia, nhưng không phải là lệnh cấm toàn diện đối với mọi giao dịch thương mại tư nhân thông thường. [Thông cáo của Bộ Quốc phòng Mỹ](https://www.war.gov/News/Releases/Release/Article/4511232/dow-releases-list-of-chinese-military-companies-in-accordance-with-section-1260/)

### 5.2 Rủi Ro Entity List Quan Trọng Nhất Thông Qua Sự Liên Tục Sản Xuất

Reuters đưa tin rằng một ủy ban liên ngành đã chấp thuận việc thêm CXMT vào Entity List, nhưng việc công bố vẫn bị hoãn đến giữa tháng 6/2026. Việc đưa vào Entity List sẽ áp đặt các hạn chế cấp phép nghiêm ngặt đối với xuất khẩu, tái xuất khẩu hoặc chuyển giao thiết bị, phần mềm, công nghệ và hỗ trợ của Mỹ cho CXMT. Mua chip DRAM thành phẩm là hành vi pháp lý khác với việc xuất khẩu công nghệ Mỹ cho nhà sản xuất.

Hệ quả thương mại vẫn còn lớn. Hạn chế phụ tùng thay thế, cập nhật phần mềm và hỗ trợ kỹ thuật có thể làm suy giảm năng suất, công suất và chuyển đổi quy trình. Apple cần sự liên tục cung ứng nhiều năm, không chỉ là khả năng thực hiện một giao dịch mua hàng ngày hôm nay. [Báo cáo Reuters về sự trì hoãn](https://www.investing.com/news/stock-market-news/us-holds-off-on-adding-deepseek-cxmt-to-trade-blacklist-reuters-reports-4746250)

### 5.3 Hạn Chế Thu Mua Liên Bang 2027 Không Phải Là Lệnh Cấm Người Tiêu Dùng

Một Quy định Thu mua Liên bang được đề xuất sẽ thực hiện các hạn chế từ ngày 23/12/2027 đối với việc mua sắm của các cơ quan liên bang đối với các sản phẩm và dịch vụ điện tử chứa chip được bao phủ từ CXMT, YMTC và SMIC. Nó không cấm người tiêu dùng thông thường mua iPhone. Tuy nhiên, nó có thể buộc Apple duy trì các cấu hình không có CXMT riêng cho các kênh chính phủ và một số doanh nghiệp. Đề xuất bao gồm ngoại lệ đến ngày 23/12/2028 cho các sản phẩm thương mại không có lựa chọn thay thế. [Quy tắc FAR được đề xuất](https://public-inspection.federalregister.gov/2026-03065.pdf)

### 5.4 YMTC Là Tiền Lệ Chính Trị Có Liên Quan

Apple đã khám phá việc sử dụng NAND của YMTC vào năm 2022 nhưng đã gác lại kế hoạch sau khi Quốc hội phản đối và các hạn chế thắt chặt hơn. CXMT không ở trong vị trí pháp lý tương tự ngày nay, nhưng sự kiện đó cho thấy áp lực chính trị có thể làm gián đoạn một kế hoạch tìm nguồn cung ứng khả thi về mặt kỹ thuật.

## 6. Con Đường Khả Thi Nhất: Sử Dụng Hạn Chế Trên Các Thiết Bị Tiêu Chuẩn Bán Tại Trung Quốc

Các mẫu tiêu chuẩn chỉ dành cho Trung Quốc mang lại sự thỏa hiệp giữa kỹ thuật, kinh tế và chính trị.

| Biến số | Áp dụng hạn chế thị trường Trung Quốc | Áp dụng chính toàn cầu |
|---|---|---|
| Chứng nhận | Sản phẩm tiêu chuẩn có thể được kiểm thử trước | Xác nhận lâu dài trên các sản phẩm cao cấp |
| Rủi ro pháp lý | Có thể tách biệt khỏi các kênh chính phủ Mỹ | Xung đột trong bán hàng cho chính phủ và doanh nghiệp |
| Vận hành chuỗi cung ứng | Danh sách vật liệu Trung Quốc riêng biệt | Mất tính đồng nhất toàn cầu lớn hơn |
| Sản lượng | Hạn chế | Hàng chục triệu thiết bị |
| Gánh nặng chính trị | Có thể quản lý được | Đối lập và rủi ro trừng phạt từ Mỹ lớn hơn nhiều |
| Xác suất hiện tại | Có điều kiện | Thấp |

Bốn điều kiện phải được đáp ứng: chứng nhận độ tin cậy của Apple, năng suất và sản lượng Trung Quốc đủ, sự liên tục pháp lý trong suốt hợp đồng và lợi ích ròng lớn hơn chi phí tìm nguồn cung kép.

## 7. Dòng Vốn và Các Điểm Tắc Nghẽn

```text
Đầu tư trung tâm dữ liệu AI tăng
→ HBM và server DRAM được ưu tiên
→ nguồn cung DRAM di động và PC kém linh hoạt hơn
→ chi phí bộ nhớ của Apple tăng
→ động lực chứng nhận CXMT tăng
```

Chuỗi chạy từ thiết bị và vật liệu qua sản xuất wafer CXMT, đóng gói và kiểm tra LPDDR5X, chứng nhận Apple, lắp ráp thiết bị và phân phối tại Trung Quốc. Bốn điểm tắc nghẽn là chất lượng và năng suất đạt chuẩn Apple, độ bền pháp lý, chi phí cấu hình khu vực riêng biệt và khả năng tiếp cận thiết bị và hỗ trợ kỹ thuật Mỹ của CXMT.

## 8. Tác Động Lên Ngành Bộ Nhớ: Tách Biệt HBM Khỏi DRAM Di Động

Vị trí cạnh tranh hiện tại của CXMT gần với DDR5 và LPDDR hơn là HBM tiên tiến. Suy diễn từ bài kiểm thử của Apple sang sự sụp đổ của toàn bộ nhóm lợi nhuận DRAM là bỏ qua kinh tế học sản phẩm.

| Công ty | Rủi ro trực tiếp từ CXMT | Biến số quan trọng hơn |
|---|---|---|
| Samsung Electronics | Áp lực giá LPDDR và thị phần tiềm năng tại Apple | Chứng nhận HBM, cơ cấu hàng hóa, thua lỗ xưởng đúc |
| SK Hynix | Một số rủi ro di động, nhưng phần lớn hơn của luận điểm cốt lõi đến từ HBM | Năng suất HBM4, thị phần, ASP và capex AI |
| Micron | Áp lực DRAM di động và PC tiềm năng | Server DRAM, tăng tốc HBM, thỏa thuận dài hạn |
| Apple | Chi phí thu mua thấp hơn và đa dạng hóa nhà cung cấp | Chi phí BOM kép, quy định, tổng biên lợi nhuận gộp |
| CXMT | Chứng nhận Apple sẽ cải thiện uy tín toàn cầu | Năng suất, chi phí, tiếp cận thiết bị, an ninh pháp lý |

Nhiều công suất di động hơn của CXMT có thể khuyến khích bộ ba hiện tại phân bổ nhiều vốn hơn cho HBM và server DRAM. Điều đó sẽ tạo áp lực lên giá hàng hóa mà không loại bỏ các rào cản chứng nhận, năng suất xếp chồng, đóng gói và lộ trình khách hàng của HBM.

Rủi ro dài hạn là có thực. Nếu CXMT nhanh chóng cải thiện năng suất DDR5 và LPDDR5X tiên tiến và hấp thụ các cú sốc kiểm soát xuất khẩu thông qua hệ sinh thái thiết bị trong nước, dòng tiền hàng hóa của các nhà cung cấp hiện tại có thể suy yếu. Nếu sau đó đạt được năng suất HBM thương mại, ranh giới sản phẩm ngày nay sẽ bị xói mòn. Bằng chứng công khai chưa cho thấy kết quả đó.

## 9. Ba Khung Đầu Tư và Phản Biện của Chúng

### Khung 1: Áp Dụng Hạn Chế Thị Trường Trung Quốc

Phân loại: alpha sự kiện đặc thù

* Giá: giá cung CXMT thấp hơn
* Số lượng: các thiết bị được chọn bán tại Trung Quốc
* Chi phí: chứng nhận, tồn kho kép, quy định và rủi ro bảo hành

Các bên hưởng lợi bao gồm tổ chức thu mua của Apple, CXMT và chuỗi đóng gói và vật liệu của Trung Quốc. Giá DRAM di động của Apple từ các nhà cung cấp hiện tại sẽ chịu áp lực.

Phản biện: Một thỏa thuận Mỹ-Trung bền vững, bến an toàn pháp lý và chứng nhận thiết bị cao cấp có thể phá vỡ giả định chỉ dành cho Trung Quốc. Bài kiểm thử độ tin cậy thất bại sẽ vô hiệu hóa ngay cả việc áp dụng hạn chế.

### Khung 2: Tác Động Đàm Phán Xuất Hiện Trước Tác Động Thị Phần

Phân loại: alpha sự kiện đặc thù

* Giá: giá hợp đồng Apple với bộ ba hiện tại
* Số lượng: toàn bộ sổ thu mua DRAM của Apple
* Chi phí: duy trì chứng nhận CXMT

Các nhà đầu tư có thể quan sát thị phần nhà cung cấp, nhưng nhà cung cấp cận biên có thể ảnh hưởng đến giá hợp đồng từ lâu trước khi giành được thị phần lớn.

Phản biện: Dư thừa bộ nhớ sẽ buộc các nhà cung cấp hiện tại phải cắt giảm giá mà không cần CXMT. Chứng nhận Apple thất bại cũng sẽ làm cho lựa chọn này không đáng tin cậy.

### Khung 3: Rủi Ro CXMT Tập Trung Vào DRAM Di Động và Client

Phân loại: giao dịch cơ cấu sản phẩm

* Giá: trần giá DRAM di động và PC
* Số lượng: công suất CXMT và lô hàng trong nước
* Chi phí: năng suất node tiên tiến và hạn chế thiết bị Mỹ

Người mua DRAM di động và nhà cung cấp nặng về HBM là những bên hưởng lợi tương đối. Các nhà cung cấp phụ thuộc vào DRAM di động Apple hoặc tăng giá hàng hóa đối mặt với rủi ro cao hơn.

Phản biện: Tiến bộ nhanh chóng trong năng suất node tiên tiến và HBM thương mại sẽ làm yếu sự phân tách sản phẩm. Sự sụp đổ trong đầu tư trung tâm dữ liệu AI cũng sẽ loại bỏ lợi thế tương đối của HBM.

## 10. Cổng Theo Dõi Riêng Theo Cổ Phiếu

Đây là những đánh giá sự kiện có điều kiện, không phải khuyến nghị mua độc lập.

| Chứng khoán | Quan điểm | P/E hiển thị ngày 14/7/2026 | Diễn giải sự kiện |
|---|---|---:|---|
| SK Hynix | Theo Dõi | 16,97x | HBM4 và đầu tư AI quan trọng hơn rủi ro CXMT trực tiếp |
| Samsung Electronics | Chờ Đợi | 20,99x | Áp lực giá di động cần được cân nhắc so với phục hồi HBM |
| Apple | Chờ Đợi | 38,38x | iPhone, dịch vụ và tổng biên lợi nhuận gộp quan trọng hơn khoản tiết kiệm CXMT chưa được chứng minh |

Số liệu P/E là giá trị hiển thị từ [Google Finance cho Samsung](https://www.google.com/finance/quote/005930:KRX), [SK Hynix](https://www.google.com/finance/quote/000660:KRX) và [Apple](https://www.google.com/finance/quote/AAPL:NASDAQ). P/E kéo dài có thể đánh giá quá mức sự rẻ cho các công ty bộ nhớ theo chu kỳ gần đỉnh lợi nhuận.

### SK Hynix

Cổng xác nhận: Thời gian chứng nhận và sản xuất HBM4 còn nguyên vẹn, ước tính năng suất và ASP của HBM không giảm và sự suy yếu giá cổ phiếu liên quan đến CXMT xảy ra mà không có sự hạ cấp thu nhập HBM.

Vô hiệu hóa: Chậm trễ chứng nhận HBM4, đa dạng hóa khách hàng làm giảm thị phần hoặc CXMT đạt được năng suất thương mại trong server DRAM tiên tiến hoặc HBM.

### Samsung Electronics

Cổng xác nhận: Vị thế nhà cung cấp chính cho thế hệ Apple tiếp theo, việc sử dụng CXMT giới hạn ở sản lượng thị trường Trung Quốc và cải thiện năng suất HBM và chứng nhận khách hàng rõ ràng.

Vô hiệu hóa: Phân bổ thiết bị Trung Quốc nhiều năm đáng kể cho CXMT, mất đồng thời thị phần LPDDR và giá, hoặc phục hồi HBM quá chậm để bù đắp áp lực di động.

### Apple

Cổng xác nhận: Hướng dẫn biên lợi nhuận gộp giữ nguyên bất chấp lạm phát bộ nhớ, quy định cung cấp sự rõ ràng bền vững và ước tính iPhone và dịch vụ tăng độc lập với đa dạng hóa nhà cung cấp.

Vô hiệu hóa: Quy định loại bỏ lựa chọn CXMT, lạm phát bộ nhớ thúc đẩy cả tăng giá và suy yếu nhu cầu, hoặc tăng trưởng iPhone và dịch vụ chậm hơn không đủ để hỗ trợ định giá.

## 11. Bằng Chứng Sẽ Thay Đổi Luận Điểm

Bằng chứng tích cực bao gồm xác nhận nhà cung cấp chính thức của Apple, bằng chứng tháo rời chip DRAM CXMT, chứng nhận vượt ra ngoài sản phẩm thị trường Trung Quốc, bến an toàn Mỹ bền vững hoặc năng suất sản lượng lớn cho sản phẩm 10.667Mbps và thế hệ tiếp theo của CXMT.

Bằng chứng tiêu cực bao gồm kiểm thử độ tin cậy Apple thất bại, hành động Entity List làm gián đoạn hỗ trợ thiết bị, chứng nhận kết thúc mà không có hợp đồng, chi phí tìm nguồn kép vượt quá khoản tiết kiệm hoặc dư thừa DRAM loại bỏ nhu cầu của Apple đối với nhà cung cấp thứ tư.

## 12. Phân Loại Bằng Chứng

### Thực Tế

* Theo báo cáo, Apple đang kiểm thử DRAM CXMT cho các thiết bị thị trường Trung Quốc.
* Theo báo cáo, Apple đã yêu cầu sự rõ ràng pháp lý từ Mỹ liên quan đến CXMT.
* CXMT sản xuất hàng loạt LPDDR5X 8.533Mbps và 9.600Mbps và lấy mẫu sản phẩm 10.667Mbps.
* Counterpoint ước tính thị phần doanh thu DRAM toàn cầu Q1/26 của CXMT ở mức khoảng 8%.
* CXMT xuất hiện trong danh sách Section 1260H tháng 6/2026.
* Section 1260H tự nó không tự động cấm các giao dịch mua tư nhân thông thường.
* CXMT chưa được chính thức thêm vào Entity List tính đến giữa tháng 6/2026.
* Quy tắc FAR được đề xuất thực hiện hạn chế thu mua liên bang ngày 23/12/2027 đối với các bán dẫn được bao phủ.

### Suy Luận

* Sử dụng thương mại ban đầu nhiều khả năng nhất giới hạn ở các thiết bị tiêu chuẩn bán tại Trung Quốc.
* Lợi ích kinh tế lớn nhất của Apple có thể là đòn bẩy đàm phán với các nhà cung cấp hiện tại hơn là chiết khấu chip trực tiếp.
* Mối đe dọa ngắn hạn của CXMT tập trung vào DRAM di động và client hơn là HBM.
* Các cấu hình Trung Quốc và toàn cầu riêng biệt có nhiều khả năng hơn là chuyển đổi toàn cầu hoàn toàn.

### Phỏng Đoán

* Kiểm thử có liên quan đến iPhone, iPad hay Mac không
* Thời điểm ra mắt thương mại
* Sản lượng ban đầu và thời hạn hợp đồng
* Liệu Washington có cung cấp bến an toàn bền vững không

### Chặn

* Kết quả chứng nhận nội bộ của Apple
* Giá riêng của Apple và mức chiết khấu so với các nhà cung cấp hiện tại
* Mức tiêu thụ điện chuẩn Apple, độ dày gói, tỷ lệ lỗi và độ tin cậy
* Năng suất sản lượng Apple và công suất CXMT hàng tháng
* Thời hạn hợp đồng và sản lượng tối thiểu
* Thị phần và giá cấp sản phẩm chính xác của các nhà cung cấp hiện tại tại Apple

## Kết Luận

Apple có thể sử dụng CXMT, nhưng con đường duy nhất được báo cáo hiện nay là kiểm thử cho các thiết bị bán tại Trung Quốc. Thông số kỹ thuật công khai biện minh cho chứng nhận, trong khi chất lượng đạt chuẩn Apple, năng suất sản lượng lớn và an ninh pháp lý nhiều năm vẫn chưa được chứng minh.

Biến số thị trường đầu tiên cần theo dõi không phải là thị phần Apple của CXMT. Đó là liệu một nhà cung cấp thứ tư có uy tín thương mại có thay đổi giá hợp đồng DRAM di động cho bộ ba hiện tại không. Áp lực đó có nhiều khả năng xuất hiện trong LPDDR và client DRAM trước HBM.

Không có lý do gì để đối xử với mọi cổ phiếu bộ nhớ Hàn Quốc như nhau. Samsung phải cân bằng áp lực giá di động so với phục hồi HBM. Đối với SK Hynix, năng suất HBM4 và độ bền của đầu tư AI vẫn quan trọng hơn CXMT. Quyết định tiếp theo nên theo sau xác nhận nhà cung cấp chính thức, tháo rời sản phẩm, quyết định Entity List và sản lượng thương mại được công bố.
