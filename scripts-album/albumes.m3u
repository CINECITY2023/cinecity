const albums = [
  {
    name: "Linkin Park - Hybrid Theory",
    m3u: "https://raw.githubusercontent.com/CINECITY2023/cinecity/refs/heads/cinecity.net/album-mp3-m3u/linkin_park_hybridtheory.m3u",
    cover: "https://ia803204.us.archive.org/11/items/linkinparkhybridtheory_202007/Linkin_Park_Hybrid_Theory_Album_Cover.jpg?cnt=0"
  },
  {
    name: "RHCP - Californication",
    m3u: "https://raw.githubusercontent.com/CINECITY2023/cinecity/refs/heads/cinecity.net/album-mp3-m3u/rhc-californication.m3u",
    cover: "https://ia600306.us.archive.org/33/items/02-parallel-universe/cover.jpg?cnt=0"
  },
  {
    name: "Eurotecno",
    m3u: "https://raw.githubusercontent.com/CINECITY2023/cinecity/refs/heads/cinecity.net/album-mp3-m3u/Eurotecno.m3u",
    cover: "https://raw.githubusercontent.com/CINECITY2023/cinecity/refs/heads/cinecity.net/logos/album-mp3/eurotecno.jpg"
  },
  {
    name: "Guns'n Roses - Greatest Hits",
    m3u: "https://raw.githubusercontent.com/CINECITY2023/cinecity/refs/heads/cinecity.net/album-mp3-m3u/guns-n-roses.m3u",
    cover: "https://ia601702.us.archive.org/1/items/guns-n-roses_202301/GUNS_N_ROSES_GREATEST_HITS.jpg?cnt=0"
  },
  {
    name: "AC-DC - Greatest Hits",
    m3u: "https://raw.githubusercontent.com/CINECITY2023/cinecity/refs/heads/cinecity.net/album-mp3-m3u/acdc.m3u",
    cover: "https://ia600503.us.archive.org/10/items/Filmato/00.jpg?cnt=0"
  },
  {
    name: "Gorillaz - Greatest Hits",
    m3u: "https://raw.githubusercontent.com/CINECITY2023/cinecity/refs/heads/cinecity.net/album-mp3-m3u/gorillaz-68-state_vbr.m3u",
    cover: "https://i.discogs.com/7f2Y-3P53IYQHXrahXKcSfL2TEZkctJL1BM0RH_Ih24/rs:fit/g:sm/q:90/h:591/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTk3MjI2/MDMtMTQ4NTcwNTc5/Mi00MTgyLmpwZWc.jpeg"
  }
];

const container = document.getElementById('albumGrid');

albums.forEach(album => {
  const div = document.createElement('div');
  div.className = 'album';
  div.innerHTML = `
    <img src="${album.cover}" alt="${album.name}">
    <div class="album-name">${album.name}</div>
  `;
  div.onclick = () => {
    localStorage.setItem('selectedAlbum', JSON.stringify(album));
    window.location.href = 'index.html';
  };
  container.appendChild(div);
});
