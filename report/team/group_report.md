# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính. Toàn bộ dữ liệu của lab là giả lập; số có dùng phút nhân viên giả lập ghi `[simulated]`.

## 1. Thông tin nhóm

- Tên nhóm: LamNgayHomNay
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Định giá trợ lý hoàn phí LogiX-VN trên mẫu 1.200 yêu cầu và 1.624 lần chạy, rồi lập kế hoạch pilot để trình Gate 2a. Nhóm trả lời bốn câu: có đáng chạy không (A, B), khi hỏng thì sao (C), pilot thiết kế thế nào (D), đo gì và rủi ro kinh tế ra sao (E).

Chia theo bốn vai của lab (`PHAN_CONG.md`): người viết code, người kiểm số (đổi vai sau giải lao), hai người gắn nhãn độc lập, trong đó người gắn nhãn 2 giữ hồ sơ launch từ đầu buổi. Mọi số lấy từ `src/lab13.py` hoặc tính tay có ghi cách tính.

## 3. Giải pháp

- **A · Mô hình chi phí** ([bang_chi_phi.md](bang_chi_phi.md)): tử số tính mọi lần chạy, kể cả lần lỗi; mẫu số chỉ đếm việc thành công. Tách theo loại yêu cầu và cộng chi phí cố định 40 triệu đ/tháng.
- **B · Độ nhạy**: 9 kịch bản đổi từng yếu tố, một cặp, giới hạn số lần chạy 1/2/3, và kịch bản xem lại 100%.
- **C · Bảng lỗi** ([bang_loi.md](bang_loi.md)): hai người gắn nhãn 20 ca độc lập theo năm loại của Google PAIR, commit trước khi so; bảng khắc phục 5 ca, mỗi loại một ca, có event, ngưỡng, tần suất và vai trò phụ trách.
- **D · Pilot** ([pilot_plan.yaml](pilot_plan.yaml)): so ba cách chia (theo yêu cầu, theo nhân viên, theo depot), chọn ngẫu nhiên theo nhân viên; ba luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ.
- **E · Chỉ số và rủi ro** ([chi_so.md](chi_so.md)): ba chỉ số chính, dùng, an toàn, thêm hai chỉ số đề xuất, 10 event có `trace_id`, ba dòng rủi ro kinh tế. Ghép thành [hồ sơ launch v0](ho_so_launch_v0.md).

## 4. Kết quả

- Chi phí mỗi việc thành công **4.472 đ**, gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ) [simulated]. Giờ nhân viên chiếm 92,5% chi phí: làm lại 51,8%, xem lại 40,7%.
- Cả hệ thống, cộng 222 ca nhân viên làm thay: **5.865 đ/yêu cầu = 0,49×** mức nhân viên tự làm 12.000 đ [simulated].
- `quoc_te` tốn 22.515 đ/việc = 1,88× và chạy lại không giúp (tỉ lệ ok lần 1/2/3: 30,0% · 11,4% · 2,2%), nên phạm vi pilot thu hẹp về `noi_dia` + `hang_nang`: **4.599 đ/việc = 0,38×** sau khi cộng cố định [simulated].
- Ba yếu tố nhạy nhất: làm lại gấp đôi +51,8%, xem lại gấp đôi +40,7%, lương +25% → +23,1%; giá token gấp đôi chỉ +5,6% [simulated]. Giới hạn 2 lần chạy rẻ nhất cho cả hệ thống (6.901.220 đ).
- Con số bất lợi: xem lại 100% đưa chi phí lên **11.743–12.414 đ = 0,98–1,03×**, gần như không tiết kiệm [simulated].
- Bảng lỗi: đồng thuận **19/20 = 95%**, lệch ca 13, thống nhất là Giới hạn hệ thống.
- Pilot: chia theo yêu cầu cần 1.251/nhóm nhưng dễ lây ảnh hưởng; theo nhân viên với 75 yêu cầu/người cần 42 người/nhóm, vượt 40 người. Nhóm chọn 20 nhân viên/nhóm, chấp nhận mức chênh 6 điểm (859 hiệu dụng/nhóm, 299 yêu cầu/người); nếu tác động thật là 5 điểm thì power chỉ khoảng 0,64.
- Chỉ số trong đợt chạy thử: chính 82,83%, bỏ qua gợi ý 27,12%, mở lại 7 ngày 4,25% (3,97% trong phạm vi pilot).
- **Đề xuất cuối: Go có điều kiện** cho pilot `noi_dia` + `hang_nang`; điều kiện chặn là sửa ca 7 (báo "đã hoàn" khi sổ cái lỗi) trước ngày bắt đầu.
- Kết quả duyệt chéo nhóm nhận được từ hội đồng: ... (điền sau Gate 2a)

## 5. Khó khăn và cách xử lý

- Thời gian sát: phần D đến muộn so với CP4, người giữ hồ sơ điền trước các mục đã có số và để trạng thái "Chưa" cho mục chờ, rồi cập nhật khi có số.
- Một commit lỡ thêm dòng tổng vào cuối `src/logix_requests.csv` (vi phạm quy tắc không sửa CSV). Nhóm phát hiện khi rà soát, khôi phục file gốc và chạy lại `lab13.py`: kết quả giống hệt.
- Lệch nhãn ca 13 (Hệ thống hay Giới hạn hệ thống): thống nhất theo nguyên nhân gốc là yêu cầu ngoài phạm vi, và ghi quy tắc phân biệt.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Phút xem lại và làm lại là số giả lập; cần thay bằng phút đo thật sau tuần 1 của pilot.
- Đợt chạy thử không có đối chứng, nên chỉ số hiện tại chưa nói được tác động của trợ lý.
- Với 40 nhân viên, pilot không đủ power cho mức chênh 5 điểm; cần Giám đốc vận hành chấp nhận rủi ro này hoặc kéo dài pilot.
- Các event mới mới là đặc tả; cần kiểm chứng log ghi được và nối được bằng `trace_id` trước pilot.

## 8. Tài liệu tham khảo

- `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, `docs/du_lieu_va_cong_thuc.md`, `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`.
- Google PAIR, People + AI Guidebook, chương Errors + Graceful Failure (năm loại lỗi).
