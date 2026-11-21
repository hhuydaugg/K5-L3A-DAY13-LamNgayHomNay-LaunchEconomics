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
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
