-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Apr 03, 2018 at 05:27 AM
-- Server version: 10.1.19-MariaDB
-- PHP Version: 5.6.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bill`
--

-- --------------------------------------------------------

--
-- Table structure for table `billingdata`
--

CREATE TABLE `billingdata` (
  `reference` int(11) DEFAULT NULL,
  `fries` int(11) NOT NULL,
  `noodles` int(11) NOT NULL,
  `soup` int(11) NOT NULL,
  `burger` int(11) NOT NULL,
  `sandwich` int(11) NOT NULL,
  `drinks` int(11) NOT NULL,
  `cost` int(11) NOT NULL,
  `service` int(11) NOT NULL,
  `statetax` int(11) NOT NULL,
  `subtotal` int(11) NOT NULL,
  `totalcost` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `menu`
--

CREATE TABLE `menu` (
  `id` int(11) NOT NULL,
  `item` varchar(100) NOT NULL,
  `cost` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `menu`
--

INSERT INTO `menu` (`id`, `item`, `cost`) VALUES
(1, 'Chicken Biryani', 250),
(2, 'Chicken Tikka', 230);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `billingdata`
--
ALTER TABLE `billingdata`
  ADD UNIQUE KEY `reference` (`reference`);

--
-- Indexes for table `menu`
--
ALTER TABLE `menu`
  ADD UNIQUE KEY `id` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
