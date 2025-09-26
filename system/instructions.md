# Dive Club Content Processing Instructions

## Overview

This document provides step-by-step instructions for processing new podcast interviews with Ridd's voice pattern analysis system. The workflow transforms raw transcripts and brain dumps into newsletter content that matches Ridd's authentic voice.

### Inputs Required
- **Raw transcript** - Unprocessed conversation recording
- **Brain dump document** - Ridd's post-interview reflections and editorial commentary

### Outputs Generated
- **Cleaned transcript** with topic headers for AI navigation
- **Newsletter content** (titles, hooks, descriptions, highlights, key takeaways)
- **Voice-matched content** using analyzed patterns (optional)

---

## Phase 1: Data Preparation

### Step 1.1: Create Episode Folder
```bash
# Navigate to training data directory
cd training-data/episodes/

# Create new episode folder (use guest's name)
mkdir episode-XX-firstname-lastname/
```

---

## Phase 2: Transcript Cleaning

### Step 2.1: Apply 10-Step Cleaning Process
Use the standardized process from `prompt templates/transcript-cleaner-prompt.md`:

1. Remove pre/post conversation setup
2. Standardize speaker labels (Host: "Ridd", Guest: "First Last")
3. Clean up false starts and filler words
4. Preserve complete thoughts and quotes
5. Mark clear topic transitions with "---"
6. Remove technical interruptions
7. Keep timestamps next to speaker labels
8. Add header with guest info and topics
9. Save as `*-cleaned.txt`
10. **Add descriptive topic headers** after each "---" section

### Step 2.2: Add Topic Headers
Format: `### [Brief descriptive sentence about the topic discussed in this section]`

Examples from existing transcripts:
- `### Journey to Lovable through LLM experimentation and discovering GPT Engineer`
- `### Technical background and engineering-minded approach to design`
- `### Being the sole designer at Europe's fastest growing startup`

### Step 2.3: Quality Check
- Verify all speakers are correctly labeled
- Ensure topic headers accurately describe each section
- Confirm timestamps are preserved
- Check that key quotes remain intact

---

## Phase 3: Deliverables Creation (Automated)

### Step 3.1: Register Deliverables Creator Agent
```bash
# Use Claude Code's /agents command to register the deliverables creator
/agents
# Select deliverables_creator from the list to create persistent subagent
```

### Step 3.2: Generate Deliverables with Voice Matching
Use the deliverables_creator agent to automatically generate voice-matched content:

**Input to Agent:**
- Cleaned transcript with topic headers
- Guest information (name, role, company)
- Key topics and notable quotes

**Agent Output:**
- Main title + 3 alternatives using Ridd's voice patterns
- Personal/engaging hook with curiosity generation
- 5-6 specific highlights ending with "a *lot* more"
- Unexpected newsletter title + practical subtitle
- 3 substantial key takeaways with direct quotes
- Structured deliverables file ready for review

### Step 3.3: Quality Validation
The agent automatically applies:
- **Voice Authenticity:** Signature phrases, personal authority, conversational tone
- **Editorial Standards:** Curiosity gaps, tactical depth, specific details
- **Pattern Integration:** Question hooks, transformation language, first-person authority
- **Quality Checks:** Avoids generic content, maintains 7+/10 authenticity target

### Step 3.4: Manual Review
Review generated deliverables for:
- Accuracy of quotes and details from transcript
- Guest name and company information
- Flow and readability of key takeaways
- Any interview-specific nuances to adjust

---

## Phase 4: Pattern Analysis (For Training Data)

*Note: This phase is for expanding the training dataset. Skip if only creating content.*

### Step 4.1: Data Extraction
Extract patterns from deliverables into JSON format for agent processing.

### Step 4.2: Voice Analysis Agent
**Purpose:** Identify distinctive voice characteristics
**Input:** JSON pattern data from all episodes
**Output:** Voice pattern analysis with signature phrases, structures, and authenticity markers

```bash
# Using Claude Code subagents
# Run: Voice Pattern Analyst agent with extracted data
```

### Step 4.3: Editorial Analysis Agent
**Purpose:** Extract editorial preferences from brain dumps
**Input:** Brain dump content across episodes
**Output:** Editorial decision-making patterns and quality standards

### Step 4.4: Pattern Synthesis Agent
**Purpose:** Create actionable templates and guidelines
**Input:** Voice and editorial analysis outputs
**Output:** Practical implementation frameworks

