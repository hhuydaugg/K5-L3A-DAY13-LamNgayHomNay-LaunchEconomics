# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | ... |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | ... |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | ... |
| Dùng | Tỉ lệ yêu cầu nhóm can thiệp mà nhân viên mở gợi ý của trợ lý | `agent_suggestion_opened` chia tổng `refund_request_created` thuộc nhóm can thiệp, ghép bằng `trace_id` | Không cần tính |
| An toàn | Tỉ lệ đơn hoàn sai tiền theo kiểm tra mẫu | `audit_sample_checked` có `so_tien_da_hoan != so_tien_dung`, chia số đơn đã kiểm tra | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| refund_request_created | App khách | request_id, loai, so_tien, arm, created_at, trace_id | Khi khách gửi yêu cầu |
| agent_run_completed | Agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lỗi |
| agent_suggestion_shown | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra |
| agent_suggestion_opened | Giao diện nhân viên | staff_id, request_id, arm, opened_at, trace_id | Khi nhân viên mở gợi ý |
| staff_review_decision | Nhân viên | giu/sua/bo, phut_xem_lai, trace_id | Khi nhân viên gửi, sửa hoặc bỏ gợi ý |
| staff_rework_completed | Nhân viên | phut_lam_lai, ly_do, trace_id | Khi nhân viên làm lại xong |
| refund_ledger_write | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi bút toán hoàn tiền |
| ticket_closed | Hệ thống ticket | request_id, closed_at, trace_id | Khi đóng yêu cầu |
| ticket_reopened | Khách | request_id, reopened_at, reason, trace_id | Khi mở lại yêu cầu |
| audit_sample_checked | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Khi kiểm tra mẫu hằng tuần |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính dùng `ticket_closed` và `ticket_reopened`, ghép bằng `trace_id`.
- Chỉ số dùng "bỏ qua gợi ý" dùng `staff_review_decision`, đếm `sua + bo` trong mẫu các yêu cầu được xem lại.
- Chỉ số an toàn "mở lại trong 7 ngày" dùng `ticket_reopened` trong 7 ngày theo `trace_id`.
- Chỉ số dùng đề xuất dùng `agent_suggestion_opened` chia cho yêu cầu nhóm can thiệp từ `refund_request_created`; `agent_suggestion_shown` ghi nhận việc gợi ý được hiển thị.
- Chỉ số an toàn đề xuất dùng `audit_sample_checked` để so tiền đã hoàn với tiền đúng.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, từ 4.472 lên 6.787 đ mỗi việc thành công [simulated] (B1) | Tỉ lệ làm lại theo tuần, đếm `staff_rework_completed` chia `refund_request_created` nhóm can thiệp: > 7% (đợt chạy thử: 48/982 = 4,9% trong phạm vi noi_dia + hang_nang) | Thu hẹp về noi_dia, đọc 20 trace làm lại gần nhất để tìm nguyên nhân trước khi chạy tiếp | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× của 12.000 đ; 12.414 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu [simulated] (B4) | % yêu cầu có `staff_review_decision` vẫn > 50% ở cuối tuần 2; hoặc `phut_xem_lai` trung bình > 5,1 phút (ngưỡng hoà vốn B4) | Giảm xem lại theo bậc (100% → 50% → 20%) khi tỉ lệ `sua` + `bo` < 15% trong 2 tuần liền | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu còn một nửa, tổng 5.784 đ = 0,48× [simulated] (A4) | Số việc thành công theo tuần, đếm `ticket_closed` không có `ticket_reopened` trong 7 ngày: < 50% kế hoạch | Không mở rộng pilot; xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
