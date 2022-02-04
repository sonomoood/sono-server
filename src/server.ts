import 'dotenv/config';
import '@/index';
import App from '@/app';
import HealthCheckRoute from '@routes/healthcheck.route';
import validateEnv from '@utils/validateEnv';
import RecommendationRoute from './routes/recommendation.route';


// validateEnv();

const app = new App([
    new HealthCheckRoute(),
    new RecommendationRoute()
]);

app.listen();
