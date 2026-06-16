from flask import Flask, render_template

app = Flask(__name__)

profil = {
    "nama": "Ilmu Komputer",
    "fakultas": "Fakultas Sains, Teknologi, dan Ilmu Kesehatan (FSTIK)",
    "universitas": "Universitas Bina Bangsa Getsempena",
    "akreditasi": "Baik Sekali",
    "tahun_berdiri": 2021,
    "deskripsi": (
        "Program Studi Ilmu Komputer Universitas Bina Bangsa Getsempena merupakan "
        "program studi yang berfokus pada pengembangan ilmu pengetahuan dan "
        "teknologi di bidang komputasi, kecerdasan buatan, rekayasa perangkat "
        "lunak, serta sistem informasi. Program studi ini berkomitmen pada "
        "Tridharma Perguruan Tinggi untuk menghasilkan lulusan yang kompeten, "
        "berinovasi, dan berkontribusi pada masyarakat."
    ),
    "visi": (
        "Menjadi program studi Ilmu Komputer yang unggul, mandiri, dan religius "
        "serta mampu memberikan kontribusi positif bagi masyarakat melalui "
        "inovasi, pengabdian, dan kolaborasi di tingkat nasional maupun "
        "internasional."
    ),
    "misi": [
        "Menyelenggarakan pendidikan berkualitas di bidang Ilmu Komputer yang relevan dengan kebutuhan industri dan masyarakat.",
        "Melaksanakan penelitian inovatif yang berkontribusi pada pengembangan ilmu pengetahuan dan teknologi informasi.",
        "Melaksanakan pengabdian kepada masyarakat berbasis teknologi informasi untuk mendukung program Kampus Berdampak.",
        "Membangun kerjasama strategis dengan industri, pemerintah, dan institusi pendidikan di tingkat nasional dan internasional.",
        "Menghasilkan lulusan yang kompeten, berkarakter, dan mampu beradaptasi dengan perkembangan teknologi global.",
    ],
}

dosen = [
    {
        "nama": "Dr. Ahmad Fauzi, M.T.",
        "nip": "197203152000031002",
        "bidang": "Kecerdasan Buatan",
        "email": "a.fauzi@bbg.ac.id",
        "pendidikan": "S3 – Universitas Indonesia",
    },
    {
        "nama": "Dr. Siti Rahmah, M.Kom.",
        "nip": "198005202006042001",
        "bidang": "Rekayasa Perangkat Lunak",
        "email": "s.rahmah@bbg.ac.id",
        "pendidikan": "S3 – Institut Teknologi Bandung",
    },
    {
        "nama": "Mukhlis Ramadhan, S.T., M.T.",
        "nip": "198812042015041003",
        "bidang": "Jaringan Komputer",
        "email": "m.ramadhan@bbg.ac.id",
        "pendidikan": "S2 – Universitas Gadjah Mada",
    },
    {
        "nama": "Dr. Nurul Husna, M.Sc.",
        "nip": "198706152013042002",
        "bidang": "Sistem Basis Data",
        "email": "n.husna@bbg.ac.id",
        "pendidikan": "S3 – Universiti Teknologi Malaysia",
    },
    {
        "nama": "Rizky Ananda, S.Kom., M.Cs.",
        "nip": "199001082018031001",
        "bidang": "Pemrograman Web & Mobile",
        "email": "r.ananda@bbg.ac.id",
        "pendidikan": "S2 – Universitas Gadjah Mada",
    },
    {
        "nama": "Dra. Mariana Fitri, M.Pd.",
        "nip": "197508142003122005",
        "bidang": "Sistem Informasi",
        "email": "m.fitri@bbg.ac.id",
        "pendidikan": "S2 – Universitas Syiah Kuala",
    },
]

