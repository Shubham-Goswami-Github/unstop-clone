-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 08, 2025 at 08:23 AM
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
-- Database: `unstopdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add career purpose', 7, 'add_careerpurpose'),
(26, 'Can change career purpose', 7, 'change_careerpurpose'),
(27, 'Can delete career purpose', 7, 'delete_careerpurpose'),
(28, 'Can view career purpose', 7, 'view_careerpurpose'),
(29, 'Can add candidate profile', 8, 'add_candidateprofile'),
(30, 'Can change candidate profile', 8, 'change_candidateprofile'),
(31, 'Can delete candidate profile', 8, 'delete_candidateprofile'),
(32, 'Can view candidate profile', 8, 'view_candidateprofile'),
(33, 'Can add school', 9, 'add_school'),
(34, 'Can change school', 9, 'change_school'),
(35, 'Can delete school', 9, 'delete_school'),
(36, 'Can view school', 9, 'view_school');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `candidateprofile`
--

CREATE TABLE `candidateprofile` (
  `id` int(11) NOT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `password` varchar(128) DEFAULT NULL,
  `agreed_info` tinyint(1) DEFAULT 0,
  `stay_in_loop` tinyint(1) DEFAULT 0,
  `user_type` varchar(20) DEFAULT NULL,
  `school_name` varchar(150) DEFAULT NULL,
  `current_class` int(11) DEFAULT NULL,
  `school_city` varchar(100) DEFAULT NULL,
  `domain` varchar(100) DEFAULT NULL,
  `course_name` varchar(150) DEFAULT NULL,
  `start_year` varchar(10) DEFAULT NULL,
  `end_year` varchar(10) DEFAULT NULL,
  `college_name` varchar(150) DEFAULT NULL,
  `college_city` varchar(100) DEFAULT NULL,
  `experience_years` varchar(10) DEFAULT NULL,
  `current_job_role` varchar(100) DEFAULT NULL,
  `current_company` varchar(150) DEFAULT NULL,
  `job_start_year` varchar(10) DEFAULT NULL,
  `job_end_year` varchar(10) DEFAULT NULL,
  `job_city` varchar(100) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `careerpurpose`
--

CREATE TABLE `careerpurpose` (
  `id` int(11) NOT NULL,
  `candidate_id` int(11) DEFAULT NULL,
  `purpose` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(8, 'mainapp', 'candidateprofile'),
(7, 'mainapp', 'careerpurpose'),
(9, 'mainapp', 'school'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-06-27 07:19:58.650362'),
(2, 'auth', '0001_initial', '2025-06-27 07:19:59.494594'),
(3, 'admin', '0001_initial', '2025-06-27 07:19:59.768571'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-06-27 07:19:59.785024'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-06-27 07:19:59.799697'),
(6, 'contenttypes', '0002_remove_content_type_name', '2025-06-27 07:19:59.986439'),
(7, 'auth', '0002_alter_permission_name_max_length', '2025-06-27 07:20:00.101251'),
(8, 'auth', '0003_alter_user_email_max_length', '2025-06-27 07:20:00.174186'),
(9, 'auth', '0004_alter_user_username_opts', '2025-06-27 07:20:00.195210'),
(10, 'auth', '0005_alter_user_last_login_null', '2025-06-27 07:20:00.308221'),
(11, 'auth', '0006_require_contenttypes_0002', '2025-06-27 07:20:00.311248'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2025-06-27 07:20:00.330537'),
(13, 'auth', '0008_alter_user_username_max_length', '2025-06-27 07:20:00.343771'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2025-06-27 07:20:00.376927'),
(15, 'auth', '0010_alter_group_name_max_length', '2025-06-27 07:20:00.391595'),
(16, 'auth', '0011_update_proxy_permissions', '2025-06-27 07:20:00.408630'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2025-06-27 07:20:00.435269'),
(18, 'sessions', '0001_initial', '2025-06-27 07:20:00.482390'),
(19, 'mainapp', '0001_initial', '2025-07-01 06:54:49.326442'),
(20, 'mainapp', '0002_school', '2025-07-07 05:42:06.974792');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_candidateprofile`
--

