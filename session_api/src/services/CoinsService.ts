import prisma from "@app/helpers/PrismaClient";
import { Users } from "@prisma/client";

export class CoinsService {
    async execute(id: any) {
        const result: Users | null = await prisma.users.findFirst({
            where: {
                id: id,
            },
        });

        //console.log(result);
        if (result) {
            return result.coins;
        } else {
            return "notfound";
        }
    }

    async update(id: any, addcoins: any) {

        const currentCoins: Users | null = await prisma.users.findFirst({
            where: {
                id: id
            }
        });

        const result: Users | null = await prisma.users.update({
            where: {
                id: id
            },
            data: {
                coins: currentCoins!.coins + addcoins
            }
        });

        //console.log(result.coins);
        return result.coins;
    }
}
