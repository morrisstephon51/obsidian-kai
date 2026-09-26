NAVY, ORANGE, CREAM = "#1F2A44", "#F26B3A", "#FFF4E6"
FONT = "'Arial Rounded MT Bold', 'Arial Rounded MT', Arial, sans-serif"

def svg(w, h, body, bg=None):
    rect = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{rect}{body}</svg>'

# ---- First logo: straight from the v1 brand brief (sun + rays + skyline + name) ----
rays = "".join(
    f'<rect x="494" y="170" width="12" height="70" rx="6" fill="{ORANGE}" transform="rotate({a} 500 430)"/>'
    for a in range(-90, 91, 30))
first = svg(1000, 1000, f'''
  {rays}
  <circle cx="500" cy="430" r="190" fill="{ORANGE}"/>
  <text x="500" y="480" text-anchor="middle" font-family="{FONT}" font-size="104" fill="{NAVY}" textLength="820" lengthAdjust="spacingAndGlyphs">MADISON GRIND</text>
  <path d="M170 700 h60 v-70 h50 v70 h40 v-120 h60 v120 h50 v-90 h45 v90 h60 v-150 h55 v150 h45 v-80 h50 v80 h60 v-110 h50 v110 h35" fill="none" stroke="{NAVY}" stroke-width="10" stroke-linejoin="round"/>
''', "#FFFFFF")

# ---- Final logo: lettering + one small half sun ----
def mark(text_fill, sun_fill):
    return f'''
  <path d="M440 330 A60 60 0 0 1 560 330 Z" fill="{sun_fill}"/>
  <text x="500" y="500" text-anchor="middle" font-family="{FONT}" font-size="150" fill="{text_fill}" textLength="760" lengthAdjust="spacingAndGlyphs">MADISON</text>
  <text x="500" y="670" text-anchor="middle" font-family="{FONT}" font-size="150" fill="{text_fill}" textLength="760" lengthAdjust="spacing">GRIND</text>
'''
final = svg(1000, 1000, mark(NAVY, ORANGE), "#FFFFFF")
dark  = svg(1000, 1000, mark(CREAM, ORANGE), NAVY)
icon  = svg(1000, 1000, f'''
  <text x="500" y="610" text-anchor="middle" font-family="{FONT}" font-size="400" fill="{CREAM}" letter-spacing="10">MG</text>
''', NAVY)
# transparent version for the mockup cup
final_clear = svg(1000, 1000, mark(NAVY, ORANGE))

for name, s in [("01-first-logo", first), ("02-final-logo", final), ("03-dark-version", dark),
                ("04-icon", icon), ("logo-clear", final_clear)]:
    open(f"src/{name}.svg", "w").write(s)
print("svgs written")
