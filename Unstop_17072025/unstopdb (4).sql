-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 17, 2025 at 09:25 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

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
(36, 'Can view school', 9, 'view_school'),
(37, 'Can add college', 10, 'add_college'),
(38, 'Can change college', 10, 'change_college'),
(39, 'Can delete college', 10, 'delete_college'),
(40, 'Can view college', 10, 'view_college'),
(41, 'Can add company', 11, 'add_company'),
(42, 'Can change company', 11, 'change_company'),
(43, 'Can delete company', 11, 'delete_company'),
(44, 'Can view company', 11, 'view_company'),
(45, 'Can add internship', 12, 'add_internship'),
(46, 'Can change internship', 12, 'change_internship'),
(47, 'Can delete internship', 12, 'delete_internship'),
(48, 'Can view internship', 12, 'view_internship'),
(49, 'Can add job', 13, 'add_job'),
(50, 'Can change job', 13, 'change_job'),
(51, 'Can delete job', 13, 'delete_job'),
(52, 'Can view job', 13, 'view_job'),
(53, 'Can add competition', 14, 'add_competition'),
(54, 'Can change competition', 14, 'change_competition'),
(55, 'Can delete competition', 14, 'delete_competition'),
(56, 'Can view competition', 14, 'view_competition');

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
-- Table structure for table `competitions`
--

CREATE TABLE `competitions` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `title` varchar(200) NOT NULL,
  `host_org` varchar(150) NOT NULL,
  `category` enum('Free','Paid') NOT NULL,
  `fee_amount` decimal(8,2) DEFAULT 0.00,
  `competition_type` enum('Case‑Study','Hackathon','Quiz','Idea‑Thon','Other') DEFAULT 'Other',
  `mode` enum('Online','Offline','Hybrid') DEFAULT 'Online',
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `prize_pool` varchar(120) DEFAULT NULL,
  `team_size` varchar(20) DEFAULT 'Individual',
  `registration_deadline` date DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp()
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
(10, 'mainapp', 'college'),
(11, 'mainapp', 'company'),
(14, 'mainapp', 'competition'),
(12, 'mainapp', 'internship'),
(13, 'mainapp', 'job'),
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
(20, 'mainapp', '0002_school', '2025-07-07 05:42:06.974792'),
(21, 'mainapp', '0002_job', '2025-07-15 08:22:37.359730'),
(22, 'mainapp', '0003_alter_job_category', '2025-07-15 08:43:11.380538'),
(23, 'mainapp', '0004_competition', '2025-07-16 10:36:33.664363'),
(24, 'mainapp', '0005_alter_competition_competition_type', '2025-07-16 11:00:17.476946');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('i23tmlzj0vue1kkyqb99ck00kbh19oli', '.eJyrVkpOzEvJTEksSY3PTFGysjDVQRLJS8xNVbJSCihKLEtNzVNQQpZLzU3MzAFKFkAkHdJBfL3k_FwUVQUZ-XkgI8wNjIHA0MjAVKkWAChgJsI:1uaARM:T8vsdVYE_k8vJIaYMtMiQlPbqMergOCT1b9gSQ8qP8M', '2025-07-25 09:53:12.521179'),
('yl1omdcomafwvlbv2fo0dh7uezkgmjt2', '.eJyrVkpOzEvJTEksSY3PTFGysjDTQRLJS8xNVbJSCkrMUkIWTs1NzMwBihclZjmkg9h6yfm5KCoKMvLzQDrNzU0tLS1Njc2NlWoBt-4jYA:1ubyAl:2psimVMSK0cfs3oia95nqdYfZmPJQ83lHJ75rTNEYyo', '2025-07-30 09:11:31.905219');

-- --------------------------------------------------------

--
-- Table structure for table `internships`
--

