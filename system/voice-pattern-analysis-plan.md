# Voice Pattern Analysis Implementation Plan

## Phase 1: Setup & Data Extraction
- [x] Create `/scripts/` directory
- [x] Create `/agents/` directory  
- [x] Create `/extracted_data/` directory
- [x] Create `/voice-patterns/` directory
- [x] Build extraction script (`/scripts/extract_patterns.py`)
  - [x] Parse all deliverables files systematically
  - [x] Extract structured sections into JSON
  - [x] Count frequencies, identify patterns
  - [x] Output to `/extracted_data/raw_patterns.json`

## Phase 2: Create Persistent Agent Instructions
- [x] Create `/agents/voice_analyst.md`
  - [x] Analyze extracted patterns for Ridd's unique voice
  - [x] Identify formulas, templates, and structures
  - [x] Focus on distinctiveness from AI writing
  - [x] Output specific examples with frequencies
- [x] Create `/agents/editorial_analyst.md`
  - [x] Deep dive into brain dump sections
  - [x] Extract explicit preferences Ridd mentions
  - [x] Identify what he criticizes vs praises
  - [x] Find patterns in his editorial feedback
- [x] Create `/agents/pattern_synthesizer.md`
  - [x] Create actionable templates from analysis
  - [x] Build JSON reference structures
  - [x] Generate statistical summaries
  - [x] Ensure patterns appear in 3+ episodes
- [x] Create `/agents/qa_reviewer.md` (Critical Review Agent)
  - [x] Verification checklist for pattern accuracy
  - [x] Quality challenges for vague patterns
  - [x] Distinctiveness test requirements
  - [x] Critical review standards

### Detailed Agent Specifications

#### Voice Analyst (`/agents/voice_analyst.md`)
- Analyze extracted patterns for Ridd's unique voice
- Identify formulas, templates, and structures
- Focus on distinctiveness from AI writing
- Output specific examples with frequencies
- Look for recurring phrases, sentence structures, and stylistic choices
- Document patterns that appear across multiple episodes

#### Editorial Analyst (`/agents/editorial_analyst.md`)
- Deep dive into brain dump sections
- Extract explicit preferences Ridd mentions
- Identify what he criticizes vs praises
- Find patterns in his editorial feedback
- Catalog his decision-making process and quality standards
- Note his reactions to different content approaches

#### Pattern Synthesizer (`/agents/pattern_synthesizer.md`)
- Create actionable templates from analysis
- Build JSON reference structures
- Generate statistical summaries
- Ensure patterns appear in 3+ episodes
- Transform insights into practical writing guidelines
- Create reusable structures and formulas

#### QA Reviewer (`/agents/qa_reviewer.md`)
Critical Review Agent with specific standards:

**Verification Checklist:**
- Are claimed patterns actually present in 3+ episodes?
- Do examples accurately represent the source material?
- Are statistics correctly calculated?
- Is there over-generalization from limited samples?

**Quality Challenges:**
- Challenge vague patterns ("uses engaging language" → need specifics)
- Flag generic observations that could apply to any content
- Identify missing patterns other agents overlooked
- Point out contradictions between different analyses

**Distinctiveness Test:**
- Would these patterns differentiate Ridd from generic AI?
- Are patterns specific enough to be actionable?
- Do templates capture authentic voice, not just structure?

## Phase 3: Orchestration
- [x] Create `/scripts/run_voice_analysis.py`
  - [x] Run extraction script → JSON data
  - [x] Execute agents with saved prompts
  - [x] Handle QA review and iteration
  - [x] Generate final outputs

### Orchestration Script Workflow

The orchestration script (`/scripts/run_voice_analysis.py`) will execute this sequence:

