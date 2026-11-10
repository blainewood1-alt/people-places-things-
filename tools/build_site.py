"""Builds the Blaine Wood Photo pages from the lists below.

Run:  python3 tools/build_site.py            (writes the site to the repo root)
      python3 tools/build_site.py preview    (writes a preview copy to preview/)

Edit the lists below to add or move photos, then run it again.
"""
import html
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PREVIEW = len(sys.argv) > 1 and sys.argv[1] == "preview"
OUT = os.path.join(ROOT, "preview") if PREVIEW else ROOT
UP = "../" if PREVIEW else ""  # path from the pages to the shared images folder
EMAIL = "blainewood1@gmail.com"
SIZES = ["8 × 12 in", "12 × 18 in", "16 × 24 in", "20 × 30 in", "24 × 36 in"]
YEAR = 2026
INSTAGRAM = "https://www.instagram.com/blaine_would/"
FOTO = "https://the.fotoapp.co/blaine_wood"
# Instagram glyph from Simple Icons (CC0)
IG_PATH = "M7.0301.084c-1.2768.0602-2.1487.264-2.911.5634-.7888.3075-1.4575.72-2.1228 1.3877-.6652.6677-1.075 1.3368-1.3802 2.127-.2954.7638-.4956 1.6365-.552 2.914-.0564 1.2775-.0689 1.6882-.0626 4.947.0062 3.2586.0206 3.6671.0825 4.9473.061 1.2765.264 2.1482.5635 2.9107.308.7889.72 1.4573 1.388 2.1228.6679.6655 1.3365 1.0743 2.1285 1.38.7632.295 1.6361.4961 2.9134.552 1.2773.056 1.6884.069 4.9462.0627 3.2578-.0062 3.668-.0207 4.9478-.0814 1.28-.0607 2.147-.2652 2.9098-.5633.7889-.3086 1.4578-.72 2.1228-1.3881.665-.6682 1.0745-1.3378 1.3795-2.1284.2957-.7632.4966-1.636.552-2.9124.056-1.2809.0692-1.6898.063-4.948-.0063-3.2583-.021-3.6668-.0817-4.9465-.0607-1.2797-.264-2.1487-.5633-2.9117-.3084-.7889-.72-1.4568-1.3876-2.1228C21.2982 1.33 20.628.9208 19.8378.6165 19.074.321 18.2017.1197 16.9244.0645 15.6471.0093 15.236-.005 11.977.0014 8.718.0076 8.31.0215 7.0301.0839m.1402 21.6932c-1.17-.0509-1.8053-.2453-2.2287-.408-.5606-.216-.96-.4771-1.3819-.895-.422-.4178-.6811-.8186-.9-1.378-.1644-.4234-.3624-1.058-.4171-2.228-.0595-1.2645-.072-1.6442-.079-4.848-.007-3.2037.0053-3.583.0607-4.848.05-1.169.2456-1.805.408-2.2282.216-.5613.4762-.96.895-1.3816.4188-.4217.8184-.6814 1.3783-.9003.423-.1651 1.0575-.3614 2.227-.4171 1.2655-.06 1.6447-.072 4.848-.079 3.2033-.007 3.5835.005 4.8495.0608 1.169.0508 1.8053.2445 2.228.408.5608.216.96.4754 1.3816.895.4217.4194.6816.8176.9005 1.3787.1653.4217.3617 1.056.4169 2.2263.0602 1.2655.0739 1.645.0796 4.848.0058 3.203-.0055 3.5834-.061 4.848-.051 1.17-.245 1.8055-.408 2.2294-.216.5604-.4763.96-.8954 1.3814-.419.4215-.8181.6811-1.3783.9-.4224.1649-1.0577.3617-2.2262.4174-1.2656.0595-1.6448.072-4.8493.079-3.2045.007-3.5825-.006-4.848-.0608M16.953 5.5864A1.44 1.44 0 1 0 18.39 4.144a1.44 1.44 0 0 0-1.437 1.4424M5.8385 12.012c.0067 3.4032 2.7706 6.1557 6.173 6.1493 3.4026-.0065 6.157-2.7701 6.1506-6.1733-.0065-3.4032-2.771-6.1565-6.174-6.1498-3.403.0067-6.156 2.771-6.1496 6.1738M8 12.0077a4 4 0 1 1 4.008 3.9921A3.9996 3.9996 0 0 1 8 12.0077"

