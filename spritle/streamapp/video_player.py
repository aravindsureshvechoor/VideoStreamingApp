import cv2

class VideoPlayer:
    def __init__(self, video_url):
        self.video_url = video_url

    def play_video(self):
        cap = cv2.VideoCapture(self.video_url)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            cv2.imshow('Video Player', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
