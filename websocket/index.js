const Server = require('socket.io').Server;
const http = require('http');

let io = new Server(5000);

io.on('connection', (socket) => {
    console.log('Hello world! I have absolutely no idea why I exist but probably because i want to lol ijkn;dscx ,vmfdnfdsddwrafdg')
})

let server = http.createServer();
io.attach(server);

server.listen(5000);
