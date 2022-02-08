import { Router } from 'express';
import { Routes } from "@interfaces/routes.interface";
import RecommendationController from '@recommendation/recommendation.controller';

export default class RecommendationRoute implements Routes{
  public path = '/recommendation';
  public router = Router();
  public recommendationController = new RecommendationController();

  constructor() {
    this.initializeRoutes();
  }

  private initializeRoutes() {
      this.router.get(`${this.path}/from-twitter`, this.recommendationController.fromTwitter);
  }
}