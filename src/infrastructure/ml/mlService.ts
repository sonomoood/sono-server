import MlConfig from "./mlConfig";
import axios, {AxiosInstance} from "axios";

export default class MlService {

    mlConfig: MlConfig;
    mlClient: AxiosInstance;

    constructor(mlConfig: MlConfig) {
        this.mlConfig = mlConfig;
        this.mlClient = axios.create({
            baseURL: mlConfig.baseUrl
        })
    }

    async fromTwitter(tweets: string) : Promise<any>{
        var response = await this.mlClient.post(this.mlConfig.fromTwitterUrl, tweets);
        return response.data;
    }
}
