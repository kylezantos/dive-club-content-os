#!/usr/bin/env python3
"""
Voice Pattern Extraction Script

Parses all deliverables files to extract Ridd's writing patterns into structured JSON.
Analyzes titles, hooks, highlights, takeaways, and brain dumps for pattern identification.
"""

import os
import json
import re
from pathlib import Path
from collections import defaultdict, Counter
from typing import Dict, List, Any


class VoicePatternExtractor:
    def __init__(self, deliverables_dir: str = "episode-deliverables"):
        self.deliverables_dir = Path(deliverables_dir)
        self.patterns = {
            "titles": {
                "main_titles": [],
                "alternative_titles": [],
                "newsletter_titles": [],
                "newsletter_subtitles": []
            },
            "hooks": [],
            "highlights": [],
            "takeaways": [],
            "brain_dumps": [],
            "structural_patterns": {
                "bullet_point_styles": [],
                "emphasis_patterns": [],
                "quote_formats": [],
                "transition_phrases": [],
                "recurring_phrases": Counter()
            },
            "episodes": {}
        }
    
    def extract_from_file(self, filepath: Path) -> Dict[str, Any]:
        """Extract patterns from a single deliverable file"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        episode_name = filepath.stem
        episode_data = {
            "filename": filepath.name,
            "sections": {},
            "patterns": {}
        }
        
        # Extract main sections
        sections = self._parse_sections(content)
        episode_data["sections"] = sections
        
        # Analyze patterns within this episode
        episode_data["patterns"] = self._analyze_episode_patterns(sections)
        
        return episode_name, episode_data
    
    def _parse_sections(self, content: str) -> Dict[str, Any]:
        """Parse markdown content into structured sections"""
        sections = {}
        
        # Extract title sections
        title_match = re.search(r'## Title\n\nMain Title:\n\n- (.+?)(?=\n\n|\n-|\nAlternative)', content, re.DOTALL)
        if title_match:
            sections["main_title"] = title_match.group(1).strip()
        
        alt_titles_match = re.search(r'Alternative Titles:\n\n((?:- .+?\n)+)', content, re.DOTALL)
        if alt_titles_match:
            sections["alternative_titles"] = [
                line.strip()[2:] for line in alt_titles_match.group(1).strip().split('\n') 
                if line.strip().startswith('-')
            ]
        
        # Extract description hook
        hook_match = re.search(r'### Description Hook\n\n(.+?)(?:\n\n---|\n\n###)', content, re.DOTALL)
        if hook_match:
            sections["description_hook"] = hook_match.group(1).strip()
        
        # Extract highlights
        highlights_match = re.search(r'### Description Highlights\n\n((?:- .+?\n)+)', content, re.DOTALL)
        if highlights_match:
            sections["highlights"] = [
                line.strip()[2:] for line in highlights_match.group(1).strip().split('\n')
                if line.strip().startswith('-')
            ]
        
        # Extract newsletter info
        newsletter_title_match = re.search(r'### Newsletter Info:.*?Title:\n\n- (.+?)\n', content, re.DOTALL)
        if newsletter_title_match:
            sections["newsletter_title"] = newsletter_title_match.group(1).strip()
        
        newsletter_subtitle_match = re.search(r'Subtitle:\n\n- (.+?)\n', content, re.DOTALL)
        if newsletter_subtitle_match:
            sections["newsletter_subtitle"] = newsletter_subtitle_match.group(1).strip()
        
        # Extract takeaways (numbered highlights section)
        takeaways_match = re.search(r'(?:### 3 (?:key ideas|highlights)|## 3 highlights).*?\n\n(.*?)(?:\n\n### Ridd\'s Brain dump|\Z)', content, re.DOTALL)
        if takeaways_match:
            takeaway_content = takeaways_match.group(1)
            # Parse individual takeaways
            takeaway_sections = re.findall(r'\*\*(\d[^*]+)\*\*\n(.*?)(?=\n\*\*\d|\Z)', takeaway_content, re.DOTALL)
            sections["takeaways"] = [
                {
                    "title": title.strip(),
                    "content": content.strip()
                }
                for title, content in takeaway_sections
            ]
        
        # Extract brain dump - look for "Brain dump" and get content after it
        brain_dump_match = re.search(r'Brain dump\n\n(.+?)(?=\n\n###|\Z)', content, re.DOTALL | re.IGNORECASE)
        if brain_dump_match:
            sections["brain_dump"] = brain_dump_match.group(1).strip()
        
        # Also check for brain dumps embedded in takeaway content
        for takeaway in sections.get("takeaways", []):
            if "Brain dump" in takeaway.get("content", ""):
                brain_dump_content = re.search(r'Brain dump\n\n(.+)', takeaway["content"], re.DOTALL | re.IGNORECASE)
                if brain_dump_content:
                    if "brain_dump" not in sections:  # Only if we haven't found one already
                        sections["brain_dump"] = brain_dump_content.group(1).strip()
                    # Clean the takeaway content to remove the brain dump
                    takeaway["content"] = re.sub(r'\n\n.*Brain dump\n\n.+', '', takeaway["content"], flags=re.DOTALL | re.IGNORECASE).strip()
        
        return sections
    
    def _analyze_episode_patterns(self, sections: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze patterns within a single episode"""
        patterns = {
            "title_patterns": {},
            "hook_patterns": {},
            "structural_elements": {},
            "voice_elements": {}
        }
        
        # Analyze titles
        if "main_title" in sections:
            patterns["title_patterns"]["main_title_structure"] = self._analyze_title_structure(sections["main_title"])
        
        # Analyze hook patterns
        if "description_hook" in sections:
            patterns["hook_patterns"] = self._analyze_hook_patterns(sections["description_hook"])
        
        # Analyze takeaway structures
        if "takeaways" in sections:
            patterns["takeaway_patterns"] = self._analyze_takeaway_patterns(sections["takeaways"])
        
        # Extract recurring phrases
        all_text = self._get_all_text(sections)
        patterns["recurring_phrases"] = self._extract_recurring_phrases(all_text)
        
        # Analyze emphasis and formatting
        patterns["formatting_patterns"] = self._analyze_formatting_patterns(all_text)
        
        return patterns
    
    def _analyze_title_structure(self, title: str) -> Dict[str, Any]:
        """Analyze title structure patterns"""
        return {
            "length": len(title.split()),
            "starts_with_article": title.lower().startswith(('a ', 'an ', 'the ')),
            "contains_numbers": bool(re.search(r'\d', title)),
            "contains_how_to": 'how to' in title.lower(),
            "contains_new": 'new' in title.lower(),
            "action_words": self._extract_action_words(title)
        }
    
    def _analyze_hook_patterns(self, hook: str) -> Dict[str, Any]:
        """Analyze description hook patterns"""
        sentences = re.split(r'[.!?]+', hook)
        return {
            "sentence_count": len([s for s in sentences if s.strip()]),
            "contains_links": bool(re.search(r'\[.*?\]\(.*?\)', hook)),
            "contains_personal_reference": any(word in hook.lower() for word in ['i ', 'my ', 'we ']),
            "opening_structure": sentences[0].strip()[:50] if sentences else "",
            "contains_guest_intro": bool(re.search(r'\[.*?\]\(https?://.*?\)', hook))
        }
    
    def _analyze_takeaway_patterns(self, takeaways: List[Dict]) -> Dict[str, Any]:
        """Analyze takeaway structure patterns"""
        patterns = {
            "count": len(takeaways),
            "title_patterns": [],
            "emoji_usage": [],
            "quote_patterns": []
        }
        
        for takeaway in takeaways:
            title = takeaway["title"]
            content = takeaway["content"]
            
            patterns["title_patterns"].append({
                "has_emoji": bool(re.search(r'[^\w\s]', title)),
                "starts_with_number": title[0].isdigit() if title else False,
                "structure": re.sub(r'[^\w\s]', '', title)[:30]
            })
            
            # Find quotes
            quotes = re.findall(r'> "(.+?)"\n> \n- (.+)', content, re.DOTALL)
            if quotes:
                patterns["quote_patterns"].extend([
                    {"quote": quote.strip(), "attribution": attr.strip()}
                    for quote, attr in quotes
                ])
        
        return patterns
    
    def _get_all_text(self, sections: Dict[str, Any]) -> str:
        """Combine all text from sections for pattern analysis"""
        all_text = []
        
        for key, value in sections.items():
            if isinstance(value, str):
                all_text.append(value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, str):
                        all_text.append(item)
                    elif isinstance(item, dict) and "content" in item:
                        all_text.append(item["content"])
        
        return " ".join(all_text)
    
    def _extract_recurring_phrases(self, text: str) -> Dict[str, int]:
        """Find recurring phrases across the text"""
        # Common Ridd phrases and patterns
        ridd_phrases = [
            r'a \*lot\* more',
            r'[Aa]nd I\'m (?:feeling )?(?:incredibly )?(?:grateful|excited)',
            r'[Tt]he fact is',
            r'[Hh]ere\'s the thing',
            r'[Bb]ut it turns out',
            r'[Aa]nd that\'s',
            r'[Tt]he times .+ have (?:failed|succeeded)',
            r'[Ii]n the interview',
            r'[Ii] asked (?:him|her)',
            r'[Ww]hich means',
            r'[Aa]nd so'
        ]
        
        phrase_counts = {}
        for phrase_pattern in ridd_phrases:
            matches = re.findall(phrase_pattern, text, re.IGNORECASE)
            if matches:
                phrase_counts[phrase_pattern] = len(matches)
        
        return phrase_counts
    
    def _analyze_formatting_patterns(self, text: str) -> Dict[str, Any]:
        """Analyze formatting and emphasis patterns"""
        return {
            "bold_usage": len(re.findall(r'\*\*(.*?)\*\*', text)),
            "italic_usage": len(re.findall(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', text)),
            "parenthetical_usage": len(re.findall(r'\([^)]+\)', text)),
            "em_dash_usage": len(re.findall(r'—', text)),
            "ellipsis_usage": len(re.findall(r'\.{3}', text)),
            "emoji_usage": len(re.findall(r'[^\w\s.,!?()-]', text))
        }
    
    def _extract_action_words(self, text: str) -> List[str]:
        """Extract action words from text"""
        action_words = [
            'build', 'create', 'design', 'ship', 'become', 'succeed', 'grow',
            'learn', 'understand', 'discover', 'unlock', 'master', 'achieve'
        ]
        found_words = []
        for word in action_words:
            if word in text.lower():
                found_words.append(word)
        return found_words
    
    def extract_all_patterns(self) -> Dict[str, Any]:
        """Extract patterns from all deliverable files"""
        if not self.deliverables_dir.exists():
            raise FileNotFoundError(f"Deliverables directory not found: {self.deliverables_dir}")
        
        # Process each deliverable file
        for filepath in self.deliverables_dir.glob("*-deliverables.md"):
            episode_name, episode_data = self.extract_from_file(filepath)
            self.patterns["episodes"][episode_name] = episode_data
            
            # Aggregate patterns
            self._aggregate_episode_patterns(episode_data)
        
        # Generate summary statistics
        self.patterns["summary"] = self._generate_summary_stats()
        
        return self.patterns
    
    def _aggregate_episode_patterns(self, episode_data: Dict[str, Any]):
        """Aggregate patterns from individual episode into main patterns dict"""
        sections = episode_data["sections"]
        
        # Collect titles
        if "main_title" in sections:
            self.patterns["titles"]["main_titles"].append(sections["main_title"])
        if "alternative_titles" in sections:
            self.patterns["titles"]["alternative_titles"].extend(sections["alternative_titles"])
        if "newsletter_title" in sections:
            self.patterns["titles"]["newsletter_titles"].append(sections["newsletter_title"])
        if "newsletter_subtitle" in sections:
            self.patterns["titles"]["newsletter_subtitles"].append(sections["newsletter_subtitle"])
        
        # Collect other sections
        if "description_hook" in sections:
            self.patterns["hooks"].append(sections["description_hook"])
        if "highlights" in sections:
            self.patterns["highlights"].extend(sections["highlights"])
        if "takeaways" in sections:
            self.patterns["takeaways"].extend(sections["takeaways"])
        if "brain_dump" in sections:
            self.patterns["brain_dumps"].append(sections["brain_dump"])
        
        # Aggregate recurring phrases
        episode_phrases = episode_data["patterns"].get("recurring_phrases", {})
        for phrase, count in episode_phrases.items():
            self.patterns["structural_patterns"]["recurring_phrases"][phrase] += count
    
    def _generate_summary_stats(self) -> Dict[str, Any]:
        """Generate summary statistics across all episodes"""
        return {
            "total_episodes": len(self.patterns["episodes"]),
            "total_titles": len(self.patterns["titles"]["main_titles"]),
            "total_hooks": len(self.patterns["hooks"]),
            "total_takeaways": len(self.patterns["takeaways"]),
            "most_common_phrases": dict(self.patterns["structural_patterns"]["recurring_phrases"].most_common(10)),
            "episodes_with_brain_dumps": len([ep for ep in self.patterns["episodes"].values() 
                                            if "brain_dump" in ep["sections"]])
        }
    
    def save_patterns(self, output_path: str = "extracted_data/raw_patterns.json"):
        """Save extracted patterns to JSON file"""
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.patterns, f, indent=2, ensure_ascii=False)
        
        print(f"Patterns extracted and saved to {output_file}")
        print(f"Processed {self.patterns['summary']['total_episodes']} episodes")


def main():
    """Main execution function"""
    extractor = VoicePatternExtractor()
    
    try:
        patterns = extractor.extract_all_patterns()
        extractor.save_patterns()
        
        # Print summary
        summary = patterns["summary"]
        print("\n=== EXTRACTION SUMMARY ===")
        print(f"Episodes processed: {summary['total_episodes']}")
        print(f"Brain dumps found: {summary['episodes_with_brain_dumps']}")
        print(f"Total takeaways extracted: {summary['total_takeaways']}")
        
        print("\nMost common recurring phrases:")
        for phrase, count in summary["most_common_phrases"].items():
            print(f"  {phrase}: {count}")
        
    except Exception as e:
        print(f"Error during extraction: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())