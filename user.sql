-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 11, 2025 at 02:20 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `user`
--

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `id` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `date_of_birth` date NOT NULL,
  `Address` varchar(100) NOT NULL,
  `state` varchar(50) NOT NULL,
  `country` varchar(50) NOT NULL,
  `aadhar_no` varchar(100) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `resume` varchar(100) NOT NULL,
  `profile_image` varchar(500) NOT NULL,
  `fun_video` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`id`, `first_name`, `last_name`, `date_of_birth`, `Address`, `state`, `country`, `aadhar_no`, `email`, `password`, `resume`, `profile_image`, `fun_video`) VALUES
(1, 'Prince', 'Kumar', '2000-02-21', 'Vidya Nagar Near SBI Bank Neelmatha', 'UP', 'IN', '12345678910', 'liltorch011@gmail.com', '', 'collegeid_1.jpg', '20250410172611_collegeid.jpg', 'gif1.mp4'),
(3, 'pallavi', 'pallav', '2000-03-21', 'kalibagh', 'MH', 'US', '323242323423', '121@c.com', 'a@Adadadaa123', 'collegeid.jpg', '20250410124440_collegeid.jpg', ''),
(4, 'Prince', 'Kumar', '2000-01-01', 'ayodhya', 'UP', 'IN', '232342423423', 'princekumar9764@gmail.com', 'A@1234asddf', 'python_assignment_1.pdf', '20250409182206_Nitro_Wallpaper_01_3840x2400.jpg', 'gif1.mp4'),
(8, 'ram', 'shyam', '2002-02-01', 'g', 'GJ', 'IN', '788868558868', 'a@a.com', 'F@gfhhsgfk34223', 'python_assignment_1.pdf', 'snehasign2.jpg', ''),
(9, 'ramesh', 'yadav', '2001-07-03', 'transport nagar', 'UP', 'IN', '232342423423', 'r123@gmail.com', 'A@123weffffw', 'GATE-_DA_2025_Syllabus.pdf', 'butterflies.webp', ''),
(10, 'vineet', 'yadav', '2003-12-09', 'topkhana', 'UP', 'IN', '213423444522', 'a@gmail.com', 'A@123weddfds', '2025030146.pdf', 'butterflies.webp', 'gif1.mp4'),
(12, 'p', 'k', '2002-12-04', 'w', 'AP', 'IN', '12313132334', 'd@d.com', 'D@123ert', 'ConfirmationPage-253510558295.pdf', 'collegeid.jpg', ''),
(13, 'sprite', 'cola', '2003-07-08', 'usa', 'MH', 'UK', '387234837384', 'usa@g.com', '$2b$12$ALD5hjdmYsMG9e8YTrBCPuGqnfYQGQjXXs8pA.YJQ9BAjRCQDGENm', 'python_assignment_1.pdf', 'Nitro_Wallpaper_03_3840x2400_-_Copy.jpg', ''),
(14, 'cola', 'sprite', '2002-02-21', 'lime', 'WB', 'US', '342342323423', 'cola@g.com', '$2b$12$1qi7y7cI.n8EQ6UxBFiKnO5WMBrpQID/sXXIopTvVLBqKsmNmfkVC', 'template.pdf', 'Nitro_Wallpaper_03_3840x2400.jpg', ''),
(15, 'sprite', 'pepsi', '2001-02-09', 'inomia', 'AP', 'US', '234234324433', 's@s.com', '$2b$12$78yw14ap.Yg9IDxR8nypyOCLL/cbKb0H69op8uWAfMQ9JmRSqqwpS', 'template.pdf', 'Nitro_Wallpaper_03_3840x2400_-_Copy.jpg', ''),
(17, 'fh', 'dfgd', '2002-02-03', 'ghf', 'UP', 'IN', '546466454544', 'a@d.com', '$2b$12$0cmXii.Rn4VZAf9NEXcCoOVcGDZW86El0S7kTsTy3C5jEw8BKIrc6', 'Document.pdf', 'collegeid.jpg', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
