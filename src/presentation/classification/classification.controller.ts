import { Request, Response } from 'express';
import { logger } from '@utils/logger';
import config from 'config';
import { StatusCodes } from 'http-status-codes';
import MlService from '@/infrastructure/ml/mlService';
import MlConfig from '@/infrastructure/ml/mlConfig';
import Music from '@/domain/music/music';
import { musicModel } from '@/infrastructure/databases/music/music';

export default class ClassificationController{

    mlService: MlService;

    constructor(){
        var mlConfig : MlConfig = config.get("mlService");
        this.mlService = new MlService(mlConfig);
    }

    /**
     * @openapi
     * /classification/from-lyrics:
     *   get:
     *     description: Classify a music from its lyrics
     *     parameters:
     *       - name: music
     *         in: body
     *         required: true
     *         type: Music
     *     responses:
     *       200:
     *         description: Returns classification.
     */
    public fromLyrics = async (req: Request<{}, {}, Music>, res: Response) => {
        var music:Music = req.body;
        var classification = await this.mlService.classifyFromText(music.lyrics);

        var musicDocument = new musicModel();
        musicDocument.title = music.title;
        musicDocument.lyrics = music.lyrics; 
        musicDocument.author = music.author;

        if(classification == "Unrecognized text content. Plase provide some known words."){
            musicDocument.mood = undefined;
        }
        else{
            musicDocument.mood = classification;
        }

        musicModel.create(musicDocument);
        return res.send(classification).status(StatusCodes.ACCEPTED);
    }
}