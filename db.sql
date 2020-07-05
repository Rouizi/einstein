-- MySQL dump 10.13  Distrib 8.0.20, for Linux (x86_64)
--
-- Host: localhost    Database: einstein
-- ------------------------------------------------------
-- Server version	8.0.20-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `core_exercise`
--

DROP TABLE IF EXISTS `core_exercise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_exercise` (
  `id` int NOT NULL AUTO_INCREMENT,
  `link` varchar(200) NOT NULL,
  `wihda_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_exercise_wihda_id_d84681e7_fk_core_wihda_id` (`wihda_id`),
  CONSTRAINT `core_exercise_wihda_id_d84681e7_fk_core_wihda_id` FOREIGN KEY (`wihda_id`) REFERENCES `core_wihda` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_exercise`
--

LOCK TABLES `core_exercise` WRITE;
/*!40000 ALTER TABLE `core_exercise` DISABLE KEYS */;
INSERT INTO `core_exercise` VALUES (1,'https://drive.google.com/file/d/1i-UurVUCqIvSDjBn_8ME1yGm1TpVnChX/view?usp=sharing',3),(4,'https://drive.google.com/file/d/1GW-xKPLIb8RkJ72OEu8Yurd9TvmI11Q9/view?usp=sharing',3),(5,'https://drive.google.com/file/d/1gqYvIcZcp2fVTCtWm-88-dnmjjfIt_zU/view?usp=sharing',3);
/*!40000 ALTER TABLE `core_exercise` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-07-05 13:18:45
