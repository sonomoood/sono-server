import { Request, Response } from 'express';
import { logger } from '@utils/logger';
import config from 'config';
import { TwitterApi } from 'twitter-api-v2';
import { StatusCodes } from 'http-status-codes';


export default class RecommendationController{

    public fromTwitter = async (req: Request, res: Response) => {
        if(!req.query.twitter_username){
            return res.status(StatusCodes.BAD_REQUEST)
            .send("Twitter username is missing");
        }

        // Twitter authentication
        const twitterClient = new TwitterApi(config.get("twitter.bearer_token"));
        const roClient = twitterClient.readOnly;

        // Get user twitter ID
        var twitterUsername = req.query.twitter_username.toString();
        var userResponse = await roClient.v2.userByUsername(twitterUsername);
        if(userResponse.errors){
            return res.status(400).send(userResponse.errors[0].detail);
        }
        var userId = userResponse.data.id;

        // Get user 10 latest tweet
        var userTimeline = await roClient.v2.userTimeline(userId);
        var latestTweets :String[] = new Array();
        userTimeline.data.data.forEach(tweet => latestTweets.push(tweet.text));

        return res.send(latestTweets).status(StatusCodes.ACCEPTED);
    }
}