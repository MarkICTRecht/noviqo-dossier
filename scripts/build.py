#!/usr/bin/env python3
"""Bouwt het deelnemerspakket Gemeente Lindewoude uit de markdownbronnen.

Markdown blijft de bron. Dit script maakt per stuk een Word-bestand, een PDF of een
'gescande' PDF, volgens MANIFEST hieronder, en pakt alles in een zip in dist/.

Benodigd: pandoc, LibreOffice (soffice), poppler-utils (pdftoppm), ImageMagick (convert),
img2pdf, fontconfig. Lokaal draaien: python3 scripts/build.py
"""
import pathlib
import shutil
import subprocess
import sys
import tempfile
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "scripts" / "templates"
DIST = ROOT / "dist"
PAKKET = "noviqo-gemeente-lindewoude"
S1 = "20 Gemeente Lindewoude/Spoor 1 Handhaving terras"
S2 = "20 Gemeente Lindewoude/Spoor 2 Contract PlanGrip"

# (bron, map in de zip, formaat, huisstijl)
# formaat: docx | pdf | scan     huisstijl: gemeente | noviqo | extern
MANIFEST = [
    ("20 Gemeente Lindewoude/00 Lees mij eerst - deelnemerspakket Gemeente Lindewoude.md", "", "pdf", "extern"),
    (f"{S1}/Constateringsrapport terras Brasserie De Waag (2026-07-18).md", "Spoor 1 Handhaving terras", "pdf", "gemeente"),
    (f"{S1}/Voornemen last onder dwangsom Brasserie De Waag (2026-07-21).md", "Spoor 1 Handhaving terras", "docx", "gemeente"),
    (f"{S1}/Zienswijze Brasserie De Waag per e-mail (2026-07-27).md", "Spoor 1 Handhaving terras", "pdf", "extern"),
    (f"{S1}/Besluit last onder dwangsom Brasserie De Waag (2026-08-06).md", "Spoor 1 Handhaving terras", "docx", "gemeente"),
    (f"{S1}/Bezwaarschrift Brasserie De Waag (2026-09-02).md", "Spoor 1 Handhaving terras", "scan", "extern"),
    (f"{S1}/Beleidsregel handhaving terrassen Lindewoude 2025.md", "Spoor 1 Handhaving terras", "docx", "gemeente"),
    (f"{S1}/Format advies commissie bezwaarschriften Lindewoude.md", "Spoor 1 Handhaving terras", "docx", "gemeente"),
    ("05 Verkoopcontracten/Overeenkomst PlanGrip - Gemeente Lindewoude (2026-03-16).md", "Spoor 2 Contract PlanGrip", "pdf", "extern"),
    (f"{S2}/E-mailwisseling implementatie PlanGrip Lindewoude (april-augustus 2026).md", "Spoor 2 Contract PlanGrip", "pdf", "extern"),
    (f"{S2}/Boeteaanzegging Noviqo oplevering en incidentmelding (2026-09-07).md", "Spoor 2 Contract PlanGrip", "docx", "gemeente"),
    (f"{S2}/Reactie Noviqo op boeteaanzegging Lindewoude (2026-09-21).md", "Spoor 2 Contract PlanGrip", "pdf", "noviqo"),
]

# Extra's op de gescande stukken: ontvangststempel en handgeschreven aantekening.
SCAN_EXTRAS = {
    "Bezwaarschrift Brasserie De Waag (2026-09-02).md": {
        "stempel": "ONTVANGEN\n4 SEP 2026\nGEMEENTE LINDEWOUDE",
        "hand": "PS. Mijn mail van 27/7 en de\nbevestiging van mw. Dijkhuis\nstuur ik nog na!  T.H.",
    },
}


def run(cmd, **kw):
    subprocess.run(cmd, check=True, **kw)


def naar_docx(bron: pathlib.Path, doel: pathlib.Path, stijl: str):
    run([
        "pandoc", str(bron), "-f", "markdown+hard_line_breaks", "-o", str(doel),
        f"--reference-doc={TEMPLATES / f'reference-{stijl}.docx'}",
    ])


def naar_pdf(docx: pathlib.Path, doelmap: pathlib.Path) -> pathlib.Path:
    run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(doelmap), str(docx)],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return doelmap / (docx.stem + ".pdf")


def font(naam: str) -> str:
    return subprocess.run(["fc-match", "-f", "%{file}", naam], capture_output=True, text=True).stdout.strip()


def scan(pdf: pathlib.Path, doel: pathlib.Path, extras: dict | None, tmp: pathlib.Path):
    """Maakt van een nette PDF een scan-achtige PDF: rasteren, grijs, licht scheef, ruis."""
    prefix = tmp / "pagina"
    run(["pdftoppm", "-r", "110", "-gray", "-png", str(pdf), str(prefix)])
    paginas = sorted(tmp.glob("pagina*.png"))
    hand = font("Z003:italic") or font("cursive")
    stempelfont = font("DejaVu Sans:bold")
    uit = []
    for i, p in enumerate(paginas):
        q = tmp / f"scan-{i:02d}.png"
        cmd = ["convert", str(p)]
        if extras and i == 0 and extras.get("stempel"):
            cmd += ["-font", stempelfont, "-pointsize", "17", "-fill", "gray35", "-stroke", "gray35",
                    "-strokewidth", "0.6", "-gravity", "NorthEast", "-annotate", "-8x-8+70+150",
                    extras["stempel"]]
        if extras and i == len(paginas) - 1 and extras.get("hand"):
            cmd += ["-font", hand, "-pointsize", "22", "-fill", "gray15", "-stroke", "none",
                    "-gravity", "SouthEast", "-annotate", "-4x-4+70+95", extras["hand"]]
        cmd += ["-background", "white", "-rotate", "0.7" if i % 2 == 0 else "-0.5",
                "-attenuate", "0.35", "+noise", "Gaussian", "-blur", "0x0.4",
                "-level", "8%,92%", "-alpha", "off", "-quality", "70", str(q)]
        run(cmd)
        uit.append(str(q))
    run(["img2pdf", *uit, "-o", str(doel)])


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    staging = DIST / PAKKET
    staging.mkdir(parents=True)
    for bron_rel, map_in_zip, formaat, stijl in MANIFEST:
        bron = ROOT / bron_rel
        if not bron.exists():
            sys.exit(f"Bron ontbreekt: {bron_rel}")
        doelmap = staging / map_in_zip
        doelmap.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory() as t:
            tmp = pathlib.Path(t)
            docx = tmp / (bron.stem + ".docx")
            naar_docx(bron, docx, stijl)
            if formaat == "docx":
                shutil.copy(docx, doelmap / docx.name)
            else:
                pdf = naar_pdf(docx, tmp)
                if formaat == "pdf":
                    shutil.copy(pdf, doelmap / pdf.name)
                else:
                    scan(pdf, doelmap / pdf.name, SCAN_EXTRAS.get(bron.name), tmp)
        print(f"{formaat:5} {bron.name}")
    zippad = DIST / f"{PAKKET}.zip"
    with zipfile.ZipFile(zippad, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(staging.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(DIST))
    print(f"Klaar: {zippad.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
