CREATE TABLE IF NOT EXISTS "PERSON" (
	"id" integer,
	"firstName" varchar,
	"lastName" varchar,
	"phone" varchar,
	"email" string,
	PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS "EMPLOYEE" (
	"id" integer,
	"specialty" string,
	PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS "VISITS" (
	"id" integer,
	"date" date,
	"category" string,
	PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS "EVENT_TICKET" (
	"id" integer,
	"category" string,
	"eventId" integer,
	PRIMARY KEY ("id"),
	FOREIGN KEY ("eventId") REFERENCES "EVENT" ("id")
            ON UPDATE CASCADE
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "EVENT" (
	"id" integer,
	"category" string,
	"description" text,
	"startDate" date,
	"endDate" date,
	"eventRoomId" integer,
	PRIMARY KEY ("id"),
	FOREIGN KEY ("eventRoomId") REFERENCES "EVENT_ROOM" ("id")
            ON UPDATE CASCADE
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "EVENT_ROOM" (
	"id" integer,
	"name" string,
	"description" text,
	"availability" boolean,
	"capacity" integer,
	PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS "REQUEST" (
	"id" integer,
	"description" text,
	"submitionDate" date,
	"startDate" date,
	"endDate" date,
	"personId" integer,
	"" ,
	PRIMARY KEY ("id"),
	FOREIGN KEY ("personId") REFERENCES "PERSON" ("id")
            ON UPDATE CASCADE
            ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS "EXGANGE_REQUEST" (
	"id" integer,
	"country" string,
	"city" string,
	"postCode" varchar,
	"address" string,
	"addressNumber" integer,
	"phone" string,
	PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS "RESEARCH_REQUEST" (
	"id" integer,
	"type" string,
	"description" text,
	PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS "EVENT_REQUEST" (
	"id" integer,
	"type" string,
	"eventId" integer,
	PRIMARY KEY ("id"),
	FOREIGN KEY ("eventId") REFERENCES "EVENT" ("id")
            ON UPDATE CASCADE
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "ROOM_REQUEST" (
	"id" integer,
	"pieceCapacity" integer,
	"description" text,
	PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS "EXHIBIT" (
	"id" varchar,
	"name" string,
	"matterial" string,
	"rythm" string,
	"description" text,
	"value" integer,
	"exavationPlace" text,
	"exavationDate" date,
	"categoryId" integer,
	"positionId" varchar,
	PRIMARY KEY ("id"),
	FOREIGN KEY ("categoryId") REFERENCES "CATEGORY" ("id")
            ON UPDATE CASCADE
            ON DELETE SET NULL,
	FOREIGN KEY ("positionId") REFERENCES "POSITION" ("id")
            ON UPDATE CASCADE
            ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS "POSITION" (
	"id" varchar,
	"column" integer,
	"row" integer,
	PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS "CATEGORY" (
	"id" integer,
	"start_date" date,
	"end_date" date,
	"name" varchar,
	PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS "DIMENSIONS" (
	"id" integer,
	"height" float,
	"width" float,
	"length" float,
	"exhibitId" string,
	PRIMARY KEY ("id"),
	FOREIGN KEY ("exhibitId") REFERENCES "EXHIBIT" ("id")
            ON UPDATE CASCADE
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "PLANS" (
	"employeeId" integer,
	"eventId" integer,
	PRIMARY KEY ("employeeId", "eventId"),
	FOREIGN KEY ("employeeId") REFERENCES "EMPLOYEE" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT,
	FOREIGN KEY ("eventId") REFERENCES "EVENT" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "REFERS_TO_RESEARCH" (
	"researchId" integer,
	"exhibitId" varchar,
	PRIMARY KEY ("researchId", "exhibitId"),
	FOREIGN KEY ("researchId") REFERENCES "RESEARCH_REQUEST" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT,
	FOREIGN KEY ("exhibitId") REFERENCES "EXHIBIT" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "REFERS_TO_EXCHANGE" (
	"exchangeId" integer,
	"exhibitId" varchar,
	PRIMARY KEY ("exchangeId", "exhibitId"),
	FOREIGN KEY ("exchangeId") REFERENCES "EXGANGE_REQUEST" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT,
	FOREIGN KEY ("exhibitId") REFERENCES "EXHIBIT" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "APPROVE" (
	"id" integer,
	"approveDate" date,
	"requestId" integer,
	"employeeId" integer,
	PRIMARY KEY ("id"),
	FOREIGN KEY ("requestId") REFERENCES "REQUEST" ("id")
            ON UPDATE CASCADE
            ON DELETE RESTRICT,
	FOREIGN KEY ("employeeId") REFERENCES "EMPLOYEE" ("id")
            ON UPDATE CASCADE
            ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS "VISIT_TICKET" (
	"id" integer,
	"category" varchar,
	"visitId" integer,
	PRIMARY KEY ("id"),
	FOREIGN KEY ("visitId") REFERENCES "VISITS" ("id")
            ON UPDATE CASCADE
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "REQUEST_REFERS_ROOM" (
	"roomId" integer,
	"requestId" integer,
	"startDate" date,
	"endDate" date,
	PRIMARY KEY ("roomId", "requestId"),
	FOREIGN KEY ("roomId") REFERENCES "EVENT_ROOM" ("id")
            ON UPDATE CASCADE
            ON DELETE RESTRICT,
	FOREIGN KEY ("requestId") REFERENCES "ROOM_REQUEST" ("id")
            ON UPDATE CASCADE
            ON DELETE RESTRICT
);

