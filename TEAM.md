# Team

## Thông tin nhóm

- Tên nhóm: LamNgayHomNay
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-LamNgayHomNay-LaunchEconomics`
- URL repo: https://github.com/hhuydaugg/K5-L3A-DAY13-LamNgayHomNay-LaunchEconomics · nhánh nộp: `main` · commit chốt: (điền khi nộp)
- Phân công và thứ tự làm: [PHAN_CONG.md](PHAN_CONG.md)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Hoàng Huy | 2A202603410 | hhuynguyen2803@gmail.com | hhuydaugg | Người viết code (CP1–CP2) → người kiểm số (CP4–CP5); nhóm trưởng |
|   2 | Phan Hải Đăng | 2A202603409 | haidangphan2015@gmail.com | dangph12 | Người kiểm số (CP1–CP2) → người viết code (CP4–CP5) |
|   3 | Hồ Xuân Vũ | 2A202603406 | (tự điền) | Him2K2 | Người gắn nhãn 1 |
|   4 | (tự điền họ tên) | (tự điền) | (tự điền) | KhuatHieu | Người gắn nhãn 2, kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-

## NguyenHoangHuy-2A202603410

### Phần việc phụ trách

- Người viết code trước giải lao: nhiệm vụ A (A1–A4) và B (B1–B4) trong `src/lab13.py`; các bảng số trong `report/team/bang_chi_phi.md`.
- Sau giải lao (người kiểm số): kiểm tay một số D1, rà soát nhãn `simulated` và từ bị cấm trong hồ sơ trước khi nộp; điền `TEAM.md`; push bản chốt.

### Đóng góp cụ thể

- A1: ba hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`, ba phép thử in ĐẠT (1,20 · 1,25 · 1,25).
- A2–A4: hàm `mo_hinh`; chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ); tách theo loại (quoc_te 1,88× của 12.000 đ); phạm vi noi_dia + hang_nang cộng chi phí cố định: 4.599 đ = 0,38× [simulated].
- B1–B4: 9 kịch bản độ nhạy (làm lại gấp đôi +51,8%, xem lại gấp đôi +40,7%), một cặp (+46,3%), giới hạn 2 lần chạy rẻ nhất cho cả hệ thống (6.901.220 đ), xem lại 100% = 11.743 đ = 0,98× [simulated].

### Bằng chứng

- `src/lab13.py` (chạy `cd src && python lab13.py`), `report/team/bang_chi_phi.md`; báo cáo cá nhân `report/team/2A202603410_NguyenHoangHuy.md`.

## PhanHaiDang-2A202603409

### Phần việc phụ trách

- Người kiểm số (CP1–CP2): đối chiếu số liệu, hoàn thiện bảng và câu trả lời A–B trong `report/team/bang_chi_phi.md`.
- Theo phân công đổi sang viết code CP4–CP5; phần D1/E1 chưa được xác nhận hoàn thành trong báo cáo cá nhân.

### Đóng góp cụ thể

- Điền bảng A1–A4, B1–B3 và trả lời đến B4 theo số liệu hướng dẫn; bổ sung nhãn `simulated` và lưu ý phạm vi chi phí.
- Giải thích chi phí 4.472 đ/việc thành công, gấp 16,3 lần hoá đơn mỗi yêu cầu [simulated]; xếp hạng yếu tố ảnh hưởng: làm lại, xem lại, lương nhân viên.
- Nêu giới hạn 2 lần chạy rẻ nhất cho cả hệ thống: 6.901.220 đ [simulated]; phân tích xem lại 100% theo hai giả định thời gian làm lại.
- Dùng ChatGPT/Codex hỗ trợ tổng hợp và soạn nội dung từ hướng dẫn; không chạy lại Python, cần đọc lại và xác nhận trước khi nộp.

### Bằng chứng

- [Bảng chi phí A–B](report/team/bang_chi_phi.md).
- [Báo cáo cá nhân](report/team/2A202603409_PhanHaiDang.md).
- Nguồn đối chiếu: [Hướng dẫn chi tiết](docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md), phần A–B.
