import { Request, Response } from 'express';
import { logger } from '@utils/logger';
import config from 'config';
import { TwitterApi } from 'twitter-api-v2';
import { StatusCodes } from 'http-status-codes';
import MlService from '@/infrastructure/ml/mlService';
import MlConfig from '@/infrastructure/ml/mlConfig';


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
     *         description: Returns 10 latest tweets.
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

        // Twitter authentication
        const twitterClient = new TwitterApi(config.get("twitter.bearerToken"));
        const roClient = twitterClient.readOnly;

        // Get user twitter ID
        var twitterUsername = req.query.twitter_username.toString();
        var userResponse = await roClient.v2.userByUsername(twitterUsername);
        if(userResponse.errors){
            return res
            .status(StatusCodes.BAD_REQUEST)
            .send(userResponse.errors[0].detail);
        }
        var userId = userResponse.data.id;

        // Get user 10 latest tweet
        var userTimeline = await roClient.v2.userTimeline(userId);
        var latestTweets : string = "";

        if(userTimeline.data.data){
            userTimeline.data.data.forEach(tweet => latestTweets += " " + tweet.text);
        }
        
        var mood = await this.mlService.fromTwitter(latestTweets);

        logger.info("Tweets are :\n" + latestTweets + "\n----\nMood is : " + mood);

        return res.send(mood).status(StatusCodes.ACCEPTED);
    }
}