import '@/index';
import config from "config";
import MlConfig from "./mlConfig";
import MlService from "./mlService";

test('ML Service - From Twitter mock', async () => {

    var mlConfig : MlConfig = config.get("mlService");
    var mlService = new MlService(mlConfig);

    const data = await mlService.classifyFromText("I don't like reggae. I love it . Don't like Jamaica. I love her");
    expect(data).toBe("hurt");
});