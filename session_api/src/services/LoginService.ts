import prisma from "@app/helpers/PrismaClient";
import { Users } from "@prisma/client";
import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";
import dotenv from "dotenv";
dotenv.config();

export class LoginService {
    async execute(email: string, password: string) {
        
        const result: Users | null = await prisma.users.findFirst({
            where: {
                email: email,
            },
        });

        if (result) {
            const checkPassword = await bcrypt.compare(
                password,
                result.password
            );
            if (!checkPassword) {
                throw "invalidpass";
            } else {
                const token = jwt.sign(
                    {
                        id: result.id,
                        name: result.name,
                        email: result.email,
                    },
                    process.env.SECRET as string,
                    { expiresIn: "1d" }
                );

                try {
                    jwt.verify(token, process.env.SECRET as string);
                    const userObject = {
                        token: token
                    };
                    return userObject;
                } catch (err) {
                    throw "invalidjwt";
                }
            }
        } else {
            throw "emailnotfound";
        }
    }
}
