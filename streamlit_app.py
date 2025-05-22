import streamlit as st

st.title("Cara turu nyenyak tanpa ketindihan")
st.write(
    "Beragama, meyakini bahwa tuhan ada & berdoa sebelum tidur. (jgn lupa niatnya tidur ya, bukan nguli 60 soal mtk"
)

st.image("64c5f432fdf27f66506429bfb56f7ca2.jpg") 
st.image("8ff452acf79a743fe577576c29ab4551.jpg") 

st.write(
    "Udah ah, cape"
)





st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
  st.write(f"{angka} adalah Bilangan Genap")
else:
  st.write(f"{angka} adalah Bilangan Ganjil")
