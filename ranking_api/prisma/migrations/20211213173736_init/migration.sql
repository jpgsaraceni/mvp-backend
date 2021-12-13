/*
  Warnings:

  - You are about to drop the column `username` on the `Ranking` table. All the data in the column will be lost.
  - You are about to drop the column `username` on the `Ranking_Mock` table. All the data in the column will be lost.
  - Added the required column `name` to the `Ranking` table without a default value. This is not possible if the table is not empty.
  - Added the required column `name` to the `Ranking_Mock` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "Ranking" DROP COLUMN "username",
ADD COLUMN     "name" VARCHAR NOT NULL;

-- AlterTable
ALTER TABLE "Ranking_Mock" DROP COLUMN "username",
ADD COLUMN     "name" VARCHAR NOT NULL;
