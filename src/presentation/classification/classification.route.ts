import { Router } from 'express';
import { Routes } from "@interfaces/routes.interface";
import ClassificationController from './classification.controller';

export default class ClassificationRoute implements Routes{
  public path = '/classification';
  public router = Router();
  public classificationController = new ClassificationController();

  constructor() {
    this.initializeRoutes();
  }

  private initializeRoutes() {
      this.router.post(`${this.path}/from-lyrics`, this.classificationController.fromLyrics);
  }
}