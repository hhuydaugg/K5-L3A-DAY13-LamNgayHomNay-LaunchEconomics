# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 994/1.200 = **82,83%** |
| Dùng | Tỉ lệ bỏ qua gợi ý | Trong các yêu cầu có `duoc_xem_lai = 1`, đếm quyết định `sua` hoặc `bo`, chia số yêu cầu được xem lại | 48/177 = **27,12%** |
| An toàn | Tỉ lệ mở lại trong 7 ngày (chỉ báo lỗi lọt đến khách) | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 51/1.200 = **4,25%**; phạm vi pilot: 39/982 = **3,97%** |
| Dùng | Tỉ lệ yêu cầu nhóm can thiệp mà nhân viên mở gợi ý của trợ lý | Số request_id duy nhất có `agent_suggestion_opened` chia số request_id duy nhất có `refund_request_created` thuộc nhóm can thiệp | Không cần tính |
| An toàn | Tỉ lệ đơn hoàn sai tiền theo kiểm tra mẫu | Số request_id duy nhất có kiểm tra phát hiện `so_tien_da_hoan != so_tien_dung`, chia số request_id duy nhất đã kiểm tra | Không cần tính |

Chỉ số trong đợt chạy thử là các giá trị trên, tính từ 1.200 yêu cầu trong `logix_requests.csv`. Toàn bộ dữ liệu là giả lập; chưa có đối chứng để kết luận trợ lý làm tăng chỉ số. Mở lại chỉ là chỉ báo an toàn, không bao quát mọi lỗi.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| refund_request_created | App khách | request_id, loai, so_tien, arm, created_at, trace_id | Khi khách gửi yêu cầu |
| agent_run_completed | Agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lỗi |
| agent_suggestion_shown | Giao diện nhân viên | request_id, staff_id, so_tien_de_xuat, shown_at, trace_id | Khi gợi ý hiện ra |
| agent_suggestion_opened | Giao diện nhân viên | staff_id, request_id, arm, opened_at, trace_id | Khi nhân viên mở gợi ý |
| staff_review_decision | Nhân viên | request_id, staff_id, arm, decision_id, decision (giu/sua/bo), phut_xem_lai, decided_at, trace_id | Khi nhân viên gửi, sửa hoặc bỏ gợi ý |
| staff_rework_completed | Nhân viên | request_id, phut_lam_lai, ly_do, completed_at, trace_id | Khi nhân viên làm lại xong |
| refund_ledger_write | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi bút toán hoàn tiền |
| ticket_closed | Hệ thống ticket | request_id, closed_at, ket_qua (thanh_cong/lam_lai/chuyen_nhan_vien), trace_id | Khi đóng yêu cầu |
| ticket_reopened | Khách | request_id, reopened_at, reason, trace_id | Khi mở lại yêu cầu |
| audit_sample_checked | Kế toán | request_id, audit_id, checked_at, so_tien_da_hoan, so_tien_dung, trace_id | Khi kiểm tra mẫu hằng tuần |

**Quy tắc đo và kiểm tra chéo**

- Mỗi event có `event_id` để loại bản ghi gửi lại, `request_id` để ghép một yêu cầu và `trace_id` để truy lần chạy. Một yêu cầu có thể có nhiều trace; không đếm mỗi trace thành một yêu cầu. Thuộc tính `arm` và `staff_id` lấy từ phân nhóm cố định khi tạo yêu cầu.
- Chỉ số chính: mẫu số là request_id duy nhất từ `refund_request_created` trong kỳ đã đủ 7 ngày kể từ `created_at`; tử số có lần đóng đầu tiên trong 24 giờ và không có `ticket_reopened` trong 7 ngày kể từ khi tạo yêu cầu. Dùng `created_at`, `closed_at`, `reopened_at`; yêu cầu chưa đóng vẫn nằm trong mẫu số. Đây là định nghĩa cửa sổ đề xuất cho pilot, phải chốt trước T0; CSV chỉ cung cấp cờ kết quả.
- Bỏ qua gợi ý: mẫu số là request_id duy nhất có `staff_review_decision`; tử số có quyết định cuối cùng là `sua` hoặc `bo`, chọn theo `decided_at`. Không lấy mọi yêu cầu hoặc số lần chạy làm mẫu số.
- Mở lại 7 ngày: mẫu số là request_id duy nhất từ `refund_request_created` đã đủ 7 ngày theo dõi; tử số có ít nhất một `ticket_reopened` trong cửa sổ 7 ngày kể từ khi tạo yêu cầu, mỗi yêu cầu chỉ đếm một lần. Tính riêng từng nhóm, cùng thời gian và phạm vi; loại yêu cầu chưa đủ theo dõi khỏi cả tử và mẫu.
- Mở gợi ý: tử số là request_id duy nhất có `agent_suggestion_opened`; mẫu số là request_id duy nhất thuộc nhóm can thiệp trong `refund_request_created`, cùng kỳ. Không cộng nhiều lượt mở của cùng một yêu cầu.
- Hoàn sai tiền: dùng `audit_sample_checked`; mỗi request_id chọn lần kiểm tra đầu tiên trong kỳ để không trộn kết quả sau sửa; mẫu số là số yêu cầu được kiểm tra, tử số là số yêu cầu sai tiền. Báo cáo kèm cách chọn mẫu, không coi đây là tỉ lệ của toàn bộ yêu cầu nếu mẫu không đại diện.
- Các event trên là đặc tả cần triển khai và kiểm chứng trước pilot; sự hiện diện trong tài liệu chưa chứng minh hệ thống đã ghi log được.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, từ 4.472 lên 6.787 đ mỗi việc thành công [simulated] (B1) | Tỉ lệ làm lại theo tuần, đếm request_id duy nhất có `staff_rework_completed` chia request_id duy nhất có `refund_request_created` cùng kỳ, cùng phạm vi nhóm can thiệp: > 7% (đợt chạy thử: 48/982 = 4,9% trong phạm vi noi_dia + hang_nang) | Thu hẹp về noi_dia, đọc 20 trace làm lại gần nhất để tìm nguyên nhân trước khi chạy tiếp | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× của 12.000 đ; 12.414 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu [simulated] (B4) | % request_id có xem lại trên tổng request_id có ít nhất một lần chạy ok vẫn > 50% ở cuối tuần 2; hoặc thời gian xem lại trung bình vượt 5,1 phút nếu làm lại 9 phút/ca, hay 4,8 phút nếu làm lại 15,3 phút/ca [simulated] | Chỉ giảm xem lại theo bậc (100% → 50% → 20%) khi tỉ lệ bỏ qua gợi ý < 15% trong 2 tuần liền, mẫu đủ 7 ngày theo dõi không vi phạm luật an toàn trong pilot_plan.yaml và kiểm tra mẫu không phát hiện sai tiền; Trưởng nhóm CSKH duyệt trước mỗi bậc, thiếu bằng chứng thì giữ mức xem lại và không mở rộng | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu còn một nửa, tổng 5.784 đ = 0,48× [simulated] (A4) | Số request_id duy nhất có kết quả thành công theo định nghĩa A2, đối chiếu trạng thái yêu cầu sau xử lý (cần ghi thêm ket_qua vào ticket_closed): < 50% kế hoạch tuần; không thay bằng chỉ số chính đóng trong 24 giờ và không mở lại | Không mở rộng pilot; xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |

