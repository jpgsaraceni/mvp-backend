import express from "express";
import compression from "compression";
import cors from "cors";
import cookieParser from 'cookie-parser';

const app = express();

app.use(express.urlencoded({ extended: false }));
app.use(express.json());
app.use(compression());

const corsOptions = {
    origin: "*",
    credentials: true,
};

app.use(cookieParser());
app.use(cors(corsOptions));

export default app;