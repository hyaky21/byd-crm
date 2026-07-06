-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : lun. 06 juil. 2026 à 15:31
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `byd_crm`
--

-- --------------------------------------------------------

--
-- Structure de la table `canaux`
--

CREATE TABLE `canaux` (
  `id` int(11) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `actif` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `canaux`
--

INSERT INTO `canaux` (`id`, `nom`, `actif`, `created_at`) VALUES
(1, 'Showroom', 1, '2026-07-02 10:23:55'),
(2, 'Leads', 1, '2026-07-02 10:23:55'),
(3, 'Planning', 1, '2026-07-02 10:23:55'),
(4, 'Prospection terrain', 1, '2026-07-02 10:23:55'),
(5, 'Recommandation', 1, '2026-07-02 10:23:55');

-- --------------------------------------------------------

--
-- Structure de la table `commerciaux`
--

CREATE TABLE `commerciaux` (
  `id` int(11) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `actif` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `commerciaux`
--

INSERT INTO `commerciaux` (`id`, `nom`, `actif`, `created_at`) VALUES
(1, 'Mouna', 1, '2026-07-02 10:23:55'),
(2, 'Driss', 1, '2026-07-02 10:23:55'),
(3, 'Omar', 1, '2026-07-02 10:23:55'),
(5, 'Siham', 1, '2026-07-02 10:23:55'),
(6, 'Khalil', 1, '2026-07-02 10:23:55'),
(8, 'Amal', 1, '2026-07-02 12:57:25');

-- --------------------------------------------------------

--
-- Structure de la table `couleurs`
--

CREATE TABLE `couleurs` (
  `id` int(11) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `actif` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `couleurs`
--

INSERT INTO `couleurs` (`id`, `nom`, `actif`, `created_at`) VALUES
(1, 'White', 1, '2026-07-02 10:23:55'),
(2, 'Time Grey', 1, '2026-07-02 10:23:55'),
(3, 'Smokey Grey', 1, '2026-07-02 10:23:55'),
(4, 'Black', 1, '2026-07-02 10:23:55'),
(5, 'Atlantis Grey', 1, '2026-07-02 10:23:55'),
(6, 'Cyan Blue', 1, '2026-07-02 10:23:55'),
(7, 'Green', 1, '2026-07-02 10:23:55'),
(8, 'ND', 1, '2026-07-02 10:23:55');

-- --------------------------------------------------------

--
-- Structure de la table `detail_canaux`
--

CREATE TABLE `detail_canaux` (
  `id` int(11) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `actif` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `detail_canaux`
--

INSERT INTO `detail_canaux` (`id`, `nom`, `actif`, `created_at`) VALUES
(1, 'Affichage', 1, '2026-07-02 10:23:55'),
(2, 'Client BYD', 1, '2026-07-02 10:23:55'),
(3, 'Réseaux sociaux', 1, '2026-07-02 10:23:55'),
(4, 'Autre', 1, '2026-07-02 10:23:55');

-- --------------------------------------------------------

--
-- Structure de la table `financements`
--

CREATE TABLE `financements` (
  `id` int(11) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `actif` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `financements`
--

INSERT INTO `financements` (`id`, `nom`, `actif`, `created_at`) VALUES
(1, 'Comptant', 1, '2026-07-02 10:23:55'),
(2, 'Wafasalaf', 1, '2026-07-02 10:23:55'),
(3, 'Sofac', 1, '2026-07-02 10:23:55'),
(4, 'Vivalis', 1, '2026-07-02 10:23:55'),
(5, 'Eqdom', 1, '2026-07-02 10:23:55'),
(6, 'Salafin', 1, '2026-07-02 10:23:55'),
(7, 'Banque Islamique', 1, '2026-07-02 10:23:55'),
(8, 'Organisme de leasing', 1, '2026-07-02 10:23:55'),
(10, 'Epder', 1, '2026-07-03 14:14:41'),
(11, 'ND', 1, '2026-07-06 13:30:11');

-- --------------------------------------------------------

--
-- Structure de la table `interieurs`
--

CREATE TABLE `interieurs` (
  `id` int(11) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `actif` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `interieurs`
--

INSERT INTO `interieurs` (`id`, `nom`, `actif`, `created_at`) VALUES
(1, 'Brown Black', 1, '2026-07-02 10:23:55'),
(2, 'Black', 1, '2026-07-02 10:23:55'),
(3, 'Beige', 1, '2026-07-02 10:23:55'),
(4, 'ND', 1, '2026-07-02 10:23:55'),
(5, 'blue', 1, '2026-07-03 12:12:40');

-- --------------------------------------------------------

--
-- Structure de la table `modeles`
--

CREATE TABLE `modeles` (
  `id` int(11) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `actif` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `modeles`
--

INSERT INTO `modeles` (`id`, `nom`, `actif`, `created_at`) VALUES
(1, 'Seal U', 1, '2026-07-02 10:23:55'),
(2, 'Seal 5', 1, '2026-07-02 10:23:55'),
(3, 'Atto 2', 1, '2026-07-02 10:23:55'),
(4, 'Atto 3', 1, '2026-07-02 10:23:55'),
(5, 'Seagull', 1, '2026-07-02 10:23:55'),
(6, 'Han', 1, '2026-07-02 10:23:55'),
(7, 'Sealion 7', 1, '2026-07-02 10:23:55'),
(8, 'Sealion 5', 1, '2026-07-02 10:23:55');

-- --------------------------------------------------------

--
-- Structure de la table `motorisations`
--

CREATE TABLE `motorisations` (
  `id` int(11) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `actif` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `motorisations`
--

INSERT INTO `motorisations` (`id`, `nom`, `actif`, `created_at`) VALUES
(1, 'PHEV', 1, '2026-07-02 10:23:55'),
(2, 'EV', 1, '2026-07-02 10:23:55');

-- --------------------------------------------------------

--
-- Structure de la table `potentiels`
--

CREATE TABLE `potentiels` (
  `id` int(11) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `actif` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `potentiels`
--

INSERT INTO `potentiels` (`id`, `nom`, `actif`, `created_at`) VALUES
(1, 'Opportunité', 1, '2026-07-02 10:23:55'),
(2, 'Affaire chaude', 1, '2026-07-02 10:23:55'),
(3, 'Commande', 1, '2026-07-02 10:23:55');

-- --------------------------------------------------------

--
-- Structure de la table `prospects`
--

CREATE TABLE `prospects` (
  `id` int(11) NOT NULL,
  `annee` int(11) NOT NULL,
  `mois` varchar(30) NOT NULL,
  `date_contact` date NOT NULL,
  `commercial_id` int(11) NOT NULL,
  `nom_client` varchar(100) NOT NULL,
  `prenom_client` varchar(100) NOT NULL,
  `telephone` varchar(30) NOT NULL,
  `email` varchar(120) DEFAULT NULL,
  `ville` varchar(100) DEFAULT NULL,
  `potentiel_id` int(11) NOT NULL,
  `modele_id` int(11) NOT NULL,
  `version_id` int(11) NOT NULL,
  `couleur_id` int(11) DEFAULT NULL,
  `interieur_id` int(11) DEFAULT NULL,
  `motorisation_id` int(11) DEFAULT NULL,
  `financement_id` int(11) DEFAULT NULL,
  `canal_id` int(11) DEFAULT NULL,
  `detail_canal_id` int(11) DEFAULT NULL,
  `commentaire` text DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `prospects`
--

INSERT INTO `prospects` (`id`, `annee`, `mois`, `date_contact`, `commercial_id`, `nom_client`, `prenom_client`, `telephone`, `email`, `ville`, `potentiel_id`, `modele_id`, `version_id`, `couleur_id`, `interieur_id`, `motorisation_id`, `financement_id`, `canal_id`, `detail_canal_id`, `commentaire`, `created_at`) VALUES
(2, 2026, 'Septembre', '2026-07-23', 1, 'grqetr\'', 'geqqr', '0637778555', 'fezq@gmail.com', 'fes', 2, 3, 2, 5, 2, 2, 8, 3, 1, 'efzefq', '2026-07-02 10:38:38'),
(4, 2026, 'Janvier', '2026-02-07', 6, 'jhgyh', 'jnjh', '0657894563', 'bvft@jnhb.com', 'marrakech', 2, 5, 2, 6, 3, 2, 8, 1, 4, 'bj,hbjh', '2026-07-02 16:20:55'),
(5, 2027, '06', '2027-06-02', 8, 'hjkjj', 'bj,hgyg', '0789654123', 'baderhatlove@gmail.com', 'casa', 2, 7, 3, 7, 3, 2, 1, 5, 1, 'jh;kjhuh', '2026-07-02 16:27:50'),
(6, 2026, '08', '2026-08-27', 6, 'kaks', 'cqscdes', '0789654123', 'aghdcjqsb@gmail.com', 'tanger', 3, 3, 2, 2, 2, 2, 7, 3, 1, 'csdcsfvf<v', '2026-07-03 09:15:51'),
(7, 2026, '07', '2026-07-01', 2, 'gersgt', 'gstrg', '0657894563', 'badeff@gmail.com', 'marrakech', 3, 2, 2, 6, 2, 1, 7, 2, 1, 'qcsdsc', '2026-07-03 10:42:51'),
(8, 2026, '07', '2026-07-07', 8, 'gfrdfr', 'frdsef', '0657894563', 'bnfe@gmail.com', 'marrakech', 2, 3, 1, 4, 2, 1, 4, 1, 2, 'esfre', '2026-07-03 11:57:43'),
(9, 2026, '07', '2026-07-28', 6, 'GREVFVG', 'FREWVGF', '0637778555', 'fqvqg@gmail.com', 'FEZQ<Q', 2, 4, 2, 4, 2, 1, 7, 2, 4, '', '2026-07-03 14:33:01');

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `email` varchar(120) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` varchar(50) DEFAULT NULL,
  `actif` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `versions`
--

CREATE TABLE `versions` (
  `id` int(11) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `actif` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `versions`
--

INSERT INTO `versions` (`id`, `nom`, `actif`, `created_at`) VALUES
(1, 'Comfort', 1, '2026-07-02 10:23:55'),
(2, 'Design', 1, '2026-07-02 10:23:55'),
(3, 'Design Sport', 1, '2026-07-02 10:23:55'),
(4, 'Design AWD', 1, '2026-07-02 10:23:55');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `canaux`
--
ALTER TABLE `canaux`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nom` (`nom`);

--
-- Index pour la table `commerciaux`
--
ALTER TABLE `commerciaux`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nom` (`nom`);

--
-- Index pour la table `couleurs`
--
ALTER TABLE `couleurs`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nom` (`nom`);

--
-- Index pour la table `detail_canaux`
--
ALTER TABLE `detail_canaux`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nom` (`nom`);

--
-- Index pour la table `financements`
--
ALTER TABLE `financements`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nom` (`nom`);

--
-- Index pour la table `interieurs`
--
ALTER TABLE `interieurs`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nom` (`nom`);

--
-- Index pour la table `modeles`
--
ALTER TABLE `modeles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nom` (`nom`);

--
-- Index pour la table `motorisations`
--
ALTER TABLE `motorisations`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nom` (`nom`);

--
-- Index pour la table `potentiels`
--
ALTER TABLE `potentiels`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nom` (`nom`);

--
-- Index pour la table `prospects`
--
ALTER TABLE `prospects`
  ADD PRIMARY KEY (`id`),
  ADD KEY `commercial_id` (`commercial_id`),
  ADD KEY `potentiel_id` (`potentiel_id`),
  ADD KEY `modele_id` (`modele_id`),
  ADD KEY `version_id` (`version_id`),
  ADD KEY `couleur_id` (`couleur_id`),
  ADD KEY `interieur_id` (`interieur_id`),
  ADD KEY `motorisation_id` (`motorisation_id`),
  ADD KEY `financement_id` (`financement_id`),
  ADD KEY `canal_id` (`canal_id`),
  ADD KEY `detail_canal_id` (`detail_canal_id`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Index pour la table `versions`
--
ALTER TABLE `versions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nom` (`nom`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `canaux`
--
ALTER TABLE `canaux`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT pour la table `commerciaux`
--
ALTER TABLE `commerciaux`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT pour la table `couleurs`
--
ALTER TABLE `couleurs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT pour la table `detail_canaux`
--
ALTER TABLE `detail_canaux`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `financements`
--
ALTER TABLE `financements`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT pour la table `interieurs`
--
ALTER TABLE `interieurs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT pour la table `modeles`
--
ALTER TABLE `modeles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT pour la table `motorisations`
--
ALTER TABLE `motorisations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `potentiels`
--
ALTER TABLE `potentiels`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `prospects`
--
ALTER TABLE `prospects`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `versions`
--
ALTER TABLE `versions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `prospects`
--
ALTER TABLE `prospects`
  ADD CONSTRAINT `prospects_ibfk_1` FOREIGN KEY (`commercial_id`) REFERENCES `commerciaux` (`id`),
  ADD CONSTRAINT `prospects_ibfk_10` FOREIGN KEY (`detail_canal_id`) REFERENCES `detail_canaux` (`id`),
  ADD CONSTRAINT `prospects_ibfk_2` FOREIGN KEY (`potentiel_id`) REFERENCES `potentiels` (`id`),
  ADD CONSTRAINT `prospects_ibfk_3` FOREIGN KEY (`modele_id`) REFERENCES `modeles` (`id`),
  ADD CONSTRAINT `prospects_ibfk_4` FOREIGN KEY (`version_id`) REFERENCES `versions` (`id`),
  ADD CONSTRAINT `prospects_ibfk_5` FOREIGN KEY (`couleur_id`) REFERENCES `couleurs` (`id`),
  ADD CONSTRAINT `prospects_ibfk_6` FOREIGN KEY (`interieur_id`) REFERENCES `interieurs` (`id`),
  ADD CONSTRAINT `prospects_ibfk_7` FOREIGN KEY (`motorisation_id`) REFERENCES `motorisations` (`id`),
  ADD CONSTRAINT `prospects_ibfk_8` FOREIGN KEY (`financement_id`) REFERENCES `financements` (`id`),
  ADD CONSTRAINT `prospects_ibfk_9` FOREIGN KEY (`canal_id`) REFERENCES `canaux` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
