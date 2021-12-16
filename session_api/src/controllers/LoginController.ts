import { Request, Response } from "express";
import handleError from "@app/helpers/WriteLog";
import { LoginService } from "@app/services/LoginService";

export class LoginController {
    async handle(req: Request, res: Response) {
        if (!req.headers.authorization) {
            res.status(400).send({ error: "Authorization header missing" });
        } else {
            const [, hash]: any = req.headers.authorization?.split(" ");
            const [email, password] = Buffer.from(hash, "base64")
                .toString()
                .split(":");

            const service = new LoginService();

            try {
                const result = await service.execute(email, password);
                res.status(201).send(result);
            } catch (err: any) {
                if (err == "invalidpass") {
                    res.status(401).json({ error: "Invalid password" });
                } else if (err == "invalidjwt") {
                    res.status(401).json({ error: "Invalid token" });
                } else if (err == "emailnotfound") {
                    res.status(401).json({ error: "Email not found" });
                } else {
                    handleError(err, "RegisterController");
                    res.status(500).json({
                        error: "an error has occurred, check logs for more details",
                    });
                }
            }
        }
    }
}
