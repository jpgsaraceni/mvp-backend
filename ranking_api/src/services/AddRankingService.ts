import prisma from "@app/helpers/PrismaClient";
import { Ranking } from "@prisma/client";

export class AddRankingService {
  async execute(name: string, score: number) {
    const newranking: Ranking = await prisma.ranking.create({
      data: {
        name: name,
        score: score
      }
    });

    return newranking;
  }
}