# Single prints: [file in images/prints, alt text, title]
PRINTS = json.load(open(os.path.join(ROOT, "tools", "prints.json")))
PRINT_BY_TITLE = {t: (f, a) for f, a, t in PRINTS}


def P(title):
    """A photo that lives in images/prints (looked up by its print title)."""
    f, a = PRINT_BY_TITLE[title]
    return ("prints/" + f, a, title)


def F(slug, alt, title):
    """A photo that lives in images/portfolio."""
    return ("portfolio/" + slug + ".jpg", alt, title)


# ---------- Portfolio galleries ----------
_OLD_GALLERIES = [
    ("street", "Street", "Everyday Atlanta: light, shadow and people going about their day.", [
        P("Long Shadow"), F("look-left", "A woman in a pink hat walking past a black car and a painted 'Look Left' sign", "Look Left"),
        F("sun-shield", "A man shading his head with a sheet of paper as he crosses a sunny street", "Sun Shield"),
        F("bench-in-the-light", "A figure on a bench in a slice of hard light surrounded by black shadow", "Bench in the Light"),
        P("Morning Walk"), F("red-umbrella", "A red umbrella on an escalator seen from above", "Red Umbrella"),
        P("Window Shopping"), F("under-the-bridge", "Sun bursting under a dark overpass beside a street lamp", "Under the Bridge"),
        P("Welcome to Inman Park"), P("Platform"), F("tower", "A lone figure at the foot of a tall building in deep shadow", "Tower"),
        P("Into the Light"), P("Stone Steps"), P("Splash Pad"), P("Passing Train"),
        F("ribbed-corridor", "A ribbed white corridor narrowing to a bright doorway", "Ribbed Corridor"),
        F("atrium", "Looking straight up a hotel atrium lined with balconies", "Atrium"),
        F("the-dome", "Looking up into the ornate dome of the Georgia Capitol", "The Dome"),
        P("Mural Reflection"),
    ]),
    ("signs", "Signs and Neon", "Ghost signs, marquees and neon that give Atlanta its character.", [
        P("Majestic Diner"), P("The Fox"), P("The Varsity"), P("Motor Hotel, Black and White"),
        F("clermont", "The Clermont Hotel neon sign glowing against a blue night sky", "Clermont"),
        F("birdcage", "A pink neon 'Birdcage' sign on a white wall above a blue bench", "Birdcage"),
        F("ponce-at-night", "Ponce City Market's tower lit up at night", "Ponce at Night"),
        P("Ponce City Market"), P("Motor Hotel, Afternoon"), P("Clermont Nights"),
        F("drink-coca-cola", "A faded hand-painted Drink Coca-Cola ad on a brick wall", "Drink Coca-Cola"),
        F("ice-cold", "A painted 'Ice Cold Coca-Cola Sold Here' sign", "Ice Cold"),
        F("manuels-tavern", "The painted Manuel's Tavern sign on a brick wall at night", "Manuel's Tavern"),
        F("millers-rexall", "The Miller's Rexall Drugs sign", "Miller's Rexall"),
        F("red-bar", "A bar glowing red with reflections on the counter", "Red Bar"),
        F("arches", "Neon arches reflected in a dark floor", "Arches"),
        F("ferris-wheel", "A Ferris wheel lit in red, white and blue at night", "Ferris Wheel"),
        F("gas-station", "A brightly lit gas station at night", "Gas Station"),
        P("Georgia Girl"),
    ]),
    ("places", "Places", "Atlanta from above, the Gulf Coast, Yellowstone and Vietnam.", [
        F("karst-valley", "A green river valley between karst mountains in Vietnam", "Karst Valley"),
        F("skyline-rays", "Rays of light over the Midtown Atlanta skyline at sunrise", "Skyline Rays"),
        F("grand-prismatic", "The rainbow rings of Grand Prismatic Spring", "Grand Prismatic"),
        F("city-lights", "Atlanta lit up at night from above", "City Lights"),
        F("old-faithful", "Old Faithful erupting under a blue sky", "Old Faithful"),
        P("Pier at Sunset"), F("golden-morning", "Golden morning light across the Atlanta skyline", "Golden Morning"),
        F("morning-glory", "The turquoise and orange Morning Glory Pool", "Morning Glory"),
        P("Trail to the Beach"), P("Heron on the Dock"), P("The Boathouse"),
        F("river-rapids", "White-water rapids in a pine-lined Yellowstone river", "River Rapids"),
        F("ember-sky", "A deep orange sunset sky over a dark city skyline", "Ember Sky"),
        P("Palm Silhouettes"), F("meadow-stream", "A stream winding through a green Yellowstone meadow", "Meadow Stream"),
        F("steaming-pool", "Steam rising off a bright blue hot spring", "Steaming Pool"),
        P("Beach Umbrella"), F("container-wall", "Stacked shipping containers under a deep blue sky", "Container Wall"),
        P("Boxcar"), F("the-mural", "A woman beside a bright geometric mural", "The Mural"),
        P("Old Cadillac"), P("Hood Ornament"), P("Last Light"), P("Rush Hour"),
        F("midnight", "Downtown Atlanta glowing at midnight from above", "Midnight"),
    ]),
    ("silhouettes", "Silhouettes and Light", "Dark shapes against bright skies and the last light of the day.", [
        F("lone-cypress", "A wind-shaped cypress tree silhouetted against a white sky, with birds", "Lone Cypress"),
        F("windswept", "A twisted white cypress on a coastal bluff", "Windswept"),
        F("in-the-window", "A man silhouetted in a bright window frame", "In the Window"),
        P("On the Edge"), F("leap", "A woman leaping, silhouetted against a bright sky", "Leap"),
        P("Lone Angler"), F("into-the-fog", "Two towers disappearing into fog", "Into the Fog"),
        F("surf-casters", "Fishermen casting into the surf at blue hour", "Surf Casters"),
        F("two-at-dusk", "Two people sitting on a dune at dusk under a crescent moon", "Two at Dusk"),
        P("Swing Ride"), F("pier-at-sundown", "A long pier on the horizon at sundown", "Pier at Sundown"),
        F("angler-blue-hour", "A lone angler at the water's edge under a deep blue sky", "Angler, Blue Hour"),
        P("Paddle Out"), F("walk-with-the-dog", "A woman and her dog walking toward the setting sun", "Walk with the Dog"),
    ]),
    ("faces", "Faces", "Strangers and neighbors met along the way.", [
        P("The Cowboy"), F("the-barber", "A barber at work by a window", "The Barber"),
        F("looking-up", "A woman in sunglasses looking up, in black and white", "Looking Up"),
        P("Gray Beanie"), F("waiting-at-marta", "A woman in a striped dress waiting outside a MARTA station", "Waiting at MARTA"),
        F("three-on-a-wall", "Three friends sitting on a low wall", "Three on a Wall"),
        P("The Fisherman"), P("Sun Seeker"),
    ]),
    ("film", "Film", "One roll on the Gulf Coast, plus a few frames from home.", [
        F("white-dunes", "White dunes and green brush under a pale sky", "White Dunes"),
        F("sea-oats", "Sea oats on a dune against a blue sky", "Sea Oats"),
        F("film-palm", "A lone palm on a sandy dune at sunset", "Lone Palm"),
        F("marsh", "A golden marsh stretching to the horizon", "Marsh"),
        F("walker-on-the-shore", "A lone walker far down an empty beach", "Walker on the Shore"),
        F("red-wall-blue-sky", "A cyclist passing a red and white wall under a blue sky", "Red Wall, Blue Sky"),
        P("Quiet Beach"),
    ]),
]


