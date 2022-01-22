import { Router } from 'express';
import { Routes } from "@interfaces/routes.interface";
import HealthcheckController from '@controllers/healthcheck.controller';

class HealthCheckRoute implements Routes{
  public path = '/';
  public router = Router();
  public healthController = new HealthcheckController();

  constructor() {
    this.initializeRoutes();
  }

  private initializeRoutes() {
    this.router.get("/healthcheck", this.healthController.healthCheck);
    // this.router.post(`${this.path}signup`, validationMiddleware(CreateUserDto, 'body'), this.authController.signUp);
  }
}

export default HealthCheckRoute;
