SET SQL_MODE = "NO_ATO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `student` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `subjectid` varchar(255) NOT NULL,
  `term` int NOT NULL,
  `year` int NOT NULL
) ENGINE = InnoDB CHARSET=utf8 COLLATE utf8_general_ci;

ALTER TABLE `student`
  ADD PRIMARY KEY (`id`, `subjectid`, `term`, `year`);

COMMIT;