############################## KAMERAYI KAYDET ##############################
"""

def kamerayi_Kaydet(kamera_Adi,kamera_IP,kamera_Protokol,kullanici_Adi,kullanici_Sifre,kamera_Uzanti,aciklama):
    import pyodbc as odbccon
    conn = odbccon.connect(
    'Driver={SQL Server};'
    'Server=ALPHA\SQLEXPRESS;'
    'Database=kullaniciGiris;'
    'Trusted_Connection=yes;')
    
    print("Bağlantı Gerçekleşti")
    cursor = conn.cursor()
    print("Cursor Oluşturuldu")
    imlec = conn.cursor()
    print("İmlec Oluşturuldu")
    conn.commit()
    
    
    def tabloolustur(kamera_Adi,kamera_IP,kamera_Protokol,kullanici_Adi,kullanici_Sifre,kamera_Uzanti,aciklama):
        conn = odbccon.connect(
            'Driver={SQL Server};'
            'Server=ALPHA\SQLEXPRESS;'
            'Database=kullaniciGiris;'
            'Trusted_Connection=yes;')
        imlec = conn.cursor()
        komut='INSERT INTO KameraBilgileri VALUES (?,?,?,?,?,?,?)'
        veriler=(kamera_Adi,kamera_IP,kamera_Protokol,kullanici_Adi,kullanici_Sifre,kamera_Uzanti,aciklama)
        imlec.execute(komut,veriler)
        conn.commit()
    tabloolustur(kamera_Adi,kamera_IP,kamera_Protokol,kullanici_Adi,kullanici_Sifre,kamera_Uzanti,aciklama)
    print("Kamera kaydı başarıyla gerçekleşti")

"""

def kamerayi_Kaydet(kamera_Adi,kamera_IP,kamera_Protokol,kullanici_Adi,kullanici_Sifre,kamera_Uzanti,aciklama):
    #rtsp://admin:123456@192.168.1.216/H264?ch=1&subtype=0
    import pickle
    print("Kamera kaydediliyor, lütfen bekleyiniz...")
    
    name_List=[]
    adress_List=[]
    
    file=open('cameras.pkl','rb') #Önceki kayıtları al
    datas=pickle.load(file)
    file.close()
    
    for data in datas: #Önceki kayırları listeye al
        name_List.append(data)
        adress_List.append(datas[data])
    
    
    
    name=kamera_Adi
    adress=kamera_Protokol+kullanici_Adi+":"+kullanici_Sifre+"@"+kamera_IP+"/"+kamera_Uzanti
    name_List.append(name)
    adress_List.append(adress)
        
    
    data={}
    for i in range (0,len(name_List)): #Son listeyi kaydet
        data[name_List[i]]=adress_List[i]
    file =open('cameras.pkl','wb')
    
    pickle.dump(data,file)
    file.close()
    print("Kamera kaydedildi, işleminize devam edebilirsiniz.")
    
    """
############################## KAMERAYI DÜZENLE ##############################


def kamerayi_Duzenle(kamera_ID,kamera_Adi,kamera_IP,kamera_Protokol,kullanici_Adi,kullanici_Sifre,kamera_Uzanti,aciklama):
    import pyodbc as odbccon
    conn = odbccon.connect(
            'Driver={SQL Server};'
            'Server=ALPHA\SQLEXPRESS;'
            'Database=kullaniciGiris;'
            'Trusted_Connection=yes;')
    imlec = conn.cursor()
    sonuc = imlec.execute('UPDATE KameraBilgileri SET Kamera_Adi = ?,Kamera_IP=?,Kamera_Protokol=?,Kullanici_Adi=?,Sifre=?,Uzanti=?,Aciklama=? WHERE id = ?',(kamera_Adi,kamera_IP,kamera_Protokol,kullanici_Adi,kullanici_Sifre,kamera_Uzanti,aciklama,kamera_ID))
    conn.commit()
    
    print(kamera_Adi + " kamerası güncellendi.")
    
    

############################## KAMERAYI SİL ##############################


def kamerayi_Sil(kamera_ID,kamera_Adi):
    import pyodbc as odbccon
    conn = odbccon.connect(
            'Driver={SQL Server};'
            'Server=ALPHA\SQLEXPRESS;'
            'Database=kullaniciGiris;'
            'Trusted_Connection=yes;')
    imlec = conn.cursor()
    sonuc = imlec.execute('DELETE FROM KameraBilgileri WHERE id = ?',(kamera_ID))
    conn.commit()
    
    print(kamera_Adi + " kamerası silindi.")
    
    
"""










