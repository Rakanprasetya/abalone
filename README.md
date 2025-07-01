
# 🐚 Abalone Age Predictor with Streamlit and Linear Regression

**Abalone Age Predictor** adalah aplikasi web interaktif berbasis **Streamlit** yang memprediksi umur abalone berdasarkan karakteristik fisiknya menggunakan model **Linear Regression**. Proyek ini merupakan bagian dari Capstone Project dalam bidang Data Science yang berfokus pada prediksi regresi dengan interpretabilitas tinggi.

---

## 🚀 Fitur Utama

- Prediksi jumlah cincin abalone (indikator umur biologis)
- Estimasi umur dalam tahun (Rings + 1.5)
- Aplikasi berbasis web interaktif menggunakan **Streamlit**
- Model Machine Learning yang telah dilatih dan disimpan dalam format `.joblib`
- Teknik rekayasa fitur canggih untuk meningkatkan akurasi model

---

## 🧠 Teknologi yang Digunakan

- Python 3.x
- Streamlit
- Scikit-learn
- Pandas, NumPy
- Joblib
- Jupyter Notebook (`linear_regression.ipynb`)

---

## 📁 Struktur Folder

```
abalone-age-predictor/
│
├── streamlit_app.py                  # Aplikasi Streamlit untuk prediksi umur abalone
├── abalone_prediction_model.joblib   # Model Linear Regression yang sudah dilatih
├── linear_regression.ipynb           # Notebook eksplorasi data, preprocessing, modeling
└── README.md                         # Dokumentasi proyek
```

---

## 🎯 Cara Menjalankan Aplikasi

### 1. Clone Repository
```bash
git clone https://github.com/username/abalone-age-predictor.git
cd abalone-age-predictor
```

### 2. Install Dependencies
Disarankan menggunakan virtual environment.
```bash
pip install -r requirements.txt
```

Jika belum ada `requirements.txt`, instal manual:
```bash
pip install streamlit scikit-learn pandas numpy joblib
```

### 3. Jalankan Aplikasi
```bash
streamlit run streamlit_app.py
```

Akses aplikasi di browser Anda: `http://localhost:8501`

---

## 📊 Deskripsi Model

Model dikembangkan menggunakan algoritma **Linear Regression** setelah melalui beberapa tahap:
- Eksplorasi dataset abalone
- Feature engineering (rasio panjang, berat, dan encoding kategorikal)
- Transformasi log target (opsional)
- Evaluasi dengan MSE & R² Score

File `linear_regression.ipynb` mendokumentasikan seluruh proses training.

---

## 📦 Dataset

Dataset yang digunakan berasal dari [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/abalone), dengan label target berupa jumlah cincin (`Rings`) yang kemudian dikonversi ke estimasi umur (`Age = Rings + 1.5`).

---

## 👨‍💻 Tim Pengembang

- Muhammad Hilmy Munsarif  
- Muhammad Naufal Ariq  
- Rakan Shafy Prasetya

---

## 📌 Lisensi

Proyek ini dapat digunakan untuk keperluan pembelajaran dan non-komersial. Untuk penggunaan lainnya, silakan hubungi pengembang.

---

## 💡 Catatan

Jika model gagal dimuat di Streamlit, pastikan file `abalone_prediction_model.joblib` berada pada path:  
```bash
./src/abalone_prediction_model.joblib
```
Atau sesuaikan path di dalam `streamlit_app.py`.

---
