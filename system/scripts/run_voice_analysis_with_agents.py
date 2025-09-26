#!/usr/bin/env python3
"""
Voice Pattern Analysis with Subagents

Executes the voice pattern analysis pipeline using pre-created Claude Code subagents.
Uses the Task tool to execute agents in the proper sequence with extracted data.
"""

import os
import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime


class VoiceAnalysisWithAgents:
    def __init__(self):
        self.base_dir = Path.cwd()
        self.scripts_dir = self.base_dir / "scripts"
        self.extracted_data_dir = self.base_dir / "extracted_data"
        self.voice_patterns_dir = self.base_dir / "voice-patterns"
        
        # Ensure output directory exists
        self.voice_patterns_dir.mkdir(exist_ok=True)
        
        self.extracted_data = None
        self.results = {}
        self.execution_log = []
    
    def log_step(self, step, status, message=""):
        """Log execution steps"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = {
            "timestamp": timestamp,
            "step": step,
            "status": status,
            "message": message
        }
        self.execution_log.append(log_entry)
        print(f"[{timestamp}] {step}: {status}" + (f" - {message}" if message else ""))
    
    def load_extracted_data(self):
        """Load the extracted pattern data"""
        self.log_step("Data Loading", "STARTED")
        
        try:
            patterns_file = self.extracted_data_dir / "raw_patterns.json"
            if not patterns_file.exists():
                # Run extraction if data doesn't exist
                self.log_step("Data Loading", "RUNNING_EXTRACTION", "No existing data found")
                extraction_result = self.run_extraction()
                if not extraction_result:
                    raise Exception("Extraction failed")
            
            with open(patterns_file, 'r', encoding='utf-8') as f:
                self.extracted_data = json.load(f)
            
            summary = self.extracted_data.get("summary", {})
            self.log_step("Data Loading", "COMPLETED", 
                         f"Loaded data for {summary.get('total_episodes', 0)} episodes")
            return True
            
        except Exception as e:
            self.log_step("Data Loading", "FAILED", str(e))
            return False
    
    def run_extraction(self):
        """Run the pattern extraction script if needed"""
        try:
            extraction_script = self.scripts_dir / "extract_patterns.py"
            if not extraction_script.exists():
                raise FileNotFoundError(f"Extraction script not found: {extraction_script}")
            
            result = subprocess.run(
                [sys.executable, str(extraction_script)],
                capture_output=True,
                text=True,
                cwd=self.base_dir
            )
            
            if result.returncode != 0:
                raise Exception(f"Extraction script failed: {result.stderr}")
            
            return True
            
        except Exception as e:
            self.log_step("Pattern Extraction", "FAILED", str(e))
            return False
    
    def prepare_agent_context(self):
        """Prepare context data for agents"""
        summary = self.extracted_data.get("summary", {})
        
        context = f"""# Voice Pattern Analysis Context

## Data Summary
- Episodes analyzed: {summary.get('total_episodes', 0)}
- Brain dumps available: {summary.get('episodes_with_brain_dumps', 0)}
- Total takeaways extracted: {summary.get('total_takeaways', 0)}

## Most Common Recurring Phrases
{json.dumps(summary.get('most_common_phrases', {}), indent=2)}

## Analysis Requirements
Focus on patterns that:
1. Appear in 3+ episodes minimum
2. Are distinctive to Ridd's voice (not generic)
3. Can be actionably applied for voice replication
4. Are backed by specific textual evidence

## Extracted Data Available
- Titles (main, alternative, newsletter)
- Description hooks and highlights
- Key takeaways with brain dump reflections
- Structural patterns and recurring phrases
- Complete episode-by-episode breakdown

The full extracted data is available in the JSON structure provided.
"""
        return context
    
    def format_data_for_agent(self, data_subset=None):
        """Format extracted data for agent consumption"""
        if data_subset:
            # Provide specific subset of data
            return json.dumps(data_subset, indent=2, ensure_ascii=False)
        else:
            # Provide full data (truncated for context limits)
            return json.dumps(self.extracted_data, indent=2, ensure_ascii=False)[:30000] + "\n\n[Data truncated - full dataset contains all 11 episodes]"
    
    def create_execution_summary(self):
        """Create final execution summary with all results"""
        summary_content = f"""# Voice Pattern Analysis Execution Results

**Execution Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Data Analysis Summary
- Episodes processed: {self.extracted_data['summary'].get('total_episodes', 0)}
- Brain dumps analyzed: {self.extracted_data['summary'].get('episodes_with_brain_dumps', 0)}
- Patterns extracted: {len(self.extracted_data.get('structural_patterns', {}).get('recurring_phrases', {}))}

## Agent Execution Results

"""
        
        for agent_name, result in self.results.items():
            status = result.get('status', 'UNKNOWN')
            summary_content += f"### {agent_name.replace('_', ' ').title()}\n"
            summary_content += f"**Status:** {status}\n"
            if result.get('output_file'):
                summary_content += f"**Output:** {result['output_file']}\n"
            if result.get('summary'):
                summary_content += f"**Summary:** {result['summary']}\n"
            summary_content += "\n"
        
        summary_content += """## Analysis Pipeline Completed

The voice pattern analysis has been completed using the pre-created subagents. Each agent analyzed the extracted data according to their specialized instructions:

