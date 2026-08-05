---
repo: akaunting-gmail-skills
description: AI Accounting Agent: Browser-based automation using Claude Code + Claude in Chrome to create invoices in Akaunting and send them via Gmail
language: None
stars: 0
forks: 0
created: 2026-02-18
updated: 2026-02-18
topics: 
is_fork: False
kb: 23
---

# akaunting-gmail-skills
# AI Accounting Agent

Browser-based accounting automation using **Claude Code** + **Claude in Chrome**. No APIs required - the agent interacts with web applications purely through browser automation, filling forms, clicking buttons, and navigating pages just like a human would.

## Inspiration

This project was inspired by the YouTube video **["Did My Claude Code AI Agent Automate a Six Figure Job?"](https://www.youtube.com/watch?v=7lyU_CKp3WA)** by All About AI. In that video, a Claude Code agent running on a Mac Mini demonstrates autonomous browser-based accounting workflows - creating invoices, downloading PDFs, sending emails, and logging bills - all without any API integrations.

Claude Code was asked to replicate the workflow introduced in that video. It produced two Claude Code Skills (`accounting/SKILL.md` and `gmail/SKILL.md`) that guide the browser automation agent through Akaunting and Gmail respectively.

## How It Works

The project uses **Claude Code Skills** - markdown instruction files that teach the AI agent how to navigate specific web applications. When a user gives a natural language prompt, Claude Code:

1. Invokes the relevant skill (`/accounting` or `/gmail`)
2. Uses the **Claude in Chrome** MCP extension to control a Chrome browser
3. Takes screenshots to understand the current page state
4. Clicks, types, scrolls, and navigates just like a human operator
5. Reports back and asks for confirmation before irreversible actions (sending emails, downloading files)

## Project Structure

```
.
├── CLAUDE.md                          # Agent instructions & workflow definitions
├── README.md                          # This file
├── .claude/
│   └── skills/
│       ├── accounting/
│       │   └── SKILL.md               # Akaunting browser automation skill
│       └── gmail/
│           └── SKILL.md               # Gmail browser automation skill
└── docs/
    ├── README_transcript.txt          # Transcript of the source YouTube video
    └── gemini3_summary.txt            # AI-generated summary of the video workflow
```

## Requirements

- **Claude Code** CLI with an active subscription
- **Claude in Chrome** MCP extension installed and connected
- A **Gmail** account, logged in within the Chrome browser
- An **Akaunting** instance (e.g., `https://app.akaunting.com/{company-id}/`), logged in within the Chrome browser

## Skills

### `/accounting` - Akaunting Browser Automation

Handles all interactions with the Akaunting web application:

- **Create invoices**: Navigate to the invoice form, select or create customers, add line items, set prices, save as draft
- **Log bills**: Create vendor records, enter bill details from source documents
- **Manage contacts**: Create new customers and vendors inline or via dedicated pages
- **Download PDFs**: Locate and download invoice/bill PDFs from detail pages
- **Dashboard checks**: Verify receivables, payables, and cash flow after changes

### `/gmail` - Gmail Browser Automation

Handles all interactions with Gmail in the browser:

- **Scan inbox**: Search for emails containing invoices or bills
- **Read emails**: Open and extract content, sender info, amounts, and dates
- **Extract attachments**: Locate and download PDF attachments
- **Compose emails**: Create new messages with recipients, subjects, and body text
- **Attach files**: Locate the attach button and trigger the file picker
- **Send emails**: Click send with user confirmation

## Workflows

### Outbound: Create & Send Invoice

The primary tested workflow. Given a prompt like:

> "Create a draft invoice for customer Jane Miller for a $1,000 sponsorship job and email it to her"

The agent:
1. Invokes `/accounting` to navigate to Akaunting's invoice creation form
2. Creates the customer if they don't exist
3. Adds line items (e.g., "Sponsorship", qty 1, $1,000)
4. Saves the invoice as a draft
5. Downloads the invoice PDF (with user confirmation)
6. Invokes `/gmail` to open Gmail and compose a new email
7. Fills in the recipient, subject, and body
8. Attaches the PDF (requires user to select the file from the native file picker)
9. Sends the email (with user confirmation)
10. Returns to Akaunting and marks the invoice as "Sent"

### Inbound: Fetch & Log Bills

Designed but not yet tested in this repository. The intended flow:
1. Invoke `/gmail` to scan the inbox for emails with invoice/bill attachments
2. Extract sender, amount, date, and line items from the email or PDF
3. Invoke `/accounting` to create a vendor (if new) and log the bill
4. Navigate to the Akaunting Dashboard to verify updated Payables

## Testing

### Test Conducted: Outbound Invoice Workflow

The outbound workflow was tested end-to-end with the following prompt:

> "Create a draft invoice for customer [name] for a $1,000 sponsorship job and email it to him"

**Results**:
- The agent successfully completed the full workflow across both Akaunting and Gmail
- ~45 browser tool calls were made in total
- 4 errors were encountered and self-resolved by the agent (see below)
- 3 human interventions were required

### Human Interventions Required

| Step | Reason | Avoidable? |
|------|--------|------------|
| Akaunting URL correction | Agent guessed wrong URL; base URL was not stored in config | Yes - store URL in CLAUDE.md |
| PDF file attachment in Gmail | Native OS file picker cannot be controlled by browser automation | No - platform limitation |
| Send / Download confirmations | Required by Claude's security rules | No - intentional safety gates |

**Note on PDF attachment**: The steps of downloading the invoice PDF from Akaunting and manually attaching it in Gmail were not strictly necessary. Akaunting has a built-in "Send Email" feature that can email the invoice directly to the customer. Using Akaunting's native email would eliminate the need for the Gmail attachment step entirely.

### Errors Encountered & Self-Resolved

| Error | Root Cause | How Agent Resolved |
|-------|-----------|-------------------|
| Wrong Akaunting URL | Base URL not in config; agent guessed from repo name | User provided correct URL; agent retried |
| Price showed $10 instead of $1,000 | Formatted currency field partially overwrote typed value | Agent re-selected field, typed "1000.00" explicitly |
| Subject text entered in wrong Gmail field | Coordinate-based click hit the wrong field after dynamic reflow | Agent recovered draft from Gmail's auto-save |
| Compose window closed by Escape key | Escape closes compose window, not just popups | Agent reopened draft from Gmail's Drafts folder |

### Skill Effectiveness Ratings

- **Accounting Skill**: 7/10 - Invoice creation flow well-documented; gaps in currency input handling and onboarding popup dismissal
- **Gmail Skill**: 6/10 - Compose flow correct; file attachment section overstates capabilities (native file picker is a hard blocker)

A detailed session report with full click paths and analysis is available in `.ignore/browser_automation_session_report.md`.

## Customization

The two skills are currently hardcoded for **Akaunting** as the accounting platform and **Gmail** as the email client. To adapt this project for a different setup:

### Accounting Skill (`.claude/skills/accounting/SKILL.md`)

- **Platform**: Replace all Akaunting-specific instructions (URL paths, form field names, button labels, sidebar navigation) with those of your accounting software (e.g., QuickBooks, Xero, FreshBooks, Wave)
- **URL paths**: Update navigation routes like `/{company}/sales/invoices/create` to match your platform's URL structure
- **Form fields**: Update `find` queries and field selectors to match your platform's DOM (e.g., customer dropdowns, line item rows, price fields)
- **PDF download**: Adjust the download flow to match how your platform generates and exports documents

### Gmail Skill (`.claude/skills/gmail/SKILL.md`)

- **Email client**: If using a different email client (Outlook, etc.), rewrite the compose, attach, and send flows to match that client's web UI
- **Compose fields**: Update coordinate hints and `find` queries for the To, Subject, and Body fields
- **Attachment flow**: The native file picker limitation applies to all web email clients, not just Gmail

### CLAUDE.md

- **Base URL**: Update the Akaunting instance URL to your own (e.g., `https://app.akaunting.com/{your-company-id}/`)
- **Navigation paths**: Update the route reference table to match your platform
- **Workflow steps**: Adjust the outbound/inbound workflows if your accounting platform has different capabilities (e.g., built-in email sending)

## Limitations

- **No API integration**: All automation is browser-based, which makes it slower and more fragile than API-driven approaches. UI changes to Akaunting or Gmail may break the skills.
- **Native file picker**: The Claude in Chrome extension cannot interact with OS-level file dialogs. Attaching locally downloaded files always requires human intervention.
- **Login flows**: The agent assumes both Gmail and Akaunting are already logged in. It does not handle authentication.
- **Single-threaded**: The agent operates one tab at a time. It cannot perform parallel actions across multiple tabs.
- **Coordinate fragility**: Some actions use screen coordinates which may break at different screen resolutions or zoom levels. Using `find` queries is more robust.

## License

This project is for educational and demonstration purposes.
