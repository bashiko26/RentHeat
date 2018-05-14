import { Request, Response, Router } from "express";

const usersRouter: Router = Router();

let users = { users:[
	{
		id: 1,
		address: "test1"
	},
	{
		id: 2,
		address: "test2"
	}
]};

usersRouter.get("/", (request: Request, response: Response) => {
	response.json(users);
});

export { usersRouter };


