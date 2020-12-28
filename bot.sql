-- MariaDB dump 10.17  Distrib 10.5.6-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: bot
-- ------------------------------------------------------
-- Server version	10.5.6-MariaDB

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
-- Table structure for table `user`
--



drop user if exists 'pyprog'@'localhost';

FLUSH PRIVILEGES;

CREATE USER 'pyprog'@'localhost' IDENTIFIED BY 'itpas';

GRANT ALL PRIVILEGES ON * . * TO 'pyprog'@'localhost';

FLUSH PRIVILEGES;


DROP DATABASE IF EXISTS `bot`;

CREATE DATABASE `bot`;

use `bot` ;








DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` varchar(120) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `mode` varchar(15) DEFAULT NULL,
  `mode2` varchar(15) DEFAULT NULL,
  `mode3` varchar(20) DEFAULT NULL,
  `fmode` text DEFAULT NULL,
  `fmode2` text DEFAULT NULL,
  `fmode3` text DEFAULT NULL,
  `ready` enum('True','False','False2','True2') DEFAULT NULL,
  `modint` int(11) DEFAULT NULL,
  `word1` varchar(200) DEFAULT NULL,
  `word2` varchar(200) DEFAULT NULL,
  `word3` varchar(200) DEFAULT NULL,
  `word4` varchar(200) DEFAULT NULL,
  `word5` varchar(200) DEFAULT NULL,
  `tday` enum('True','False','False2','True2') DEFAULT NULL,
  `word6` varchar(200) DEFAULT NULL,
  `word7` varchar(200) DEFAULT NULL,
  `word8` varchar(200) DEFAULT NULL,
  `word9` varchar(200) DEFAULT NULL,
  `word10` varchar(200) DEFAULT NULL,
  `qmode` TEXT ,
  `sendtime` int(11) ,
  `flo` float 
  
  ) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--
--
-- Table structure for table `words`
--

DROP TABLE IF EXISTS `words`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `words` (
  `en` varchar(50) DEFAULT NULL,
  `fa` varchar(240) DEFAULT NULL,
  `num` int(11) DEFAULT NULL,
  `mode` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `words`
--

LOCK TABLES `words` WRITE;
/*!40000 ALTER TABLE `words` DISABLE KEYS */;
INSERT INTO `words` VALUES ('avicenna','a0ab0bn0n s0sy0yn0na0a',1,'False'),('leopard','p0pl0ln0ng0g',2,'False'),('box','j0jA0Ab0bh0h',3,'False'),('laptop','l0lp0p t0ta0ap0p',4,'False'),('visitor','m0ml0la0ag0ha0at0t c0kn0nn0nd0dh0h,m0ml0la0ag0ha0at0t g0gr0r,b0ba0az0zd0dy0yd0d c0kn0nn0nd0dh0h',5,'False'),('die out','m0mn0ng0hr0rZ0Z s0hd0dn0n',6,'False'),('cut','g0hT0TA0A c0kr0rd0dn0n  d0dr0rk0ht0t  k0hT0T v0w',7,'False'),('elephant','f0fy0yl0l',8,'False'),('foot','p0pa0a  a0az0z a0an0ng0gs0ht0t  h0ha0a t0ta0a  m0mc0h',9,'False'),('human','a0an0ns0sa0an0n',10,'False'),('will','f0fA0Al0l c0km0mc0ky0y  z0zm0ma0an0n A0ay0yn0nd0dh0h',11,'False'),('trip','s0sf0fr0r',12,'False'),('earth','z0zm0my0yn0n',13,'False'),('duck','a0ar0rd0dc0k',14,'False'),('travel','s0sf0fr0r c0kr0rd0dn0n',15,'False'),('life','z0zn0nd0dg0gy0y',16,'False'),('mean','b0bh0h m0mA0An0ny0y  c0hy0yz0zy0y  b0bv0wd0dn0n',17,'False'),('endangered','d0dr0r m0mA0Ar0rZ0Z  a0an0ng0hr0ra0aZ0Z',18,'False'),('small','c0kv0wc0hc0k',19,'False'),('gazelle','g0Hz0za0al0l',20,'False'),('hurt','z0zk0hm0my0y c0kr0rd0dn0n  f0fy0yz0zy0yc0ky0y',21,'False'),('person','f0fr0rd0d',22,'False'),('alive','z0zn0nd0dh0h',23,'False'),('plain','j0jl0lg0gh0h',24,'False'),('tiger','b0bb0br0r',25,'False'),('instead','d0dr0r A0Av0wZ0Z',26,'False'),('sky','A0as0sm0ma0an0n',27,'False'),('information','a0aT0Tl0la0aA0Aa0at0t',28,'False'),('increase','a0af0fz0za0ay0ys0h y0ya0af0ft0tn0n',29,'False'),('around','d0dv0wr0r',30,'False'),('future','A0ay0yn0nd0dh0h',31,'False'),('wild','v0wH0Hs0hy0y',32,'False'),('dolphin','d0dl0lf0fy0yn0n',33,'False'),('injured','A0as0sy0yb0b  d0dy0yd0dh0h',34,'False'),('learn','y0ya0ad0d g0gr0rf0ft0tn0n',35,'False'),('hear','s0hn0ny0yd0dn0n',36,'False'),('hunter','s0hc0ka0ar0rc0hy0y',37,'False'),('today','a0am0mr0rv0wz0z',38,'False'),('pay attention','t0tv0wj0jh0h c0kn0ny0yd0d',39,'False'),('destroy','n0na0ab0bv0wd0d c0kr0rd0dn0n',40,'False'),('among','d0dr0r  m0my0ya0an0n',41,'False'),('protect','m0mH0Ha0af0fZ0zt0t c0kr0rd0dn0n',42,'False'),('hunt','s0hc0ka0ar0r c0kr0rd0dn0n',43,'False'),('low','c0km0m',44,'False'),('save','n0nj0ja0at0t d0da0ad0dn0n',45,'False'),('nowadays','a0am0mr0rv0wz0zh0h',46,'False'),('jungle','j0jn0ng0gl0l',47,'False'),('for example','b0br0ra0ay0y m0ms0ca0al0l',48,'False'),('goat','b0bz0z',49,'False'),('road','j0ja0ad0dh0h',50,'False'),('world','j0jh0ha0an0n',51,'False'),('nature','T0Tb0by0yA0At0t',52,'False'),('high','b0bl0ln0nd0d',53,'False'),('beautiful','z0zy0yb0ba0a',54,'False'),('zookeeper','n0ng0gh0hb0ba0an0n b0ba0ag0H  v0wH0Hs0h',55,'False'),('natural','T0Tb0by0yA0Ay0y',56,'False'),('pain','d0dr0rd0d',57,'False'),('go hunting','b0bh0h s0hc0ka0ar0r  r0rf0ft0tn0n',58,'False'),('program','b0br0rn0na0am0mh0h  z0zm0ma0an0ny0y  c0ka0am0mp0py0yv0wt0tr0ry0y  t0tl0lv0wy0yz0zy0yv0wn0ny0y v0w',59,'False'),('whale','n0nh0hn0ng0g',60,'False'),('forest','j0jn0ng0gl0l',61,'False'),('bear','k0hr0rs0s',62,'False'),('bird','p0pr0rn0nd0dh0h',63,'False'),('boring','k0hs0st0th0h  c0kn0nn0nd0dh0h',64,'False'),('wildlife','H0Hy0ya0at0t v0wH0Hs0h',65,'False'),('attention','t0tv0wj0jh0h',66,'False'),('recently','a0ak0hy0yr0ra0a',67,'False'),('safe','a0am0mn0n',68,'False'),('lose','g0gm0m c0kr0rd0dn0n',69,'False'),('go out','b0by0yr0rv0wn0n r0rf0ft0tn0n',70,'False'),('giraffe','z0zr0ra0af0fh0h',71,'False'),('anymore','d0dy0yg0gr0r',72,'False'),('wolf','g0gr0rg0g',73,'False'),('cheetah','y0yv0wz0zp0pl0ln0ng0g',74,'False'),('danger','k0hT0Tr0r',75,'False'),('plant','g0gy0ya0ah0h',76,'False'),('cat','g0gr0rb0bh0h',77,'False'),('noun','a0as0sm0m',78,'False'),('hopefully','a0an0ns0ha0aa0al0ll0lh0h',79,'False'),('lion','s0hy0yr0r  H0Hy0yv0wa0an0n',80,'False'),('zebra','g0gv0wr0rk0hr0r',81,'False'),('a few','t0tA0Ad0da0ad0dy0y',82,'False'),('movies','s0sy0yn0nm0ma0a',83,'False'),('panda','p0pa0an0nd0da0a',84,'False'),('sea','d0dr0ry0ya0a',85,'False'),('orbit','m0md0da0ar0r',86,'False'),('large','b0bz0zr0rg0g',87,'False'),('expensive','g0gr0ra0an0n',88,'False'),('telescope','t0tl0ls0sc0kv0wp0p',89,'False'),('long','b0bl0ln0nd0d',90,'False'),('quality','v0wy0yz0hg0gy0y',91,'False'),('fact','H0Hg0hy0yg0ht0t',92,'False'),('daily','r0rv0wz0za0an0nh0h',93,'False'),('microscope','m0my0yc0kr0rv0ws0sc0kv0wp0p',94,'False'),('Neptune','n0np0pt0tv0wn0n',95,'False'),('powerful','n0ny0yr0rv0wm0mn0nd0d',96,'False'),('dark','t0ty0yr0rh0h',97,'False'),('farthest','d0dv0wr0rt0tr0ry0yn0n',98,'False'),('real','v0wa0ag0hA0Ay0y',99,'False'),('opinion','n0nZ0zr0r',100,'False'),('thousand','h0hz0za0ar0r',101,'False'),('easy','s0sa0ad0dh0h',102,'False'),('better','b0bh0ht0tr0r',103,'False'),('Mars','m0mr0ry0yk0h',104,'False'),('type','n0nv0wA0A',105,'False'),('plasma','p0pl0la0as0sm0ma0a  k0hv0wn0n',106,'False'),('interested','A0Al0la0ag0hh0h  m0mn0nd0d',107,'False'),('people','m0mr0rd0dm0m',108,'False'),('tall','m0mr0rt0tf0fA0A',109,'False'),('best','b0bh0ht0tr0ry0yn0n',110,'False'),('fatty','c0hr0rb0b',111,'False'),('pepper','f0fl0lf0fl0l',112,'False'),('much','z0zy0ya0ad0d',113,'False'),('liquid','n0ng0hd0d',114,'False'),('material','m0ma0ad0dh0h',115,'False'),('heavens','A0as0sm0ma0an0n h0ha0a',116,'False'),('camel','s0ht0tr0r',117,'False'),('bad','b0bd0d',118,'False'),('alike','s0hb0by0yh0h  b0bh0h h0hm0m',119,'False'),('gold','T0Tl0la0a',120,'False'),('ugly','z0zs0ht0t',121,'False'),('Saturn','z0zH0Hl0l  s0sy0ya0ar0rh0h',122,'False'),('cloudy','a0ab0br0ry0y',123,'False'),('oxygen','a0ac0ks0sy0yz0hn0n',124,'False'),('wooden','c0hv0wb0by0y',125,'False'),('more','b0by0ys0ht0tr0r',126,'False'),('exercise','v0wr0rz0zs0h',127,'False'),('planet','s0sy0ya0ar0rh0h',128,'False'),('ticket','b0bl0ly0yt0t',129,'False'),('more','t0tr0r  n0ns0ha0an0nh0h S0Sf0ft0t  t0tf0fZ0Zy0yl0ly0y',130,'False'),('worse','b0bd0dt0tr0r',131,'False'),('medium','m0mt0tv0ws0sT0T',132,'False'),('golden','T0Tl0la0ay0yy0y  r0rn0ng0g',133,'False'),('different','m0mt0tf0fa0av0wt0t',134,'False'),('carbon dioxide','d0dy0y a0ac0ks0sy0yd0d  c0kr0rb0bn0n  s0hy0ym0my0y',135,'False'),('without','b0bd0dv0wn0n',136,'False'),('silver','n0ng0hr0rh0h',137,'False'),('microbe','m0my0yc0kr0rv0wb0b',138,'False'),('wonder','c0hy0yz0z A0Aj0jy0yb0b',139,'False'),('sun','k0hv0wr0rs0hy0yd0d',140,'False'),('rocky','s0sn0ng0gy0y',141,'False'),('worst','b0bd0dt0tr0ry0yn0n',142,'False'),('brain','m0mg0Hz0z',143,'False'),('above','b0ba0al0la0ay0y',144,'False'),('most','t0tr0ry0yn0n  n0ns0ha0an0nh0h S0Sf0ft0t  y0ya0a g0hy0yd0d  A0Aa0al0ly0y',145,'False'),('liquid','m0ma0ay0yA0A',146,'False'),('ring','H0Hl0lg0hh0h',147,'False'),('pump','p0pm0mp0pa0az0h c0kr0rd0dn0n',148,'False'),('strong','n0ny0yr0rv0wm0mn0nd0d',149,'False'),('both','h0hr0r d0dv0w',150,'False'),('creation','A0af0fr0ry0yn0ns0h',151,'False'),('difficult','m0ms0hc0kl0l',152,'False'),('Uranus','a0av0wr0ra0an0nv0ws0s  s0sy0ya0ar0rh0h',153,'False'),('cross','A0Ab0bv0wr0r c0kr0rd0dn0n',154,'False'),('nation','c0ks0hv0wr0r',155,'False'),('metal','f0fl0lz0z',156,'False'),('drop','g0hT0Tr0rh0h',157,'False'),('ant','m0mv0wr0rc0hh0h',158,'False'),('far','d0dv0wr0r',159,'False'),('energy','a0an0nr0rz0hy0y',160,'False'),('million','m0my0yl0ly0yv0wn0n',161,'False'),('heart','g0hl0lb0b',162,'False'),('plastic','p0pl0la0as0st0ty0yc0ky0y',163,'False'),('False','v0wa0ag0hA0Ay0y',164,'False'),('as','b0bh0h a0an0nd0da0az0zh0h',165,'False'),('useful','s0sv0wd0dm0mn0nd0d',166,'False'),('body','b0bd0dn0n',167,'False'),('round','d0dv0wr0r',168,'False'),('Mercury','A0AT0Ta0ar0rd0d',169,'False'),('ball','t0tv0wp0p',170,'False'),('blood','k0hv0wn0n',171,'False'),('fresh','t0ta0az0zh0h',172,'False'),('go around','H0Hv0wl0l c0hy0yz0zy0y  g0gs0ht0tn0n',173,'False'),('paint','r0rn0ng0g',174,'False'),('seafood','g0Hz0Za0ay0y d0dr0ry0ya0ay0yy0y',175,'False'),('organ','A0AZ0Zv0w',176,'False'),('donate','a0ah0hd0da0a c0kr0rd0dn0n',177,'False'),('moon','m0ma0ah0h',178,'False'),('healthy','s0sa0al0lm0m',179,'False'),('color','r0rn0ng0g',180,'False'),('everyone','h0hm0mh0h',181,'False'),('modern','m0md0dr0rn0n',182,'False'),('light','r0rv0ws0hn0n c0kr0rd0dn0n',183,'False'),('delicious','k0hv0ws0hm0mz0zh0h',184,'False'),('Venus','z0zh0hr0rh0h  s0sy0ya0ar0rh0h',185,'False'),('fast food','f0fs0st0t f0fv0wd0d',186,'False'),('defend','d0df0fa0aA0A c0kr0rd0dn0n',187,'False'),('system','s0sy0ys0st0tm0m',188,'False'),('allah','a0al0ll0lh0h',189,'False'),('carry','H0Hm0ml0l c0kr0rd0dn0n',190,'False'),('farther','d0dv0wr0rt0tr0r',191,'False'),('adjective','S0Sf0ft0t',192,'False'),('cell','s0sl0lv0wl0l  z0zy0ys0st0t  s0hn0na0as0sy0y',193,'False'),('observatory','r0rS0Sd0dk0ha0an0nh0h',194,'False'),('lamp','c0hr0ra0ag0H',195,'False'),('clear','v0wa0aZ0ZH0H',196,'False'),('Jupiter','m0ms0ht0tr0ry0y  s0sy0ya0ar0rh0h',197,'False'),('collect','j0jm0mA0A  A0av0wr0ry0y c0kr0rd0dn0n',198,'False'),('sign','n0ns0ha0an0nh0h',199,'False'),('important','m0mh0hm0m',200,'False'),('deep','A0Am0my0yg0h',201,'False'),('size','a0an0nd0da0az0zh0h',202,'False'),('much','z0zy0ya0ad0d',203,'False'),('much','z0zy0ya0ad0d',204,'False'),('end','p0pa0ay0ya0an0n',205,'False');
/*!40000 ALTER TABLE `words` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-09 16:28:34
