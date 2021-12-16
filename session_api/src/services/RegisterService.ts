import prisma from "@app/helpers/PrismaClient";
import { Users } from "@prisma/client";


export class RegisterService {
    async execute(email: string, name: string, password: string) {
        const result: Users = await prisma.users.create({
            data: {
                email: email,
                name: name,
                password: password
            }
        });

        return result;
    }
}