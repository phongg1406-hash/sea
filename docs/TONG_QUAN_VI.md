# SUNLIT SHORE — Bản bàn giao bằng tiếng Việt

**Trạng thái:** Đã hoàn tất bản đặc tả, sơ đồ không gian, wireframe và website mẫu có tương tác. **Chưa phải sản phẩm production; chưa triển khai lên Internet.**

## Ý tưởng thống nhất

Sunlit Shore là portfolio lấy cảm hứng từ bãi biển mùa hè, có màu xanh ngọc, cát kem, nắng vàng, thiết kế Playful Brutalism tiết chế và các module sáng tạo. Người dùng có thể kéo để khám phá một không gian 2D trên desktop; các dự án được thể hiện bằng postcard kết hợp card tối giản.

Đặc trưng là **Directional Water Wake**: khi con trỏ đi qua nước, những vệt nước lệch theo hướng di chuyển và tan dần, như đang dùng tay khua nước. Không tạo vòng sóng đồng tâm giống ném đá xuống nước. Nước không được mô phỏng bằng hệ vật lý phức tạp; đồ họa được tạo bằng CSS, SVG và Canvas.

## Điều quan trọng khi hiểu “canvas toàn website”

Trên desktop, đây là một **thế giới giao diện 2D**, trong đó có nhiều khu vực khác nhau và camera có thể di chuyển; không phải mọi nội dung đều được vẽ bằng thẻ `<canvas>`. Văn bản, nút và liên kết vẫn là HTML bình thường. Điều này hỗ trợ SEO, accessibility và AI coding không có Vision.

Trên điện thoại, cách khám phá được chuyển thành cuộn dọc tự nhiên. Cố ép người dùng kéo cả thế giới bằng ngón tay sẽ làm khó việc đọc và xung đột với thao tác cuộn.

## Sáu vùng chính

1. **Ocean Hero:** giới thiệu, nước tương tác, nút dẫn đến dự án.
2. **Selected Work:** dự án nổi bật với postcard trên nền cát.
3. **Playground:** các đồ vật/module kéo thả trong vùng riêng.
4. **Project Archive:** danh sách dự án có chế độ Grid/List.
5. **About:** giới thiệu cá nhân với các ô Bento.
6. **Contact:** email và mạng xã hội, có kiểm tra placeholder.

Đường đi thông thường là Hero → Selected Work → Playground → Archive → About → Contact. Người dùng cũng có thể chọn vùng trực tiếp bằng navigation hoặc mini-map.

## Trạng thái tương tác

**Đã có trong prototype:** desktop pan, zoom và điều hướng; Water Wake nhẹ; mini-map; postcard và project modal; Grid/List; Playground kéo thả và reset; giảm chuyển động; bố cục mobile; menu mobile.

**Chưa hoàn tất để công bố:** ảnh chụp dự án thật, danh tính/câu giới thiệu thật, email/GitHub thật, case study, tối ưu theo kết quả đo trên phần cứng thật, kiểm định accessibility chuyên sâu và triển khai hosting.

## Hiệu năng và giới hạn

- Hiệu ứng nước chỉ chạy khi có vệt mới và tự dừng sau khi tan.
- Không dùng ảnh mạng, thư viện framework, fluid solver hoặc mô hình 3D.
- Kết quả kiểm thử Chromium hiện tại cho thấy tương tác cơ bản hoạt động và không có lỗi JavaScript ở các kịch bản được chạy.
- Đã kiểm tra viewport từ 360px đến 1920px và không thấy tràn ngang trong các lần kiểm tra đó.
- **Chưa đo LCP, INP, CLS hay FPS trên thiết bị của bạn.** Không nên xem các mục tiêu này là số liệu thực tế đã đạt.

## Sử dụng

Giải nén, mở `index.html` trên Windows. Có thể mở bằng VS Code và chạy `py -m http.server 8000` để sử dụng trình duyệt tại `http://localhost:8000`.

Mở `docs/DESIGN_SPEC.md` để đọc đặc tả đầy đủ, `docs/SPATIAL_MAP.svg` để xem sơ đồ, `docs/WIREFRAMES.svg` để xem bố cục, `docs/AI_HANDOFF.md` để giao cho AI coding.

### Dữ liệu cần tự cung cấp trước khi đưa lên Internet

- Tên hoặc thương hiệu portfolio, tagline, tiểu sử ngắn.
- Danh sách dự án thật, screenshot, mô tả, repository, demo.
- Email, GitHub và các đường dẫn liên hệ chính xác.

Các dự án và địa chỉ chưa có trong prototype đều được đánh dấu placeholder hoặc mẫu. Không tự suy đoán dữ liệu để thay thế.
