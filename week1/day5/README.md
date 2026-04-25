# Smart Library Management System

## Özet
Bu teknik rapor, Nesne Yönelimli Programlama (OOP) prensipleri kullanılarak geliştirilmiş bir Akıllı Kütüphane Yönetim Sistemi'nin mimari tasarımını, teknik gereksinimlerini ve uygulama süreçlerini belgelemektedir. Projenin temel amacı, kütüphane bünyesindeki kitap, üye ve ödünç alma süreçlerini gerçek dünya nesneleriyle eşleştirerek dijital bir ekosistem yaratmaktır. Geliştirilen bu sistem, kodun tekrar kullanılabilirliğini, sistem güvenliğini ve gelecekteki genişletilebilirlik imkanlarını maksimize eden mühendislik tabanlı bir çözüm olarak tasarlanmıştır.

## OOP (Nesne Yönelimli Programlama) Neden Gereklidir?
Yazılım geliştirme süreci, kodun karmaşıklığı arttıkça yönetilmesi güç bir hale gelir. Geleneksel prosedürel programlama, orta ve büyük ölçekli sistemlerde verinin ve fonksiyonların birbirine karışmasına (spagetti kod) neden olur.
* OOP, karmaşıklığı çözmek için sınıflandırma mantığını kullanır. 
* Yazılımı somut varlıklara (nesnelere) bölerek, her bir nesnenin sadece kendi verisinden ve görevinden sorumlu olduğu bir düzen kurar. 
* Bu düzen, kodun okunabilirliğini artırır, yazılımın uzun ömürlü olmasını sağlar ve yeni özelliklerin sisteme zarar vermeden eklenmesine olanak tanır.

## Class ve Object Farkı
* **Sınıf (Class)**: Sistemimizin mimari planıdır; içinde verilerin hangi isimlerle tutulacağını ve hangi işlevlerin (metotların) bu verilerle çalışacağını tanımlarız. Bellekte somut bir yer kaplamaz, yalnızca bir şablondur.
* **Nesne (Object)**: O şablondan türetilen, bellekte verileriyle birlikte var olan somut bir örnektir. Örneğin Book sınıfı bir matbaa kalıbıysa, 'Suç ve Ceza' isimli kitap o kalıptan çıkmış, kendine has değerlere sahip gerçek bir nesnedir.

## Inheritance (Kalıtım)
Inheritance, doğadaki biyolojik hiyerarşinin yazılıma uyarlanmış halidir. Alt sınıfların üst sınıfların tüm özelliklerini ve davranışlarını miras almasını sağlayarak kod tekrarını sıfıra indirir. Örneğin, bir 'Dijital Kitap' kavramı, 'Kitap' kavramının tüm temel özelliklerini barındırır. Bu durum, "daha az kod, daha çok işlevsellik" prensibini hayata geçirir.

## Bu Projede Neden OOP Tercih Edildi?
* Kütüphane gibi varlıkların birbirleriyle sürekli etkileşimde olduğu sistemleri en doğal şekilde modellemek için OOP en uygun yaklaşımdır.
* Bir üye nesnesi ile bir kitap nesnesi arasındaki ödünç alma işlemi, OOP dünyasında üye nesnesinin bir metodu aracılığıyla kitabın durumunu değiştirmek kadar basittir. 
* OOP'nin sunduğu genişletilebilirlik, sistemin gelecekte sesli kitap veya farklı kullanıcı tipleri gibi yeni gereksinimlerle büyümesine olanak tanır.

## Try/Except Yapısının Kritikliği
Yazılım geliştirme, kullanıcı hataları ve sistem belirsizlikleriyle dolu bir dünyada gerçekleşir. 
* Bir kullanıcıdan sayı girmesini istediğimizde harf girmesi veya sistemin hatalı bir hesaplama yapması, programın aniden durmasına neden olabilir.
* Try/except bloğu, sistemin hata yapma ihtimalini öngören bir sigorta görevi görür. Hata olduğunda kodun çökmesi yerine, sistemin hatayı yakalamasını ve kullanıcıya anlamlı bir mesaj vererek akışı güvenli bir şekilde devam ettirmesini sağlar.

Hazırlayan: İkra Narin Soran
