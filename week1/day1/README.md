# Smart User Data Cleaner

## Projenin Amacı
Smart User Data Cleaner projesinin amacı, ham ve yapılandırılmamış verileri sistemin işleyebileceği temiz ve standart bir formata dönüştürmektir.

## Veri Temizlemenin Önemi
* Veri temizleme, ham veride bulunan gürültüleri ve format bozukluklarını ayıklayarak veriyi analiz edilebilir ve güvenilir bir forma dönüştürme sürecidir.
* Hatalı veya düzensiz veriler yazılım sistemlerinde Runtime Error oluşmasına veya yanlış sonuçlar üretilmesine neden olduğu için, Data Preprocessing aşaması projenin en kritik adımını oluşturur.
* Bu proje ile kullanıcıdan gelen standart dışı girdiler, Python'un metin işleme yetenekleri kullanılarak Normalization sürecinden geçirilmiş ve sistemin işleyebileceği rafine çıktılar elde edilmiştir.

## String İşlemlerinin Rolü
* String işlemleri, yapılandırılmamış metin verilerini belirli bir düzene sokarak bilgisayar sistemlerinin bu verileri anlamlandırabilmesini ve işlemesini sağlar.
* Veri dönüştürme sürecinde kritik bir rol oynayan bu işlemler; verideki gürültüleri temizlemek, karmaşık metinleri parçalara ayırmak ve bilgiyi standart bir formata getirmek için kullanılan en temel araçlardır.

## Kullanılan Python Konuları
* **Variables**: Verilerin bilgisayar belleğinde geçici olarak saklandığı isimlendirilmiş depolama birimleridir. Bu projede ham verinin parçalanmış hallerini ve işlenmiş sonuçlarını organize bir şekilde yönetmek amacıyla kullanılmıştır.
* **String Veri Tipi**: Metinsel ifadeleri temsil eden veri yapısıdır. Bu projede kullanıcı bilgilerinin (isim, email vb.) saklanması ve manipüle edilmesi için temel yapı taşı görevini görmüştür.
* **String Slicing**: Bir metin dizisinin belirli bir alt kümesine indeks numaraları kullanarak erişme işlemidir. Veri içerisinden sadece ihtiyaç duyulan karakterlerin cımbızla çekilip alınmasını sağlar.
* **String Metodları**: 
    * **strip()**: Metnin dış çeperindeki gereksiz boşlukları temizleyerek veri bütünlüğünü sağlar.
    * **lower()**: Metindeki tüm harfleri küçük harfe dönüştürerek veri karşılaştırmalarında ve işlemede standart bir zemin oluşturur.
    * **title()**: Her kelimenin ilk harfini büyüterek özel isim gibi verilerin yazım kurallarına uygun hale getirilmesini sağlar.
    * **split()**: Belirli bir ayırıcı karakteri baz alarak uzun bir metni yönetilebilir parçalara böler.
    * **find()**: Metin içerisinde belirli bir karakterin konumunu tespit ederek dinamik kesme işlemleri yapılmasına olanak tanır.
* **Type Casting (int ve float)**: Metin olarak gelen sayısal ifadelerin matematiksel işleme sokulabilmesi için veri tipinin değiştirilmesidir. Yaş gibi tam sayı veya boy gibi ondalıklı sayı gerektiren verilerin aritmetiksel hesaplamalara uygun hale getirilmesini sağlar.

## Veri Temizleme Süreci
### Ham Verideki Problemler
* **Gereksiz Boşluklar**: Verilerin başında, sonunda ve arasında bulunan tutarsız boşluklar.
* **Düzensiz Büyük-Küçük Harf Kullanımı**: Verilerin standart bir yazım diline sahip olmaması.
* **Veri Tipi Uyumsuzluğu**: Yaş ve boy gibi sayısal olması gereken verilerin metin formatında gelmesi.
* **Bitişik Veri Yapısı**: Tüm bilgilerin tek bir uzun metin içerisinde, ayırıcılarla birbirine girmiş olması.

### Çözüm Adımları
1. **Genel Temizlik ve Parçalama**: strip() ile dış boşluklar atılmış, split(";") ile bitişik yapı parçalara bölünmüştür.
2. **Metin Normalizasyonu**: İsim ve e-posta verileri title(), lower() ve slicing teknikleriyle standartlara getirilmiştir.
3. **Matematiksel Dönüşüm**: int() ve float() dönüşümleriyle sayısal veriler üzerindeki string engeli kaldırılmış, aritmetik hesaplamalar mümkün kılınmıştır.
4. **Özel Bilgi Çıkarımı**: find("@") ve slicing ile e-postanın tamamı yerine sadece istenen kullanıcı kodu dinamik olarak elde edilmiştir.

## Sonuç ve Değerlendirme
* Temizlenmemiş veri, yazılımın tüm aşamalarında Runtime Error ve Logic Error riski oluşturur.
* Bu proje, kullanıcı kaynaklı düzensiz veri girişlerinin filtrelenmesini sağlamış, veri tabanı mimarisine uygun, temiz ve atomik bir veri seti oluşturmuştur.

**Gerçek Hayatta Kullanım Alanları**:
* Form Verisi İşleme
* Log Analizi
* CSV/Excel Ön İşleme

**Kazanılan Beceriler**: String Manipulation, Slicing, Type Casting ve Method Chaining teknikleri pekiştirilmiştir.

Hazırlayan: İkra Narin Soran