mahasiswa = [
    {"nim": "24210001", "nama": "Andi Maulana",       "angkatan": 2024, "ipk": 3.85, "status": "Aktif"},
    {"nim": "24210002", "nama": "Bunga Pertiwi",      "angkatan": 2024, "ipk": 3.72, "status": "Aktif"},
    {"nim": "24210003", "nama": "Chairul Anwar",      "angkatan": 2024, "ipk": 3.50, "status": "Aktif"},
    {"nim": "24210004", "nama": "Dina Marlina",       "angkatan": 2024, "ipk": 2.90, "status": "Cuti"},
    {"nim": "24210005", "nama": "Eko Prasetyo",       "angkatan": 2024, "ipk": 3.10, "status": "Aktif"},
    {"nim": "25210001", "nama": "Fitri Handayani",    "angkatan": 2025, "ipk": 3.65, "status": "Aktif"},
    {"nim": "25210002", "nama": "Gilang Ramadhan",    "angkatan": 2025, "ipk": 3.45, "status": "Aktif"},
    {"nim": "25210003", "nama": "Hana Safira",        "angkatan": 2025, "ipk": 3.80, "status": "Aktif"},
    {"nim": "25210004", "nama": "Ilham Syahputra",    "angkatan": 2025, "ipk": 2.75, "status": "Cuti"},
    {"nim": "25210005", "nama": "Julia Maharani",     "angkatan": 2025, "ipk": 3.40, "status": "Aktif"},
    {"nim": "26210001", "nama": "Kevin Kurniawan",    "angkatan": 2026, "ipk": 3.55, "status": "Aktif"},
    {"nim": "26210002", "nama": "Laila Nur Fadhilah", "angkatan": 2026, "ipk": 3.78, "status": "Aktif"},
    {"nim": "26210003", "nama": "Muhammad Rizal",     "angkatan": 2026, "ipk": 3.20, "status": "Aktif"},
    {"nim": "26210004", "nama": "Nadia Syahputri",    "angkatan": 2026, "ipk": 2.60, "status": "Cuti"},
    {"nim": "26210005", "nama": "Omar Abdillah",      "angkatan": 2026, "ipk": 3.90, "status": "Aktif"},
]

kontak = {
    "alamat": "Gedung UBBG Jl. Tanggul Krueng Lamnyong No.34 Rukoh, Kecamatan Syiah Kuala, Kota Banda Aceh, Indonesia 23112",
    "telepon": "(+62) 823-2121-1883",
    "website": "https://bbg.ac.id",
    "email": "info@bbg.ac.id",
    "pengaduan": "https://lapor.bbg.ac.id",
    "jam_operasional": "Senin – Jumat, 08.00 – 16.00 WIB",
    "sosmed": [
        {"nama": "Instagram",  "icon": "IG", "url": "https://www.instagram.com/ubbgofficial", "handle": "@ubbgofficial"},
        {"nama": "YouTube",    "icon": "YT", "url": "https://www.youtube.com/@ubbgofficial",  "handle": "@ubbgofficial"},
        {"nama": "LinkedIn",   "icon": "LI", "url": "https://www.linkedin.com/company/ubbgofficial", "handle": "@ubbgofficial"},
        {"nama": "Facebook",   "icon": "FB", "url": "https://www.facebook.com/ubbgofficial",  "handle": "@ubbgofficial"},
        {"nama": "TikTok",     "icon": "TK", "url": "https://www.tiktok.com/@ubbgofficial",   "handle": "@ubbgofficial"},
        {"nama": "X / Twitter","icon": "X",  "url": "https://x.com/ubbgofficial",             "handle": "@ubbgofficial"},
    ],
}


@app.route("/")
def home():
    stats = {
        "total_dosen": len(dosen),
        "total_mahasiswa": len(mahasiswa),
        "total_aktif": sum(1 for m in mahasiswa if m["status"] == "Aktif"),
        "akreditasi": profil["akreditasi"],
    }
    return render_template("home.html", profil=profil, stats=stats)


@app.route("/profil")
def profil_prodi():
    return render_template("profil.html", profil=profil)


@app.route("/dosen")
def daftar_dosen():
    return render_template("dosen.html", dosen=dosen, profil=profil)


@app.route("/mahasiswa")
def daftar_mahasiswa():
    return render_template("mahasiswa.html", mahasiswa=mahasiswa, profil=profil)


@app.route("/kontak")
def kontak_prodi():
    return render_template("kontak.html", kontak=kontak, profil=profil)


if __name__ == "__main__":
    app.run(debug=True)