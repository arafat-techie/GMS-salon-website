# LUMÉ Salon Website

Open `index.html` in a browser (or upload the folder to any static host).
Everything (HTML, CSS, JS) is in index.html. Pages are hash-routed (#/about, #/services, ...).

## Replace placeholder art with real photos
1. Put images in the `images/` folder (WebP recommended).
2. In index.html, find `const IMG={};` and add entries, e.g.
   IMG['G-0']='images/gallery-0.webp';   // gallery tile 0
   IMG['S-6']='images/bridal-makeup.webp'; // service 6
   Keys: G-n gallery, S-n service, T-n team, C-n client, O-n offer, B-n/A-n before/after, H/H1/H2 hero.

## Replace details
Search for: 12 Rose Court, +91 00000 00000, hello@lume.example, wa.me/910000000000.
Booking and contact forms only show on-screen confirmations; connect them to your backend or a form service.
