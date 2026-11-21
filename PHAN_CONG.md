# Phân công Lab 13 — nhóm LamNgayHomNay (4 người)

Repo nhóm: `hhuydaugg/K5-L3A-DAY13-LamNgayHomNay-LaunchEconomics`. Mọi lệnh chạy trong `src/`, đã bật venv.

Thành viên là 4 collaborator của repo nhóm. Họ tên lấy từ GitHub; ai chưa ghi họ tên thì tự điền họ tên và MSSV vào `TEAM.md`.

Chia theo 4 vai bắt buộc của lab (`TEAM.md`). Lab yêu cầu đổi người viết code sau giờ giải lao, nên TV1 và TV2 đổi vai cho nhau lúc 15:35.

## Vai và phần việc

| TV | Vai | Phần việc chính | File phụ trách |
|---|---|---|---|
| TV1 Nguyễn Hoàng Huy (`hhuydaugg`, nhóm trưởng) | Viết code trước giải lao → kiểm số sau giải lao | A1–A4 và B1–B4 trong `lab13.py`; kiểm tay một số D1; rà soát cuối; `TEAM.md`; push bản chốt | `src/lab13.py` (CP1, CP2), số trong `bang_chi_phi.md`, `TEAM.md` |
| TV2 Phan Hải Đăng (`dangph12`) | Kiểm số trước giải lao → viết code sau giải lao | Tính tay đối chiếu A1, A2; viết câu trả lời A, xếp hạng B, B3, B4; code D1 và tỉ lệ `mo_lai_trong_7_ngay`; tính thử 3 chỉ số E1 | câu trả lời trong `bang_chi_phi.md`, `src/lab13.py` (CP4), các trường số của `pilot_plan.yaml` |
| TV3 Hồ Xuân Vũ (`Him2K2`) | Gắn nhãn 1 | Bộ nhãn 1 cho 20 ca, tỉ lệ đồng thuận, quy tắc cho ca lệch; 5 câu D2 và 3 luật dừng; danh sách ≥ 6 event và 2 chỉ số đề xuất; dẫn phần chấm nhóm khác | `bang_loi.md` (nhãn 1, đồng thuận), luật dừng trong `pilot_plan.yaml`, `chi_so.md`, `phieu_cham.md` |
| TV4 Khuất Duy Hiếu (`KhuatHieu`) | Gắn nhãn 2, kiêm giữ hồ sơ | Điền hồ sơ launch v0 từ đầu buổi; bộ nhãn 2 cho 20 ca; bảng khắc phục 5 ca; ≥ 2 dòng rủi ro kinh tế; trình bày ở Gate 2a; báo cáo nhóm | `ho_so_launch_v0.md`, `bang_loi.md` (nhãn 2, bảng khắc phục), phần rủi ro trong `chi_so.md`, `group_report.md` |

Mỗi người tự làm báo cáo cá nhân `report/team/MSSV_HoTen.md` (copy từ file mẫu, giữ lại file mẫu), và tự nộp link repo trên LMS.

## Thứ tự làm

### Trước buổi lab

1. **TV1:**
   - ~~mời TV2, TV3, TV4 làm collaborator~~: đã xong, cả 3 đã có quyền ghi;
   - điền thông tin nhóm và bảng thành viên trong `TEAM.md`, rồi commit.
2. **Cả nhóm:**
   - clone repo nhóm, tạo venv, `pip install -r requirements.txt`;
   - chạy kiểm tra thư viện, phải in `san sang`;
   - đọc `docs/du_lieu_va_cong_thuc.md`.

### 14:10 · CP1 — nhiệm vụ A

3. **TV1** viết code theo thứ tự trong hướng dẫn chi tiết:
   - **A1:** ba hàm, phải in `ĐẠT` (1,20 · 1,25 · 1,25) trước khi làm tiếp;
   - **A2:** hàm `mo_hinh`;
   - **A4:** thêm 40 triệu đ/tháng chi phí cố định cho `noi_dia` + `hang_nang`;
   - **A3:** tính lại theo từng giá trị cột `loai`.
4. **TV2** đối chiếu số:
   - tính tay một số A1 và một số A2;
   - chép bảng A2 (9 dòng; hai dòng giả lập ghi `simulated`), A3 (4 dòng), A4 vào `bang_chi_phi.md`;
   - viết câu trả lời "vì sao tử số tính mọi lần chạy".
5. **TV4** ~~mở `ho_so_launch_v0.md`, điền mục chi phí ngay khi có số A2~~: đã xong (điền luôn mục 1–3 theo số A2, A4, B1).
6. **TV3** đọc trước định nghĩa năm loại lỗi của Google PAIR và phần D, E trong hướng dẫn chi tiết.

### 14:53 · CP2 — nhiệm vụ B

