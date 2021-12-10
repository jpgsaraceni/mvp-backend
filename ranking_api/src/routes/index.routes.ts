import app from "../app";
import swaggerUi from "swagger-ui-express";

import swaggerFile from "../swagger.json";

import Tasks from "./ranking.routes";

app.use("/docs", swaggerUi.serve, swaggerUi.setup(swaggerFile));

app.use(Tasks);

export { app }