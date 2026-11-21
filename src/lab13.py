"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    # lần chạy thứ i chỉ xảy ra khi i-1 lần trước đều sai: tổng (1-p)^(i-1), i = 1..k
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    # tử số: mọi lần chạy (kể cả lỗi); mẫu số: chỉ yêu cầu thành công. Kết quả luôn bằng 1/p, k triệt tiêu
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]  # A3 truyền một phần reqs: chỉ giữ lần chạy của các yêu cầu đó
    if max_lan_chay is not None:  # B1, B3: bỏ lần chạy vượt giới hạn; yêu cầu cần nhiều lần hơn thì chuyển nhân viên
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai  # tử số: MỌI lần chạy, kể cả lần lỗi
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())   # mẫu số: chỉ việc thành công
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


CHI_PHI_CO_DINH = 40_000_000   # đồng / tháng (A4)
YC_MOI_THANG = 45_000          # yêu cầu hoàn phí / tháng ở quy mô đầy đủ (A4)
PHAM_VI = ['noi_dia', 'hang_nang']   # phạm vi pilot (A4, B4)
PHUT_XEM_LAI_100 = 5           # B4 (đề bài): phút xem lại mỗi yêu cầu khi xem lại tất cả
PHUT_LAM_LAI_DE = 9            # B4 (đề bài): phút làm lại mỗi ca lam_lai


def in_bang(tieu_de, cot, dong):
    print(f'\n== {tieu_de}')
    print(' | '.join(cot))
    for d in dong:
        print(' | '.join(d))


def nghin(x):
    return f'{x:,.0f}'.replace(',', '.')


def phan_tram(x, dau=False):
    return (f'{x * 100:+.1f}%' if dau else f'{x * 100:.1f}%').replace('.', ',')


def lan(x):
    return f'{x:.2f}×'.replace('.', ',')


