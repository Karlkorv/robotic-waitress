#!/usr/bin/env python3

import argparse
import sys
import time

import numpy as num
import cv2
from tflite_support.task import core
from tflite_support.task import processor
from tflite_support.task import vision

class Human():
    def __init__(self, model: str, camera_id: int, width: int, height: int, num_threads: int, enable_edgetpu: bool):
        self.model = model
        self.camera_id = camera_id
        self.width = width
        self.height = height 
        self.num_threads = num_threads
        self.enable_edgetpu = enable_edgetpu

        base_options = core.BaseOptions( file_name=model, use_coral=enable_edgetpu, num_threads=num_threads)
        detection_options = processor.DetectionOptions(max_results=3, score_threshold=0.3)
        options = vision.ObjectDetectorOptions(base_options=base_options, detection_options=detection_options)
        detector = vision.ObjectDetector.create_from_options(options)

    def detectHuman(self, camera) -> None:
        if(camera.IsOpened()):
            success, image = camera.read()
            image = cv2.flip(image, 1)
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            input_tensor = vision.TensorImage.create_from_array(rgb_image)
            detection_result = self.detector.detect(input_tensor)
            self.foundHuman(detection_result)
            camera.release()
            cv2.destroyAllWindows()

        if not success:
            sys.exit('ERROR: No camera found.')

    
    def foundHuman(result: processor.DetectionResult) -> bool:
        for result_current in result.detections:
            category  = result_current.categories[0]
            category_name = category.category_name
            probability = round(category.score, 2)
            if (category_name == "person"):
                return True
        
        return False
        
   
