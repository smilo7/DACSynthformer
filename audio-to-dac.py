import dac
from audiotools import AudioSignal

# Download a model
model_path = dac.utils.download(model_type="44khz")
model = dac.DAC.load(model_path)

filename = "DSWind--strength-00.50--c-01--x-95"

# # Load audio signal file
# signal = AudioSignal(f'testdata/dac-train{filename}.wav')

# signal = signal.cpu()
# x = model.compress(signal)

# # Save and load to and from disk
# x.save(f"testdata/dac-train-mine/{filename}.dac")


x = dac.DACFile.load(f"testdata/dac-val/{filename}.dac")

# # Decompress it back to an AudioSignal
y = model.decompress(x)

# # Write to file
y.write('output4.wav')