# Every photo above, looked up by title, so the galleries below can just list titles.
PHOTO = {ph[2]: ph for _, _, _, photos in _OLD_GALLERIES for ph in photos}


def G(*titles):
    return [PHOTO[t] for t in titles]


def ORDER(photos, *titles):
    """Return photos in the given title order (every photo must be listed once)."""
    by = {ph[2]: ph for ph in photos}
    assert sorted(by) == sorted(titles), set(by) ^ set(titles)
    return [by[t] for t in titles]


GALLERIES = [
    ("people", "People", "Strangers, neighbors and lone figures in the light.", ORDER(
        G(
        "Long Shadow", "The Cowboy", "The Barber", "Looking Up", "Lone Angler",
        "Bench in the Light", "Morning Walk", "In the Window", "Window Shopping",
        "Gray Beanie", "Platform", "The Fisherman", "Into the Light", "Two at Dusk", "Stone Steps", "Splash Pad",
        "Sun Seeker", "On the Edge", "Paddle Out") + [
        F("peace-dove", "A man jogging past a mural of a white dove and a parked car", "Peace Dove"),
        F("platinum", "A platinum-blonde woman in a black dress walking down steps toward a city park", "Platinum"),
        F("the-crowd", "A sea of soccer fans in blue and white jerseys, seen from above", "The Crowd"),
        F("champions", "Soccer fans in Argentina jerseys shouting and celebrating at dusk", "Champions"),
        F("the-dive", "A swimmer flipping off a dock into the water under big clouds", "The Dive"),
        F("red-sweater", "A woman in a red sweater walking through a slice of sun on a yellow wall", "Red Sweater"),
        F("red-bike", "A cyclist in red pedaling across a blurred plaza", "Red Bike"),
        F("market-day", "People browsing under yellow tarps at an outdoor market", "Market Day"),
        F("on-horseback", "A man in a cowboy hat riding a horse down a city street", "On Horseback"),
        F("river-crossing", "Women in white and conical hats riding a rowboat on a river", "River Crossing"),
        F("weathered", "A black and white portrait of an older man with a lined face", "Weathered"),
        F("after-hours", "A young woman with copper bangs holding a drink at night", "After Hours"),
        F("street-chess", "Two men playing chess at a sidewalk table while a boy and others watch", "Street Chess"),
        F("curlers", "A woman in pink hair curlers with a cigarette, holding up a pink sandal", "Curlers"),
        F("rodeo-clown", "A man in clown makeup and a cowboy hat crouching beside a fire hydrant", "Rodeo Clown"),
        F("three-in-black", "Three people in black suits walking toward the camera, backlit between towers", "Three in Black"),
        F("the-doorway", "A woman silhouetted walking down a dark hallway toward a lit doorway", "The Doorway"),
        F("over-the-shoulder", "A toddler pointing at the camera over a woman's shoulder", "Over the Shoulder"),
        F("on-the-tracks", "A man in a flat cap sitting on a railroad track under a bridge", "On the Tracks"),
        PHOTO["Birdcage"],
        F("night-parade", "Men in striped nightgowns and nightcaps walking in a procession at night", "Night Parade"),
        F("waiting-for-a-set", "A surfer sitting on a longboard in open turquoise water, seen from above", "Waiting for a Set"),
        F("afternoon-nap", "A person in a patterned tracksuit napping on a red sofa with a towel over their head", "Afternoon Nap"),
        F("in-the-woods", "A man in a fur hat and shearling coat standing in bare winter woods", "In the Woods"),
        F("blue-eyes", "A close-up of pale blue eyes, half the face in shadow", "Blue Eyes"),
        F("unspoken", "A blonde woman in a black cap and oval sunglasses in hard evening light", "Unspoken"),
        F("half-light", "A man in a dark suit, his face cut in half by a slash of hard light", "Half Light")],
        # Sequence: dawn to night, alternating black-and-white and color.
        "Lone Angler", "The Fisherman", "River Crossing", "Morning Walk", "Peace Dove",
        "Over the Shoulder", "Platform", "Long Shadow", "Red Bike", "Into the Light",
        "Red Sweater", "Window Shopping", "The Barber", "Market Day", "On Horseback",
        "Rodeo Clown", "The Cowboy", "Three in Black", "Street Chess", "Looking Up",
        "Bench in the Light", "Waiting for a Set", "Paddle Out", "Sun Seeker", "Unspoken",
        "The Dive", "Splash Pad", "The Crowd", "Stone Steps", "Champions",
        "On the Edge", "Platinum", "Two at Dusk", "Gray Beanie", "Birdcage",
        "Night Parade", "Curlers", "In the Window", "After Hours", "Half Light", "Weathered",
        "Blue Eyes", "On the Tracks", "The Doorway", "In the Woods", "Afternoon Nap")),
    ("places", "Places", "From Atlanta and beyond...", G(
        "Karst Valley", "Skyline Rays", "Lone Cypress", "Windswept",
        "Pier at Sunset", "Under the Bridge", "Golden Morning", "Morning Glory", "Into the Fog",
        "Trail to the Beach", "Sea Oats", "The Boathouse", "Palm Silhouettes", "Pier at Sundown", "Marsh", "Quiet Beach", "Last Light", "Rush Hour") + [
        F("manarola", "Pastel houses stacked on a cliff above the harbor in Manarola, Italy", "Manarola"),
        F("rolling-hills", "Green rolling hills and a line of trees under a pink and teal dusk sky", "Rolling Hills"),
        F("blue-and-white", "Rows of blue and white striped umbrellas and blue loungers on a beach in Italy", "Blue and White"),
        F("green-water", "Emerald green surf rolling toward a hazy line of beach hotels", "Green Water"),
        F("low-tide", "A lone figure on a bright sandbar beneath a dark bridge at low tide", "Low Tide")]),
    ("things", "Things", "Signs, neon, cars and the buildings around them.", G(
        "The Fox", "The Varsity", "Old Cadillac", "Motor Hotel, Black and White", "Atrium", "Ponce at Night", "Ribbed Corridor", "Ponce City Market", "Hood Ornament", "Miller's Rexall", "Motor Hotel, Afternoon", "Clermont Nights", "Swing Ride", "Georgia Girl",
        "Passing Train", "Mural Reflection") + [
        F("red-car", "A red sports car parked alone at the end of an empty, weathered concrete garage", "Red Car")]),
]

