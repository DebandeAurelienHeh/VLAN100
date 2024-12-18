-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 18, 2024 at 10:37 AM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ecole_vlan100`
--

-- --------------------------------------------------------

--
-- Table structure for table `absences`
--

CREATE TABLE `absences` (
  `id_absence` int NOT NULL,
  `id_etudiant` int NOT NULL,
  `id_cours` int NOT NULL,
  `date_absence` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `cours_global`
--

CREATE TABLE `cours_global` (
  `id_cours` int NOT NULL,
  `nom_cours` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `description` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `id_professeur` int NOT NULL,
  `id_salle` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `etudiants`
--

CREATE TABLE `etudiants` (
  `id_etudiant` int NOT NULL,
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `mdp` varchar(255) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `prenom` varchar(100) NOT NULL,
  `departement` varchar(100) DEFAULT NULL,
  `statut` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `incidents_globaux`
--

CREATE TABLE `incidents_globaux` (
  `id_incident` int NOT NULL,
  `id_salle` int NOT NULL,
  `description_incident` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `date_signalement` date NOT NULL,
  `statut` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inscriptions_globales`
--

CREATE TABLE `inscriptions_globales` (
  `id_inscription_globale` int NOT NULL,
  `id_etudiant` int NOT NULL,
  `id_cours` int NOT NULL,
  `statut` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `notes_globales`
--

CREATE TABLE `notes_globales` (
  `id_note` int NOT NULL,
  `id_etudiant` int NOT NULL,
  `id_cours` int NOT NULL,
  `note` float DEFAULT NULL,
  `date_saisie` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `plannings_globaux`
--

CREATE TABLE `plannings_globaux` (
  `id_planning` int NOT NULL,
  `id_cours` int NOT NULL,
  `departement` varchar(100) DEFAULT NULL,
  `horaire` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `professeurs`
--

CREATE TABLE `professeurs` (
  `id_professeur` int NOT NULL,
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `nom` varchar(100) NOT NULL,
  `prenom` varchar(100) NOT NULL,
  `mdp` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `departement` varchar(100) DEFAULT NULL,
  `statut` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `professeurs_notes`
--

CREATE TABLE `professeurs_notes` (
  `id_professeurs_notes` int NOT NULL,
  `id_professeur` int NOT NULL,
  `id_note` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `salles_globales`
--

CREATE TABLE `salles_globales` (
  `id_salle` int NOT NULL,
  `numero_salle` int NOT NULL,
  `statut` tinyint(1) DEFAULT NULL,
  `departement` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `absences`
--
ALTER TABLE `absences`
  ADD PRIMARY KEY (`id_absence`),
  ADD KEY `id_etudiant` (`id_etudiant`),
  ADD KEY `id_cours` (`id_cours`);

--
-- Indexes for table `cours_global`
--
ALTER TABLE `cours_global`
  ADD PRIMARY KEY (`id_cours`),
  ADD KEY `id_professeur` (`id_professeur`),
  ADD KEY `id_salle` (`id_salle`);

--
-- Indexes for table `etudiants`
--
ALTER TABLE `etudiants`
  ADD PRIMARY KEY (`id_etudiant`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `incidents_globaux`
--
ALTER TABLE `incidents_globaux`
  ADD PRIMARY KEY (`id_incident`),
  ADD KEY `id_salle` (`id_salle`);

--
-- Indexes for table `inscriptions_globales`
--
ALTER TABLE `inscriptions_globales`
  ADD PRIMARY KEY (`id_inscription_globale`),
  ADD KEY `id_etudiant` (`id_etudiant`),
  ADD KEY `id_cours` (`id_cours`);

--
-- Indexes for table `notes_globales`
--
ALTER TABLE `notes_globales`
  ADD PRIMARY KEY (`id_note`),
  ADD KEY `id_etudiant` (`id_etudiant`),
  ADD KEY `id_cours` (`id_cours`);

--
-- Indexes for table `plannings_globaux`
--
ALTER TABLE `plannings_globaux`
  ADD PRIMARY KEY (`id_planning`),
  ADD KEY `id_cours` (`id_cours`);

--
-- Indexes for table `professeurs`
--
ALTER TABLE `professeurs`
  ADD PRIMARY KEY (`id_professeur`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `professeurs_notes`
--
ALTER TABLE `professeurs_notes`
  ADD PRIMARY KEY (`id_professeurs_notes`),
  ADD KEY `id_professeur` (`id_professeur`),
  ADD KEY `id_note` (`id_note`);

--
-- Indexes for table `salles_globales`
--
ALTER TABLE `salles_globales`
  ADD PRIMARY KEY (`id_salle`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `absences`
--
ALTER TABLE `absences`
  MODIFY `id_absence` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cours_global`
--
ALTER TABLE `cours_global`
  MODIFY `id_cours` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `etudiants`
--
ALTER TABLE `etudiants`
  MODIFY `id_etudiant` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `incidents_globaux`
--
ALTER TABLE `incidents_globaux`
  MODIFY `id_incident` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inscriptions_globales`
--
ALTER TABLE `inscriptions_globales`
  MODIFY `id_inscription_globale` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `notes_globales`
--
ALTER TABLE `notes_globales`
  MODIFY `id_note` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `plannings_globaux`
--
ALTER TABLE `plannings_globaux`
  MODIFY `id_planning` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `professeurs`
--
ALTER TABLE `professeurs`
  MODIFY `id_professeur` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `professeurs_notes`
--
ALTER TABLE `professeurs_notes`
  MODIFY `id_professeurs_notes` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `salles_globales`
--
ALTER TABLE `salles_globales`
  MODIFY `id_salle` int NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `absences`
--
ALTER TABLE `absences`
  ADD CONSTRAINT `absences_ibfk_1` FOREIGN KEY (`id_etudiant`) REFERENCES `etudiants` (`id_etudiant`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `absences_ibfk_2` FOREIGN KEY (`id_cours`) REFERENCES `cours_global` (`id_cours`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `cours_global`
--
ALTER TABLE `cours_global`
  ADD CONSTRAINT `cours_global_ibfk_1` FOREIGN KEY (`id_professeur`) REFERENCES `professeurs` (`id_professeur`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `cours_global_ibfk_2` FOREIGN KEY (`id_salle`) REFERENCES `salles_globales` (`id_salle`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `incidents_globaux`
--
ALTER TABLE `incidents_globaux`
  ADD CONSTRAINT `incidents_globaux_ibfk_1` FOREIGN KEY (`id_salle`) REFERENCES `salles_globales` (`id_salle`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `inscriptions_globales`
--
ALTER TABLE `inscriptions_globales`
  ADD CONSTRAINT `inscriptions_globales_ibfk_1` FOREIGN KEY (`id_etudiant`) REFERENCES `etudiants` (`id_etudiant`),
  ADD CONSTRAINT `inscriptions_globales_ibfk_2` FOREIGN KEY (`id_cours`) REFERENCES `cours_global` (`id_cours`);

--
-- Constraints for table `notes_globales`
--
ALTER TABLE `notes_globales`
  ADD CONSTRAINT `notes_globales_ibfk_1` FOREIGN KEY (`id_etudiant`) REFERENCES `etudiants` (`id_etudiant`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `notes_globales_ibfk_2` FOREIGN KEY (`id_cours`) REFERENCES `cours_global` (`id_cours`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `plannings_globaux`
--
ALTER TABLE `plannings_globaux`
  ADD CONSTRAINT `plannings_globaux_ibfk_1` FOREIGN KEY (`id_cours`) REFERENCES `cours_global` (`id_cours`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `professeurs_notes`
--
ALTER TABLE `professeurs_notes`
  ADD CONSTRAINT `professeurs_notes_ibfk_1` FOREIGN KEY (`id_professeur`) REFERENCES `professeurs` (`id_professeur`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `professeurs_notes_ibfk_2` FOREIGN KEY (`id_note`) REFERENCES `notes_globales` (`id_note`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
