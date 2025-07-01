import streamlit as st

# WAJIB: set_page_config harus di paling atas sebelum perintah streamlit lainnya
st.set_page_config(
    page_title="Abalone Age Predictor",
    page_icon="🐚",
    layout="centered"
)

import pandas as pd
import numpy as np
import joblib
import os

# =====================================================================================
# 1. DEFINISI CLASS (harus sama seperti yang digunakan saat menyimpan joblib)
# =====================================================================================
class AbalonePredictionModel:
    def __init__(self, model, preprocessor, categorical_cols, encoding_maps, log_transform=False):
        self.model = model
        self.preprocessor = preprocessor
        self.categorical_cols = categorical_cols
        self.encoding_maps = encoding_maps
        self.log_transform = log_transform
        self.global_mean = None

    def prepare_features(self, data):
        if isinstance(data, dict):
            data = pd.DataFrame([data])
        df = data.copy()

        # Feature Engineering
        df["Weight_to_Length"] = df["WholeWeight"] / df["Length"]
        df["Length_to_Diameter"] = df["Length"] / df["Diameter"]
        df["Shell_to_WholeWeight"] = df["ShellWeight"] / df["WholeWeight"]
        df["InnerWeight"] = df["ShuckedWeight"] + df["VisceraWeight"]
        df["Height_to_Length"] = df["Height"] / df["Length"]

        # Target Encoding
        for col in self.categorical_cols:
            encoding_map = self.encoding_maps.get(col, {})
            df[f'{col}_encoded'] = df[col].map(encoding_map)
            if df[f'{col}_encoded'].isna().any():
                df[f'{col}_encoded'].fillna(self.global_mean, inplace=True)

        return df

    def predict(self, data):
        df_prepared = self.prepare_features(data)
        X_transformed = self.preprocessor.transform(df_prepared)
        pred_log = self.model.predict(X_transformed)
        pred = np.expm1(pred_log) if self.log_transform else pred_log
        return pred[0]

# =====================================================================================
# 2. LOAD MODEL
# =====================================================================================
@st.cache_resource
def load_model():
    try:
        model = joblib.load("./src/abalone_prediction_model.joblib")
        return model, None
    except Exception as e:
        return None, str(e)

model_bundle, error = load_model()
if model_bundle is None:
    st.error(f"Gagal memuat model: {error}")
    st.stop()

# =====================================================================================
# 3. HALAMAN UTAMA
# =====================================================================================
st.title("🐚 Abalone Age Predictor")
st.write("Masukkan data abalone untuk memprediksi jumlah rings (umur).")

# =====================================================================================
# 4. FORM INPUT FITUR
# =====================================================================================
with st.form("input_form"):
    st.subheader("🔢 Input Data Abalone")
    col1, col2, col3 = st.columns(3)

    with col1:
        sex = st.selectbox("Sex", ["M", "F", "I"])
        length = st.number_input("Length", 0.01, 1.0, 0.5, step=0.01)
        diameter = st.number_input("Diameter", 0.01, 1.0, 0.4, step=0.01)

    with col2:
        height = st.number_input("Height", 0.01, 1.0, 0.15, step=0.01)
        whole_weight = st.number_input("Whole Weight", 0.01, 3.0, 1.0, step=0.01)
        shucked_weight = st.number_input("Shucked Weight", 0.01, 2.0, 0.4, step=0.01)

    with col3:
        viscera_weight = st.number_input("Viscera Weight", 0.01, 1.5, 0.2, step=0.01)
        shell_weight = st.number_input("Shell Weight", 0.01, 2.0, 0.3, step=0.01)

    submitted = st.form_submit_button("🔍 Predict Age")

# =====================================================================================
# 5. PREDIKSI
# =====================================================================================
if submitted:
    try:
        input_data = {
            "Sex": sex,
            "Length": length,
            "Diameter": diameter,
            "Height": height,
            "WholeWeight": whole_weight,
            "ShuckedWeight": shucked_weight,
            "VisceraWeight": viscera_weight,
            "ShellWeight": shell_weight
        }

        # Prediksi
        pred_rings = model_bundle.predict(input_data)
        estimated_age = pred_rings + 1.5  # Umur = Rings + 1.5

        st.success(f"🔮 Prediksi Jumlah Cincin: {pred_rings:.2f}")
        st.info(f"📅 Estimasi Umur Abalone: **{estimated_age:.2f} tahun**")

    except Exception as e:
        st.error(f"Terjadi error saat prediksi: {e}")

# Footer
st.markdown("---")
st.markdown("*Built with Streamlit • Muhammad Hilmy Munsarif, Muhammad Naufal Ariq, Rakan Shafy Prasetya*")