CREATE TABLE `internships` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `title` varchar(200) NOT NULL,
  `company_name` varchar(150) NOT NULL,
  `domain` varchar(100) NOT NULL,
  `mode` enum('Online','Offline','Hybrid') DEFAULT 'Online',
  `category` enum('Paid','Unpaid') NOT NULL,
  `stipend_amount` decimal(10,2) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `duration_weeks` int(11) DEFAULT NULL,
  `location` varchar(120) DEFAULT NULL,
  `application_link` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp()
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
(77, 'Shubham', 'Das Goswami', 'shubhamsuraj8990@gmail.com', '07759995373', 'Male', 'pbkdf2_sha256$600000$uVvNHzP09cGaNGKEb7jfWM$Zw0cxbpSXwkokGUnLlA1niHibFzyst650tv3FB46yJE=', 1, 1, 'school', 12, 'Patna', '', '', '', '', '', '', '', '', '', '', '2025-07-08 15:25:44.450270', 4, NULL, NULL, 'St. Xavier\'s High School', '', ''),
(78, 'Akash ', 'Thakur', 'akash879@gmail.com', '7759995373', 'Male', 'pbkdf2_sha256$600000$OpbyTPfw3IRCS0zAfCq44w$vH40hoYyaT0xsN/HgrZJD8otQbeIMrxU/OcqFOtKmNk=', 1, 1, 'college', NULL, '', 'Engineering', 'B.Tech', '2021', '2024', 'Bhubaneswar', '', '', '', '', '', '2025-07-08 15:26:35.367850', NULL, 16, NULL, '', 'Kalinga Institute of Industrial Technology', ''),
(79, 'Neeraj', 'Kumar', 'neeraj8990@gmail.com', '77599953373', 'Male', 'pbkdf2_sha256$600000$nTDQTaxUxr9AZVA3h1dfeZ$rBEsrm3uP+qWFKJs9s1FSM3SZe7xDfPbqUkTwE3k1vI=', 1, 1, 'fresher', NULL, '', 'Commerce', 'MBA', '2025', '2022', 'Rajpura', '', '', '', '', '', '2025-07-08 15:27:27.898445', NULL, 17, NULL, '', 'Chitkara University', ''),
(80, 'Ajay', 'Kumar', 'ajay@gmail.com', '7759995373', 'Male', 'pbkdf2_sha256$600000$91nCbB9X5iv1o2qtJDkk12$NWrANmbX8IKK+NEKaCLNkEyuNVR6Gg/HXLVeguvhRks=', 1, 1, 'professional', NULL, '', '', '', '', '', '', 'mca', 'ASSISTANT', '2020', '2026', 'Kolkata', '2025-07-08 15:28:05.512498', NULL, NULL, 8, '', '', 'AlphaByte Solutions'),
(81, 'Yashansi', 'Priya', 'yashansi@gmail.com', '7759995373', 'Male', 'pbkdf2_sha256$600000$OptmNhOpblVzF63Vu7R9Sm$Mc0r8dRMLpg49m9fXNyAeTjdWLfpOUd0++O5nMGfLZA=', 1, 1, 'fresher', NULL, '', 'Medicine', 'BA', '2024', '2027', 'Pune', '', '', '', '', '', '2025-07-08 16:32:04.023763', NULL, 19, NULL, '', 'MIT World Peace University', ''),
(82, 'arjun', 'kumar', 'arjun@gmail.com', '7759995373', 'Male', 'pbkdf2_sha256$600000$e9AgNMRGWhY4Wig2sIXF6G$sz+BuZbPmo6EvpwzqYf2cOmn4icgvztdXDiuw+4OrN8=', 1, 1, 'college', NULL, '', 'Arts', 'MBA', '2002', '2023', 'Rajpura', '', '', '', '', '', '2025-07-08 16:45:07.521363', NULL, 17, NULL, '', 'Chitkara University', ''),
(83, 'Shubham', 'Das Goswami', 'A3dmin@gmail.com', '07759995373', 'Male', 'pbkdf2_sha256$600000$40UmPIQXpSqciWAXAF8zCv$xJjQZaGAtbXMuiLzUrNhpRI1swkzFHTMizqCIAMH7ig=', 1, 1, 'school', 3, 'Patna', '', '', '', '', '', '', '', '', '', '', '2025-07-09 06:38:25.714801', 14, NULL, NULL, 'St. Karen\'s Secondary School', '', ''),
(84, 'Shubham', 'Das Goswami', 'shubhamr@gmail.com', '07759995373', 'Male', 'pbkdf2_sha256$600000$7vbfoecqm4GJkcmyrjiEtT$cozTl5SZjeNd/dZZq3VpyP5o4i5jVuXa4DksMxmcnBM=', 1, 1, 'school', 12, 'Ranchi', '', '', '', '', '', '', '', '', '', '', '2025-07-10 08:16:30.971157', 18, NULL, NULL, 'St. Thomas School', '', ''),
(85, 'Praveen ', 'Kumar', 'praveen@gmail.com', '7033331205', 'Male', 'pbkdf2_sha256$600000$OP4qKuH0svh4QiRGZkijZf$5fr1/c1o7Pi7fl4UjpRkc4nmO1bBLz/qTW2h9cIDWGQ=', 1, 1, 'college', NULL, '', 'Business', 'MBA', '2025', '2026', 'Noida', '', '', '', '', '', '2025-07-10 09:38:50.498280', NULL, 7, NULL, '', 'Amity University', ''),
(86, 'Raj', 'Kumar', 'raj@gmail.com', '7759995373', 'Male', 'pbkdf2_sha256$600000$q9ot84pU2gMA4Wladh1yUw$s3zTwi7asW983Ys4C5arvBm24JYDhh3fnDhfS30UA3E=', 1, 1, 'professional', NULL, '', 'Architecture', '', '', '', 'Phagwara', '4', 'Engineer', '2020', '2025', 'Noida', '2025-07-16 09:11:09.649263', 15, 5, 7, '', '', 'NextGen Softwares');

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
(29, 'compete_&_upskill', 77),
(30, 'to_find_a_job', 78),
(31, 'to_find_a_job', 79),
(32, 'to_be_a_mentor', 80),
(33, 'to_host_an_event', 81),
(34, 'to_be_a_mentor', 82),
(35, 'to_find_a_job', 83),
(36, 'to_find_a_job', 84),
(37, 'to_find_a_job', 85),
(38, 'to_be_a_mentor', 86);

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
(3, 'Coders Arena', '78 Code Blvd', 'Pune', '9012345678', 'jobs@codersarena.in', 1, '2025-07-07 13:49:33'),
(4, 'Bright Minds Inc.', '23 Innovation Road', 'Delhi', '9988776655', 'recruit@brightminds.com', 1, '2025-07-07 13:49:33'),
(5, 'DataNest Technologies', '67 AI Street', 'Chennai', '8899776655', 'careers@datanest.ai', 1, '2025-07-07 13:49:33'),
(6, 'Skyline Infotech', '101 Cloud Lane', 'Mumbai', '9123456789', 'info@skylineinfotech.com', 1, '2025-07-07 13:49:33'),
(7, 'NextGen Softwares', '12 Future Park', 'Noida', '9871234567', 'support@nextgensoft.com', 1, '2025-07-07 13:49:33'),
(8, 'AlphaByte Solutions', '90 Digital Drive', 'Kolkata', '9765432100', 'alpha@alphabyte.com', 1, '2025-07-07 13:49:33'),
(9, 'GreenPixel Pvt Ltd', '33 Design Street', 'Ahmedabad', '9678901234', 'team@greenpixel.co.in', 0, '2025-07-07 13:49:33'),
(10, 'Quantum Core', '77 Quantum Road', 'Jaipur', '9321456789', 'admin@quantumcore.com', 1, '2025-07-07 13:49:33'),
(11, 'Wipro', 'Ranchi', 'Ranchi', '7759995373', 'wip@gmail.com', 1, '2025-07-07 09:10:08'),
(12, 'Wipro Elite', 'Wipro Elite, Bangalore', 'Ranchi', '7759995373', 'Shubhamsuraj8990@gmail.com', 1, '2025-07-09 08:33:42');

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_competition`
--

CREATE TABLE `mainapp_competition` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `host_org` varchar(150) NOT NULL,
  `category` varchar(4) NOT NULL,
  `fee_amount` decimal(8,2) NOT NULL,
  `competition_type` varchar(20) NOT NULL,
  `mode` varchar(7) NOT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `prize_pool` varchar(120) DEFAULT NULL,
  `team_size` varchar(20) NOT NULL,
  `registration_deadline` date DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mainapp_competition`
