import { validationResult, check } from "express-validator";
import { Request } from "express";

const validate = {
    check() {
        return [
            check("name").notEmpty().withMessage("Name is required"),
            check("score")
                .notEmpty()
                .withMessage("Score is required")
                .isLength({ min: 1 })
                .withMessage("The score should have at least one character")
        ];
    },

    resultsValidator(req: Request) {
        const messages = [];
        if (!validationResult(req).isEmpty()) {
            const errors = validationResult(req).array();
            for (const i of errors) {
                messages.push(i);
            }
        }
        return messages;
    },
};

export default validate;
