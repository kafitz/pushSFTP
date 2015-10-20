# pushSFTP
Simple interface to upload file to a remote SFTP directory

### Config
Within the config.py field, specify the following parameters:
  - hostname
  - username
  - password
  - port
  - remote directory (relative to ssh user home)

PushSFTP handles the rest when setting up the class instance.

### Usage
```python

from push_sftp import SFTP

S = SFTP()
filepath = './blob.dat'
S.upload(filepath, display=True)

```
An upload in progress...
![Running](https://github.com/kafitz/pushSFTP/blob/master/media/part1.png)
Complete!
![Complete](https://github.com/kafitz/pushSFTP/blob/master/media/part2.png)


#### TO DO
 - key-based authentication
