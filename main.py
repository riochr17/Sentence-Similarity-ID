from sentence_simi import SentenceSimi

sentleft = [
	"Pengadilan Negeri Jakarta Utara benarkan surat gugatan cerai Ahok",
	"Surat gugatan cerai bertanggal 5 Januari 2018 itu dilayangkan kepada Ketua Pengadilan Negeri Jakarta Utara",
	"Pengadilan Negeri (PN) Jakarta Utara membenarkan  masuknya surat gugatan cerai  mantan Gubernur DKI Jakarta Basuki Tjahaja Purnama atau Ahok terhadap istrinya",
	"Dalam surat itu disebut Fifi Lety Indra, SH, LLM dan Josefina Agata Syukur, SH, MA, berlaku sebagai kuasa hukum Ahok",
	"Astronot kawakan Amerika John Young meninggal pada usia 87 tahun",
	"Mantan pilot angkatan laut AS itu adalah orang kesembilan yang menginjakkan kaki di bulan",
	"Dia satu-satunya orang yang terlibat terbang di ketiga jenis program ini",
	"Dia dibunuh oleh tukang pijit langganannya yang bernama AM (20)",
	"Korban mengatakan bahwa pelaku hanya bisa meminta-minta uang saja",
	"Ditemukan di selokan , karyawati BUMN diduga terjun dari lantai 10",
	"Meritha yang diketahui bekerja di perusahaan BUMN diduga tewas setelah melompat dari lantai 10 apartemen tersebut",
	"Pagi ini , Jokowi bakal penuhi janjinya kunjungi Pulau Rote",
	"Presiden Jokowi akan bertolak ke Kupang , NTT terlebih dahulu menggunakan pesawat kepresidenan dari Pangkalan Udara TNI AU Halim Perdanakusuma , Jakarta Timur",
	"Presiden akan membagikan kartu Indonesia Pintar , memberikan kuliah umum di Universitas Muhammadiyah Kupang , dan menyerahkan sertifikat tanah untuk rakyat",
	"Kasus korupsi e-KTP , KPK kembali panggil Marzuki Alie",
	"Selain Marzuki , ada 2 saksi lain yang dipanggil untuk tersangka yang sama",
	"Mantan Ketua DPR Marzuki Alie kembali dipanggil penyidik KPK terkait kasus korupsi proyek e-KTP",
	"Pemerintah Iran dikabarkan melarang pengajaran bahasa Inggris di sekolah-sekolah dasar di seluruh negeri itu",
	"Langkah ini diambil setelah pemimpian tertinggi Iran mengatakan , pembelajaran bahasa asing di masa-masa awal sekolah melicinkan jalan invasi budaya Barat ke negeri tersebut",
	"Pada 2016 , pemimpin tertinggi Ayatollah Ali Khamenei , yang menjadi penentu kebijakan di Iran , mengungkapkan kemarahannya setelah mengetahui bahwa bahasa Inggris diajarkan di taman kanak-kanak",
	"Istri dan Dua Anak Setya Novanto Diperiksa KPK",
	"Desti Tagor hadir di KPK pukul 13.50 WIB",
	"Dalam pemeriksaan dua anak Novanto itu, KPK ingin mendalami kepemilikan saham PT Mondialindo Graha Perdana yang merupakan pemegang saham mayoritas dari PT Murakabi Sejahtera",
	"Dokter Rumah Sakit Rawat Setya Novanto Tersangka?",
	"Selain Bimanesh, dalam perkara menghalangi penyidikan itu KPK pun telah menetapkan eks pengacara Setnov, Fredrich Yunadi sebagai tersangka."
];

sentRight = [
	"Pengacara benarkan Ahok gugat cerai Veronica Tan",
	"Surat gugatan telah didaftarkan di Pengadilan Negeri Jakarta Utara pada Jumat (5/1/2018)",
	"Seorang petugas pendaftaran perkara perdata di PN Jakarta Utara membenarkan adanya 3 gugatan itu",
	"Ahok menunjuk Law Firm Fifi Lety Indra & Partners sebagai kuasa hukumnya dalam kasus itu",
	"Young , astronaut paling berpengalaman AS meninggal dunia",
	"Young yang melakukan perjalanan ke ruang angkasa sebanyak enam kali adalah manusia ke sembilan yang menapakkan kakinya di bulan",
	"Dia adalah satu-satunya orang yang terbang ke ruang angkasa dalam tiga program",
	"Ia dihabisi oleh Acep , tukang pijat langganannya sendiri",
	"Korban justru mengatakan datang kalau butuh uang saja",
	"Lompat dari lantai 10 apartemen , perempuan  ini tewas mengenaskan di depan Thamrin City",
	"Meritha yang diketahui sebagai pegawai BUMN diduga bunuh diri dengan cara melompat dari lantai 10 apartemen Cosmo Park",
	"Tepati janji , Jokowi kunjungi Pulau Rote hari ini",
	"Jokowi dan Ibu Negara Iriana Jokowi hari ini bertolak menuju Kupang , NTT , dari Pangkalan TNI AU Halim Perdanakusuma Jakarta , pada pukul 06.42 WIB menggunakan pesawat kepresidenan Indonesia-1",
	"Mantan Gubernur DKI Jakarta itu akan membagikan Kartu Indonesia Pintar , memberikan kuliah umum di Universitas Muhammadiyah Kupang , dan menyerahkan sertifikat tanah untuk rakyat",
	"Kasus E-KTP , KPK periksa mantan ketua DPR Marzuki Alie",
	"Selain Marzuki ,  ada dua anggota DPR periode 2009-2014 lainnya yang diperiksa",
	"Marzuki akan diperiksa terkait kasus dugaan korupsi pengadaan kartu tanda penduduk elektronik",
	"Seorang pejabat pendidikan senior mengatakan Iran melarang pengajaran bahasa Inggris di Sekolah Dasar (SD)",
	"Larangan ini diberlakukan setelah para pemimpin Islam memperingatkan bahwa pembelajaran bahasa tersebut awal membuka jalan menuju invasi budaya Barat",
	"Pemimpin tertinggi , Ayatollah Ali Khamenei , menyuarakan kemarahan pada tahun 2016 atas pengajaran bahasa Inggris yang menyebar ke sekolah dasar",
	"Selain Setya Novanto dan Anaknya, Istri Kedua Novanto Juga Datangi KPK",
	"Deisti tiba di KPK Rabu sekitar pukul 13.47 WIB",
	"Dalam pemeriksaan terhadap Dwina Michaella, Kamis (21/12/2017), penyidik KPK mendalami yang berkaitan dengan saham PT Murakabi Sejahtera.",
	"Selain Fredrich, KPK Juga Tetapkan Dokter sebagai Tersangka",
	"Bimanesh ditetapkan bersama-sama dengan mantan kuasa hukum Setnov dalam kasus e-KTP, Fredrich Yunadi."
]

for i in range(25):
	ss = SentenceSimi(sentleft[i], sentRight[i])
	print sentleft[i], "\n", sentRight[i], "\n", ss.getSimilarityScore(), "\n"

