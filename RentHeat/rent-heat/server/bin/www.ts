import * as http from "http";
import { app } from "../app";
import { serverPort } from "../config";

const port = process.env.PORT || serverPort;
app.set("port", port);

const server = http.createServer(app);

server.listen(port);
