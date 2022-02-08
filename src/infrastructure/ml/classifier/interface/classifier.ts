export interface Classifier {
    classifyFromText(text: string): Promise<any>
}