-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 24, 2021 at 05:34 AM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 7.3.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `apollohospital`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(3) NOT NULL,
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`) VALUES
(1, 'devesh', 'b\'RGV2ZXNo\'');

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `id` int(4) NOT NULL,
  `name` varchar(45) NOT NULL,
  `department` varchar(45) NOT NULL,
  `mobile` bigint(10) NOT NULL,
  `status` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`id`, `name`, `department`, `mobile`, `status`) VALUES
(1, 'Karan', 'Orthopaedics', 9874561548, 'permanent'),
(2, 'Arjun', 'surgen', 9147483647, 'permanent'),
(4, 'Karan', 'Cardiology', 7486980186, 'permanent'),
(5, 'Devesh', 'Cardiology', 9876541548, 'permanent'),
(7, 'Naman', 'Neurology', 8497561236, 'pending'),
(8, 'Kunal', 'ENT', 9635412875, 'permanent'),
(9, 'Dhruv', 'ENT', 6598743265, 'pending'),
(10, 'Chirag', 'dental', 9876598742, 'pending');

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `idpatient` int(11) NOT NULL,
  `Name` varchar(45) NOT NULL,
  `Symptoms` varchar(45) NOT NULL,
  `Mobile` bigint(10) NOT NULL,
  `Status` varchar(45) NOT NULL,
  `Admiting` datetime NOT NULL,
  `Address` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`idpatient`, `Name`, `Symptoms`, `Mobile`, `Status`, `Admiting`, `Address`) VALUES
(1, 'Shubham', 'cough', 7486980186, 'hold', '2021-11-06 00:00:00', 'Railway colony'),
(2, 'Karan', 'Fatigue', 9874563214, 'admitted', '2021-11-06 00:00:00', '12/s dfsf'),
(3, 'Ajay', 'fever', 9635874125, 'hold', '2021-11-06 00:00:00', ''),
(4, 'Ashok', 'indigestion', 9816254962, 'hold', '2021-11-06 00:00:00', 'nana sak market.'),
(5, 'Bishal', 'Dengue', 9456321875, 'admitted', '2021-11-07 00:00:00', 'Haripura sardar society');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`idpatient`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `doctor`
--
ALTER TABLE `doctor`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `patient`
--
ALTER TABLE `patient`
  MODIFY `idpatient` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