# ---------- Print sets ----------
SETS = [
    ("Coast at Dusk", "Lone figures against the last light on the Gulf, deep blue fading to orange.", [
        P("Lone Angler"), F("angler-blue-hour", "", "Angler, Blue Hour"), F("surf-casters", "", "Surf Casters"),
        F("two-at-dusk", "", "Two at Dusk"), F("pier-at-sundown", "", "Pier at Sundown"), F("walk-with-the-dog", "", "Walk with the Dog")]),
    ("Ghost Signs", "Hand-painted brick-wall ads in red, cream and black. The most Atlanta set of all.", [
        F("drink-coca-cola", "", "Drink Coca-Cola"), F("refreshing", "", "Refreshing"), F("delicious", "", "Delicious"),
        F("ice-cold", "", "Ice Cold"), F("manuels-tavern", "", "Manuel's Tavern"), F("millers-rexall", "", "Miller's Rexall")]),
    ("Silhouettes", "Dark shapes against bright, empty skies, with plenty of room to breathe.", [
        F("lone-cypress", "", "Lone Cypress"), F("windswept", "", "Windswept"), F("in-the-window", "", "In the Window"),
        F("leap", "", "Leap"), F("into-the-fog", "", "Into the Fog")]),
    ("Neon Nights", "Saturated color glowing out of the dark.", [
        F("ferris-wheel", "", "Ferris Wheel"), F("gas-station", "", "Gas Station"), F("birdcage", "", "Birdcage"),
        F("arches", "", "Arches"), F("red-bar", "", "Red Bar"), F("ponce-at-night", "", "Ponce at Night"), F("clermont", "", "Clermont")]),
    ("Atlanta Skyline, Dawn to Night", "The same city from above as the light changes through the day.", [
        F("golden-morning", "", "Golden Morning"), F("skyline-rays", "", "Sunrise Rays"), F("ember-sky", "", "Ember Sky"),
        F("blue-hour-skyline", "", "Blue Hour"), F("city-lights", "", "City Lights"), F("midnight", "", "Midnight")]),
    ("Light and Shadow", "Black-and-white street frames cut by hard light.", [
        P("Long Shadow"), F("sun-shield", "", "Sun Shield"), F("bench-in-the-light", "", "Bench in the Light"),
        F("under-the-bridge", "", "Under the Bridge"), F("tower", "", "Tower")]),
    ("Yellowstone", "Mineral colors, steam and big sky from July 2021.", [
        F("old-faithful", "", "Old Faithful"), F("grand-prismatic", "", "Grand Prismatic"), F("steaming-pool", "", "Steaming Pool"),
        F("morning-glory", "", "Morning Glory"), F("river-rapids", "", "River Rapids"), F("meadow-stream", "", "Meadow Stream")]),
    ("Gulf Coast on Film", "Soft pastel sand and sky from one roll of film. Prints up to 20 × 30 in.", [
        F("white-dunes", "", "White Dunes"), F("sea-oats", "", "Sea Oats"), F("film-palm", "", "Lone Palm"),
        F("marsh", "", "Marsh"), F("walker-on-the-shore", "", "Walker on the Shore")]),
]

