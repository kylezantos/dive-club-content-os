# Dive Club Content OS

## Project Goal
Train an analysis system to match Ridd's voice using 11 past episodes with comprehensive training materials including cleaned transcripts, final deliverables, and reflective brain dumps.

## Current Status
**All transcripts cleaned** ✅ following standardized 9-step process
**Episode deliverables normalized** ✅ and organized into structured training folders
**Topic headers added (experimental):** ✅ 4 episodes with descriptive section headers for AI navigation feedback
- Nad Ridd interview (37 topic sections)
- Soleio Ridd interview (20 topic sections) 
- Thiago Costa interview (20 topic sections)
- Vitaly Friedman interview (20 topic sections)

**Voice pattern analysis completed** ✅ using specialized AI agents:
- Voice analysis (patterns, phrases, structural elements)
- Editorial analysis (preferences, decision-making patterns)
- Pattern synthesis (actionable templates and guidelines)
- QA review (validation and evidence quality)

**Remaining work:**
- 🔄 Apply topic headers to 7 remaining transcripts (andrei, balint, chris, figma-make, gavin, meng, mig)
- 📝 Implement voice matching system using analyzed patterns
- 🧪 Test voice authenticity scoring (target: 7+/10)

## Training Data Structure
Each episode contains:
1. **Raw transcript** - Original conversation recording
2. **Cleaned transcript** - Processed following 10-step cleaning procedure with topic headers for AI navigation
3. **Newsletter content** - Titles, hooks, descriptions, bullet points, key takeaways
4. **Reflective brain dump** - Ridd's contextual opinions and thoughts on the output quality

## Workflow
1. ✅ Clean transcripts using standardized process (see /prompt-templates/transcript-cleaner-prompt.md)
2. ✅ Add descriptive topic headers for AI navigation (experimental - 4 episodes completed for feedback)
3. ✅ Organize episodes into structured training folders
4. 🔄 Apply topic headers to remaining 7 episodes based on feedback
5. ✅ Extract voice patterns from final deliverables using AI agents
6. ✅ Create comprehensive analysis with specialized agents (voice, editorial, synthesis, QA)
7. 📝 Implement voice matching system using pattern analysis
8. 🧪 Test voice authenticity scoring (target: 7+/10)

## Key Principle
Brain dumps included with future episodes provide editorial direction at a high level (what topics seem interesting to write about, AKA "what to say"). The challenge is matching Ridd's voice (how to say it). The reflective brain dumps included in the files we already have were done after the release of these episodes, but add crucial context about output quality and editorial decisions and things he liked and didn't like.

## File Structure
```
/raw-transcripts/          - Original recordings
/cleaned-transcripts/      - Processed with topic headers (4/11 complete)
/prompt-templates/         - Cleaning instructions
/training-data/episodes/   - Organized episode folders (11 episodes)
  ├── episode-01-nad-chishtie/      ✅ (37 topic headers)
  ├── episode-02-soleio/            ✅ (20 topic headers)
  ├── episode-03-thiago-costa/      ✅ (20 topic headers)
  ├── episode-04-vitaly-friedman/   ✅ (20 topic headers)
  ├── episode-05-andrei-herasimchuk/  🔄 (needs topic headers)
  ├── episode-06-balint-orosz/        🔄 (needs topic headers)
  ├── episode-07-chris-abad/          🔄 (needs topic headers)
  ├── episode-08-figma-make/          🔄 (needs topic headers)
  ├── episode-09-gavin-nelson/        🔄 (needs topic headers)
  ├── episode-10-meng-to/             🔄 (needs topic headers)
  └── episode-11-mig-reyes/           🔄 (needs topic headers)
/voice-patterns/           - AI-generated voice analysis (v2 files are primary)
  ├── ridd-voice-analysis-v2.md       - Voice patterns and phrases
  ├── ridd-editorial-analysis-v2.md   - Editorial preferences
  ├── ridd-pattern-synthesis-v2.md    - Actionable templates
  ├── ridd-qa-review-v2.md           - Quality validation
  ├── pattern-reference.json         - Structured pattern data
  ├── pattern-reference-guide.md     - Implementation guide
  └── old-vp-files/                  - Archived analysis files
/episode-training-data/    - Legacy deliverables (now organized above)
```

## Target
7+/10 voice authenticity score using comprehensive training dataset