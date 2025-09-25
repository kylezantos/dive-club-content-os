# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**First Action:** Always read `instructions.md` in addition to this document to understand the complete workflow when processing new raw transcripts and the process it goes through.

## Project Overview
Content analysis system for Ridd's voice pattern identification using 11 podcast episodes. The project extracts voice characteristics from newsletter deliverables and brain dumps to create authentic content matching templates.

## Key Commands

### Data Processing
- `python3 scripts/extract_patterns.py` - Extract voice patterns from episode deliverables to JSON
- `python3 scripts/run_voice_analysis.py` - Full pipeline orchestration (extraction + agent prep)
- `python3 scripts/run_voice_analysis_with_agents.py` - Agent-based analysis workflow

### File Operations
No build/lint/test commands - this is a data processing and analysis project.

## Architecture

### Data Flow
1. **Raw Data**: `/episode-deliverables/` contains 11 markdown files with titles, hooks, highlights, takeaways, and Ridd's editorial brain dumps
2. **Pattern Extraction**: Python scripts parse markdown files into structured JSON patterns
3. **AI Analysis**: Specialized agents analyze patterns for voice characteristics, editorial preferences, and synthesis templates
4. **Output**: Voice matching templates and reference guides in `/voice-patterns/`

### Key Components
- **VoicePatternExtractor** (`scripts/extract_patterns.py`): Main data parser that converts 11 markdown deliverables into structured pattern data
- **Specialized Agents** (`.claude/agents/`): Voice analyst, editorial analyst, pattern synthesizer, and QA reviewer for deep analysis
- **Reference System** (`voice-patterns/pattern-reference-guide.md`): Actionable templates for voice replication

### Agent System
The project uses 5 specialized AI agents:
- `voice-pattern-analyst`: Identifies distinctive voice patterns from content samples
- `editorial-analyst`: Extracts editorial preferences from brain dump reflections  
- `ridd-deliverables-creator`: Transforms podcast transcripts into newsletter content
- `voice-pattern-synthesizer`: Creates actionable templates from analysis
- `qa-voice-pattern-reviewer`: Validates analysis quality and evidence

### Data Structure
- `/episode-deliverables/`: Final newsletter content + Ridd's reflective commentary
- `/voice-patterns/`: AI-generated analysis files (v2 files are primary)
- `/extracted_data/`: JSON output from pattern extraction
- `/scripts/`: Python data processing utilities
- `/agents/`: Local copies of agent definitions

## Working with Voice Patterns
- Brain dump sections are gold standard - they contain Ridd's unfiltered editorial thinking
- All patterns require 3+ episode frequency to be considered significant
- "a *lot* more" is the primary signature phrase (7/11 episodes)
- Focus on actionable specificity over generic observations

## Key Principles
- Voice analysis prioritizes authenticity over generic "good writing"
- Every pattern must be backed by specific textual evidence
- Editorial brain dumps reveal decision-making patterns crucial for voice matching
- Target: 7+/10 voice authenticity score using comprehensive training dataset