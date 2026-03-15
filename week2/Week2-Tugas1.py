import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox, QFrame

class FormBiodata(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikasi Form Biodata Mahasiswa")
        self.resize(450, 550)
        
        self.setStyleSheet("QWidget { background-color: #f8f9fa; color: black; font-family: Arial; }")

        self.layout_utama = QVBoxLayout()
        self.layout_utama.setContentsMargins(30, 20, 30, 20)
        self.layout_utama.setSpacing(10)

        style_input = """
            QLineEdit {
                background-color: #eaf4ea;
                border: 1px solid #5cb85c;
                border-radius: 6px;
                padding: 8px;
                font-size: 14px;
            }
        """

        style_combo = """
            QComboBox {
                background-color: white;
                border: 1px solid #ced4da;
                border-radius: 6px;
                padding: 8px;
                font-size: 14px;
            }
            
            QComboBox QAbstractItemView {
                background-color: white;
                color: black;
            }
        """

        self.lbl_nama = QLabel("Nama Lengkap:")
        self.input_nama = QLineEdit()
        self.input_nama.setStyleSheet(style_input)

        self.lbl_nim = QLabel("NIM:")
        self.input_nim = QLineEdit()
        self.input_nim.setPlaceholderText("Masukkan NIM")
        self.input_nim.setStyleSheet(style_input)

        self.lbl_kelas = QLabel("Kelas:")
        self.input_kelas = QLineEdit()
        self.input_kelas.setPlaceholderText("Contoh: TI-2A")
        self.input_kelas.setStyleSheet(style_input)

        self.lbl_jk = QLabel("Jenis Kelamin:")
        self.combo_jk = QComboBox()
        self.combo_jk.addItems(["Laki-laki", "Perempuan"])
        self.combo_jk.setPlaceholderText("Pilih Jenis Kelamin")
        self.combo_jk.setCurrentIndex(-1)
        self.combo_jk.setStyleSheet(style_combo)

        self.layout_btn = QHBoxLayout()
        self.btn_tampil = QPushButton("Tampilkan")
        self.btn_tampil.setStyleSheet("background-color: #3498db; color: white; border-radius: 6px; padding: 10px 15px;")
        self.btn_tampil.clicked.connect(self.tampilkan_data)

        self.btn_reset = QPushButton("Reset")
        self.btn_reset.setStyleSheet("background-color: #95a5a6; color: white; border-radius: 6px; padding: 10px 15px;")
        self.btn_reset.clicked.connect(self.reset_data)

        self.layout_btn.addWidget(self.btn_tampil)
        self.layout_btn.addWidget(self.btn_reset)
        self.layout_btn.addStretch()

        self.frame_hasil = QFrame()
        self.frame_hasil.setStyleSheet("background-color: #d8ead3; border-left: 4px solid #1b5e20; border-radius: 4px;")
        
        self.layout_hasil = QVBoxLayout()
        self.lbl_judul = QLabel("DATA BIODATA")
        self.lbl_judul.setStyleSheet("font-weight: bold; color: #003300; border: none;")
        self.lbl_isi = QLabel("")
        self.lbl_isi.setStyleSheet("color: #003300; border: none;")
        
        self.layout_hasil.addWidget(self.lbl_judul)
        self.layout_hasil.addWidget(self.lbl_isi)
        self.frame_hasil.setLayout(self.layout_hasil)
        self.frame_hasil.hide()

        self.layout_utama.addWidget(self.lbl_nama)
        self.layout_utama.addWidget(self.input_nama)
        self.layout_utama.addSpacing(5)
        self.layout_utama.addWidget(self.lbl_nim)
        self.layout_utama.addWidget(self.input_nim)
        self.layout_utama.addSpacing(5)
        self.layout_utama.addWidget(self.lbl_kelas)
        self.layout_utama.addWidget(self.input_kelas)
        self.layout_utama.addSpacing(5)
        self.layout_utama.addWidget(self.lbl_jk)
        self.layout_utama.addWidget(self.combo_jk)
        self.layout_utama.addSpacing(10)
        self.layout_utama.addLayout(self.layout_btn)
        self.layout_utama.addWidget(self.frame_hasil)
        self.layout_utama.addStretch()

        self.setLayout(self.layout_utama)

    def tampilkan_data(self):
        nama = self.input_nama.text()
        nim = self.input_nim.text()
        kelas = self.input_kelas.text()
        jk = self.combo_jk.currentText()

        if nama == "" or nim == "" or kelas == "" or jk == "":
            msg = QMessageBox()
            msg.setWindowTitle("Validasi")
            msg.setText("Semua field harus diisi!")
            msg.setStyleSheet("color: black; background-color: white;")
            msg.exec()
        else:
            hasil = f"Nama: {nama}\nNIM: {nim}\nKelas: {kelas}\nJenis Kelamin: {jk}"
            self.lbl_isi.setText(hasil)
            self.frame_hasil.show()

    def reset_data(self):
        self.input_nama.setText("")
        self.input_nim.setText("")
        self.input_kelas.setText("")
        self.combo_jk.setCurrentIndex(-1)
        self.frame_hasil.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormBiodata()
    window.show()
    sys.exit(app.exec())