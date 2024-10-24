import time

# Example sentence for TTS
sentence = "यह एक उदाहरण वाक्य है"

# Measure inference time
start_time = time.time()
tts.tts_to_file(text=sentence, speaker=tts.speakers[0], file_path="output.wav")
inference_time = time.time() - start_time

print(f"Inference time: {inference_time:.4f} seconds")