def so(x, n=1):
    return f'{x:.{n}f}'.replace('.', ',')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    sim = ' [simulated]'

    # ---------- A2 · mô hình gốc ----------
    goc = mo_hinh(runs, reqs)
    in_bang('A2 · Mô hình chi phí từ trace', ['Khoản', 'Số tiền (đ)', 'Nhãn'], [
        ['Token (mọi lần chạy)', nghin(goc['token']), 'đo từ trace'],
        [f'Tool ({runs["tool_calls"].sum():,} lần gọi)'.replace(',', '.'), nghin(goc['tool']), 'đo từ trace'],
        ['Trong đó, lần chạy thứ 2 và 3', nghin(goc['chay_lai']), 'đo từ trace'],
        [f'Xem lại ({reqs["phut_xem_lai_simulated"].sum():,} phút)'.replace(',', '.'), nghin(goc['xem_lai']), 'simulated'],
        [f'Làm lại ({reqs["phut_lam_lai_simulated"].sum():,} phút)'.replace(',', '.'), nghin(goc['lam_lai']), 'simulated'],
        ['Tổng chi phí', nghin(goc['tong']), 'có phần simulated'],
        ['Số việc thành công', str(goc['thanh_cong']), ''],
        ['Chi phí mỗi việc thành công', nghin(goc['cps']), 'simulated'],
        ['Hoá đơn token + tool chia số yêu cầu', so(goc['hoa_don_moi_yc']), 'đo từ trace'],
    ])
    nv = (reqs['phut_xem_lai_simulated'].sum() + reqs['phut_lam_lai_simulated'].sum()) * LUONG_PHUT
    khong_tc = len(reqs) - goc['thanh_cong']
    print(f'Chi phí mỗi việc thành công / hoá đơn mỗi yêu cầu = {so(goc["cps"] / goc["hoa_don_moi_yc"])} lần')
    print(f'Tỉ trọng: làm lại {phan_tram(goc["lam_lai"] / goc["tong"])}{sim}, xem lại {phan_tram(goc["xem_lai"] / goc["tong"])}{sim}, '
          f'giờ nhân viên {phan_tram(nv / goc["tong"])}{sim}, token + tool {phan_tram((goc["token"] + goc["tool"]) / goc["tong"])}')
    he_thong = (goc['tong'] + khong_tc * BASELINE) / len(reqs)  # cộng phần nhân viên làm thay các ca không thành công
    print(f'Chi phí cả hệ thống mỗi yêu cầu (cộng {khong_tc} ca nhân viên làm thay × 12.000 đ) = {nghin(he_thong)} đ = '
          f'{lan(he_thong / BASELINE)} của 12.000 đ{sim}')

    # ---------- A3 · theo loại yêu cầu ----------
    dong = []
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs['loai'] == loai]
        m = mo_hinh(runs, r)
        so_lan = runs['request_id'].isin(r['request_id']).sum() / len(r)
        dong.append([loai, str(len(r)), phan_tram(m['thanh_cong'] / len(r)), so(so_lan, 2),
                     nghin(m['cps']) + ' đ', lan(m['cps'] / BASELINE)])
    in_bang('A3 · Tách theo loại yêu cầu', ['Loại', 'Số yêu cầu', 'Tỉ lệ thành công', 'Số lần chạy mỗi yêu cầu',
                                            'Chi phí mỗi việc thành công' + sim, 'So với 12.000 đ'], dong)
    ok_theo_lan = runs.merge(reqs[['request_id', 'loai']]).assign(ok=lambda d: d['status'] == 'ok') \
        .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean')
    print('Tỉ lệ lần chạy ok theo lần thử (attempt):')
    print(ok_theo_lan.map(phan_tram).to_string())

    # ---------- A4 · chi phí cố định, phạm vi noi_dia + hang_nang ----------
    pv = reqs[reqs['loai'].isin(PHAM_VI)]
    m_pv = mo_hinh(runs, pv)
    dong = []
    for ten, he_so in [(f'{nghin(YC_MOI_THANG)} yêu cầu/tháng', 1), ('Một nửa khối lượng', 0.5)]:
        tc_thang = YC_MOI_THANG * he_so * m_pv['thanh_cong'] / len(reqs)  # tỉ lệ thành công trong phạm vi / cả mẫu
        co_dinh = CHI_PHI_CO_DINH / tc_thang
        dong.append([ten, nghin(tc_thang), nghin(co_dinh) + ' đ', nghin(m_pv['cps'] + co_dinh) + ' đ', lan((m_pv['cps'] + co_dinh) / BASELINE)])
    in_bang(f'A4 · Chi phí cố định (phạm vi noi_dia + hang_nang: {m_pv["thanh_cong"]}/{len(reqs)} việc thành công; '
            f'chi phí mỗi việc thành công chưa cộng cố định {nghin(m_pv["cps"])} đ{sim})',
            ['Khối lượng', 'Việc thành công mỗi tháng', 'Chi phí cố định mỗi việc', 'Chi phí mỗi việc thành công + cố định' + sim,
             'So với 12.000 đ'], dong)

    # ---------- B1 · đổi từng yếu tố ----------
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%': dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần': dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần': dict(max_lan_chay=1),
    }
    doi = {ten: mo_hinh(runs, reqs, **kw)['cps'] / goc['cps'] - 1 for ten, kw in kich_ban.items()}
    in_bang(f'B1 · Đổi từng yếu tố (gốc {nghin(goc["cps"])} đ{sim})', ['Kịch bản', 'Chi phí mỗi việc thành công' + sim, 'Thay đổi'],
            [[ten, nghin(goc['cps'] * (1 + d)) + ' đ', phan_tram(d, dau=True)] for ten, d in doi.items()])
    for to, nho in [('Giá token gấp đôi', 'Giá token giảm một nửa'), ('Tỉ lệ xem lại gấp đôi', 'Tỉ lệ xem lại giảm một nửa'),
                    ('Số ca làm lại gấp đôi', 'Số ca làm lại giảm một nửa')]:  # mô hình tuyến tính: "giảm một nửa" = -1/2 "gấp đôi"
        assert abs(doi[nho] + doi[to] / 2) < 1e-9, (to, nho)
    print('Tự kiểm: mỗi kịch bản "giảm một nửa" bằng đúng nửa mức tăng của "gấp đôi": ĐẠT')

    # ---------- B2 · đổi một cặp ----------
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    tong_rieng = doi['Giá token gấp đôi'] + doi['Tỉ lệ xem lại gấp đôi']
    print(f'\n== B2 · Giá token gấp đôi + tỉ lệ xem lại gấp đôi: {nghin(cap)} đ ({phan_tram(cap / goc["cps"] - 1, dau=True)}){sim}; '
          f'tổng hai tác động riêng {phan_tram(tong_rieng, dau=True)}')
    tang = {ten: d for ten, d in doi.items() if 'gấp đôi' in ten or 'tăng' in ten}
    print('Mức tăng theo từng yếu tố (để xếp hạng):', ', '.join(f'{t} {phan_tram(d, dau=True)}' for t, d in sorted(tang.items(), key=lambda x: -x[1])))

    # ---------- B3 · giới hạn chạy lại ----------
    dong = []
    for k in [1, 2, 3]:
        m = mo_hinh(runs, reqs, max_lan_chay=k)
        khong = len(reqs) - m['thanh_cong']
        dong.append([f'{k} lần', nghin(m['tong']) + ' đ', str(khong), nghin(m['tong'] + khong * BASELINE) + ' đ', nghin(m['cps']) + ' đ'])
    in_bang('B3 · Giới hạn chạy lại (cả hệ thống = tổng trợ lý + 12.000 đ × yêu cầu không thành công)',
            ['Giới hạn', 'Tổng chi phí trợ lý' + sim, 'Số yêu cầu không thành công', 'Chi phí cả hệ thống' + sim,
             'Chi phí mỗi việc thành công' + sim], dong)

    # ---------- B4 · xem lại 100% trong phạm vi noi_dia + hang_nang ----------
    run_pv = runs[runs['request_id'].isin(pv['request_id'])]
    co_ok = run_pv.loc[run_pv['status'] == 'ok', 'request_id'].nunique()  # yêu cầu có câu trả lời để xem lại
    ca_lam_lai = int((pv['ket_qua'] == 'lam_lai').sum())
    token_tool = (run_pv['tokens_in'] / 1000 * GIA_VAO + run_pv['tokens_out'] / 1000 * GIA_RA + run_pv['tool_calls'] * GIA_TOOL).sum()
    xem_100 = co_ok * PHUT_XEM_LAI_100 * LUONG_PHUT
    phut_lam_lai_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated']
    print(f'\n== B4 · Xem lại 100% (phạm vi noi_dia + hang_nang, {len(pv)} yêu cầu, {m_pv["thanh_cong"]} việc thành công)')
    for nhan, phut_ll in [(f'{PHUT_LAM_LAI_DE} phút làm lại/ca (đề bài)', PHUT_LAM_LAI_DE),
                          (f'{so(phut_lam_lai_tb.mean())} phút làm lại/ca (trung bình cột simulated, trung vị {so(phut_lam_lai_tb.median())})',
                           phut_lam_lai_tb.mean())]:
        lam_lai_tien = ca_lam_lai * phut_ll * LUONG_PHUT
        tong_b4 = token_tool + xem_100 + lam_lai_tien
        hoa_von = (BASELINE * m_pv['thanh_cong'] - token_tool - lam_lai_tien) / (co_ok * LUONG_PHUT)  # phút xem lại tối đa để bằng 12.000 đ
        print(f'- {nhan}: xem lại {co_ok} yêu cầu × {PHUT_XEM_LAI_100} phút = {nghin(xem_100)} đ; làm lại {ca_lam_lai} ca = {nghin(lam_lai_tien)} đ; '
              f'token + tool {nghin(token_tool)} đ; tổng {nghin(tong_b4)} đ → {nghin(tong_b4 / m_pv["thanh_cong"])} đ/việc = '
              f'{lan(tong_b4 / m_pv["thanh_cong"] / BASELINE)}{sim}; hoà vốn khi mỗi lần xem lại ≤ {so(hoa_von)} phút')

    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
