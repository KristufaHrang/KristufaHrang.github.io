// JavaScript Document
 const menuToggle = document.querySelector('.toggle');
      const showcase = document.querySelector('.showcase');

      menuToggle.addEventListener('click', () => {
        menuToggle.classList.toggle('active');
        showcase.classList.toggle('active');
      })

var fade_in_videos = document.querySelectorAll('.fade-in-video');
for( i=0; i<fade_in_videos.length; i++ ) {
    fade_in_videos[i].addEventListener("playing", function(){
        this.className += ' is-playing';
    });
}