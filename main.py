import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QTableWidgetItem, QTableWidget, QLabel, QFrame, QDesktopWidget, QFileDialog, QTextEdit
from PyQt5.QtCore import Qt 
import pygame
import time
import numpy as np
import math
import os

SM1 = []
SM2 = []
SM3 = []
SM4 = []
RNOTA = ["Do","Re","Mi","Fa","Sol","La","Si"]

def play_music(notes):
    # Pygame başlatma
    pygame.init()                                               #  Yc_Yusuf_Ciğerci

    # Ses çıkışı ayarları
    pygame.mixer.init()

    # Ses çalma fonksiyonu
    def play_sound(note):
        # Ses dosyasını yükle
        sound = pygame.mixer.Sound(f"Music-Player/midi_notes/{note}.wav")
        sound.play()

        # Ses dosyasının uzunluğunu al
        duration = sound.get_length()

        # Ses dosyasının çalınmasını bekle>
        time.sleep(duration-2)

    # Müziği çalma
    for note in notes:
        try:
            play_sound(note)
        except Exception as e:
            print(f"{note} için ses dosyası bulunamadı veya çalınamadı: {e}")

    # Pygame kapatma
    pygame.quit()


def notalari_hesapla_1(veri):
    columns_to_convert = [1, 3, 5, 7]  # 2., 4., 6. ve 8. sütunlar
    notes = []  # Notaları tutacak bir liste oluştur
    for col_index in columns_to_convert:
        column_header = veri.columns[col_index]
        column_data = veri.iloc[:, col_index]
        for i, value in enumerate(column_data):
            if pd.notna(value):  # Eğer hücrede veri varsa
                note = notaya_cevir_1(value)
                notes.append((column_header, note))

    return notes

def notalari_hesapla_2(veri):
    columns_to_convert = [1, 3, 5, 7]  # 2., 4., 6. ve 8. sütunlar
    notes = []  # Notaları tutacak bir liste oluştur
    for col_index in columns_to_convert:
        column_header = veri.columns[col_index]
        column_data = veri.iloc[:, col_index]
        for i, value in enumerate(column_data):
            if pd.notna(value):  # Eğer hücrede veri varsa
                note = notaya_cevir_2(value)
                notes.append((column_header, note))

    return notes

def notalari_hesapla_3(veri):
    columns_to_convert = [1, 3, 5, 7]  # 2., 4., 6. ve 8. sütunlar
    notes = []  # Notaları tutacak bir liste oluştur
    for col_index in columns_to_convert:
        column_header = veri.columns[col_index]
        column_data = veri.iloc[:, col_index]
        for i, value in enumerate(column_data):
            if pd.notna(value):  # Eğer hücrede veri varsa
                note = notaya_cevir_3(value)
                notes.append((column_header, note))

    return notes

def notalari_hesapla_4(veri):
    columns_to_convert = [1, 3, 5, 7]  # 2., 4., 6. ve 8. sütunlar
    notes = []  # Notaları tutacak bir liste oluştur
    for col_index in columns_to_convert:
        column_header = veri.columns[col_index]
        column_data = veri.iloc[:, col_index]
        for i, value in enumerate(column_data):
            if pd.notna(value):  # Eğer hücrede veri varsa
                note = notaya_cevir_4(value)
                notes.append((column_header, note))

    return notes

def notaya_cevir_1(deger):
    if 0 <= deger < 0.2:
        return "Do"
    elif 0.2 <= deger < 0.4:
        return "Re"
    elif 0.4 <= deger < 0.6:
        return "Mi"
    elif 0.6 <= deger < 0.8:
        return "Fa"
    elif 0.8 <= deger < 1:
        return "Sol"
    else:
        return "Belirsiz"

def notaya_cevir_2(deger):

    try:
        deger = float(deger)
    except ValueError:
        return "Belirsiz"
    
    if 0 <= deger < 0.2:
        return "Do"
    elif 0.2 <= deger < 0.4:
        return "Re"
    elif 0.4 <= deger < 0.6:
        return "Mi"
    elif 0.6 <= deger < 0.8:
        return "Fa"
    elif 0.8 <= deger < 1:
        return "Sol"
    else:
        return "Belirsiz"

