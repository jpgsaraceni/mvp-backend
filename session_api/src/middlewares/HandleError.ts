import { Request, Response, NextFunction } from "express";
import handleError from "@helpers/WriteLog";

export function HandleError(
    error: any,
    req: Request,
    res: Response,
    next: NextFunction
) {
    if (error instanceof SyntaxError) {
        res.status(400).send({ error: "Syntax Error" });
    } else if (error instanceof Error) {
        handleError(error, "RequestErrors");
        res.status(500).send({
            error: "An error has occurred check logs for more details",
        });
    } else {
        next();
    }
}