### Step 4.5: QA Review Agent
**Purpose:** Validate analysis quality and evidence
**Input:** All agent outputs
**Output:** Quality validation report with improvement suggestions

---

## Phase 5: Voice Matching (For Production Content)

### Step 5.1: Use Analyzed Patterns
Apply patterns from `voice-patterns/` directory:
- `ridd-voice-analysis-v2.md` - Core voice patterns
- `ridd-editorial-analysis-v2.md` - Editorial preferences
- `ridd-pattern-synthesis-v2.md` - Implementation guidelines
- `pattern-reference.json` - Structured pattern data

### Step 5.2: Content Generation
Generate content using identified patterns:
- Signature phrases ("a *lot* more", transformational language)
- Structural elements (question-hook openings, parenthetical asides)
- Editorial perspective (personal authority, practical framing)
- Conversational authenticity (direct reader address, casual language)

### Step 5.3: Voice Authenticity Scoring
Evaluate generated content against the 7+/10 authenticity target:
- Distinctiveness vs. generic content
- Pattern consistency with training data
- Natural flow and conversational feel
- Editorial alignment with Ridd's preferences

---

## Phase 6: Review & Refinement

### Step 6.1: Ridd's Review Process
Present deliverables to Ridd for feedback focusing on:
- Title effectiveness and curiosity generation
- Hook engagement and personal voice
- Highlight specificity and value
- Key takeaway depth and actionability
- Overall voice authenticity

### Step 6.2: Iterative Improvement
Based on Ridd's feedback:
- Adjust content to match preferences
- Refine voice patterns if systematic issues emerge
- Update guidelines for future content

### Step 6.3: Final Deliverables
Finalize content for publication:
- Newsletter title and subtitle
- Episode description and highlights
- Key takeaways for social/content distribution

---

## Agent Reference

### Claude Code Subagents Available
Use `/agents` command to access:
- **voice-pattern-analyst** - Analyzes writing samples for distinctive voice patterns
- **editorial-analyst** - Extracts editorial preferences from brain dumps
- **voice-pattern-synthesizer** - Transforms analysis into actionable templates
- **qa-voice-pattern-reviewer** - Validates analysis quality and evidence

### Agent Descriptions (from `/agents` folder)
- `deliverables_creator.md` - **[PRIMARY]** Generates voice-matched deliverables from cleaned transcripts
- `voice_analyst.md` - Identifies recurring patterns and conversational authenticity (for training)
- `editorial_analyst.md` - Deep dives into brain dumps for editorial philosophy (for training)
- `pattern_synthesizer.md` - Creates implementation frameworks (for training)
- `qa_reviewer.md` - Quality validation and evidence checking (for training)

---

## File Templates

### Raw Transcript Header Template
```
# Dive Club Interview: [Guest Full Name]
## Episode Notes
**Host:** Ridd
**Guest:** [Guest Full Name] ([Title], [Company])
**Topics:** [3-4 main topic areas discussed]

---
```

### Topic Header Examples
```
### [Action/Journey] through [specific context/method]
### [Technical/Professional aspect] and [philosophical approach]  
### [Role/Responsibility] at [specific context/achievement]
```

---

## Common Issues & Troubleshooting

### Transcript Cleaning Issues
- **Overlapping speakers:** Mark with [overlapping] and clean up in post
- **Technical terms:** Preserve exact spelling for industry terms
- **Unclear audio:** Mark with [unclear] rather than guessing

### Voice Matching Issues
- **Too generic:** Add more specific details and personal references
- **Wrong tone:** Check against editorial preferences in brain dumps
- **Pattern overuse:** Balance signature phrases with natural variation

### Content Quality Issues
- **Weak hooks:** Reference specific tools/outcomes mentioned in interview
- **Vague highlights:** Add concrete examples and metrics where available
- **Short takeaways:** Expand with additional context and implementation details

---

## Success Metrics

- **Voice Authenticity:** 7+/10 score when compared to original Ridd content
- **Editorial Alignment:** Matches preferences expressed in brain dumps
- **Reader Engagement:** Creates curiosity gaps and actionable value
- **Pattern Consistency:** Uses identified signature elements naturally
- **Content Quality:** Specific, tactical, and transformation-focused

---

*Last Updated: 09/03/25*
*System Version: Voice Pattern Analysis v2*