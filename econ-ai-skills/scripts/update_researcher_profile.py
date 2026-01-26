#!/usr/bin/env python3
"""
Update Researcher Profile

This script provides a mechanism to update researcher profiles from web sources.
It can be run manually or scheduled to keep profiles current.

Usage:
    python update_researcher_profile.py --name "Eugen Dimant" --website "https://eugendimant.github.io/"
    python update_researcher_profile.py --profile profiles/eugen-dimant.yaml --refresh
"""

import argparse
import yaml
import os
from datetime import datetime
from pathlib import Path


def load_profile(profile_path: str) -> dict:
    """Load an existing profile from YAML."""
    with open(profile_path, 'r') as f:
        return yaml.safe_load(f)


def save_profile(profile: dict, profile_path: str) -> None:
    """Save profile to YAML with proper formatting."""
    # Update timestamp
    profile_content = yaml.dump(profile, default_flow_style=False, allow_unicode=True, sort_keys=False)

    # Add header comment with update timestamp
    header = f"""# Researcher Profile: {profile.get('name', 'Unknown')}
# Last Updated: {datetime.now().strftime('%Y-%m-%d')}
# Source: {profile.get('website', 'Manual entry')}

"""
    with open(profile_path, 'w') as f:
        f.write(header)
        f.write(profile_content)


def generate_profile_filename(name: str) -> str:
    """Generate a filename from researcher name."""
    return name.lower().replace(' ', '-').replace('.', '') + '.yaml'


def create_empty_profile(name: str, website: str = None) -> dict:
    """Create an empty profile template."""
    return {
        'name': name,
        'website': website,
        'positions': [],
        'fields': {
            'primary': [],
            'secondary': [],
            'applied': []
        },
        'research_themes': {},
        'methodology': {
            'primary': [],
            'econometric': [],
            'other': []
        },
        'collaborators': [],
        'publications': {
            'top_journal_publications': [],
            'other_publications': [],
            'recent_working_papers': []
        },
        'data_expertise': {},
        'comparative_advantage': [],
        'potential_directions': []
    }


def add_publication(profile: dict, publication: dict, category: str = 'other_publications') -> dict:
    """Add a publication to the profile."""
    if category not in profile['publications']:
        profile['publications'][category] = []

    # Check for duplicates by title
    existing_titles = [p.get('title', '').lower() for p in profile['publications'][category]]
    if publication.get('title', '').lower() not in existing_titles:
        profile['publications'][category].append(publication)

    return profile


def add_collaborator(profile: dict, collaborator: dict) -> dict:
    """Add a collaborator to the profile."""
    existing_names = [c.get('name', '').lower() for c in profile.get('collaborators', [])]
    if collaborator.get('name', '').lower() not in existing_names:
        profile['collaborators'].append(collaborator)
    return profile


def main():
    parser = argparse.ArgumentParser(description='Update researcher profile')
    parser.add_argument('--name', type=str, help='Researcher name')
    parser.add_argument('--website', type=str, help='Researcher website URL')
    parser.add_argument('--profile', type=str, help='Path to existing profile')
    parser.add_argument('--refresh', action='store_true', help='Refresh from web sources')
    parser.add_argument('--output-dir', type=str, default='profiles', help='Output directory')

    args = parser.parse_args()

    profiles_dir = Path(__file__).parent.parent / args.output_dir
    profiles_dir.mkdir(exist_ok=True)

    if args.profile:
        # Load and update existing profile
        profile = load_profile(args.profile)
        profile_path = args.profile
    elif args.name:
        # Create or load profile by name
        filename = generate_profile_filename(args.name)
        profile_path = profiles_dir / filename

        if profile_path.exists():
            profile = load_profile(str(profile_path))
        else:
            profile = create_empty_profile(args.name, args.website)
    else:
        parser.error('Either --name or --profile must be specified')
        return

    if args.refresh:
        print(f"Note: Automatic web refresh requires AI assistance.")
        print(f"To update profile from web sources, use an AI tool with web access:")
        print(f"  'Update my researcher profile from {profile.get('website', 'my website')}'")

    # Save the profile
    save_profile(profile, str(profile_path))
    print(f"Profile saved to: {profile_path}")


if __name__ == '__main__':
    main()
