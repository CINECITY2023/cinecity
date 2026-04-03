import re
import json
import requests

M3U_URL = "https://raw.githubusercontent.com/CINECITY2023/cinecity/refs/heads/cinecity.net/pluto_ar.m3u"
JSON_FILE = "scripts-album/PlutoTV.json"

# Descargar M3U
m3u = requests.get(M3U_URL).text

# Extraer URLs por ID
pattern = r'(https://cfd-v4-service-channel-stitcher-use1-1\.prd\.pluto\.tv[^\s]+)'
urls = re.findall(pattern, m3u)

# Crear diccionario {id: url}
url_dict = {}
for url in urls:
    match = re.search(r'/channel/([a-z0-9]+)/', url)
    if match:
        channel_id = match.group(1)
        url_dict[channel_id] = url

# Cargar JSON
with open(JSON_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# Reemplazar URLs
for canal in data:
    if "url" in canal:
        match = re.search(r'/channel/([a-z0-9]+)/', canal["url"])
        if match:
            cid = match.group(1)
            if cid in url_dict:
                canal["url"] = url_dict[cid]

# Guardar JSON actualizado
with open(JSON_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
