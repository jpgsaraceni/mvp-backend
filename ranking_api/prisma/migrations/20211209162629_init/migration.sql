-- CreateTable
CREATE TABLE "Ranking" (
    "id" SERIAL NOT NULL,
    "username" VARCHAR NOT NULL,
    "score" INTEGER NOT NULL,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "Ranking_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Ranking_Mock" (
    "id" SERIAL NOT NULL,
    "username" VARCHAR NOT NULL,
    "score" INTEGER NOT NULL,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "Ranking_Mock_pkey" PRIMARY KEY ("id")
);
