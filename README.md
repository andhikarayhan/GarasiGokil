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


=================================================================TUGAS 4===================================================================================
1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
UserCreationForm adalah sebuah formulir (form) yang disediakan oleh Django untuk memudahkan proses pembuatan pengguna (user) dalam sistem otentikasi Django. Formulir ini secara khusus digunakan untuk mendaftarkan pengguna baru.

Kelebihan:
a. Mudah Digunakan
UserCreationForm menyediakan antarmuka pengguna yang mudah digunakan untuk mendaftarkan pengguna baru tanpa perlu menulis kode validasi dan penanganan form dari awal.

b. Integrasi Dengan Django
Form ini terintegrasi dengan baik dengan model pengguna bawaan Django (User). Ini mempermudah untuk membuat dan menyimpan pengguna baru ke dalam database.

c. Validasi Otomatis
UserCreationForm mencakup validasi otomatis untuk memastikan data yang dimasukkan sesuai dengan kebutuhan, seperti memastikan alamat email unik, password dengan panjang yang cukup, dll.

Kekurangan:
a. Tidak Fleksibel
Secara default, UserCreationForm memiliki struktur dan validasi bawaan yang mungkin tidak sesuai dengan kebutuhan proyek tertentu. Pada kasus tertentu, Anda mungkin perlu menyesuaikan atau memperluas fungsionalitasnya, yang memerlukan penyesuaian tambahan.


2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi adalah proses verifikasi identitas pengguna untuk memastikan bahwa pengguna yang mengakses sistem adalah pengguna yang sebenarnya dan memiliki izin untuk melakukannya. Ini melibatkan validasi kredensial yang diajukan oleh pengguna, seperti username dan password.

Otorisasi adalah proses mengontrol akses atau izin yang diberikan kepada pengguna setelah mereka berhasil terautentikasi. Ini menentukan apa yang diizinkan atau tidak diizinkan oleh pengguna yang terotentikasi dalam sistem.

Kedua hal ini penting karena autentikasi dan otorisasi adalah fondasi keamanan aplikasi, menjaga identitas pengguna dan mengendalikan akses ke sumber daya, sesuai dengan kebijakan dan peraturan yang berlaku.


3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies adalah file teks kecil yang disimpan pada perangkat pengguna oleh situs web yang dikunjungi. Cookies ini memungkinkan situs web untuk menyimpan informasi yang akan digunakan kembali, seperti preferensi pengguna atau data sesi, saat pengguna melanjutkan menjelajah situs tersebut.

Dalam konteks Django, cookies digunakan untuk mengelola data sesi pengguna. Data sesi adalah informasi yang dihasilkan dan disimpan di server untuk mengenali pengguna selama mereka berinteraksi dengan aplikasi web. Django menggunakan cookies untuk menyimpan identifier unik yang mengaitkan pengguna dengan data sesinya di server.

Secara khusus, Django menggunakan session middleware untuk mengelola cookies. Saat pengguna pertama kali mengakses aplikasi, server akan menghasilkan identifier unik (session ID) untuk sesi pengguna dan menyimpannya dalam cookie di perangkat pengguna. Selanjutnya, setiap permintaan yang dilakukan oleh pengguna akan menyertakan session ID ini, memungkinkan Django untuk mengidentifikasi dan memuat data sesi yang sesuai.

Dengan menggunakan cookies untuk mengelola data sesi, Django memungkinkan aplikasi untuk mempertahankan keadaan dan informasi pengguna antar permintaan, yang merupakan elemen kunci dalam pengembangan aplikasi web yang interaktif dan personal.


4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Cookies adalah file teks kecil yang disimpan pada perangkat pengguna oleh situs web yang dikunjungi. Cookies ini memungkinkan situs web untuk menyimpan informasi yang akan digunakan kembali, seperti preferensi pengguna atau data sesi, saat pengguna melanjutkan menjelajah situs tersebut.

Dalam konteks Django, cookies digunakan untuk mengelola data sesi pengguna. Data sesi adalah informasi yang dihasilkan dan disimpan di server untuk mengenali pengguna selama mereka berinteraksi dengan aplikasi web. Django menggunakan cookies untuk menyimpan identifier unik yang mengaitkan pengguna dengan data sesinya di server.

Secara khusus, Django menggunakan session middleware untuk mengelola cookies. Saat pengguna pertama kali mengakses aplikasi, server akan menghasilkan identifier unik (session ID) untuk sesi pengguna dan menyimpannya dalam cookie di perangkat pengguna. Selanjutnya, setiap permintaan yang dilakukan oleh pengguna akan menyertakan session ID ini, memungkinkan Django untuk mengidentifikasi dan memuat data sesi yang sesuai.

Dengan menggunakan cookies untuk mengelola data sesi, Django memungkinkan aplikasi untuk mempertahankan keadaan dan informasi pengguna antar permintaan, yang merupakan elemen kunci dalam pengembangan aplikasi web yang interaktif dan personal.


5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama saya mengimplementasi fungsi register, login, dan logout pada views.py, lalu saya memodifikasi pesan-pesan agar sesuai dengan tema aplikasi saya.
Lalu untuk register dan login saya buatkan berkas-berkas HTML-nya masing-masing. Saya menambahkan restiksi agar user login/register terlebih dahulu dengan menambahkan @login_required pada sebelum fungsi show_main.

Untuk cookiesnya, pada fungsi show_main bagian context, saya menambahkan 'last_login': request.COOKIES['last_login'] agar tersimpan data cookies setiap user. Lalu saya hubungkan Item dengan User yang sesuai dengan menggunakan Foreign Key. Terakhir saya stylize page register dan login agar sesuai tema aplikasi saya.

