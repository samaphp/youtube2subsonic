youtube2subsonic
================

Minimal server to convert Youtube to mp3 file then save it directly to subsonic media folder. (it's not secure, for personal use only!!)

## Requirements

  * [Web.py](http://webpy.org/)
  * [youtube-dl](https://github.com/rg3/youtube-dl)
  * wget
  * ffmpeg
  * lame
  
On Ubuntu, these requirements can be installed using this comand:

      apt-get install youtube-dl wget ffmpeg lame
		sudo easy_install web.py
		
## Usage

    1. Edit app.py and change 'music_folder' to your music full path folder.
    2. Run this command 'python app.py'
	 3. Go to your domain http://your-domain:8080/
	 
	 
## Notes
    You can run the server on diffrent port by write 'python app.py 8888'