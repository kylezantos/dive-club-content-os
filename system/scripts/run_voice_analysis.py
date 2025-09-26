#!/usr/bin/env python3
"""
Voice Pattern Analysis Orchestration Script

Executes the complete voice pattern analysis pipeline using persistent agents.
Runs extraction, analysis, synthesis, and QA review in sequence.
"""

import os
import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime


class VoiceAnalysisOrchestrator:
    def __init__(self):
        self.base_dir = Path.cwd()
        self.scripts_dir = self.base_dir / "scripts"
        self.agents_dir = self.base_dir / "agents"
        self.extracted_data_dir = self.base_dir / "extracted_data"
        self.voice_patterns_dir = self.base_dir / "voice-patterns"
        
        # Ensure output directory exists
        self.voice_patterns_dir.mkdir(exist_ok=True)
        
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
    
    def run_extraction(self):
        """Step 1: Run the pattern extraction script"""
        self.log_step("Pattern Extraction", "STARTED")
        
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
            
            # Verify output file exists
            patterns_file = self.extracted_data_dir / "raw_patterns.json"
            if not patterns_file.exists():
                raise FileNotFoundError("Extraction output file not created")
            
            # Load extracted data for use by agents
            with open(patterns_file, 'r', encoding='utf-8') as f:
                self.extracted_data = json.load(f)
            
            self.log_step("Pattern Extraction", "COMPLETED", f"Processed {self.extracted_data['summary']['total_episodes']} episodes")
            return True
            
        except Exception as e:
            self.log_step("Pattern Extraction", "FAILED", str(e))
            return False
    
    def execute_agent(self, agent_name, agent_description):
        """Execute a single agent with its persistent prompt"""
        self.log_step(f"Agent: {agent_name}", "STARTED")
        
        try:
            # Load agent instructions
            agent_file = self.agents_dir / f"{agent_name}.md"
            if not agent_file.exists():
                raise FileNotFoundError(f"Agent file not found: {agent_file}")
            
            with open(agent_file, 'r', encoding='utf-8') as f:
                agent_instructions = f.read()
            
            # Prepare the prompt
            prompt = self._build_agent_prompt(agent_name, agent_instructions, agent_description)
            
            # For this implementation, we'll save the prompt and instructions for manual execution
            # In a production environment, this would interface with an AI API
            prompt_file = self.voice_patterns_dir / f"{agent_name}_prompt.md"
            with open(prompt_file, 'w', encoding='utf-8') as f:
                f.write(prompt)
            
            self.log_step(f"Agent: {agent_name}", "PREPARED", f"Prompt saved to {prompt_file}")
            
            # For now, create placeholder output files
            output_file = self.voice_patterns_dir / f"{agent_name}_output.md"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"# {agent_name.title().replace('_', ' ')} Output\n\n")
                f.write(f"*This file will contain the output from the {agent_name} analysis.*\n\n")
                f.write(f"**Instructions:** Use the prompt in `{agent_name}_prompt.md` with the extracted data to generate the analysis.\n\n")
                f.write(f"**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            self.results[agent_name] = {
                "status": "prepared",
                "prompt_file": str(prompt_file),
                "output_file": str(output_file)
            }
            
            return True
            
        except Exception as e:
            self.log_step(f"Agent: {agent_name}", "FAILED", str(e))
            return False
    
    def _build_agent_prompt(self, agent_name, instructions, description):
        """Build the complete prompt for an agent"""
        
        # Include summary stats for context
        summary = self.extracted_data.get("summary", {})
        
        prompt = f"""# {agent_name.title().replace('_', ' ')} Analysis Task

## Context
You are analyzing voice patterns from Ridd's podcast deliverables to understand his unique writing style.

## Data Summary
- Episodes analyzed: {summary.get('total_episodes', 0)}
- Brain dumps available: {summary.get('episodes_with_brain_dumps', 0)}
- Total takeaways extracted: {summary.get('total_takeaways', 0)}
- Most common recurring phrases: {summary.get('most_common_phrases', {})}

## Task Description
{description}

## Agent Instructions
{instructions}

## Extracted Data
The following JSON contains all extracted patterns from the 11 episodes:

```json
{json.dumps(self.extracted_data, indent=2)[:50000]}...
[Data truncated for prompt length - full data available in extracted_data/raw_patterns.json]
```

## Expected Output
Please provide a comprehensive analysis following the instructions above. Focus on patterns that:
1. Appear in 3+ episodes
2. Are distinctive to Ridd's voice
3. Can be actionably applied for voice replication
4. Are backed by specific evidence

Your analysis should be thorough, specific, and actionable for voice pattern matching.
"""
        return prompt
    
    def run_analysis_pipeline(self):
        """Execute the complete analysis pipeline"""
        self.log_step("Voice Analysis Pipeline", "STARTED")
        
        # Define the agents in execution order
        agents = [
            ("voice_analyst", "Analyze extracted patterns for Ridd's unique voice characteristics"),
            ("editorial_analyst", "Extract editorial preferences from brain dump sections"),
            ("pattern_synthesizer", "Create actionable templates from analysis results"),
            ("qa_reviewer", "Critically review and validate all analysis outputs")
        ]
        
        success_count = 0
        
        # Execute each agent
        for agent_name, description in agents:
            if self.execute_agent(agent_name, description):
                success_count += 1
            else:
                self.log_step("Voice Analysis Pipeline", "FAILED", f"Agent {agent_name} failed")
                return False
        
        self.log_step("Voice Analysis Pipeline", "COMPLETED", f"Prepared {success_count}/{len(agents)} agents")
        return True
    
    def generate_execution_summary(self):
        """Generate a summary of the analysis execution"""
        summary_file = self.voice_patterns_dir / "execution_summary.md"
        
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write("# Voice Pattern Analysis Execution Summary\n\n")
            f.write(f"**Execution Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("## Extraction Results\n")
            if hasattr(self, 'extracted_data'):
                summary = self.extracted_data.get("summary", {})
                f.write(f"- Episodes processed: {summary.get('total_episodes', 0)}\n")
                f.write(f"- Brain dumps found: {summary.get('episodes_with_brain_dumps', 0)}\n")
                f.write(f"- Total takeaways: {summary.get('total_takeaways', 0)}\n")
                
                if summary.get('most_common_phrases'):
                    f.write("\n**Most Common Recurring Phrases:**\n")
                    for phrase, count in summary['most_common_phrases'].items():
                        f.write(f"- `{phrase}`: {count} occurrences\n")
            
            f.write("\n## Agent Execution Status\n")
            for agent_name, result in self.results.items():
                status = result['status'].upper()
                f.write(f"- **{agent_name.title().replace('_', ' ')}**: {status}\n")
                f.write(f"  - Prompt: `{result['prompt_file']}`\n")
                f.write(f"  - Output: `{result['output_file']}`\n")
            
            f.write("\n## Next Steps\n")
            f.write("1. Review each agent's prompt file\n")
            f.write("2. Execute the prompts using your preferred AI system\n")
            f.write("3. Save results to the corresponding output files\n")
            f.write("4. Run QA review last to validate all outputs\n\n")
            
            f.write("## Execution Log\n")
            for entry in self.execution_log:
                f.write(f"- [{entry['timestamp']}] {entry['step']}: {entry['status']}")
                if entry['message']:
                    f.write(f" - {entry['message']}")
                f.write("\n")
        
        self.log_step("Execution Summary", "GENERATED", f"Summary saved to {summary_file}")
    
    def run(self):
        """Execute the complete voice analysis workflow"""
        print("=" * 60)
        print("VOICE PATTERN ANALYSIS ORCHESTRATION")
        print("=" * 60)
        
        # Step 1: Run extraction
        if not self.run_extraction():
            print("\n❌ Extraction failed. Aborting pipeline.")
            return False
        
        # Step 2: Execute analysis pipeline
        if not self.run_analysis_pipeline():
            print("\n❌ Analysis pipeline failed.")
            return False
        
        # Step 3: Generate summary
        self.generate_execution_summary()
        
        print("\n" + "=" * 60)
        print("PIPELINE COMPLETED SUCCESSFULLY")
        print("=" * 60)
        print("\nNext steps:")
        print("1. Review prompt files in voice-patterns/ directory")
        print("2. Execute each agent prompt with your AI system") 
        print("3. Save results to corresponding output files")
        print("4. Check execution_summary.md for detailed status")
        
        return True


def main():
    """Main execution function"""
    try:
        orchestrator = VoiceAnalysisOrchestrator()
        success = orchestrator.run()
        return 0 if success else 1
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Pipeline interrupted by user")
        return 1
    except Exception as e:
        print(f"\n❌ Pipeline failed with error: {e}")
        return 1


if __name__ == "__main__":
    exit(main())