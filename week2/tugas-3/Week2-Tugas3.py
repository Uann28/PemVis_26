# Nama  : Juan Jordan Anugrah
# NIM   : F1D02310061
# Kelas : D

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QCheckBox, QPushButton, QFrame
from PySide6.QtCore import Qt

class FormLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikasi Form Login")
        self.resize(350, 450)
        
        self.setStyleSheet("QWidget { background-color: #f4f6f9; color: black; font-family: Arial; }")

        self.layout_utama = QVBoxLayout()
        self.layout_utama.setContentsMargins(25, 20, 25, 20)
        self.layout_utama.setSpacing(10)

        self.lbl_banner = QLabel("LOGIN")
        self.lbl_banner.setAlignment(Qt.AlignCenter)
        self.lbl_banner.setStyleSheet("background-color: #9b59b6; color: white; font-size: 16px; font-weight: bold; padding: 15px; border-radius: 6px;")

        self.style_input_default = """
            QLineEdit {
                background-color: white;
                border: 1px solid #ced4da;
                border-radius: 6px;
                padding: 8px;
                font-size: 14px;
            }
        """

        self.lbl_user = QLabel("Username:")
        self.input_user = QLineEdit()
        self.input_user.setStyleSheet(self.style_input_default)

        self.lbl_pass = QLabel("Password:")
        self.input_pass = QLineEdit()
        self.input_pass.setEchoMode(QLineEdit.Password)
        self.input_pass.setStyleSheet(self.style_input_default)

        self.cb_show = QCheckBox("Tampilkan Password")
        style_cb = """
            QCheckBox {
                font-size: 13px;
                margin-top: 5px;
                margin-bottom: 5px;
            }
            QCheckBox::indicator {
                width: 16px;
                height: 16px;
                border: 1px solid #7f8c8d;
                border-radius: 3px;
                background-color: white;
            }
            QCheckBox::indicator:checked {
                background-color: #27ae60;
                border: 1px solid #27ae60;
                image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'><polyline points='20 6 9 17 4 12'></polyline></svg>");
            }
        """
        self.cb_show.setStyleSheet(style_cb)
        self.cb_show.stateChanged.connect(self.toggle_password)

        self.layout_btn = QHBoxLayout()
        self.btn_login = QPushButton("Login")
        self.btn_login.setStyleSheet("background-color: #27ae60; color: white; border-radius: 6px; padding: 8px 0px; font-weight: bold;")
        self.btn_login.clicked.connect(self.proses_login)

        self.btn_reset = QPushButton("Reset")
        self.btn_reset.setStyleSheet("background-color: #95a5a6; color: white; border-radius: 6px; padding: 8px 0px; font-weight: bold;")
        self.btn_reset.clicked.connect(self.reset_form)

        self.layout_btn.addWidget(self.btn_login)
        self.layout_btn.addWidget(self.btn_reset)

        self.frame_hasil = QFrame()
        self.layout_hasil = QVBoxLayout()
        self.lbl_hasil = QLabel("")
        self.lbl_hasil.setWordWrap(True)
        self.layout_hasil.addWidget(self.lbl_hasil)
        self.frame_hasil.setLayout(self.layout_hasil)
        self.frame_hasil.hide()

        self.layout_utama.addWidget(self.lbl_banner)
        self.layout_utama.addSpacing(10)
        self.layout_utama.addWidget(self.lbl_user)
        self.layout_utama.addWidget(self.input_user)
        self.layout_utama.addSpacing(5)
        self.layout_utama.addWidget(self.lbl_pass)
        self.layout_utama.addWidget(self.input_pass)
        self.layout_utama.addWidget(self.cb_show)
        self.layout_utama.addLayout(self.layout_btn)
        self.layout_utama.addSpacing(10)
        self.layout_utama.addWidget(self.frame_hasil)
        self.layout_utama.addStretch()

        self.setLayout(self.layout_utama)

    def toggle_password(self):
        if self.cb_show.isChecked():
            self.input_pass.setEchoMode(QLineEdit.Normal)
        else:
            self.input_pass.setEchoMode(QLineEdit.Password)

    def proses_login(self):
        user = self.input_user.text()
        pwd = self.input_pass.text()

        if user == "admin" and pwd == "12345":
            style_input_sukses = "QLineEdit { background-color: #eaf4ea; border: 1px solid #27ae60; border-radius: 6px; padding: 8px; font-size: 14px; }"
            self.input_user.setStyleSheet(style_input_sukses)
            self.input_pass.setStyleSheet(style_input_sukses)
            
            self.frame_hasil.setStyleSheet("background-color: #d8ead3; border-left: 6px solid #1b5e20; border-radius: 6px;")
            self.lbl_hasil.setStyleSheet("color: #1b5e20; border: none;")
            self.lbl_hasil.setText("Login berhasil! Selamat datang, admin.")
        else:
            style_input_gagal = "QLineEdit { background-color: white; border: 1px solid #e74c3c; border-radius: 6px; padding: 8px; font-size: 14px; }"
            self.input_user.setStyleSheet(style_input_gagal)
            self.input_pass.setStyleSheet(style_input_gagal)
            
            self.frame_hasil.setStyleSheet("background-color: #f8d7da; border-left: 6px solid #dc3545; border-radius: 6px;")
            self.lbl_hasil.setStyleSheet("color: #721c24; border: none;")
            self.lbl_hasil.setText("Login gagal! Username atau password salah.")

        self.frame_hasil.show()

    def reset_form(self):
        self.input_user.setText("")
        self.input_pass.setText("")
        self.cb_show.setChecked(False)
        self.input_pass.setEchoMode(QLineEdit.Password)
        
        self.input_user.setStyleSheet(self.style_input_default)
        self.input_pass.setStyleSheet(self.style_input_default)
        
        self.frame_hasil.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormLogin()
    window.show()
    sys.exit(app.exec())