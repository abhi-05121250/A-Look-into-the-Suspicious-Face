const http = require('http');

const requestListener = function (req, res) {
  
  res.send('index.html');
}
//alert("hello ")
const video = document.getEelementById('video')
function startvideo(){
    navigator.getUserMedia(
        {
            video:{} },
          stream => video.srcObject =stream,
          err => console.error() 
        
    )
}

const server = http.createServer(requestListener);
server.listen(8080);
