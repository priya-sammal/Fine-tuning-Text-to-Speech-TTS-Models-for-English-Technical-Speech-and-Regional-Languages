from jiwer import wer

# Example ground truth and hypothesis (generated) sentences
ground_truth = "यह एक उदाहरण वाक्य है"  # Replace with actual ground truth sentence
hypothesis = "यह एक उदाहरण वाक़्य है"  # Replace with the model-generated transcription

# Calculate WER
error_rate = wer(ground_truth, hypothesis)
print(f"Word Error Rate (WER): {error_rate:.2f}")
