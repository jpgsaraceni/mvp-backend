import handleError from "@app/helpers/WriteLog";
import { GetRankingService } from "@app/services/GetRankingService";
import { Request, Response } from "express";


export class GetRankingController {
    async handle(req: Request, res: Response) {

        const service = new GetRankingService();

        try {
            const result = await service.execute();
            res.status(200).send(result);
        } catch (err) {
            handleError(err, "GetRankingController");
            res.status(500).json({
                error: "an error has occurred, check logs for more details",
            });
        }
    }
}