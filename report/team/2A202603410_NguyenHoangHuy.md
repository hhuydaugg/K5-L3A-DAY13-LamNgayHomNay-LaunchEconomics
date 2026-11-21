# Báo cáo cá nhân — NguyenHoangHuy-2A202603410

## 1. Thông tin thành viên

- Họ tên: Nguyễn Hoàng Huy
- MSSV: 2A202603410
- Email: hhuynguyen2803@gmail.com
- Vai trong nhóm: người viết code trước giải lao (CP1–CP2), người kiểm số sau giải lao (CP4–CP5); nhóm trưởng

## 2. Phần việc phụ trách

- **Nhiệm vụ A** trong `src/lab13.py`:
  - A1: ba hàm kinh tế của việc chạy lại;
  - A2: mô hình chi phí từ trace;
  - A3: tách theo loại yêu cầu;
  - A4: cộng chi phí cố định.
- **Nhiệm vụ B** trong `src/lab13.py`: B1 (9 kịch bản), B2 (một cặp), B3 (giới hạn số lần chạy), B4 (xem lại 100%).
- Các bảng số trong `report/team/bang_chi_phi.md`. Câu trả lời và xếp hạng là phần của người kiểm số.
- Sau giải lao: kiểm tay một số D1, rà soát hồ sơ trước khi nộp, điền `TEAM.md`, push bản chốt.

## 3. Đóng góp cụ thể

- **A1:** ba phép thử in ĐẠT (1,20 · 1,25 · 1,25). Hệ số chi phí mỗi việc thành công luôn bằng 1/p, vì k triệt tiêu.
- **A2:** chi phí mỗi việc thành công là **4.472 đ [simulated]**, gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu (274,7 đ).
  - Tử số là 4.373.585 đ, tính trên mọi lần chạy kể cả lần lỗi. Mẫu số là 978 việc thành công.
  - Làm lại chiếm 51,8% [simulated], xem lại 40,7% [simulated] tổng chi phí.
  - Nếu cộng 222 ca nhân viên làm thay: **5.865 đ mỗi yêu cầu = 0,49×** của 12.000 đ [simulated].
- **A3:**
  - quoc_te tốn 22.515 đ mỗi việc thành công = 1,88× [simulated], tỉ lệ thành công 27,3%;
  - chạy lại không giúp quoc_te: tỉ lệ lần chạy ok ở lần 1, 2, 3 là 30,0%, 11,4%, 2,2%.
- **A4:** phạm vi noi_dia + hang_nang.
  - 45.000 yêu cầu/tháng: cộng chi phí cố định 1.185 đ mỗi việc, ra **4.599 đ = 0,38×** [simulated].
  - Khối lượng giảm một nửa: 5.784 đ = 0,48×.
- **B1–B2:** yếu tố mạnh nhất là số ca làm lại gấp đôi (+51,8%), rồi tỉ lệ xem lại gấp đôi (+40,7%), rồi lương tăng 25% (+23,1%). Giá token gấp đôi chỉ +5,6%. Cặp token + xem lại: 6.543 đ (+46,3%), bằng tổng hai tác động riêng.
- **B3:** chi phí cả hệ thống ở các mức giới hạn 1, 2, 3 lần chạy lần lượt là 7.449.781 đ, 6.901.220 đ và 7.037.585 đ.
  - Giới hạn 2 lần rẻ nhất cho công ty.
  - Chi phí mỗi việc thành công thấp nhất lại ở giới hạn 1 lần (4.111 đ).
- **B4:** xem lại 100% trong phạm vi tốn **11.743 đ = 0,98×** [simulated] với 9 phút làm lại mỗi ca, và 12.415 đ = 1,03× với 15,3 phút (trung bình cột simulated). Hoà vốn khi mỗi lần xem lại ≤ 5,1 phút hoặc ≤ 4,8 phút.
- **D1 (người kiểm số sau giải lao):** kiểm tay cả 5 câu theo công thức, không dùng hàm `co_mau` trong code, và đều khớp với code của người viết code CP4:
  - a) (1,95996 × √0,39875 + 0,84162 × √0,3975)² ÷ 0,05² = 1.250,71 → **1.251**;
  - b) DE 2,48 → 3.103 yêu cầu = 42 người mỗi nhóm;
  - c) 1.000; d) 300;
  - e) 2,82m ≥ 841,82 → **m ≥ 299** (DE 6,96).
  - Đã ghi kết quả vào phần chú thích D1 đầu `pilot_plan.yaml`.

## 4. Bằng chứng

- `src/lab13.py`: chạy `cd src && python lab13.py`, in ba phép thử ĐẠT và mọi bảng A, B.
- `report/team/bang_chi_phi.md`: bảng A1, A2 (9 dòng, có nhãn `simulated`), A3 (4 dòng), A4, B1 (9 dòng), B3, B4.
- `report/team/pilot_plan.yaml`: phần chú thích D1 (a–e) kèm phép tính tay.
- Commit: `45e5bdd` (CP1–CP2: code A, B và bảng số); commit kiểm số D1 theo sau.

## 5. Công cụ AI đã dùng

- **Claude Code (Claude Opus 5.5):** viết code A1–B4 theo công thức trong `docs/du_lieu_va_cong_thuc.md` và hướng dẫn chi tiết, và dán số vào bảng.
- **Cách tự kiểm tra:**
  - ba phép thử A1 phải in ĐẠT trước khi tính tiếp;
  - trong code có kiểm tra tự động: mỗi kịch bản "giảm một nửa" bằng đúng nửa mức tăng của "gấp đôi";
  - mọi số A2–B4 đều khớp số đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch < 2%). Riêng B4 với 15,3 phút ra 12.415 đ so với 12.414 đ, vì code dùng trung bình chính xác 15,2996 phút thay vì làm tròn.
  - Cuối cùng tự tính tay lại một số: 4.373.585 ÷ 978 = 4.472 đ.

## 6. Tự đánh giá

- **Phần A, B:** đủ số và khớp đáp án.
- **D1:** kiểm tay xong, khớp code.
- **Chưa xong:** rà soát cuối và push bản chốt, vì còn chờ các trường còn `?` trong `pilot_plan.yaml`, phần tính thử chỉ số, phiếu chấm và báo cáo nhóm.
- **Rút kinh nghiệm:** chi phí thật nằm ở giờ nhân viên (92,5% tổng chi phí [simulated]), không nằm ở token. Muốn giảm chi phí thì phải theo dõi tỉ lệ làm lại và tỉ lệ xem lại trong pilot.
