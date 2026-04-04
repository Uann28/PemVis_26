# Nama : Juan Jordan Anugrah
# NIM  : F1D02310061

import sys
import re
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                               QLabel, QLineEdit, QRadioButton, QPushButton, 
                               QStackedWidget, QFrame, QDateEdit, QButtonGroup,
                               QSizePolicy, QTextEdit)
from PySide6.QtCore import Qt, Signal, QDate

class FormDaftar(QWidget):
    ganti_halaman = Signal(int)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Registrasi")
        self.resize(550, 450) 
        self.setStyleSheet("background-color: #FFFFFF; font-family: 'Segoe UI', Arial; color: black;")
        self.langkah_sekarang = 0
        self.total_langkah = 3
        
        self.atur_tampilan()
        self.atur_tombol()
        self.update_layar(0)

    def atur_tampilan(self):
        self.layout_utama = QVBoxLayout(self)
        self.layout_utama.setContentsMargins(0, 0, 0, 0)
        self.layout_utama.setSpacing(0)

        self.gaya_biasa = "QLineEdit, QDateEdit, QTextEdit { border: 1px solid #CED4DA; border-radius: 6px; padding: 8px; font-size: 14px; background-color: white; color: black;}"
        self.gaya_bener = "QLineEdit, QDateEdit, QTextEdit { border: 2px solid #27AE60; border-radius: 6px; padding: 8px; font-size: 14px; background-color: white; color: black;}"
        self.gaya_salah = "QLineEdit, QTextEdit { border: 2px solid #F39C12; border-radius: 6px; padding: 8px; font-size: 14px; background-color: white; color: black;}"
        self.gaya_teks = "color: #7F8C8D; font-size: 13px; margin-bottom: 2px; background-color: transparent;"

        self.bingkai_atas = QFrame()
        self.bingkai_atas.setStyleSheet("background-color: #F8F9FA; border-bottom: 1px solid #E9ECEF;")
        layout_atas = QVBoxLayout(self.bingkai_atas)
        layout_atas.setContentsMargins(30, 20, 30, 20)

        self.layout_progres = QHBoxLayout()
        self.layout_progres.setAlignment(Qt.AlignCenter)
        
        self.bulatan = []
        self.garis = []
        self.teks_langkah = ["Data Pribadi", "Kontak", "Akun"]
        self.label_langkah = []

        for i in range(self.total_langkah):
            b = QLabel(str(i + 1))
            b.setAlignment(Qt.AlignCenter)
            b.setFixedSize(36, 36)
            self.bulatan.append(b)
            self.layout_progres.addWidget(b)

            if i < self.total_langkah - 1:
                g = QFrame()
                g.setFixedHeight(4)
                g.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                self.garis.append(g)
                self.layout_progres.addWidget(g)

        self.layout_teks_atas = QHBoxLayout()
        for i in range(self.total_langkah):
            l = QLabel(self.teks_langkah[i])
            l.setAlignment(Qt.AlignCenter)
            l.setFixedWidth(80)
            l.setStyleSheet("background-color: transparent;")
            self.label_langkah.append(l)
            self.layout_teks_atas.addWidget(l)
            if i < self.total_langkah - 1:
                self.layout_teks_atas.addStretch()

        layout_atas.addLayout(self.layout_progres)
        layout_atas.addSpacing(5)
        layout_atas.addLayout(self.layout_teks_atas)
        self.layout_utama.addWidget(self.bingkai_atas)

        self.tumpukan_halaman = QStackedWidget()
        self.tumpukan_halaman.setContentsMargins(30, 20, 30, 10)
        self.tumpukan_halaman.setStyleSheet("background-color: #FFFFFF;")
        
        self.buat_halaman_1()
        self.buat_halaman_2()
        self.buat_halaman_3()
        self.buat_halaman_4()

        self.layout_utama.addWidget(self.tumpukan_halaman)

        self.bingkai_bawah = QFrame()
        self.bingkai_bawah.setStyleSheet("background-color: #FFFFFF; border: none;")
        layout_bawah = QVBoxLayout(self.bingkai_bawah)
        layout_bawah.setContentsMargins(30, 15, 30, 20)

        layout_tombol = QHBoxLayout()
        
        self.tombol_kembali = QPushButton("← Kembali")
        self.tombol_kembali.setFixedSize(120, 40)
        self.tombol_kembali.setStyleSheet("QPushButton { background-color: #E9ECEF; color: #333; border: 1px solid #CED4DA; border-radius: 6px; font-size: 14px;} QPushButton:hover { background-color: #DEE2E6; }")
        
        self.tombol_lanjut = QPushButton("Lanjut →")
        self.tombol_lanjut.setFixedSize(120, 40)
        self.tombol_lanjut.setStyleSheet("QPushButton { background-color: #3498DB; color: white; border: none; border-radius: 6px; font-size: 14px; font-weight: bold;} QPushButton:disabled { background-color: #95A5A6; } QPushButton:hover:!disabled { background-color: #2980B9; }")

        layout_tombol.addWidget(self.tombol_kembali)
        layout_tombol.addStretch()
        layout_tombol.addWidget(self.tombol_lanjut)

        self.teks_bawah = QLabel("Step 1 dari 3 — Lengkapi semua field untuk melanjutkan")
        self.teks_bawah.setStyleSheet("color: #7F8C8D; font-size: 12px; background-color: transparent;")
        
        layout_bawah.addLayout(layout_tombol)
        layout_bawah.addSpacing(15)
        layout_bawah.addWidget(self.teks_bawah)

        self.layout_utama.addWidget(self.bingkai_bawah)

    def buat_halaman_1(self):
        halaman = QWidget()
        halaman.setStyleSheet("background-color: #FFFFFF;")
        layout = QVBoxLayout(halaman)
        layout.setAlignment(Qt.AlignTop)

        judul = QLabel("Step 1: Data Pribadi")
        judul.setStyleSheet("font-size: 18px; font-weight: bold; color: #2C3E50; margin-bottom: 15px; background-color: transparent;")
        layout.addWidget(judul)

        layout.addWidget(QLabel("Nama Lengkap", styleSheet=self.gaya_teks))
        self.isian_nama = QLineEdit()
        self.isian_nama.setStyleSheet(self.gaya_biasa)
        self.isian_nama.textChanged.connect(self.cek_halaman_1)
        layout.addWidget(self.isian_nama)
        layout.addSpacing(10)

        layout.addWidget(QLabel("Tanggal Lahir", styleSheet=self.gaya_teks))
        self.isian_tanggal = QDateEdit(QDate.currentDate())
        self.isian_tanggal.setDisplayFormat("dd/MM/yyyy")
        self.isian_tanggal.setCalendarPopup(True)
        self.isian_tanggal.setStyleSheet(self.gaya_biasa)
        self.isian_tanggal.dateChanged.connect(self.cek_halaman_1)
        
        gaya_kalender = "QCalendarWidget QWidget { background-color: white; color: black; } QCalendarWidget QToolButton { color: black; background-color: transparent; font-size: 14px; font-weight: bold; } QCalendarWidget QToolButton:hover { background-color: #E9ECEF; } QCalendarWidget QMenu { background-color: white; color: black; } QCalendarWidget QSpinBox { background-color: white; color: black; } QCalendarWidget QAbstractItemView:enabled { background-color: white; color: black; selection-background-color: #3498DB; selection-color: white; } QCalendarWidget QAbstractItemView:disabled { color: #BDC3C7; }"
        self.isian_tanggal.calendarWidget().setStyleSheet(gaya_kalender)
        layout.addWidget(self.isian_tanggal)
        layout.addSpacing(10)

        layout.addWidget(QLabel("Jenis Kelamin", styleSheet=self.gaya_teks))
        self.grup_kelamin = QButtonGroup(self)
        layout_jk = QHBoxLayout()
        self.pilih_cowok = QRadioButton("Laki-laki")
        self.pilih_cewek = QRadioButton("Perempuan")
        
        gaya_radio = "QRadioButton { color: black; font-size: 14px; background-color: transparent; } QRadioButton::indicator { width: 14px; height: 14px; border: 2px solid #CED4DA; border-radius: 8px; background-color: white; } QRadioButton::indicator:checked { border: 2px solid #3498DB; background-color: white; image: url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><circle cx='12' cy='12' r='6' fill='%233498DB'/></svg>\"); }"
        
        self.pilih_cowok.setStyleSheet(gaya_radio)
        self.pilih_cewek.setStyleSheet(gaya_radio)
        
        self.grup_kelamin.addButton(self.pilih_cowok)
        self.grup_kelamin.addButton(self.pilih_cewek)
        layout_jk.addWidget(self.pilih_cowok)
        layout_jk.addWidget(self.pilih_cewek)
        layout_jk.addStretch()
        layout.addLayout(layout_jk)
        
        self.pilih_cowok.toggled.connect(self.cek_halaman_1)
        self.pilih_cewek.toggled.connect(self.cek_halaman_1)

        self.tumpukan_halaman.addWidget(halaman)

    def buat_halaman_2(self):
        halaman = QWidget()
        halaman.setStyleSheet("background-color: #FFFFFF;")
        layout = QVBoxLayout(halaman)
        layout.setAlignment(Qt.AlignTop)

        judul = QLabel("Step 2: Informasi Kontak")
        judul.setStyleSheet("font-size: 18px; font-weight: bold; color: #2C3E50; margin-bottom: 15px; background-color: transparent;")
        layout.addWidget(judul)

        layout.addWidget(QLabel("Email", styleSheet=self.gaya_teks))
        self.isian_email = QLineEdit()
        self.isian_email.setPlaceholderText("contoh@email.com")
        self.isian_email.setStyleSheet(self.gaya_biasa)
        self.isian_email.textChanged.connect(self.cek_halaman_2)
        layout.addWidget(self.isian_email)
        layout.addSpacing(10)

        layout.addWidget(QLabel("Telepon", styleSheet=self.gaya_teks))
        self.isian_hape = QLineEdit()
        self.isian_hape.setStyleSheet(self.gaya_biasa)
        self.isian_hape.textChanged.connect(self.cek_halaman_2)
        layout.addWidget(self.isian_hape)
        
        self.peringatan_hape = QLabel("⚠ Nomor minimal 10 digit")
        self.peringatan_hape.setStyleSheet("color: #F39C12; font-size: 12px; background-color: transparent;")
        self.peringatan_hape.hide()
        layout.addWidget(self.peringatan_hape)
        layout.addSpacing(10)

        layout.addWidget(QLabel("Alamat Lengkap", styleSheet=self.gaya_teks))
        self.isian_alamat = QTextEdit()
        self.isian_alamat.setFixedHeight(60)
        self.isian_alamat.setStyleSheet(self.gaya_biasa)
        self.isian_alamat.textChanged.connect(self.cek_halaman_2)
        layout.addWidget(self.isian_alamat)

        self.tumpukan_halaman.addWidget(halaman)

    def buat_halaman_3(self):
        halaman = QWidget()
        halaman.setStyleSheet("background-color: #FFFFFF;")
        layout = QVBoxLayout(halaman)
        layout.setAlignment(Qt.AlignTop)

        judul = QLabel("Step 3: Informasi Akun")
        judul.setStyleSheet("font-size: 18px; font-weight: bold; color: #2C3E50; margin-bottom: 15px; background-color: transparent;")
        layout.addWidget(judul)

        layout.addWidget(QLabel("Username", styleSheet=self.gaya_teks))
        self.isian_user = QLineEdit()
        self.isian_user.setStyleSheet(self.gaya_biasa)
        self.isian_user.textChanged.connect(self.cek_halaman_3)
        layout.addWidget(self.isian_user)
        layout.addSpacing(10)

        layout.addWidget(QLabel("Password", styleSheet=self.gaya_teks))
        self.isian_sandi = QLineEdit()
        self.isian_sandi.setEchoMode(QLineEdit.Password)
        self.isian_sandi.setStyleSheet(self.gaya_biasa)
        self.isian_sandi.textChanged.connect(self.cek_halaman_3)
        layout.addWidget(self.isian_sandi)
        layout.addSpacing(10)

        layout.addWidget(QLabel("Konfirmasi Password", styleSheet=self.gaya_teks))
        self.isian_sandi2 = QLineEdit()
        self.isian_sandi2.setEchoMode(QLineEdit.Password)
        self.isian_sandi2.setStyleSheet(self.gaya_biasa)
        self.isian_sandi2.textChanged.connect(self.cek_halaman_3)
        layout.addWidget(self.isian_sandi2)

        self.peringatan_sandi = QLabel("⚠ Password tidak cocok")
        self.peringatan_sandi.setStyleSheet("color: #E74C3C; font-size: 12px; background-color: transparent;")
        self.peringatan_sandi.hide()
        layout.addWidget(self.peringatan_sandi)

        self.tumpukan_halaman.addWidget(halaman)

    def buat_halaman_4(self):
        halaman = QWidget()
        halaman.setStyleSheet("background-color: #FFFFFF;")
        layout = QVBoxLayout(halaman)
        layout.setAlignment(Qt.AlignTop)

        judul = QLabel("Review Data Registrasi")
        judul.setStyleSheet("font-size: 18px; font-weight: bold; color: #2C3E50; margin-bottom: 15px; background-color: transparent;")
        layout.addWidget(judul)

        self.teks_hasil = QLabel("")
        self.teks_hasil.setStyleSheet("font-size: 14px; color: black; line-height: 1.5; background-color: transparent;")
        self.teks_hasil.setWordWrap(True)
        layout.addWidget(self.teks_hasil)

        self.tumpukan_halaman.addWidget(halaman)

    def cek_halaman_1(self):
        nama_ok = len(self.isian_nama.text().strip()) >= 3
        jk_ok = self.pilih_cowok.isChecked() or self.pilih_cewek.isChecked()
        
        if nama_ok:
            self.isian_nama.setStyleSheet(self.gaya_bener)
        elif len(self.isian_nama.text()) > 0:
            self.isian_nama.setStyleSheet(self.gaya_salah)
        else:
            self.isian_nama.setStyleSheet(self.gaya_biasa)

        self.isian_tanggal.setStyleSheet(self.gaya_bener)

        self.tombol_lanjut.setEnabled(nama_ok and jk_ok)

    def cek_halaman_2(self):
        email = self.isian_email.text()
        hape = self.isian_hape.text()
        alamat = self.isian_alamat.toPlainText()

        email_ok = bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))
        if email_ok:
            self.isian_email.setStyleSheet(self.gaya_bener)
        elif len(email) > 0:
            self.isian_email.setStyleSheet(self.gaya_salah)
        else:
            self.isian_email.setStyleSheet(self.gaya_biasa)

        hape_ok = hape.isdigit() and len(hape) >= 10
        if hape_ok:
            self.isian_hape.setStyleSheet(self.gaya_bener)
            self.peringatan_hape.hide()
        elif len(hape) > 0:
            self.isian_hape.setStyleSheet(self.gaya_salah)
            self.peringatan_hape.show()
        else:
            self.isian_hape.setStyleSheet(self.gaya_biasa)
            self.peringatan_hape.hide()

        alamat_ok = len(alamat.strip()) >= 5
        if alamat_ok:
            self.isian_alamat.setStyleSheet(self.gaya_bener)
        elif len(alamat) > 0:
            self.isian_alamat.setStyleSheet(self.gaya_salah)
        else:
            self.isian_alamat.setStyleSheet(self.gaya_biasa)

        self.tombol_lanjut.setEnabled(email_ok and hape_ok and alamat_ok)

    def cek_halaman_3(self):
        user = self.isian_user.text()
        sandi1 = self.isian_sandi.text()
        sandi2 = self.isian_sandi2.text()

        user_ok = len(user) >= 4
        if user_ok:
            self.isian_user.setStyleSheet(self.gaya_bener)
        else:
            if len(user) == 0:
                self.isian_user.setStyleSheet(self.gaya_biasa)
            else:
                self.isian_user.setStyleSheet(self.gaya_salah)

        sandi_ok = len(sandi1) >= 6
        if sandi_ok:
            self.isian_sandi.setStyleSheet(self.gaya_bener)
        else:
            if len(sandi1) == 0:
                self.isian_sandi.setStyleSheet(self.gaya_biasa)
            else:
                self.isian_sandi.setStyleSheet(self.gaya_salah)

        cocok = sandi1 == sandi2 and sandi_ok
        if cocok:
            self.isian_sandi2.setStyleSheet(self.gaya_bener)
            self.peringatan_sandi.hide()
        elif len(sandi2) > 0:
            self.isian_sandi2.setStyleSheet(self.gaya_salah)
            self.peringatan_sandi.show()
        else:
            self.isian_sandi2.setStyleSheet(self.gaya_biasa)
            self.peringatan_sandi.hide()

        self.tombol_lanjut.setEnabled(user_ok and sandi_ok and cocok)

    def atur_tombol(self):
        self.tombol_lanjut.clicked.connect(self.maju)
        self.tombol_kembali.clicked.connect(self.mundur)
        self.ganti_halaman.connect(self.update_layar)

    def maju(self):
        if self.langkah_sekarang < self.total_langkah:
            if self.langkah_sekarang == 2:
                self.siapkan_review()
            self.langkah_sekarang += 1
            self.tumpukan_halaman.setCurrentIndex(self.langkah_sekarang)
            self.ganti_halaman.emit(self.langkah_sekarang) 

    def mundur(self):
        if self.langkah_sekarang > 0:
            self.langkah_sekarang -= 1
            self.tumpukan_halaman.setCurrentIndex(self.langkah_sekarang)
            self.ganti_halaman.emit(self.langkah_sekarang) 

    def siapkan_review(self):
        if self.pilih_cowok.isChecked():
            jk = "Laki-laki"
        else:
            jk = "Perempuan"
        
        tulisan = f"<b>Data Pribadi:</b><br>Nama: {self.isian_nama.text()}<br>Tanggal Lahir: {self.isian_tanggal.date().toString('dd/MM/yyyy')}<br>Jenis Kelamin: {jk}<br><br><b>Informasi Kontak:</b><br>Email: {self.isian_email.text()}<br>Telepon: {self.isian_hape.text()}<br>Alamat: {self.isian_alamat.toPlainText()}<br><br><b>Informasi Akun:</b><br>Username: {self.isian_user.text()}"
        self.teks_hasil.setText(tulisan)

    def update_layar(self, langkah):
        if langkah == 0:
            self.cek_halaman_1()
        elif langkah == 1:
            self.cek_halaman_2()
        elif langkah == 2:
            self.cek_halaman_3()

        if langkah == self.total_langkah:
            self.tombol_lanjut.setText("Submit Data")
            self.tombol_lanjut.setStyleSheet("background-color: #27AE60; color: white; border-radius: 6px; font-weight: bold;")
            self.teks_bawah.setText("Review kembali data Anda sebelum melakukan submit.")
            self.tombol_lanjut.setEnabled(True)
        else:
            self.tombol_lanjut.setText("Lanjut →")
            self.tombol_lanjut.setStyleSheet("QPushButton { background-color: #3498DB; color: white; border: none; border-radius: 6px; font-size: 14px; font-weight: bold;} QPushButton:disabled { background-color: #95A5A6; } QPushButton:hover:!disabled { background-color: #2980B9; }")
            self.teks_bawah.setText(f"Step {langkah + 1} dari {self.total_langkah} — Lengkapi semua field untuk melanjutkan")

        if langkah > 0:
            self.tombol_kembali.setVisible(True)
        else:
            self.tombol_kembali.setVisible(False)

        for i in range(self.total_langkah):
            if i < langkah:
                self.bulatan[i].setText("✔")
                self.bulatan[i].setStyleSheet("background-color: #27AE60; color: white; border-radius: 18px; font-size: 16px; font-weight: bold;")
                self.label_langkah[i].setStyleSheet("color: #27AE60; font-size: 12px; background-color: transparent;")
                if i < self.total_langkah - 1:
                    self.garis[i].setStyleSheet("background-color: #27AE60;")
            elif i == langkah:
                self.bulatan[i].setText(str(i + 1))
                self.bulatan[i].setStyleSheet("background-color: #3498DB; color: white; border-radius: 18px; font-size: 14px; font-weight: bold;")
                self.label_langkah[i].setStyleSheet("color: #3498DB; font-size: 12px; font-weight: bold; background-color: transparent;")
                if i < self.total_langkah - 1:
                    self.garis[i].setStyleSheet("background-color: #CED4DA;")
            else:
                self.bulatan[i].setText(str(i + 1))
                self.bulatan[i].setStyleSheet("background-color: #CED4DA; color: white; border-radius: 18px; font-size: 14px; font-weight: bold;")
                self.label_langkah[i].setStyleSheet("color: #7F8C8D; font-size: 12px; background-color: transparent;")
                if i < self.total_langkah - 1:
                    self.garis[i].setStyleSheet("background-color: #CED4DA;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    jendela = FormDaftar()
    jendela.show()
    sys.exit(app.exec())