import 'dotenv/config';
import '@/index';
import App from '@/presentation/app';
import HealthCheckRoute from '@healthcheck/healthcheck.route';
import validateEnv from '@utils/validateEnv';
import RecommendationRoute from '@recommendation/recommendation.route';
import ClassificationRoute from './presentation/classification/classification.route';
import MusicRoute from './presentation/music/music.route';

// validateEnv();

const app = new App([
    new HealthCheckRoute(),
    new RecommendationRoute(),
    new ClassificationRoute(),
    new MusicRoute()
]);

app.listen();
