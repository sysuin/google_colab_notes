#!git clone

#%cd ..
#%cd ./root

#!mkdir .kaggle
#%cd ./.kaggle

#from google.colab import files
#up = files.upload()

#%cd ..
#%cd ..
#%cd ./content

#!chmod 600 /root/.kaggle/kaggle.json
#!kaggle competitions download -c web-traffic-time-series-forecasting

#!unzip household_power_consumption.zip
#!7z e train.json.7z
#!ls

%%file example.py
# %%file is an Ipython magic function that saves the code cell as a file