# ---------- helpers ----------
e = html.escape


_SIZES = {}


def size_attrs(src):
    """width/height attributes, so the browser (and the gallery script) know each photo's shape."""
    if src not in _SIZES:
        from PIL import Image
        with Image.open(os.path.join(ROOT, "images", src)) as im:
            _SIZES[src] = im.size
    return ' width="%d" height="%d"' % _SIZES[src]


def img(photo, cls="", lazy=True, zoom=False):
    src, alt, title = photo
    c = (cls + (" zoom" if zoom else "")).strip()
    return '<img src="%simages/%s" alt="%s"%s%s%s%s>' % (
        UP, src, e(alt or title), size_attrs(src), ' class="%s"' % c if c else "", ' loading="lazy"' if lazy else "",
        ' data-title="%s"' % e(title) if zoom else "")


NAV = [("index.html", "Home"), ("portfolio.html", "Portfolio"), ("prints.html", "Prints"),
       ("about.html", "About"), ("contact.html", "Contact")]


def page(fname, title, body, desc, lightbox=False, extra_js=""):
    nav = "\n".join('    <a href="%s"%s>%s</a>' % (h, ' class="active" aria-current="page"' if h == fname else "", t)
                    for h, t in NAV)
    lb = """
<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Full screen photo">
  <button class="lb-close" aria-label="Close">&times;</button>
  <button class="lb-prev" aria-label="Previous photo">&#8249;</button>
  <img alt="">
  <p></p>
  <button class="lb-next" aria-label="Next photo">&#8250;</button>
</div>
<script src="site.js"></script>""" if lightbox else ""
    doc = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<link rel="stylesheet" href="site.css">
