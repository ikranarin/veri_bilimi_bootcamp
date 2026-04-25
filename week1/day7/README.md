# Smart Expense & Notification Management System

## Özet
Bu proje, kullanıcının finansal harcamalarını nesne tabanlı olarak modelleyen, bütçe limitlerini anlık kontrol eden ve limit aşımlarında farklı bildirim kanalları üzerinden uyarı üreten modüler bir finans yönetim sistemidir. Sistem; Expense ve Budget sınıfları üzerinden veri tutarlılığını sağlarken, Notification hiyerarşisi ile yazılım mimarisinde esnekliği temel alan profesyonel bir altyapı sunar.

## OOP ve Modülerliğin Önemi
Projenin modüler yapıda (ayrı dosyalar halinde) geliştirilmesi, "Kaygıları Ayrıştırma" (Separation of Concerns) ilkesinin bir sonucudur.
* Harcama verisini tutan modeller, bildirim mantığı ve kullanıcı arayüzü birbirinden izole edilmiştir.
* Bu sayede, örneğin bildirim sistemine yeni bir kanal eklendiğinde, finansal analiz kodlarına dokunulmasına gerek kalmaz. 
* Bu yaklaşım, sistemin sürdürülebilirliği için kritik bir tasarım kararıdır.

## Polymorphism (Çok Biçimlilik)
Polymorphism, aynı arayüze (send() metodu) sahip farklı sınıfların, birbirinden tamamen farklı işlemler yapabilmesidir.
* Sistemde EmailNotification ve SMSNotification sınıfları aynı send() metoduna sahiptir.
* Program döngü içinde notification.send() komutunu verdiğinde, Python hangi bildirim türü gelirse gelsin, o nesnenin kendi türüne özgü olan gönderim davranışını otomatik olarak çalıştırır.
* Bu özellik, sisteme yeni bir bildirim türü eklemek istediğimizde mevcut kod yapımızı değiştirmemize gerek kalmadığı anlamına gelir.

## Hata Yönetimi: "Sistem Neden Çökmemeli?"
Kullanıcıdan veri alınan fonksiyonlarda kullanılan try/except yapısı, sistemin dayanıklılığını sağlar:
* Kullanıcı yanlışlıkla bir sayı yerine harf girdiğinde veya geçersiz formatta veri girişi yaptığında, program aniden durmak yerine kullanıcıya açıklayıcı bir uyarı verir ve döngüyü güvenli bir şekilde devam ettirir.
* Profesyonel sistemlerde bir uygulamanın hata anında kapanması bir yazılım arızası olarak kabul edilir; hata yönetimi ise bu arızaları kontrollü bir sürece dönüştürür.

## Sonuç
Smart Expense & Notification Management System; Modülerlik, OOP ve Hata Yönetimi prensiplerinin birleştiği bir prototiptir. Sistem, basitten başlayıp profesyonel seviyeye evrilmiş; kodun sadece işlevsel değil, aynı zamanda okunabilir, test edilebilir ve gelecekteki geliştirmelere açık (Scalable) olması hedeflenmiştir.

Hazırlayan: İkra Narin Soran