--

INSERT INTO `mainapp_competition` (`id`, `title`, `host_org`, `category`, `fee_amount`, `competition_type`, `mode`, `start_date`, `end_date`, `prize_pool`, `team_size`, `registration_deadline`, `created_at`, `updated_at`) VALUES
(1, 'AI Challenge 2025', 'TechFest IIT', 'Free', 0.00, 'Hackathon', 'Online', '2025-08-01', '2025-08-10', '₹1,00,000', 'Team of 3', '2025-07-31', '2025-07-16 10:50:44.001821', '2025-07-16 10:50:44.001821'),
(2, 'AI Innovation Challenge', 'NVIDIA', 'Free', 0.00, 'Hackathons', 'Online', '2025-08-01', '2025-08-10', '₹1,00,000', 'Team of 3', '2025-07-25', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(3, 'National Coding League', 'CodeChef', 'Paid', 100.00, 'Competitions', 'Online', '2025-08-05', '2025-08-12', '₹50,000', 'Individual', '2025-07-28', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(4, 'Global Quiz Fest', 'Quizizz', 'Free', 0.00, 'Quizzes', 'Offline', '2025-08-03', '2025-08-03', 'Medals & Certificates', 'Team of 2', '2025-07-30', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(5, 'Smart India Hackathon', 'AICTE', 'Free', 0.00, 'Hackathons', 'Hybrid', '2025-08-10', '2025-08-15', '₹2,00,000', 'Team of 6', '2025-08-01', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(6, 'Scholar Hunt 2025', 'MHRD', 'Free', 0.00, 'Scholarships', 'Online', '2025-08-20', '2025-09-20', 'Full Tuition Fee', 'Individual', '2025-08-10', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(7, 'Women in Tech Conference', 'Google', 'Free', 0.00, 'Conferences', 'Online', '2025-08-14', '2025-08-16', NULL, 'Individual', '2025-08-05', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(8, 'Open Source Workshop', 'GitHub', 'Free', 0.00, 'Workshops', 'Online', '2025-08-08', '2025-08-09', NULL, 'Individual', '2025-07-31', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(9, 'Robotics Bootcamp', 'IIT Bombay', 'Paid', 500.00, 'Workshops', 'Offline', '2025-08-18', '2025-08-20', NULL, 'Team of 4', '2025-08-05', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(10, 'Creative Minds Fest', 'DU Cultural Committee', 'Free', 0.00, 'Cultural Events', 'Offline', '2025-08-25', '2025-08-27', 'Goodies & Vouchers', 'Team of 5', '2025-08-15', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(11, 'Data Science Showdown', 'IIT Madras', 'Paid', 250.00, 'Competitions', 'Hybrid', '2025-08-05', '2025-08-10', '₹75,000', 'Team of 3', '2025-07-29', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(12, 'Scholar Pro 2025', 'UNESCO', 'Free', 0.00, 'Scholarships', 'Online', '2025-09-01', '2025-09-30', 'International Grant', 'Individual', '2025-08-20', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(13, 'Tech Titans Hack', 'Microsoft', 'Free', 0.00, 'Hackathons', 'Online', '2025-08-10', '2025-08-12', '₹1,50,000', 'Team of 4', '2025-08-01', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(14, 'Python Coding Sprint', 'Coding Ninjas', 'Paid', 150.00, 'Competitions', 'Online', '2025-08-07', '2025-08-09', '₹30,000', 'Individual', '2025-07-31', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(15, 'National Quiz Cup', 'BYJU\'s', 'Free', 0.00, 'Quizzes', 'Online', '2025-08-11', '2025-08-11', 'Trophies', 'Team of 2', '2025-08-05', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(16, 'Cybersecurity Workshop', 'IBM', 'Free', 0.00, 'Workshops', 'Online', '2025-08-14', '2025-08-14', NULL, 'Individual', '2025-08-07', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(17, 'AI in Healthcare', 'Stanford', 'Free', 0.00, 'Conferences', 'Hybrid', '2025-08-20', '2025-08-21', NULL, 'Individual', '2025-08-10', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(18, 'Dance Battle Royale', 'Delhi Univ.', 'Paid', 300.00, 'Cultural Events', 'Offline', '2025-08-23', '2025-08-23', 'Trophy & Cash Prize', 'Team of 6', '2025-08-18', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(19, 'Hack the Valley', 'Amazon', 'Free', 0.00, 'Hackathons', 'Online', '2025-08-15', '2025-08-17', '₹1,00,000', 'Team of 4', '2025-08-05', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(20, 'Quant Masters Quiz', 'IMS', 'Paid', 100.00, 'Quizzes', 'Offline', '2025-08-12', '2025-08-12', '₹10,000', 'Individual', '2025-08-01', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(21, 'Space Science Scholarship', 'ISRO', 'Free', 0.00, 'Scholarships', 'Online', '2025-08-22', '2025-09-22', 'Stipend + Trip to ISRO', 'Individual', '2025-08-10', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(22, 'Startup Pitch Fest', 'NASSCOM', 'Free', 0.00, 'Competitions', 'Hybrid', '2025-08-25', '2025-08-26', 'Incubation + ₹50k', 'Team of 2', '2025-08-15', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(23, 'UX/UI Bootcamp', 'Adobe', 'Paid', 200.00, 'Workshops', 'Offline', '2025-08-17', '2025-08-18', NULL, 'Individual', '2025-08-05', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(24, 'Green Hack Day', 'UNEP', 'Free', 0.00, 'Hackathons', 'Online', '2025-08-06', '2025-08-07', '₹60,000', 'Team of 5', '2025-07-31', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(25, 'Art & Culture Meet', 'IGNCA', 'Free', 0.00, 'Cultural Events', 'Offline', '2025-08-26', '2025-08-27', NULL, 'Team of 3', '2025-08-15', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(26, 'NextGen TechConf', 'TCS', 'Free', 0.00, 'Conferences', 'Online', '2025-08-19', '2025-08-20', NULL, 'Individual', '2025-08-10', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(27, 'Math Marathon', 'Vidyamandir', 'Paid', 120.00, 'Quizzes', 'Offline', '2025-08-11', '2025-08-11', '₹20,000', 'Individual', '2025-08-01', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(28, 'Ethical Hacking 101', 'EC-Council', 'Paid', 250.00, 'Workshops', 'Online', '2025-08-13', '2025-08-14', NULL, 'Individual', '2025-08-03', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000'),
(29, 'Women Leaders Summit', 'UN Women', 'Free', 0.00, 'Conferences', 'Online', '2025-08-15', '2025-08-15', NULL, 'Individual', '2025-08-05', '2025-07-16 16:38:10.000000', '2025-07-16 16:38:10.000000');

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_internship`
--

CREATE TABLE `mainapp_internship` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `title` varchar(200) NOT NULL,
  `company_name` varchar(150) NOT NULL,
  `domain` varchar(100) NOT NULL,
  `mode` enum('Online','Offline','Hybrid') DEFAULT 'Online',
  `category` enum('Paid','Unpaid') NOT NULL,
  `stipend_amount` decimal(10,2) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `duration_weeks` int(11) DEFAULT NULL,
  `location` varchar(120) DEFAULT NULL,
  `application_link` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mainapp_internship`
--

INSERT INTO `mainapp_internship` (`id`, `title`, `company_name`, `domain`, `mode`, `category`, `stipend_amount`, `start_date`, `end_date`, `duration_weeks`, `location`, `application_link`, `created_at`, `updated_at`) VALUES
(3, 'Frontend Developer Intern', 'TechNova Pvt Ltd', 'SDE', 'Online', 'Paid', 8000.00, '2025-08-01', '2025-09-12', 6, NULL, 'https://technova.intern/apply', '2025-07-11 17:48:45', '2025-07-11 17:48:45'),
(4, 'HR Intern', 'PeopleFirst Solutions', 'HR', 'Offline', 'Unpaid', NULL, '2025-07-15', '2025-08-15', 4, 'Mumbai, India', 'https://peoplefirst.com/careers/hr-intern', '2025-07-11 17:48:45', '2025-07-11 17:48:45'),
(5, 'Marketing Intern', 'AdSpark Digital', 'Marketing', 'Hybrid', 'Paid', 5000.00, '2025-08-10', '2025-10-10', 8, 'Delhi, India', 'https://adspark.in/internships', '2025-07-11 17:48:45', '2025-07-11 17:48:45'),
(6, 'Data Analyst Intern', 'InsightIQ Analytics', 'Data Science', 'Online', 'Paid', 10000.00, '2025-09-01', '2025-10-27', 8, NULL, 'https://insightiq.com/jobs/data-intern', '2025-07-11 17:48:45', '2025-07-11 17:48:45'),
(7, 'UI/UX Design Intern', 'PixelFrame Studio', 'Design', 'Online', 'Unpaid', NULL, '2025-08-01', '2025-08-31', 4, NULL, 'https://pixelframe.in/uiux-intern', '2025-07-11 17:48:45', '2025-07-11 17:48:45'),
(8, 'Business Development Intern', 'StartUpXpress', 'Business', 'Hybrid', 'Paid', 6000.00, '2025-07-20', '2025-08-30', 6, 'Bangalore, India', 'https://startupxpress.com/interns', '2025-07-11 17:48:45', '2025-07-11 17:48:45'),
(9, 'Cybersecurity Intern', 'SecureNet Solutions', 'Cybersecurity', 'Online', 'Paid', 12000.00, '2025-08-05', '2025-10-05', 8, NULL, 'https://securenet.co/apply', '2025-07-11 17:48:45', '2025-07-11 17:48:45'),
(10, 'Content Writer Intern', 'WriteWise Media', 'Content Writing', 'Online', 'Unpaid', NULL, '2025-08-01', '2025-08-28', 4, NULL, 'https://writewise.com/join-us', '2025-07-11 17:48:45', '2025-07-11 17:48:45'),
(11, 'Machine Learning Intern', 'AlgoBrain AI', 'AI/ML', 'Offline', 'Paid', 15000.00, '2025-08-15', '2025-10-15', 8, 'Hyderabad, India', 'https://algobrain.ai/careers', '2025-07-11 17:48:45', '2025-07-11 17:48:45'),
(12, 'Finance Intern', 'InvestCraft Pvt Ltd', 'Finance', 'Hybrid', 'Unpaid', NULL, '2025-07-25', '2025-09-05', 6, 'Pune, India', 'https://investcraft.com/internships', '2025-07-11 17:48:45', '2025-07-11 17:48:45'),
(13, 'Web Development Intern', 'DevLabs Inc', 'SDE', 'Online', 'Paid', 7000.00, '2025-08-10', '2025-09-21', 6, NULL, 'https://devlabs.io/join', '2025-07-11 17:48:45', '2025-07-11 17:48:45'),
(14, 'Operations Intern', 'QuickKart', 'Operations', 'Offline', 'Unpaid', NULL, '2025-08-01', '2025-09-01', 4, 'Chennai, India', 'https://quickkart.com/intern-ops', '2025-07-11 17:48:45', '2025-07-11 17:48:45'),
(15, 'SEO Intern', 'RankUp Agency', 'Marketing', 'Online', 'Paid', 4000.00, '2025-08-10', '2025-09-21', 6, NULL, 'https://rankup.agency/seo-intern', '2025-07-11 17:48:45', '2025-07-11 17:48:45'),
(16, 'Game Design Intern', 'PixelPlay Games', 'Game Development', 'Hybrid', 'Paid', 9000.00, '2025-08-20', '2025-10-15', 8, 'Bangalore, India', 'https://pixelplay.games/careers', '2025-07-11 17:48:45', '2025-07-11 17:48:45'),
(17, 'Legal Intern', 'LawBridge LLP', 'Legal', 'Offline', 'Unpaid', NULL, '2025-07-15', '2025-08-30', 6, 'Delhi, India', 'https://lawbridge.in/internship', '2025-07-11 17:48:45', '2025-07-11 17:48:45'),
(18, 'UI/UX Design Intern', 'DesignNest Studios', 'UI/UX', 'Online', 'Unpaid', NULL, '2025-08-01', '2025-09-15', 6, NULL, 'https://designnest.internship/apply', '2025-07-11 21:45:10', '2025-07-11 21:45:10'),
(19, 'Game Development Intern', 'PixelPlay Games', 'Game Development', 'Offline', 'Paid', 6000.00, '2025-07-20', '2025-10-20', 12, 'Bangalore', 'https://pixelplay.jobs/game-intern', '2025-07-11 21:45:10', '2025-07-11 21:45:10'),
(20, 'Legal Research Intern', 'LexGen Advocates', 'Legal', 'Hybrid', 'Unpaid', NULL, '2025-08-05', '2025-09-25', 7, 'Delhi', 'https://lexgen.internships/apply', '2025-07-11 21:45:10', '2025-07-11 21:45:10'),
(21, 'Mechanical Engineering Intern', 'MechaCore Ltd', 'Mechanical', 'Offline', 'Paid', 7500.00, '2025-08-01', '2025-10-15', 10, 'Pune', 'https://mechacore.careers/mech-intern', '2025-07-11 21:45:10', '2025-07-11 21:45:10'),
(22, 'Sales and Outreach Intern', 'BizGrow Partners', 'Sales', 'Online', 'Paid', 5000.00, '2025-07-25', '2025-08-25', 4, NULL, 'https://bizgrow.in/sales-opportunity', '2025-07-11 21:45:10', '2025-07-11 21:45:10'),
(23, 'Social Media Intern', 'GramBoost Agency', 'Social Media', 'Online', 'Unpaid', NULL, '2025-08-10', '2025-09-30', 7, NULL, 'https://gramboost.io/join', '2025-07-11 21:45:10', '2025-07-11 21:45:10'),
(24, 'Research Assistant Intern', 'ThinkTank Global', 'Research', 'Hybrid', 'Paid', 7000.00, '2025-08-01', '2025-10-01', 8, 'Hyderabad', 'https://thinktank.org/research-opportunity', '2025-07-11 21:45:10', '2025-07-11 21:45:10'),
(25, 'Cloud Computing Intern', 'Nimbus Tech', 'Cloud Computing', 'Online', 'Paid', 9000.00, '2025-07-15', '2025-09-15', 9, NULL, 'https://nimbus.tech/cloud-intern', '2025-07-11 21:45:10', '2025-07-11 21:45:10'),
(26, 'Data Analyst Intern', 'InsightBase Inc.', 'Data Analysis', 'Offline', 'Paid', 8500.00, '2025-08-01', '2025-09-30', 8, 'Mumbai', 'https://insightbase.com/da-apply', '2025-07-11 21:45:10', '2025-07-11 21:45:10'),
(27, 'Interior Design Intern', 'SpaceCraft Studio', 'Interior Design', 'Offline', 'Unpaid', NULL, '2025-07-20', '2025-08-30', 6, 'Jaipur', 'https://spacecraftstudio.in/interns', '2025-07-11 21:45:10', '2025-07-11 21:45:10'),
(28, 'Digital Marketing Intern', 'Boostify Labs', 'Digital Marketing', 'Hybrid', 'Paid', 6000.00, '2025-08-10', '2025-10-10', 9, 'Chennai', 'https://boostifylabs.com/apply', '2025-07-11 21:45:10', '2025-07-11 21:45:10'),
(29, 'Product Management Intern', 'Innovana Tech', 'Product Management', 'Online', 'Paid', 10000.00, '2025-07-25', '2025-09-25', 8, NULL, 'https://innovana.io/product-intern', '2025-07-11 21:45:10', '2025-07-11 21:45:10'),
(30, 'Video Editing Intern', 'VidSpark Creators', 'Video Editing', 'Offline', 'Unpaid', NULL, '2025-08-01', '2025-09-01', 4, 'Noida', 'https://vidspark.in/edit-intern', '2025-07-11 21:45:10', '2025-07-11 21:45:10'),
(31, 'AI/ML Intern', 'NeuralShift AI', 'Artificial Intelligence', 'Online', 'Paid', 12000.00, '2025-07-20', '2025-10-20', 12, NULL, 'https://neuralshift.ai/internships', '2025-07-11 21:45:10', '2025-07-11 21:45:10'),
(32, 'Public Relations Intern', 'MediaNet Group', 'Public Relations', 'Hybrid', 'Unpaid', NULL, '2025-08-05', '2025-09-15', 6, 'Kolkata', 'https://medianetgrp.com/join-us', '2025-07-11 21:45:10', '2025-07-11 21:45:10'),
(33, 'Android Developer Intern', 'AppVerse Technologies', 'Android Development', 'Online', 'Paid', 8000.00, '2025-08-01', '2025-10-01', 8, NULL, 'https://appverse.in/android-intern', '2025-07-11 21:45:10', '2025-07-11 21:45:10'),
(34, 'Operations Intern', 'UrbanFleet', 'Operations', 'Offline', 'Paid', 6500.00, '2025-07-18', '2025-09-18', 8, 'Ahmedabad', 'https://urbanfleet.com/careers', '2025-07-11 21:45:10', '2025-07-11 21:45:10'),
(35, 'Fashion Design Intern', 'TrendSoul Studio', 'Fashion Design', 'Offline', 'Unpaid', NULL, '2025-08-10', '2025-09-25', 6, 'Delhi', 'https://trendsoulstudio.com/internship', '2025-07-11 21:45:10', '2025-07-11 21:45:10'),
(36, 'Business Analyst Intern', 'StratEdge Corp', 'Business Analysis', 'Hybrid', 'Paid', 9500.00, '2025-08-01', '2025-09-30', 8, 'Mumbai', 'https://stratedge.com/apply-ba', '2025-07-11 21:45:10', '2025-07-11 21:45:10'),
(37, 'Cybersecurity Intern', 'SafeGuard Systems', 'Cybersecurity', 'Online', 'Paid', 11000.00, '2025-07-25', '2025-10-25', 12, NULL, 'https://safeguardsys.io/cyber-intern', '2025-07-11 21:45:10', '2025-07-11 21:45:10'),
(38, 'Frontend Development Intern', 'CodeVista Labs', 'Frontend Development', 'Online', 'Paid', 7000.00, '2025-08-05', '2025-09-30', 8, NULL, 'https://codevista.dev/intern/frontend', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(39, 'Content Writing Intern', 'Inkspire Media', 'Content Writing', 'Hybrid', 'Unpaid', NULL, '2025-07-25', '2025-08-31', 5, 'Lucknow', 'https://inkspiremedia.com/join', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(40, 'Blockchain Intern', 'CryptoCore Pvt Ltd', 'Blockchain', 'Online', 'Paid', 10000.00, '2025-08-01', '2025-10-15', 10, NULL, 'https://cryptocore.io/internships', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(41, 'Finance Intern', 'FinEdge Corp', 'Finance', 'Offline', 'Unpaid', NULL, '2025-08-10', '2025-09-20', 6, 'Pune', 'https://finedge.interns/apply', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(42, 'Animation Intern', 'ToonForge Studios', 'Animation', 'Online', 'Paid', 5500.00, '2025-07-20', '2025-08-30', 6, NULL, 'https://toonforge.io/interns', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(43, 'HR Intern', 'TalentSphere HR', 'HR', 'Hybrid', 'Paid', 5000.00, '2025-08-01', '2025-09-15', 6, 'Bhopal', 'https://talentsphere.in/hr-apply', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(44, 'Photography Intern', 'ShutterPro Media', 'Photography', 'Offline', 'Unpaid', NULL, '2025-07-18', '2025-08-28', 6, 'Kolkata', 'https://shutterpro.in/join', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(45, 'Full Stack Intern', 'ByteBridge Ltd', 'Full Stack Development', 'Online', 'Paid', 9000.00, '2025-07-25', '2025-09-25', 8, NULL, 'https://bytebridge.com/intern/fullstack', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(46, 'Event Management Intern', 'EliteEvents Group', 'Event Management', 'Hybrid', 'Unpaid', NULL, '2025-08-05', '2025-09-05', 4, 'Indore', 'https://eliteevents.in/apply', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(47, 'Data Entry Intern', 'InfoSpark Pvt Ltd', 'Data Entry', 'Offline', 'Paid', 3000.00, '2025-07-15', '2025-08-15', 4, 'Ranchi', 'https://infospark.in/dataentry', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(48, 'AR/VR Intern', 'VirtuTech Innovations', 'AR/VR', 'Online', 'Paid', 12000.00, '2025-08-10', '2025-10-10', 9, NULL, 'https://virtutech.io/arvr-intern', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(49, 'Public Speaking Intern', 'Orator Club', 'Public Speaking', 'Offline', 'Unpaid', NULL, '2025-08-01', '2025-09-10', 6, 'Chandigarh', 'https://oratorclub.com/join', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(50, 'E-commerce Operations Intern', 'ShopCart Pvt Ltd', 'E-commerce', 'Online', 'Paid', 6000.00, '2025-07-25', '2025-09-15', 7, NULL, 'https://shopcart.in/careers', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(51, 'Customer Support Intern', 'HelpBuddy Services', 'Customer Support', 'Hybrid', 'Paid', 4000.00, '2025-08-05', '2025-09-05', 4, 'Nagpur', 'https://helpbuddy.in/internship', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(52, 'AI Research Intern', 'VisionEdge AI', 'AI Research', 'Online', 'Paid', 13000.00, '2025-08-01', '2025-10-30', 12, NULL, 'https://visionedge.ai/join', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(53, 'Data Labeling Intern', 'AnnotateX', 'Data Labeling', 'Online', 'Unpaid', NULL, '2025-08-10', '2025-09-20', 6, NULL, 'https://annotatex.com/apply', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(54, 'Web Security Intern', 'SecuWeb Inc', 'Web Security', 'Online', 'Paid', 10500.00, '2025-07-20', '2025-09-20', 8, NULL, 'https://secuweb.io/intern', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(55, 'Product Design Intern', 'ProtoNest', 'Product Design', 'Offline', 'Unpaid', NULL, '2025-08-01', '2025-09-15', 6, 'Surat', 'https://protonest.design/internship', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(56, 'Power BI Intern', 'DashBoardPro Pvt Ltd', 'Power BI', 'Hybrid', 'Paid', 8000.00, '2025-08-05', '2025-10-05', 9, 'Delhi', 'https://dashboardpro.in/apply', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(57, 'Civil Engineering Intern', 'UrbanPlan Infra', 'Civil Engineering', 'Offline', 'Paid', 9000.00, '2025-07-25', '2025-09-25', 8, 'Patna', 'https://urbanplan.in/civil-intern', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(58, 'Graphic Design Intern', 'PixelDrop Studio', 'Graphic Design', 'Online', 'Unpaid', NULL, '2025-08-01', '2025-09-01', 4, NULL, 'https://pixeldrop.design/join', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(59, 'Network Engineering Intern', 'NetSol Pvt Ltd', 'Networking', 'Offline', 'Paid', 8500.00, '2025-08-10', '2025-10-10', 9, 'Bangalore', 'https://netsol.io/internship', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(60, 'Copywriting Intern', 'AdBlend Media', 'Copywriting', 'Hybrid', 'Paid', 5500.00, '2025-08-01', '2025-09-15', 6, 'Jaipur', 'https://adblend.in/copyintern', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(61, 'Testing Intern', 'TestBench QA', 'Software Testing', 'Online', 'Paid', 7000.00, '2025-07-20', '2025-09-20', 8, NULL, 'https://testbenchqa.com/join', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(62, 'Architecture Intern', 'ArcVision Studio', 'Architecture', 'Offline', 'Unpaid', NULL, '2025-08-10', '2025-09-30', 7, 'Hyderabad', 'https://arcvision.interns', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(63, 'Game Art Intern', 'PlayBrush Studios', 'Game Art', 'Online', 'Paid', 7500.00, '2025-08-05', '2025-09-20', 6, NULL, 'https://playbrush.io/art-apply', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(64, 'Communication Intern', 'TalkTrek Org', 'Communication', 'Hybrid', 'Unpaid', NULL, '2025-08-01', '2025-09-10', 6, 'Delhi', 'https://talktrek.org/apply', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(65, 'Market Research Intern', 'BizPulse Analytics', 'Market Research', 'Online', 'Paid', 6500.00, '2025-07-25', '2025-09-10', 7, NULL, 'https://bizpulse.in/research', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(66, 'SaaS Product Intern', 'SaaSmart Tech', 'SaaS', 'Online', 'Paid', 9500.00, '2025-08-01', '2025-10-01', 8, NULL, 'https://saasmart.tech/joinus', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(67, 'Biotech Intern', 'GeneCore Labs', 'Biotechnology', 'Offline', 'Unpaid', NULL, '2025-08-10', '2025-09-30', 7, 'Ahmedabad', 'https://genecore.bio/intern', '2025-07-11 22:01:52', '2025-07-11 22:01:52'),
(68, 'QA Automation Intern', 'AutoLogic', 'QA Automation', 'Hybrid', 'Paid', 8800.00, '2025-07-25', '2025-09-25', 8, 'Mumbai', 'https://autologic.io/qa', '2025-07-11 22:01:52', '2025-07-11 22:01:52');

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_internshipapplication`
--

CREATE TABLE `mainapp_internshipapplication` (
  `id` bigint(20) NOT NULL,
  `applied_at` datetime(6) NOT NULL,
  `payment_success` varchar(3) NOT NULL,
  `candidate_id` bigint(20) NOT NULL,
  `internship_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_job`
--

CREATE TABLE `mainapp_job` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `company_name` varchar(150) NOT NULL,
  `domain` varchar(100) NOT NULL,
  `employment_type` varchar(20) NOT NULL,
  `salary_min_lpa` decimal(10,2) DEFAULT NULL,
  `salary_max_lpa` decimal(10,2) DEFAULT NULL,
  `experience_level` varchar(20) NOT NULL,
  `location` varchar(120) DEFAULT NULL,
  `remote_allowed` tinyint(1) NOT NULL,
  `apply_by` date DEFAULT NULL,
  `job_description` longtext DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `category` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mainapp_job`
--

INSERT INTO `mainapp_job` (`id`, `title`, `company_name`, `domain`, `employment_type`, `salary_min_lpa`, `salary_max_lpa`, `experience_level`, `location`, `remote_allowed`, `apply_by`, `job_description`, `created_at`, `updated_at`, `category`) VALUES
(1, 'Junior Software Developer', 'TechSpark Solutions', 'Full Stack Development', 'Full-time', 4.50, 6.50, 'Fresher', 'Noida', 1, '2025-08-15', 'Work on web applications using Django and React.', '2025-07-16 17:25:05.000000', '2025-07-16 17:25:05.000000', 'Software Development'),
(2, 'Marketing Analyst', 'Unilever', 'Digital Marketing', 'Full-time', 6.00, 9.00, '0-2 Yrs', 'Mumbai', 0, '2025-08-10', 'Analyze digital marketing campaigns.', '2025-07-16 17:25:05.000000', '2025-07-16 17:25:05.000000', 'Marketing'),
(3, 'HR Executive', 'TCS', 'Recruitment', 'Internship', 1.20, 1.50, 'Fresher', 'Chennai', 0, '2025-08-20', 'Assist in hiring and onboarding.', '2025-07-16 17:25:05.000000', '2025-07-16 17:25:05.000000', 'Human Resources'),
(4, 'Finance Associate', 'Deloitte', 'Financial Analysis', 'Full-time', 7.00, 10.00, '2-5 Yrs', 'Bangalore', 0, '2025-08-12', 'Work on client financial reporting.', '2025-07-16 17:25:05.000000', '2025-07-16 17:25:05.000000', 'Finance'),
(5, 'Operations Manager', 'Flipkart', 'Logistics', 'Contract', 8.50, 12.00, '5+ Yrs', 'Delhi', 0, '2025-08-30', 'Oversee supply chain operations.', '2025-07-16 17:25:05.000000', '2025-07-16 17:25:05.000000', 'Operations'),
(6, 'Backend Engineer', 'Google', 'Backend Systems', 'Full-time', 14.00, 20.00, '2-5 Yrs', 'Hyderabad', 1, '2025-09-05', 'Develop scalable backend APIs.', '2025-07-16 17:25:05.000000', '2025-07-16 17:25:05.000000', 'Software Development'),
(7, 'HR Intern', 'Infosys', 'Employee Engagement', 'Internship', 0.80, 1.00, 'Fresher', 'Pune', 0, '2025-08-25', 'Support HR team initiatives.', '2025-07-16 17:25:05.000000', '2025-07-16 17:25:05.000000', 'Human Resources'),
(8, 'Digital Marketing Executive', 'Zara', 'Social Media', 'Part-time', 3.50, 5.00, '0-2 Yrs', 'Remote', 1, '2025-08-22', 'Manage digital campaigns.', '2025-07-16 17:25:05.000000', '2025-07-16 17:25:05.000000', 'Marketing'),
(9, 'Finance Intern', 'ICICI Bank', 'Audit & Compliance', 'Internship', 1.00, 1.20, 'Fresher', 'Kolkata', 0, '2025-08-18', 'Assist in audit documentation.', '2025-07-16 17:25:05.000000', '2025-07-16 17:25:05.000000', 'Finance'),
(10, 'Operations Analyst', 'Amazon', 'Delivery Operations', 'Full-time', 5.00, 7.50, '0-2 Yrs', 'Gurgaon', 1, '2025-09-01', 'Monitor operations efficiency.', '2025-07-16 17:25:05.000000', '2025-07-16 17:25:05.000000', 'Operations');

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

-- --------------------------------------------------------

--
-- Table structure for table `mentorships`
--

CREATE TABLE `mentorships` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `mentor_name` varchar(150) NOT NULL,
  `mentor_company` varchar(120) DEFAULT NULL,
  `mentor_role` varchar(120) DEFAULT NULL,
  `session_topic` varchar(200) NOT NULL,
  `domain` varchar(100) NOT NULL,
  `category` enum('Paid','Free') NOT NULL,
  `price` decimal(10,2) DEFAULT 0.00,
  `duration_minutes` int(11) DEFAULT 60,
  `session_mode` enum('1‑on‑1','Group','Webinar') DEFAULT '1‑on‑1',
  `available_slots` int(11) DEFAULT 0,
  `booking_link` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `practice_sets`
--

CREATE TABLE `practice_sets` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `title` varchar(200) NOT NULL,
  `domain` varchar(120) NOT NULL,
  `difficulty` enum('Beginner','Intermediate','Advanced') DEFAULT 'Beginner',
  `category` enum('Free','Paid') NOT NULL,
  `price` decimal(8,2) DEFAULT 0.00,
  `question_count` int(11) DEFAULT 0,
  `time_limit_min` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
-- Indexes for table `competitions`
--
ALTER TABLE `competitions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idx_comp_category` (`category`),
  ADD KEY `idx_type` (`competition_type`);

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
-- Indexes for table `internships`
--
ALTER TABLE `internships`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idx_domain` (`domain`),
  ADD KEY `idx_category` (`category`);

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
-- Indexes for table `mainapp_competition`
--
ALTER TABLE `mainapp_competition`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `mainapp_internship`
--
ALTER TABLE `mainapp_internship`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idx_domain` (`domain`),
  ADD KEY `idx_category` (`category`);

--
-- Indexes for table `mainapp_internshipapplication`
--
ALTER TABLE `mainapp_internshipapplication`
  ADD PRIMARY KEY (`id`),
  ADD KEY `mainapp_internshipap_candidate_id_31f08675_fk_mainapp_c` (`candidate_id`);

--
-- Indexes for table `mainapp_job`
--
ALTER TABLE `mainapp_job`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `mainapp_school`
--
ALTER TABLE `mainapp_school`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `mentorships`
--
ALTER TABLE `mentorships`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idx_domain_mentor` (`domain`),
  ADD KEY `idx_category_mentor` (`category`);

--
-- Indexes for table `practice_sets`
--
ALTER TABLE `practice_sets`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idx_practice_domain` (`domain`),
  ADD KEY `idx_practice_category` (`category`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

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
-- AUTO_INCREMENT for table `competitions`
--
ALTER TABLE `competitions`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `internships`
--
ALTER TABLE `internships`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `mainapp_candidateprofile`
--
ALTER TABLE `mainapp_candidateprofile`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=87;

--
-- AUTO_INCREMENT for table `mainapp_careerpurpose`
--
ALTER TABLE `mainapp_careerpurpose`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `mainapp_college`
--
ALTER TABLE `mainapp_college`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `mainapp_company`
--
ALTER TABLE `mainapp_company`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `mainapp_competition`
--
ALTER TABLE `mainapp_competition`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `mainapp_internship`
--
ALTER TABLE `mainapp_internship`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT for table `mainapp_internshipapplication`
--
ALTER TABLE `mainapp_internshipapplication`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `mainapp_job`
--
ALTER TABLE `mainapp_job`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `mainapp_school`
--
ALTER TABLE `mainapp_school`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `mentorships`
--
ALTER TABLE `mentorships`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `practice_sets`
--
ALTER TABLE `practice_sets`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

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

--
-- Constraints for table `mainapp_internshipapplication`
--
ALTER TABLE `mainapp_internshipapplication`
  ADD CONSTRAINT `mainapp_internshipap_candidate_id_31f08675_fk_mainapp_c` FOREIGN KEY (`candidate_id`) REFERENCES `mainapp_candidateprofile` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
