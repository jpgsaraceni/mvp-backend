import prisma from "@app/helpers/PrismaClient";
import { Ranking } from "@prisma/client";

export class GetRankingService {
  async execute() {
    let getranking: Ranking[] = await prisma.ranking.findMany({
        take: 10,
        orderBy: {
            score: 'desc'
        }
    });

    const formattedRanking = getranking.map((element, i) => {
        return {
            position: i + 1,
            name: element.name,
            score: element.score
        }
    })
    return formattedRanking;
  }
}