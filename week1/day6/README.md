# Smart Notification System

## Polymorphism ve Inheritance: Temel Farklar
Sıklıkla karıştırılan bu iki kavram, nesne yönelimli programlamanın farklı ihtiyaçlarını karşılar:
* **Inheritance (Kalıtım)**: Bir yapı aktarımıdır. Alt sınıfın, üst sınıftaki öznitelikleri ve metotları aynen alıp kullanmasıdır. Kodun hiyerarşik organizasyonunu sağlar (Örn: "Bir SMSNotification, bir Notification'dır").
* **Polymorphism (Çok Biçimlilik)**: Bir davranış çeşitliliğidir. Inheritance ile kazanılan bir metodun (örneğin send()), farklı sınıflarda bambaşka sonuçlar üretmesidir. Inheritance yapıyı kurarken, polymorphism o yapının esnekliğini sağlar.

## Özel Metotlar (__str__ vb.) Neden Kullanılır?
Python'daki çift alt çizgili (dunder) metotlar, nesnelerimizin Python'un çekirdek mekanizmalarıyla etkileşime girmesini sağlar.
* **__str__ Metodu**: Bir nesneyi print() ile ekrana bastığımızda Python varsayılan olarak nesnenin hafıza adresini gösterir. __str__ metodunu özelleştirerek, nesnenin içeriğini kullanıcı dostu bir metin formatına dönüştürebiliriz. Bu, hata ayıklama (debugging) sürecini kolaylaştırır ve sistemin şeffaf olmasını sağlar.
* **Sihirli Bağlantı**: Bu metotlar, kodun daha akıcı ve Python'a özgü (Pythonic) olmasını sağlar; nesne üzerinde yerleşik bir tipmiş gibi işlem yapabilmemize olanak tanır.

## Modüler Kodun Avantajları: "Parçala ve Yönet"
Projeyi tek bir dosyaya yığmak yerine modüllere (notifications.py ve utils.py) bölmek, yazılımın ölçeklenebilirliğini artırır:
* **İzolasyon**: Bir modüldeki mantığı değiştirdiğinizde, diğer sınıfların bozulma riski olmaz.
* **Ekip Çalışması**: Büyük projelerde farklı geliştiriciler çakışma yaşamadan ayrı modüller üzerinde çalışabilir.
* **Yeniden Kullanılabilirlik**: Hazırlanan modüller, ileride başka projelerde kopyalanarak kolayca kullanılabilir.

## Hata Yönetimi: Neden Kritik?
Hata yönetimi (try/except) olmayan bir sistem "kırılgan" bir sistemdir:
* **Kullanıcı Kaybı**: Bir sistem çöktüğünde (crash), kullanıcı bunu hatalı yazılım olarak algılar ve uygulamayı terk eder. Hata yönetimi, sistemin zarif bir şekilde hata mesajı vermesini ve çalışmaya devam etmesini sağlar.
* **Veri Güvensizliği**: Hata anında sistem aniden durursa, üzerinde çalışılan veriler kaydedilmeden kaybolabilir. Hata yönetimi, sistemin durumu güvenli bir şekilde kapatmasını sağlar.
* **Profesyonellik**: Hata yönetimi, sistemin tahmin edilemezliği karşısında geliştiricinin kontrolü elinde tuttuğunun somut kanıtıdır.

## Özet
Bu proje, farklı bildirim kanallarının tek bir arayüzle yönetilmesi sürecinde polymorphism kullanılarak esnek ve genişletilebilir bir yapı kurulmuştur. Proje, kodun modüler hale getirilmesiyle bakım kolaylığını ve hata yönetimi ile sistemin sürekliliğini hedeflemiştir. Yazılım mühendisliğinde kodun sadece çalışmasının yetmediğini; aynı zamanda öngörülebilir, sağlam ve gelecekteki değişikliklere uyum sağlayabilir olması gerektiğini ortaya koymaktadır.

Hazırlayan: İkra Narin Soran
