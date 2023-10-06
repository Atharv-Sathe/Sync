// Function to restart the video when the image button is clicked
function restartVideo() {
    const video = document.getElementById('video-background');
    video.currentTime = 0; // Reset video to the beginning
    video.play(); // Play the video
}
