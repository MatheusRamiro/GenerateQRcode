import qrcode

links_lives = {
    "Pedro": "https://www.twitch.tv/pegroso",
    "Matheus": "https://www.twitch.tv/ram1rofps"
}
for live in links_lives:
    link = links_lives[live]
    imagem_qrcode = qrcode.make(link)
    imagem_qrcode.save(f"qrcode_{live}.png")