7. **TV1** code B1 (9 kịch bản), B2 (một cặp), B3 (giới hạn 1/2/3 lần chạy), B4 (xem lại 100% cho `noi_dia` + `hang_nang`).
8. **TV2:**
   - điền bảng B1 và xếp hạng ba yếu tố mạnh nhất;
   - viết B3, B4 (mỗi câu ≤ 3 dòng, có số);
   - tự kiểm: tác động của "giảm một nửa" bằng nửa tác động của "gấp đôi".

### 15:20 – 15:35 · Giải lao. TV1 và TV2 đổi vai.

### 15:35 · CP3 — nhiệm vụ C

9. **TV3 và TV4:**
   - ngồi tách nhau, mỗi người gắn nhãn độc lập 20 ca (trong file docx đề bài) trong 8 phút, không trao đổi;
   - commit hai bộ nhãn trước khi so; không sửa bộ nhãn sau khi đã so.
   - TV4: ~~gắn và commit bộ nhãn 2~~: đã xong (commit `c674ed3`, trước khi so).
10. **TV1 và TV2** làm nốt CP2 trong lúc đó, rồi đọc trước phần D1.
11. **TV3** so nhãn, tính tỉ lệ đồng thuận (cần ≥ 16/20; thấp hơn thì viết lại định nghĩa), và viết một câu quy tắc cho mỗi ca lệch.
12. **TV4** ~~điền bảng khắc phục 5 ca, đủ năm loại~~: đã xong (ca 9, 7, 18, 13, 17). Mỗi dòng có cách phát hiện đo được (event, ngưỡng, tần suất) và một vai trò phụ trách, không ghi "cả đội".

### 16:08 · CP4 — nhiệm vụ D

13. **TV2** (giờ là người viết code):
    - code năm câu D1 (cỡ mẫu theo yêu cầu, theo nhân viên, theo depot, mức chênh 6 điểm);
    - tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại;
    - điền các trường số trong `pilot_plan.yaml`.
14. **TV1** kiểm tay một số D1, ghi kết quả D1 vào phần chú thích đầu `pilot_plan.yaml`.
15. **TV3:**
    - trả lời 5 câu D2;
    - viết ít nhất 3 luật dừng (an toàn, chi phí, mức độ sử dụng) theo mẫu NẾU – TRONG – THÌ – KHÔNG THÌ.
16. **TV2** chạy hai lệnh tự kiểm (`yaml.safe_load` và lệnh `grep` tìm dấu `?`).

### 16:36 · CP5 — nhiệm vụ E

17. **TV2** tính thử ba chỉ số: chính, dùng, an toàn.
18. **TV3** viết `chi_so.md`: đặc tả chỉ số, thêm 1 chỉ số dùng và 1 chỉ số an toàn, liệt kê ≥ 6 event có `trace_id`.
19. **TV4:**
    - ~~thêm ≥ 2 dòng rủi ro kinh tế lấy số từ bảng độ nhạy~~: đã xong (3 dòng trong `chi_so.md`);
    - ~~hoàn thiện `ho_so_launch_v0.md`: bảy mục, dòng cuối là Go / Go có điều kiện / No-go~~: đã xong (Go có điều kiện).
20. **TV1** rà soát:
    - mọi số giả lập có nhãn `simulated`;
    - `grep -rni production report/team` không in gì;
    - mỗi mục hồ sơ có người phụ trách là một vai trò.

### 17:00 · Duyệt chéo Gate 2a

21. **TV4** trình bày hồ sơ của nhóm. TV1 trả lời câu hỏi về chi phí và code, TV2 trả lời câu hỏi về cỡ mẫu.
22. **TV3** dẫn phần chấm nhóm n + 1, điền `phieu_cham.md`. Cả nhóm cùng thống nhất điểm.

### 17:45 · Đóng gói và nộp

23. **TV4** ~~điền `group_report.md`~~: đã xong, còn kết quả duyệt chéo điền sau Gate 2a.
24. **Mỗi người:**
    - tạo báo cáo cá nhân;
    - ghi phần đóng góp của mình trong `TEAM.md`;
    - ghi công cụ AI đã dùng và cách tự kiểm.
25. **TV1** chạy `cd src && python lab13.py` trên một máy khác, rà checklist trong `SUBMISSION.md`, commit và push bản chốt. Hạn: trước 23:59 GMT+7.
26. **Cả bốn người** nộp link repo trên LMS.

## Cách commit để tránh xung đột

- Mỗi người chỉ sửa file trong cột "File phụ trách" của mình. Trước khi push, chạy `git pull --rebase`.
- Hai file có hai người cùng sửa thì làm lần lượt:
  - `bang_chi_phi.md`: TV1 dán số → TV2 viết câu trả lời;
  - `bang_loi.md`: TV3 và TV4 commit nhãn riêng → TV3 viết đồng thuận → TV4 viết bảng khắc phục;
  - `pilot_plan.yaml`: TV2 điền số → TV3 viết D2 và luật dừng;
  - `chi_so.md`: TV3 viết chỉ số và event → TV4 thêm rủi ro.
- Không force-push, không sửa hai file CSV, không commit `.venv/` hay `.env`.
