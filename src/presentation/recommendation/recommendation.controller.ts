import { Request, Response } from 'express';
import { logger } from '@utils/logger';
import config from 'config';
import { TwitterApi } from 'twitter-api-v2';
import { StatusCodes } from 'http-status-codes';
import MlService from '@/infrastructure/ml/mlService';
import MlConfig from '@/infrastructure/ml/mlConfig';
import escapeRegex from '@/utils/escapeRegex';
import { musicModel } from '@/infrastructure/databases/music/music';
import TwitterService from '@/infrastructure/twitter/twitterService';


export default class RecommendationController{

    mlService: MlService;

    constructor(){
        var mlConfig : MlConfig = config.get("mlService");
        this.mlService = new MlService(mlConfig);
    }

    /**
     * @openapi
     * /recommendation/from-twitter:
     *   get:
     *     description: Recommend music from a user tweet's
     *     parameters:
     *       - name: twitter_username
     *         in: query
     *         required: true
     *         type: string
     *     responses:
     *       200:
     *         description: Returns recommended musics.
     *       400:
     *         description: Error with the username
     */
    public fromTwitter = async (req: Request, res: Response) => {
        logger.info("Recommendation from twitter for user : " + req.query.twitter_username);
        if(!req.query.twitter_username){
            logger.info(req.query.twitter_username + " username is missing")
            return res.status(StatusCodes.BAD_REQUEST)
                .send("Twitter username is missing");
        }

        var twitterService : TwitterService = new TwitterService();
        var twitterSeviceResponse = await twitterService.getLatestMergedTweets(req.query.twitter_username.toString());

        if(twitterSeviceResponse.error){
            return res
            .status(StatusCodes.BAD_REQUEST)
            .send(twitterSeviceResponse.content);
        }

        var latestTweets = twitterSeviceResponse.content;
        var mood = await this.mlService.classifyFromText(latestTweets);

        logger.info("Tweets are :\n" + latestTweets + "\n----\nMood is : " + mood);

        //Get recommended music in database
        var escapedMood = escapeRegex(mood);
        var musics = await musicModel.find({mood: {$regex: escapedMood, $options: "i"}}).exec()

        var responseBody = {
            mood: mood,
            musics: musics
        }
        return res.send(responseBody).status(StatusCodes.ACCEPTED);
    }
}