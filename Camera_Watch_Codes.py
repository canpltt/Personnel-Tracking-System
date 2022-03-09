import face_recognition
import cv2
import pickle
import logging
import os
import mediapipe as mp
import datetime
import zipfile as z
import winsound

simple_format = '%(asctime)s - %(name)s - %(message)s'       #Log kayıt biçimi
name_List=[]
encoding_List=[]
camera_List=[]
camera_Name_List=[]
camera_Adress_List=[]




file=open('encoding_data.pkl','rb')         #Yüz kayıtlarını al
datas=pickle.load(file)
file.close()
file=open('cameras.pkl','rb')       #Kamera kayıtlarını al
cameras=pickle.load(file)
file.close()

mpFaceDetection=mp.solutions.face_detection
mpDraw=mp.solutions.drawing_utils
faceDetection=mpFaceDetection.FaceDetection(0.75)


i=0
for camera in cameras:       #Kamera kayıtlarını listeye kaydet
    camera_Name_List.append(camera)
    camera_Adress_List.append(cameras[camera])
    i+=1



for data in datas:       #Yüz kayıtlarını listeye kaydet
    name_List.append(data)
    encoding_List.append(datas[data])

logging.basicConfig(          #Log kayıtlarının biçimleri
    filename='Logfile.log',
    filemode='a',
    format=simple_format,
    level=logging.INFO,
    datefmt='%d.%m.%y - %H.%M'
)
logger = logging.getLogger('Giriş')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(simple_format)
ch.setFormatter(formatter)
logger.addHandler(ch)
    
    

named="Tanimlaniyor"



def mail_gonder(dosya_adi):
    import smtplib
    from email.message import EmailMessage
    
    mesaj=EmailMessage()
    
    dosya_adi="Zipler/"+dosya_adi
    mesaj["Subject"]="Deneme"
    mesaj["From"]="icanpltt1@gmail.com"
    mesaj["To"]="icanpltt1@gmail.com"
    
    mesaj.set_content("Deneme")
    
    with open(dosya_adi,"rb") as f:
        file_data = f.read()
        file_name=f.name
    
    
    mesaj.add_attachment(file_data,maintype="application", subtype="octet-stream",filename=file_name)
    
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login("icanpltt1@gmail.com","takatuka21")
        smtp.send_message(mesaj)



def kontrol(pathTest):
    color = (0,255,0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    image = cv2.imread(pathTest)


    testImage = face_recognition.load_image_file(pathTest)
    faceLocations = face_recognition.face_locations(testImage)
    faceEncodings = face_recognition.face_encodings(testImage, faceLocations)
    
    for faceLoc, faceEncoding in zip(faceLocations,faceEncodings):
        topLeftY,bottomRightX,bottomRightY,topLeftX = faceLoc
        matchedFaces = face_recognition.compare_faces(encoding_List, faceEncoding)
        name = "unknown"
        
        if True in matchedFaces:
            matchedIndex = matchedFaces.index(True)
            name = name_List[matchedIndex]
            global named
            named=name
            logger.info(name)
            f=500
            d=750
            winsound.Beep(f, d)
            
        cv2.rectangle(image, (topLeftX,topLeftY), (bottomRightX,bottomRightY), color, 1)
        cv2.putText(image, name, (topLeftX,topLeftY), font, 1, color, 1)




def  take_screenshot(frame,gun,ay,yil,saat,dakika,saniye):
    path, dirs, files = next(os.walk("Images"))
    image_name="{}.{}.{}-{}.{}.{}".format(str(saat),str(dakika),str(saniye),str(gun),str(ay),str(yil))
    
    filepath=os.path.join("Images/{}.png".format(image_name))
    cv2.imwrite(filepath, frame)
    kontrol(filepath)




def gunluk_Kayit(gun,ay,yil):
    kayit_kontrol=True
    dosyalar=os.listdir('Zipler')
    dosya_adi='{}-{}-{}.zip'.format(str(gun),str(ay),str(yil))
    for i in dosyalar:
        if(i==dosya_adi):
            kayit_kontrol=False
            
    if(kayit_kontrol==True):
        zip=z.ZipFile('Zipler/{}-{}-{}.zip'.format(str(gun),str(ay),str(yil)),'w')
        path, dirs, files = next(os.walk("Images"))
        i=1
        resimler=os.listdir('Images')
        for a in resimler:
            zip.write("Images/{}".format(a))
            os.remove("Images/{}".format(a))
        mail_gonder(dosya_adi)
        



def kamerayi_Ac(number):
    try:
        selected_Camera=number        #Oynatılacak kamera kaydını seç
        print ("Aktif Kamera: ",selected_Camera)
        process_this_frame = True
        timer_screenshot=30
        timer_name=13
        cap=cv2.VideoCapture(0)
        #pTime=0 
        while True:         #Kamerada yüz arama
            if(timer_name==0):
                global named
                named="Tanimlaniyor"
                timer_name=13
            else: timer_name-=1
            now = datetime.datetime.now()
            gun=now.day
            ay=now.month
            yil=now.year
            saat=now.hour
            dakika=now.minute
            saniye=now.second
            today8pm = now.replace(hour=20, minute=0)
            if(now > today8pm):
                gunluk_Kayit(gun,ay,yil)
            success, img=cap.read()
            success, img1=cap.read()
            imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = faceDetection.process(imgRGB)
            bboxs=[]
            process_this_frame = True
            if results.detections:
                timer_screenshot-=1
                for id,detection in enumerate(results.detections):
                    bboxC=detection.location_data.relative_bounding_box
        
                    ih, iw, ic=img.shape
                    bbox=int(bboxC.xmin * iw), int(bboxC.ymin * ih),\
                    int(bboxC.width * iw), int(bboxC.height * ih)
                    bboxs.append([id, bbox, detection.score])
                
                if(named=="Tanimlaniyor"):
                    cv2.rectangle(img,bbox,(0,255,255),2)
                    cv2.putText(img, f'{named}', (bboxs[0][1][0] + 50, bboxs[0][1][1] - 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 255), 2)
                else:
                    cv2.rectangle(img,bbox,(0,255,0),2)
                    cv2.putText(img, f'{named}', (bboxs[0][1][0] + 50, bboxs[0][1][1] - 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
                if(timer_screenshot==0):
                    take_screenshot(img1,gun,ay,yil,saat,dakika,saniye)
                    timer_screenshot=20
                
        
            process_this_frame = not process_this_frame
        
            cv2.imshow("Guvenlik Kamerasi",img)
            if cv2.waitKey(1) & 0xFF == ord('q'): #q harfine basılırsa kamerayı sonlandır
                break
        img.release()
        img1.release()
        cv2.destroyAllWindows()
            
            
    except AttributeError:
        print("Kamera Kapatıldı.")
    except UnboundLocalError:
        print("Kamera Kapatıldı.")
        
    
    


kamerayi_Ac(1)

