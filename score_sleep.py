import mne
from visbrain.gui import Sleep
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget
import sys
import os


# variables
channel2keep = ('Fp1','Fp2','F3','F4','C3','C4','P3','P4','O1','O2')
sampling_frequency = 500
lowpass_frequency = 0.3
highpass_frequency = 35





app = QApplication(sys.argv)
window = QWidget()


datafile, _ = QFileDialog.getOpenFileName(window, "Open dataset", '',
                               "Any EEG files (*.fif *.vhdr *.edf *.gdf *.bdf *.eeg "
                               "*.egi *.mff *.cnt *.trc *.set *.rec);;"
                               "MEG (*.fif);;BrainVision (*.vhdr);;EDF (*.edf);;"
                               "GDF (*.gdf);;BDF (*.bdf);;Elan (*.eeg);;"
                               "EGI (*.egi);;MFF (*.mff);;CNT (*.cnt);;"
                               "Micromed (*.trc);;EEGLab (*.set);;REC (*.rec)"
                               "")


# open file in mne
data = mne.io.read_raw(datafile)

# select the channel
data = data.pick(channel2keep)

# load the data
data.load_data()

#preprocess the data
data = data.resample(sfreq= sampling_frequency)

# take data apart for visbrain
raw_data = data.get_data()
raw_channels = data.ch_names


# open visbrain
Sleep(data=raw_data, sf=sampling_frequency, channels=raw_channels).show()
