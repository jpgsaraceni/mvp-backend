import { validationResult, check } from "express-validator";
import { Request } from "express";

const validate = {
    check() {
        return [
            check("email").notEmpty().withMessage("E-mail is required").isEmail().withMessage("Invalid E-mail"),
            check("name").notEmpty().withMessage("Name is required"),
            check("password")
                .notEmpty()
                .withMessage("Password is required")
                .isLength({ min: 6 })
                .withMessage("The password should have at least 6 characters")
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
