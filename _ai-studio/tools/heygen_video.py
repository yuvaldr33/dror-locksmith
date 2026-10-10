#!/usr/bin/env python3
"""Generate a talking-presenter video with the HeyGen API and download it.

Usage:
  HEYGEN_API_KEY=... python3 heygen_video.py <avatar_id> <voice_id> "<script>" out.mp4 [9:16|16:9]
List your avatars/voices: GET https://api.heygen.com/v2/avatars and /v2/voices.
Endpoints follow HeyGen API v2; check https://docs.heygen.com if a call is rejected.
"""
import json, os, sys, time, urllib.request

API = "https://api.heygen.com"

def call(path, data=None):
    req = urllib.request.Request(API + path, method="POST" if data else "GET",
                                 headers={"X-Api-Key": os.environ["HEYGEN_API_KEY"],
                                          "Content-Type": "application/json"})
    with urllib.request.urlopen(req, json.dumps(data).encode() if data else None, timeout=120) as r:
        return json.loads(r.read())

def main():
    if len(sys.argv) < 5 or "HEYGEN_API_KEY" not in os.environ:
        sys.exit(__doc__)
    avatar, voice, script, out = sys.argv[1:5]
    w, h = (1080, 1920) if (sys.argv[5] if len(sys.argv) > 5 else "9:16") == "9:16" else (1920, 1080)
    job = call("/v2/video/generate", {
        "video_inputs": [{
            "character": {"type": "avatar", "avatar_id": avatar, "avatar_style": "normal"},
            "voice": {"type": "text", "input_text": script, "voice_id": voice},
        }],
        "dimension": {"width": w, "height": h},
    })
    vid = job["data"]["video_id"]
    print("rendering:", vid, flush=True)
    while True:
        st = call(f"/v1/video_status.get?video_id={vid}")["data"]
        if st["status"] == "completed":
            urllib.request.urlretrieve(st["video_url"], out)
            print("saved:", out)
            return
        if st["status"] == "failed":
            sys.exit(f"failed: {st.get('error')}")
        time.sleep(10)

if __name__ == "__main__":
    main()
