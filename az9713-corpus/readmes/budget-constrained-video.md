# The Last Lighthouse

A 47-second AI-generated movie trailer, made autonomously by an AI agent from a single prompt — *"suggest a video project that uses up my $5 fal.ai credit and 72 Higgsfield credits"* — for a total cost of **$5 + 72 credits**.

[![Watch the trailer](screenshot.jpg)](https://az9713.github.io/budget-constrained-video/)

**▶ [Watch the trailer (1440p)](https://az9713.github.io/budget-constrained-video/)** · [720p master](https://github.com/az9713/budget-constrained-video/raw/main/the_last_lighthouse.mp4) · [Poster](poster.png)

> *The water took everything. Except the light. For twenty years, he kept it burning — waiting for an answer. This year... something answered.*

## What this is

An experiment in **budget-constrained autonomous video production**: given only two prepaid balances and a high-level goal, an AI agent (Claude Code) chose the project, wrote the story, designed every frame, picked the models by price/performance, generated all assets, cut the film, verified it, and spent 97%+ of both budgets — with no human in the loop beyond picking the theme from four pitches.

The full creative and technical post-mortem is in **[DEVELOPMENT_JOURNEY.md](DEVELOPMENT_JOURNEY.md)** — every decision, price, prompt strategy, gotcha, and the 12 lessons learned.

## Pipeline

| Stage | Tool / model | Cost |
|---|---|---|
| 12 keyframes + poster | fal.ai · FLUX.1 [dev] | ~$0.30 |
| 6 voiceover lines | fal.ai · MiniMax Speech-02 HD | ~$0.02 |
| 47s score | fal.ai · Stable Audio | ~$0.05 |
| 11 animated shots | Higgsfield · Kling v3.0 (image-to-video, sound off) | 70.5 / 72.64 credits |
| 2× upscale to 2560×1440 | fal.ai · Topaz Video AI | ~$4+ (rest of the $5) |
| Edit, mix, verify | local ffmpeg + Python stdlib | $0 |

The core budgeting idea: **iterate where it's cheap, commit where it's expensive.** Every shot was designed and approved as a 2-cent FLUX still before a single ~50-cent video credit was spent animating it.

## Repository contents

```
the_last_lighthouse_1440p_web.mp4  # final film, web-compressed 1440p
the_last_lighthouse.mp4            # 720p master (original edit)
poster.png                         # FLUX-generated one-sheet
DEVELOPMENT_JOURNEY.md             # full post-mortem & lessons
shots.json                         # shot list + shared style string
gen_keyframes.py                   # FLUX keyframe generator (stdlib only)
gen_audio.py                       # VO + music generator (stdlib only)
upscale.py                         # Topaz queue submit/poll (stdlib only)
keyframes/                         # all 12 approved stills
clips/                             # all 11 Kling shots
audio/                             # 6 VO lines + score
```

To re-cut the film from the assets, see the ffmpeg concat + `filter_complex` recipe in [DEVELOPMENT_JOURNEY.md](DEVELOPMENT_JOURNEY.md) §8.

## Credits

Made with [fal.ai](https://fal.ai) (FLUX.1 dev, MiniMax Speech-02 HD, Stable Audio, Topaz Video AI) and [Higgsfield](https://higgsfield.ai) (Kling v3.0), orchestrated end-to-end by Claude Code.
