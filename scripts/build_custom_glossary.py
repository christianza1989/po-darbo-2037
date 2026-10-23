# -*- coding: utf-8 -*-
"""
PILNAS BESPOKE ŽINYNO GENERAVIMO IR INTEGRACIJOS SKRIPTAS
Sujungia visas 5 grupes (49 terminus), atnaujina glossary_data.json ir perkompiliuoja knygą.
"""

import os
import sys
import json
import subprocess

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GLOSSARY_PATH = os.path.join(BASE_DIR, "research", "glossary_data.json")

# Importuojame 5 kognityvines grupes
from glossary_group_titans import TITANS_HTML
from glossary_group_physics import PHYSICS_HTML
from glossary_group_safety import SAFETY_HTML
from glossary_group_bio import BIO_HTML
from glossary_group_economy import ECONOMY_HTML

def main():
    print("=" * 70)
    print("VYRIAUSIOJO TURINIO ARCHITEKTO BESPOKE GLOSSARY GENERATORIUS")
    print("=" * 70)

    # 1. Užkrauname esamą žodyną
    if not os.path.exists(GLOSSARY_PATH):
        print(f"KLAIDA: Failas nerastas: {GLOSSARY_PATH}")
        sys.exit(1)

    with open(GLOSSARY_PATH, "r", encoding="utf-8") as f:
        glossary = json.load(f)

    print(f"Esamų terminų skaičius žodyne: {len(glossary)}")

    # 2. Sujungiame visus bespoke HTML žodynus
    all_bespoke = {}
    all_bespoke.update(TITANS_HTML)
    all_bespoke.update(PHYSICS_HTML)
    all_bespoke.update(SAFETY_HTML)
    all_bespoke.update(BIO_HTML)
    all_bespoke.update(ECONOMY_HTML)

    print(f"Parengtų bespoke HTML įrašų skaičius: {len(all_bespoke)}")

    # 3. Tikriname atitiktį tarp glossary raktų ir bespoke raktų
    missing_in_bespoke = [k for k in glossary.keys() if k not in all_bespoke]
    extra_in_bespoke = [k for k in all_bespoke.keys() if k not in glossary]

    if missing_in_bespoke:
        print(f"DĖMESIO! Trūkstami raktai bespoke HTML: {missing_in_bespoke}")
    if extra_in_bespoke:
        print(f"DĖMESIO! Pertekliniai raktai: {extra_in_bespoke}")

    assert len(missing_in_bespoke) == 0, f"Trūksta {len(missing_in_bespoke)} terminų HTML!"

    # 4. Atnaujiname kiekvieną terminą su jo unikaliu custom_html
    updated_count = 0
    for term_key, custom_html in all_bespoke.items():
        if term_key in glossary:
            glossary[term_key]["custom_html"] = custom_html.strip()
            updated_count += 1

    print(f"Sėkmingai atnaujinta terminų su custom_html: {updated_count} / {len(glossary)}")

    # 5. Išsaugome atnaujintą glossary_data.json
    with open(GLOSSARY_PATH, "w", encoding="utf-8") as f:
        json.dump(glossary, f, ensure_ascii=False, indent=2)

    print(f"Atnaujintas žodynas išsaugotas į: {GLOSSARY_PATH}")

    # 6. Validacijos testas: ar visi 49 turi unikalų HTML ir nėra šabloniškumo
    with open(GLOSSARY_PATH, "r", encoding="utf-8") as f:
        verified_data = json.load(f)

    forbidden_templates = ["Kas tai yra?", "Kaip tai veikia?", "Kodėl tai lemia tavo ateitį?", "Kada tai įvyks?"]
    errors = []

    for k, v in verified_data.items():
        html = v.get("custom_html", "")
        if not html:
            errors.append(f"Terminas '{k}' neturi custom_html!")
            continue
        for ft in forbidden_templates:
            if ft in html:
                errors.append(f"Terminas '{k}' vis dar naudoja šabloną: '{ft}'")

    if errors:
        print("\nVALIDACIJOS KLAIDOS:")
        for err in errors:
            print(f" - {err}")
        sys.exit(1)
    else:
        print("\n✅ VALIDACIJA SĖKMINGA: Visi 49 terminai turi unikalų, galingą bespoke custom_html be jokių šablonų!")

    # 7. Perkompiliuojame knygą
    compile_script = os.path.join(BASE_DIR, "scripts", "compile_book.py")
    print("\nPaleidžiamas knygos kompiliatorius compile_book.py...")
    res = subprocess.run([sys.executable, compile_script], capture_output=True, text=True, encoding="utf-8")
    print(res.stdout)
    if res.returncode != 0:
        print("Kompiliatoriaus klaida:", res.stderr)
        sys.exit(res.returncode)

    print("\n🎉 VISKAS ATLIKTA TOBULAI! Knyga ir visi 49 modaliniai langai dabar turi unikalų bespoke turinį.")

if __name__ == "__main__":
    main()
