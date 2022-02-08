import axios, { AxiosInstance } from "axios";
import config from "config";
import MlConfig from "../../mlConfig";
import { Classifier } from "../interface/classifier";


export class DefaultClassifier implements Classifier {
    mlConfig: MlConfig;
    mlClient: AxiosInstance;

    constructor() {
        this.mlConfig = config.get("mlService");
        this.mlClient = axios.create({
            baseURL: this.mlConfig.baseUrl
        })
    }

    async classifyFromText(text: string) : Promise<any>{
        var response = await this.mlClient.post(this.mlConfig.classifyTextUrl, text);
        return response.data;
    }
}