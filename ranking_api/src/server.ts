import { app } from "@routes/index.routes";

app.listen(4000, () => {
  console.log("Server running on port 4000");
  console.log("Swagger API Docs running at localhost:4000/docs")
})