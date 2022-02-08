import MlConfig from "./mlConfig";
import axios, {AxiosInstance} from "axios";
import { FactoryClassifierImpl } from "./classifier/impl/factory_classifier_impl";


export default class MlService {

    public classify(text: string, type: string = "default"): Promise<string> {
        return FactoryClassifierImpl.getInstance().create(type)
        .classifyFromText(text)
        .then((result) => {
           return result;
        });
    }
}
