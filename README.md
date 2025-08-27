# Dive Club Content OS

## Project Goal
Train an analysis system to match Ridd's voice using 11 past episodes with comprehensive training materials including cleaned transcripts, final deliverables, and reflective brain dumps.

## Current Status
**All transcripts cleaned** following standardized 9-step process
**Episode deliverables normalized** and organized into structured training folders
**Topic headers added (experimental):** 4 episodes with descriptive section headers for AI navigation feedback
- Nad Ridd interview (37 topic sections)
- Soleio Ridd interview (20 topic sections) 
- Thiago Costa interview (24 topic sections)
- Vitaly Friedman interview (25 topic sections)

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
4. 🔄 Apply topic headers to remaining episodes based on feedback
5. Extract voice patterns from final deliverables
6. Create analysis agent based on patterns
7. Test voice matching accuracy

## Key Principle
Brain dumps included with future episodes provide editorial direction at a high level (what topics seem interesting to write about, AKA "what to say"). The challenge is matching Ridd's voice (how to say it). The reflective brain dumps included in the files we already have were done after the release of these episodes, but add crucial context about output quality and editorial decisions and things he liked and didn't like.

## File Structure
```
/raw-transcripts/          - Original recordings
/cleaned-transcripts/      - Processed with topic headers
/prompt-templates/         - Cleaning instructions
/training-data/episodes/   - Organized episode folders (11 episodes)
  ├── episode-01-nad-chishtie/
  ├── episode-02-soleio/
  ├── episode-03-thiago-costa/
  ├── episode-04-vitaly-friedman/
  ├── episode-05-andrei-herasimchuk/
  ├── episode-06-balint-orosz/
  ├── episode-07-chris-abad/
  ├── episode-08-figma-make/
  ├── episode-09-gavin-nelson/
  ├── episode-10-meng-to/
  └── episode-11-mig-reyes/
/episode-training-data/    - Legacy deliverables (now organized above)
```

## Target
7+/10 voice authenticity score using comprehensive training dataset