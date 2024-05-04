-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 04, 2024 at 09:03 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hospitaldb`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminlog`
--

CREATE TABLE `adminlog` (
  `ID` int(20) NOT NULL,
  `Username` varchar(30) NOT NULL,
  `Password` varchar(30) NOT NULL,
  `U_type` varchar(30) NOT NULL,
  `U_status` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `adminlog`
--

INSERT INTO `adminlog` (`ID`, `Username`, `Password`, `U_type`, `U_status`) VALUES
(1, 'admin', 'admin', 'admin', 1),
(2, 'headdoc', 'headdoc', 'medicalofficer', 0),
(3, 'headnur', 'headnur', 'nursingofficer', 0),
(4, 'rec', 'rec', 'receptionist', 0),
(13, 'kar123', 'kar123', 'receptionist', 0);

-- --------------------------------------------------------

--
-- Table structure for table `dep`
--

CREATE TABLE `dep` (
  `ID` int(20) NOT NULL,
  `Department_ID` varchar(30) NOT NULL,
  `Department_Name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dep`
--

INSERT INTO `dep` (`ID`, `Department_ID`, `Department_Name`) VALUES
(1, 'd1', 'Doctor'),
(8, 'd2', 'Cleaning'),
(9, 'd3', 'Reception'),
(10, 'd4', 'Pharmacy');

-- --------------------------------------------------------

--
-- Table structure for table `doc`
--

CREATE TABLE `doc` (
  `ID` int(20) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Doctor_ID` varchar(30) NOT NULL,
  `Department` varchar(30) NOT NULL,
  `Qualification` varchar(30) NOT NULL,
  `Experience` varchar(30) NOT NULL,
  `Contact` varchar(30) NOT NULL,
  `Photo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `doc`
--

INSERT INTO `doc` (`ID`, `Name`, `Doctor_ID`, `Department`, `Qualification`, `Experience`, `Contact`, `Photo`) VALUES
(1, 'Megha', 'meg1', 'Pediatrics', 'MBBS', '3', '9747633602', '1703168692077.jpg'),
(2, 'Karthik', 'kar123', 'Ophthalmology', 'MD', '5', '9847257320', '1703168692072.jpg'),
(3, 'Sreelakshmi', 'sree123', 'Gynaecology', 'MS', '8', '9739904227', 'maxresdefault.jpg'),
(4, 'Sneha', 'sne123', 'Gynaecology', 'None', '8', '9747633602', 'b.jpg.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `headdoc`
--

CREATE TABLE `headdoc` (
  `ID` int(20) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Username` varchar(30) NOT NULL,
  `Password` varchar(30) NOT NULL,
  `Qualification` varchar(30) NOT NULL,
  `Experience` varchar(30) NOT NULL,
  `Contact` varchar(30) NOT NULL,
  `Photo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `headdoc`
--

INSERT INTO `headdoc` (`ID`, `Name`, `Username`, `Password`, `Qualification`, `Experience`, `Contact`, `Photo`) VALUES
(1, 'Megha', 'headdoc', 'headdoc', 'General', '9', '9747633602', '1703168692077.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `headnur`
--

CREATE TABLE `headnur` (
  `ID` int(20) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Username` varchar(30) NOT NULL,
  `Password` varchar(30) NOT NULL,
  `Qualification` varchar(30) NOT NULL,
  `Experience` varchar(30) NOT NULL,
  `Contact` varchar(30) NOT NULL,
  `Photo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `headnur`
--

INSERT INTO `headnur` (`ID`, `Name`, `Username`, `Password`, `Qualification`, `Experience`, `Contact`, `Photo`) VALUES
(1, 'Megha', 'headnur', 'headnur', 'General', '6', '9747633602', '1703168692072.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `pat`
--

CREATE TABLE `pat` (
  `ID` int(20) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `OP_number` varchar(30) NOT NULL,
  `Date` varchar(30) NOT NULL,
  `Doctor` varchar(30) NOT NULL,
  `Department` varchar(30) NOT NULL,
  `Address` varchar(30) NOT NULL,
  `Contact` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pat`
--

INSERT INTO `pat` (`ID`, `Name`, `OP_number`, `Date`, `Doctor`, `Department`, `Address`, `Contact`) VALUES
(1, 'Megha', '1', '01/26/2024', 'Megha', 'Pediatrics', 'Varkala', '9747633603'),
(2, 'Karthik', '2', '01/27/2024', 'Megha', 'Pediatrics', 'Varkala', '9747636302'),
(4, 'Simmy', '3', '2024-01-28', 'Karthik', 'Opthalmology', 'Varkala', '9747633602'),
(10, 'Sneha', '4', '2024-01-28', 'Sreelakshmi', 'Gynaecology', 'Trivandrum', '9747633602'),
(29, 'Sreelakshmi', '333540', '2024-01-28', 'Megha', 'Pediatrics', 'Varkala', '9747633602'),
(30, 'Manu', '907861', '2024-01-28', 'Karthik', 'Opthalmology', 'Varkala', '9747633602'),
(31, 'Megha', '535663', '2024-01-28', 'Sreelakshmi', 'Gynaecology', 'Varkala', '9747633602'),
(32, 'Megha', '770630', '2024-01-30', 'Karthik', 'Opthalmology', 'Varkala', '9747633602');

-- --------------------------------------------------------

--
-- Table structure for table `rec`
--

CREATE TABLE `rec` (
  `ID` int(20) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Staff_ID` varchar(30) NOT NULL,
  `Username` varchar(30) NOT NULL,
  `Password` varchar(30) NOT NULL,
  `Qualification` varchar(30) NOT NULL,
  `Experience` varchar(30) NOT NULL,
  `Contact` varchar(30) NOT NULL,
  `Photo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `rec`
--

INSERT INTO `rec` (`ID`, `Name`, `Staff_ID`, `Username`, `Password`, `Qualification`, `Experience`, `Contact`, `Photo`) VALUES
(1, 'Kayle', 'kay123', 'rec', 'rec', 'BA', '3', '9747633602', '1703168692072.jpg'),
(9, 'Karthik', '701345', 'kar123', 'kar123', 'BSc', '9', '9747633602', 'maxresdefault.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adminlog`
--
ALTER TABLE `adminlog`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `dep`
--
ALTER TABLE `dep`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `doc`
--
ALTER TABLE `doc`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `headdoc`
--
ALTER TABLE `headdoc`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `headnur`
--
ALTER TABLE `headnur`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `pat`
--
ALTER TABLE `pat`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `rec`
--
ALTER TABLE `rec`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `adminlog`
--
ALTER TABLE `adminlog`
  MODIFY `ID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `dep`
--
ALTER TABLE `dep`
  MODIFY `ID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `doc`
--
ALTER TABLE `doc`
  MODIFY `ID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `headdoc`
--
ALTER TABLE `headdoc`
  MODIFY `ID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `headnur`
--
ALTER TABLE `headnur`
  MODIFY `ID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `pat`
--
ALTER TABLE `pat`
  MODIFY `ID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `rec`
--
ALTER TABLE `rec`
  MODIFY `ID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
