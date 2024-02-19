//alert("hello ")
const video = document.getEelementById('video')
function startvideo(){
    navigator.getUserMedia(
        {
            video:{} },
          stream => video.srcObject =stream,
          err => console.error(error) 
        
    )
}
startvideo()
