import { LoginController } from "@app/controllers/LoginController";
import { RegisterController } from "@app/controllers/RegisterController";
import validate from "@app/validations/RegisterValidator";
import { Router } from "express";

const router = Router();

router.post('/register', validate.check(), new RegisterController().handle);
router.post('/login', new LoginController().handle);

export default router;