1. **Run extraction script** → Generate `/extracted_data/raw_patterns.json`
2. **Save extracted data** as JSON for agent consumption
3. **Execute voice analyst**: Prompt with `/agents/voice_analyst.md` instructions using `/extracted_data/`
4. **Execute editorial analyst**: Prompt with `/agents/editorial_analyst.md` instructions using `/extracted_data/`
5. **Execute pattern synthesizer**: Prompt with `/agents/pattern_synthesizer.md` instructions
6. **Execute QA reviewer**: Prompt with `/agents/qa_reviewer.md` to critically review all outputs
7. **Handle iterations**: If QA finds issues → re-run specific agents
8. **Generate final outputs**: Validated voice pattern analysis results

### Prompt Format Examples
```python
# Voice Analyst Execution
prompt = f"""
Use the instructions in /agents/voice_analyst.md to analyze the extracted data in /extracted_data/raw_patterns.json

Focus on identifying Ridd's unique voice patterns that distinguish his writing from generic AI content.
"""

# QA Review Execution  
prompt = f"""
Use the critical review standards in /agents/qa_reviewer.md to evaluate:
- Voice analyst output: {voice_analysis_result}
- Editorial analyst output: {editorial_analysis_result}
- Pattern synthesizer output: {pattern_synthesis_result}

Apply verification checklist, quality challenges, and distinctiveness tests.
"""
```

## Phase 4: Execution Checklist
- [ ] Run extraction script
- [ ] Execute voice analyst with persistent prompt
- [ ] Execute editorial analyst with persistent prompt
- [ ] Execute pattern synthesizer with persistent prompt
- [ ] Execute QA reviewer for critical assessment
- [ ] Iterate based on QA feedback if needed
- [ ] Generate final validated outputs

## Expected Outputs
- [ ] `/voice-patterns/ridd-voice-analysis.md`
- [ ] `/voice-patterns/editorial-preferences.md`
- [ ] `/voice-patterns/pattern-reference.json`
- [ ] `/voice-patterns/extraction-summary.md`
- [ ] `/voice-patterns/qa-review-report.md`

## System Architecture Details

### Persistent Agent System Benefits:
1. **Consistency**: Same instructions every time
2. **Versioning**: Can track prompt evolution
3. **Modularity**: Easy to update individual agents
4. **Reusability**: Run on any batch with same commands
5. **Transparency**: Instructions visible and auditable

### QA Reviewer Critical Standards:
The QA reviewer will:
- Require evidence for every pattern claim
- Challenge patterns with <3 occurrences
- Identify gaps in analysis coverage
- Flag overfitting to specific episodes
- Ensure patterns are Ridd-specific, not generic
- Validate that examples match claimed patterns
- Point out any circular reasoning
- Check for confirmation bias in analysis

### Advantages of Persistent Agent System:

1. **Consistency**: Same instructions every time - eliminates variance in analysis approach
2. **Versioning**: Can track prompt evolution - allows for iterative improvement of agent instructions
3. **Modularity**: Easy to update individual agents - modify one agent without affecting others
4. **Reusability**: Run on any batch with same commands - scalable for future episode analysis
5. **Transparency**: Instructions visible and auditable - clear documentation of analysis methodology

### Directory Structure:
```
/scripts/
  extract_patterns.py          # Deterministic extraction
  run_voice_analysis.py        # Orchestration
  
/agents/
  voice_analyst.md             # Persistent prompt
  editorial_analyst.md         # Persistent prompt
  pattern_synthesizer.md       # Persistent prompt
  qa_reviewer.md              # Critical review prompt
  
/extracted_data/
  raw_patterns.json           # Script output
  
/voice-patterns/
  ridd-voice-analysis.md      # Agent 1 output
  editorial-preferences.md    # Agent 2 output
  pattern-reference.json      # Agent 3 output
  extraction-summary.md       # Final summary
  qa-review-report.md        # QA findings
```

### Execution Flow:
1. Run extraction script → JSON data
2. Execute voice analyst with saved prompt
3. Execute editorial analyst with saved prompt  
4. Execute pattern synthesizer with saved prompt
5. Execute QA reviewer for critical assessment
6. If QA finds issues → iterate specific agents
7. Generate final validated outputs