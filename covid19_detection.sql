-- phpMyAdmin SQL Dump
-- version 4.8.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 08, 2021 at 05:27 PM
-- Server version: 10.1.32-MariaDB
-- PHP Version: 7.2.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `covid19_detection`
--

-- --------------------------------------------------------

--
-- Table structure for table `doctors_data`
--

CREATE TABLE `doctors_data` (
  `Id` int(11) NOT NULL,
  `User_Id` int(100) NOT NULL,
  `Patient_Name` varchar(30) NOT NULL,
  `Prediction_Status` varchar(20) NOT NULL,
  `Img_Name` varchar(100) NOT NULL,
  `Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `doctors_data`
--

INSERT INTO `doctors_data` (`Id`, `User_Id`, `Patient_Name`, `Prediction_Status`, `Img_Name`, `Date`) VALUES
(1, 2, 'Ajit kumar dev', 'Covid-19 Positive', '1d435a4b.jpg', '2021-04-08'),
(2, 2, 'Ramesh jadhav', 'Covid-19 Positive', '1.CXRCTThoraximagesofCOVID-19fromSingapore.pdf-002-fig3b.png', '2021-04-08'),
(3, 2, 'Devkumar jain', 'Covid-19 Positive', '1.CXRCTThoraximagesofCOVID-19fromSingapore.pdf-000-fig1b.png', '2021-04-08'),
(4, 2, 'suresh varma', 'Covid-19 Positive', '1-s2.0-S1684118220300608-main.pdf-002.jpg', '2021-04-08'),
(5, 2, 'ayush singh', 'Normal', 'IM-0183-0001.jpeg', '2021-04-08'),
(6, 2, 'Rohini varma', 'Normal', 'IM-0135-0001_1.jpeg', '2021-04-08');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `Id` int(11) NOT NULL,
  `First_Name` varchar(15) NOT NULL,
  `Last_Name` varchar(15) NOT NULL,
  `Email_Id` varchar(30) NOT NULL,
  `Password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`Id`, `First_Name`, `Last_Name`, `Email_Id`, `Password`) VALUES
(2, 'Aniket ', 'Kankute', 'aniketkankute@gmail.com', '$2b$12$XTVyS9wX83cdcyKUFMBy.u7Mi95RKXCQa7Azbobi29hG7ixy.1B/2');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `doctors_data`
--
ALTER TABLE `doctors_data`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`Id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `doctors_data`
--
ALTER TABLE `doctors_data`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
