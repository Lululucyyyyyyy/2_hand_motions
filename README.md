# Hand Motion Classifier

The hand motion classifier is a trained neural network that can distinguish 2 hand motions: one and five. This model will return a single line in the terminal: “one” or “five”  following the input of an image. From data collection to deploying the model, every step was a learning experience that had its own challenges. This readme will teach you how you can set up your very own hand motion classifier. 


## Getting Started

This model has 2 demos: a laptop demo and a raspberry pi demo. It is compatible with the macos system for the laptop, and a raspberry pi 4b and logitech webcam for the raspberry pi demo.

### Prerequisites

To run this, you will first need to install a few modules. This demo assumes that you have python3 already installed.

```
pip install os
pip install io
pip install sys
pip install glob
pip install math
pip install numpy
pip install h5py
pip install matplotlib
pip install pylab
pip install scipy
pip install PIL
pip install tensorflow
pip install random
pip install time
pip install subprocess
pip install cv2
pip install imagesnap
```

On the raspberry pi, you will need to install the following modules.
```
pip install subprocess
pip install PIL
pip install numpy
pip install tensorflow
pip install cv2
pip install time
```
Now you are ready to clone the repo.

### Cloning

To clone this repo, simple create an empty directory in your terminal. Then, run the following line in your terminal;

```
git clone https://github.com/Lululucyyyyyyy/2_hand_motions.git
```

And you have the code!

## Laptop demo

To run the laptop demo, run the following line in the local terminal
```
python demo.py
```

### Raspberry Pi demo

To run the raspberry pi demo, use scp to send the files to your raspberry pi through the local terminal. You must be ssh -ed into your raspberry pi to do this. If you are having troubles with this, check out [the raspberry pi docs](https://www.raspberrypi.org/documentation/remote-access/ssh/)
```
scp the_tflite.tflite pi_demo.py pi@192.168.0.0: 
#use your own ip address. You can find this by running: 
ping raspberrypi.local
```
Now check that these two files are on the raspbery pi:
```
ls
```
The 2 files should be in the list. 

Now, run the following line to run the demo.

```
python pi_demo.py
```

## Built With

* [tf.keras](https://www.tensorflow.org/guide/keras) - The main library used to build the network
* [tf.lite](https://www.tensorflow.org/lite/guide/get_started) - The library used to convert and deploy the model
* [imagesnap](https://github.com/rharder/imagesnap) - Used to capture images for laptop demo
* [cv2](https://pypi.org/project/opencv-python/) - Used to create the live webcam feed
* [fswebcam](https://github.com/fsphil/fswebcam) - Used to capture images for raspberry pi demo

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Lucy Mo** - *Initial work* - [Lululucyyyyyyy](https://github.com/lululucyyyyyyy)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Special thanks to MIT HanLab and Professor Song Han for guiding me through this project
* Special thanks to [jeffreyzpan](https://github.com/jeffreyzpan) for helping me with this project

