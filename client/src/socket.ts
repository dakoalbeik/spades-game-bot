// socket.js
import {io} from 'socket.io-client';

const socket = io('http://localhost:4000');

socket.on('connect', () => {
    console.log('Connected:', socket.id)
});


socket.on('disconnect', () => {
    console.log('Disconnected');
});

export default socket;
