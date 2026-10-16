# Kết quả kiểm tra trình duyệt — 16/10/2026

Bản local: http://localhost:3000/ — CSS version `20261016_review8`.

Người dùng đã cho phép kiểm tra trình duyệt và chụp ảnh đối chiếu. Không gửi đăng ký thử hoặc thay đổi hosting.

## Kết quả

| Kiểm tra | Kết quả |
|---|---|
| Header/hero desktop và mobile | Logo/tên sự kiện hiển thị; ảnh hero giữ nguyên. Không tràn ngang ở các độ rộng đo. |
| Diễn giả: tên/chức danh/tổ chức | Không có trường bị cắt hoặc ellipsis tại 320, 359, 360, 390, 768, 1440px. |
| Corporate: căn dòng tổ chức | 10 thẻ có cùng vị trí tương đối của dòng tổ chức tại mỗi độ rộng sau sửa. |
| Corporate: thứ tự và trang trí | Tên → Chức danh → Tổ chức; nền/khung ảnh/viền trên đồng bộ với nhóm keynote; chữ trắng và hover tổ chức Cyan. |
| PILLAR | Bốn viền Gray 3, 1px; cùng chiều cao 309px trên desktop 1440px; xem được viền trên mobile. Blue là trạng thái hover. |
| Strategic Panel | Ảnh tải đúng 2912×1632; khung cắt đúng 4:5; đầu máy và chip nằm trong khung trên desktop/mobile. |
| Thông tin diễn giả | Mở Mr. Khoa Tran hiển thị đúng tên và Renesas Electronics Vietnam; đóng hoạt động. |
| Agenda | Lọc Strategic Panel còn đúng một phiên; All Sessions khôi phục 19 phiên. |
| Menu mobile | Mở, chọn About Summit, tự đóng và di chuyển tới phần tương ứng. |
| Lỗi JavaScript quan sát được | Không có trong log đã kiểm tra của tab thử nghiệm. |

## Các sửa lỗi hiển thị phát hiện trong lần kiểm tra này

- Cập nhật sau phản hồi và phê duyệt của người dùng: bỏ chiều cao giữ chỗ ở cả 10 tên/chức danh Corporate, kể cả quy tắc riêng cho điện thoại hẹp. Khoảng cách Tên → Chức danh và Chức danh → Tổ chức đều 2px; min-height đều 0px. Kiểm tra lại tại 320, 390 và 1440px không tràn ngang hoặc cắt chữ. Giữ nguyên nội dung, màu và khung thẻ.
- Cho chức danh/tổ chức nhóm phía trên xuống dòng thay vì cắt bằng ellipsis. Không đổi chữ hoặc giá trị các trường.
- Khôi phục đúng ký tự `Đ` từ chuỗi lỗi mã hóa có thể chuyển ngược, tại hai vị trí tham chiếu quyết định. Không đổi số hoặc nội dung.

## Ảnh đối chiếu

Desktop — nhóm Corporate:

![Desktop speakers](<D:/Landing Page/vietnam-semiconductor-summit-2026.marvell.com/output/qa/speakers-natural-desktop.jpg>)

Mobile — nhóm Corporate:

![Mobile speakers](<D:/Landing Page/vietnam-semiconductor-summit-2026.marvell.com/output/qa/speakers-natural-mobile.jpg>)

PILLAR desktop:

![Desktop pillars](<D:/Landing Page/vietnam-semiconductor-summit-2026.marvell.com/output/qa/pillars-desktop.jpg>)

Strategic Panel desktop:

![Desktop panel](<D:/Landing Page/vietnam-semiconductor-summit-2026.marvell.com/output/qa/panel-desktop.jpg>)

Strategic Panel mobile:

![Mobile panel](<D:/Landing Page/vietnam-semiconductor-summit-2026.marvell.com/output/qa/panel-mobile.jpg>)

## Mục còn mở

- Nhận xét ảnh hero quá rối: giữ ảnh gốc, chưa tự đổi ảnh hay chọn lại mức che/mờ.
- Các độ rộng kiểm tra là kiểm tra responsive trong trình duyệt desktop, không thay thế thử nghiệm trên thiết bị iPhone/MacBook thật.
- Chưa commit, push hoặc deploy các cập nhật ngày 16/10. Cần người dùng nghiệm thu bản local.

## Đồng bộ chức danh và tổ chức theo phê duyệt tiếp theo

Bản mới thay thế các giá trị rút gọn trong mục trước:
- Loan Nguyen: Co-Founder & Chief Executive Officer (CEO), thống nhất thẻ, Bio metadata và hai agenda.
- Loan Pham-Nguyen: Head of IC Design & Embedded Systems Laboratory, thống nhất ba nguồn; tổ chức HUST thống nhất với thẻ/agenda.
- Trang Hoang: Head of Examination & QA Office, Senior IC Design Faculty; giải thưởng vẫn nằm trong Bio văn xuôi.
- Mai Nguyen: Viet Nam National University Ho Chi Minh City (VNU-HCM), thống nhất thẻ, Bio metadata, hai agenda và danh sách panel.
- Không thay học hàm, Bio văn xuôi, tên phiên hoặc thời gian. Học hàm Mai Nguyen vẫn chờ nguồn xác nhận.
- app.js review9 để tránh cache metadata cũ; CSS review8 không đổi.
- Hai generator build thành công, node --check app.js và git diff --check đạt. QA độc lập đạt. Browser: bốn thẻ 390px không cắt trường hoặc tràn ngang; mở Bio Loan Nguyen đúng chức danh; agenda riêng chứa đủ bốn giá trị mới. Ảnh: output/qa/speakers-bio-sync-desktop.jpg.
- Chưa commit, push, deploy.
## Bio Noam và thay Moderator theo nội dung khách hàng mới gửi

- Thay nguyên văn Bio Noam bằng đoạn khách hàng cung cấp, giữ cách viết và kết thúc “a MBA ... Cum Laude”.
- Agenda session 17 (16:15–16:55): Noam là moderator duy nhất; bỏ Quang-Dam và chuyển Noam ra khỏi panelists. Ba panelists còn lại giữ nguyên.
- Đồng bộ khối #panel: Moderator Noam, bỏ Quang-Dam khỏi danh sách Leadership. Noam trong danh sách Leadership được ghi rõ Moderator.
- Lịch Bio Quang-Dam bỏ riêng phiên panel; giữ các phiên 09:00, 09:30, 16:55. Lịch Noam ghi Moderator.
- Hai generator build thành công; node --check app.js, git diff --check đạt. QA độc lập xác nhận JSON, hai agenda và lịch Bio; Lead đối chiếu nguyên văn Bio trên trình duyệt.
- Browser: mở Bio Noam và Quang-Dam, kiểm tra agenda trang chủ/trang riêng; agenda mobile 390px không tràn ngang. Ảnh: output/qa/noam-bio-update.jpg.
- app.js review10; CSS không đổi. Chưa commit, push hoặc deploy.