</head>
<body id="top">
<header class="site-header">
  <a class="logo" href="index.html">Blaine Wood Photo<span>People + Places + Things</span></a>
  <nav aria-label="Main">
%s
  </nav>
</header>
%s
<footer class="site-footer">
  <div class="socials">
    <a href="%s" target="_blank" rel="noopener" aria-label="Blaine on Instagram"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="%s"/></svg><span>Instagram</span></a>
    <a href="%s" target="_blank" rel="noopener" aria-label="Blaine on Foto"><svg viewBox="0 0 24 24" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M3 8a2 2 0 0 1 2-2h2.5l1.5-2h6l1.5 2H19a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><circle cx="12" cy="13" r="4"/></g></svg><span>Foto</span></a>
  </div>
  <p>&copy; %d Blaine Wood Photo &middot; Atlanta, GA &middot; <a href="mailto:%s">%s</a></p>
</footer>%s%s
</body>
</html>
""" % (e(title), e(desc), nav, body, INSTAGRAM, IG_PATH, FOTO, YEAR, EMAIL, EMAIL, lb, extra_js)
    with open(os.path.join(OUT, fname), "w") as fh:
        fh.write(doc)


def size_select(label):
    return '<select aria-label="%s">%s</select>' % (e(label), "".join("<option>%s</option>" % s for s in SIZES))


# ---------- Home ----------
def build_home():
    body = """<section class="hero" style="background-image:url('%simages/hero.jpg')">
  <div>
    <h1>Blaine Wood Photo</h1>
    <p>People, places and things around Atlanta and beyond.</p>
    <a class="btn btn-light" href="portfolio.html">See the work</a>
  </div>
