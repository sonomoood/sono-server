import 'dotenv/config';
import '@/index';
import App from '@/app';
import HealthCheckRoute from '@routes/healthcheck.route';
import validateEnv from '@utils/validateEnv';


// validateEnv();

const app = new App([
    new HealthCheckRoute()
]);

app.listen();
