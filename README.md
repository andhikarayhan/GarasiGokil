Perbedaan antara Form POST dan Form GET dalam Django?
Form POST: Mengirimkan data form melalui body permintaan HTTP, tidak terlihat di URL. Ideal untuk data sensitif. 
Form GET: Mengirimkan data form melalui URL. Data dapat terlihat di URL, digunakan untuk data non-sensitif atau pencarian. 

Perbedaan antara XML, JSON, dan HTML dalam konteks pengiriman data? 
XML (eXtensible Markup Language): Bahasa markup untuk mendefinisikan aturan khusus dalam dokumen teks, digunakan untuk pertukaran data terstruktur. 
JSON (JavaScript Object Notation): Format pertukaran data ringan, mudah dibaca manusia, dan mudah diinterpretasikan oleh mesin. Umum digunakan dalam pertukaran data antar aplikasi. 
HTML (HyperText Markup Language): Bahasa markup untuk mendefinisikan struktur dan tampilan konten di web, tidak untuk pertukaran data antar aplikasi.

Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON merupakan format data yang sederhana dan mudah dipahami oleh manusia. Selain itu, JSON memiliki kompatibilitas yang luas dengan hampir semua bahasa pemrograman, memudahkan pertukaran data antar berbagai aplikasi. Cocok dengan lingkungan pengembangan aplikasi web modern, terutama yang berbasis JavaScript. Keunggulannya juga terletak pada efisiensi pertukaran data karena ukuran JSON lebih kecil dibandingkan XML, menjadi penting untuk aplikasi web dengan kinerja tinggi.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
1. Membuat sebuah forms.py dimana dari berkas models dari aplikasi main mengimport sebuah Item atau untuk konteks ini sebuah mobil
2. Pada berkas views.py, saya membuat sebuah fungsi bernama create_item, lalu pada fungsi show_main saya memasukkan seluruh hasil form ke dalam variabel bernama Items. Pada form tersebut saya membuat page form dengan create_item.html
3. saya integrasikan page form dengan ke main page saya dengan melakukan beberapa kustomisasi saya sendiri
4. Untuk melakukan poin 2 dan 3 pada tugas 3, saya cukup menambahkan fungsi untuk XML, JSON ,XML_BY_ID,JSON_BY_ID dan mentranslate objek modoel atau mobil saya menjadi format yang sesuai

---------POSTMAN-----------------
![XML](https://github.com/andhikarayhan/GarasiGokil/blob/main/Screenshot%202023-09-20%20034533.png)
![JSON](https://github.com/andhikarayhan/GarasiGokil/blob/main/Screenshot%202023-09-20%20034604.png)
![XMLBYID](https://github.com/andhikarayhan/GarasiGokil/blob/main/Screenshot%202023-09-20%20035029.png)
![JSONBYID](https://github.com/andhikarayhan/GarasiGokil/blob/main/Screenshot%202023-09-20%20035146.png)