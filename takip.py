import cv2
from ultralytics import YOLO

def gorsel_tespit():
    try:
        # 1. Modeli yüklüyoruz
        print("Model yukleniyor...")
        model = YOLO('yolov8n.pt')

        # 2. kedi.webp dosyasini analiz ediyoruz
        # classes=[15] ile sadece kediyi filtreliyoruz
        print("Gorsel analiz ediliyor: kedi.webp")
        # predict yerine track kullanıyoruz
        results = model.track(source=r"C:\Users\Ceren\Downloads\kedi.webp", classes=[15], conf=0.5, persist=True)
       # results = model.predict(source=r"C:\Users\Ceren\Downloads\kedi.webp", classes=[15], conf=0.5)

        # 3. Sonuclari gorsellestiriyoruz
        # results[0].plot() tespit kutularini resmin uzerine cizer
        resim_sonuc = results[0].plot()

        # 4. Ekranda gosteriyoruz
        cv2.imshow("Kedi Tespit Sonucu", resim_sonuc)
        
        # 5. Tespitli hali bilgisayara 'kedi_tespit_edildi.jpg' olarak kaydediyoruz
        cv2.imwrite('kedi_tespit_edildi.jpg', resim_sonuc)
        print("Tespit edilen gorsel 'kedi_tespit_edildi.jpg' olarak kaydedildi.")

        print("\nKapatmak icin herhangi bir tusa basin...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"Hata: {e}")
        print("Lutfen 'kedi.webp' dosyasinin kodla ayni klasorde oldugundan emin olun.")

if __name__ == "__main__":
    gorsel_tespit()