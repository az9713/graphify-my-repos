# Transcript to Notebook

Convert an arbitrary timestamped transcript file into a self-contained,
interactive HTML notebook designed for active viewing.

Keep the video in one window and the notebook in another. Edit awkward source
text, highlight important passages, attach margin comments, insert your own
notes, and paste screenshots beside the exact idea they illustrate.

## Interactive note-taking

- **Edit the transcript directly.** Insert, rewrite, or delete text while you
  watch.
- **Highlight passages.** Apply a yellow highlighter without creating a
  comment, and erase highlights independently.
- **Write margin comments.** Select a passage, attach a comment, and jump
  between the note and its source text.
- **Insert note blocks.** Add your own prose between transcript paragraphs.
- **Insert screenshots.** Choose an image or paste one with
  <kbd>Ctrl</kbd>+<kbd>V</kbd>, add a caption, and display it at compact, wide,
  or full width.
- **Navigate quickly.** Move by detected chapter, search the transcript, or
  enter focus mode.
- **Configure the reader.** Change typeface, text size, line height, text
  width, color mode, and accent color.
- **Work locally.** The generated notebook has no runtime dependencies and
  sends nothing to a server.

## Quick start

Node.js 18 or newer is required. The generator has no third-party runtime
packages.

```powershell
git clone https://github.com/az9713/transcript-to-notebook.git
cd transcript-to-notebook
node .\build_transcript_notebook.js "C:\path\to\my interview.vtt"
```

The input is a transcript **file path**, not a specially named folder. The
filename and extension may be arbitrary. By default, the output is written
beside the input:

```text
C:\path\to\my-interview_notebook.html
```

Choose an explicit output file:

```powershell
node .\build_transcript_notebook.js ".\captures\session.log" `
  --output ".\notebooks\research-session.html"
```

Or pass an output directory; it will be created when necessary:

```powershell
node .\build_transcript_notebook.js ".\captures\session.log" `
  --output ".\notebooks"
```

Run `node .\build_transcript_notebook.js --help` for every option.

## Supported transcript structures

Parsing is content-based. No behavior depends on a known person, video,
folder, or filename.

The same generic path handles:

- explicit `Chapter`, `Section`, or `Part` markers;
- Markdown section headings;
- compact timestamp lines such as `02:14 Speaker: text`;
- bracketed cues such as `[00:02:14] Speaker: text`;
- verbose timestamp prefixes exported by video transcript interfaces;
- SRT and WebVTT timing cues; and
- unchaptered transcripts, which become one complete `Transcript` section.

When explicit section markers exist, the generator preserves them as notebook
navigation. Otherwise, it uses the one-section fallback rather than dropping
unclassified content. Source URLs and useful preamble text become notebook
metadata.

Normalization is deliberately conservative. It removes timestamp syntax,
known transcript-interface labels, lowercase filler pauses, obvious repeated
function-word stutters, and spacing artifacts. It does not contain
domain-specific spelling corrections or rewrite proper nouns and technical
facts. Correct any remaining source errors directly in the notebook.

## Optional metadata

Place `notebook.config.json` beside the transcript, or select another file with
`--config`:

```json
{
  "title": "Research Interview",
  "brand": "Field Research Notebook",
  "author": "A. Researcher",
  "description": "Notes from the instrumentation interview.",
  "sourceUrl": "https://example.com/video",
  "exportStem": "research-interview",
  "storageKey": "my-stable-notebook-key"
}
```

CLI options such as `--title`, `--brand`, and `--author` override config-file
values. Without metadata, the title, branding, and export filenames are safely
derived from the input filename. The browser autosave key is a stable hash of
the resolved input path, preventing collisions between unrelated transcripts.

## Working with screenshots

Place the cursor near the relevant paragraph and either:

1. Choose **Image** and select a PNG, JPEG, WebP, or GIF; or
2. Copy a screenshot, click inside the transcript, and press
   <kbd>Ctrl</kbd>+<kbd>V</kbd>.

Images are resized to a maximum dimension of 1,600 pixels, compressed, and
embedded directly into notebook state. Add a caption and choose compact, wide,
or full-width presentation.

## Saving and exporting

Text edits, highlights, comments, inserted notes, screenshots, and appearance
settings autosave in the current browser.

Browser autosave does **not** rewrite the generated HTML file on disk. Use the
controls panel for a durable or portable copy:

- **Export HTML** downloads a self-contained edited notebook.
- **Backup notes** downloads the complete notebook state as JSON.
- **Restore backup** loads a previous JSON backup.
- **Print / PDF** creates a reading copy.

Wait for the status indicator to say **Saved** before reloading. Browser data
can be cleared or isolated between browsers, so export important work
regularly. The notebook warns when embedded screenshots approach the browser's
storage limit.

## Keyboard shortcuts

| Action | Shortcut |
|---|---|
| Find in transcript | <kbd>Ctrl</kbd>+<kbd>F</kbd> |
| Add margin comment | <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>M</kbd> |
| Highlight selection | <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>H</kbd> |
| Undo | <kbd>Ctrl</kbd>+<kbd>Z</kbd> |
| Redo | <kbd>Ctrl</kbd>+<kbd>Y</kbd> |

## Tests

```powershell
npm test
```

The fixture suite covers three materially different structures and multiple
arbitrary filenames. It verifies section extraction, no-chapter fallback,
conservative normalization, output paths, config metadata, every core
interactive control, and syntax validity of the embedded notebook JavaScript.

## Repository privacy

Common raw-transcript formats, default generated notebooks, browser exports,
and backup files are ignored. Arbitrarily named inputs and custom output paths
cannot be identified safely by filename alone, so review `git status` before
committing. An exported notebook may contain personal notes and embedded
screenshots; review it before sharing.
