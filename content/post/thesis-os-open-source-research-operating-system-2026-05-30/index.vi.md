---
title: "Blog này được tạo ra như thế nào: Giới thiệu Thesis OS, hệ điều hành nghiên cứu mã nguồn mở của chúng tôi"
date: 2026-05-30T11:00:00+09:00
description: "Các bài viết trên Korea Invest Insights không được viết từng bài từ con số không — chúng được tạo ra thông qua một cấu trúc gọi là Thesis Investment OS. Alpha thu thập bằng chứng, Lattice biến bằng chứng đó thành phán đoán, và Arki giữ cho toàn bộ hệ thống khỏe mạnh. Ba vai trò này cùng nhau tạo nên một hệ điều hành nghiên cứu mã nguồn mở. Bài viết này giải thích cấu trúc đó bằng ngôn ngữ dễ hiểu và mời bạn ghé thăm kho lưu trữ GitHub."
categories: ["Tools"]
tags:
  - "Thesis OS"
  - "mã nguồn mở"
  - "phương pháp nghiên cứu"
  - "nghiên cứu đầu tư"
  - "Alpha"
  - "Lattice"
  - "Arki"
  - "Research OS"
  - "GitHub"
slug: thesis-os-open-source-research-operating-system-2026-05-30
draft: false
---

