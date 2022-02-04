import { Request, Response } from 'express';
import { logger } from '@utils/logger';
import { StatusCodes } from 'http-status-codes';

class HealthcheckController{

    /**
     * @openapi
     * /healthcheck:
     *   get:
     *     description: Healthcheck endpoint
     *     responses:
     *       200:
     *         description: Return status 200 if alive.
     */
    public healthCheck = async (req: Request, res: Response) => {
        logger.info("GET healthcheck")
        return res.send("Sonomood backend is up !").status(StatusCodes.OK);
    }
}

export default HealthcheckController