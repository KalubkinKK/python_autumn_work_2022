CREATE TABLE "auto" (
  "id" SERIAL PRIMARY KEY,
  "reg_number" VARCHAR(16) NOT NULL,
  "color" VARCHAR(15) NOT NULL,
  "brand" VARCHAR(20) NOT NULL,
  "model" VARCHAR(20) NOT NULL,
  "mileage" VARCHAR(10) NOT NULL,
  "cr_year" DATE,
  "eng_number" VARCHAR(50) NOT NULL,
  "hijacking" BOOLEAN,
  "car_accident" BOOLEAN,
  "accident_date" DATE
);

CREATE TABLE "driver" (
  "id" SERIAL PRIMARY KEY,
  "name" VARCHAR(20) NOT NULL,
  "surname" VARCHAR(30) NOT NULL,
  "bd" DATE,
  "dt_buy" DATE,
  "dt_sell" DATE
);

CREATE TABLE "auto_driver" (
  "id_auto" SMALLINT NOT NULL,
  "id_driver" SMALLINT NOT NULL,
  PRIMARY KEY ("id_auto", "id_driver")
);

CREATE INDEX "idx_auto_driver__id_driver" ON "auto_driver" ("id_driver");

ALTER TABLE "auto_driver" ADD CONSTRAINT "fk_auto_driver__id_auto" FOREIGN KEY ("id_auto") REFERENCES "auto" ("id") ON DELETE CASCADE;

ALTER TABLE "auto_driver" ADD CONSTRAINT "fk_auto_driver__id_driver" FOREIGN KEY ("id_driver") REFERENCES "driver" ("id") ON DELETE CASCADE