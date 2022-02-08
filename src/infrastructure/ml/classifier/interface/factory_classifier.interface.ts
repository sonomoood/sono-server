import { Classifier } from "./classifier";

export interface FactoryClassifier {
    create(type: string): Classifier
}