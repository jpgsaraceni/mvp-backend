import { Request, Response } from "express";
import handleError from "@app/helpers/WriteLog";
import { CoinsService } from "@app/services/CoinsService";
import jwt from "jsonwebtoken";
import dotenv from "dotenv";
dotenv.config();

export class CoinsController {
    async handle(req: Request, res: Response) {
        if (!req.headers.authorization) {
            res.status(400).send({ error: "Authorization header missing" });
        } else {
            const [, token]: any = req.headers.authorization?.split(" ");

            const service = new CoinsService();

            try {
                jwt.verify(
                    token,
                    process.env.SECRET as string,
                    async function (err: any, decoded: any) {
                        if (err) {
                            res.status(400).send({ error: "Invalid token" });
                        } else {
                            const result = await service.execute(decoded.id);
                            res.status(200).send((result).toString());
                        }
                    }
                );
            } catch (err: any) {
                if (err == "notfound") {
                    res.status(404).json({ error: "User not found" });
                } else {
                    handleError(err, "CoinsController");
                    res.status(500).json({
                        error: "an error has occurred, check logs for more details",
                    });
                }
            }
        }
    }

    async update(req: Request, res: Response) {
        if (!req.headers.authorization) {
            res.status(400).send({ error: "Authorization header missing" });
        } else {
            const [, token]: any = req.headers.authorization?.split(" ");
            const coins = req.body.coins;

            const service = new CoinsService();

            try {
                jwt.verify(
                    token,
                    process.env.SECRET as string,
                    async function (err: any, decoded: any) {
                        if (err) {
                            res.status(400).send({ error: "Invalid token" });
                        } else {
                            const result = await service.update(decoded.id, coins);
                            res.status(200).send((result).toString());
                        }
                    }
                );
            } catch (err: any) {
                if (err == "notfound") {
                    res.status(404).json({ error: "User not found" });
                } else {
                    handleError(err, "CoinsController");
                    res.status(500).json({
                        error: "an error has occurred, check logs for more details",
                    });
                }
            }
        }
    }
}
