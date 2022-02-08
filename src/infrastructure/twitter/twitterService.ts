import config from "config";
import { TweetV2, TwitterApi, TwitterApiReadOnly } from "twitter-api-v2";

export default class TwitterService {

    client: TwitterApi;
    roClient: TwitterApiReadOnly;

    constructor(){
        this.client = new TwitterApi(config.get("twitter.bearerToken"));
        this.roClient = this.client.readOnly;
    }


    // Get twitter user id from its username
    async getUserId(username: string) : Promise<TwitterServiceResponse>{
        // Get user twitter ID
        var twitterUsername = username;
        var userResponse = await this.roClient.v2.userByUsername(twitterUsername);
        if(userResponse.errors){
            return {
                error: true,
                content: userResponse.errors[0].detail
            }
        }

        return {
            error: false,
            content: userResponse.data.id
        }
    }

    //Get 10 latest tweets
    async getLatestTweets(username: string) : Promise<TwitterServiceResponse>{
        var userIdResponse = await this.getUserId(username);
        if(userIdResponse.error){
            return userIdResponse;
        }
        var tweetsResponse = await this.roClient.v2.userTimeline(userIdResponse.content);

        return {
            error: false,
            content: tweetsResponse.data.data
        }
    }

    async getLatestMergedTweets(username: string) : Promise<TwitterServiceResponse>{
        var tweetsResponse = await this.getLatestTweets(username);
        if(tweetsResponse.error){
            return tweetsResponse;
        }
        var mergedTweets = this.mergeTweets(tweetsResponse.content);

        return {
            error: false,
            content: mergedTweets
        }
    }

    private mergeTweets(tweets: TweetV2[]): string{
        var mergedTweet = ""
        if(tweets){
            tweets.forEach(tweet => mergedTweet += " " + tweet.text);
        }
        return mergedTweet;
    }
}