import { io } from 'socket.io-client';
import config from './config';
// "undefined" means the URL will be computed from the `window.location` object
// const URL = process.env.NODE_ENV === 'production' ? undefined : 'http://localhost:5000';

export const socket = io(config.apiUrl);