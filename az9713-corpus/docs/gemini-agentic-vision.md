---
repo: gemini-agentic-vision
description: Demonstration of Google's Agentic Vision capability in Gemini 3 Flash
language: Python
stars: 1
forks: 0
created: 2026-01-28
updated: 2026-02-20
topics: 
is_fork: False
kb: 3
---

# gemini-agentic-vision
# Gemini Agentic Vision Demo

A demonstration of Google's **Agentic Vision** capability in Gemini 3 Flash, which transforms static image understanding into an active, iterative investigation process.

## What is Agentic Vision?

Agentic Vision is a new feature in Gemini 3 Flash that allows the model to dynamically inspect and manipulate images step-by-step, rather than processing them in a single pass. It uses a **Think-Act-Observe** loop:

1. **Think**: The model analyzes the query and image, formulating a multi-step plan
2. **Act**: Generates and executes Python code (using Pillow) to manipulate images - zoom, crop, rotate, annotate
3. **Observe**: The transformed image is added to context for further inspection; the loop repeats until the task is complete

### Key Benefits

- **5-10% quality boost** across vision benchmarks when code execution is enabled
- Better accuracy for counting objects, reading fine details, and parsing complex data
- Grounds answers in visual evidence through active investigation

### Use Cases

- Object counting with bounding box annotations
- Reading gauges, serial numbers, and street signs by zooming in
- Parsing high-density tables and complex charts
- Industrial inspection (e.g., insurance underwriting, detecting vehicle damage)

## Setup

### 1. Create a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (macOS/Linux)
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install google-genai
```

See the package documentation: https://pypi.org/project/google-genai/

### 3. Set Up Your API Key

You need a **Google API Key** to use the Gemini API.

1. Get your API key from [Google AI Studio](https://aistudio.google.com/)
2. Create a `.env` file in the project root:

```
GOOGLE_API_KEY=your_api_key_here
```

## Usage

Run the demo script:

```bash
python agentic_vision.py
```

## Test Image

The demo uses an **impossible shape** image to test the model's visual reasoning capabilities:

![Impossible Shape](https://cdn.pixabay.com/photo/2023/06/13/13/12/impossible-shape-8060935_1280.jpg)

Source: https://cdn.pixabay.com/photo/2023/06/13/13/12/impossible-shape-8060935_1280.jpg

## Sample Output

The `agentic_vision.py` script was run **twice** to demonstrate the model's analysis. Both runs successfully identified the impossible object, with slightly different explanations:

---

### Run 1 Response

> **Warning:** there are non-text parts in the response: ['thought_signature', 'executable_code', 'code_execution_result', 'inline_data', 'inline_data', 'thought_signature'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.

The image depicts an **impossible object**, a type of optical illusion where a 3D shape is drawn in a way that cannot exist in real physical space. Specifically, it is a variation of the **impossible cube** or **Penrose rectangle**.

The primary "wrong" things about this image include:

1. **Contradictory Overlaps (The Outer Frame):** If you follow the connections of the rectangular loop, you will notice a series of impossible overlaps at the corners. For example, at the top-left corner, the vertical beam appears to be in front of the horizontal one. However, following the loop around to the other corners shows a cycle of "in front of" and "behind" relationships that logically cannot close in three dimensions.

2. **Impossible Intersection:** Look at the long horizontal beam passing through the center:
   - On the **left side**, the horizontal beam is clearly **in front of** the vertical structure.
   - On the **right side**, the vertical structure is clearly **in front of** the horizontal beam.

   For a single, straight horizontal beam and a rigid vertical frame, this "twist" is physically impossible.

3. **Perspective Paradox:** The wood grain and shadows are rendered consistently to trick your brain into seeing depth, but the actual geometry of how the pieces connect violates the rules of Euclidean 3D space. It creates a "loop" where one side is simultaneously closer to and further away from the viewer than the opposite side.

---

### Run 2 Response

> **Warning:** there are non-text parts in the response: ['thought_signature', 'executable_code', 'code_execution_result', 'inline_data', 'inline_data', 'thought_signature'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.

The image depicts an **impossible object**, a type of optical illusion where a 3D shape is drawn in a way that cannot exist in real physical space. Specifically, it is a variation of the **impossible cube** or **Penrose rectangle**.

The primary "wrong" things about this image include:

1. **Contradictory Overlaps (The Outer Frame):** If you follow the connections of the rectangular loop, you will notice a series of impossible overlaps at the corners. For example, at the top-left corner, the vertical beam appears to be in front of the horizontal one. However, following the loop around to the other corners shows a cycle of "in front of" and "behind" relationships that logically cannot close in three dimensions.

2. **Impossible Intersection:** Look at the long horizontal beam passing through the center:
   - On the **left side**, the horizontal beam is clearly **in front of** the vertical structure.
   - On the **right side**, the vertical structure is clearly **in front of** the horizontal beam.

   For a single, straight horizontal beam and a rigid vertical frame, this "twist" is physically impossible.

3. **Perspective Paradox:** The wood grain and shadows are rendered consistently to trick your brain into seeing depth, but the actual geometry of how the pieces connect violates the rules of Euclidean 3D space. It creates a "loop" where one side is simultaneously closer to and further away from the viewer than the opposite side.

---

Both runs demonstrate the model's ability to use Agentic Vision (code execution with image manipulation) to analyze and reason about the impossible geometry in the image.

## References

- **Inspiration**: This demo is inspired by the YouTube video [Google UNLOCKs a NEW frontier!](https://www.youtube.com/watch?v=28ZfucX-hfs) by 1littlecoder
- **Google Blog**: [Introducing Agentic Vision in Gemini 3 Flash](https://blog.google/innovation-and-ai/technology/developers-tools/agentic-vision-gemini-3-flash/)
- **Google AI Studio**: https://aistudio.google.com/

## License

This is a demo project for educational purposes.
