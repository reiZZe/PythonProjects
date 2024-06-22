# import tkinter
from tkinter import *
# import speedtest
from speedtest import Speedtest


# Speed Function
def test():
  download = Speedtest().download()
  upload = Speedtest().upload()
  download_speed = round(download / (10**6), 2)
  upload_speed = round(upload / (10**6), 2)


# config
  download_label.config(text='Download Speed: \n' + str(download_speed) + 'MbPs')
  upload_label.config(text='Upload Speed:\n' + str(upload_speed) + 'MbPs')

# Root Object
root = Tk()

# Size and Title
root.title('SpeedTest')
root.geometry('275x325')

# Button
button = Button(root, text='Start', font=50, command=test)
button.pack(side=BOTTOM, pady=40)

# Download Speed
download_label = Label(root, text='Download Speed:\n', font=40)
download_label.pack(pady=(50, 0))

# Upload Speed
upload_label = Label(root, text='Upload Speed:\n', font=40)
upload_label.pack(pady=(10, 0))

# Run
root.mainloop()
