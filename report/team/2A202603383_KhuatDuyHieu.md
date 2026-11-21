# Báo cáo cá nhân — KhuatDuyHieu-2A202603383

## 1. Thông tin thành viên

- Họ tên: Khuất Duy Hiếu
- MSSV: 2A202603383
- Email: hieukhuatduy@gmail.com
- Vai trong nhóm: người gắn nhãn 2, kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- `report/team/ho_so_launch_v0.md`: điền hồ sơ launch v0 từ đầu buổi, đủ bảy mục và đề xuất cuối.
- `report/team/bang_loi.md`: bộ nhãn 2 cho 20 ca (gắn độc lập), bảng khắc phục 5 ca.
- `report/team/chi_so.md`: phần E2 · rủi ro kinh tế (≥ 2 dòng).
- Trình bày hồ sơ ở Gate 2a; `report/team/group_report.md`.

## 3. Đóng góp cụ thể

- Hồ sơ launch v0, mục 1–3 (sau khi có số A2, B1 của người viết code):
  - mục 1: 4.472 đ mỗi việc thành công, gấp 16,3× hoá đơn token + tool chia số yêu cầu; phạm vi noi_dia + hang_nang cộng cố định 4.599 đ [simulated];
  - mục 2: ba yếu tố nhạy nhất là làm lại (+51,8%), xem lại (+40,7%), lương (+23,1%) [simulated];
  - mục 3: 0,38× của 12.000 đ trong phạm vi; nêu con số bất lợi quoc_te 1,88× và xem lại 100% 0,98× [simulated].
- Gắn nhãn 2 cho 20 ca, độc lập, commit `c674ed3` trước khi so; đồng thuận 19/20 = 95%, ca lệch duy nhất là 13 (tôi gắn Hệ thống, nhóm thống nhất Giới hạn hệ thống vì nguyên nhân gốc là yêu cầu ngoài phạm vi).
- Bảng khắc phục 5 ca, mỗi loại một ca: 9 (Do người dùng), 7 (Hệ thống), 18 (Ngữ cảnh), 13 (Giới hạn hệ thống), 17 (Ngầm); dùng event trong danh sách của `chi_so.md`.
- E2: ba dòng rủi ro kinh tế lấy số từ bảng độ nhạy.
- Hồ sơ mục 4–7 và đề xuất Go có điều kiện; `group_report.md`.
- Rà soát: khôi phục `src/logix_requests.csv` về bản gốc (một commit lỡ thêm dòng tổng), chạy lại `lab13.py`, kết quả giống hệt.

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- Commit `90788b4`, `c674ed3`, `95b8fb6`, `18611f1`, `132318b`.
- `report/team/ho_so_launch_v0.md`, `report/team/bang_loi.md` (cột nhãn 2, bảng khắc phục), `report/team/chi_so.md` (E2), `report/team/group_report.md`.

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- Claude Code: đọc phân công, chép số từ `bang_chi_phi.md` vào hồ sơ, soạn nháp bảng khắc phục, rủi ro E2 và báo cáo nhóm, chạy `lab13.py` và các lệnh tự kiểm. Không dùng AI để gắn nhãn: bộ nhãn 2 do tôi tự gắn rồi mới đưa vào file.
- Tự kiểm: đối chiếu từng con số với `bang_chi_phi.md`, output `lab13.py` và số đối chiếu trong hướng dẫn; tính lại ba chỉ số E1 trên CSV gốc (994/1.200, 48/177, 51/1.200); duyệt từng dòng bảng khắc phục trước khi commit.

## 6. Tự đánh giá

- Làm tốt: giữ hồ sơ cập nhật theo từng checkpoint, nêu rõ con số bất lợi (xem lại 100% 0,98×, power 0,64), gắn nhãn đạt đồng thuận 95%.
- Cần cải thiện: ca 13 tôi gắn theo chỗ cần sửa (trả lời chung chung) thay vì nguyên nhân gốc (ngoài phạm vi); lần sau hỏi "có làm được không" trước khi hỏi "có làm sai không".
