CREATE TABLE IF NOT EXISTS "PERSON" (
	"id" integer,
	"firstName" varchar,
	"lastName" varchar,
	"phone" varchar,
	"email" string,
	PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS "EMPLOEEY" (
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

CREATE TABLE IF NOT EXISTS "TICKET" (
	"id" integer,
	"category" string,
	PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS "EVENT" (
	"id" integer,
	"category" string,
	"description" text,
	"startDate" date,
	"endDate" date,
	PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS "EVENT_ROOM" (
	"id" integer,
	"name" string,
	"description" text,
	"availability" boolean,
	PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS "REQUEST" (
	"id" integer,
	"description" text,
	"submitionDate" date,
	"startDate" date,
	"endDate" date,
	PRIMARY KEY ("id")
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
	PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS "ROOM_REQUEST" (
	"id" integer,
	"attendance" integer,
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
	PRIMARY KEY ("id")
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
	PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS "PLANS" (
	"emploeeyId" integer,
	"eventId" integer,
	PRIMARY KEY ("emploeeyId", "eventId"),
	FOREIGN KEY ("emploeeyId") REFERENCES "EMPLOEEY" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT,
	FOREIGN KEY ("eventId") REFERENCES "EVENT" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "APPROVE" (
	"emploeeyId" integer,
	"requestId" integer,
	PRIMARY KEY ("emploeeyId", "requestId"),
	FOREIGN KEY ("emploeeyId") REFERENCES "EMPLOEEY" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT,
	FOREIGN KEY ("requestId") REFERENCES "REQUEST" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "MAKES" (
	"personId" integer,
	"requestId" integer,
	PRIMARY KEY ("personId", "requestId"),
	FOREIGN KEY ("personId") REFERENCES "PERSON" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT,
	FOREIGN KEY ("requestId") REFERENCES "REQUEST" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "REFERS_TO_EVENT" (
	"eventReqId" integer,
	"eventId" integer,
	PRIMARY KEY ("eventReqId", "eventId"),
	FOREIGN KEY ("eventReqId") REFERENCES "EVENT_REQUEST" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT,
	FOREIGN KEY ("eventId") REFERENCES "EVENT" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "REFERS_TO_ROOM" (
	"roomReqId" integer,
	"roomId" integer,
	PRIMARY KEY ("roomReqId", "roomId"),
	FOREIGN KEY ("roomReqId") REFERENCES "ROOM_REQUEST" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT,
	FOREIGN KEY ("roomId") REFERENCES "EVENT_ROOM" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "OCCUPIES" (
	"eventId" integer,
	"roomId" integer,
	PRIMARY KEY ("eventId", "roomId"),
	FOREIGN KEY ("eventId") REFERENCES "EVENT" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT,
	FOREIGN KEY ("roomId") REFERENCES "EVENT_ROOM" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "ISSUE_EVENT" (
	"eventId" integer,
	"ticketId" integer,
	PRIMARY KEY ("eventId", "ticketId"),
	FOREIGN KEY ("eventId") REFERENCES "EVENT" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT,
	FOREIGN KEY ("ticketId") REFERENCES "TICKET" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "ISSUE_VISIT" (
	"visitId" integer,
	"ticketId" integer,
	PRIMARY KEY ("visitId", "ticketId"),
	FOREIGN KEY ("visitId") REFERENCES "VISITS" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT,
	FOREIGN KEY ("ticketId") REFERENCES "TICKET" ("id")
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

CREATE TABLE IF NOT EXISTS "PLACED" (
	"exhibitId" varchar,
	"positionId" string,
	PRIMARY KEY ("exhibitId", "positionId"),
	FOREIGN KEY ("exhibitId") REFERENCES "EXHIBIT" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT,
	FOREIGN KEY ("positionId") REFERENCES "POSITION" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "BELONGS" (
	"exhibitId" string,
	"categoryId" integer,
	PRIMARY KEY ("exhibitId", "categoryId"),
	FOREIGN KEY ("exhibitId") REFERENCES "EXHIBIT" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT,
	FOREIGN KEY ("categoryId") REFERENCES "CATEGORY" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "HAS" (
	"exhibitId" varchar,
	"dimentionsId" integer,
	PRIMARY KEY ("exhibitId", "dimentionsId"),
	FOREIGN KEY ("exhibitId") REFERENCES "EXHIBIT" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT,
	FOREIGN KEY ("dimentionsId") REFERENCES "DIMENSIONS" ("id")
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
);

