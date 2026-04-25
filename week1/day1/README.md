# Smart User Data Cleaner

## Projenin Amacı
[cite_start]Smart User Data Cleaner projesinin amacı, ham ve yapılandırılmamış verileri sistemin işleyebileceği temiz ve standart bir formata dönüştürmektir[cite: 3].

## Veri Temizlemenin Önemi
* [cite_start]Veri temizleme, ham veride bulunan gürültüleri ve format bozukluklarını ayıklayarak veriyi analiz edilebilir ve güvenilir bir forma dönüştürme sürecidir[cite: 5].
* [cite_start]Hatalı veya düzensiz veriler yazılım sistemlerinde *Runtime Error* oluşmasına veya yanlış sonuçlar üretilmesine neden olduğu için, *Data Preprocessing* aşaması projenin en kritik adımını oluşturur[cite: 6].
* [cite_start]Bu proje ile kullanıcıdan gelen standart dışı girdiler, Python'un metin işleme yetenekleri kullanılarak *Normalization* sürecinden geçirilmiş ve sistemin işleyebileceği rafine çıktılar elde edilmiştir[cite: 7].

## String İşlemlerinin Rolü
* [cite_start]*String* işlemleri, yapılandırılmamış metin verilerini belirli bir düzene sokarak bilgisayar sistemlerinin bu verileri anlamlandırabilmesini ve işlemesini sağlar[cite: 9].
* [cite_start]Veri dönüştürme sürecinde kritik bir rol oynayan bu işlemler; verideki gürültüleri temizlemek, karmaşık metinleri parçalara ayırmak ve bilgiyi standart bir formata getirmek için kullanılan en temel araçlardır[cite: 10].

## Kullanılan Python Konuları
* [cite_start]**Variables**: Verilerin bilgisayar belleğinde geçici olarak saklandığı isimlendirilmiş depolama birimleridir[cite: 12]. [cite_start]Bu projede ham verinin parçalanmış hallerini ve işlenmiş sonuçlarını organize bir şekilde yönetmek amacıyla kullanılmıştır[cite: 13].
* [cite_start]**String Veri Tipi**: Metinsel ifadeleri temsil eder; kullanıcı bilgilerinin saklanması ve manipüle edilmesi için temel yapı taşı görevini görmüştür[cite: 14].
* [cite_start]**String Slicing**: Bir metin dizisinin belirli bir alt kümesine indeks numaraları kullanarak erişme işlemidir[cite: 15]. [cite_start]Veri içerisinden sadece ihtiyaç duyulan karakterlerin (örneğin e-posta adresindeki kullanıcı adı kısmı gibi) cımbızla çekilip alınmasını sağlar[cite: 16].
* **String Metodları**:
    * [cite_start]`strip()`: Metnin dış çeperindeki gereksiz boşlukları temizleyerek veri bütünlüğünü sağlar[cite: 18].
    * [cite_start]`lower()`: Tüm harfleri küçük harfe dönüştürerek standart bir zemin oluşturur[cite: 19].
    * [cite_start]`title()`: Her kelimenin ilk harfini büyüterek yazım kurallarına uygun hale getirilmesini sağlar[cite: 20].
    * [cite_start]`split()`: Belirli bir ayırıcı karakteri baz alarak uzun bir metni yönetilebilir parçalara böler[cite: 21].
    * [cite_start]`find()`: Metin içerisinde belirli bir karakterin konumunu tespit ederek dinamik kesme işlemleri yapılmasına olanak tanır[cite: 22, 23, 24].
* [cite_start]**Type Casting (int/float)**: Metin olarak gelen sayısal ifadelerin matematiksel işleme sokulabilmesi için veri tipinin değiştirilmesidir[cite: 25]. [cite_start]Yaş veya boy gibi verilerin aritmetiksel hesaplamalara uygun hale getirilmesini sağlar[cite: 26].

## Veri Temizleme Süreci
### Ham Verideki Problemler
* [cite_start]**Gereksiz Boşluklar**: Verilerin başında, sonunda ve arasında bulunan tutarsız boşluklar[cite: 29].
* [cite_start]**Düzensiz Büyük-Küçük Harf**: Verilerin standart bir yazım diline sahip olmaması[cite: 30].
* [cite_start]**Veri Tipi Uyumsuzluğu**: Sayısal olması gereken verilerin metin formatında gelmesi[cite: 31].
* [cite_start]**Bitişik Veri Yapısı**: Bilgilerin ayırıcılarla birbirine girmiş halde tek bir metin olması[cite: 32].

### Çözüm Adımları
1. [cite_start]**Genel Temizlik ve Parçalama**: `strip()` ile boşluklar atılmış, `split(";")` ile bitişik yapı parçalara bölünmüştür[cite: 34].
2. [cite_start]**Metin Normalizasyonu**: İsim ve e-posta verileri `title()`, `lower()` ve *slicing* teknikleriyle standartlara getirilmiştir[cite: 35].
3. [cite_start]**Matematiksel Dönüşüm**: `int()` ve `float()` dönüşümleriyle sayısal veriler üzerindeki "string engeli" kaldırılmış; aritmetik hesaplamalar mümkün kılınmıştır[cite: 36].
4. [cite_start]**Özel Bilgi Çıkarımı**: `find("@")` ve *slicing* ile e-postanın tamamı yerine sadece istenen "kullanıcı kodu" dinamik olarak elde edilmiştir[cite: 37].

## Sonuç ve Değerlendirme
* [cite_start]Temizlenmemiş veri, yazılımın tüm aşamalarında *Runtime Error* ve *Logic Error* riski oluşturur[cite: 39, 46].
* [cite_start]Bu proje, kullanıcı kaynaklı düzensiz veri girişlerinin filtrelenmesini sağlamış, veri tabanı mimarisine uygun atomik bir veri seti oluşturmuştur[cite: 44, 45].

**Gerçek Hayatta Kullanım Alanları**:
* [cite_start]Form Verisi İşleme [cite: 49]
* [cite_start]Log Analizi [cite: 50]
* [cite_start]CSV/Excel Ön İşleme (*Data Wrangling*) [cite: 51]

[cite_start]**Kazanılan Beceriler**: *String Manipulation*, *Slicing*, *Type Casting* ve *Method Chaining* teknikleri pekiştirilmiştir[cite: 54, 55].

---
[cite_start]*Hazırlayan: İkra Narin Soran* [cite: 56]