> 🔗 <strong>Đến kho lưu trữ</strong>: <strong>[github.com/youngseongshin/thesis-investment-os](https://github.com/youngseongshin/thesis-investment-os)</strong> — hệ thống mã nguồn mở vận hành phần nghiên cứu của blog này

Bài hôm nay hơi khác thường lệ. Nó không nói về một cổ phiếu, mà nói về <strong>cách các bài viết trên blog này thực sự được tạo ra</strong>. Hãy để tôi vén bức màn sân khấu một chút.

![Kiến trúc Thesis Investment OS — một hệ điều hành nghiên cứu nơi Alpha, Lattice và Arki khớp vào nhau](thesis-os-architecture.png)

## Cần gì để tạo ra một bài viết

Các bài trên Korea Invest Insights không phải do một người ngồi trước màn hình trắng ứng tác ra. Đằng sau chúng là một hệ điều hành nhỏ tên là <strong>Thesis Investment OS</strong>. Cái tên nghe to tát, nhưng ý tưởng thì đơn giản.

> Làm cho phán đoán đầu tư trở nên <strong>nhìn thấy được, kiểm chứng được, và trung thực về thành tích của chính nó.</strong>

Đây không phải bot giao dịch tự động, không phải dịch vụ bán tín hiệu, cũng không phải "AI chọn cổ phiếu giúp bạn". Nó là một <strong>khung làm việc</strong> gom thông tin thị trường rời rạc thành một luận điểm (thesis), và cho phép bạn quay lại sau để kiểm tra xem luận điểm đó đúng hay sai.

Cấu trúc chia thành ba vai trò. Hãy hình dung chúng như ba con người trong cùng một đội.

---

## 1. Alpha — người thu thập bằng chứng

Alpha là vai trò <strong>thu thập và xác minh các sự kiện.</strong>

- <strong>Dữ liệu định lượng</strong>: giá, khối lượng, dòng tiền, cơ bản, hồ sơ công bố
- <strong>Dữ liệu định tính</strong>: tin tức, hồ sơ, bản ghi báo cáo kết quả, tín hiệu cộng đồng
- Lọc ứng viên bằng bộ sàng (screener), rồi phủ thêm bối cảnh để làm nổi bật những mã đáng theo dõi

Thứ Alpha tạo ra là các bản ghi bằng chứng, ảnh chụp thị trường, cảnh báo trong phiên, danh sách ứng viên từ bộ sàng, và các gói nghiên cứu. Nói gọn, đây là người <strong>chất đống một cách trung thực "chuyện gì đã xảy ra."</strong> Nó chưa phán đoán. Nó chỉ thu gom nguyên liệu.

---

## 2. Lattice — người dựng phán đoán từ bằng chứng

Cái tên Lattice đến từ ý tưởng của Charlie Munger về một <strong>"mạng lưới các mô hình tư duy" (latticework of mental models)</strong> — một trí óc được dựng nên từ nhiều khung khớp vào nhau.

Vai trò của nó là lấy nguyên liệu Alpha đã gom và biến thành một quyết định đầu tư thực sự.

- Đăng ký một luận điểm và sắp xếp nó thành thẻ quyết định (decision card)
- Chạy một đợt soát xét theo kiểu <strong>luật sư của quỷ (devil's advocate)</strong>, cố tình lập luận cho phía ngược lại
- Ghi các dự đoán vào sổ dự đoán (prediction ledger), rồi xem lại sau để biết chúng có đứng vững không

Cấu trúc bạn đọc trên blog — "đây là kết luận", "đây là sự kiện và đây là phỏng đoán" — đến thẳng từ Lattice. Điểm mấu chốt là <strong>đưa ra một phán đoán, nhưng để lại ở dạng có thể chấm điểm về sau.</strong>

---

## 3. Arki — người giữ cho hệ thống vận hành

Arki là vai trò ít lộ diện nhất, và có lẽ quan trọng nhất. Nó là người <strong>giữ cho toàn bộ hệ thống khỏe mạnh.</strong>

- Định nghĩa các lược đồ (schema) chứa dữ liệu và bố cục kho lưu trữ (vault) để cất giữ chúng
- Quản lý các công việc lặp lại (recurring jobs) và chạy kiểm tra sức khỏe (health check)
- Lưu nhật ký thay đổi (migration log) và quản lý quyền hạn cũng như quy tắc của từng vai trò

Nếu hệ thống là một ngôi nhà, Arki là người lo cho điện, nước và sưởi không ngừng chạy trong khi Alpha và Lattice làm việc. Không hào nhoáng, nhưng thiếu Arki thì hai vai kia chẳng trụ được lâu.

---

## Ba vai trò này đã tạo ra gì — ví dụ thực tế

Nói suông thì trừu tượng, nên đây là hai bài gần đây đã đi qua hệ thống này.

- [Kết quả quý 1 của Dell và đọc tham chiếu biên lợi nhuận máy chủ AI Hàn Quốc](/vi/post/dell-q1-fy2027-earnings-korea-ai-server-margin-readthrough-2026-05-29/) — Alpha gom các con số kết quả của Dell, còn Lattice nối chúng vào chuỗi giá trị bán dẫn và máy chủ Hàn Quốc để dựng một quan điểm.
- [Kết quả Marvell quý 1 FY2027 và đọc tham chiếu cho bán dẫn Hàn Quốc](/vi/post/marvell-q1-fy2027-korea-semiconductor-readthrough-2026-05-28/) — cùng dòng chảy: khởi đi từ các con số silicon tùy chỉnh của Marvell và đưa sang phần đọc tham chiếu cho Hàn Quốc.

Cả hai bài đều tách bạch "đây là Sự kiện, đây là Suy luận, đây là Phỏng đoán". Thói quen đó chính là cấu trúc mà Lattice buộc phải có, và những sự kiện chống đỡ nó là những thứ Alpha đã gom.

---

## Vì sao công bố điều này

Khi nghiên cứu đủ lâu, điều đáng sợ nhất là <strong>"không nhớ trước đây mình đã nói gì."</strong> Những luận điểm trông đẹp thì nhiều; quay lại kiểm tra xem chúng có thực sự đúng không thì lại nhàm và khó chịu. Vì thế phần lớn phân tích viết một lần rồi bị quên.

Thesis OS cố tình đưa sự khó chịu đó vào trong hệ thống. Mỗi phán đoán đều được gắn bằng chứng, mỗi dự đoán đều được ghi lại, và mọi thứ đều được chấm điểm về sau. Không phải vì nó hoàn hảo, mà vì nó được dựng để <strong>khi sai, bạn nhìn thấy được.</strong>

Hệ thống được thiết kế để chạy cục bộ. Bạn có thể thử với dữ liệu mẫu đi kèm — không cần khóa API, không cần đăng nhập công ty chứng khoán, không cần nguồn dữ liệu trả phí. Giấy phép là MIT, và cần Python 3.10 trở lên.

Và ba kênh mà hệ thống này công bố ra chính là: <strong>blog (Korea Invest Insights)</strong> bạn đang đọc, <strong>Telegram @korea_invest_insights</strong>, và <strong>Substack</strong>.

---

## Hãy ghé xem thử

Mục đích của bài này không phải khoe khoang — mà là một lời mời. Nếu bạn từng tự hỏi làm sao để nghiên cứu đầu tư trung thực hơn và kiểm chứng được hơn, hãy ghé qua xem.

> Bạn không phải đọc hết mã nguồn. Chỉ cần lướt qua README cũng đủ để cảm được "à, hóa ra những bài blog này được tạo ra theo cách này."

👉 <strong>[github.com/youngseongshin/thesis-investment-os](https://github.com/youngseongshin/thesis-investment-os)</strong>

Một ngôi sao thì rất quý, nhưng chỉ ngắm nghía cấu trúc thôi cũng được. Chỉ có một lý do để vén màn: <strong>để bạn tự mình thấy các phán đoán của blog này ra đời từ đâu và như thế nào.</strong>

---

*Tuyên bố miễn trừ: Chỉ nhằm mục đích nghiên cứu và cung cấp thông tin. Không phải tư vấn đầu tư cá nhân hóa. Hệ thống mã nguồn mở được mô tả là một công cụ nghiên cứu; người đọc tự chịu trách nhiệm về các quyết định đầu tư và kết quả của mình.*
