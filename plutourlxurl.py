import re

source_file = "pluto_ar.m3u"

# todos los m3u que quieres actualizar
target_files = [
    "principal.m3u",
    "Alicia.m3u",
    "juanpablo.m3u",
    "mariano.m3u"
]

channel_urls = {}

# leer pluto_ar
with open(source_file, "r", encoding="utf-8") as f:
    for line in f:
        if "pluto.tv" in line and "/channel/" in line:
            m = re.search(r'/channel/([^/]+)/', line)
            if m:
                channel_id = m.group(1)
                channel_urls[channel_id] = line.strip()

# actualizar cada lista
for target_file in target_files:

    new_lines = []

    with open(target_file, "r", encoding="utf-8") as f:
        for line in f:
            if "/channel/" in line:
                m = re.search(r'/channel/([^/]+)/', line)
                if m:
                    cid = m.group(1)
                    if cid in channel_urls:
                        line = channel_urls[cid] + "\n"
            new_lines.append(line)

    with open(target_file, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print(f"{target_file} actualizado")
