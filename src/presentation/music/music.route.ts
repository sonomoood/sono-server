import { Router } from 'express';
import { Routes } from "@interfaces/routes.interface";
import MusicController from './music.controller';

export default class MusicRoute implements Routes{
  public path = '/music';
  public router = Router();
  public musicController = new MusicController();

  constructor() {
    this.initializeRoutes();
  }

  private initializeRoutes() {
      this.router.get(`${this.path}/get`, this.musicController.getMusic);
  }
}