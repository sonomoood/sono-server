import 'dotenv/config';
import '@/index';
import App from '@/presentation/app';
import HealthCheckRoute from '@healthcheck/healthcheck.route';
import validateEnv from '@utils/validateEnv';
import RecommendationRoute from '@recommendation/recommendation.route';

// validateEnv();

const app = new App([
    new HealthCheckRoute(),
    new RecommendationRoute()
]);

app.listen();
