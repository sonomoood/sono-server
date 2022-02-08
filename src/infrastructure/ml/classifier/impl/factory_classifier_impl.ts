import { Classifier } from "../interface/classifier";
import { FactoryClassifier } from "../interface/factory_classifier.interface";
import { DefaultClassifier } from "./default_classifier";
import { SentimentClassifier } from "./sentiment_classifier";
import { EmotionClassifier } from "./emotion_classifier";

export class FactoryClassifierImpl implements FactoryClassifier {
    private static instance: FactoryClassifierImpl;
    public static getInstance(): FactoryClassifierImpl {
        if (!FactoryClassifierImpl.instance) {
            FactoryClassifierImpl.instance = new FactoryClassifierImpl();
        }
        return FactoryClassifierImpl.instance;
    }

    create(type: string = "default"): Classifier {
        switch(type) {
            case "sentiment": return new SentimentClassifier();
            break;
            case "emotion": return new EmotionClassifier();
            break;
            default: return new DefaultClassifier();
        }
    }
}