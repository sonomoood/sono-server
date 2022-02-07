import { Request, Response } from 'express';
import { logger } from '@utils/logger';
import config from 'config';
import { StatusCodes } from 'http-status-codes';
import MlService from '@/infrastructure/ml/mlService';
import MlConfig from '@/infrastructure/ml/mlConfig';
import Music from '@/domain/music/music';
import { musicModel } from '@/infrastructure/databases/music/music';
import MusicQueryDTO from '../dtos/musicQueryDTO';
import escapeRegex from '@/utils/escapeRegex';


export default class MusicController{
    /**
     * @openapi
     * /music/get:
     *   get:
     *     description: Get musics
     *     parameters:
     *       - name: title
     *         in: query
     *         required: false
     *         type: string
     *     responses:
     *       200:
     *         description: Returns list of music.
     */
    public getMusic = async (req: Request<{}, {}, {}, MusicQueryDTO>, res: Response) => {
        var musicQuery: MusicQueryDTO = req.query;
        if(!musicQuery.title){
            musicQuery.title = ""
        }
        var escapedTitle = escapeRegex(musicQuery.title);
        var musics = await musicModel.find({title: {$regex: escapedTitle, $options: "i"}}, {title: 1}).exec()
        
        return res.send(musics);
    }
}