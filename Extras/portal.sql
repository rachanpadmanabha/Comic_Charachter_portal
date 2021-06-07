-- MySQL dump 10.13  Distrib 5.7.32, for Linux (x86_64)
--
-- Host: localhost    Database: portal
-- ------------------------------------------------------
-- Server version	5.7.32-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ALLIANCE`
--

DROP TABLE IF EXISTS `ALLIANCE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ALLIANCE` (
  `Team_id` int(10) NOT NULL,
  `Name` varchar(30) DEFAULT NULL,
  `Created` varchar(25) DEFAULT NULL,
  `No_Of_Characters` int(3) DEFAULT NULL,
  PRIMARY KEY (`Team_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ALLIANCE`
--

LOCK TABLES `ALLIANCE` WRITE;
/*!40000 ALTER TABLE `ALLIANCE` DISABLE KEYS */;
INSERT INTO `ALLIANCE` VALUES (101,'Batman','JUSTICE LEAGUE',7),(102,'Lex Luthor','LEGION OF DOOM',7),(103,'Robin','TEEN TITANS',8),(104,'Psimon','FEARSOME FIVE',5),(105,'Deadshot','SUICIDE SQUAD',6),(106,'Captain America','AVENGERS',6),(107,'Thanos','BLACK ORDER',6),(108,'Spider-Man','DEFENDERS',5),(109,'Venom','CARNAGE FAMILY',5),(110,'Hyomei Himejima','THE PILLARS',9),(111,'Kokushibo','UPPER MOON',6),(112,'Genryusai Yamamoto','GOTEI 13',13),(113,'Coyote Stark','ESPADA',10),(114,'Kaido','YONKO',5),(115,'Sengoku','NAVY ADMIRALS',5),(116,'Jahad','JAHADS ARMY',7),(117,'Grace Luslec','FUG SLAYERS',7);
/*!40000 ALTER TABLE `ALLIANCE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ANTAGONIST`
--

DROP TABLE IF EXISTS `ANTAGONIST`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ANTAGONIST` (
  `Antagonist_id` int(10) NOT NULL,
  `Publisher_id` int(10) DEFAULT NULL,
  `Team_id` int(10) DEFAULT NULL,
  `Protagonist_id` int(10) DEFAULT NULL,
  `Name` varchar(30) DEFAULT NULL,
  `Alias` varchar(30) DEFAULT NULL,
  `Appearance` int(5) DEFAULT NULL,
  PRIMARY KEY (`Antagonist_id`),
  KEY `Publisher_id` (`Publisher_id`),
  KEY `Team_id` (`Team_id`),
  KEY `Protagonist_id` (`Protagonist_id`),
  CONSTRAINT `ANTAGONIST_ibfk_1` FOREIGN KEY (`Publisher_id`) REFERENCES `PUBLISHER` (`Publisher_id`) ON DELETE CASCADE,
  CONSTRAINT `ANTAGONIST_ibfk_2` FOREIGN KEY (`Team_id`) REFERENCES `ALLIANCE` (`Team_id`) ON DELETE CASCADE,
  CONSTRAINT `ANTAGONIST_ibfk_3` FOREIGN KEY (`Protagonist_id`) REFERENCES `PROTAGONIST` (`Protagonist_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ANTAGONIST`
--

LOCK TABLES `ANTAGONIST` WRITE;
/*!40000 ALTER TABLE `ANTAGONIST` DISABLE KEYS */;
INSERT INTO `ANTAGONIST` VALUES (2001,1,102,1001,'Melvin Lipshitz','Bane',1993),(2002,1,102,1002,'Barbara Minerva','Cheetah',1943),(2003,1,102,1003,'Alexander Luthor','Lex Luthor',1940),(2004,1,102,1004,'Thaal Sinestro','Sinestro',1961),(2005,1,102,1005,'Leonard Snart','Captain Cold',1957),(2006,1,102,1006,'David Hyde','Black Manta',1967),(2007,1,102,1007,'maalefaak jonnz','Maalefaak',1998),(2008,1,104,1008,'Simon Jones','Psimon',1981),(2009,1,104,1012,'Jinx','Jinx',1985),(2010,1,104,1010,'Baron Flinders','Mammoth',1981),(2011,1,104,1011,'Mikron Jeneus','Gizmo',1981),(2012,1,104,1009,'Selinda Flinder','Shimmer',1981),(2013,2,107,1023,'Thanos','Thanos',1973),(2014,2,107,1024,'Ebony Maw','Ebony Maw',2013),(2015,2,107,1025,'Black Dwarf','Black Dwarf',2013),(2016,2,107,1026,'Proxima Midnight','Proxima Midnight',2013),(2017,2,107,1027,'Corvus Glaive','Corvus Glaive',2013),(2018,2,107,1022,'Super Giant','Super Giant',2013),(2019,2,109,1028,'Eddie Brock','Venom',1984),(2020,2,109,1028,'Ben Riley','Carnage',1992),(2021,2,109,1028,'Patrick Mulligan','Toxin',2004),(2022,2,109,1028,'Donna Diego','Scream',1993),(2023,2,109,1028,'Lee Price','Mania',2003),(2024,3,111,1033,'Kokushibo','Upper Moon 1',2016),(2025,3,111,1035,'Doma','Upper Moon 2',2016),(2026,3,111,1034,'Akaza','Upper Moon 3',2016),(2027,3,111,1041,'Hantengu','Upper Moon 4',2016),(2028,3,111,1036,'Gyokko','Upper Moon 5',2016),(2029,3,111,1037,'Kaigaku','Upper Moon 6',2016),(2030,3,113,1049,'Coyote Stark','Espada #1',2004),(2031,3,113,1043,'Barragan Lousiebar','Espada #2',2004),(2032,3,113,1051,'Tier Harribiel','Espada #3',2004),(2033,3,113,1054,'Ulquoirra Cifer','Espada #4',2004),(2034,3,113,1052,'Nnoitara Gilga','Espada #5',2004),(2035,3,113,1051,'Luppiantenou','Espada #6',2004),(2036,3,113,1050,'Grimmjaw','Espada #7',2004),(2037,3,113,1053,'Zzummarirrureax','Espada #8',2004),(2038,3,113,1046,'Szaleyaporo Granz','Espada #9',2004),(2039,3,113,1048,'Aaroniero','Espada #10',2004),(2040,3,115,1067,'Sengoku','Fleet Admiral',1999),(2041,3,115,1067,'Akainu','Admiral 1',1999),(2042,3,115,1067,'Kizaru','Admiral 2',1999),(2043,3,115,1067,'Aokiji','Admiral 3',1999),(2044,3,115,1067,'Monkey D Garp','Vice Admiral',1999),(2045,4,117,1066,'Jahad','King Jahad',2010),(2046,4,117,1063,'Po Bidau Lyborick Khun','Commander 3',2010),(2047,4,117,1061,'Lo Po Bia Yastrach','Commander 4',2010),(2048,4,117,1065,'Kallavan','Commander 5',2010),(2049,4,117,1067,'Elpathion','Vice Sqd Commander 4',2010),(2050,4,117,1067,'Mc Cage','Vice Sqd Commander 5',2010),(2051,4,117,1065,'Khun Mascheny Jahad','Staff Officer',2010),(2052,4,101,1067,'NULL','NULL',9999);
/*!40000 ALTER TABLE `ANTAGONIST` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PROTAGONIST`
--

DROP TABLE IF EXISTS `PROTAGONIST`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PROTAGONIST` (
  `Protagonist_id` int(10) NOT NULL,
  `Publisher_id` int(10) DEFAULT NULL,
  `Team_id` int(10) DEFAULT NULL,
  `Name` varchar(30) DEFAULT NULL,
  `Alias` varchar(30) DEFAULT NULL,
  `Appearance` int(5) DEFAULT NULL,
  `Creator` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`Protagonist_id`),
  KEY `Publisher_id` (`Publisher_id`),
  KEY `Team_id` (`Team_id`),
  CONSTRAINT `PROTAGONIST_ibfk_1` FOREIGN KEY (`Publisher_id`) REFERENCES `PUBLISHER` (`Publisher_id`) ON DELETE CASCADE,
  CONSTRAINT `PROTAGONIST_ibfk_2` FOREIGN KEY (`Team_id`) REFERENCES `ALLIANCE` (`Team_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PROTAGONIST`
--

LOCK TABLES `PROTAGONIST` WRITE;
/*!40000 ALTER TABLE `PROTAGONIST` DISABLE KEYS */;
INSERT INTO `PROTAGONIST` VALUES (1001,1,101,'Bruce Wayne','Batman',1939,'Bob Kane'),(1002,1,101,'Diana Prince','Wonder Woman',1941,'William Marston'),(1003,1,101,'Clark Kent','Superman',1938,'Jerry Siegel'),(1004,1,101,'Hal Jordan','Green Lantern',1959,'John Broome'),(1005,1,101,'Barry Allen','Flash',1940,'Gardner Fox'),(1006,1,101,'Arthur Curry','Aquaman',1941,'Mort Weisinger'),(1007,1,101,'Jon Jones','Martian Manhunter',1955,'Joseph Samachson'),(1008,1,103,'Damian Wayne','Robin',1987,'Andy Kubert'),(1009,1,103,'Rachel Roth','Raven',1980,'George Perez'),(1010,1,103,'Changeling','Beast Boy',1965,'Arnold Drake'),(1011,1,103,'Dan Garnet','Blue Beetle',1939,'Charles Nicholas'),(1012,1,103,'Victor Stone','Cyborg',1980,'Marv Wolfman'),(1013,1,103,'Wally West','Kid Flash',1959,'John Broome'),(1014,1,103,'Connor Kent','Superboy',1993,'Karl Kessel'),(1015,1,103,'Kory Anders','Starfire',1980,'Marv Wolfman'),(1016,1,105,'Floyd Lawton','Deadshot',1950,'Bob Kane'),(1017,1,105,'Harleen Quinzel','Harley Quinn',1993,'Paul Dini'),(1018,1,105,'Chato Santana','El Diablo',1970,'Ande parks'),(1019,1,105,'George Harkness','Captain Boomerang',1960,'John Broome'),(1020,1,105,'Tatsu Yamasiro','Katana',1983,'Jim Aparo'),(1021,1,105,'Waylon Jones','Killer Croc',1983,'Gerry Conway'),(1022,2,106,'Steve Rogers','Captain America',1941,'Joe Simon'),(1023,2,106,'Anthoy Stark','Iron Man',1963,'Stan Lee'),(1024,2,106,'Bruce Banner','Hulk',1962,'Stan Lee'),(1025,2,106,'Natasha Romanoff','Black Widow',1964,'Stan Lee'),(1026,2,106,'Clint Barton','Hawk Eye',1964,'Stan Lee'),(1027,2,106,'Thor Odinson','Thor',1962,'Stan Lee'),(1028,2,108,'Peter Parker','Spider-Man',1962,'Stan Lee'),(1029,2,108,'Victor Alvarez','Powerman',2010,'Mahmud Asarar'),(1030,2,108,'Danny Rand','Iron Fist',1974,'Ray Thomas'),(1031,2,108,'Greer Grant Nelson','Tigeress',1972,'Stan Lee'),(1032,2,108,'Richard Rider','Nova',1976,'Marv Wolfman'),(1033,3,110,'Hyomei Himejima','Rock Pillar',2016,'Koyoharu Gotoge'),(1034,3,110,'Giyuu Tomioka','Water Pillar',2016,'Koyoharu Gotoge'),(1035,3,110,'Shinobu Kocho','Insect Pillar',2016,'Koyoharu Gotoge'),(1036,3,110,'Mitsuri Kanroji','Love Pillar',2016,'Koyoharu Gotoge'),(1037,3,110,'Tengen Uzui','Sound Pillar',2016,'Koyoharu Gotoge'),(1038,3,110,'Obanai Iguro','Snake Pillar',2016,'Koyoharu Gotoge'),(1039,3,110,'Kyojuro Rengoku','Flame Pillar',2016,'Koyoharu Gotoge'),(1040,3,110,'Sanemi Shinaguzawa','Wind Pillar',2016,'Koyoharu Gotoge'),(1041,3,110,'Muichiro Tokita','Mist Pillar',2016,'Koyoharu Gotoge'),(1042,3,112,'Genryusai Yamamoto','General Commander',2001,'Tite Kubo'),(1043,3,112,'Sui Feng','Second Division Captain',2001,'Tite Kubo'),(1044,3,112,'Rojuro Otoribashi','Third Division Captain',2001,'Tite Kubo'),(1045,3,112,'Retsu Unohana','Fourth Division Captain',2001,'Tite Kubo'),(1046,3,112,'Shinji Hirako','Fifth Division Captain',2001,'Tite Kubo'),(1047,3,112,'Byakuya Kuchiki','Sixth Division Captain',2001,'Tite Kubo'),(1048,3,112,'Sajin Komamura','Seventh Division Captain',2001,'Tite Kubo'),(1049,3,112,'Shunsui Kyoraku','8th Division Captain',2001,'Tite Kubo'),(1050,3,112,'Kensei Muguruma','9th Division Captain',2001,'Tite Kubo'),(1051,3,112,'Toshiro Hitsugaya','10th Division Captain',2001,'Tite Kubo'),(1052,3,112,'Kenpachi Zaraki','11th Division Captain',2001,'Tite Kubo'),(1053,3,112,'Mayuri Kurotsuchi','12th Division Captain',2001,'Tite Kubo'),(1054,3,112,'Rukia Kuchiki','13th Division Captain',2001,'Tite Kubo'),(1055,3,114,'Kaido','Kaido',1999,'Oda Ichiro'),(1056,3,114,'Monkey D Luffy','Straw Hat',1999,'Oda Ichiro'),(1057,3,114,'Shanks','Red Haired',1999,'Oda Ichiro'),(1058,3,114,'Charlotte Linlin','Big Mom',1999,'Oda Ichiro'),(1059,3,114,'Marshal D Teach','Black Beard',1999,'Oda Ichiro'),(1060,4,117,'Grace Luslec','Slayer Commander',2010,'SIU'),(1061,4,117,'Baylord Yama','Slayer 7',2010,'SIU'),(1062,4,117,'White','Slayer 10',2010,'SIU'),(1063,4,117,'Karaka','Slayer 11',2010,'SIU'),(1064,4,117,'Khel Hellan','Slayer Elder',2010,'SIU'),(1065,4,117,'Jinsung Ha','Slayer Executive',2010,'SIU'),(1066,4,117,'Jue Viole Grace','Slayer Candidate',2010,'SIU'),(1067,4,101,'NULL','NULL',9999,'NULL');
/*!40000 ALTER TABLE `PROTAGONIST` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PUBLISHER`
--

DROP TABLE IF EXISTS `PUBLISHER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PUBLISHER` (
  `Publisher_id` int(10) NOT NULL,
  `Publisher_name` varchar(25) DEFAULT NULL,
  `Established` date DEFAULT NULL,
  `Country` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`Publisher_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PUBLISHER`
--

LOCK TABLES `PUBLISHER` WRITE;
/*!40000 ALTER TABLE `PUBLISHER` DISABLE KEYS */;
INSERT INTO `PUBLISHER` VALUES (1,'DC COMICS','1939-01-01','USA'),(2,'MARVEL','1945-01-01','USA'),(3,'SHUEISHA','1949-03-31','JPN'),(4,'WEBTOON','2003-01-01','KOR');
/*!40000 ALTER TABLE `PUBLISHER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `STATS`
--

DROP TABLE IF EXISTS `STATS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `STATS` (
  `Protagonist_id` int(10) DEFAULT NULL,
  `Antagonist_id` int(10) DEFAULT NULL,
  `Intelligence` int(3) DEFAULT NULL,
  `Strength` int(3) DEFAULT NULL,
  `Speed` int(3) DEFAULT NULL,
  `Durability` int(3) DEFAULT NULL,
  `Power` int(3) DEFAULT NULL,
  `Combat` int(3) DEFAULT NULL,
  `Tier` int(3) DEFAULT NULL,
  KEY `Protagonist_id` (`Protagonist_id`),
  KEY `Antagonist_id` (`Antagonist_id`),
  CONSTRAINT `STATS_ibfk_1` FOREIGN KEY (`Protagonist_id`) REFERENCES `PROTAGONIST` (`Protagonist_id`) ON DELETE CASCADE,
  CONSTRAINT `STATS_ibfk_2` FOREIGN KEY (`Antagonist_id`) REFERENCES `ANTAGONIST` (`Antagonist_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `STATS`
--

LOCK TABLES `STATS` WRITE;
/*!40000 ALTER TABLE `STATS` DISABLE KEYS */;
INSERT INTO `STATS` VALUES (1001,2052,90,13,20,12,25,100,1),(1002,2052,85,100,100,100,100,100,6),(1003,2052,95,100,100,100,100,95,6),(1004,2052,85,100,100,100,75,65,6),(1005,2052,55,70,100,85,95,70,6),(1006,2052,60,50,25,25,45,60,3),(1007,2052,85,100,100,100,100,75,6),(1008,2052,80,10,10,10,15,90,1),(1009,2052,80,25,25,60,85,60,6),(1010,2052,60,25,25,20,40,45,2),(1011,2052,75,30,85,75,70,30,5),(1012,2052,85,100,50,75,60,30,5),(1013,2052,75,25,100,55,85,70,6),(1014,2052,75,85,100,75,75,50,5),(1015,2052,65,45,55,60,70,75,4),(1016,2052,55,15,50,13,17,85,1),(1017,2052,85,5,7,13,15,75,1),(1018,2052,60,18,30,80,100,70,3),(1019,2052,60,1,19,12,15,65,1),(1020,2052,65,1,25,12,10,95,1),(1021,2052,45,25,20,18,25,40,1),(1022,2052,60,25,20,15,15,84,1),(1023,2052,90,75,35,50,80,60,4),(1024,2052,70,100,85,100,100,70,6),(1025,2052,75,5,8,12,12,95,1),(1026,2052,65,5,25,12,18,80,1),(1027,2052,80,100,100,100,100,90,6),(1028,2052,90,25,25,45,50,80,2),(1029,2052,80,75,45,90,60,85,2),(1030,2052,65,30,25,20,55,100,2),(1031,2052,61,14,10,12,60,70,1),(1032,2052,75,100,90,100,80,75,6),(1033,2052,60,100,70,87,81,89,2),(1034,2052,70,85,90,82,70,88,2),(1035,2052,90,62,65,61,74,82,2),(1036,2052,69,84,78,73,81,85,2),(1037,2052,85,91,95,92,99,82,2),(1038,2052,73,77,80,75,85,82,2),(1039,2052,79,80,85,65,80,79,2),(1040,2052,60,83,70,88,90,95,2),(1041,2052,82,70,71,76,60,90,2),(1042,2052,75,90,95,100,100,100,4),(1043,2052,89,70,98,70,78,85,3),(1044,2052,70,82,85,90,70,75,3),(1045,2052,80,85,75,90,90,90,3),(1046,2052,83,80,85,90,80,75,3),(1047,2052,88,78,80,60,86,85,3),(1048,2052,80,75,70,81,80,85,3),(1049,2052,95,90,92,100,90,100,3),(1050,2052,80,75,79,80,85,79,3),(1051,2052,80,70,85,83,70,77,3),(1052,2052,75,80,85,100,95,100,3),(1053,2052,95,80,70,90,75,95,3),(1054,2052,70,82,75,80,73,85,3),(1055,2052,60,100,95,100,100,100,5),(1056,2052,40,90,91,90,90,90,4),(1057,2052,82,78,87,95,100,100,5),(1058,2052,65,93,66,99,97,80,5),(1059,2052,88,90,79,83,94,100,5),(1060,2052,999,999,999,999,999,999,6),(1061,2052,86,91,80,85,96,92,5),(1062,2052,74,75,83,95,100,100,5),(1063,2052,89,76,79,90,97,95,4),(1064,2052,90,83,89,100,87,93,5),(1065,2052,92,100,100,100,100,100,5),(1066,2052,85,91,80,98,94,96,4),(1067,2001,85,25,35,20,20,95,1),(1067,2002,85,95,85,60,70,90,4),(1067,2005,90,13,25,10,15,40,1),(1067,2003,95,30,35,50,60,40,3),(1067,2004,70,100,100,90,80,7,5),(1067,2006,85,30,25,40,40,85,2),(1067,2007,85,100,100,100,90,85,5),(1067,2008,95,30,40,35,100,65,3),(1067,2009,90,12,60,50,100,55,3),(1067,2010,80,60,75,70,40,40,3),(1067,2011,100,35,70,75,50,40,3),(1067,2012,75,40,73,80,85,71,3),(1067,2013,100,100,100,100,100,85,7),(1067,2014,100,18,60,65,100,85,4),(1067,2015,65,100,65,100,65,95,4),(1067,2016,90,85,70,80,75,95,4),(1067,2018,90,50,80,80,100,85,4),(1067,2017,95,80,75,100,100,85,4),(1067,2019,65,30,25,25,40,70,2),(1067,2020,60,30,25,25,40,70,2),(1067,2021,90,80,40,85,95,70,2),(1067,2022,75,80,50,62,95,80,2),(1067,2023,60,25,25,20,40,70,2),(1067,2024,85,100,85,95,89,97,3),(1067,2025,90,85,76,93,86,90,3),(1067,2026,86,90,94,93,84,97,3),(1067,2027,69,45,85,75,74,63,3),(1067,2028,90,70,65,89,85,90,3),(1067,2029,75,84,100,65,85,90,3),(1067,2030,90,95,85,65,88,92,3),(1067,2031,80,65,62,100,85,95,3),(1067,2032,84,75,86,92,83,83,3),(1067,2033,95,86,89,82,94,97,3),(1067,2034,75,90,84,94,91,92,3),(1067,2035,10,65,74,65,70,50,2),(1067,2036,50,85,89,84,90,84,3),(1067,2037,60,75,79,74,70,74,3),(1067,2038,90,65,80,85,64,69,3),(1067,2039,40,85,55,95,94,95,3),(1067,2040,96,85,50,85,89,80,4),(1067,2041,86,90,60,91,86,90,4),(1067,2042,85,76,100,95,97,90,4),(1067,2043,90,85,85,94,94,90,4),(1067,2044,65,90,82,92,91,97,4),(1067,2046,92,81,67,81,75,80,3),(1067,2045,999,999,999,999,999,999,7),(1067,2047,85,91,75,76,85,84,3),(1067,2048,75,100,75,92,95,97,4),(1067,2049,74,78,65,84,73,84,2),(1067,2050,76,87,70,79,85,81,2),(1067,2051,89,90,84,83,94,92,4);
/*!40000 ALTER TABLE `STATS` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-07  7:02:47
