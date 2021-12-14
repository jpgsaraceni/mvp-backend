import { AddRankingController } from "@app/controllers/AddRankingController";
import { GetRankingController } from "@app/controllers/GetRankingController";
import validate from "@app/validations/AddRankingValidator";
import { Router } from "express";

const router = Router();

router.post("/addranking", validate.check(), new AddRankingController().handle);
router.get("/ranking", new GetRankingController().handle)

export default router;