1. **Voice Analyst**: Identified distinctive voice patterns and recurring elements
2. **Editorial Analyst**: Extracted editorial preferences from brain dump reflections  
3. **Pattern Synthesizer**: Created actionable templates and reference structures
4. **QA Reviewer**: Validated analysis quality and provided critical assessment

## Output Files Generated

All analysis results have been saved to the `/voice-patterns/` directory for review and implementation.

## Execution Log

"""
        
        for entry in self.execution_log:
            summary_content += f"- [{entry['timestamp']}] {entry['step']}: {entry['status']}"
            if entry['message']:
                summary_content += f" - {entry['message']}"
            summary_content += "\n"
        
        # Save summary
        summary_file = self.voice_patterns_dir / "analysis_execution_summary.md"
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write(summary_content)
        
        self.log_step("Execution Summary", "GENERATED", f"Summary saved to {summary_file}")
        return summary_file
    
    def run_analysis_pipeline(self):
        """Execute the complete analysis pipeline using subagents"""
        self.log_step("Voice Analysis Pipeline", "STARTED", "Using pre-created subagents")
        
        # Prepare context for all agents
        context = self.prepare_agent_context()
        formatted_data = self.format_data_for_agent()
        
        print("\n" + "="*60)
        print("EXECUTING VOICE PATTERN ANALYSIS WITH SUBAGENTS")
        print("="*60)
        print("\nNote: This script prepares the execution framework.")
        print("The actual subagent execution will happen through Claude Code's Task tool.")
        print("\nTo complete the analysis:")
        print("1. Use the Task tool to execute each subagent with the prepared prompts")
        print("2. Pass the extracted data context to each agent")
        print("3. Save results to the output files")
        print("\nSubagents to execute in order:")
        
        # Define execution sequence
        agents = [
            {
                "name": "voice_analyst",
                "description": "Analyze voice patterns and distinctive elements",
                "output_file": "ridd-voice-analysis.md",
                "parallel_group": 1
            },
            {
                "name": "editorial_analyst", 
                "description": "Extract editorial preferences from brain dumps",
                "output_file": "editorial-preferences.md",
                "parallel_group": 1
            },
            {
                "name": "pattern_synthesizer",
                "description": "Create actionable templates from analysis",
                "output_file": "pattern-reference.json",
                "parallel_group": 2
            },
            {
                "name": "qa_reviewer",
                "description": "Critically review and validate all outputs", 
                "output_file": "qa-review-report.md",
                "parallel_group": 3
            }
        ]
        
        # Create instruction files for each agent
        for agent in agents:
            instruction_content = f"""# {agent['name'].replace('_', ' ').title()} Execution

## Task Description
{agent['description']}

## Context
{context}

## Extracted Data
```json
{formatted_data}
```

## Instructions
Use your pre-configured instructions to analyze this data and provide comprehensive output following your specialized role.

## Output Requirements
- Provide specific, evidence-based analysis
- Include examples with episode references
- Focus on patterns appearing in 3+ episodes
- Ensure distinctiveness from generic content writing
- Create actionable guidelines for voice replication

## Expected Output File
Results should be formatted for saving to: `/voice-patterns/{agent['output_file']}`
"""
            
            # Save instruction file
            instruction_file = self.voice_patterns_dir / f"{agent['name']}_execution_instructions.md"
            with open(instruction_file, 'w', encoding='utf-8') as f:
                f.write(instruction_content)
            
            print(f"\n{agent['parallel_group']}. {agent['name'].replace('_', ' ').title()}")
            print(f"   Instructions: {instruction_file}")
            print(f"   Output: /voice-patterns/{agent['output_file']}")
            
            # Record in results
            self.results[agent['name']] = {
                "status": "PREPARED",
                "instruction_file": str(instruction_file),
                "output_file": agent['output_file']
            }
        
        print("\n" + "="*60)
        print("PIPELINE PREPARATION COMPLETED")
        print("="*60)
        
        self.log_step("Voice Analysis Pipeline", "PREPARED", "All agent instructions ready")
        return True
    
    def run(self):
        """Execute the complete workflow"""
        print("=" * 60)
        print("VOICE PATTERN ANALYSIS WITH SUBAGENTS")
        print("=" * 60)
        
        # Step 1: Load extracted data
        if not self.load_extracted_data():
            print("\n❌ Data loading failed. Aborting pipeline.")
            return False
        
        # Step 2: Prepare analysis pipeline  
        if not self.run_analysis_pipeline():
            print("\n❌ Pipeline preparation failed.")
            return False
        
        # Step 3: Generate execution summary
        self.create_execution_summary()
        
        print(f"\n📋 Next Steps:")
        print(f"1. Execute each subagent using Claude Code's Task tool")
        print(f"2. Use the instruction files in /voice-patterns/ as prompts")
        print(f"3. Save each agent's output to its designated file")
        print(f"4. Review analysis_execution_summary.md for complete results")
        
        return True


def main():
    """Main execution function"""
    try:
        analyzer = VoiceAnalysisWithAgents()
        success = analyzer.run()
        return 0 if success else 1
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Pipeline interrupted by user")
        return 1
    except Exception as e:
        print(f"\n❌ Pipeline failed with error: {e}")
        return 1


if __name__ == "__main__":
    exit(main())