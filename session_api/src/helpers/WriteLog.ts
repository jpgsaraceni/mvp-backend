import { promises as fs } from "fs";
import * as path from "path";

const handleError = async (err: any, file: string) => {
  fs.appendFile(
    path.join(__dirname, `../logs/${file}.log`),
    `${err}; Date: ${new Date().toLocaleDateString("en-us")}\n\n`,
    "utf-8"
  );
};

export default handleError;
