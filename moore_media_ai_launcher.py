"""Launch MoneyPrinterTurbo with Moore Media AI branding.

This wrapper intentionally leaves the upstream WebUI engine untouched. It creates a
small runtime copy of webui/Main.py, applies presentation-only substitutions, and
launches Streamlit against that copy. When the app exits, the runtime file is removed.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "webui" / "Main.py"
RUNTIME = ROOT / "webui" / "_moore_media_ai_runtime.py"


def build_runtime() -> Path:
    if not SOURCE.exists():
        raise FileNotFoundError(f"Could not find MoneyPrinterTurbo WebUI: {SOURCE}")

    text = SOURCE.read_text(encoding="utf-8")

    replacements = (
        ('page_title="MoneyPrinterTurbo"', 'page_title="Moore Media AI"'),
        ('page_icon="🤖"', 'page_icon="🎬"'),
        (
            '"Report a bug": "https://github.com/harry0703/MoneyPrinterTurbo/issues"',
            '"Report a bug": "https://github.com/mooreliving777/MoneyPrinterTurbo/issues"',
        ),
        (
            '<span class="mpt-brand__name">MoneyPrinterTurbo</span>',
            '<span class="mpt-brand__name">Moore Media AI</span>',
        ),
        (
            'href="https://github.com/harry0703/MoneyPrinterTurbo"',
            'href="https://github.com/mooreliving777/MoneyPrinterTurbo"',
        ),
        (
            'aria-label="Open MoneyPrinterTurbo on GitHub"',
            'aria-label="Open Moore Media AI on GitHub"',
        ),
    )

    for old, new in replacements:
        text = text.replace(old, new)

    # Add a branded subtitle immediately after the main project heading while
    # preserving the original generation controls and backend behavior.
    brand_marker = '<span class="mpt-brand__name">Moore Media AI</span>'
    marker_index = text.find(brand_marker)
    if marker_index != -1:
        call_end = text.find("        unsafe_allow_html=True,\n    )", marker_index)
        if call_end != -1:
            call_end += len("        unsafe_allow_html=True,\n    )")
            tagline = '''\n    st.markdown(\n        """\n        <div style="margin-top:-0.35rem;margin-bottom:1rem;opacity:.88;">\n            <strong>AI Production Studio</strong> · Create once. Publish everywhere.\n        </div>\n        """,\n        unsafe_allow_html=True,\n    )'''
            text = text[:call_end] + tagline + text[call_end:]

    # Presentation-only brand layer. The core MoneyPrinterTurbo CSS is still loaded
    # first, so all existing responsive behavior remains intact.
    style_anchor = "st.markdown(streamlit_style, unsafe_allow_html=True)"
    brand_css = r'''
st.markdown(
    """
    <style>
    :root {
        --moore-navy: #0A0A23;
        --moore-gold: #FFD700;
        --moore-panel: #15152F;
    }
    .mpt-brand__name {
        letter-spacing: -0.02em !important;
        background: linear-gradient(90deg, #FFD700, #FFF2A8, #FFD700);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent !important;
    }
    div.stButton > button[kind="primary"],
    div.stDownloadButton > button[kind="primary"] {
        border-color: var(--moore-gold) !important;
        box-shadow: 0 0 0 1px rgba(255,215,0,.12);
    }
    div.stButton > button[kind="primary"]:hover,
    div.stDownloadButton > button[kind="primary"]:hover {
        box-shadow: 0 0 20px rgba(255,215,0,.18);
    }
    </style>
    """,
    unsafe_allow_html=True,
)
'''
    if style_anchor in text:
        text = text.replace(style_anchor, style_anchor + "\n" + brand_css, 1)

    RUNTIME.write_text(text, encoding="utf-8")
    return RUNTIME


def main() -> int:
    runtime = build_runtime()
    host = os.environ.get("MPT_WEBUI_HOST", "127.0.0.1")
    port = os.environ.get("MPT_WEBUI_PORT", "8501")

    command = [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        str(runtime),
        f"--server.address={host}",
        f"--server.port={port}",
        f"--browser.serverAddress={host}",
        "--browser.gatherUsageStats=False",
        "--client.toolbarMode=minimal",
        "--logger.hideWelcomeMessage=True",
        "--server.showEmailPrompt=False",
        "--server.enableCORS=True",
    ]

    print("=" * 68)
    print("MOORE MEDIA AI — AI Production Studio")
    print(f"Open: http://{host}:{port}")
    print("Engine: MoneyPrinterTurbo")
    print("=" * 68)

    try:
        return subprocess.call(command, cwd=ROOT)
    finally:
        try:
            runtime.unlink(missing_ok=True)
        except OSError:
            pass


if __name__ == "__main__":
    raise SystemExit(main())
