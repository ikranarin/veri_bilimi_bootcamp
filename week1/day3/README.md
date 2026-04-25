# Smart Survey Analyzer

## Projenin Amacı
Smart Survey Analyzer projesinin temel amacı, bir üniversite ortamındaki öğrenci memnuniyetini ölçen anket verilerini otomatize edilmiş bir sistemle analiz etmektir. Manuel veri girişinin yarattığı hataları minimize etmek, belirsiz sayıda gelen geri bildirimleri dinamik olarak işlemek ve veri seti içindeki kritik memnuniyetsizlik gibi uç durumları anlık olarak tespit eden bir erken uyarı mekanizması kurmaktır.

## Döngü Stratejileri: For ve While Kullanımı
Yazılım mimarisinde doğru döngü tipini seçmek performans ve okunabilirlik açısından kritiktir:

* **While Döngüsü**: Adım sayısının önceden kestirilemediği durumlarda kullanılır. Projemizde veri toplama aşamasında while tercih edilmiştir; çünkü kullanıcının ne zaman 0 basıp çıkacağını veya sistemin ne zaman geçersiz veri üreteceğini bilemeyiz. "Hedeflenen veri miktarına ulaşana kadar devam et" mantığı için en uygun araçtır.
* **For Döngüsü**: Veri seti (liste) belli olduktan sonra, bu verilerin üzerinden teker teker geçmek için kullanılır. Analiz aşamasında (ortalama hesaplama, sayaç tutma) for kullanılmıştır. Çünkü listenin başı ve sonu bellidir; her elemana dokunup işlem yapmak temel amaçtır.

## Hata Yönetimi ve Veri Temizleme (Data Cleaning)
Projede kullanılan continue ifadesi, veri bilimindeki Data Cleaning sürecini temsil eder. Gerçek dünyadaki veri setleri her zaman mükemmel değildir; hatalı girişler veya boş değerler içerir. Bu projede geçersiz puanların yok sayılması, kirli verinin analiz sonuçlarını (ortalama, min/max) saptırmasını önlemek adına proaktif bir yaklaşımdır.

## Akış Kontrolü: Break ve Continue
Kodun içindeki bu komutlar, gerçek hayattaki karar anlarının dijital karşılığıdır:

* **Break (Acil Çıkış / İptal)**: Gerçek hayatta bir yangın alarmı çaldığında binayı terk etmeye benzer. Projede, kullanıcı 0 girdiğinde anketi hemen bitir veya arka arkaya düşük puan geldiğinde analizi durdur ve uyar komutu, sistemin güvenliğini ve vaktini koruyan bir acil çıkış kapısıdır.
* **Continue (Pas Geçme / Filtreleme)**: Kalite kontrol bandındaki bozuk bir ürünü kenara ayırıp bandı durdurmadan sıradaki ürüne bakmaya benzer. Projede hatalı veri geldiğinde yapılan işlem budur; veri sisteme kaydedilmez, sadece o adım atlanır ve süreç kesintisiz devam eder.

## Random Veri Üretmenin Test Sürecindeki Rolü
Gerçek bir anket yapılmadan önce yazılımı test etmek için Random kütüphanesi hayati önem taşır:
* **Simülasyon**: Sistemin farklı senaryolara (örneğin hep düşük puan gelmesi veya aniden 0 girilmesi) nasıl tepki vereceğini görmemizi sağlar.
* **Objektiflik**: Rastgele veri, beklenmedik kombinasyonlar yaratarak sistemin dayanıklılığını (robustness) ölçer.

## Döngülerin Veri Analizindeki Önemi
Veri analizi özünde büyük veri kütlelerini anlamlı bilgilere dönüştürme işlemidir. Döngüler bu sürecin motorudur:
1. **Hız**: Binlerce anket sonucunu saniyeler içinde kategorize edebilirler.
2. **Ölçeklenebilirlik**: Kod, bugün 20 anket sonucunu analiz ettiği gibi, hiçbir değişiklik yapılmadan yarın 20.000 anket sonucunu da analiz edebilir.
3. **Hata Payı**: Manuel hesaplamalarda insan yorgunluğundan kaynaklanan hatalar döngülerde söz konusu değildir; mantık bir kez doğru kurulduğunda her zaman doğru sonucu üretir.

## Algoritmik Verimlilik (Scalability)
Geliştirilen sistem, ölçeklenebilir bir yapıdadır. Şu an üzerinde çalışılan örneklem büyüklüğü ne olursa olsun, while ve for döngülerinin esnekliği sayesinde sistem donanım kaynakları dahilinde milyonlarca veri satırını aynı tutarlılıkla işleyebilir. Bu da yazılımın sürdürülebilirliğini kanıtlar.

## Sonuç
Smart Survey Analyzer projesi, Python'un kontrol yapılarını kullanarak ham veriden nasıl anlamlı içgörüler (ortalama puan, memnuniyet oranları vb.) çıkarılabileceğini göstermiştir. Özellikle break ve continue gibi yapıların kullanımı, sadece veri işlemeyi değil, aynı zamanda veriyi işlerken sistemi korumayı da sağlamaktadır.

Hazırlayan: İkra Narin Soran
