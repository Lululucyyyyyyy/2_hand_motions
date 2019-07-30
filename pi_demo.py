import subprocess
from PIL import Image
import numpy as np
import tensorflow as tf
import cv2
import time

interpreter = tf.lite.Interpreter(model_path='/home/pi/the_tflite.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

input_shape = input_details[0]['shape']

while True:
	subprocess.call("fswebcam -D 0.01 --no-banner --quiet img.jpeg", shell=True)
	img = Image.open("img.jpeg")
	input_data = np.expand_dims(np.array(img.resize((224, 224)), dtype=np.float32), 0)

	interpreter.set_tensor(input_details[0]['index'], input_data) 

	toc = time.time()
	interpreter.invoke()
	tic = time.time()
	the_time = tic - toc

	output_data = interpreter.get_tensor(output_details[0]['index'])
	answer = np.argmax(output_data)
	if output == 1:
		print('one')
	else:
		print('five')
