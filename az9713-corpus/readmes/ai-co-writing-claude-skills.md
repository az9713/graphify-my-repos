# AI Co-Writing System

A complete Claude Code writing system for content creators, based on context engineering principles.

## Quick Start

1. Open this folder in Cursor (or your preferred editor with Claude Code)
2. Run the context profile creators to set up your profiles
3. Start writing with Claude as your co-writer

## Folder Structure

```
my-writing-system/
├── .claude/
│   ├── skills/                 # Claude Skills (packaged expertise)
│   │   ├── business-profile-creator/
│   │   ├── how-to-guide/
│   │   ├── icp-creator/
│   │   ├── linkedin-post/
│   │   ├── linkedin-profile-optimizer/
│   │   ├── sales-email-sequence/
│   │   ├── social-media-bio-generator/
│   │   ├── substack-note/
│   │   ├── thought-leadership/
│   │   ├── twitter-thread/
│   │   └── voice-dna-creator/
│   └── agents/                 # Future: Autonomous workflows
├── context/                    # Your context profiles
│   ├── voice-dna.json         # How you sound
│   ├── icp.json               # Who you write for
│   └── business-profile.json  # What you offer
├── knowledge/                  # Your content brain
│   ├── drafts/                # Work in progress
│   ├── notes/                 # Ideas and research
│   └── archive/               # Published content
├── claude.md                   # System instructions (auto-loaded)
└── README.md                   # This file
```

## Setup Instructions

### Step 1: Create Your Context Profiles

Run these skills in Claude Code to create your profiles:

1. **Voice DNA**: Say "Help me create my voice DNA profile"
   - Attach 3-10 writing samples
   - Claude will analyze and create your voice profile

2. **ICP**: Say "Help me create my ICP"
   - Answer interview questions about your audience
   - Claude will generate your ideal client profile

3. **Business Profile**: Say "Help me create my business profile"
   - Answer questions about your business
   - Claude will generate your business context

### Step 2: Add Your Content (Optional)

Add published content to `/knowledge/archive/` to help Claude:
- Learn more about your voice
- Avoid repeating content
- Reference past work for repurposing

### Step 3: Start Writing

Just ask Claude to write:
- "Write me a LinkedIn post about [topic]"
- "Create 10 Substack notes from my latest newsletter"
- "Help me write a thought leadership piece on [topic]"
- "Generate a Twitter thread about [topic]"

Claude will automatically:
1. Read your context profiles
2. Find relevant skills
3. Create content in your voice

## Available Skills

| Skill | Purpose |
|-------|---------|
| `voice-dna-creator` | Create voice profile from samples |
| `icp-creator` | Create ideal client profile |
| `business-profile-creator` | Create business context |
| `linkedin-post` | LinkedIn posts |
| `linkedin-profile-optimizer` | LinkedIn profile sections |
| `twitter-thread` | Twitter/X threads |
| `substack-note` | Substack notes |
| `thought-leadership` | Long-form thought pieces |
| `sales-email-sequence` | Email campaigns |
| `social-media-bio-generator` | Bios for any platform |
| `how-to-guide` | Tutorials and guides |

## Tips

1. **Start simple**: Create your 3 context profiles first
2. **Iterate**: Update your voice DNA as you refine your style
3. **Build knowledge**: Add more content to improve results over time
4. **Be specific**: Tell Claude exactly what you want
5. **Give feedback**: If output doesn't match, tell Claude what to adjust

## The Formula

**Context + Instructions = Quality Output**

- Context = Your profiles in `/context/`
- Instructions = Skills in `/.claude/skills/`
- Output = Content that sounds like you

## Resources

- Claude Code Documentation: https://code.claude.com/docs
- Agent Skills: https://code.claude.com/docs/en/skills

## Acknowledgement

This repository is inspired by the YouTube video ["Claude Code Masterclass: Build Your AI Co-Writing System"](https://www.youtube.com/watch?v=Ip566JVP_30&t=1s) by Alex McFarland.

---

Built with Claude Code. Context engineering > Prompt engineering.
