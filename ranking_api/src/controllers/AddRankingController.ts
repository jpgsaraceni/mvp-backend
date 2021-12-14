import handleError from "@app/helpers/WriteLog";
import { AddRankingService } from "@app/services/AddRankingService";
import validate from "@app/validations/AddRankingValidator";
import { Request, Response } from "express";


export class AddRankingController {
    async handle(req: Request, res: Response) {
        const { name } = req.body;
        const { score } = req.body;

        const service = new AddRankingService();

        const errors = validate.resultsValidator(req);
        if (errors.length > 0) {
            return res.status(409).json({
                error: errors,
            });
        }

        try {
            const result = await service.execute(name, score);
            res.status(201).send(result);
        } catch (err) {
            handleError(err, "AddRankingController");
            res.status(500).json({
                error: "an error has occurred, check logs for more details",
            });
        }
    }
}