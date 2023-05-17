-- MySQL dump 10.18  Distrib 10.3.27-MariaDB, for debian-linux-gnueabihf (armv8l)
--
-- Host: localhost    Database: lotto_db
-- ------------------------------------------------------
-- Server version	10.3.27-MariaDB-0+deb10u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin_table`
--

DROP TABLE IF EXISTS `admin_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_table` (
  `id` int(11) NOT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_table`
--

LOCK TABLES `admin_table` WRITE;
/*!40000 ALTER TABLE `admin_table` DISABLE KEYS */;
/*!40000 ALTER TABLE `admin_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lotto_info`
--

DROP TABLE IF EXISTS `lotto_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lotto_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lotto_date` date DEFAULT NULL,
  `slot_1130` int(11) DEFAULT 0,
  `slot_1230` int(11) DEFAULT 0,
  `slot_1330` int(11) DEFAULT 0,
  `slot_1530` int(11) DEFAULT 0,
  `slot_1830` int(11) DEFAULT 0,
  `slot_1930` int(11) DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lotto_info`
--

LOCK TABLES `lotto_info` WRITE;
/*!40000 ALTER TABLE `lotto_info` DISABLE KEYS */;
INSERT INTO `lotto_info` VALUES (2,'2021-06-11',9842,3302,7601,3302,8891,8891),(4,'2021-06-13',7601,9842,8383,8012,3302,7601),(5,'2021-05-13',3302,3921,7601,8362,7782,7782),(7,'2021-05-12',8012,3921,8012,9842,7782,3302),(8,'2021-05-11',3921,9842,3921,8362,3921,8362),(9,'2021-05-10',8012,3921,2839,9842,7601,3302),(10,'2021-06-01',7601,7782,7782,9842,3921,8362),(11,'2021-06-02',3921,7782,9027,8891,9842,7601),(12,'2021-06-03',8012,8012,3302,3302,7601,8362),(13,'2021-06-05',3921,8891,3302,3302,9842,8362),(14,'2021-06-07',1234,1234,1234,1234,1234,1234);
/*!40000 ALTER TABLE `lotto_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lotto_slots`
--

DROP TABLE IF EXISTS `lotto_slots`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lotto_slots` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lotto_timing` time DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `lotto_timing_UNIQUE` (`lotto_timing`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lotto_slots`
--

LOCK TABLES `lotto_slots` WRITE;
/*!40000 ALTER TABLE `lotto_slots` DISABLE KEYS */;
INSERT INTO `lotto_slots` VALUES (1,'11:30:00'),(2,'12:30:00'),(3,'13:30:00'),(4,'15:30:00'),(5,'18:30:00'),(6,'19:30:00');
/*!40000 ALTER TABLE `lotto_slots` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-17  5:08:49
