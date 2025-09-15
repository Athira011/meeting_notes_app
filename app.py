import whisper
import ollama

# Step 1: Transcribe audio with Whisper
def transcribe_audio(file_path):
    print("Transcribing audio...")
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result["text"]

# Step 2: Extract meeting notes using LLaMA 2 via Ollama
def extract_notes_and_actions(transcript):
    print("\nExtracting notes and action items with LLaMA 2...")
    prompt = f"""
You are a helpful assistant. Extract structured meeting notes and action items from the following transcript.

Transcript:
{transcript}

Respond in this format:

Meeting Summary:
- ...

Action Items:
- Person A: Action 1
- Person B: Action 2
"""
    response = ollama.chat(model="llama2", messages=[
        {"role": "user", "content": prompt}
    ])
    return response['message']['content']

# Main
if __name__ == "__main__":
    audio_path = "meeting.mp3"

    transcript = transcribe_audio(audio_path)
    print("\nTranscript:\n", transcript)

    output = extract_notes_and_actions(transcript)
    print("\nExtracted Notes & Action Items:\n", output)