</section>
<main>
  <section class="intro">
    <p>I'm Blaine Wood, an Atlanta photographer who shoots for the love of it. Most days that means street scenes, people, landscapes and whatever the light and shadows are doing. This is where I share my favorites and offer the opportunity to purchase my prints.</p>
  </section>
  <section class="split">
    <div>
      <h2>Portfolio</h2>
      <p>Three galleries of my favorite photos: people, places and things.</p>
      <a class="btn" href="portfolio.html">See the portfolio</a>
    </div>
    <div>
      <h2>Prints</h2>
      <p>Most of these photos are available as archival prints from 8 &times; 12 up to 24 &times; 36 inches, on their own or as a set of related images.</p>
      <a class="btn" href="prints.html">Browse prints and sets</a>
    </div>
    <div>
      <h2>Working together</h2>
      <p>Photography is a hobby for me, not a business I advertise. Still, if you have a portrait, event or project in mind, I'm always happy to hear about it.</p>
      <a class="btn btn-outline" href="contact.html">Get in touch</a>
    </div>
  </section>
</main>""" % UP
    page("index.html", "Blaine Wood Photo | Atlanta photography", body,
         "Street, places and portrait photography by Blaine Wood in Atlanta, GA, with fine art prints for sale.")


# ---------- Portfolio ----------
def build_portfolio():
    chips = "\n".join('    <a href="#%s" data-view="%s"%s>%s</a>' % (gid, gid, ' class="active"' if i == 0 else "", e(name))
                       for i, (gid, name, _, _) in enumerate(GALLERIES))
    secs = []
    for gid, name, blurb, photos in GALLERIES:
        figs = "\n".join("      <figure>%s</figure>" % img(p, zoom=True) for p in photos)
        secs.append("""  <section class="gallery tab-panel" id="%s" data-gallery>
    <h2>%s</h2>
    <p class="note">%s</p>
    <div class="masonry">
%s
    </div>
  </section>""" % (gid, e(name), e(blurb), figs))
    body = """<main>
  <h1 class="page-title">Portfolio</h1>
  <nav class="chips view-tabs" aria-label="Galleries">
%s
  </nav>
%s
  <p class="cta">Like something you see? <a href="prints.html">Most of these are available as prints.</a></p>
  <p class="to-top"><a class="btn btn-outline" href="#top">Back to top &uarr;</a></p>
</main>""" % (chips, "\n".join(secs))
    page("portfolio.html", "Portfolio | Blaine Wood Photo", body,
         "Galleries of street, signs and neon, places, silhouettes, faces and film photography by Blaine Wood.",
         lightbox=True)


# ---------- Prints ----------
def build_prints():
    sets = []
    for name, blurb, photos in SETS:
        n = len(photos)
        thumbs = "\n".join("        %s" % img(p, zoom=True) for p in photos)
        names = ", ".join(p[2] for p in photos)
        count = '<select aria-label="How many prints for %s"><option>All %d prints</option><option>Any 3 (tell me which)</option></select>' % (e(name), n)
        sets.append("""    <article class="set" data-gallery>
      <div class="set-strip" style="--n:%d">
%s
      </div>
      <div class="set-info">
        <h3>%s</h3>
        <p>%s</p>
        <p class="meta">%s</p>
        <div class="buy">%s %s <a class="btn" href="mailto:%s">Buy set</a></div>
      </div>
    </article>""" % (n, thumbs, e(name), e(blurb), e(names), count, size_select("Size for " + name), EMAIL))
    singles = []
    for f, alt, title in PRINTS:
        singles.append("""    <article class="print">
      %s
      <h3>%s</h3>
      <div class="buy">%s <a class="btn" href="mailto:%s">Buy</a></div>
    </article>""" % (img(("prints/" + f, alt, title), zoom=True), e(title), size_select("Size for " + title), EMAIL))
    body = """<main>
  <h1 class="page-title">Prints</h1>
  <p class="note">Every print is made to order on archival paper. Choose a size and click Buy to send me an order request, and I'll reply with the price and details. Prints ship in 5&ndash;7 days.</p>
  <nav class="chips view-tabs" aria-label="Print sections">
    <a href="#singles" data-view="singles" class="active" aria-current="true">Single prints</a>
    <a href="#sets" data-view="sets">Sets</a>
  </nav>
  <section id="sets" class="tab-panel">
    <h2>Sets</h2>
    <p class="note">Related photos made to hang together. Buy the whole set, or pick any three.</p>
