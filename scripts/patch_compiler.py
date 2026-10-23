import re

path = r"C:\Users\Lenovo\Downloads\AI KNYGA\scripts\compile_book.py"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

new_patterns = '''    ("karpathy_software", r"\\b(Software 1\\.0|Software 2\\.0|Software 3\\.0|Andrej Karpathy|Karpathy)\\b"),
    ("one_person_unicorn", r"\\b(1 zmogaus vienaragis|vienaragio|vienaragi|1 žmogaus vienaragis|vienaragio|One-person unicorn)\\b"),
    ("backpropagation", r"\\b(Backpropagation|atgalinė sklaida|atgalinės sklaidos|atgalinio sklidimo|atgaline sklaida)\\b"),
    ("kardashev_scale", r"\\b(Kardaševo skalė|Kardaševo skalės|Kardaševo skalę|Kardashev Scale|Kardasevo skale|Kardaševo II|II Kardashev)\\b"),
    ("eliezeryudkowsky", r"\\b(Eliezer Yudkowsky|Eliezerio Yudkowsky|Yudkowsky|Yudkowskis)\\b"),
    ("eric_schmidt", r"\\b(Eric Schmidt|Erico Schmidto|Schmidtas|Schmidto)\\b"),
    ("david_baker", r"\\b(David Baker|Davido Bakerio|Bakeris|Bakerio)\\b"),
    ("daron_acemoglu", r"\\b(Daron Acemoglu|Darono Acemoglu|Acemoglu)\\b"),
    ("mustafa_suleyman", r"\\b(Mustafa Suleyman|Mustafos Suleymano|Suleymanas)\\b"),
    ("brett_adcock", r"\\b(Brett Adcock|Bretto Adcocko|Adcockas)\\b"),
    ("ship_of_theseus", r"\\b(Tesėjo laivas|Tesėjo laivo|Tesėjo laivą|Tesejo laivas|Ship of Theseus)\\b"),
    ("landauer_limit", r"\\b(Landauerio riba|Landauerio ribos|Landauerio principas|Landauerio limitas)\\b"),
    ("von_neumann_probes", r"\\b(Von Neumanno zondai|Von Neumanno zondų|Von Neumanno zondas|Von Neumann probes)\\b"),
    ("crispr", r"\\b(CRISPR|Cas9|genų inžinerija|DNR redagavimas)\\b"),
    ("longevity_escape_velocity", r"\\b(pabėgimo greitis nuo senėjimo|Ilgaamžiškumo pabėgimo greitis|Longevity Escape Velocity)\\b"),
    ("paperclip_maximizer", r"\\b(sąvaržėlių maksimizatorius|sąvaržėlių maksimizatoriaus|Paperclip Maximizer)\\b")
]'''

content = re.sub(r'    \("karpathy_software",.*?\n    \("one_person_unicorn",.*?\n\]', new_patterns, content, flags=re.DOTALL)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated compile_book.py with all 49 term patterns!")
