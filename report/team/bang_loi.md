# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Hồ Xuân Vũ · Người gắn nhãn 2: Khuất Duy Hiếu (TV4) (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 19 / 20 = 95%

## Quy tắc phân biệt cho ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Ca 13: Thống nhất là **Giới hạn hệ thống** vì yêu cầu hoàn phí bảo hiểm đối tác nằm ngoài phạm vi agent; câu trả lời chung chung là lỗi xử lý giới hạn, không làm thay đổi nguyên nhân gốc.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event mới `order_id_invalid` (trace_id, mẫu mã khách nhập), ghép với `refund_request_created`; theo dõi hằng ngày; cảnh báo khi > 3% yêu cầu trong ngày, hoặc > 20% số ca này không gửi lại trong 30 phút | Nhận diện định dạng mã đơn của sàn TMĐT, chỉ cho khách chỗ lấy mã vận đơn kèm ví dụ thay vì chỉ báo "mã không hợp lệ"; nếu tra được thì tự đổi mã sàn sang mã vận đơn | Product designer trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ theo `trace_id`: `ticket_closed` báo đã hoàn nhưng không có `refund_ledger_write` với `ket_qua` thành công; ngưỡng 0 ca, có 1 ca là cảnh báo ngay | Chỉ báo khách "đã hoàn" khi sổ cái xác nhận ghi thành công; nếu vẫn lỗi sau 3 lần thử thì báo "đang xử lý" và chuyển nhân viên; chặn ca này trước ngày bắt đầu pilot | Kỹ sư backend trợ lý hoàn phí |
| 18 | Ngữ cảnh | `ticket_reopened` có `reason` là hoàn thiếu, trong khi `audit_sample_checked` cho thấy `so_tien_da_hoan` bằng `so_tien_dung`; theo dõi hằng tuần; cảnh báo khi > 1% yêu cầu hoàn một phần bị mở lại vì lý do này | Tin nhắn luôn ghi cách tính: phí gốc, tỉ lệ hoàn, điều khoản áp dụng (ví dụ "30.000 đ × 50% do trễ 24–48 giờ = 15.000 đ") | Product designer trợ lý hoàn phí |
| 13 | Giới hạn hệ thống | Event mới `out_of_scope_detected` (trace_id, chủ đề) khi nhận ra yêu cầu bảo hiểm hoặc sản phẩm đối tác; hằng tuần đọc 30 trace có từ khoá bảo hiểm mà không có event này; ngưỡng: > 2/30 trace trả lời chung chung | Trả lời rõ "trợ lý không xử lý hoàn phí bảo hiểm", chuyển đúng kênh công ty bảo hiểm đối tác hoặc nhân viên kèm tóm tắt, không trả lời chung chung về phí vận chuyển | PM trợ lý hoàn phí |
| 17 | Ngầm | `audit_sample_checked` hằng ngày trên 50 lệnh hoàn ngẫu nhiên, tính lại bằng bảng giá hiện hành; cảnh báo khi ≥ 1% mẫu có `so_tien_da_hoan` khác `so_tien_dung`; thêm thuộc tính `phien_ban_bang_gia` vào `agent_run_completed`, cảnh báo ngay khi khác bản hiện hành | Xoá bộ nhớ đệm bảng giá mỗi khi có bản mới, ghi phiên bản bảng giá vào mỗi lệnh hoàn; truy lại 212 đơn lệch để hoàn bù hoặc ghi nhận | Kỹ sư dữ liệu trợ lý hoàn phí |
