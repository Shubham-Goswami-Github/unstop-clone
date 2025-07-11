/* =============================== *
 * 1.  INTERNSHIPS TABLE           *
 * =============================== */
CREATE TABLE `internships` (
  `id`               BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `title`            VARCHAR(200)    NOT NULL,
  `company_name`     VARCHAR(150)    NOT NULL,
  `domain`           VARCHAR(100)    NOT NULL,          -- e.g. HR, SDE, Marketing
  `mode`             ENUM('Online','Offline','Hybrid') DEFAULT 'Online',
  `category`         ENUM('Paid','Unpaid')             NOT NULL,
  `stipend_amount`   DECIMAL(10,2)   DEFAULT NULL,      -- nullable for Unpaid
  `start_date`       DATE           DEFAULT NULL,
  `end_date`         DATE           DEFAULT NULL,
  `duration_weeks`   INT            DEFAULT NULL,
  `location`         VARCHAR(120)   DEFAULT NULL,
  `application_link` VARCHAR(255)   DEFAULT NULL,
  `created_at`       DATETIME       DEFAULT CURRENT_TIMESTAMP,
  `updated_at`       DATETIME       DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX  `idx_domain` (`domain`),
  INDEX  `idx_category` (`category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


/* =============================== *
 * 2.  JOBS  TABLE                 *
 * =============================== */
CREATE TABLE `jobs` (
  `id`               BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `title`            VARCHAR(200)    NOT NULL,
  `company_name`     VARCHAR(150)    NOT NULL,
  `domain`           VARCHAR(100)    NOT NULL,          -- eg. Data Science, Finance…
  `employment_type`  ENUM('Full‑time','Part‑time','Contract','Internship') DEFAULT 'Full‑time',
  `salary_min_lpa`   DECIMAL(10,2)   DEFAULT NULL,
  `salary_max_lpa`   DECIMAL(10,2)   DEFAULT NULL,
  `experience_level` ENUM('Fresher','0‑2 Yrs','2‑5 Yrs','5+ Yrs') DEFAULT 'Fresher',
  `location`         VARCHAR(120)    DEFAULT NULL,
  `remote_allowed`   TINYINT(1)      DEFAULT 0,
  `apply_by`         DATE            DEFAULT NULL,
  `job_description`  TEXT            DEFAULT NULL,
  `created_at`       DATETIME        DEFAULT CURRENT_TIMESTAMP,
  `updated_at`       DATETIME        DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX  `idx_domain_jobs` (`domain`),
  INDEX  `idx_location` (`location`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


/* =============================== *
 * 3.  COMPETITIONS TABLE          *
 * =============================== */
CREATE TABLE `competitions` (
  `id`               BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `title`            VARCHAR(200)    NOT NULL,
  `host_org`         VARCHAR(150)    NOT NULL,
  `category`         ENUM('Free','Paid') NOT NULL,
  `fee_amount`       DECIMAL(8,2)    DEFAULT 0.00,
  `competition_type` ENUM('Case‑Study','Hackathon','Quiz','Idea‑Thon','Other') DEFAULT 'Other',
  `mode`             ENUM('Online','Offline','Hybrid') DEFAULT 'Online',
  `start_date`       DATE            DEFAULT NULL,
  `end_date`         DATE            DEFAULT NULL,
  `prize_pool`       VARCHAR(120)    DEFAULT NULL,      -- e.g. "₹1 Lakh + PPI"
  `team_size`        VARCHAR(20)     DEFAULT 'Individual',
  `registration_deadline` DATE      DEFAULT NULL,
  `created_at`       DATETIME        DEFAULT CURRENT_TIMESTAMP,
  `updated_at`       DATETIME        DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX  `idx_comp_category` (`category`),
  INDEX  `idx_type` (`competition_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


/* =============================== *
 * 4.  MENTORSHIPS TABLE           *
 * =============================== */
CREATE TABLE `mentorships` (
  `id`               BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `mentor_name`      VARCHAR(150)    NOT NULL,
  `mentor_company`   VARCHAR(120)    DEFAULT NULL,      -- eg. Google
  `mentor_role`      VARCHAR(120)    DEFAULT NULL,      -- eg. SDE2
  `session_topic`    VARCHAR(200)    NOT NULL,          -- eg. "CV Review"
  `domain`           VARCHAR(100)    NOT NULL,          -- eg. MBA Prep
  `category`         ENUM('Paid','Free') NOT NULL,
  `price`            DECIMAL(10,2)   DEFAULT 0.00,      -- 0 for free
  `duration_minutes` INT             DEFAULT 60,
  `session_mode`     ENUM('1‑on‑1','Group','Webinar') DEFAULT '1‑on‑1',
  `available_slots`  INT             DEFAULT 0,
  `booking_link`     VARCHAR(255)    DEFAULT NULL,
  `created_at`       DATETIME        DEFAULT CURRENT_TIMESTAMP,
  `updated_at`       DATETIME        DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX  `idx_domain_mentor` (`domain`),
  INDEX  `idx_category_mentor` (`category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


/* =============================== *
 * 5.  PRACTICE SETS TABLE         *
 * =============================== */
CREATE TABLE `practice_sets` (
  `id`               BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `title`            VARCHAR(200)    NOT NULL,
  `domain`           VARCHAR(120)    NOT NULL,          -- Coding, Aptitude, etc.
  `difficulty`       ENUM('Beginner','Intermediate','Advanced') DEFAULT 'Beginner',
  `category`         ENUM('Free','Paid') NOT NULL,
  `price`            DECIMAL(8,2)    DEFAULT 0.00,
  `question_count`   INT             DEFAULT 0,
  `time_limit_min`   INT             DEFAULT NULL,      -- timer if any
  `created_at`       DATETIME        DEFAULT CURRENT_TIMESTAMP,
  `updated_at`       DATETIME        DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX  `idx_practice_domain` (`domain`),
  INDEX  `idx_practice_category` (`category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
