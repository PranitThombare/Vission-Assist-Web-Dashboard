class PositionAnalyzer:
    def __init__(self):
        self.frame_width = None
        self.frame_height = None

    def set_frame_dimensions(self, width, height):
        self.frame_width = width
        self.frame_height = height

    def get_position_description(self, bbox):
        """Convert bounding box coordinates to position description"""
        if not all([self.frame_width, self.frame_height]):
            return ""
            
        x1, y1, x2, y2 = bbox
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2
        
        h_pos = self._get_horizontal_position(center_x)
        v_pos = self._get_vertical_position(center_y)
            
        return f"{h_pos} {v_pos}"

    def _get_horizontal_position(self, x):
        if x < self.frame_width * 0.33:
            return "on the left"
        elif x > self.frame_width * 0.66:
            return "on the right"
        return "in the center"

    def _get_vertical_position(self, y):
        if y < self.frame_height * 0.33:
            return "top"
        elif y > self.frame_height * 0.66:
            return "bottom"
        return "middle" 