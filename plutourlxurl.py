import re

source_file = "pluto_ar.m3u"
target_file = "principal.m3u"
output_file = "principal.m3u"

channel_urls = {}

# leer lista de pluto
with open(source_file, "r", encoding="utf-8") as f:
    for line in f:
        if "pluto.tv" in line and "/channel/" in line:
            m = re.search(r'/channel/([^/]+)/', line)
            if m:
                channel_id = m.group(1)
                channel_urls[channel_id] = line.strip()

new_lines = []

# leer lista principal
with open(target_file, "r", encoding="utf-8") as f:
    for line in f:
        if "/channel/" in line:
            m = re.search(r'/channel/([^/]+)/', line)
            if m:
                cid = m.group(1)
                if cid in channel_urls:
                    line = channel_urls[cid] + "\n"
        new_lines.append(line)

# guardar archivo actualizado
with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("principal.m3u actualizado")
