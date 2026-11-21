# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhóm: **LamNgayHomNay** · Lớp: **L3A**. Hồ sơ đề xuất kế hoạch pilot; toàn bộ dữ liệu lab là giả lập. Nhãn `simulated` chỉ các kết quả có chi phí thời gian nhân viên giả lập.

| Mục | Con số chính và bằng chứng | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.373.585 đ / 978 việc = **4.472 đ/việc**, gấp **16,3×** hoá đơn token + tool/yêu cầu (274,7 đ). Trong phạm vi `noi_dia + hang_nang`: **3.414 đ/việc**, cộng cố định 40 triệu đ/tháng ở 45.000 yêu cầu/tháng thành **4.599 đ/việc** [simulated]. [Bảng A2, A4](bang_chi_phi.md). | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Làm lại gấp đôi: **+51,8%**, lên 6.787 đ; xem lại gấp đôi: **+40,7%**, lên 6.292 đ; lương tăng 25%: **+23,1%**, lên 5.506 đ. Token gấp đôi chỉ tăng 5,6% [simulated]. [Bảng B1, B2](bang_chi_phi.md). | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả mẫu, cộng 222 ca nhân viên làm thay: **5.865 đ/yêu cầu = 0,49×** mức 12.000 đ, chưa cộng cố định. Phạm vi pilot cộng cố định: 4.599 đ/việc thành công, chưa cộng nhân viên làm thay nên chưa phải chi phí hệ thống/yêu cầu. Bất lợi: xem lại 100% tốn **11.743–12.414 đ/việc = 0,98–1,03×**; `quoc_te` tốn 22.515 đ/việc nên loại [simulated]. [A2–A4, B4](bang_chi_phi.md). | Giả lập | Trưởng nhóm CSKH |
| 4 · Chỉ số chính, dùng, an toàn | Chỉ số trong đợt chạy thử: đóng trong 24 giờ và không mở lại 7 ngày **82,83% (994/1.200)**; bỏ qua gợi ý **27,12% (48/177)**; mở lại 7 ngày **4,25% (51/1.200)**, trong phạm vi pilot **3,97% (39/982)**. Mở lại là chỉ báo an toàn, không bao quát mọi lỗi. Chưa có đối chứng để kết luận tác động; 10 event dự kiến có `trace_id` trong [đặc tả chỉ số](chi_so.md). | Giả lập | Chuyên viên phân tích dữ liệu |
| 5 · Bảng lỗi và cách khắc phục | Theo [bảng lỗi](bang_loi.md): 20 ca, đồng thuận **19/20 = 95%**, lệch ca 13; có 5 phương án khắc phục đủ năm loại, kèm event, ngưỡng và vai trò. **Chưa có bằng chứng triển khai và kiểm thử** sửa ca 7: báo đã hoàn khi sổ cái lỗi; đây là điều kiện chặn trước pilot. | Chưa | Kỹ sư backend trợ lý hoàn phí |
| 6 · Pilot plan | Chỉ `noi_dia + hang_nang` tại 6 depot; ngẫu nhiên theo nhân viên, phân tầng depot, seed 13; **20 cụm/nhóm**, đối chứng đồng thời. Chấp nhận **MDE 6 điểm**, 859 mẫu hiệu dụng/nhóm; **299 yêu cầu/người**, 5.980 yêu cầu/nhóm, DE 6,96. Không đủ cho 5 điểm; nếu tác động thật 5 điểm, power khoảng **0,64**. Rollout 4 → 10 → 20 nhân viên; chỉ đo hiệu quả ở bước cuối, chờ đủ 7 ngày. Ngày duyệt **05/01/2027**; thiếu mẫu thì chưa mở rộng. Có 3 luật dừng và rollback 30 phút trong [kế hoạch pilot](pilot_plan.yaml). | Giả lập | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi làm chi phí tăng **51,8%**; xem lại 100% kéo chi phí lên **0,98–1,03×** mức tự làm; khối lượng giảm một nửa làm cố định tăng từ 1.185 lên 2.370 đ/việc, tổng **5.784 đ/việc** [simulated]. Theo dõi làm lại, thời gian xem lại và khối lượng; thu hẹp phạm vi hoặc dừng mở rộng khi vượt ngưỡng trong [bảng rủi ro](chi_so.md). | Giả lập | PM trợ lý hoàn phí |

**Điều kiện thông qua pilot** (T0 là ngày bắt đầu, chỉ chốt sau khi đủ điều kiện):

- **Kỹ sư backend — trước T0:** sửa ca 7, có bằng chứng kiểm thử chỉ báo “đã hoàn” khi sổ cái xác nhận thành công; kiểm tra rollback có hiệu lực trong 30 phút.
- **Chuyên viên phân tích dữ liệu — trước T0:** xác nhận log nối được bằng `trace_id`, tái tính ba chỉ số và kiểm tra kế hoạch YAML đọc được; lưu phân nhóm ngẫu nhiên trước khi chạy.
- **Giám đốc vận hành — trước T0 và mỗi lần chuyển bước:** duyệt nguồn lực đạt 299 yêu cầu/người ở bước cuối; áp dụng ba luật dừng đã ghi trước: mở lại chênh ≥ 2 điểm hoặc > 6% trong 3 lần kiểm tra ngày liên tiếp; chi phí > 8.000 đ trong 2 tuần; bỏ qua gợi ý > 40% trong 1 tuần.
- **Trưởng nhóm CSKH — cuối tuần 2 và trước chuyển bước:** kiểm tra tỉ lệ, thời gian xem lại và chất lượng; chỉ giảm xem lại khi có bằng chứng an toàn. Dùng cả giả định làm lại 9 và 15,3 phút, với ngưỡng hoà vốn xem lại tương ứng 5,1 và 4,8 phút [simulated].
- **Giám đốc vận hành — 05/01/2027:** duyệt khi đủ mẫu và đủ thời gian theo dõi; nếu thiếu điều kiện thì ghi chưa đủ bằng chứng và không mở rộng.

**Đề xuất: Go có điều kiện.**
