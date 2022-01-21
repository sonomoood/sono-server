import { Request, Response } from 'express';


class HealthcheckController{
    public healthCheck = async (req: Request, res: Response) => {
        return res.send("Sonomood backend is up !").status(200);
    }
}

export default HealthcheckController