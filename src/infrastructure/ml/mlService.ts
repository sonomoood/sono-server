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

    async classifyFromText(text: string) : Promise<any>{
        var response = await this.mlClient.post(this.mlConfig.classifyTextUrl, text);
        return response.data;
    }
}