def notaya_cevir_3(deger):
    if 100 <= deger < 142943:
        return "Do"
    elif 142943 <= deger < 285786:
        return "Re"
    elif 285786 <= deger < 428629:
        return "Mi"
    elif 428629 <= deger < 571472:
        return "Fa"
    elif 571472 <= deger < 714315:
        return "Sol"
    elif 714315 <= deger < 857758:
        return "La"
    elif 857758 <= deger < 1000001:
        return "Si"
    else:
        return "Belirsiz"

def notaya_cevir_4(deger):
    if 100 <= deger < 142943:
        return "Do"
    elif 142943 <= deger < 285786:
        return "Re"
    elif 285786 <= deger < 428629:
        return "Mi"
    elif 428629 <= deger < 571472:
        return "Fa"
    elif 571472 <= deger < 714315:
        return "Sol"
    elif 714315 <= deger < 857758:
        return "La"
    elif 857758 <= deger < 1000001:
        return "Si"
    else:
        return "Belirsiz"

class AnaPencere(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("background-color: #222; color: white;") 

        self.setWindowTitle("Ana Pencere")

        ekran = QDesktopWidget().screenGeometry()
        genislik = ekran.width() // 2
        yukseklik = int(ekran.height() * 0.9)
        self.setGeometry(0, 0, genislik, yukseklik)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        ust_layout = QGridLayout()
        alt_layout = QGridLayout()

        dikdortgen_etiketi = QLabel("CERN BEAM PLAYER")
        dikdortgen_etiketi.setAlignment(Qt.AlignCenter)
        dikdortgen_etiketi.setStyleSheet("font-size: 20pt; font-weight: bold;")
        dikdortgen = QFrame()
        dikdortgen.setFrameShape(QFrame.Box)
        dikdortgen.setStyleSheet("background-color: #333; border: 2px solid black;")
        dikdortgen_layout = QVBoxLayout()
        dikdortgen_layout.addWidget(dikdortgen_etiketi)
        dikdortgen.setLayout(dikdortgen_layout)

        # Sütun başlıkları
        sutun_basliklari = ["Yusuf", "Tuğra", "Enver", "Enes", "Duru", "Betül", "Şevval", "Atakan"]

        for i in range(4):
            tablo = QTableWidget(10, 8)
            tablo.setObjectName(f"tablo_{i}")  # Tablo nesnelerine uygun isim verildi
            tablo.setFixedSize(genislik // 2, yukseklik // 3)
            tablo.setStyleSheet("QTableWidget { background-color: #444; color: white; border: 2px solid black; }"
                                "QHeaderView::section { background-color: black; color: white; }")
            tablo.verticalHeader().setVisible(False)  

            tablo_basligi = QLabel(f"SETUP {i + 1}")
            tablo_basligi.setAlignment(Qt.AlignCenter)
            tablo_basligi.setStyleSheet("font-weight: bold; font-size: 16pt;")  
            tablo_basligi.setFixedSize(genislik // 2, tablo_basligi.fontMetrics().height() + 10)

            if i == 2:  # SETUP 3 için sütun başlıklarını değiştir
                sutun_basliklari = ["Ciğerci", "Çalışkan", "Balcı", "Arıcan", "Yıldızay", "Sayın", "Sin/Cos", "Kaya"]

            for j, baslik in enumerate(sutun_basliklari):
                tablo.setHorizontalHeaderItem(j, QTableWidgetItem(baslik))

            if i < 2:
                ust_layout.addWidget(tablo_basligi, 0, i)
                ust_layout.addWidget(tablo, 1, i)
            else:
                alt_layout.addWidget(tablo_basligi, 0, i - 2)
                alt_layout.addWidget(tablo, 1, i - 2)

        # PLAY ve benzeri düğmelerin layoutu
        play_layout = QHBoxLayout()
        play_layout.setAlignment(Qt.AlignCenter)

        for i in range(1, 5):  # Play 5 butonu çıkarıldı
            düğme = QPushButton(f"PLAY {i}")
            düğme.setFixedSize(150, 50)
            düğme.setStyleSheet("background-color: #555; color: white; border: 1px solid black;")
            düğme.clicked.connect(self.butona_basildi)
            play_layout.addWidget(düğme)

        # CSV ekleme düğmelerinin layoutu
        csv_layout = QHBoxLayout()
        csv_layout.setAlignment(Qt.AlignCenter)

        for i, konum in enumerate(["sol üst", "sağ üst", "sol alt", "sağ alt"]):
            düğme = QPushButton(f"Add_csv {i+1}")
            düğme.setProperty("konum", konum)
            düğme.setFixedSize(150, 50)
            düğme.setStyleSheet("background-color: #555; color: white; border: 1px solid black;")
            düğme.clicked.connect(lambda _, index=i+1: self.csv_ekle(index))
            csv_layout.addWidget(düğme)

        # Layout'a bileşenleri ekle
        layout.addWidget(dikdortgen)
        layout.addSpacing(20)  
        layout.addLayout(ust_layout)
        layout.addSpacing(20)
        layout.addLayout(alt_layout)
        layout.addSpacing(20)
        layout.addLayout(play_layout)
        layout.addSpacing(20)
        layout.addLayout(csv_layout)

        self.setLayout(layout)

        # Müzik çalma durumu değişkeni
        self.müzik_çalıyor = 0

    


    def butona_basildi(self):

        düğme = self.sender()

        if düğme:
            print(f"Buton {düğme.text()} basıldı.")

        if düğme.text() == "PLAY 1":
            print("Setup 1 nota")
            not_defteri_bulundu = False
            temizlenmis_liste1 = []

            for liste_ogesi in SM1:
                if "Not Defteri 1" in liste_ogesi and not_defteri_bulundu:
                    break
                elif "Not Defteri 1" in liste_ogesi and not_defteri_bulundu == False:
                    not_defteri_bulundu = True

            temizlenmis_liste1.append(liste_ogesi)
            print("tekrarlanmamış liste")
            print(temizlenmis_liste1)

            temizlenmişnota1 = []

            # Liste içindeki öğeleri kontrol ederek notaları ayırma
            ayrilmis_notlar1 = []
            for satir in temizlenmis_liste1:
                for kelime in satir.split():
                    for nota in RNOTA:
                        if nota in kelime:
                            temizlenmişnota1.append(nota)

            print(temizlenmişnota1)
            play_music(temizlenmişnota1)

        elif düğme.text() == "PLAY 2":
            print("Setup 2 nota")
            not_defteri_bulundu = False
            temizlenmis_liste2 = []

            for liste_ogesi in SM2:
                if "Not Defteri 2" in liste_ogesi and not_defteri_bulundu:
                    break
                elif "Not Defteri 2" in liste_ogesi and not_defteri_bulundu == False:
                    not_defteri_bulundu = True

            temizlenmis_liste2.append(liste_ogesi)
            print("tekrarlanmamış liste")
            print(temizlenmis_liste2)

            temizlenmişnota2 = []

            for satir in temizlenmis_liste2:
                for kelime in satir.split():
                    for nota in RNOTA:
                        if nota in kelime:
                            temizlenmişnota2.append(nota)

            play_music(temizlenmişnota2)

        elif düğme.text() == "PLAY 3":
            print("Setup 3 nota")
            not_defteri_bulundu = False
            temizlenmis_liste3 = []

            for liste_ogesi in SM3:
                if "Not Defteri 3" in liste_ogesi and not_defteri_bulundu:
                    break
                elif "Not Defteri 3" in liste_ogesi and not_defteri_bulundu == False:
                    not_defteri_bulundu = True

            temizlenmis_liste3.append(liste_ogesi)
            print("tekrarlanmamış liste")
            print(temizlenmis_liste3)

            temizlenmişnota3 = []

            for satir in temizlenmis_liste3:
                for kelime in satir.split():
                    for nota in RNOTA:
                        if nota in kelime:
                            temizlenmişnota3.append(nota)
            play_music(temizlenmişnota3)

        elif düğme.text() == "PLAY 4":
            print("Setup 4 nota")
            not_defteri_bulundu = False
            temizlenmis_liste4 = []

            for liste_ogesi in SM4:
                if "Not Defteri 4" in liste_ogesi and not_defteri_bulundu:
                    break
                elif "Not Defteri 4" in liste_ogesi and not_defteri_bulundu == False:
                    not_defteri_bulundu = True

            temizlenmis_liste4.append(liste_ogesi)
            print("tekrarlanmamış liste")
            print(temizlenmis_liste4)

            temizlenmişnota4 = []

            for satir in temizlenmis_liste4:
                for kelime in satir.split():
                    for nota in RNOTA:
                        if nota in kelime:
                            temizlenmişnota4.append(nota)
            play_music(temizlenmişnota4)    


    def csv_ekle(self, index):
        if index not in [1, 2, 3, 4]:  # Sadece SETUP1, SETUP2, SETUP3 ve SETUP4 için işlem yap
            return

        dosya_adı, _ = QFileDialog.getOpenFileName(self, "CSV Dosyası Seç", "", "CSV Dosyaları (*.csv)")
        if dosya_adı:
            veri = pd.read_csv(dosya_adı)
            veri = uygun_hale_getir(veri)  # Gelen veriyi uygun hale getir
            self.tabloya_veri_ekle(veri, index)

            # Notaları hesapla ve ikinci pencereye gönder
            if index == 1:
                notes_func = notalari_hesapla_1
            elif index == 2:
                notes_func = notalari_hesapla_2
            elif index == 3:
                notes_func = notalari_hesapla_3
            elif index == 4:
                notes_func = notalari_hesapla_4

            notes = notes_func(veri)
            ikinci_pencere.not_defterler[index - 1].append('\n'.join([f"{column}: {note}" for column, note in notes]))

            ikinci_pencere.notlari_guncelle()  # Notları güncelle

            print("Notlar ikinci pencereye gönderildi.")

    def tabloya_veri_ekle(self, veri, index):
     konum = self.sender().property("konum")
     if konum == "sol üst":
        table_index = 0
     elif konum == "sağ üst":
        table_index = 1
     elif konum == "sol alt":
        table_index = 2
     elif konum == "sağ alt":
        table_index = 3

     table_name = f"tablo_{table_index}"
     table = self.findChild(QTableWidget, table_name)
     if table is None:
        print(f"{table_name} tablosu bulunamadı.")
        return

     # Sütun sayısını 8'e eşitle
     if veri.shape[1] > 8:
        veri = veri.iloc[:, :8]
     elif veri.shape[1] < 8:
        eksik_sutun_sayisi = 8 - veri.shape[1]
        for _ in range(eksik_sutun_sayisi):
            veri[f"Ek_Sutun_{_}"] = None

     # Fazla satırları kaldır
     if veri.shape[0] > 10:
        veri = veri.head(10)

     #  Eksik satırları ekle
     while len(veri) < 10:
        veri = veri.append(pd.Series([None] * 8, index=veri.columns), ignore_index=True)

     # Sütun başlıklarını al
     column_headers = veri.columns.tolist()

     # Tablonun sütun başlıklarını ayarla
     for j, baslik in enumerate(column_headers):
        table.setHorizontalHeaderItem(j, QTableWidgetItem(baslik))

     # Veriyi tabloya ekle
     row_count, col_count = veri.shape
     table.setRowCount(row_count)  # Tablo satır sayısını güncelle
     table.setColumnCount(8)  # Her zaman 8 sütun olduğunu garanti et

     for i in range(row_count):
        for j in range(col_count):
            item = veri.iloc[i, j]
            if pd.notna(item):  # Eğer hücrede veri varsa
                table.setItem(i, j, QTableWidgetItem(str(item)))
            else:  # Eğer hücre boşsa
                table.setItem(i, j, QTableWidgetItem(""))  # Boş hücre ekleyin

     # Eksik hücreleri kontrol edin ve uygun şekilde doldurun
     for i in range(row_count):
        for j in range(col_count, 8):
            table.setItem(i, j, None)  # Eksik hücreleri None olarak işaretleyin

     # Belirli sütunlardaki notaları hesapla ve ikinci pencereye gönder
     if index == 1:
        notes_func = notalari_hesapla_1
     elif index == 2:
        notes_func = notalari_hesapla_2
     elif index == 3:
        notes_func = notalari_hesapla_3
     elif index == 4:
        notes_func = notalari_hesapla_4

     notes = notes_func(veri)
     ikinci_pencere.not_defterler[index - 1].append('\n'.join([f"{column}: {note}" for column, note in notes]))

     ikinci_pencere.notlari_guncelle()  # Notları güncelle

     print("Notlar ikinci pencereye gönderildi.")


def uygun_hale_getir(veri):
    # Satır ve sütun sayısını kontrol et
    satir_sayisi, sutun_sayisi = veri.shape

    # Sütun sayısını 8'e eşitle
    if sutun_sayisi > 8:
        veri = veri.iloc[:, :8]
    elif sutun_sayisi < 8:
        eksik_sutun_sayisi = 8 - sutun_sayisi
        for _ in range(eksik_sutun_sayisi):
            veri[f"Ek_Sutun_{_}"] = None

    # Fazla satırları kaldır
    if satir_sayisi > 10:
        veri = veri.head(10)

    # Eksik satırları ekle
    while len(veri) < 10:
        veri = veri.append(pd.Series([None] * 8, index=veri.columns), ignore_index=True)

    return veri

class IkinciPencere(QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("İkinci Pencere")
        self.setGeometry(100, 100, 800, 600)  # Boyutları büyütüldü
        self.setStyleSheet("background-color: #333; color: white;")

        layout = QVBoxLayout()  # Ana layout oluşturuldu

        self.not_defterler = [[] for _ in range(4)]  # Her CSV dosyası için ayrı bir not defteri tutulacak

        self.not_defteri_widgetleri = []

        for i in range(4):
            not_defteri_etiketi = QLabel(f"Notebook {i+1}:")
            not_defteri_etiketi.setStyleSheet("font-weight: bold;")
            layout.addWidget(not_defteri_etiketi, alignment=Qt.AlignLeft)  # Sol üst köşeye yerleştirildi

            not_defteri = QTextEdit()
            not_defteri.setPlaceholderText("Notunuzu buraya yazabilirsiniz.")
            not_defteri.setStyleSheet("background-color: #444; color: white; border: 2px solid black;")
            layout.addWidget(not_defteri)
            self.not_defteri_widgetleri.append(not_defteri)

        self.setLayout(layout)

    def notlari_guncelle(self):
        for i, not_defteri in enumerate(self.not_defteri_widgetleri):
            not_defteri.setText("\n".join(self.not_defterler[i]))
            SM1.extend([f"Not Defteri 1: {note}" for note in self.not_defterler[0]])
            SM2.extend([f"Not Defteri 2: {note}" for note in self.not_defterler[1]])
            SM3.extend([f"Not Defteri 3: {note}" for note in self.not_defterler[2]])
            SM4.extend([f"Not Defteri 4: {note}" for note in self.not_defterler[3]])
            print("Setup 1 nota")
            print(SM1)
            print("Setup 2 nota")
            print(SM2)
            print("Setup 3 nota")
            print(SM3)
            print("Setup 4 nota")
            print(SM4)
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ana_pencere = AnaPencere()
    ikinci_pencere = IkinciPencere()
    ana_pencere.show()
    ikinci_pencere.show()
    sys.exit(app.exec_())
