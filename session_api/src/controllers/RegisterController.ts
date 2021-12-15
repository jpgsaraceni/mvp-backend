import { Request, Response } from "express";
import bcrypt from "bcrypt";
import validate from "@app/validations/RegisterValidator";
import handleError from "@app/helpers/WriteLog";
import { RegisterService } from "@app/services/RegisterService";

export class RegisterController {
    async handle(req: Request, res: Response) {

        const errors = validate.resultsValidator(req);
        if (errors.length > 0) {
            return res.status(409).json({
                error: errors,
            });
        }

        const { email } = req.body;
        const { name } = req.body;
        const password = await bcrypt.hash(req.body.password, 10);

        const service = new RegisterService();

        try {
            const result = await service.execute(email, name, password);
            res.status(201).send(result);
        } catch (err: any) {
            if (err.code == "P2002") {
                res.status(400).json({ error: "E-mail already exists" });
            } else {
                handleError(err, "RegisterController");
                res.status(500).json({
                    error: "an error has occurred, check logs for more details",
                });
            }
        }
    }
}
