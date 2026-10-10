#!/usr/bin/env python3
"""Text to speech with ElevenLabs (Hebrew works with eleven_v3 + language_code "he").

Usage:
  python3 elevenlabs_tts.py "<text>" out.mp3 [voice_id] [model_id]
ELEVENLABS_API_KEY is read from the environment; in the cloud session the proxy injects it.
"""
import json, os, sys, urllib.request

def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    text, out = sys.argv[1], sys.argv[2]
    voice = sys.argv[3] if len(sys.argv) > 3 else "JBFqnCBsd6RMkjVDRZzb"
    model = sys.argv[4] if len(sys.argv) > 4 else "eleven_v3"
    body = {"text": text, "model_id": model}
    if any("֐" <= c <= "׿" for c in text):
        body["language_code"] = "he"
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice}?output_format=mp3_44100_128",
        data=json.dumps(body).encode(), method="POST",
        headers={"Content-Type": "application/json"},
    )
    if os.environ.get("ELEVENLABS_API_KEY"):
        req.add_header("xi-api-key", os.environ["ELEVENLABS_API_KEY"])
    with urllib.request.urlopen(req, timeout=120) as r, open(out, "wb") as f:
        f.write(r.read())
    print("saved:", out)

if __name__ == "__main__":
    main()
