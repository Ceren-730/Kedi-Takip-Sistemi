🐱 YOLOv8 ile Kedi Tespiti (Cat Detection)

Bu proje, Ultralytics YOLOv8 modeli kullanılarak tek bir görüntü üzerinde kedi (cat) nesnesinin tespit edilmesini amaçlamaktadır. Önceden eğitilmiş YOLOv8n ağırlıkları kullanılmıştır. Tespit edilen nesneler görüntü üzerine bounding box ile çizdirilir, sonuç hem ekranda gösterilir hem de dosya olarak kaydedilir. Projede track() fonksiyonu kullanılarak nesne kimliği (ID) korunmuştur.

Kullanılan Teknolojiler

Python 3.x, Ultralytics YOLOv8, OpenCV (cv2)

Dataset Yapısı (YOLO Formatı)
C:/Cat-1
├── train/images
├── test/images
└── data.yaml

path: C:/Cat-1

train: train/images

val: test/images

test: test/images


nc: 1
names: ['cat']


Bu dataset tek sınıflıdır ve yalnızca cat etiketini içermektedir.

Kurulum
pip install ultralytics opencv-python

Kullanım

Kod, belirtilen görsel üzerinde yalnızca kedi nesnesini tespit edecek şekilde çalışır. COCO sınıf indeksine göre 15 = cat olacak şekilde filtreleme yapılmıştır.

results = model.track(
   
    source=r"C:\Users\Ceren\Downloads\kedi.webp",
   
    classes=[15],
   
    conf=0.5,
   
    persist=True
)


track() : Nesne takibi (ID korunur)

conf=0.5 : Minimum güven skoru

classes=[15] : Sadece kedi sınıfı

Çıktı

Tespit edilen kedi görüntü üzerinde bounding box ile işaretlenir. Sonuç görseli otomatik olarak aşağıdaki adla kaydedilir:

 kedi_tespit_edildi.jpg

Amaç

Bu proje, YOLOv8 mimarisinin temel kullanımını göstermek, tek sınıflı nesne tespit sürecini örneklemek ve staj / portföy projelerinde kullanılabilecek sade ve anlaşılır bir bilgisayarla görü (computer vision) demosu sunmak amacıyla hazırlanmıştır.

Geliştirici

Ceren Akgün
Bilgisayar Mühendisliği Öğrencisi
