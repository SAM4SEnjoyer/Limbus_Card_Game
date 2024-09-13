-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: limbuscardproject
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `board`
--

DROP TABLE IF EXISTS `board`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `board` (
  `User_ID` int NOT NULL,
  `Board_ID` int NOT NULL AUTO_INCREMENT,
  `Hero_ID` int NOT NULL,
  PRIMARY KEY (`Board_ID`),
  KEY `Board_heroes_Hero_ID_fk` (`Hero_ID`),
  KEY `User_ID` (`User_ID`),
  CONSTRAINT `Board_heroes_Hero_ID_fk` FOREIGN KEY (`Hero_ID`) REFERENCES `heroes` (`Hero_ID`),
  CONSTRAINT `User_ID` FOREIGN KEY (`User_ID`) REFERENCES `users` (`User_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `board`
--

LOCK TABLES `board` WRITE;
/*!40000 ALTER TABLE `board` DISABLE KEYS */;
/*!40000 ALTER TABLE `board` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `card_in_deck`
--

DROP TABLE IF EXISTS `card_in_deck`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `card_in_deck` (
  `Card_ID` int NOT NULL,
  `Deck_ID` int NOT NULL,
  `card_in_deck_ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`card_in_deck_ID`),
  KEY `Card_ID` (`Card_ID`),
  KEY `Deck_ID` (`Deck_ID`),
  CONSTRAINT `Card_ID` FOREIGN KEY (`Card_ID`) REFERENCES `cards` (`Card_ID`),
  CONSTRAINT `Deck_ID` FOREIGN KEY (`Deck_ID`) REFERENCES `decks` (`Deck_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=401 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `card_in_deck`
--

LOCK TABLES `card_in_deck` WRITE;
/*!40000 ALTER TABLE `card_in_deck` DISABLE KEYS */;
INSERT INTO `card_in_deck` VALUES (5,3,16),(5,3,17),(4,3,20),(4,3,21),(4,1,29),(4,1,30),(5,5,36),(5,5,37),(5,5,38),(5,5,39),(5,1,43),(5,1,44),(5,1,45),(5,1,46),(5,1,47),(5,1,48),(5,1,49),(5,1,50),(5,1,51),(5,1,52),(5,1,53),(5,1,54),(5,1,55),(5,1,56),(5,1,57),(5,1,58),(5,1,59),(5,1,60),(5,1,61),(5,1,62),(5,1,63),(4,1,64),(4,1,65),(4,1,66),(4,1,67),(4,1,68),(4,1,69),(4,1,70),(4,1,71),(4,1,72),(5,1,73),(5,1,74),(5,1,75),(5,1,76),(5,1,77),(5,1,78),(4,1,79),(4,1,80);
/*!40000 ALTER TABLE `card_in_deck` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cards`
--

DROP TABLE IF EXISTS `cards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cards` (
  `Card_ID` int NOT NULL AUTO_INCREMENT,
  `Name` text NOT NULL,
  `Card_Type` text,
  PRIMARY KEY (`Card_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cards`
--

LOCK TABLES `cards` WRITE;
/*!40000 ALTER TABLE `cards` DISABLE KEYS */;
INSERT INTO `cards` VALUES (4,'1','EGO_Gift'),(5,'po','Sinner');
/*!40000 ALTER TABLE `cards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cards_in_board`
--

DROP TABLE IF EXISTS `cards_in_board`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cards_in_board` (
  `Card_ID` int NOT NULL,
  `Board_ID` int NOT NULL,
  KEY `Cards_In_Board_board_Board_ID_fk` (`Board_ID`),
  KEY `Cards_In_Board_cards_Card_ID_fk` (`Card_ID`),
  CONSTRAINT `Cards_In_Board_board_Board_ID_fk` FOREIGN KEY (`Board_ID`) REFERENCES `board` (`Board_ID`),
  CONSTRAINT `Cards_In_Board_cards_Card_ID_fk` FOREIGN KEY (`Card_ID`) REFERENCES `cards` (`Card_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cards_in_board`
--

LOCK TABLES `cards_in_board` WRITE;
/*!40000 ALTER TABLE `cards_in_board` DISABLE KEYS */;
/*!40000 ALTER TABLE `cards_in_board` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cards_in_hand`
--

DROP TABLE IF EXISTS `cards_in_hand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cards_in_hand` (
  `Card_ID` int NOT NULL,
  `Hand_ID` int NOT NULL,
  `card_in_hand_ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`card_in_hand_ID`),
  KEY `Cards_In_Hand_cards_Card_ID_fk` (`Card_ID`),
  KEY `Cards_In_Hand_hand_Hand_ID_fk` (`Hand_ID`),
  CONSTRAINT `Cards_In_Hand_cards_Card_ID_fk` FOREIGN KEY (`Card_ID`) REFERENCES `cards` (`Card_ID`),
  CONSTRAINT `Cards_In_Hand_hand_Hand_ID_fk` FOREIGN KEY (`Hand_ID`) REFERENCES `hand` (`Hand_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cards_in_hand`
--

LOCK TABLES `cards_in_hand` WRITE;
/*!40000 ALTER TABLE `cards_in_hand` DISABLE KEYS */;
/*!40000 ALTER TABLE `cards_in_hand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `decks`
--

DROP TABLE IF EXISTS `decks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `decks` (
  `Deck_ID` int NOT NULL AUTO_INCREMENT,
  `Number_of_Cards` int NOT NULL,
  `Name` text NOT NULL,
  `Hero_ID` int DEFAULT NULL,
  `Type` text NOT NULL,
  PRIMARY KEY (`Deck_ID`),
  KEY `decks_heroes_Hero_ID_fk` (`Hero_ID`),
  CONSTRAINT `decks_heroes_Hero_ID_fk` FOREIGN KEY (`Hero_ID`) REFERENCES `heroes` (`Hero_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `decks`
--

LOCK TABLES `decks` WRITE;
/*!40000 ALTER TABLE `decks` DISABLE KEYS */;
INSERT INTO `decks` VALUES (1,40,'Bili\'s Deck',1,'1'),(3,0,'Polo\'s Deck',1,'1'),(4,1,'1',NULL,'2'),(5,40,'Emmanuel Macron\'s Deck',1,'main');
/*!40000 ALTER TABLE `decks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `decks_in_board`
--

DROP TABLE IF EXISTS `decks_in_board`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `decks_in_board` (
  `Board_ID` int NOT NULL,
  `Deck_ID` int NOT NULL,
  KEY `Decks_In_Board_board_Board_ID_fk` (`Board_ID`),
  KEY `Decks_In_Board_decks_Deck_ID_fk` (`Deck_ID`),
  CONSTRAINT `Decks_In_Board_board_Board_ID_fk` FOREIGN KEY (`Board_ID`) REFERENCES `board` (`Board_ID`),
  CONSTRAINT `Decks_In_Board_decks_Deck_ID_fk` FOREIGN KEY (`Deck_ID`) REFERENCES `decks` (`Deck_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `decks_in_board`
--

LOCK TABLES `decks_in_board` WRITE;
/*!40000 ALTER TABLE `decks_in_board` DISABLE KEYS */;
/*!40000 ALTER TABLE `decks_in_board` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ego`
--

DROP TABLE IF EXISTS `ego`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ego` (
  `Card_ID` int NOT NULL,
  `Name` text NOT NULL,
  `Cost` int NOT NULL,
  `Ability` text,
  `Ability_text` text,
  `Passive` text,
  `Passive_text` text,
  `Sinner_name` text NOT NULL,
  `Damage` int NOT NULL,
  `Target_Number` int NOT NULL,
  KEY `EGO_cards_Card_ID_fk` (`Card_ID`),
  CONSTRAINT `EGO_cards_Card_ID_fk` FOREIGN KEY (`Card_ID`) REFERENCES `cards` (`Card_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ego`
--

LOCK TABLES `ego` WRITE;
/*!40000 ALTER TABLE `ego` DISABLE KEYS */;
/*!40000 ALTER TABLE `ego` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ego_gifts`
--

DROP TABLE IF EXISTS `ego_gifts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ego_gifts` (
  `Card_ID` int NOT NULL,
  `Name` text NOT NULL,
  `Cost` int NOT NULL,
  `Ability` text NOT NULL,
  `Ability_text` text NOT NULL,
  KEY `ego_gifts_cards_Card_ID_fk` (`Card_ID`),
  CONSTRAINT `ego_gifts_cards_Card_ID_fk` FOREIGN KEY (`Card_ID`) REFERENCES `cards` (`Card_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ego_gifts`
--

LOCK TABLES `ego_gifts` WRITE;
/*!40000 ALTER TABLE `ego_gifts` DISABLE KEYS */;
INSERT INTO `ego_gifts` VALUES (4,'1',1,'1','1');
/*!40000 ALTER TABLE `ego_gifts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game`
--

DROP TABLE IF EXISTS `game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game` (
  `Game_ID` int NOT NULL AUTO_INCREMENT,
  `State` text,
  PRIMARY KEY (`Game_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game`
--

LOCK TABLES `game` WRITE;
/*!40000 ALTER TABLE `game` DISABLE KEYS */;
INSERT INTO `game` VALUES (1,'1');
/*!40000 ALTER TABLE `game` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hand`
--

DROP TABLE IF EXISTS `hand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hand` (
  `Hand_ID` int NOT NULL AUTO_INCREMENT,
  `User_ID` int NOT NULL,
  PRIMARY KEY (`Hand_ID`),
  KEY `Hand___fk` (`User_ID`),
  CONSTRAINT `Hand___fk` FOREIGN KEY (`User_ID`) REFERENCES `users` (`User_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hand`
--

LOCK TABLES `hand` WRITE;
/*!40000 ALTER TABLE `hand` DISABLE KEYS */;
/*!40000 ALTER TABLE `hand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `heroes`
--

DROP TABLE IF EXISTS `heroes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `heroes` (
  `Name` text NOT NULL,
  `Hero_ID` int NOT NULL AUTO_INCREMENT,
  `Life` int NOT NULL,
  `Passive` text NOT NULL,
  `Passive_Text` text NOT NULL,
  PRIMARY KEY (`Hero_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `heroes`
--

LOCK TABLES `heroes` WRITE;
/*!40000 ALTER TABLE `heroes` DISABLE KEYS */;
INSERT INTO `heroes` VALUES ('BetaTesteur',1,50,'Exist','Exist');
/*!40000 ALTER TABLE `heroes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sinners`
--

DROP TABLE IF EXISTS `sinners`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sinners` (
  `Card_ID` int NOT NULL,
  `Name` text NOT NULL,
  `Sinner` text NOT NULL,
  `Cost` int NOT NULL,
  `Attack` int NOT NULL,
  `Defense_type` text NOT NULL,
  `Defense_value` int NOT NULL,
  `Speed` int NOT NULL,
  `Stagger` int NOT NULL,
  `Life` int NOT NULL,
  `abilities` text,
  `Text` text,
  KEY `Sinners_cards_Card_ID_fk` (`Card_ID`),
  CONSTRAINT `Sinners_cards_Card_ID_fk` FOREIGN KEY (`Card_ID`) REFERENCES `cards` (`Card_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sinners`
--

LOCK TABLES `sinners` WRITE;
/*!40000 ALTER TABLE `sinners` DISABLE KEYS */;
INSERT INTO `sinners` VALUES (5,'po','po',1,1,'1',1,1,1,1,'1','1');
/*!40000 ALTER TABLE `sinners` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `spell`
--

DROP TABLE IF EXISTS `spell`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `spell` (
  `Card_ID` int NOT NULL,
  `Cost` int NOT NULL,
  `ability` text NOT NULL,
  `Name` text NOT NULL,
  `Text` text NOT NULL,
  `Hero_ID` int NOT NULL,
  KEY `spell_cards_Card_ID_fk` (`Card_ID`),
  KEY `spell_heroes_Hero_ID_fk` (`Hero_ID`),
  CONSTRAINT `spell_cards_Card_ID_fk` FOREIGN KEY (`Card_ID`) REFERENCES `cards` (`Card_ID`),
  CONSTRAINT `spell_heroes_Hero_ID_fk` FOREIGN KEY (`Hero_ID`) REFERENCES `heroes` (`Hero_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `spell`
--

LOCK TABLES `spell` WRITE;
/*!40000 ALTER TABLE `spell` DISABLE KEYS */;
/*!40000 ALTER TABLE `spell` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_in_game`
--

DROP TABLE IF EXISTS `user_in_game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_in_game` (
  `User_ID` int NOT NULL,
  `Game_ID` int NOT NULL,
  KEY `user_in_game_game_Game_ID_fk` (`Game_ID`),
  KEY `user_in_game_users_User_ID_fk` (`User_ID`),
  CONSTRAINT `user_in_game_game_Game_ID_fk` FOREIGN KEY (`Game_ID`) REFERENCES `game` (`Game_ID`),
  CONSTRAINT `user_in_game_users_User_ID_fk` FOREIGN KEY (`User_ID`) REFERENCES `users` (`User_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_in_game`
--

LOCK TABLES `user_in_game` WRITE;
/*!40000 ALTER TABLE `user_in_game` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_in_game` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `Name` text NOT NULL,
  `User_ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`User_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('XxGameMasterxX',1),('MasterMind',2);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-13 19:33:36
