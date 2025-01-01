from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtCore import QDate, QRegExp

from db.studentManagement import StudentManagement

from ui.ogrenci_kaydet import Ui_window_ogrenci_kaydet


class OgrenciKaydet(QMainWindow):
    def __init__(self):
        super(OgrenciKaydet, self).__init__()
        self.ui = Ui_window_ogrenci_kaydet()
        self.ui.setupUi(self)

        self.setupValidators()
        self.setupLineEdits()
        self.settings()
        self.setupButtons()

        self.student_management = StudentManagement()

    def settings(self):
        """Giriş alanlarını ve tarih seçimlerini varsayılan değerlere ayarlar."""
        self.ui.cbox_ogrenci_karti_sinifi.setCurrentIndex(-1)
        self.ui.dateEdit_ogrenci_karti_kayit_tarihi.setDate(QDate.currentDate())
        self.ui.dateEdit_ogrenci_karti_dogum_tarihi.setDate(QDate.currentDate())
        self.ui.dateEdit_ogrenci_karti_taksit_baslangic_tarihi.setDate(
            QDate.currentDate()
        )

    def setupButtons(self):
        """Butonlara işlevler bağlanır."""
        # Buton Bağlantıları
        self.ui.btn_ogrenci_karti_kaydet.clicked.connect(self.save_student_to_db)
        # self.ui.btn_yazdir_ogrenci_karti_kayit_formu.clicked.connect(self.sssss)

    def setupCbox(self):
        self.ui.cbox_ogrenci_karti_sinifi.currentIndexChanged.connect(
            self.update_ogrenci_no
        )

    def setupLineEdits(self):
        """LineEdit alanları için gerekli bağlantılar yapılır."""
        self.ui.le_ogrenci_karti_ogrenim_ucreti_tutar.editingFinished.connect(
            self.set_student_price_informations
        )
        self.ui.le_ogrenci_karti_ogrenim_ucreti_indirim_tutari.editingFinished.connect(
            self.set_student_price_informations
        )
        self.ui.le_ogrenci_karti_yayin_ucreti_tutar.editingFinished.connect(
            self.set_student_price_informations
        )
        self.ui.le_ogrenci_karti_yayin_ucreti_indirim_tutari.editingFinished.connect(
            self.set_student_price_informations
        )

    def setupValidators(self):
        """Giriş alanları için doğrulayıcılar ayarlanır."""
        self.ui.le_ogrenci_karti_ogrenim_ucreti_tutar.setValidator(QIntValidator())
        self.ui.le_ogrenci_karti_ogrenim_ucreti_indirim_tutari.setValidator(
            QIntValidator()
        )
        self.ui.le_ogrenci_karti_yayin_ucreti_tutar.setValidator(QIntValidator())
        self.ui.le_ogrenci_karti_yayin_ucreti_indirim_tutari.setValidator(
            QIntValidator()
        )
        self.ui.le_ogrenci_karti_adi.setValidator(
            QRegExpValidator(QRegExp("[a-zA-Z ]*"))
        )
        self.ui.le_ogrenci_karti_soyadi.setValidator(
            QRegExpValidator(QRegExp("[a-zA-Z ]*"))
        )
        self.ui.le_ogrenci_karti_tcno.setValidator(QIntValidator())
        self.ui.le_ogrenci_karti_cep_tel.setValidator(QIntValidator())

    def get_field_text(self, field, default="nothing"):
        """Bir giriş alanının (LineEdit) metnini döndürür. Boşsa varsayılan değeri döndürür."""
        text = field.text()
        return text if len(text) > 0 else default

    def get_field_text_price(self, field, default=0):
        """Bir giriş alanının fiyat değerini float olarak döndürür."""
        text = field.text()
        try:
            return float(text) if text else default
        except ValueError:
            return default

    def update_registration_fee(self):
        try:
            ogrenim_ucreti = self.get_field_text_price(
                self.ui.le_ogrenci_karti_ogrenim_ucreti_tutar
            )
            indirim_tutari = self.get_field_text_price(
                self.ui.le_ogrenci_karti_ogrenim_ucreti_indirim_tutari
            )
            kayit_ucreti = ogrenim_ucreti - (ogrenim_ucreti * indirim_tutari / 100)
            self.ui.le_ogrenci_karti_kayit_ucreti.setText(str(kayit_ucreti))
        except ValueError:
            QMessageBox.warning(
                self, "Hata", "Geçersiz öğrenim ücreti veya indirim tutarı."
            )

    def set_student_price_informations(self):
        """Öğrencinin öğrenim ve yayın ücretleriyle ilgili bilgileri hesaplar ve günceller."""
        try:
            ogr_ogrenim_ucreti = self.get_field_text_price(
                self.ui.le_ogrenci_karti_ogrenim_ucreti_tutar
            )
            ogr_yayin_ucreti = self.get_field_text_price(
                self.ui.le_ogrenci_karti_yayin_ucreti_tutar
            )

            ogr_ogrenim_ucreti_indirim_tutari = self.get_field_text_price(
                self.ui.le_ogrenci_karti_ogrenim_ucreti_indirim_tutari
            )
            ogr_yayin_ucreti_indirim_tutari = self.get_field_text_price(
                self.ui.le_ogrenci_karti_yayin_ucreti_indirim_tutari
            )

            h_kayit_ucreti = ogr_ogrenim_ucreti - ogr_ogrenim_ucreti * (
                ogr_ogrenim_ucreti_indirim_tutari / 100
            )
            h_yayin_ucreti = ogr_yayin_ucreti - ogr_yayin_ucreti * (
                ogr_yayin_ucreti_indirim_tutari / 100
            )

            self.ui.le_ogrenci_karti_kayit_ucreti.setText(str(h_kayit_ucreti))

            self.ui.le_ogrenci_karti_yayin_ucreti_kayit_ucreti.setText(
                str(h_yayin_ucreti)
            )

            self.ui.le_ogrenci_karti_toplam_ucret.setText(
                str(h_kayit_ucreti + h_yayin_ucreti)
            )
        except ValueError:
            QMessageBox.warning(
                self, "Hata", "Geçersiz öğrenim ücreti veya indirim tutarı."
            )

    def save_student_to_db(self):
        """Öğrenci bilgilerini veritabanına kaydeder."""

        parent_data = {
            "anne_adi": self.get_field_text(self.ui.le_ogrenci_karti_anne_adi),
            "anne_soyadi": self.get_field_text(self.ui.le_ogrenci_karti_anne_soyadi),
            "anne_meslek": self.get_field_text(self.ui.le_ogrenci_karti_anne_meslek),
            "anne_tel": self.get_field_text(self.ui.le_ogrenci_karti_anne_tel),
            "baba_adi": self.get_field_text(self.ui.le_ogrenci_karti_baba_adi),
            "baba_soyadi": self.get_field_text(self.ui.le_ogrenci_karti_baba_soyadi),
            "baba_meslek": self.get_field_text(self.ui.le_ogrenci_karti_baba_meslek),
            "baba_tel": self.get_field_text(self.ui.le_ogrenci_karti_baba_tel),
        }

        student_data = {
            "student_no": self.get_field_text(self.ui.le_ogrenci_karti_no),
            "first_name": self.get_field_text(self.ui.le_ogrenci_karti_adi),
            "last_name": self.get_field_text(self.ui.le_ogrenci_karti_soyadi),
            "tc_no": self.get_field_text(self.ui.le_ogrenci_karti_tcno),
            "birth_date": self.ui.dateEdit_ogrenci_karti_dogum_tarihi.date().toString(
                "dd-MM-yyyy"
            ),
            "gender": self.ui.cbox_ogrenci_karti_cinsiyet.currentIndex(),
            "status": self.ui.cbox_ogrenci_karti_durumu.currentIndex(),
            "address": self.get_field_text(self.ui.le_ogrenci_karti_adres),
            "class_level": self.ui.cbox_ogrenci_karti_sinifi.currentIndex(),
            "registration_date": self.ui.dateEdit_ogrenci_karti_kayit_tarihi.date().toString(
                "dd-MM-yyyy"
            ),
            "registration_type": self.ui.cbox_ogrenci_karti_kayit_sekli.currentIndex(),
            "email": self.get_field_text(self.ui.le_ogrenci_karti_eposta),
            "phone": self.get_field_text(self.ui.le_ogrenci_karti_cep_tel),
            "notes": self.get_field_text(self.ui.le_ogrenci_karti_ozel_notlar),
            "total_debt": self.get_field_text_price(
                self.ui.le_ogrenci_karti_borclar_toplami
            ),
            "total_paid": self.get_field_text_price(
                self.ui.le_ogrenci_karti_odenen_toplam
            ),
            "total_unpaid": self.get_field_text_price(
                self.ui.le_ogrenci_karti_kalan_tutar
            ),
        }

        services_data = [
            {
                "total_fee": self.get_field_text_price(
                    self.ui.le_ogrenci_karti_toplam_ucret
                ),
                "publication_fee": self.get_field_text_price(
                    self.ui.le_ogrenci_karti_yayin_ucreti_kayit_ucreti
                ),
                "registration_fee": self.get_field_text_price(
                    self.ui.le_ogrenci_karti_kayit_ucreti
                ),
            }
        ]

        self.student_management.add_student(student_data, services_data, parent_data)
        self.reset_all()

    def reset_all(self):
        """Tüm giriş alanlarını varsayılan değerlere sıfırlar."""
        self.settings()
        self.ui.le_ogrenci_karti_adi.clear()
        self.ui.le_ogrenci_karti_soyadi.clear()
        self.ui.le_ogrenci_karti_tcno.clear()
        self.ui.le_ogrenci_karti_adres.clear()
        self.ui.le_ogrenci_karti_cep_tel.clear()
        self.ui.le_ogrenci_karti_eposta.clear()
        self.ui.le_ogrenci_karti_ozel_notlar.clear()
        self.ui.le_ogrenci_karti_anne_adi.clear()
        self.ui.le_ogrenci_karti_anne_soyadi.clear()
        self.ui.le_ogrenci_karti_anne_meslek.clear()
        self.ui.le_ogrenci_karti_anne_tel.clear()
        self.ui.le_ogrenci_karti_baba_adi.clear()
        self.ui.le_ogrenci_karti_baba_soyadi.clear()
        self.ui.le_ogrenci_karti_baba_meslek.clear()
        self.ui.le_ogrenci_karti_baba_tel.clear()
        self.ui.le_ogrenci_karti_ogrenim_ucreti_tutar.clear()
        self.ui.le_ogrenci_karti_ogrenim_ucreti_indirim_tutari.clear()
        self.ui.le_ogrenci_karti_yayin_ucreti_tutar.clear()
        self.ui.le_ogrenci_karti_yayin_ucreti_indirim_tutari.clear()
        self.ui.le_ogrenci_karti_kayit_ucreti.clear()
        self.ui.le_ogrenci_karti_yayin_ucreti_kayit_ucreti.clear()
        self.ui.le_ogrenci_karti_toplam_ucret.clear()
        self.ui.le_ogrenci_karti_borclar_toplami.clear()
        self.ui.le_ogrenci_karti_odenen_toplam.clear()
        self.ui.le_ogrenci_karti_kalan_tutar.clear()
        self.ui.cbox_ogrenci_karti_cinsiyet.setCurrentIndex(0)
        self.ui.cbox_ogrenci_karti_durumu.setCurrentIndex(0)
        self.ui.cbox_ogrenci_karti_sinifi.setCurrentIndex(0)
        self.ui.cbox_ogrenci_karti_kayit_sekli.setCurrentIndex(0)
