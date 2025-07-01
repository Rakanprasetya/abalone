
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
- Streamlit
- Scikit-learn
- Pandas, NumPy
- Jupyter Notebook (`linear_regression.ipynb`)

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



---
