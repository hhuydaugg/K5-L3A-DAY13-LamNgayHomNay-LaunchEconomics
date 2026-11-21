# Bảng chi phí · Nhiệm vụ A và B

Nguồn tham khảo: `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, phần A–B. Số liệu dưới đây dùng số đối chiếu đã có trong hướng dẫn, chưa chạy lại code. Toàn bộ dữ liệu của lab là giả lập; nhãn `simulated` đánh dấu các kết quả có sử dụng chi phí thời gian nhân viên giả lập. Tiền làm tròn đến đồng.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 = 1/p |

Đối chiếu tay: E với k = 2 là (1 − 0,2²)/0,8 = 1,20; với k = 3, E/P = (0,992/0,8)/0,992 = 1,25.

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv`, mọi lần chạy | đo từ trace |
| Tool | 84.000 | `logix_runs.csv`, 5.600 lần gọi × 15 đ | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1; đã nằm trong token + tool | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated`: 890 phút × 2.000 đ | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated`: 1.132 phút × 2.000 đ | simulated |
| Tổng chi phí | 4.373.585 | Token + tool + xem lại + làm lại | simulated |
| Số việc thành công | 978 | `ket_qua` bằng `thanh_cong` | đếm từ dữ liệu |
| Chi phí mỗi việc thành công | 4.472 | 4.373.585 / 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (245.585 + 84.000) / 1.200 | đo từ trace |

- **Chi phí mỗi việc thành công gấp bao nhiêu lần “hoá đơn chia số yêu cầu”?** Khoảng **16,3 lần** (4.472 / 274,7), do cộng thêm chi phí xem lại, làm lại và chỉ chia cho 978 việc thành công.
- **Khoản nào chiếm tỉ trọng lớn nhất?** Làm lại chiếm **51,8%**, tiếp theo là xem lại **40,7%**; tổng giờ nhân viên chiếm **92,5%** chi phí.
- **Vì sao tử số tính mọi lần chạy?** Lần chạy lỗi vẫn tiêu token và gọi tool; bỏ chúng sẽ làm thiếu chi phí. Vì vậy cộng cả 1.624 lần chạy, nhưng mẫu số chỉ đếm 978 yêu cầu thành công.

**Lưu ý khi so với nhân viên tự làm:** Chi phí cả hệ thống là (4.373.585 + 222 × 12.000) / 1.200 = **5.865 đ/yêu cầu**, bằng **0,49×** mức 12.000 đ, chưa cộng cố định. Không dùng riêng 4.472 đ/việc thành công để kết luận mức tiết kiệm cho toàn bộ yêu cầu.

## A3 · Tách theo loại yêu cầu

Các cột chi phí mỗi việc thành công và so với 12.000 đ đều là **simulated**; tỉ số chỉ so trực tiếp chi phí trên việc trợ lý làm thành công, chưa cộng chi phí nhân viên làm thay và chi phí cố định.

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công [simulated] | So với 12.000 đ [simulated] |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

- **Loại nào không đáng để trợ lý xử lý? Chạy lại tới 3 lần có giúp không?** `quoc_te` có chi phí 22.515 đ/việc, bằng 1,88× mức tham chiếu, thành công chỉ 27,3%; tỉ lệ ok ở lần 1/2/3 giảm từ 30% xuống 11,4% và 2,2%, nên chạy lại tới 3 lần không cho thấy hiệu quả đủ để đưa vào pilot.
- **Phạm vi đề xuất:** Chọn `noi_dia` và `hang_nang`; loại `doi_tac` khỏi pilot vì chi phí đã bằng 0,85× mức tham chiếu, thành công chỉ 54,4% và còn có điều khoản riêng.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Dùng 900 việc thành công trong phạm vi trên tổng mẫu 1.200 yêu cầu; chi phí biến đổi trong phạm vi là 3.072.513 / 900 = **3.414 đ/việc**. Khối lượng tháng là tổng yêu cầu mọi loại, giữ cơ cấu như mẫu.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định [simulated] | So với 12.000 đ [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| Một nửa khối lượng: 22.500 yêu cầu/tháng | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- **Chi phí cố định có đổi kết luận không? Ở khối lượng nào?** Không đổi kết luận so sánh trực tiếp ở 45.000 và 22.500 yêu cầu/tháng: chi phí sau cố định lần lượt 4.599 và 5.784 đ/việc, đều dưới 12.000 đ; khối lượng giảm một nửa làm cố định mỗi việc tăng gấp đôi.

## B1 · Đổi từng yếu tố

Mốc gốc là **4.472 đ/việc thành công**. Chi phí và phần trăm thay đổi trong toàn bộ bảng đều có nhãn **simulated**.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công [simulated] | Thay đổi (%) [simulated] |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ attempt > 2; yêu cầu có so_lan_chay > 2 chuyển nhân viên, phút xem lại và làm lại bằng 0 | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

**Tự đối chiếu:** Mức giảm khi giảm một nửa bằng nửa mức tăng khi gấp đôi: token 5,6% → 2,8%; xem lại 40,7% → khoảng 20,3%; làm lại 51,8% → 25,9%. Chênh nhỏ do làm tròn.

## B2 · Đổi một cặp và xếp hạng

- **Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi:** **6.543 đ/việc thành công, tăng 46,3%**; bằng tổng hai tác động riêng 5,6% + 40,7% vì mô hình cộng tuyến tính.
- **Ba yếu tố ảnh hưởng mạnh nhất:** 1. Số ca làm lại (**+51,8%** khi gấp đôi); 2. Tỉ lệ xem lại (**+40,7%** khi gấp đôi); 3. Lương nhân viên (**+23,1%** khi tăng 25%), theo các kịch bản của đề.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công. Các cột chi phí dưới đây đều là **simulated**, chưa cộng cố định.

| Giới hạn | Tổng chi phí trợ lý [simulated] | Số yêu cầu không thành công | Chi phí cả hệ thống [simulated] | Chi phí mỗi việc thành công [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- **Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không?** Giới hạn **2 lần** rẻ nhất cho công ty: **6.901.220 đ**; giới hạn **1 lần** có chi phí mỗi việc thành công thấp nhất (4.111đ) nhưng đẩy thêm **85 yêu cầu** sang nhân viên so với 2 lần.

## B4 · Nếu phải xem lại tất cả

Phạm vi: 982 yêu cầu `noi_dia` + `hang_nang`, trong đó 948 yêu cầu có ít nhất một lần chạy ok cần xem lại, 48 ca làm lại và 900 việc thành công. Xem lại 100% ở đây là xem mọi yêu cầu có câu trả lời ok.

- **Chi phí mỗi việc thành công khi xem lại 100%, so với 12.000 đ:** Với 5 phút xem lại và 9 phút làm lại/ca: (224.513 + 9.480.000 + 864.000) / 900 = **11.743 đ = 0,98×**; nếu làm lại 15,3 phút/ca thì **12.414 đ = 1,03×**, theo số phút làm tròn trong hướng dẫn.
- **Kết quả này nói gì về thứ pilot cần học được?** Pilot cần xác định tỉ lệ xem lại có thể giảm an toàn và thời gian mỗi lần xem lại; để chi phí/việc không vượt 12.000 đ, thời gian xem lại cần ≤ **5,1 phút** khi làm lại 9 phút hoặc ≤ **4,8 phút** khi làm lại 15,3 phút.
