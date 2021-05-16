BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "session" (
	"id"	INT,
	"course_id"	INT,
	"session_start_time"	VARCHAR,
	"session_end_time"	VARCHAR,
	"created_on"	TIME UNIQUE,
	"session_date"	DATE,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "course" (
	"id"	INT,
	"course_name"	VARCHAR NOT NULL,
	"course_code"	VARCHAR NOT NULL,
	"created_on"	TIME UNIQUE,
	""	,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "attendance" (
	"id"	INT,
	"session_id"	INT,
	"timestamp"	TIME,
	"students_id"	INT,
	"sessions_id"	INT,
	PRIMARY KEY("id"),
	FOREIGN KEY("students_id") REFERENCES "student"("unique_id"),
	FOREIGN KEY("sessions_id") REFERENCES "session"("id")
);
CREATE TABLE IF NOT EXISTS "student" (
	"id"	INT,
	"unique_id"	VARCHAR NOT NULL UNIQUE,
	"first_name"	STRING NOT NULL,
	"last_name"	STRING NOT NULL,
	"username"	VARCHAR NOT NULL UNIQUE,
	"password"	VARCHAR NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "lecturer" (
	"id"	INTEGER,
	"id_number"	VARCHAR NOT NULL UNIQUE,
	"first_name"	VARCHAR NOT NULL,
	"last_name"	VARCHAR NOT NULL,
	"gender"	VARCHAR NOT NULL,
	"username"	VARCHAR NOT NULL UNIQUE,
	"password"	VARCHAR NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
COMMIT;
