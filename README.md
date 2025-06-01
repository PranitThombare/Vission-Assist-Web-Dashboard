# Vision Assist - Real-time Object Detection System

Vision Assist is a powerful real-time object detection system that uses YOLOv5 and Flask to provide a web-based interface for object detection. The system can be accessed locally or over a network, making it perfect for various applications like security monitoring, object tracking, and more.

## Features

- 🎯 Real-time object detection using YOLOv5
- 🌐 Web-based interface accessible from any device
- 🔊 Audio feedback for detected objects
- 📊 Live detection log
- ⚙️ Adjustable settings panel
- 📱 Responsive design for all devices
- 🔄 Network access support
- 🎨 Modern and intuitive UI

## Prerequisites

- Python 3.7 or higher
- Webcam
- Internet connection (for first-time model download)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Vision-Assist.git
   cd Vision-Assist
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the application:

   ```bash
   python main.py
   ```

2. Access the application:
   - Local access: Open `http://localhost:5000` in your web browser
   - Network access: Use the Network URL shown in the console (e.g., `http://192.168.x.x:5000`)

3. Using the interface:
   - The video feed will automatically start
   - Detected objects will be highlighted with bounding boxes
   - Audio feedback will announce detected objects
   - Use the settings panel to adjust detection parameters
   - View detection history in the log panel

## Network Access

The application can be accessed from any device on your local network:

1. Make sure all devices are connected to the same network
2. Note the Network URL shown in the console when starting the application
3. Access the application from other devices using the Network URL
4. The URL is also displayed in the web interface footer

### Troubleshooting Network Access

If you can't access the application from other devices:
1. Check if your firewall is blocking port 5000
2. Verify that all devices are on the same network
3. Try temporarily disabling your firewall to test
4. Make sure no other application is using port 5000

## Project Structure

```
Vision-Assist/
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── templates/          # HTML templates
│   └── index.html     # Main web interface
├── static/            # Static files
│   └── css/          # CSS styles
│       └── style.css # Main stylesheet
└── src/              # Source code
    ├── detector/     # Detection modules
    ├── audio/        # Audio feedback
    └── utils/        # Utility functions
```

## Features in Detail

### Object Detection
- Uses YOLOv5 for accurate real-time detection
- Configurable confidence threshold
- Multiple detection speed options

### Web Interface
- Clean, modern design
- Real-time video streaming
- Detection log with timestamps
- Settings panel for customization
- Responsive layout for all devices

### Audio Feedback
- Voice announcements for detected objects
- Position-based descriptions
- Configurable audio settings

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- YOLOv5 by Ultralytics
- Flask web framework
- OpenCV for video processing
- All other open-source libraries used in this project

## Author

Harshal Taware, Pranit Thombare

## Support

For support, please open an issue in the GitHub repository or contact the author.
