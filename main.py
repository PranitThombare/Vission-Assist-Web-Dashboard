import cv2
from flask import Flask, render_template, Response
from src.detector.object_detector import ObjectDetector
import threading
import time
import socket

app = Flask(__name__)

def get_local_ip():
    try:
        # Create a socket to get the local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

# Global variables
detector = ObjectDetector(conf_threshold=0.3)
camera = None
output_frame = None
lock = threading.Lock()

def generate_frames():
    global output_frame, lock
    
    while True:
        with lock:
            if output_frame is None:
                continue
            
            # Encode the frame in JPEG format
            (flag, encodedImage) = cv2.imencode(".jpg", output_frame)
            
            if not flag:
                continue
                
        # Yield the output frame in the byte format
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
              bytearray(encodedImage) + b'\r\n')

def process_video():
    global camera, output_frame, lock
    
    while True:
        ret, frame = camera.read()
        if not ret:
            print("Failed to grab frame")
            break
            
        # Process frame using existing detector
        annotated_frame, results = detector.process_frame(frame)
        
        # Update the output frame
        with lock:
            output_frame = annotated_frame.copy()
            
        time.sleep(0.1)  # Small delay to prevent high CPU usage

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def main():
    global camera
    
    # Get local IP address
    local_ip = get_local_ip()
    print("\n" + "="*50)
    print(f"Vision Assist is running!")
    print(f"Local URL: http://localhost:5000")
    print(f"Network URL: http://{local_ip}:5000")
    print("="*50 + "\n")
    
    # Initialize video capture
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        raise RuntimeError("Failed to open webcam")
    
    # Start a thread that will perform video processing
    t = threading.Thread(target=process_video)
    t.daemon = True
    t.start()
    
    # Start the Flask app
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)

if __name__ == "__main__":
    main() 
    