%s
  </section>
  <section id="singles" class="tab-panel" data-gallery>
    <h2>Single prints</h2>
    <div class="grid">
%s
    </div>
  </section>
  <p class="to-top"><a class="btn btn-outline" href="#top">Back to top &uarr;</a></p>
</main>""" % ("\n".join(sets), "\n".join(singles))
    js = """
<script>
document.querySelectorAll('.set, .print').forEach(function (card) {
  var btn = card.querySelector('.btn');
  btn.addEventListener('click', function () {
    var title = card.querySelector('h3').textContent;
    var sel = card.querySelectorAll('select');
    var size = sel[sel.length - 1].value;
    var isSet = card.classList.contains('set');
    var what = isSet ? 'the "' + title + '" set (' + sel[0].value + ')' : 'a print of "' + title + '"';
    var body = 'Hi Blaine,\\n\\nI would like to order ' + what + ' in ' + size + '.\\n\\n';
    var subject = (isSet ? 'Set order: ' : 'Print order: ') + title + ' (' + size + ')';
    btn.href = 'mailto:%s?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
  });
});
</script>""" % EMAIL
    page("prints.html", "Prints | Blaine Wood Photo", body,
         "Fine art prints and print sets by Atlanta photographer Blaine Wood, from 8 x 12 to 24 x 36 inches.",
         lightbox=True, extra_js=js)


# ---------- About ----------
def build_about():
    body = """<main>
  <div class="about">
    <img src="%simages/portrait.jpg" alt="Black and white portrait of Blaine Wood">
    <div>
      <h1 class="page-title">About me</h1>
      <p>Hi, I'm Blaine Wood. Photography started as a hobby and turned into the way I notice the world. I capture the people, places, and things I come across: street scenes, portraits, the light around us, and the small details most people walk past.</p>
      <p>I'm based in Atlanta, GA, and I shoot images with a Leica M11. What draws me to a scene is light and shadow, people with a positive energy, and the gestures that make up candid moments.</p>
      <h2>Prints</h2>
      <p>Every print is made to order on archival paper so it will last for decades. <a href="prints.html">See what's available.</a></p>
      <h2>Working together</h2>
      <p>I'm a hobbyist, so I don't advertise sessions. But I do take on the occasional portrait, event or creative project when it's a good fit. If you have something in mind, tell me about it.</p>
      <p><a class="btn" href="contact.html">Get in touch</a></p>
    </div>
  </div>
</main>""" % UP
    page("about.html", "About | Blaine Wood Photo", body,
         "About Blaine Wood, a hobbyist photographer in Atlanta, GA shooting with a Leica M11.")


# ---------- Contact ----------
def build_contact():
    body = """<main class="narrow">
  <h1 class="page-title">Contact</h1>
  <p class="lead">The easiest way to reach me is email:</p>
  <p class="email"><a href="mailto:%s">%s</a></p>
  <div class="contact-cols">
    <div>
      <h2>Prints</h2>
      <p>Tell me which photo or set you'd like and the size. I'll reply with the price, paper options and shipping.</p>
      <a class="btn btn-outline" href="prints.html">Browse prints</a>
    </div>
    <div>
      <h2>Portraits, events and projects</h2>
      <p>I take on a small amount of work when the timing and the idea are right. Share the date, the place and what you have in mind, and I'll let you know if I can help.</p>
      <a class="btn" href="mailto:%s?subject=Photography%%20inquiry">Send an inquiry</a>
    </div>
  </div>
</main>""" % (EMAIL, EMAIL, EMAIL)
    page("contact.html", "Contact | Blaine Wood Photo", body,
         "Get in touch with Blaine Wood about prints, portraits, events or projects.")


os.makedirs(OUT, exist_ok=True)
import shutil
for asset in ("site.css", "site.js"):
    shutil.copy(os.path.join(ROOT, "tools", asset), os.path.join(OUT, asset))
build_home()
build_portfolio()
build_prints()
build_about()
build_contact()
print("wrote site to", OUT)
