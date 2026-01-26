# Researcher Profiles

This directory contains persistent researcher profiles that provide context for AI-assisted research tools across projects.

## Purpose

Researcher profiles enable:
- **Personalized research question generation** - Suggestions align with your expertise and comparative advantage
- **Relevant literature recommendations** - Focus on papers in your fields
- **Consistency across sessions** - AI tools remember your research context
- **Collaboration matching** - Identify complementary expertise

## Profile Structure

Each profile is a YAML file containing:

```yaml
name: Researcher Name
positions: [...]           # Current institutional affiliations
fields: [...]              # Primary and secondary research fields
research_themes: [...]     # Core research questions and themes
methodology: [...]         # Methodological expertise
collaborators: [...]       # Key co-authors and their topics
publications: [...]        # Selected publications by theme
data_expertise: [...]      # Data sources and platforms used
comparative_advantage: [...] # What makes your research distinctive
potential_directions: [...] # Inferred future research interests
```

## Updating Your Profile

### Manual Update
Edit your YAML file directly when you have:
- New publications
- Changed positions
- New collaborators
- Shifted research focus

### Automated Update
Use the update script to refresh from web sources:

```bash
python scripts/update_researcher_profile.py --name "Your Name" --website "https://yourwebsite.com"
```

### Update Triggers
Consider updating when:
- A new paper is published or accepted
- You start a new research project
- Your methodological toolkit expands
- You join a new institution

## Using Profiles with Skills

When invoking research-ideation or other skills, the AI will automatically reference your profile if available:

```
> Generate research questions based on my profile

The AI will read econ-ai-skills/profiles/your-name.yaml and tailor suggestions accordingly.
```

## Privacy Note

Profiles contain only publicly available information from academic websites, CVs, and published research. Do not include unpublished ideas, confidential data access, or sensitive institutional information.
