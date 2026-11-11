"""Maakt de referentie-docx-bestanden voor pandoc (eenmalig; resultaat staat in templates/).

Gebruik: python3 scripts/make_templates.py
"""
import subprocess, pathlib
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

HERE = pathlib.Path(__file__).parent
OUT = HERE / "templates"
OUT.mkdir(exist_ok=True)

HUISSTIJLEN = {
    "gemeente": {
        "font": "Arial", "size": 10, "kleur": RGBColor(0x1F, 0x4E, 0x3D),
        "kop": "Gemeente Lindewoude",
        "subkop": "Raadhuisplein 1  ·  Postbus 100, 8000 AC Lindewoude  ·  www.lindewoude.example",
    },
    "noviqo": {
        "font": "Calibri", "size": 10.5, "kleur": RGBColor(0x3B, 0x2A, 0x8C),
        "kop": "noviqo",
        "subkop": "Noviqo B.V.  ·  Verzonnelkade 88, 1099 ZZ Amsterdam  ·  KvK 91234567  ·  noviqo.example",
    },
    "extern": {
        "font": "Times New Roman", "size": 11, "kleur": RGBColor(0x20, 0x20, 0x20),
        "kop": None, "subkop": None,
    },
}
VOETTEKST = "Fictief oefendocument uit het Noviqo-dossier. Bevat geen echte personen of persoonsgegevens."

def basis(pad):
    subprocess.run(["pandoc", "-o", str(pad), "--print-default-data-file", "reference.docx"], check=True)

for naam, s in HUISSTIJLEN.items():
    pad = OUT / f"reference-{naam}.docx"
    basis(pad)
    doc = Document(pad)
    for stijl in doc.styles:
        try:
            if stijl.font is not None:
                stijl.font.name = s["font"]
                if stijl.name.startswith("Heading") or stijl.name == "Title":
                    stijl.font.color.rgb = s["kleur"]
        except Exception:
            pass
    for st in ("Normal", "Body Text", "First Paragraph", "Compact"):
        try:
            doc.styles[st].font.size = Pt(s["size"])
        except KeyError:
            pass
    for st, grootte in (("Heading 1", 14), ("Heading 2", 12), ("Heading 3", 11), ("Title", 18)):
        try:
            doc.styles[st].font.size = Pt(grootte)
        except KeyError:
            pass
    sec = doc.sections[0]
    sec.top_margin, sec.bottom_margin = Cm(3.0), Cm(2.2)
    sec.left_margin = sec.right_margin = Cm(2.4)
    kop = sec.header.paragraphs[0]
    kop.text = ""
    if s["kop"]:
        r = kop.add_run(s["kop"]); r.bold = True; r.font.size = Pt(15); r.font.color.rgb = s["kleur"]; r.font.name = s["font"]
        p2 = sec.header.add_paragraph()
        r2 = p2.add_run(s["subkop"]); r2.font.size = Pt(8); r2.font.color.rgb = RGBColor(0x60, 0x60, 0x60); r2.font.name = s["font"]
    voet = sec.footer.paragraphs[0]
    voet.text = ""
    rv = voet.add_run(VOETTEKST); rv.font.size = Pt(7.5); rv.italic = True; rv.font.color.rgb = RGBColor(0x80, 0x80, 0x80)
    voet.alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.save(pad)
    print("gemaakt:", pad)
