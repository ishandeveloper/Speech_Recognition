## Speech Recognition
Speech Recognition and Text-To-Speech implemented using Google Text-To-Speech Service in Python.

### Examples
<pre><b>Jarvis >></b> How Can I Help You ?<br><b>You    >></b> I want to search something on Google<br><b>Jarvis >></b> What do you want to search for?<br><b>You    >></b> Cats<br><b>Jarvis >></b> Here's what I found for Cats</pre>

<pre><b>Jarvis >></b> How Can I Help You ?<br><b>You    >></b> I want to look for a place<br><b>Jarvis >></b> Which place are you looking for?<br><b>You    >></b> Nearest Subway Restaurant<br><b>Jarvis >></b> Here's The Location Of Nearest Subway Restaurant <b>(opens Google Maps)</b></pre>

### Installation
### clone code
```
git clone https://github.com/ishandeveloper/Speech_Recognition
cd Speech_Recognition
```

### pyaudio
#### requirements portaudio from http://www.portaudio.com/
```
git clone  https://git.assembla.com/portaudio.git
./configure --prefix=/path/to/your/local
make
make install
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/path/to/your/local/lib
export LIDRARY_PATH=$LIBRARY_PATH:/path/to/your/local/lib
export CPATH=$CPATH:/path/to/your/local/include
source ~/.bashrc
```
### Install requirements
```
pip install -r requirements.txt
```

##### Made with ♥ by <a href="https://github.com/ishandeveloper">ishandeveloper</a>

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/ishandeveloper)
