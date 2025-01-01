import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from ui.giris import Ui_MainWindow
from views.menu_ogrenci_kaydet import OgrenciKaydet
from db.database import init_db


class Giris(QMainWindow):
    def __init__(self):
        super(Giris, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.seasonStart = 0
        self.ogrenciKaydet = None
        self.kayitli_ogrenciler = None
        self.gelir_ekle = None
        self.gider_ekle = None
        self.setupButtons()
        init_db()

        self.ui.spin_giris_sezon_baslangic.valueChanged.connect(self.setupSpinSezon)

        self.setPassive()

    def setupSpinSezon(self):
        sayi = int(self.ui.spin_giris_sezon_baslangic.text())
        self.ui.spin_giris_sezon_bitis.setValue(sayi + 1)

    def setSezonStart(self):
        self.seasonStart = 1
        self.setActive()
        self.ui.spin_giris_sezon_baslangic.setEnabled(False)
        self.ui.spin_giris_sezon_bitis.setEnabled(False)
        self.ui.btn_sezonKaydet.setEnabled(False)

    def setPassive(self):
        if self.seasonStart == 0:
            # Muhasebe
            self.ui.menu_btn_aylik_tablo.setEnabled(False)
            self.ui.menu_btn_cari_goster.setEnabled(False)
            self.ui.menu_btn_gelir_ekle.setEnabled(False)
            self.ui.menu_btn_gider_ekle.setEnabled(False)
            self.ui.menu_btn_yillik_tablo.setEnabled(False)

            # Öğrenci
            self.ui.menu_btn_ogrenci_ekle.setEnabled(False)
            self.ui.menu_btn_kayitli_ogrenciler.setEnabled(False)
            self.ui.menu_btn_tahsilat_islemi.setEnabled(False)
            self.ui.menu_btn_tahsilat_raporu.setEnabled(False)
            self.ui.menu_btn_vadesi_gecmis_taksitler.setEnabled(False)
            self.ui.menu_btn_vadesi_gelen_taksitler.setEnabled(False)

    def setActive(self):
        if self.seasonStart == 1:
            # Muhasebe
            self.ui.menu_btn_aylik_tablo.setEnabled(True)
            self.ui.menu_btn_cari_goster.setEnabled(True)
            self.ui.menu_btn_gelir_ekle.setEnabled(True)
            self.ui.menu_btn_gider_ekle.setEnabled(True)
            self.ui.menu_btn_yillik_tablo.setEnabled(True)

            # Öğrenci
            self.ui.menu_btn_ogrenci_ekle.setEnabled(True)
            self.ui.menu_btn_kayitli_ogrenciler.setEnabled(True)
            self.ui.menu_btn_tahsilat_islemi.setEnabled(True)
            self.ui.menu_btn_tahsilat_raporu.setEnabled(True)
            self.ui.menu_btn_vadesi_gecmis_taksitler.setEnabled(True)
            self.ui.menu_btn_vadesi_gelen_taksitler.setEnabled(True)

    def setupButtons(self):

        self.ui.menu_btn_ogrenci_ekle.clicked.connect(self.openAddStudentMenu)
        self.ui.menu_btn_kayitli_ogrenciler.clicked.connect(
            self.openRegisteredStudentsMenu
        )
        self.ui.menu_btn_gelir_ekle.clicked.connect(self.openGelirEkleMenu)
        self.ui.menu_btn_gider_ekle.clicked.connect(self.openGiderEkleMenu)
        self.ui.btn_sezonKaydet.clicked.connect(self.setSezonStart)

    def openAddStudentMenu(self):
        if self.ogrenciKaydet and self.ogrenciKaydet.isVisible():
            QMessageBox.warning(self, "Hata", "Öğrenci kaydı penceresi zaten açık.")
        else:
            self.ogrenciKaydet = OgrenciKaydet()
            self.ogrenciKaydet.show()

    def openRegisteredStudentsMenu(self):
        if self.kayitli_ogrenciler and self.kayitli_ogrenciler.isVisible():
            QMessageBox.warning(
                self, "Hata", "Kayıtlı öğrenciler penceresi zaten açık."
            )
        else:
            self.kayitli_ogrenciler = KayitliOgrenciler()
            self.kayitli_ogrenciler.show()

    def openGelirEkleMenu(self):
        if self.gelir_ekle and self.gelir_ekle.isVisible():
            QMessageBox.warning(self, "Hata", "Gelir Ekleme penceresi zaten açık.")
        else:
            self.gelir_ekle = GelirEkle()
            self.gelir_ekle.show()

    def openGiderEkleMenu(self):
        if self.gider_ekle and self.gider_ekle.isVisible():
            QMessageBox.warning(self, "Hata", "Gider Ekleme penceresi zaten açık.")
        else:
            self.gider_ekle = GiderEkle()
            self.gider_ekle.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Giris()
    main_window.show()
    sys.exit(app.exec())
