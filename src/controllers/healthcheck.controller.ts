import { Request, Response } from 'express';
import { logger } from '@utils/logger';

class HealthcheckController{
    public healthCheck = async (req: Request, res: Response) => {
        logger.info("GET healthcheck")
        return res.send("Sonomood backend is up !").status(200);
    }
}

export default HealthcheckController