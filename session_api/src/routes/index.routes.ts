import UserRoutes from "./session.routes";
import app from "@app/app";

app.use(UserRoutes);

export { app };