CREATE TABLE `mainapp_candidateprofile` (
  `id` bigint(20) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `password` varchar(128) NOT NULL,
  `agreed_info` tinyint(1) NOT NULL,
  `stay_in_loop` tinyint(1) NOT NULL,
  `user_type` varchar(20) NOT NULL,
  `current_class` int(11) DEFAULT NULL,
  `school_city` varchar(100) DEFAULT NULL,
  `domain` varchar(100) DEFAULT NULL,
  `course_name` varchar(150) DEFAULT NULL,
  `start_year` varchar(10) DEFAULT NULL,
  `end_year` varchar(10) DEFAULT NULL,
  `college_city` varchar(100) DEFAULT NULL,
  `experience_years` varchar(10) DEFAULT NULL,
  `current_job_role` varchar(100) DEFAULT NULL,
  `job_start_year` varchar(10) DEFAULT NULL,
  `job_end_year` varchar(10) DEFAULT NULL,
  `job_city` varchar(100) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `school_id` bigint(20) DEFAULT NULL,
  `college_id` bigint(20) DEFAULT NULL,
  `company_id` bigint(20) DEFAULT NULL,
  `school_name` varchar(150) DEFAULT NULL,
  `college_name` varchar(150) DEFAULT NULL,
  `current_company` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mainapp_candidateprofile`
--

INSERT INTO `mainapp_candidateprofile` (`id`, `first_name`, `last_name`, `email`, `phone`, `gender`, `password`, `agreed_info`, `stay_in_loop`, `user_type`, `current_class`, `school_city`, `domain`, `course_name`, `start_year`, `end_year`, `college_city`, `experience_years`, `current_job_role`, `job_start_year`, `job_end_year`, `job_city`, `created_at`, `school_id`, `college_id`, `company_id`, `school_name`, `college_name`, `current_company`) VALUES
(52, 'Shubham', 'Das Goswami', 'Shubhamsuraj8990@gmail.com', '7759995373', 'Male', 'pbkdf2_sha256$600000$lXfmjKeQgpAuAq69QSY8yC$lgm27t3KME35q2mLPMh/c0+6rOqkhPXxIfsxhrSTgUQ=', 1, 1, 'college', NULL, '', 'Engineering', 'MCA', '2020', '2023', 'Ranchi', '', '', '', '', '', '2025-07-07 05:10:41.336159', NULL, NULL, NULL, NULL, NULL, NULL),
(53, 'Shubham', 'Das Goswami', 'Admintttt@gmail.com', '07759995373', 'Male', 'pbkdf2_sha256$600000$wiqK8e1mttqdKY88PxF3FM$yyuyVZAlMczhS6ulSyNJniN5PYoY8MGq+n1im3SIefA=', 1, 1, 'school', NULL, NULL, '', '', '', '', NULL, '', '', '', '', '', '2025-07-07 09:57:25.882848', NULL, NULL, NULL, 'St. Xavier\'s High School', '', ''),
(54, 'Shubham', 'Das Goswami', 's@gmail.com', '07759995373', 'Male', 'pbkdf2_sha256$600000$OYYXb2k7Ra9pS5zeex8Z6y$ZKenhL3Loec99VDQEHJd4Tx6SANkAyTKpzEptHEheP0=', 1, 1, 'school', NULL, NULL, '', '', '', '', NULL, '', '', '', '', '', '2025-07-07 10:00:46.131848', NULL, NULL, NULL, 'Bishop Cotton Boys\' School', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_careerpurpose`
--

CREATE TABLE `mainapp_careerpurpose` (
  `id` bigint(20) NOT NULL,
  `purpose` varchar(50) NOT NULL,
  `candidate_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mainapp_careerpurpose`
--

INSERT INTO `mainapp_careerpurpose` (`id`, `purpose`, `candidate_id`) VALUES
(6, 'to_find_a_job', 52),
(7, 'to_host_an_event', 53),
(8, 'to_find_a_job', 54);

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_college`
--

CREATE TABLE `mainapp_college` (
  `id` bigint(20) NOT NULL,
  `name` varchar(150) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `contact_number` varchar(20) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `is_approved` tinyint(1) NOT NULL,
  `domains_accepted` longtext DEFAULT NULL,
  `courses_accepted` longtext DEFAULT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mainapp_college`
--

INSERT INTO `mainapp_college` (`id`, `name`, `address`, `city`, `contact_number`, `email`, `is_approved`, `domains_accepted`, `courses_accepted`, `created_at`) VALUES
(1, 'Sarala Birla University', 'Ranchi-Purulia Road, Ara, Ranchi', 'Ranchi', '06512222333', 'info@sbu.ac.in', 1, '[\"Engineering\", \"Management\"]', '[\"B.Tech\", \"MBA\"]', '2025-07-07 13:51:51.681584'),
(2, 'Usha Martin University', 'Near Hardag, Lalgutwa, Ranchi', 'Ranchi', '06512334455', 'admission@umu.ac.in', 1, '[\"Science\", \"Arts\"]', '[\"B.Sc\", \"BA\"]', '2025-07-07 13:51:51.681584'),
(3, 'Delhi Technological University', 'Bawana Road, Delhi', 'Delhi', '01127871018', 'contact@dtu.ac.in', 1, '[\"Engineering\"]', '[\"B.Tech\", \"M.Tech\"]', '2025-07-07 13:51:51.681584'),
(4, 'Indian Institute of Technology Bombay', 'Powai', 'Mumbai', '02225722545', 'iitb@iitb.ac.in', 1, '[\"Engineering\", \"Science\"]', '[\"B.Tech\", \"PhD\"]', '2025-07-07 13:51:51.681584'),
(5, 'Lovely Professional University', 'Jalandhar-Delhi G.T. Road', 'Phagwara', '18001024431', 'admission@lpu.in', 1, '[\"Engineering\", \"Business\"]', '[\"B.Tech\", \"MBA\"]', '2025-07-07 13:51:51.681584'),
(6, 'SRM Institute of Science and Technology', 'Kattankulathur', 'Chennai', '04427455510', 'srm@srmist.edu.in', 1, '[\"Engineering\", \"Law\"]', '[\"B.Tech\", \"LLB\"]', '2025-07-07 13:51:51.681584'),
(7, 'Amity University', 'Sector 125', 'Noida', '01202443971', 'info@amity.edu', 1, '[\"Management\", \"Commerce\"]', '[\"MBA\", \"B.Com\"]', '2025-07-07 13:51:51.681584'),
(8, 'Christ University', 'Hosur Road', 'Bangalore', '08040129100', 'admissions@christuniversity.in', 1, '[\"Humanities\", \"Law\"]', '[\"BA\", \"LLB\"]', '2025-07-07 13:51:51.681584'),
(9, 'Manipal University', 'Madhav Nagar', 'Manipal', '08202572201', 'admission@manipal.edu', 1, '[\"Engineering\", \"Medicine\"]', '[\"B.Tech\", \"MBBS\"]', '2025-07-07 13:51:51.681584'),
(10, 'Banaras Hindu University', 'Ajagara', 'Varanasi', '05422367000', 'info@bhu.ac.in', 1, '[\"Science\", \"Arts\"]', '[\"M.Sc\", \"BA\"]', '2025-07-07 13:51:51.681584'),
(11, 'Jadavpur University', '188, Raja S.C. Mallick Rd', 'Kolkata', '03324146666', 'contact@jaduniv.edu.in', 1, '[\"Engineering\", \"Arts\"]', '[\"B.Tech\", \"BA\"]', '2025-07-07 13:51:51.681584'),
(12, 'Sharda University', 'Knowledge Park III', 'Greater Noida', '01204356789', 'info@sharda.ac.in', 1, '[\"Business\", \"Pharmacy\"]', '[\"MBA\", \"B.Pharm\"]', '2025-07-07 13:51:51.681584'),
(13, 'Chandigarh University', 'NH-95 Chandigarh-Ludhiana Highway', 'Mohali', '01604510100', 'cu@cumail.in', 1, '[\"Engineering\", \"Hospitality\"]', '[\"B.Tech\", \"BHMCT\"]', '2025-07-07 13:51:51.681584'),
(14, 'Graphic Era University', 'Bell Road', 'Dehradun', '18001805555', 'admissions@geu.ac.in', 1, '[\"Engineering\", \"Management\"]', '[\"B.Tech\", \"MBA\"]', '2025-07-07 13:51:51.681584'),
(15, 'Galgotias University', 'Yamuna Expressway', 'Greater Noida', '01202391111', 'info@galgotiasuniversity.edu.in', 1, '[\"Engineering\", \"Law\"]', '[\"B.Tech\", \"LLB\"]', '2025-07-07 13:51:51.681584'),
(16, 'Kalinga Institute of Industrial Technology', 'Patia', 'Bhubaneswar', '06742472232', 'admission@kiit.ac.in', 1, '[\"Engineering\", \"Dental\"]', '[\"B.Tech\", \"BDS\"]', '2025-07-07 13:51:51.681584'),
(17, 'Chitkara University', 'Chandigarh-Patiala National Highway', 'Rajpura', '01762507052', 'info@chitkara.edu.in', 1, '[\"Business\", \"Pharmacy\"]', '[\"MBA\", \"B.Pharm\"]', '2025-07-07 13:51:51.681584'),
(18, 'Vellore Institute of Technology', 'Katpadi', 'Vellore', '04162201999', 'admission@vit.ac.in', 1, '[\"Engineering\", \"Architecture\"]', '[\"B.Tech\", \"B.Arch\"]', '2025-07-07 13:51:51.681584'),
(19, 'MIT World Peace University', 'Paud Road', 'Pune', '02071177104', 'mitwpu@mitwpu.edu.in', 1, '[\"Engineering\", \"Political Science\"]', '[\"B.Tech\", \"BA\"]', '2025-07-07 13:51:51.681584'),
(20, 'Presidency University', 'Itgalpur Rajanakunte', 'Bangalore', '08049122222', 'info@presidencyuniversity.in', 1, '[\"Law\", \"Commerce\"]', '[\"LLB\", \"B.Com\"]', '2025-07-07 13:51:51.681584');

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_company`
--

CREATE TABLE `mainapp_company` (
  `id` bigint(20) NOT NULL,
  `name` varchar(150) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `contact_number` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `is_approved` tinyint(1) DEFAULT 0,
  `created_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mainapp_company`
--

INSERT INTO `mainapp_company` (`id`, `name`, `address`, `city`, `contact_number`, `email`, `is_approved`, `created_at`) VALUES
(1, 'TechNova Pvt Ltd', '123 Silicon Street', 'Bangalore', '9876543210', 'hr@technova.com', 1, '2025-07-07 13:49:33'),
(2, 'Infoway Solutions', '45 Park Avenue', 'Hyderabad', '9845012345', 'contact@infoway.com', 1, '2025-07-07 13:49:33'),
(3, 'Coders Arena', '78 Code Blvd', 'Pune', '9012345678', 'jobs@codersarena.in', 0, '2025-07-07 13:49:33'),
(4, 'Bright Minds Inc.', '23 Innovation Road', 'Delhi', '9988776655', 'recruit@brightminds.com', 1, '2025-07-07 13:49:33'),
(5, 'DataNest Technologies', '67 AI Street', 'Chennai', '8899776655', 'careers@datanest.ai', 1, '2025-07-07 13:49:33'),
(6, 'Skyline Infotech', '101 Cloud Lane', 'Mumbai', '9123456789', 'info@skylineinfotech.com', 0, '2025-07-07 13:49:33'),
(7, 'NextGen Softwares', '12 Future Park', 'Noida', '9871234567', 'support@nextgensoft.com', 1, '2025-07-07 13:49:33'),
(8, 'AlphaByte Solutions', '90 Digital Drive', 'Kolkata', '9765432100', 'alpha@alphabyte.com', 1, '2025-07-07 13:49:33'),
(9, 'GreenPixel Pvt Ltd', '33 Design Street', 'Ahmedabad', '9678901234', 'team@greenpixel.co.in', 0, '2025-07-07 13:49:33'),
(10, 'Quantum Core', '77 Quantum Road', 'Jaipur', '9321456789', 'admin@quantumcore.com', 1, '2025-07-07 13:49:33'),
(11, 'Wipro', 'Ranchi', 'Ranchi', '7759995373', 'wip@gmail.com', 1, '2025-07-07 09:10:08');

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_school`
--

CREATE TABLE `mainapp_school` (
  `id` bigint(20) NOT NULL,
  `name` varchar(150) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `contact_number` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `is_approved` tinyint(1) DEFAULT 0,
  `created_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mainapp_school`
--

INSERT INTO `mainapp_school` (`id`, `name`, `address`, `city`, `contact_number`, `email`, `is_approved`, `created_at`) VALUES
(1, 'Delhi Public School', 'Sector 45', 'Gurgaon', '9810012345', 'info@dpsgurgaon.org', 1, '2025-07-07 13:53:29'),
(2, 'The Shri Ram School', 'D-3 Street, Vasant Vihar', 'Delhi', '9876543210', 'contact@tsrs.org', 1, '2025-07-07 13:53:29'),
(3, 'La Martiniere for Boys', '11 Loudon Street', 'Kolkata', '9830011122', 'admin@lamartiniereschool.in', 1, '2025-07-07 13:53:29'),
(4, 'St. Xavier\'s High School', 'East Boring Canal Road', 'Patna', '9304567890', 'xavierspatna@gmail.com', 1, '2025-07-07 13:53:29'),
(5, 'Loreto Convent School', 'Shivpuri', 'Ranchi', '9638527410', 'loreto.ranchi@gmail.com', 1, '2025-07-07 13:53:29'),
(6, 'DAV Public School', 'Sector-14', 'Faridabad', '9587812345', 'dav14@davmail.com', 1, '2025-07-07 13:53:29'),
(7, 'Bishop Cotton Boys\' School', 'St Mark\'s Road', 'Bangalore', '9448822100', 'office@bishopcottonboysschool.edu.in', 1, '2025-07-07 13:53:29'),
(8, 'Modern School', 'Barakhamba Road', 'Delhi', '9990023456', 'modern@modernschool.edu.in', 1, '2025-07-07 13:53:29'),
(9, 'National Public School', 'Indiranagar', 'Bangalore', '8884455667', 'info@npsinr.com', 1, '2025-07-07 13:53:29'),
(10, 'St. Michael\'s High School', 'Digha Ghat', 'Patna', '9304001122', 'stmichaelspatna@gmail.com', 1, '2025-07-07 13:53:29'),
(11, 'Don Bosco School', 'Liluah', 'Howrah', '9830123456', 'info@donboscoliluah.org', 1, '2025-07-07 13:53:29'),
(12, 'Ryan International School', 'Kandivali East', 'Mumbai', '9819876543', 'ryan.kandivali@ryanschools.in', 1, '2025-07-07 13:53:29'),
(13, 'Birla High School', 'Moira Street', 'Kolkata', '9477856341', 'birla@bhs.in', 1, '2025-07-07 13:53:29'),
(14, 'St. Karen\'s Secondary School', 'Gola Road', 'Patna', '7765432187', 'stkarenspatna@gmail.com', 1, '2025-07-07 13:53:29'),
(15, 'Cambridge School', 'Srinivaspuri', 'Delhi', '9090909090', 'cambridge@srinivaspuri.org', 1, '2025-07-07 13:53:29'),
(16, 'Doon School', 'Mall Road', 'Dehradun', '8888999911', 'info@doonschool.com', 1, '2025-07-07 13:53:29'),
(17, 'Springdales School', 'Pusa Road', 'Delhi', '9012345678', 'springdales@school.org', 1, '2025-07-07 13:53:29'),
(18, 'St. Thomas School', 'Dhurwa', 'Ranchi', '7998887766', 'stthomasranchi@gmail.com', 1, '2025-07-07 13:53:29'),
(19, 'Sapphire International School', 'Hardag', 'Ranchi', '9123456723', 'info@sapphire.ac.in', 1, '2025-07-07 13:53:29'),
(20, 'Vikas Vidyalaya', 'Neori Vikas', 'Ranchi', '9431132345', 'vikasvidyalaya@school.in', 1, '2025-07-07 13:53:29');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `candidateprofile`
--
ALTER TABLE `candidateprofile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `careerpurpose`
--
ALTER TABLE `careerpurpose`
  ADD PRIMARY KEY (`id`),
  ADD KEY `candidate_id` (`candidate_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `mainapp_candidateprofile`
--
ALTER TABLE `mainapp_candidateprofile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `fk_candidate_school` (`school_id`),
  ADD KEY `fk_candidate_college` (`college_id`),
  ADD KEY `fk_candidate_company` (`company_id`);

--
-- Indexes for table `mainapp_careerpurpose`
--
ALTER TABLE `mainapp_careerpurpose`
  ADD PRIMARY KEY (`id`),
  ADD KEY `mainapp_careerpurpos_candidate_id_9b1216b0_fk_mainapp_c` (`candidate_id`);

--
-- Indexes for table `mainapp_college`
--
ALTER TABLE `mainapp_college`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `mainapp_company`
--
ALTER TABLE `mainapp_company`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `mainapp_school`
--
ALTER TABLE `mainapp_school`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `candidateprofile`
--
ALTER TABLE `candidateprofile`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `careerpurpose`
--
ALTER TABLE `careerpurpose`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `mainapp_candidateprofile`
--
ALTER TABLE `mainapp_candidateprofile`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;

--
-- AUTO_INCREMENT for table `mainapp_careerpurpose`
--
ALTER TABLE `mainapp_careerpurpose`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `mainapp_college`
--
ALTER TABLE `mainapp_college`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `mainapp_company`
--
ALTER TABLE `mainapp_company`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `mainapp_school`
--
ALTER TABLE `mainapp_school`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `careerpurpose`
--
ALTER TABLE `careerpurpose`
  ADD CONSTRAINT `careerpurpose_ibfk_1` FOREIGN KEY (`candidate_id`) REFERENCES `candidateprofile` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `mainapp_candidateprofile`
--
ALTER TABLE `mainapp_candidateprofile`
  ADD CONSTRAINT `fk_candidate_college` FOREIGN KEY (`college_id`) REFERENCES `mainapp_college` (`id`) ON DELETE SET NULL,
  ADD CONSTRAINT `fk_candidate_company` FOREIGN KEY (`company_id`) REFERENCES `mainapp_company` (`id`) ON DELETE SET NULL,
  ADD CONSTRAINT `fk_candidate_school` FOREIGN KEY (`school_id`) REFERENCES `mainapp_school` (`id`) ON DELETE SET NULL,
  ADD CONSTRAINT `fk_candidateprofile_college` FOREIGN KEY (`college_id`) REFERENCES `mainapp_college` (`id`) ON DELETE SET NULL,
  ADD CONSTRAINT `fk_company` FOREIGN KEY (`company_id`) REFERENCES `mainapp_company` (`id`),
  ADD CONSTRAINT `fk_school` FOREIGN KEY (`school_id`) REFERENCES `mainapp_school` (`id`);

--
-- Constraints for table `mainapp_careerpurpose`
--
ALTER TABLE `mainapp_careerpurpose`
  ADD CONSTRAINT `mainapp_careerpurpos_candidate_id_9b1216b0_fk_mainapp_c` FOREIGN KEY (`candidate_id`) REFERENCES `mainapp_candidateprofile` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
