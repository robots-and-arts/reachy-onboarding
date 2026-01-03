from reachy_mini import ReachyMini
from scipy.signal import resample
import time

with ReachyMini(media_backend="default") as mini:
    # Initialization - After this point, both audio devices (input/output) will be seen as busy by other applications!
    mini.media.start_recording()
    mini.media.start_playing()

    # Record
    samples = None
    while samples is None:
        samples = mini.media.get_audio_sample()
        time.sleep(20)  # 20 seconds

    # Resample (if needed)
    # samples = resample(samples, mini.media.get_output_audio_samplerate()*len(samples)/mini.media.get_input_audio_samplerate())

    # Play
    mini.media.push_audio_sample(samples)
    time.sleep(len(samples) / mini.media.get_output_audio_samplerate())

    # Release audio devices (input/output)
    mini.media.stop_recording()
    mini.media.stop_playing()

