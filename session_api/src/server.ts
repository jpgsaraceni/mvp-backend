import { app } from "@routes/index.routes";

app.listen(7001, () => {
  console.log("Server running on port 7001");
  console.log("Swagger API Docs running at localhost:7001/docs")
})