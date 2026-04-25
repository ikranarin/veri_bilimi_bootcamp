# Smart Budget Assistant

## Fonksiyon Kullanmanın Avantajları
* **Bakım Kolaylığı**: Bir hesaplama mantığını değiştirmek istediğimizde, bunu kodun her yerinde değil, sadece ilgili fonksiyonun içinde tek bir noktada güncelleriz.
* **Okunabilirlik**: Karmaşık bir bütçe yönetimi algoritmasını küçük, anlamlı parçalara (örneğin get_expenses, calculate_summary) böldüğümüzde, kod "ne yapıldığını" değil "neden yapıldığını" anlatan bir hikâyeye dönüşür.
* **Tekrar Kullanılabilirlik (DRY - Don't Repeat Yourself)**: Aynı harcama hesaplama mantığını farklı modüllerde tekrar yazmak yerine, fonksiyon ismini çağırarak kodu tekrar kullanırız.

## *args Neden Gereklidir?
* Gerçek hayatta bir sistem her zaman kaç adet veri alacağını bilmez. *args kullanımı, esneklik sağlar.
* Fonksiyona önceden tanımlanmamış sayıda argüman gönderebilmek, sistemin dinamik ihtiyaçlara uyum sağlamasına olanak tanır. 
* Örneğin, bu projede harcama listesi 3 elemanlı da olsa 300 elemanlı da olsa, *args yapısı aynı esneklikle veriyi kabul edebilir. Bu, yazılımın genişletilebilir (scalable) olmasının anahtarıdır.

## Scope (Kapsam) Hataları
Scope, bir değişkenin "yaşam alanıdır" ve hatalar genellikle şu nedenlerle oluşur:
* **Yanlış Varsayımlar**: Geliştiriciler genellikle tüm değişkenlerin "her yerden" erişilebilir olduğunu varsayar. Ancak Python'da bir değişkeni fonksiyon içinde tanımladığınızda (local), o dışarıya (global) sızamaz.
* **Çakışmalar**: Farklı fonksiyonlarda aynı isimde değişken kullanıldığında sistemin hangisini referans alacağı karışıklığı yaşanır. Kapsam kurallarını anlamak, veri sızıntılarını ve beklenmedik sistem hatalarını önlemek için kritiktir.

## Try/Except Yapısının Kritikliği
Gerçek hayatın en temel kuralı şudur: Kullanıcı her zaman hata yapacaktır. 
* Bir kullanıcıdan sayı girmesini beklerken harf girmesi (ValueError), sistemin çökmesine neden olur.
* Try/Except yapısı, sistemin "durdurulamayan" değil, "hata yöneten" bir yapı olmasını sağlar. Profesyonel sistemlerde hata yakalama, yazılımın beklenmedik durumlarda bile zarif bir şekilde çalışmaya devam etmesini ve kullanıcıya anlamlı hata mesajları vermesini sağlar.

## Sistemin Geleceği
Sistemin daha profesyonel hale getirilmesi için öneriler:
1. **Veri Kalıcılığı**: Şu an veriler RAM'de geçici tutulmaktadır. Verilerin dosya işlemleri ile bir veri tabanına veya .txt dosyasına kaydedilmesi gerekir.
2. **Girdi Validasyonu**: Sadece tip kontrolü değil, harcamaların negatif değer olamayacağı gibi mantıksal kontrollerin de try/except ile güçlendirilmesi güvenliği artıracaktır.
3. **Nesne Yönelimli Yaklaşım (OOP)**: Fonksiyonel yaklaşım bir başlangıçtır; ancak sistem karmaşıklaştıkça bütçe asistanı bir BudgetAssistant sınıfına (class) dönüştürülerek veri ve metodlar birleştirilmelidir.

Hazırlayan: İkra Narin Soran
