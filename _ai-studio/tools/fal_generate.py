#!/usr/bin/env python3
"""Run any fal.ai model (Veo, Kling, Seedance, Flux, Nano Banana, Recraft...) and download the outputs.

Usage:
  FAL_KEY=... python3 fal_generate.py <model-id> '<json-args>' [--out DIR]
Examples:
  python3 fal_generate.py fal-ai/veo3.1 '{"prompt":"...","duration":"8s","aspect_ratio":"9:16"}'
  python3 fal_generate.py fal-ai/flux-pro/v1.1-ultra '{"prompt":"...","aspect_ratio":"4:5"}'
Model ids and their arguments are listed on each model page at https://fal.ai/models.
"""
import json, os, sys, time, pathlib, urllib.request

def call(url, data=None, key=None):
    req = urllib.request.Request(url, method="POST" if data is not None else "GET")
    req.add_header("Authorization", f"Key {key}")
    req.add_header("Content-Type", "application/json")
    body = json.dumps(data).encode() if data is not None else None
    with urllib.request.urlopen(req, body, timeout=120) as r:
        return json.loads(r.read())

def find_urls(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "url" and isinstance(v, str) and v.startswith("http"):
                yield v
            else:
                yield from find_urls(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from find_urls(v)

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--out")]
    out = pathlib.Path(sys.argv[sys.argv.index("--out") + 1]) if "--out" in sys.argv else pathlib.Path("output")
    if "--out" in sys.argv:
        args.remove(str(out))
    if len(args) < 2:
        sys.exit(__doc__)
    key = os.environ.get("FAL_KEY") or sys.exit("FAL_KEY is not set")
    model, payload = args[0], json.loads(args[1])
    job = call(f"https://queue.fal.run/{model}", payload, key)
    print("queued:", job.get("request_id"), flush=True)
    while True:
        status = call(job["status_url"], key=key)
        if status.get("status") == "COMPLETED":
            break
        if status.get("status") not in ("IN_QUEUE", "IN_PROGRESS"):
            sys.exit(f"failed: {status}")
        time.sleep(5)
    result = call(job["response_url"], key=key)
    out.mkdir(parents=True, exist_ok=True)
    (out / f"{job['request_id']}.json").write_text(json.dumps(result, indent=2, ensure_ascii=False))
    for i, url in enumerate(find_urls(result)):
        name = out / f"{job['request_id']}_{i}{pathlib.Path(url.split('?')[0]).suffix}"
        urllib.request.urlretrieve(url, name)
        print("saved:", name)

if __name__ == "__main__":
    main()
