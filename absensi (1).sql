-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 13, 2020 at 12:28 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
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
-- Table structure for table `tbl_guru`
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
-- Dumping data for table `tbl_guru`
--

INSERT INTO `tbl_guru` (`nip`, `nama_guru`, `jk`, `alamat`, `no_hp`, `username`, `password`, `id_kelas`) VALUES
('10101010', 'test', 'perempuan', 'jakarta', '02838291', 'tes', 'tes', 1),
('83839292', 'coba', 'laki-laki', 'jakarta', '92832839829', 'coba', 'coba', 2),
('87654322', 'arfino', 'laki-lakia', 'bekasi smb', '0872737332', 'fino', 'pbkdf2:sha256:150000$WD1gkyxu$03691757b8a62218d61a', 8);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_kelas`
--

CREATE TABLE `tbl_kelas` (
  `id_kelas` int(11) NOT NULL,
  `ruang_kelas` varchar(30) NOT NULL,
  `jml_siswa` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_kelas`
--

INSERT INTO `tbl_kelas` (`id_kelas`, `ruang_kelas`, `jml_siswa`) VALUES
(1, 'ruang15', 15),
(3, 'ruang10', 10);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_ortu`
--

CREATE TABLE `tbl_ortu` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `nis` varchar(12) NOT NULL,
  `nama_ortu` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_ortu`
--

INSERT INTO `tbl_ortu` (`username`, `password`, `nis`, `nama_ortu`) VALUES
('sofii', 'pbkdf2:sha256:150000$P4RBUQFF$0b2ef4d62088e26c5f68', '876543222', 'sofii');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_siswa`
--

CREATE TABLE `tbl_siswa` (
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
-- Dumping data for table `tbl_siswa`
--

INSERT INTO `tbl_siswa` (`nis`, `nama_siswa`, `id_kelas`, `lokasi_terakhir`, `data_wajah`, `jam_masuk`, `jam_keluar`, `username`, `password`) VALUES
('876543215', 'coba1', 1, 'img1.jpg', 'img2.jpg', '2020-02-18 07:17:12', '2020-02-18 07:17:13', 'coba2', 'pbkdf2:sha256:150000$kw5fZksH$cea9bd08116b83a5bda5'),
('876543222', 'coba3', 3, 'img3.jpg', 'img3.jpg', '2020-02-18 07:17:12', '2020-02-18 07:17:13', 'coba3', 'pbkdf2:sha256:150000$4exCd0KC$8e904792191355d254f9');

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
  ADD PRIMARY KEY (`nis`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_kelas`
--
ALTER TABLE `tbl_kelas`
  MODIFY `id_kelas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
