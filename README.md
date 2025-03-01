# FastlyAIAccelerator-OpenAI

## OpenAI JSON Model
https://platform.openai.com/docs/api-reference/chat/object

## Fastly Doc 
https://docs.fastly.com/en/guides/about-the-ai-accelerator-page

## FYI 

Curl command for troubleshooting purposes.

```
curl -s -i https://ai.fastly.app/api.openai.com/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer $OPENAI_API_KEY" -H "Fastly-Key: $FASTLYTOKEN_AI" -H "X-Semantic-Cache-Key: my-test-key-0119c" -d '{"model": "gpt-4o-mini", "messages": [{"role": "user", "content": "What is wheather for today?"}] }'
HTTP/2 200
date: Sat, 01 Mar 2025 14:14:04 GMT
content-type: application/json
x-semantic-cache: MISS
access-control-expose-headers: X-Request-ID
openai-organization: test-1bkfpz
openai-processing-ms: 408
openai-version: 2020-10-01
x-ratelimit-limit-requests: 200
x-ratelimit-limit-tokens: 100000
x-ratelimit-remaining-requests: 196
x-ratelimit-remaining-tokens: 99777
x-ratelimit-reset-requests: 28m0.747s
x-ratelimit-reset-tokens: 1h36m16.107s
x-request-id: req_1cd77762e8da2615da2e76e35b64c469
strict-transport-security: max-age=31536000; includeSubDomains; preload
cf-cache-status: DYNAMIC
set-cookie: __cf_bm=oS8iMjfNp7nd1UpcXMXmVjLQ0FgsfRZB4WZ9ochMqAc-1740838444-1.0.1.1-g4P2pxh9Y6nJ3GmTZgW4LhB_xy5WgMHKULTEaNxehfoF9hqUGcqfzvFJXSwSg1w548wrLDBXeA9yNYP89qgj8Hs.yijXgKrtR7SuM8PQ2n0; path=/; expires=Sat, 01-Mar-25 14:44:04 GMT; domain=.api.openai.com; HttpOnly; Secure; SameSite=None
set-cookie: _cfuvid=frrNG1mpK5azQ7mbp.Hd6.GWxc2tqmDGd1ZwpC.fBp8-1740838444304-0.0.1.1-604800000; path=/; domain=.api.openai.com; HttpOnly; Secure; SameSite=None
x-content-type-options: nosniff
x-cache-hits: 0
cf-ray: 91994230fac4fd45-NRT
alt-svc: h3=":443"; ma=86400
x-cache: MISS
server: fastly cloudflare
x-served-by: cache-nrt-rjtf7700020-NRT
content-length: 951

{
  "id": "chatcmpl-B6HtLSCwFuOEHjtxeGMxgAxqPSx6L",
  "object": "chat.completion",
  "created": 1740838443,
  "model": "gpt-4o-mini-2024-07-18",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "I'm unable to provide real-time weather updates. I recommend checking a reliable weather website or using a weather app for the most current information for your location.",
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 14,
    "completion_tokens": 31,
    "total_tokens": 45,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    },
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "audio_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0
    }
  },
  "service_tier": "default",
  "system_fingerprint": "fp_06737a9306"
}

```
