-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: 15 Apr 2020 pada 16.44
-- Versi Server: 10.1.19-MariaDB
-- PHP Version: 5.6.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `absensi`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `tbl_guru`
--

CREATE TABLE `tbl_guru` (
  `nip` varchar(8) NOT NULL,
  `nama_guru` varchar(50) NOT NULL,
  `jk` varchar(10) NOT NULL,
  `alamat` varchar(255) NOT NULL,
  `no_hp` varchar(15) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `id_kelas` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `tbl_guru`
--

INSERT INTO `tbl_guru` (`nip`, `nama_guru`, `jk`, `alamat`, `no_hp`, `username`, `password`, `id_kelas`) VALUES
('12345678', 'Khesa Alviandi', 'laki-laki', 'Bogor', '0877621772131', 'khesa', 'pbkdf2:sha256:150000$MdFVSVW0$0b481673a62b5f399b5a', 3),
('87654322', 'arfino', 'laki-lakia', 'bekasi smb', '0872737332', 'fino', 'pbkdf2:sha256:150000$WD1gkyxu$03691757b8a62218d61a', 8);

-- --------------------------------------------------------

--
-- Struktur dari tabel `tbl_kelas`
--

CREATE TABLE `tbl_kelas` (
  `id_kelas` int(11) NOT NULL,
  `ruang_kelas` varchar(30) NOT NULL,
  `jml_siswa` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `tbl_kelas`
--

INSERT INTO `tbl_kelas` (`id_kelas`, `ruang_kelas`, `jml_siswa`) VALUES
(1, 'ruang15', 15),
(3, 'ruang10', 10),
(4, 'Ruang 4', 30);

-- --------------------------------------------------------

--
-- Struktur dari tabel `tbl_ortu`
--

CREATE TABLE `tbl_ortu` (
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `nis` varchar(12) NOT NULL,
  `nama_ortu` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `tbl_ortu`
--

INSERT INTO `tbl_ortu` (`username`, `password`, `nis`, `nama_ortu`) VALUES
('khairur', 'pbkdf2:sha256:150000$5cMGYekO$dfdf8003aaa7a4afd629f29de5af0665dd92e6e0ce33070b7de6d66997096e81', '12145522', 'Khairur Rozikin'),
('khesa', 'pbkdf2:sha256:150000$6j0WwHz6$560f63befb401c807f95abd1a0759d20dcc5b8f5344d87786f062c98b0214583', '12145420', 'Khesa Alviandi'),
('somad', 'pbkdf2:sha256:150000$WP5Tusvs$2177cf4888c3f1f1d2170862cc4a80bf1caf2fa4c0dae681e356d6632343af55', '12145521', 'Somad Dwi Zakaria');

-- --------------------------------------------------------

--
-- Struktur dari tabel `tbl_siswa`
--

CREATE TABLE `tbl_siswa` (
  `id` int(11) NOT NULL,
  `nis` varchar(12) NOT NULL,
  `nama_siswa` varchar(50) NOT NULL,
  `id_kelas` int(10) NOT NULL,
  `lokasi_terakhir` varchar(100) NOT NULL,
  `data_wajah` varchar(50) NOT NULL,
  `jam_masuk` datetime NOT NULL,
  `jam_keluar` datetime NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `tbl_siswa`
--

INSERT INTO `tbl_siswa` (`id`, `nis`, `nama_siswa`, `id_kelas`, `lokasi_terakhir`, `data_wajah`, `jam_masuk`, `jam_keluar`, `username`, `password`) VALUES
(1, '12145420', 'Muhammad Husain Giffary Alsaera', 1, '3_x_4.jpg', '3_x_4.jpg', '2020-04-13 07:00:00', '2020-04-13 12:00:00', 'husain211', 'pbkdf2:sha256:150000$7vyhKUzd$00156bd2d488a11773e0'),
(2, '12145521', 'Muhammad Sofii', 1, 'IMG-20200315-WA0013.jpg', 'IMG-20200315-WA0013.jpg', '2020-04-13 07:00:00', '2020-04-13 12:00:00', 'sofii', 'pbkdf2:sha256:150000$arcSiflV$6794287ff25791b4d8fa'),
(3, '12145522', 'Elva Yundra Rindyana', 1, 'IMG-20200315-WA0002.jpg', 'IMG-20200315-WA0002.jpg', '2020-04-13 07:00:00', '2020-04-13 12:00:00', 'elva', 'pbkdf2:sha256:150000$5CxjcM1D$1991e00918357e4a3e74'),
(4, '12145523', 'Nagita Slavina', 1, '0003.jpg', '0003.jpg', '2020-04-13 07:00:00', '2020-04-13 12:00:00', 'nagita', 'pbkdf2:sha256:150000$cbaDWt0h$e5e41c4cb6086232c06b'),
(5, '12145524', 'Raffi Ahmad', 1, '0004.jpg', '0004.jpg', '2020-04-13 07:00:00', '2020-04-13 12:00:00', 'raffi', 'pbkdf2:sha256:150000$h0am3unV$d32d0b08064054a66abb'),
(6, '12145525', 'Dilraba Dilmurat', 1, '0002.jpg', '0002.jpg', '2020-04-14 07:00:00', '2020-04-14 12:00:00', 'dilraba', 'pbkdf2:sha256:150000$0GEJjY0R$e944719278017935c63b'),
(7, '12145526', 'Iqbal Ramadhan', 1, '0001.jpg', '0001.jpg', '2020-04-14 07:00:00', '2020-04-14 12:00:00', 'iqbal', 'pbkdf2:sha256:150000$FcQf652k$b1d448a116c6524a29b5'),
(8, '12145527', 'Andres', 1, 'P_20200217_141528.jpg', 'P_20200217_141528.jpg', '2020-04-14 07:00:00', '2020-04-14 12:00:00', 'andres', 'pbkdf2:sha256:150000$MUA6sdka$976d1570fced11579cc4'),
(13, '12145420', 'Muhammad Husain Giffary Alsaera', 0, '20200414184033.jpg', '20200414184033.jpg', '0000-00-00 00:00:00', '2020-04-14 18:40:36', '', ''),
(14, '12145525', 'Dilraba Dilmurat', 0, '20200414184316.jpg', '20200414184316.jpg', '0000-00-00 00:00:00', '2020-04-14 18:43:16', '', ''),
(15, '12145420', 'Muhammad Husain Giffary Alsaera', 0, '20200414184341.jpg', '20200414184341.jpg', '0000-00-00 00:00:00', '2020-04-14 18:43:41', '', ''),
(16, '12145420', 'Muhammad Husain Giffary Alsaera', 0, '20200415143739.jpg', '20200415143739.jpg', '0000-00-00 00:00:00', '2020-04-15 14:37:42', '', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_guru`
--
ALTER TABLE `tbl_guru`
  ADD PRIMARY KEY (`nip`);

--
-- Indexes for table `tbl_kelas`
--
ALTER TABLE `tbl_kelas`
  ADD PRIMARY KEY (`id_kelas`);

--
-- Indexes for table `tbl_ortu`
--
ALTER TABLE `tbl_ortu`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `tbl_siswa`
--
ALTER TABLE `tbl_siswa`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_kelas`
--
ALTER TABLE `tbl_kelas`
  MODIFY `id_kelas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `tbl_siswa`
--
ALTER TABLE `tbl_siswa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
