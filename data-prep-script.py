import os
import soundfile as sf
import numpy as np
from scipy.signal import resample

input_folder = "my_input_data"
output_folder = "testdata/dac-train-mine/raw"

os.makedirs(output_folder, exist_ok=True)

TARGET_SR = 44100  # target sample rate
TARGET_DURATION = 5  # target duration in seconds
NUM_SAMPLES = TARGET_SR * TARGET_DURATION  # expected number of samples

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".wav"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        data, samplerate = sf.read(input_path)

        # convert to mono if stereo
        if len(data.shape) > 1:
            data = np.mean(data, axis=1)  # average the left & right channels

        # resample if needed
        if samplerate != TARGET_SR:
            num_samples_new = int(len(data) * (TARGET_SR / samplerate))
            data = resample(data, num_samples_new)
        
        # trim or pad to exactly 5 seconds
        if len(data) > NUM_SAMPLES:
            data = data[:NUM_SAMPLES]  # trim
        elif len(data) < NUM_SAMPLES:
            data = np.pad(data, (0, NUM_SAMPLES - len(data)), mode='constant')  # pad with silence
        
        sf.write(output_path, data, TARGET_SR)

        print(f"Processed: {filename}")

print("Processing complete. All files are now 44.1 kHz, 5 seconds, and mono.")
