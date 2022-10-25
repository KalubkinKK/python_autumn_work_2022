CREATE TABLE "group" (
  "key" SERIAL PRIMARY KEY,
  "name_of_group" VARCHAR(255) NOT NULL,
  "limit_of_participants" INTEGER,
  "full_description" TEXT NOT NULL
);

CREATE TABLE "profile" (
  "id" SERIAL PRIMARY KEY,
  "id_parent" INTEGER,
  "surname" VARCHAR(255) NOT NULL,
  "name" VARCHAR(255) NOT NULL,
  "patronim" VARCHAR(255),
  "year_bd" DATE,
  "phone" VARCHAR(50),
  "email" VARCHAR(100),
  "family_status" BOOLEAN,
  "bio" TEXT,
  "is_free" BOOLEAN,
  "weight" DOUBLE PRECISION,
  "salary" INTEGER
);

CREATE INDEX "idx_profile__id_parent" ON "profile" ("id_parent");

ALTER TABLE "profile" ADD CONSTRAINT "fk_profile__id_parent" FOREIGN KEY ("id_parent") REFERENCES "profile" ("id") ON DELETE SET NULL;

CREATE TABLE "account" (
  "id" SERIAL PRIMARY KEY,
  "id_profile" INTEGER NOT NULL,
  "login" VARCHAR(100) NOT NULL,
  "password" VARCHAR(100) NOT NULL,
  "dt_enter" TIMESTAMP,
  "dt_create" TIMESTAMP,
  "is_blocked" BOOLEAN,
  "is_online" BOOLEAN,
  "href_avatar" VARCHAR(255)
);

CREATE INDEX "account_login" ON "account" ("login");

CREATE INDEX "idx_account__id_profile" ON "account" ("id_profile");

ALTER TABLE "account" ADD CONSTRAINT "fk_account__id_profile" FOREIGN KEY ("id_profile") REFERENCES "profile" ("id");

CREATE TABLE "account_group" (
  "id_account" INTEGER NOT NULL,
  "id_group" INTEGER NOT NULL,
  PRIMARY KEY ("id_account", "id_group")
);

CREATE INDEX "idx_account_group__id_group" ON "account_group" ("id_group");

ALTER TABLE "account_group" ADD CONSTRAINT "fk_account_group__id_account" FOREIGN KEY ("id_account") REFERENCES "account" ("id") ON DELETE CASCADE;

ALTER TABLE "account_group" ADD CONSTRAINT "fk_account_group__id_group" FOREIGN KEY ("id_group") REFERENCES "group" ("key") ON DELETE CASCADE