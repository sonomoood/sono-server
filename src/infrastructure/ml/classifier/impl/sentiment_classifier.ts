import { Classifier } from "../interface/classifier";

export class SentimentClassifier implements Classifier {
    classifyFromText(text: string): Promise<any> {
        throw new Error("Method not implemented.");
    }
}