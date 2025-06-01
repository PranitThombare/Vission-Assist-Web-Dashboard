import torch
import cv2
import numpy as np
from ..audio.speech_engine import SpeechEngine
from .position_analyzer import PositionAnalyzer
from ..utils.fps_counter import FPSCounter
from datetime import datetime

class ObjectDetector:
    def __init__(self, model_name='yolov5s', conf_threshold=0.25):
        # Load model with error handling
        try:
            self.model = torch.hub.load('ultralytics/yolov5', model_name)
            self.model.conf = conf_threshold
            
            # Enable CUDA if available
            self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
            self.model.to(self.device)
            
        except Exception as e:
            raise RuntimeError(f"Failed to load model: {str(e)}")
        
        # Initialize components
        self.model.eval()
        self.fps_counter = FPSCounter()
        self.speech_engine = SpeechEngine()
        self.position_analyzer = PositionAnalyzer()
        
        # Frame dimensions (will be set when first frame is processed)
        self.frame_width = None
        self.frame_height = None

    def process_frame(self, frame):
        # Set frame dimensions if not set
        if self.frame_width is None:
            self.frame_height, self.frame_width = frame.shape[:2]
            self.position_analyzer.set_frame_dimensions(self.frame_width, self.frame_height)
        
        # Inference
        results = self.model(frame)
        
        # Update FPS
        self.fps_counter.update()
        
        # Get the annotated frame and convert to a writable array
        annotated_frame = results.render()[0].copy()
        
        # Process detections and provide audio feedback
        self._process_detections(results.xyxy[0])
        
        # Add FPS counter to frame
        fps = self.fps_counter.get_fps()
        cv2.putText(annotated_frame, f'FPS: {fps:.1f}', 
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        return annotated_frame, results

    def _process_detections(self, detections):
        if len(detections) > 0:
            for detection in detections:
                confidence = float(detection[4])
                class_id = int(detection[5])
                class_name = self.model.names[class_id]
                bbox = detection[:4].tolist()
                
                position = self.position_analyzer.get_position_description(bbox)
                speech_text = f"{class_name} detected {position}"
                self.speech_engine.speak(speech_text, class_name)
                print(f"Detection: {speech_text} (confidence: {confidence:.2f})") 