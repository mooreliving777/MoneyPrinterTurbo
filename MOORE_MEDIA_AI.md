# Moore Media AI — AI Production Studio

Moore Media AI is a branded production layer built on top of MoneyPrinterTurbo. The goal of this branch is to preserve the proven MoneyPrinterTurbo generation engine while adding a Moore-branded interface, repeatable content presets, and a path toward a private multi-format media production system.

> MoneyPrinterTurbo remains licensed under the MIT License. Keep the original LICENSE file and copyright notice with copies or substantial portions of the software.

## What is included in v1

- Moore Media AI Windows one-click launcher: `moore_media_ai.bat`
- Presentation-safe branding wrapper: `moore_media_ai_launcher.py`
- Navy-and-gold Streamlit theme
- Branded page title, icon, project heading, repository links, and AI Production Studio tagline
- Importable presets for:
  - YouTube Documentary
  - Social Short
  - Course Promo
  - Business Commercial
  - Music Promo
  - Podcast Clip
- The original `webui/Main.py` generation engine remains untouched

## Windows setup

Open PowerShell in the project folder and run:

```powershell
uv python install 3.11
uv sync --frozen
```

Then launch Moore Media AI by double-clicking:

```text
moore_media_ai.bat
```

Or from PowerShell:

```powershell
.\moore_media_ai.bat
```

The default local address is:

```text
http://127.0.0.1:8501
```

## Import a Moore production preset

The preset files are stored in:

```text
presets/moore_media_ai/
```

In the MoneyPrinterTurbo/Moore Media AI WebUI, open the settings preset import control, select the JSON preset you want, and import it. Review the loaded values before generating because media source, voice, music, and provider choices may still need to be adjusted for the specific project.

## Recommended workflow

1. Choose a production preset.
2. Set the topic or paste an approved script.
3. Choose the LLM provider.
4. Select stock, local, or AI-generated footage.
5. Choose voice mode and voice.
6. Review subtitles, music, clip duration, and aspect ratio.
7. Generate one test version.
8. Review facts, visuals, pronunciation, captions, music level, and brand consistency.
9. Generate the final version.
10. Publish only after human review.

## Preset intentions

### YouTube Documentary
16:9, slower pacing, more paragraphs, lower music level, documentary-oriented writing prompt.

### Social Short
9:16, fast clip changes, large subtitles, faster hook-and-payoff structure for Shorts/Reels/TikTok.

### Course Promo
9:16 promotional format focused on problem, transformation, learning outcomes, and an enrollment call to action without guaranteed-results language.

### Business Commercial
9:16 direct-response commercial format with restrained claims and a single clear CTA.

### Music Promo
9:16 fast visual pacing for independent release promotion without fabricated chart claims, endorsements, or audience numbers.

### Podcast Clip
9:16, large captions, quiet background music, and a prompt designed to preserve the speaker's meaning while tightening the clip.

## Brand direction

Primary brand colors used in v1:

- Midnight Navy: `#0A0A23`
- Gold: `#FFD700`
- Panel Navy: `#15152F`
- White: `#FFFFFF`

The launcher uses runtime substitutions rather than permanently renaming MoneyPrinterTurbo internals. This makes upstream updates easier to pull into the fork while reducing the chance of breaking API names, configuration schemas, or task storage.

## Planned v2

The next build can add a native Moore Media AI dashboard with clickable production modes such as:

- YouTube Documentary
- Facebook Reel
- TikTok / YouTube Short
- Course Promo
- Business Commercial
- Music Promo
- Podcast Clip
- Long-form episode

It can also add brand asset libraries, saved brand profiles, recurring show templates, custom intros/outros, publishing presets, and automatic repurposing from one master production into multiple platform cuts.

## Development branch

This customization is being developed on:

```text
moore-media-ai-v1
```

Keep `main` unchanged until the v1 branch has been run successfully on the target Windows computer.
