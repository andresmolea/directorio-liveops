import urllib.request
import os
import io
from PIL import Image

OUT_DIR = os.path.join(os.path.dirname(__file__), "avatars_small")
os.makedirs(OUT_DIR, exist_ok=True)

IMAGES = {
    "carlos-diaz": "https://avatars.slack-edge.com/2026-06-10/11332152609825_b459f0506395edbab313_original.png",
    "nestor-sivira": "https://avatars.slack-edge.com/2025-12-05/10065983225492_72ef39affc413de48a1c_original.jpg",
    "nicole-rojas": "https://avatars.slack-edge.com/2025-09-09/9475018929495_f1ef51b240e86c103262_original.png",
    "barbara-rodriguez": "https://avatars.slack-edge.com/2025-09-19/9546865038675_2ad2f98cdccc231a0d7a_original.jpg",
    "orianny-figueroa": "https://avatars.slack-edge.com/2026-06-17/11383880651462_d8973f63f3a1230b16d5_original.jpg",
    "omarlys-molina": "https://avatars.slack-edge.com/2026-07-13/11566158437047_22b4b06e5d182eb24fcd_original.jpg",
    "luisana-rivas": "https://avatars.slack-edge.com/2026-08-04/11752360895428_f8a3a33eb9d7ed61c329_original.png",
    "genesis-mestre": "https://avatars.slack-edge.com/2026-08-13/11820436501953_6f679cb1e8a21f17c9fe_original.png",
    "fabian-velazquez": "https://avatars.slack-edge.com/2026-08-18/11853314505316_c8f26c90be57df88be2c_original.png",
    "yusnery-mujica": "https://avatars.slack-edge.com/2026-09-24/12141013271910_3f51172eb3df3c091db3_original.jpg",
    "bryan-escate": "https://avatars.slack-edge.com/2026-09-29/12185037328324_9e74902696068820f6e1_original.png",

    "leon-otero": "https://avatars.slack-edge.com/2025-09-09/9486301892485_0fa96785a1f66786cd11_original.jpg",
    "eduardo-pena": "https://avatars.slack-edge.com/2026-08-04/11740088062518_426880ac68f4fc228a3e_original.jpg",
    "yeickson-diaz": "https://avatars.slack-edge.com/2025-09-23/9553640843271_0a63c0a2683c7ad40190_original.jpg",

    "johnadeisy-ramirez": "https://avatars.slack-edge.com/2026-02-09/10488820952641_da5c058b47f8b6f4d1d8_original.jpg",
    "anniuska-raga": "https://avatars.slack-edge.com/2026-03-13/10679252173207_f33131f01953854545bd_original.png",
    "gabriel-canchica": "https://avatars.slack-edge.com/2026-06-12/11342879920066_c32f1cdbffd6a6ab1b8d_original.jpg",
    "maria-medina": "https://avatars.slack-edge.com/2026-04-28/11041084668256_3a46311547c46302265b_original.png",

    "ricardo-pena": "https://avatars.slack-edge.com/2026-10-20/12364897910022_66dab0ec00c231d4d29b_original.jpg",
    "alfonso-garcia": "https://avatars.slack-edge.com/2026-10-20/12394915404672_ca89cfe60cc57e392264_original.jpg",
    "alfredo-sequera": "https://avatars.slack-edge.com/2026-10-20/12351118985831_87739f68600d73e4eb3c_original.png",
    "jeison-gonzalez": "https://avatars.slack-edge.com/2026-10-21/12372826735298_447ba22198f90f1d9fdc_original.png",
    "vereeng-ramirez": "https://avatars.slack-edge.com/2026-10-20/12361089545605_b62b9f876315b74ca8cf_original.jpg",
    "daniel-rodriguez": "https://avatars.slack-edge.com/2026-10-20/12368670710353_d5cc17f9fb06f931cb5e_original.jpg",
    "ivvanna-abzueta": "https://avatars.slack-edge.com/2026-10-20/12360251186355_6f48080b1f27d414f7bc_original.png",
    "angye-angulo": "https://avatars.slack-edge.com/2026-10-21/12358208795415_95267ca7fbecb945289c_original.png",
    "sergio-hurtado": "https://avatars.slack-edge.com/2026-10-20/12361178320021_96757b2cfb641872aca1_original.jpg",
    "sebastian-hurtado": "https://avatars.slack-edge.com/2026-10-20/12368570542817_f73d742a6541ac0e7ecd_original.jpg",
    "mikail-hidalgo": "https://avatars.slack-edge.com/2026-10-20/12360754615443_09f76102560111bc888e_original.jpg",
    "josue-tovar": "https://avatars.slack-edge.com/2026-11-11/12575284125121_78e633b8c329d2e273d4_original.jpg",
    "victoria-campos": "https://avatars.slack-edge.com/2026-10-20/12395167641264_872a1f9e47a78bfa7f26_original.jpg",
    "samuel-carrero": "https://avatars.slack-edge.com/2026-10-20/12361033393891_dc1143da6f3e6bf6b55d_original.jpg",
    "alexandra-ojeda": "https://avatars.slack-edge.com/2026-10-20/12367475433538_9673cfbf8f8156006035_original.jpg",
    "arianna-bello": "https://avatars.slack-edge.com/2026-11-15/12636474263344_eb9c4be7e594af26ce70_original.jpg",
    "estehefany-mulato": "https://avatars.slack-edge.com/2026-10-21/12371714129698_24527cefd19b3e355e38_original.jpg",
    "alesca-bracamonte": "https://avatars.slack-edge.com/2026-10-20/12370238073956_86d21003757bc6d82b0e_original.png",
    "yeniree-villa": "https://avatars.slack-edge.com/2026-10-20/12353423041527_c18352000b4cc20f7ef9_original.jpg",

    "chantal-gonzalez": "https://avatars.slack-edge.com/2026-11-18/12637468683027_1f0ef34999f47339b959_original.jpg",
    "noemi-decelis": "https://avatars.slack-edge.com/2026-11-13/12594157367254_477afdb96f3195216aea_original.png",
    "christopher-fuentes": "https://avatars.slack-edge.com/2026-11-12/12590218989441_cbd4482337b63ac251ba_original.jpg",
    "roger-sarabia": "https://avatars.slack-edge.com/2026-11-12/12578956597013_04dfdb96a76dbcc35f17_original.jpg",
    "carmen-vasquez": "https://avatars.slack-edge.com/2026-11-13/12594223182229_9a623fffe9354f024161_original.jpg",
    "lownnys-bustico": "https://avatars.slack-edge.com/2026-11-12/12593542594260_8671b0240ddbc0722947_original.jpg",
    "patricia-ceballos": "https://avatars.slack-edge.com/2026-11-19/12655265391990_52311e1320169da65025_original.jpg",
    "alexandra-ramirez": "https://avatars.slack-edge.com/2026-11-12/12614003444464_84e9113f1518f8d0d1eb_original.jpg",
}

HEADERS = {"User-Agent": "Mozilla/5.0"}

ok, fail = 0, 0
for slug, url in IMAGES.items():
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = resp.read()
        im = Image.open(io.BytesIO(data)).convert("RGB")
        # center-crop to square then resize
        w, h = im.size
        side = min(w, h)
        left = (w - side) // 2
        top = (h - side) // 2
        im = im.crop((left, top, left + side, top + side)).resize((128, 128), Image.LANCZOS)
        out_path = os.path.join(OUT_DIR, slug + ".jpg")
        im.save(out_path, "JPEG", quality=78)
        ok += 1
    except Exception as e:
        print("FAIL", slug, e)
        fail += 1

print(f"done: ok={ok} fail={fail}")
