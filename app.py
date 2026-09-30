import streamlit as st

st.set_page_config(
    page_title="Tính Lãi Tiết Kiệm",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Ứng dụng Tính Lãi Gửi Tiết Kiệm")

st.markdown("---")

# Nhập dữ liệu
so_tien = st.number_input(
    "Số tiền gửi (VNĐ)",
    min_value=0.0,
    value=10000000.0,
    step=1000000.0,
    format="%.0f"
)

ky_han = st.number_input(
    "Kỳ hạn (tháng)",
    min_value=1,
    value=12,
    step=1
)

lai_suat = st.number_input(
    "Lãi suất (%/năm)",
    min_value=0.0,
    value=6.0,
    step=0.1
)

loai_lai = st.selectbox(
    "Loại tính lãi",
    ["Lãi đơn", "Lãi kép"]
)

hinh_thuc = st.selectbox(
    "Hình thức nhận lãi",
    [
        "Lãnh lãi theo tháng",
        "Lãnh lãi theo quý",
        "Lãnh lãi cuối kỳ"
    ]
)

st.markdown("---")

if st.button("Tính toán", use_container_width=True):

    lai_thang = lai_suat / 100 / 12

    # =====================
    # LÃI ĐƠN
    # =====================
    if loai_lai == "Lãi đơn":

        tong_lai = so_tien * lai_thang * ky_han

        if hinh_thuc == "Lãnh lãi theo tháng":
            lai_dinh_ky = so_tien * lai_thang

        elif hinh_thuc == "Lãnh lãi theo quý":
            lai_dinh_ky = so_tien * lai_thang * 3

        else:  # cuối kỳ
            lai_dinh_ky = tong_lai

        tong_goc_lai = so_tien + tong_lai

    # =====================
    # LÃI KÉP
    # =====================
    else:

        if hinh_thuc == "Lãnh lãi theo tháng":

            tong_goc_lai = so_tien * (1 + lai_thang) ** ky_han
            tong_lai = tong_goc_lai - so_tien

            lai_dinh_ky = so_tien * lai_thang

        elif hinh_thuc == "Lãnh lãi theo quý":

            lai_quy = lai_suat / 100 / 4
            so_quy = ky_han / 3

            tong_goc_lai = so_tien * (1 + lai_quy) ** so_quy
            tong_lai = tong_goc_lai - so_tien

            lai_dinh_ky = so_tien * lai_quy

        else:  # cuối kỳ

            tong_goc_lai = so_tien * (1 + lai_thang) ** ky_han
            tong_lai = tong_goc_lai - so_tien

            lai_dinh_ky = tong_lai

    # Hiển thị kết quả
    st.success("Tính toán thành công!")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Tiền lãi định kỳ",
            f"{lai_dinh_ky:,.0f} VNĐ"
        )

    with col2:
        st.metric(
            "Tổng tiền lãi",
            f"{tong_lai:,.0f} VNĐ"
        )

    with col3:
        st.metric(
            "Tổng gốc + lãi",
            f"{tong_goc_lai:,.0f} VNĐ"
        )

    st.markdown("---")

    st.subheader("📊 Chi tiết")

    st.write(f"**Số tiền gửi:** {so_tien:,.0f} VNĐ")
    st.write(f"**Kỳ hạn:** {ky_han} tháng")
    st.write(f"**Lãi suất:** {lai_suat:.2f}%/năm")
    st.write(f"**Loại lãi:** {loai_lai}")
    st.write(f"**Hình thức nhận lãi:** {hinh_thuc}")
