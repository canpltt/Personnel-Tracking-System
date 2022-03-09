from PyQt5.QtWidgets import *
from Main_Compile import AnaSafanın #Anasayfayı çalıştırır
import sys

print ("Uygulama başlatılıyor lütfen bekleyiniz...")

app = QApplication([])
ex = AnaSafanın()
ex.show()
sys.exit(app.exec_())


