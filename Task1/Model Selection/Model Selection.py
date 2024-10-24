#Task 1: Fine-tuning TTS for English with Technical Vocabulary
#Model Selection (Coqui TTS or SpeechT5)

# Example using Coqui TTS
from TTS.api import TTS

# Load pre-trained TTS model
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=True)

# Example sentence with technical jargon
sentence = "We need to optimize the API and the CUDA performance for this TTS model."

# Perform inference
output_path = tts.tts_to_file(text=sentence, speaker=tts.speakers[0], file_path="output.wav")