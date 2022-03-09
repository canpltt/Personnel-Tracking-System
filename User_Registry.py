############################## KULLANICININ YÜZÜNÜ ALGILAMA ##############################

def yuz_Algilama(name,path,process):
    import face_recognition
    import pickle
    
    name_List=[]
    encoding_List=[]
    """
    file=open('encoding_data.pkl','rb') #Önceki kayıtları al
    datas=pickle.load(file)
    file.close()
    
    
    for data in datas: #Önceki kayırları listeye al
        name_List.append(data)
        encoding_List.append(datas[data])"""
    
    if(process=="Kayıt"):
        image=face_recognition.load_image_file(path)
        face_encoding = face_recognition.face_encodings(image)[0]
        
        name_List.append(name)
        encoding_List.append(face_encoding)
            
        
        data={}
        for i in range (0,len(name_List)): #Son listeyi kaydet
            data[name_List[i]]=encoding_List[i]
        file =open('encoding_data.pkl','wb')
        
        pickle.dump(data,file)
        file.close()
    elif(process=="Sil"):
        i=0
        while(i<len(name_List)):
            if(name_List[i]==name):
                break
            i+=1
            
        name_List.pop(i)
        encoding_List.pop(i)
        data={}
        for i in range (0,len(name_List)): #Son listeyi kaydet
            data[name_List[i]]=encoding_List[i]
        file =open('encoding_data.pkl','wb')
        
        pickle.dump(data,file)
        file.close()
        """
    elif(process=="Güncelle"):
        i=0
        while(i<len(name_List)):
            if(name_List[i]==name):
                break
            i+=1
            
        name_List.pop(i)
        encoding_List.pop(i)
        data={}
        for i in range (0,len(name_List)): #Son listeyi kaydet
            data[name_List[i]]=encoding_List[i]
        file =open('encoding_data.pkl','wb')
        
        pickle.dump(data,file)
        file.close()
    """
    
############################## KULLANICI KAYDETME ##############################
    
    
    
def kullanici_Kaydet(ad,soyad,telno,fotograf,cinsiyet,tc,adres):
    """
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
    def tabloolustur(ad,soyad,telno,fotograf,cinsiyet,tc,adres):
        
        conn = odbccon.connect(
        'Driver={SQL Server};'
        'Server=ALPHA\SQLEXPRESS;'
        'Database=kullaniciGiris;'
        'Trusted_Connection=yes;')
        imlec = conn.cursor()
        komut='INSERT INTO KullaniciVerileri VALUES (?,?,?,?,?,?,?)'
        veriler=(ad,soyad,telno,fotograf,cinsiyet,tc,adres)
        imlec.execute(komut,veriler)
        conn.commit()
        print(ad+" ",soyad," çalışanı sisteme eklendi.")
    tabloolustur(ad,soyad,telno,fotograf,cinsiyet,tc,adres)
    """
    print("Kullanıcının fotoğrafı taranıyor...")
    name=ad+" "+soyad
    process="Kayıt"
    yuz_Algilama(name, fotograf,process)
    print("Kullanıcının yüzü tanındı ve sisteme eklendi...")
    
    
"""

############################## KULLANICI DÜZENLE ##############################
    
    

def kullanici_Guncelle(kullanici_ID,Kullanici_Adi,Kullanici_Soyadi,Kullanici_Telefon_No,Kullanici_Fotografi,Kullanici_Cinsiyeti,Kullanici_TC_No,Kullanici_Adres):
    import pyodbc as odbccon
    conn = odbccon.connect(
            'Driver={SQL Server};'
            'Server=ALPHA\SQLEXPRESS;'
            'Database=kullaniciGiris;'
            'Trusted_Connection=yes;')
    imlec = conn.cursor()
    sonuc = imlec.execute('UPDATE KullaniciVerileri SET Kullanici_Adi = ?,Kullanici_Soyadi=?,Kullanici_Telefon_No=?,Kullanici_Fotografi=?,Kullanici_Cinsiyeti=?,Kullanici_TC_No=?,Kullanici_Adres=? WHERE id = ?',(Kullanici_Adi,Kullanici_Soyadi,Kullanici_Telefon_No,Kullanici_Fotografi,Kullanici_Cinsiyeti,Kullanici_TC_No,Kullanici_Adres,kullanici_ID))
    conn.commit()
    name=Kullanici_Adi+" "+Kullanici_Soyadi
    process="Güncelle"
    yuz_Algilama(name, Kullanici_Fotografi,process)
    print(Kullanici_Adi + " adlı çalışan güncellendi.")
    
    
    
    
############################## KULLANICI SİLME ##############################
    
    
    
    
    
def kullanici_Sil(kullanici_ID,Kullanici_Adi,Kullanici_Soyadi, Kullanici_Fotografi):
    import pyodbc as odbccon
    conn = odbccon.connect(
            'Driver={SQL Server};'
            'Server=ALPHA\SQLEXPRESS;'
            'Database=kullaniciGiris;'
            'Trusted_Connection=yes;')
    imlec = conn.cursor()
    sonuc = imlec.execute('DELETE FROM KullaniciVerileri WHERE id = ?',(kullanici_ID))
    conn.commit()
    name=Kullanici_Adi+" "+Kullanici_Soyadi
    process="Sil"
    yuz_Algilama(name, Kullanici_Fotografi,process)
    print(Kullanici_Adi + " adlı çalışan silindi")

    

"""


#kullanici_Kaydet("Can", "Polat", "65165465", "faces/can.jpg", "Erkek", "6516545", "Elazığ")


















