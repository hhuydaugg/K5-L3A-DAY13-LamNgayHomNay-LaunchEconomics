# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: LamNgayHomNay · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc trên cả mẫu 1.200 yêu cầu (4.373.585 đ ÷ 978 việc), gấp 16,3× hoá đơn token + tool chia số yêu cầu (274,7 đ). Phạm vi noi_dia + hang_nang: 3.414 đ, cộng cố định 40 triệu/tháng ở 45.000 yc/tháng thành 4.599 đ [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Số ca làm lại gấp đôi +51,8% (6.787 đ) · tỉ lệ xem lại gấp đôi +40,7% (6.292 đ) · lương nhân viên +25% → +23,1% (5.506 đ). Giá token gấp đôi chỉ +5,6% [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả mẫu, tính cả 222 ca nhân viên làm thay: 5.865 đ/yêu cầu = 0,49× của 12.000 đ, chưa cộng cố định. Phạm vi noi_dia + hang_nang: 4.599 đ = 0,38× của 12.000 đ (0,48× nếu khối lượng còn một nửa). Bất lợi: quoc_te 22.515 đ = 1,88× nên loại khỏi phạm vi; nếu xem lại 100% thì 11.743 đ = 0,98× (1,03× với 15,3 phút làm lại), gần như không tiết kiệm [simulated] | Giả lập | Trưởng nhóm CSKH |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử (chưa có đối chứng): chính 82,83% (994/1.200) đóng trong 24 giờ và không mở lại trong 7 ngày; dùng 27,12% (48/177) gợi ý bị sửa hoặc bỏ; an toàn 4,25% (51/1.200) mở lại trong 7 ngày. Tính bằng công thức E1 trong `chi_so.md`. Thêm 1 chỉ số dùng và 1 chỉ số an toàn đề xuất, đủ event có `trace_id` | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | 20 ca, hai người gắn độc lập, đồng thuận 19/20 = 95% (lệch ca 13, thống nhất Giới hạn hệ thống). Bảng khắc phục 5 ca đủ năm loại, mỗi dòng có event, ngưỡng, tần suất. Ca 7 (báo đã hoàn khi sổ cái lỗi) phải sửa trước ngày bắt đầu pilot | Xong, có bằng chứng | Kỹ sư backend trợ lý hoàn phí |
| 6 · Pilot plan | Chia ngẫu nhiên theo nhân viên, 20 nhân viên mỗi nhóm, cùng 6 depot, cùng thời gian. Chấp nhận mức chênh 6 điểm (859 yêu cầu mỗi nhóm); bất lợi: power chỉ khoảng 0,64 nếu tác động thật là 5 điểm. Luật dừng an toàn: mở lại 7 ngày cao hơn đối chứng ≥ 2 điểm hoặc vượt 6% (hiện 3,97% trong phạm vi). Ngày quyết định 2027-01-05. D1 (`lab13.py`): chia theo yêu cầu cần 1.251/nhóm; theo nhân viên m = 75 cần 42 người/nhóm, vượt 40 người; chênh 6 điểm thì mỗi nhân viên xử lý ≥ 299 yêu cầu (DE 6,96). Trường số trong `pilot_plan.yaml` còn chờ điền | Chưa | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Ba rủi ro trong `chi_so.md`: làm lại gấp đôi +51,8% (6.787 đ); xem lại 100% kéo dài 0,98–1,03× của 12.000 đ, hết tiết kiệm; khối lượng còn một nửa thì 5.784 đ = 0,48× [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất (nháp, chờ cả nhóm chốt):** Go có điều kiện, cho pilot noi_dia + hang_nang. Mỗi điều kiện có người phụ trách và ngày kiểm tra:

- Sửa ca 7 (chỉ báo "đã hoàn" khi sổ cái ghi thành công) và ca 20 (khoá chống trùng) trước ngày bắt đầu pilot · Kỹ sư backend trợ lý hoàn phí · kiểm tra trước ngày bắt đầu.
- Giám đốc vận hành ký chấp nhận mức chênh 6 điểm, biết power chỉ 0,64 nếu tác động thật là 5 điểm · Giám đốc vận hành · trước ngày bắt đầu.
- Bật đủ event có `trace_id` trong `chi_so.md`; thay phút xem lại và làm lại simulated bằng phút đo thật sau tuần 1 · PM trợ lý hoàn phí · cuối tuần 1.
- Có kế hoạch giảm xem lại theo bậc, vì xem lại 100% thì chi phí 0,98–1,03× của 12.000 đ, không tiết kiệm (B4) [simulated] · Trưởng nhóm CSKH · cuối tuần 2.
