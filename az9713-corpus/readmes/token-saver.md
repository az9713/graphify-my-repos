# Token Saver — Nate B. Jones's token-reduction strategies, explained

**Live explainer page: https://az9713.github.io/token-saver/**

An independent explainer and critique of the [Token Saver skill](https://unlock-ai.natebjones.com/guides/cut-token-waste) by Nate B. Jones — a skill for Codex and Claude Code that cuts token use without changing how you work.

## Sources

- **YouTube video:** [What's really happening inside your AI token limits?](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)
- **Substack article:** [I Built The Token Saver Skill To Cut My Token Use By 90%](https://natesnewsletter.substack.com/p/reduce-ai-token-usage)
- **Web guide:** [15 Ways to Cut Token Waste in Codex and Claude](https://unlock-ai.natebjones.com/guides/cut-token-waste) (Unlock AI)

## The problem

Every message you send to Codex or Claude re-sends the whole conversation: old answers, tool results, files, tool definitions, standing instructions. Nate's tracker logged **3.77 billion tokens in one day — 95.73% of it "reused input"** he never typed. His one matched-job test cut input + output by **85.77%** (51,712 reused input tokens → 0) while passing the same fact checklist.

## The eight strategies (from SKILL.md)

1. **Local code before a model.** Counting, sorting, exact search, format conversion — use `rg`, `jq`, or a script. Never ask a model to imitate a command.
2. **Select passages, not files.** Search first; send only matching chunks (the bundled `select_context.py` does this with zero model calls). A miss earns one more bounded passage — never a full-file load.
3. **Carry the accepted result, not the conversation.** Save the approved version (`state_delta.py`); build the next request from that result plus the one new change. Rejected drafts never ride along.
4. **Load tools lazily.** Tool definitions are input before the model does anything (~55k tokens in Anthropic's example multi-server setup). Load only what the job will call.
5. **Cheapest capable path.** Saved answer → local code → small model for bounded work → strong model for hard judgment. Never call a model to pick a model.
6. **Cache-friendly ordering.** Background that must repeat stays byte-identical at the front (provider cache pricing) — but shrink it first; cached input is still input.
7. **Answer sized to the request.** Asked for a sentence, return a sentence. Output is paid twice: once when written, again every turn it rides along.
8. **One bounded repair.** A failed check gets exactly one retry with minimal input. A token-limit failure is never retried — a second copy of an oversized request is still oversized.

Plus the accounting rule over all eight: **count the whole job** (fresh input, cached input, output, retries, model per call). Moving tokens to a cheaper model isn't a saving unless the combined total falls.

## The wider 15-move framework

The web guide expands these into 15 moves grouped by which cost they attack: stop carrying old conversation (edit/rewind, batch related questions, clean tasks, carry the result), load less (search before reading, lightest source form, settled procedures as code, return accepted answers), stop paying for waste (lazy tools, clean up old tool output, right-sized answers, whole-job model routing, hard stops on retries), cache last, and — beyond what any skill can do — a pre-call gateway (his "Ringer" project, currently Codex CLI only).

## Triggering the skill in Claude Code

Once installed (unzip to `~/.claude/skills/token-saver/`), the skill fires two ways: name it explicitly, or phrase the request so it matches the skill's description (plan limits, long chats, large files, lowering cost).

**Explicit — name it:**

> Use the token-saver skill for this job.

> Use token saver: summarize the decisions in `meeting-notes/2026-07/`.

**Implicit — describe the pain and it matches:**

> I keep hitting my plan limits. Find what we decided about the Wednesday deadline in `transcripts/` without reading the whole files.

> This chat is getting long and expensive. Continue the report we agreed on, but only change the intro to mention Q3 — don't rebuild the rest.

> What does this 2 MB log say about the auth failures? Keep token use low.

> Rewrite this workflow so it burns fewer tokens.

**What you'll see it do:** run `rg`/`select_context.py` before opening files, send a small packet to a worker instead of the full source, save your accepted result under `.token-saver/` and revise from that, keep answers to the length you asked, and refuse to retry oversized calls.

## What's in this repo

[`index.html`](index.html) — a single-page explainer ([view it live](https://az9713.github.io/token-saver/)) with:

- the measured numbers and their limits
- a flow diagram of how a job moves through the skill
- the 8 strategies, each with pointers to the code that implements it (only 3 of 8 are backed by real code; the rest are instructions)
- a tabbed line-by-line walkthrough of `SKILL.md` and all three Python scripts, each step annotated with exactly which tokens it saves
- a critique: 5 strengths, 5 weaknesses, 2 nits, and a verdict

The skill itself (SKILL.md + scripts) is distributed by Nate via the guide above and is not redistributed here.
