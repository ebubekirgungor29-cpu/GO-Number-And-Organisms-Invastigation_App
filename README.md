# Karşılaştırmalı Genomik Analiz Web Uygulaması

Bu proje, biyolojik verilerin hızlı ve karşılaştırmalı analizi için geliştirilmiş yerel bir web uygulamasıdır. Kullanıcıların belirlediği organizma listesi ile bu organizmalarda aranacak Gen Ontology (GO) veya Enzim Komisyonu (EC) numaralarını kullanarak NCBI (National Center for Biotechnology Information) veritabanında otomatik sorgulamalar yapar. Sonuçları, anlaşılması kolay bir karşılaştırma matrisi (tablo) olarak sunar.

## Kurulum

Projeyi çalıştırmadan önce gerekli Python kütüphanelerini yüklemeniz gerekmektedir.

1.  **Proje dosyalarını indirin:** Projeyi bilgisayarınıza klonlayın veya zip olarak indirin.
2.  **Bağımlılıkları yükleyin:** Terminal veya komut istemcisini proje dizininde açın ve aşağıdaki komutu çalıştırın:

    ```bash
    pip install -r requirements.txt
    ```
    Bu komut, proje için gerekli olan Flask ve BioPython kütüphanelerini yükleyecektir.

## Nasıl Çalıştırılır?

Bağımlılıklar yüklendikten sonra, uygulamayı başlatmak için terminalde aşağıdaki komutu çalıştırın:

```bash
python app.py
```

Uygulama başlatıldığında, terminalde aşağıdakine benzer bir çıktı göreceksiniz:

```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Bu, web sunucusunun yerel makinenizde `5000` portunda çalışmaya başladığı anlamına gelir.

## Nasıl Kullanılır?

1.  Web tarayıcınızı açın ve `http://127.0.0.1:5000/` adresine gidin.
2.  **"Organizmalar"** kutusuna, analiz etmek istediğiniz canlıların bilimsel adlarını her satıra bir tane gelecek şekilde yazın.
3.  **"GO veya EC Numaraları"** kutusuna, aramak istediğiniz Gen Ontology veya Enzim Komisyonu numaralarını her satıra bir tane gelecek şekilde yazın.
4.  **"Analizi Başlat"** düğmesine tıklayın.
5.  Uygulama, NCBI veritabanında her bir organizma ve terim çifti için sorgulama yapacak ve sonuçları bir matris tablosu olarak size sunacaktır. Tablodaki `✓` işareti, ilgili organizmada o terime karşılık gelen bir kayıt bulunduğunu gösterir.
