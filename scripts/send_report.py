"""
send_report.py — Generate PDF and email the weekly intelligence report via Resend

Usage:
    python scripts/send_report.py report_output/week_of_2026-03-23.html
    python scripts/send_report.py report_output/week_of_2026-03-23.html --to other@email.com
    python scripts/send_report.py report_output/week_of_2026-03-23.html --dry-run

Reads the HTML report, generates a PDF via Playwright, and sends both
as an email (HTML body + PDF attachment) via Resend.
"""

import sys
import os
import base64
import subprocess
import tempfile
from pathlib import Path
from datetime import datetime


def generate_pdf(html_path: str, pdf_path: str) -> bool:
    """Generate PDF from HTML using Python Playwright."""
    from playwright.sync_api import sync_playwright

    abs_html = str(Path(html_path).resolve())
    file_url = f"file://{abs_html}"

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(file_url, wait_until="networkidle")
            page.wait_for_timeout(1000)
            page.pdf(
                path=pdf_path,
                format="A4",
                margin={"top": "24px", "bottom": "24px", "left": "24px", "right": "24px"},
                print_background=True,
            )
            browser.close()
        return Path(pdf_path).exists()
    except Exception as e:
        print(f"  Playwright error: {e}")
        return False


def send_email(
    html_content: str,
    pdf_path: str,
    to_email: str,
    subject: str,
    from_email: str = "onboarding@resend.dev",
) -> dict:
    """Send the report via Resend with HTML body and PDF attachment."""
    import resend

    api_key = os.environ.get("RESEND_API_KEY")
    if not api_key:
        # Fallback: read from known location
        env_path = Path.home() / "Desktop" / "Rewire Master" / ".env.local"
        if env_path.exists():
            for line in env_path.read_text().splitlines():
                if line.startswith("RESEND_API_KEY"):
                    api_key = line.split("=", 1)[1].strip().strip('"')
                    break

    if not api_key:
        raise ValueError("RESEND_API_KEY not found in environment or fallback locations")

    resend.api_key = api_key

    # Read PDF and encode as base64
    pdf_bytes = Path(pdf_path).read_bytes()
    pdf_b64 = base64.b64encode(pdf_bytes).decode("utf-8")
    pdf_filename = Path(pdf_path).name

    params = {
        "from": f"OpenAI Intel Agent <{from_email}>",
        "to": [to_email],
        "subject": subject,
        "html": html_content,
        "attachments": [
            {
                "filename": pdf_filename,
                "content": pdf_b64,
            }
        ],
    }

    response = resend.Emails.send(params)
    return response


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/send_report.py <html_report_path> [--to email] [--dry-run]")
        sys.exit(1)

    html_path = sys.argv[1]
    to_email = "jackshen860302@gmail.com"
    dry_run = "--dry-run" in sys.argv

    # Parse --to flag
    if "--to" in sys.argv:
        idx = sys.argv.index("--to")
        if idx + 1 < len(sys.argv):
            to_email = sys.argv[idx + 1]

    html_file = Path(html_path)
    if not html_file.exists():
        print(f"Error: {html_path} not found")
        sys.exit(1)

    html_content = html_file.read_text()
    today = datetime.now().strftime("%Y-%m-%d")

    # Derive PDF path
    pdf_path = str(html_file.with_suffix(".pdf"))

    print(f"{'[DRY RUN] ' if dry_run else ''}OpenAI Intelligence Report Email")
    print(f"  HTML:  {html_path}")
    print(f"  To:    {to_email}")
    print()

    # Step 1: Generate PDF
    print("Step 1: Generating PDF via Playwright...")
    pdf_ok = generate_pdf(html_path, pdf_path)
    if pdf_ok:
        pdf_size = Path(pdf_path).stat().st_size
        print(f"  PDF generated: {pdf_path} ({pdf_size:,} bytes)")
    else:
        print("  WARNING: PDF generation failed. Sending email without attachment.")
        pdf_path = None

    if dry_run:
        print("\n[DRY RUN] Would send email with:")
        print(f"  Subject: OpenAI Weekly Intelligence Report — {today}")
        print(f"  To: {to_email}")
        print(f"  HTML body: {len(html_content):,} chars")
        print(f"  PDF attachment: {pdf_path or 'none'}")
        print("\nDry run complete. No email sent.")
        return

    # Step 2: Send email
    subject = f"OpenAI Weekly Intelligence Report — {today}"
    print(f"\nStep 2: Sending email via Resend...")
    print(f"  Subject: {subject}")

    try:
        if pdf_path:
            response = send_email(html_content, pdf_path, to_email, subject)
        else:
            # Send without attachment
            import resend
            api_key = os.environ.get("RESEND_API_KEY")
            if not api_key:
                env_path = Path.home() / "Desktop" / "Rewire Master" / ".env.local"
                if env_path.exists():
                    for line in env_path.read_text().splitlines():
                        if line.startswith("RESEND_API_KEY"):
                            api_key = line.split("=", 1)[1].strip().strip('"')
                            break
            resend.api_key = api_key
            response = resend.Emails.send({
                "from": f"OpenAI Intel Agent <onboarding@resend.dev>",
                "to": [to_email],
                "subject": subject,
                "html": html_content,
            })

        print(f"  Email sent successfully!")
        print(f"  Response: {response}")
    except Exception as e:
        print(f"  ERROR sending email: {e}")
        sys.exit(1)

    print(f"\nDone! Report emailed to {to_email}")


if __name__ == "__main__":
    main()
