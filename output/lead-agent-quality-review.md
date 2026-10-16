# Rà soát chất lượng bởi Lead Agent — 16/10/2026

## Kết luận hiện tại

Bản local đã được kiểm tra trực quan trên desktop/mobile sau khi người dùng cho phép. Các lỗi căn hàng và cắt chữ được phát hiện đã được sửa và kiểm tra lại. Bản sẵn sàng để người dùng duyệt trong phạm vi đã thống nhất; nhận xét ảnh hero quá rối vẫn chờ phương án riêng, không được ghi là hoàn tất.

## Phần đã làm đúng, có bằng chứng kiểm tra

- Đã đọc lại PDF gốc: 14 trang, 29 comment; không chỉ dựa vào bản tổng hợp trước đó.
- Dữ liệu agenda và backend đăng ký không thay đổi.
- `app.js` chỉ khác các giá trị màu; tiểu sử, abstract và logic tương tác giữ nguyên so với trước feedback.
- Dùng file logo Marvell khách hàng cung cấp, không tự dựng lại logo.
- Cụm đối tác dùng chữ theo chỉ đạo của người dùng; giữ file logo để chờ xác nhận.
- Ảnh Strategic Panel dùng Option 11 do người dùng cung cấp; bố cục 4:5 đã được đồng ý thử; ảnh gốc được giữ nguyên.
- Kiểm tra chức năng lọc agenda, tìm kiếm/reset, mở/đóng thông tin diễn giả, mở/đóng đăng ký và menu mobile đã đạt ở mức kiểm tra logic.
- Nhóm Corporate Architects & Academic Luminaries hiện dùng thứ tự Tên → Chức danh → Tổ chức. Đủ 10 thẻ có nội dung trường giữ nguyên; cấu trúc thẻ/khung ảnh khớp nhóm keynote phía trên.
- Đã sửa một thẻ còn lệch khoảng cách chức danh so với chín thẻ khác.
- Bốn PILLAR có viền Gray 3 rõ hơn theo phản hồi trực tiếp của người dùng.

## Phần chưa làm tốt trong quá trình thực hiện

- Diễn giải phản hồi về màu quá rộng, khiến các nền tối bị gom về cùng màu và mất phân lớp.
- Làm ảnh hero gần như biến mất bằng giảm opacity kết hợp lớp phủ đậm mà chưa có phương án được duyệt riêng.
- Áp dụng quy tắc typography, bo góc và khoảng cách quá rộng thay vì giới hạn ở vị trí ghi chú.
- Chỉnh phân cấp chữ của nhóm diễn giả nhưng chưa đối chiếu trật tự chức danh/tổ chức và cách trang trí với nhóm trên ngay từ đầu.
- Báo cáo hoàn tất dựa trên kiểm tra mã nguồn và HTTP trong khi chưa nghiệm thu hình ảnh thực tế.
- Tiếp tục xử lý sau một số lỗi lệnh mà chưa dừng đúng quy tắc dự án.

Các thay đổi vượt phạm vi nêu trên đã được hoàn tác hoặc thu hẹp. Việc đó không tự động chứng minh giao diện hiện tại đã đạt chất lượng thị giác.

## Điều kiện để xác nhận bản hoàn chỉnh

1. Nội dung: không thêm/sửa tên, chức danh, đơn vị, tiểu sử, abstract, thời gian hoặc tên phiên ngoài chỉ đạo.
2. Phạm vi: mỗi thay đổi phải gắn với comment PDF hoặc chỉ đạo trực tiếp; các điểm chưa rõ giữ trạng thái mở.
3. Đồng bộ: kiểm tra toàn bộ thẻ diễn giả cùng lúc về thứ tự dòng, phân cấp chữ, khung ảnh, đường viền, hover và vị trí liên kết; không chỉ kiểm tra một thẻ mẫu.
4. Hiển thị: xem trực tiếp ở chiều rộng desktop và mobile để kiểm tra cắt chữ, tràn ngang, chiều cao hàng, độ rõ của PILLAR, hero và ảnh panel.
5. Nhận diện: đối chiếu màu hiển thị với bảng màu được cung cấp; giữ độ phân tách nền/viền, không lặp lại việc đồng nhất màu làm mất thẻ.
6. Trạng thái: ghi rõ mục còn mở; không dùng nhãn hoàn tất khi chỉ mới qua kiểm tra mã nguồn.

## Các điểm đang chờ

- Kiểm tra trình duyệt: người dùng đã cho phép; đã thực hiện. Kết quả và ảnh đối chiếu ở `output/browser-qa-results.md` và `output/qa/`.
- Hero: giữ ảnh gốc ở trạng thái hiện tại; chưa tự chọn ảnh khác hoặc mức che/mờ mới để xử lý nhận xét quá rối.
- Bản local: `http://localhost:3000/`; chưa commit, push hoặc deploy các cập nhật của ngày 16/10.
