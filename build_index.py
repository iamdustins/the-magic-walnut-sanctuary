# -*- coding: utf-8 -*-
import os

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>the magic walnut plant shoppe // home plant nursery</title>
  <meta name="description" content="rare and unique plants for regular people that think they are rare and unique. rooted cuttings and established plants grown by one guy in a home nursery.">
  <meta property="og:title" content="the magic walnut plant shoppe">
  <meta property="og:description" content="rare and unique plants for regular people that think they are rare and unique.">
  <meta property="og:type" content="website">
  <meta name="theme-color" content="#0b0c0f">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Courier+Prime:ital,wght@0,400;0,700;1,400&family=Special+Elite&family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="css/style.css">
</head>
<body id="top">

  <!-- Floating Mascot Background Layer (Softly visible through translucent sheet) -->
  <div class="floating-bg-logo-wrap" aria-hidden="true">
    <img src="assets/logos/logoRobotWatering.png" alt="" class="floating-bg-logo">
  </div>

  <!-- Interactive Flashlight Mouse Glow -->
  <div class="cursor-glow" aria-hidden="true"></div>

  <!-- Main Smoky Glass Container -->
  <div class="glass-viewport">
    <article class="typewriter-sheet">

      <!-- Hallmark Corner Tag -->
      <div class="hallmark-tag-corner" aria-hidden="true">the magic walnut plant shoppe &bull; est. 2024</div>

      <!-- Top Sheet Header & Date Bar -->
      <header class="sheet-header">
        <div class="header-left">
          <span class="stamp-tag">[ plant shoppe ]</span>
          <span id="live-date">NOVEMBER 2026</span>
          <span class="status-indicator">
            <span class="status-dot"></span>
            <span id="header-status-text">plants from my home nursery</span>
          </span>
        </div>
        <div class="header-right">
          <button id="open-admin-btn" class="btn-type text-xs" title="Open Plant Listing Assistant">
            [ listing studio ]
          </button>
          <button id="open-cart-btn" class="btn-type btn-crate" title="Open Crate">
            <span>[ crate:</span>
            <span id="cart-count-badge">0</span>
            <span>]</span>
          </button>
        </div>
      </header>

      <!-- Hero Section (Warm, Grounded, Authentic) -->
      <section class="hero-dispatch">
        <h1 class="typed-headline">the magic walnut plant shoppe</h1>
        <p class="typed-slug">
          "rare and unique plants for regular people that think they are rare and unique"
        </p>
        <p class="typed-intro-p">
          i'm just a guy growing plants in my home nursery. rooted cuttings, established plants in chunky aroid mix, and a few plant shirts. they're not all perfect—some might have a battle scar from real greenhouse life—but they have strong roots and honest genetics.
        </p>

        <!-- Balanced 3-Part Trust Pillars in Muted Grays -->
        <div class="trust-grid">
          <div class="trust-pill">
            <strong>[ 01: wysiwyg ]</strong>
            <p>exact plant pictured. what you see in the photo is the exact plant that ships to your door.</p>
          </div>
          <div class="trust-pill">
            <strong>[ 02: direct &amp; honest ]</strong>
            <p>direct checkout via paypal, venmo, cash app, zelle, or card with zero marketplace middleman fees.</p>
          </div>
          <div class="trust-pill">
            <strong>[ 03: safe packing ]</strong>
            <p>packed with thermal insulation and 72-hour heat packs whenever transit temps drop along the route.</p>
          </div>
        </div>

        <!-- Balanced 6-Section Quick Jump Navigation Grid -->
        <div class="hero-actions-grid">
          <a href="#shoppe" class="btn-type">[ plants for sale ]</a>
          <a href="#arcade" class="btn-type">[ little arcade ]</a>
          <a href="#streams" class="btn-type">[ where to find us ]</a>
          <a href="#merch" class="btn-type">[ plant shirts ]</a>
          <a href="#care" class="btn-type">[ albo care guide ]</a>
          <a href="#about" class="btn-type">[ about the shop ]</a>
        </div>
      </section>

      <hr class="type-divider">

      <!-- Section 01: Plants Available Right Now -->
      <section id="shoppe">
        <div class="section-header-row">
          <div>
            <span class="section-label">[ 01 ] plants available right now</span>
            <span class="section-subnote">rooted cuttings and established plants &bull; what you see is what you get</span>
          </div>
          <span class="stamp-tag" id="batch-title-tag">fresh drop</span>
        </div>

        <!-- Balanced Category Filter Bar with Past Sold Plants Archive Option -->
        <div class="filter-bar" id="category-filters">
          <button class="btn-type active" data-cat="ALL">[ all plants ]</button>
          <button class="btn-type" data-cat="Monstera">[ monstera ]</button>
          <button class="btn-type" data-cat="Philodendron">[ philodendron ]</button>
          <button class="btn-type" data-cat="Epipremnum">[ epipremnum ]</button>
          <button class="btn-type" data-cat="Anthurium">[ anthurium ]</button>
          <button class="btn-type" data-cat="Syngonium">[ syngonium ]</button>
          <button class="btn-type" data-cat="SOLD">[ past sold plants ]</button>
        </div>

        <!-- Dynamic 3-Column Specimen Grid -->
        <div class="specimen-grid" id="plants-grid">
          <!-- Rendered via JavaScript -->
        </div>
      </section>

      <hr class="type-divider">

      <!-- Section 02: The Plant Arcade & Mini-Games -->
      <section id="arcade">
        <div class="section-header-row">
          <div>
            <span class="section-label">[ 02 ] the plant arcade &amp; mini-games</span>
            <span class="section-subnote">little browser games you can play while hanging out or during live shows</span>
          </div>
          <span class="stamp-tag">[ mini-games ]</span>
        </div>

        <!-- Balanced 3-Cabinet Game Selector Tabs -->
        <div class="game-tabs-grid">
          <button id="tab-game-pull" class="btn-type active">[ mystery pull ]</button>
          <button id="tab-game-box" class="btn-type">[ 8-bit prize box ]</button>
          <button id="tab-game-darts" class="btn-type">[ pixel balloon darts ]</button>
        </div>

        <div class="arcade-cabinet-frame">
          <div class="arcade-screen-header">
            <span id="current-game-title">active game: the magic walnut plant mystery pull</span>
            <div class="arcade-screen-dots">
              <span class="dot-gray"></span>
              <span class="dot-gray"></span>
              <span class="dot-gray"></span>
            </div>
          </div>
          <div class="arcade-iframe-wrap">
            <iframe id="arcade-iframe" src="google-sites-embeds/mystery-pull-embed.html" title="Plant Arcade" loading="lazy"></iframe>
          </div>
          <div class="arcade-footer-bar">
            <span>&bull; free interactive plant game &bull; play anytime</span>
            <a id="arcade-fullscreen-link" href="google-sites-embeds/mystery-pull-embed.html" target="_blank" class="btn-type text-xs">[ open full screen &nearr; ]</a>
          </div>
        </div>
      </section>

      <hr class="type-divider">

      <!-- Section 03: Other Places to Find My Plants (Balanced 3x2 Grid) -->
      <section id="streams">
        <div class="section-header-row">
          <div>
            <span class="section-label">[ 03 ] other places to find my plants</span>
            <span class="section-subnote">catch weekly live sales, greenhouse stories, and plant auctions across the web</span>
          </div>
          <span class="stamp-tag">[ other platforms ]</span>
        </div>

        <div class="streams-grid">
          <a href="https://palmstreet.app/u/themagicwalnut?pr=gPBMNjrm" target="_blank" rel="noopener noreferrer" class="stream-pill featured">
            <span>[ palmstreet ] weekly live sales &amp; surprise claims (@themagicwalnut) &nearr;</span>
          </a>
          <a href="https://www.whatnot.com/s/CDDTW1SX" target="_blank" rel="noopener noreferrer" class="stream-pill featured">
            <span>[ whatnot ] live streams, flash auctions &amp; drops (@themagicwalnut) &nearr;</span>
          </a>
          <a href="https://www.facebook.com/groups/thehobbybotanist" target="_blank" rel="noopener noreferrer" class="stream-pill">
            <span>[ facebook ] the hobby botanist community &amp; greenhouse updates &nearr;</span>
          </a>
          <a href="https://www.etsy.com/shop/TheMagicWalnutCo" target="_blank" rel="noopener noreferrer" class="stream-pill">
            <span>[ etsy ] our official etsy plant storefront &nearr;</span>
          </a>
          <a href="https://www.ebay.com/usr/themagicwalnutplantshoppe" target="_blank" rel="noopener noreferrer" class="stream-pill">
            <span>[ ebay ] occasional specimen auctions &nearr;</span>
          </a>
          <a href="https://www.instagram.com/themagicwalnutplantshoppe" target="_blank" rel="noopener noreferrer" class="stream-pill">
            <span>[ instagram ] photos, new leaves &amp; greenhouse stories (@themagicwalnutplantshoppe) &nearr;</span>
          </a>
        </div>
      </section>

      <hr class="type-divider">

      <!-- Section 04: Plant T-Shirts & Gear -->
      <section id="merch">
        <div class="section-header-row">
          <div>
            <span class="section-label">[ 04 ] plant t-shirts &amp; gear</span>
            <span class="section-subnote">heavyweight tees, puppet sketches, and house-blended chunky aroid mix</span>
          </div>
          <span class="stamp-tag">[ plant gear ]</span>
        </div>

        <div class="specimen-grid" id="merch-grid">
          <!-- Rendered via JavaScript -->
        </div>
      </section>

      <hr class="type-divider">

      <!-- Section 05: Monstera Albo Care Guide (What Actually Works) (Balanced 6-Part Grid) -->
      <section id="care">
        <div class="section-header-row">
          <div>
            <span class="section-label">[ 05 ] monstera albo care guide (what actually works)</span>
            <span class="section-subnote">practical tips and common myths from growing variegated monsteras at home</span>
          </div>
          <span class="stamp-tag">[ care guide ]</span>
        </div>

        <div class="care-grid">
          <div class="care-card">
            <div class="care-step">01: light &amp; grow lights</div>
            <h4>bright indirect foot-candles</h4>
            <p>white sectors don't have chlorophyll and can't convert sunlight, so the green parts need good light to carry the whole leaf. give them bright indirect sun or a 24w led grow light about 12&ndash;18 inches away. low light causes the plant to drop its white sectors.</p>
          </div>
          <div class="care-card">
            <div class="care-step">02: watering &amp; moisture</div>
            <h4>never let roots sit in mud</h4>
            <p>water thoroughly until water runs freely out the drainage holes, then let the top 50&ndash;60% of the chunky mix dry out before watering again. soggy dense soil is the number one cause of root issues.</p>
          </div>
          <div class="care-card">
            <div class="care-step">03: house chunky soil mix</div>
            <h4>maximum root aeration</h4>
            <p>my home recipe: 40% coarse pine bark nuggets, 25% jumbo perlite (#3/#4), 20% coconut husk chunks, 10% worm castings, and 5% horticultural charcoal. chunky substrate lets roots breathe freely.</p>
          </div>
          <div class="care-card">
            <div class="care-step">04: white leaf browning</div>
            <h4>the real causes of browning</h4>
            <p>white browning is almost always caused by irregular moisture or stagnant air, not dry air alone. keep a gentle oscillating fan moving in the room. don't mist the white leaves directly with water droplets.</p>
          </div>
          <div class="care-card">
            <div class="care-step">05: arrival &amp; acclimation</div>
            <h4>give it a week to settle</h4>
            <p>when your plant arrives, don't rush to repot it right away. set it in medium-bright indirect light for 5&ndash;7 days to recover from transit. give it a gentle drink if the substrate feels dry to the touch.</p>
          </div>
          <div class="care-card">
            <div class="care-step">06: roots &amp; propagation</div>
            <h4>aerial roots are gold</h4>
            <p>always protect the aerial root on each node. root cuttings in damp stratum or coarse perlite with a little bottom heat until secondary feeder roots reach 2&ndash;3 inches before potting into chunky mix.</p>
          </div>
        </div>
      </section>

      <hr class="type-divider">

      <!-- Section 06: About The Shop & Why I'm Here -->
      <section id="about">
        <div class="section-header-row">
          <div>
            <span class="section-label">[ 06 ] about the shop &amp; why i'm here</span>
            <span class="section-subnote">just a guy growing plants in my home nursery</span>
          </div>
          <span class="stamp-tag">[ about ]</span>
        </div>

        <div class="about-grid">
          <div class="about-card">
            <span class="card-tag">[ how it started ]</span>
            <h3 class="about-heading">just a plant guy with a home nursery.</h3>
            <p class="about-p">
              The Magic Walnut Plant Shoppe started from a simple obsession: hunting down rare cuttings, getting them rooted in healthy chunky mix, and passing them along to other plant people who love them.
            </p>
            <p class="about-p">
              They aren't mass-produced tissue-culture plugs in sterile cages. Each one is cared for by hand. Sometimes a leaf has a minor cosmetic imperfection or a battle scar from growing in a real greenhouse, but it has strong, healthy roots and honest genetics.
            </p>
          </div>

          <div class="about-card">
            <span class="card-tag">[ grown &amp; packed by one guy ]</span>
            <h3 class="about-heading">packed with care, sent from my home to yours.</h3>
            <p class="about-p">
              When you buy a plant here, you're dealing directly with me. I'm the one who takes the photos, answers your messages, wraps the pots, packs the thermal boxes, and brings them to the post office.
            </p>
            <p class="about-p">
              I check the weather forecast along your entire shipping route before releasing a package. If a freeze is blowing through, I'll hold the box or add extra thermal insulation so your plant arrives healthy.
            </p>
          </div>
        </div>
      </section>

      <hr class="type-divider">

      <!-- Section 07: Shipping & How I Pack Your Plants (Balanced in 3s) -->
      <section id="shipping">
        <div class="section-header-row">
          <div>
            <span class="section-label">[ 07 ] shipping &amp; how i pack your plants</span>
            <span class="section-subnote">careful packing so your plant arrives safe and happy</span>
          </div>
          <span class="stamp-tag">[ shipping ]</span>
        </div>

        <div class="policy-grid">
          <div class="policy-card">
            <strong>[ 01 ] careful insulated packing</strong>
            <p>all plants are shipped via usps priority or ups 2-day. pots are secured, soil is taped down, foliage is cushioned in soft polyfill, and boxes are lined with thermal bubble insulation.</p>
          </div>
          <div class="policy-card">
            <strong>[ 02 ] 72-hour winter heat packs</strong>
            <p>when temperatures along your delivery route drop below 45&deg;f, a 72-hour uniheat pack is included to keep the box warm during its journey.</p>
          </div>
          <div class="policy-card">
            <strong>[ 03 ] live arrival guarantee</strong>
            <p>i want you to be happy with your plant. if an issue happens in transit, simply send me a photo within 24 hours of delivery and i will work with you to make it right.</p>
          </div>
        </div>
      </section>

      <hr class="type-divider">

      <!-- Section 08: Personal Projects (Clean, Understated Link) -->
      <section id="elsewhere">
        <div class="section-header-row">
          <div>
            <span class="section-label">[ 08 ] my other projects</span>
            <span class="section-subnote">personal links &amp; creative work</span>
          </div>
          <span class="stamp-tag">[ links ]</span>
        </div>

        <div class="personal-link-box">
          <div class="personal-link-left">
            <strong>iamdustin.com</strong>
            <p>my personal website &mdash; home for music projects like Time Fold Static, writings, and other creative work.</p>
          </div>
          <a href="https://iamdustin.com" target="_blank" rel="noopener noreferrer" class="btn-type">
            visit iamdustin.com &nearr;
          </a>
        </div>
      </section>

      <!-- Footer -->
      <footer class="sheet-footer">
        <p>&copy; <span id="footer-year">2026</span> the magic walnut plant shoppe &bull; all rights reserved.</p>
        <p class="footer-sub">
          just a guy selling plants from home &bull; dustin
        </p>
      </footer>

    </article>
  </div>

  <!-- Floating Scroll To Top Button (Arrow) -->
  <a href="#top" id="scroll-to-top" class="scroll-to-top-btn" title="Back to top">
    <span>&uarr; top</span>
  </a>

  <!-- ========================================================================
       MODAL 01: SPECIMEN INSPECTION MODAL
       ======================================================================== -->
  <div id="specimen-modal" class="modal-backdrop hidden" role="dialog" aria-modal="true">
    <div class="typewriter-modal-sheet">
      <div class="modal-header">
        <div>
          <span class="stamp-tag">[ plant details ]</span>
          <h2 id="modal-plant-name" class="modal-title">Specimen Name</h2>
          <span id="modal-plant-botanical" class="modal-sub">Botanical classification</span>
        </div>
        <button id="close-specimen-modal" class="btn-type">[ close &times; ]</button>
      </div>

      <div class="modal-body-grid">
        <div>
          <div class="modal-main-img-wrap">
            <img id="modal-main-img" src="" alt="Specimen inspection">
          </div>
          <div id="modal-thumbnails" class="modal-thumb-row"></div>
        </div>

        <div class="modal-details-col">
          <div class="dossier-spec-box">
            <div class="spec-row">
              <span class="spec-label">type:</span>
              <span id="modal-plant-type" class="spec-val">wysiwyg</span>
            </div>
            <div class="spec-row">
              <span class="spec-label">category:</span>
              <span id="modal-plant-category" class="spec-val">monstera</span>
            </div>
            <div class="spec-row">
              <span class="spec-label">pot size:</span>
              <span id="modal-plant-pot" class="spec-val">4" chunky mix</span>
            </div>
            <div class="spec-row">
              <span class="spec-label">root status:</span>
              <span id="modal-plant-roots" class="spec-val">established in mix</span>
            </div>
            <div class="spec-row">
              <span class="spec-label">lighting:</span>
              <span id="modal-plant-light" class="spec-val">bright indirect</span>
            </div>
          </div>

          <p id="modal-plant-desc" class="modal-desc-p"></p>

          <div class="modal-action-bar">
            <div>
              <span class="spec-label">price:</span>
              <span id="modal-plant-price" class="modal-price-val">$0</span>
            </div>
            <button id="modal-add-to-cart-btn" class="btn-type btn-crate">
              [ + add to crate ]
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ========================================================================
       MODAL 02: SHOPPING CRATE DRAWER (Direct Checkout & Contact Info)
       ======================================================================== -->
  <div id="cart-drawer-overlay" class="drawer-overlay hidden">
    <div id="cart-drawer" class="cart-drawer-panel">
      <div class="drawer-header">
        <div>
          <span class="stamp-tag">[ shopping crate ]</span>
          <h3 class="drawer-title">your selected plants</h3>
        </div>
        <button id="close-cart-btn" class="btn-type">[ close &times; ]</button>
      </div>

      <!-- Items List -->
      <div id="cart-items-list" class="cart-items-scroll">
        <!-- Rendered via JS -->
      </div>

      <!-- Order Summary & Direct Checkout -->
      <div class="drawer-footer">
        <!-- Shipping Method Selector -->
        <div class="checkout-row">
          <label for="shipping-method-select" class="spec-label">shipping method:</label>
          <select id="shipping-method-select" class="input-type">
            <option value="standard">USPS Priority / UPS 2-Day ($14.00)</option>
            <option value="express">Express Overnight Shipping ($24.00)</option>
            <option value="local">Local Pickup ($0.00)</option>
          </select>
        </div>

        <!-- Winter Heat Pack Add-On -->
        <div class="heat-pack-row">
          <label class="checkbox-label">
            <input type="checkbox" id="heat-pack-checkbox">
            <span>Add 72-Hour UniHeat Shipping Pack (+$6.00)</span>
          </label>
        </div>

        <div class="cart-totals-box">
          <div class="total-line">
            <span>Subtotal:</span>
            <span id="cart-subtotal-val">$0.00</span>
          </div>
          <div class="total-line">
            <span>Shipping:</span>
            <span id="cart-shipping-val">$14.00</span>
          </div>
          <div class="total-line total-grand">
            <span>Total:</span>
            <span id="cart-total-val">$14.00</span>
          </div>
        </div>

        <!-- Direct Customer Info Fields (With Required Phone & Email) -->
        <div class="customer-info-grid">
          <input type="text" id="cust-name" class="input-type" placeholder="your name *" required>
          <input type="email" id="cust-email" class="input-type" placeholder="your email (for tracking) *" required>
          <input type="tel" id="cust-phone" class="input-type field-full" placeholder="your phone number (for shipping weather updates / texts) *" required>
          <input type="text" id="cust-address" class="input-type field-full" placeholder="shipping address (street, city, state, zip)">
          <textarea id="cust-notes" class="input-type field-full" rows="2" placeholder="special notes or social handle (palmstreet / ig / facebook)..."></textarea>
        </div>
        <p style="font-size:0.72rem; color:var(--ink-slate); line-height:1.4; margin-top:-0.2rem;">
          * i ask for your phone and email so i can reach out directly if there are any weather delays, cold snaps, or questions about your plant before shipping.
        </p>

        <!-- Checkout Buttons -->
        <div class="checkout-actions">
          <button id="generate-order-btn" class="btn-type btn-crate w-full">
            [ reserve order &amp; see payment options &nearr; ]
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- ========================================================================
       MODAL 03: ORDER INVOICE & PAYMENT DISPATCH MODAL
       ======================================================================== -->
  <div id="order-invoice-modal" class="modal-backdrop hidden" role="dialog" aria-modal="true">
    <div class="typewriter-modal-sheet">
      <div class="modal-header">
        <div>
          <span class="stamp-tag">[ order reservation ]</span>
          <h2 class="modal-title">plant reservation complete</h2>
          <span id="invoice-order-id" class="modal-sub">MW-ORDER-XXXX</span>
        </div>
        <button id="close-invoice-modal" class="btn-type">[ close &times; ]</button>
      </div>

      <div class="invoice-body">
        <p class="mb-3" style="font-size:0.82rem; line-height:1.6; color:var(--ink-charcoal);">
          your plant has been reserved! because i sell directly with zero middleman fees, you can send payment through whichever platform is easiest for you below. once received, i will pack your plant with care and send tracking to your phone/email.
        </p>

        <div class="invoice-summary-box">
          <div class="spec-row">
            <span class="spec-label">total amount due:</span>
            <strong id="invoice-total-amount" class="text-lg" style="color:var(--ink-black);">$0.00</strong>
          </div>
          <div class="spec-row">
            <span class="spec-label">customer:</span>
            <span id="invoice-cust-name">-</span>
          </div>
          <div class="spec-row">
            <span class="spec-label">phone:</span>
            <span id="invoice-cust-phone">-</span>
          </div>
          <div class="spec-row">
            <span class="spec-label">ship to:</span>
            <span id="invoice-cust-address">-</span>
          </div>
        </div>

        <h4 class="mt-4 mb-2 spec-label" style="font-size:0.8rem;">[ direct payment options ]</h4>
        <div class="payment-links-grid">
          <a href="https://paypal.me/themagicwalnutplantshoppe" target="_blank" class="btn-type">
            paypal: @themagicwalnutplantshoppe &nearr;
          </a>
          <a href="https://cash.app/$dartsilver" target="_blank" class="btn-type">
            cash app: $dartsilver &nearr;
          </a>
          <div class="btn-type cursor-text">
            venmo: @themagicwalnutplantshoppe
          </div>
          <div class="btn-type cursor-text">
            zelle: themagicwalnutplantshoppe@gmail.com
          </div>
        </div>

        <div class="mt-4 pt-3 border-t border-dashed border-gray-400 flex flex-wrap gap-2 justify-between items-center">
          <button id="download-pirate-ship-btn" class="btn-type text-xs">
            [ download pirate ship csv ]
          </button>
          <span class="text-xs text-gray-500">order logged &bull; i will text/email you when packed</span>
        </div>
      </div>
    </div>
  </div>

  <!-- ========================================================================
       MODAL 04: PLANT LISTING ASSISTANT (EASY FACEBOOK-STYLE POSTING)
       ======================================================================== -->
  <div id="admin-studio-modal" class="modal-backdrop hidden" role="dialog" aria-modal="true">
    <div class="typewriter-modal-sheet">
      <div class="modal-header">
        <div>
          <span class="stamp-tag">[ plant listing assistant ]</span>
          <h2 class="modal-title">post a plant (just like posting to facebook)</h2>
          <span class="modal-sub">take or drop pictures, name it, set the price, and post immediately</span>
        </div>
        <button id="close-admin-studio" class="btn-type">[ close &times; ]</button>
      </div>

      <div class="studio-body">
        <div class="studio-form-grid">
          <div>
            <label class="spec-label">plant name:</label>
            <input type="text" id="new-plant-name" class="input-type" placeholder="e.g. Monstera Albo Top Cutting #4">
          </div>
          <div>
            <label class="spec-label">price ($):</label>
            <input type="number" id="new-plant-price" class="input-type" placeholder="95">
          </div>
          <div>
            <label class="spec-label">category:</label>
            <select id="new-plant-cat" class="input-type">
              <option value="Monstera">Monstera</option>
              <option value="Philodendron">Philodendron</option>
              <option value="Epipremnum">Epipremnum</option>
              <option value="Anthurium">Anthurium</option>
              <option value="Syngonium">Syngonium</option>
              <option value="Other">Other Aroid / Tropical</option>
            </select>
          </div>
          <div>
            <label class="spec-label">pot size / mix:</label>
            <input type="text" id="new-plant-pot" class="input-type" placeholder="e.g. 4 inch chunky mix">
          </div>
          <div class="col-span-full">
            <label class="spec-label">grower notes &amp; description:</label>
            <input type="text" id="new-plant-desc" class="input-type" placeholder="e.g. exact plant pictured. healthy new growth point and aerial root.">
          </div>
          <div class="col-span-full">
            <label class="spec-label">plant photos (select or drop 1 or more images):</label>
            <input type="file" id="new-plant-files" class="input-type" multiple accept="image/*">
          </div>
        </div>

        <div class="mt-4 flex flex-wrap gap-2 justify-between items-center">
          <button id="add-plant-submit-btn" class="btn-type btn-crate">
            [ + post plant to shoppe ]
          </button>
          <div class="flex gap-2">
            <button id="wipe-drop-btn" class="btn-type text-xs">
              [ clear all ]
            </button>
            <button id="restore-sample-drop-btn" class="btn-type text-xs">
              [ restore defaults ]
            </button>
            <button id="export-catalog-json-btn" class="btn-type text-xs">
              [ export catalog.json ]
            </button>
          </div>
        </div>

        <!-- Plant Management Table with Quick 'Mark as Sold' -->
        <hr class="type-divider" style="margin: 1.5rem 0;">
        <h3 class="spec-label mb-2">[ active plant list &bull; click to mark sold or delete ]</h3>
        <div id="admin-plants-list" style="max-height: 240px; overflow-y: auto; font-size: 0.76rem;">
          <!-- Rendered via JS -->
        </div>
      </div>
    </div>
  </div>

  <!-- Application Logic -->
  <script>
    // Spotlight cursor effect
    const glow = document.querySelector('.cursor-glow');
    window.addEventListener('mousemove', (e) => {
      glow.style.left = e.clientX + 'px';
      glow.style.top = e.clientY + 'px';
    });

    // Scroll to top button visibility
    const scrollBtn = document.getElementById('scroll-to-top');
    window.addEventListener('scroll', () => {
      if (window.scrollY > 400) {
        scrollBtn.classList.add('visible');
      } else {
        scrollBtn.classList.remove('visible');
      }
    });

    // Default Fallback Catalog Data
    const defaultCatalog = {
      plants: [
        {
          id: 'mw-albo-01',
          name: 'Monstera Deliciosa Albo Variegata',
          botanical: 'Monstera deliciosa var. borsigiana albo-variegata',
          price: 185,
          type: 'WYSIWYG',
          category: 'Monstera',
          status: 'available',
          stock: 1,
          potSize: '4" chunky mix',
          rootStatus: 'established in chunky mix',
          light: 'bright indirect',
          badge: '1-of-1 plant',
          description: 'Authentic sectorial white marble variegation with high chlorophyll balance. Active aerial root tucked into our house chunky bark mix.',
          images: [
            'assets/logos/2.jpg',
            'assets/logos/3.jpg'
          ]
        },
        {
          id: 'mw-albo-02',
          name: 'Monstera Albo Half-Moon Specimen',
          botanical: 'Monstera deliciosa albo-variegata',
          price: 240,
          type: 'WYSIWYG',
          category: 'Monstera',
          status: 'available',
          stock: 1,
          potSize: '5" terracotta',
          rootStatus: 'heavy secondary feeder roots',
          light: 'bright filtered',
          badge: 'half-moon genetics',
          description: 'Crisp 50/50 split leaf with pure white sectoring on both stem and petiole. Hardened off in ambient home nursery conditions.',
          images: [
            'assets/logos/3.jpg',
            'assets/logos/2.jpg'
          ]
        },
        {
          id: 'mw-philo-01',
          name: 'Philodendron White Princess (Tricolor)',
          botanical: 'Philodendron erubescens cv. White Princess',
          price: 68,
          type: 'WYSIWYG',
          category: 'Philodendron',
          status: 'available',
          stock: 1,
          potSize: '4" nursery pot',
          rootStatus: 'established in chunky mix',
          light: 'medium to bright indirect',
          badge: 'tricolor blush',
          description: 'White splashed foliage with emerging pink blush nodes on the sheath. Ready for a cedar plank or moss pole.',
          images: [
            'assets/logos/4.jpg',
            'assets/logos/6.jpg'
          ]
        },
        {
          id: 'mw-epi-01',
          name: 'Epipremnum Pinnatum Albo Variegata',
          botanical: 'Epipremnum pinnatum albo',
          price: 52,
          type: 'WYSIWYG',
          category: 'Epipremnum',
          status: 'available',
          stock: 1,
          potSize: '4" chunky mix',
          rootStatus: 'vigorous aerial climber',
          light: 'bright indirect',
          badge: 'climbing cutting',
          description: 'Deep fenestrations already forming on juvenile leaves. Crisp snow-white streaks across emerald green tissue.',
          images: [
            'assets/logos/6.jpg',
            'assets/logos/4.jpg'
          ]
        },
        {
          id: 'mw-anth-01',
          name: 'Anthurium Crystallinum x Clarinervium',
          botanical: 'Anthurium hybrid',
          price: 95,
          type: 'WYSIWYG',
          category: 'Anthurium',
          status: 'available',
          stock: 1,
          potSize: '4" net pot in moss/bark',
          rootStatus: 'thick white feeder roots',
          light: 'indirect / shaded humid',
          badge: 'velvet veins',
          description: 'Deep shimmering velvet cardboard-textured leaves with electric silver veining. Potted in coarse moss and perlite.',
          images: [
            'assets/logos/2.jpg',
            'assets/logos/4.jpg'
          ]
        },
        {
          id: 'mw-syng-01',
          name: 'Syngonium Podophyllum Albo Variegatum',
          botanical: 'Syngonium podophyllum albo',
          price: 38,
          type: 'WYSIWYG',
          category: 'Syngonium',
          status: 'available',
          stock: 1,
          potSize: '3.5" pot',
          rootStatus: 'fast-growing root system',
          light: 'bright indirect',
          badge: 'high variegation',
          description: 'Panda-style high contrast white patches. Hardy grower and forgiving for first-time variegated collectors.',
          images: [
            'assets/logos/3.jpg',
            'assets/logos/6.jpg'
          ]
        }
      ],
      merch: [
        {
          id: 'mw-merch-01',
          name: 'Plant Puppet Master Heavyweight Tee',
          type: 'plant shirts',
          price: 36,
          badge: 'limited tee',
          image: 'assets/logos/1.2.jpg',
          description: 'Vintage-washed 6.5oz heavy cotton with front pocket mechanical plant puppet sketch & back typewriter quote.'
        },
        {
          id: 'mw-merch-02',
          name: 'Skeleton Botanist & Robot Tee',
          type: 'plant shirts',
          price: 36,
          badge: 'shop favorite',
          image: 'assets/logos/1.jpg',
          description: 'Signature dripping woodcut style emblem on comfortable charcoal combed ring-spun cotton.'
        },
        {
          id: 'mw-merch-03',
          name: 'House Chunky Aroid Mix (2-Gallon Bag)',
          type: 'grower soil',
          price: 22,
          badge: 'house recipe',
          image: 'assets/logos/1.1.png',
          description: 'Coarse pine bark nuggets, horticultural charcoal, jumbo perlite #4, coconut husk chunks, and worm castings.'
        }
      ]
    };

    let catalog = null;
    let cart = [];
    let currentFilter = 'ALL';

    // Initialize application
    async function initApp() {
      // Date stamps
      const now = new Date();
      const dateStr = now.toLocaleDateString('en-US', { month: 'long', year: 'numeric' }).toLowerCase();
      document.getElementById('live-date').textContent = dateStr;
      document.getElementById('footer-year').textContent = now.getFullYear();

      // Load Catalog from JSON or LocalStorage
      const saved = localStorage.getItem('mw_sanctuary_catalog');
      if (saved) {
        try { catalog = JSON.parse(saved); } catch (e) { catalog = defaultCatalog; }
      } else {
        try {
          const res = await fetch('catalog.json');
          if (res.ok) {
            catalog = await res.json();
          } else {
            catalog = defaultCatalog;
          }
        } catch (e) {
          catalog = defaultCatalog;
        }
      }

      // Load Saved Cart
      const savedCart = localStorage.getItem('mw_sanctuary_cart');
      if (savedCart) {
        try { cart = JSON.parse(savedCart); } catch (e) { cart = []; }
      }

      renderShoppe();
      renderMerch();
      renderCart();
      renderAdminList();
      bindEvents();
    }

    function saveCatalog() {
      localStorage.setItem('mw_sanctuary_catalog', JSON.stringify(catalog));
      renderShoppe();
      renderAdminList();
    }

    function saveCart() {
      localStorage.setItem('mw_sanctuary_cart', JSON.stringify(cart));
      renderCart();
    }

    // Render Specimen Grid (Symmetrical 3 Columns)
    function renderShoppe() {
      if (!catalog || !catalog.plants) return;
      const grid = document.getElementById('plants-grid');
      
      let filtered = [];
      if (currentFilter === 'ALL') {
        // Show available first, then sold
        filtered = [...catalog.plants].sort((a, b) => {
          const aSold = (a.status === 'sold' || a.stock <= 0) ? 1 : 0;
          const bSold = (b.status === 'sold' || b.stock <= 0) ? 1 : 0;
          return aSold - bSold;
        });
      } else if (currentFilter === 'SOLD') {
        filtered = catalog.plants.filter(p => p.status === 'sold' || p.stock <= 0);
      } else {
        filtered = catalog.plants.filter(p => p.category === currentFilter);
      }

      if (filtered.length === 0) {
        grid.innerHTML = `
          <div style="grid-column: 1 / -1; text-align:center; padding: 3rem 1rem; border: 1px dashed var(--paper-border);">
            <p class="stamp-tag">[ ${currentFilter === 'SOLD' ? 'sold archive empty' : 'no plants listed in this category right now'} ]</p>
            <p class="text-xs" style="color:var(--ink-faded); margin-top:0.5rem;">
              cuttings are actively rooting in the home nursery. check back soon or during live sales.
            </p>
          </div>
        `;
        return;
      }

      grid.innerHTML = filtered.map(plant => {
        const isSold = plant.status === 'sold' || plant.stock <= 0;
        const mainImg = (plant.images && plant.images[0]) ? plant.images[0] : 'assets/logos/2.jpg';

        return `
          <article class="specimen-card ${isSold ? 'sold' : ''}">
            <div>
              <div class="specimen-img-wrap" onclick="openSpecimenModal('${plant.id}')">
                <img src="${mainImg}" alt="${plant.name}" class="specimen-img" loading="lazy">
                <span class="specimen-badge ${isSold ? 'sold-badge' : ''}">${isSold ? '[ sold ]' : (plant.badge || 'wysiwyg')}</span>
              </div>

              <div class="specimen-meta-row">
                <span>${plant.category.toLowerCase()}</span>
                <span>${(plant.potSize || '4" chunky mix').toLowerCase()}</span>
              </div>

              <h3 class="specimen-title" onclick="openSpecimenModal('${plant.id}')">
                ${plant.name}
              </h3>

              <div class="specimen-botanical">${plant.botanical || ''}</div>
              <p class="specimen-desc">${plant.description}</p>
            </div>

            <div class="specimen-footer">
              <div class="specimen-price">$${plant.price}.00</div>
              <div class="specimen-card-btns">
                <button onclick="openSpecimenModal('${plant.id}')" class="btn-type text-xs">
                  inspect
                </button>
                <button ${isSold ? 'disabled' : ''} onclick="addToCart('${plant.id}', 'plant')" class="btn-type btn-crate">
                  ${isSold ? 'sold' : '+ crate'}
                </button>
              </div>
            </div>
          </article>
        `;
      }).join('');
    }

    // Render Merch Grid
    function renderMerch() {
      if (!catalog || !catalog.merch) return;
      const grid = document.getElementById('merch-grid');
      grid.innerHTML = catalog.merch.map(item => `
        <article class="specimen-card">
          <div>
            <div class="specimen-img-wrap">
              <img src="${item.image}" alt="${item.name}" class="specimen-img" loading="lazy">
              <span class="specimen-badge">${item.badge}</span>
            </div>

            <div class="specimen-meta-row">
              <span>${item.type}</span>
              <span>home nursery</span>
            </div>

            <h3 class="specimen-title">${item.name}</h3>
            <p class="specimen-desc">${item.description}</p>
          </div>

          <div class="specimen-footer">
            <div class="specimen-price">$${item.price}.00</div>
            <button onclick="addToCart('${item.id}', 'merch')" class="btn-type btn-crate">
              + crate
            </button>
          </div>
        </article>
      `).join('');
    }

    // Add Item to Crate
    window.addToCart = function(id, type) {
      let item = null;
      if (type === 'plant') {
        item = catalog.plants.find(p => p.id === id);
      } else {
        item = catalog.merch.find(m => m.id === id);
      }
      if (!item) return;

      cart.push({
        id: item.id,
        name: item.name,
        price: item.price,
        type: type,
        image: (item.images && item.images[0]) ? item.images[0] : item.image || 'assets/logos/2.jpg'
      });

      saveCart();
      openCartDrawer();
    };

    window.removeFromCart = function(idx) {
      cart.splice(idx, 1);
      saveCart();
    };

    // Render Crate Items & Calculate Totals
    function renderCart() {
      const countBadge = document.getElementById('cart-count-badge');
      if (countBadge) countBadge.textContent = cart.length;

      const list = document.getElementById('cart-items-list');
      if (!list) return;

      if (cart.length === 0) {
        list.innerHTML = `
          <div style="text-align:center; padding:3rem 1rem; color:var(--ink-dim); font-size:0.85rem;">
            [ your crate is empty ]
          </div>
        `;
      } else {
        list.innerHTML = cart.map((item, idx) => `
          <div class="cart-item-row">
            <div class="cart-item-left">
              <img src="${item.image}" alt="" class="cart-thumb">
              <div>
                <strong class="cart-item-name">${item.name}</strong>
                <span class="cart-item-type">${item.type}</span>
              </div>
            </div>
            <div class="cart-item-right">
              <span class="cart-item-price">$${item.price}.00</span>
              <button onclick="removeFromCart(${idx})" class="cart-del-btn" title="Remove">&times;</button>
            </div>
          </div>
        `).join('');
      }

      calculateCartTotals();
    }

    function calculateCartTotals() {
      const subtotal = cart.reduce((sum, item) => sum + Number(item.price), 0);
      const shippingSelect = document.getElementById('shipping-method-select');
      const heatPackCheck = document.getElementById('heat-pack-checkbox');

      let shippingCost = 14;
      if (shippingSelect) {
        if (shippingSelect.value === 'express') shippingCost = 24;
        else if (shippingSelect.value === 'local') shippingCost = 0;
      }

      let heatPackCost = (heatPackCheck && heatPackCheck.checked) ? 6 : 0;
      const total = subtotal + shippingCost + heatPackCost;

      const subtotalEl = document.getElementById('cart-subtotal-val');
      const shippingEl = document.getElementById('cart-shipping-val');
      const totalEl = document.getElementById('cart-total-val');

      if (subtotalEl) subtotalEl.textContent = `$${subtotal.toFixed(2)}`;
      if (shippingEl) shippingEl.textContent = `$${(shippingCost + heatPackCost).toFixed(2)}`;
      if (totalEl) totalEl.textContent = `$${total.toFixed(2)}`;
    }

    // Specimen Modal
    window.openSpecimenModal = function(id) {
      const plant = catalog.plants.find(p => p.id === id);
      if (!plant) return;

      document.getElementById('modal-plant-name').textContent = plant.name;
      document.getElementById('modal-plant-botanical').textContent = plant.botanical || '';
      document.getElementById('modal-plant-category').textContent = plant.category.toLowerCase();
      document.getElementById('modal-plant-pot').textContent = (plant.potSize || '4" chunky mix').toLowerCase();
      document.getElementById('modal-plant-roots').textContent = (plant.rootStatus || 'established in mix').toLowerCase();
      document.getElementById('modal-plant-light').textContent = (plant.light || 'bright indirect').toLowerCase();
      document.getElementById('modal-plant-desc').textContent = plant.description;
      document.getElementById('modal-plant-price').textContent = `$${plant.price}.00`;

      const mainImg = (plant.images && plant.images[0]) ? plant.images[0] : 'assets/logos/2.jpg';
      const mainImgEl = document.getElementById('modal-main-img');
      mainImgEl.src = mainImg;

      const thumbsEl = document.getElementById('modal-thumbnails');
      thumbsEl.innerHTML = (plant.images || [mainImg]).map(img => `
        <img src="${img}" class="modal-thumb ${img === mainImg ? 'active' : ''}" onclick="document.getElementById('modal-main-img').src='${img}'">
      `).join('');

      const addBtn = document.getElementById('modal-add-to-cart-btn');
      const isSold = plant.status === 'sold' || plant.stock <= 0;
      addBtn.disabled = isSold;
      addBtn.textContent = isSold ? '[ sold ]' : '[ + add to crate ]';
      addBtn.onclick = () => {
        if (!isSold) {
          addToCart(plant.id, 'plant');
          closeSpecimenModal();
        }
      };

      document.getElementById('specimen-modal').classList.remove('hidden');
    };

    function closeSpecimenModal() {
      document.getElementById('specimen-modal').classList.add('hidden');
    }

    function openCartDrawer() {
      document.getElementById('cart-drawer-overlay').classList.remove('hidden');
    }

    function closeCartDrawer() {
      document.getElementById('cart-drawer-overlay').classList.add('hidden');
    }

    // Render Admin Quick Management List (Mark as Sold / Delete)
    function renderAdminList() {
      const container = document.getElementById('admin-plants-list');
      if (!container || !catalog || !catalog.plants) return;

      container.innerHTML = catalog.plants.map(p => {
        const isSold = p.status === 'sold' || p.stock <= 0;
        return `
          <div style="display:flex; justify-content:space-between; align-items:center; padding:0.4rem 0; border-bottom:1px dotted var(--paper-border);">
            <div>
              <strong>${p.name}</strong> - $${p.price} (${p.category})
              ${isSold ? '<span style="color:var(--ink-slate); font-weight:bold;"> [SOLD]</span>' : ''}
            </div>
            <div style="display:flex; gap:0.35rem;">
              <button onclick="toggleSoldPlant('${p.id}')" class="btn-type text-xs" style="padding:0.2rem 0.45rem;">
                ${isSold ? 'mark available' : 'mark sold'}
              </button>
              <button onclick="deletePlant('${p.id}')" class="btn-type text-xs" style="padding:0.2rem 0.45rem;">
                delete
              </button>
            </div>
          </div>
        `;
      }).join('');
    }

    window.toggleSoldPlant = function(id) {
      const plant = catalog.plants.find(p => p.id === id);
      if (!plant) return;
      if (plant.status === 'sold') {
        plant.status = 'available';
        plant.stock = 1;
      } else {
        plant.status = 'sold';
        plant.stock = 0;
      }
      saveCatalog();
    };

    window.deletePlant = function(id) {
      if (confirm('Delete this plant from the listings?')) {
        catalog.plants = catalog.plants.filter(p => p.id !== id);
        saveCatalog();
      }
    };

    // Bind All User Events
    function bindEvents() {
      // Cart drawer buttons
      document.getElementById('open-cart-btn').onclick = openCartDrawer;
      document.getElementById('close-cart-btn').onclick = closeCartDrawer;
      document.getElementById('close-specimen-modal').onclick = closeSpecimenModal;

      // Close modal on background click
      document.getElementById('cart-drawer-overlay').onclick = (e) => {
        if (e.target.id === 'cart-drawer-overlay') closeCartDrawer();
      };
      document.getElementById('specimen-modal').onclick = (e) => {
        if (e.target.id === 'specimen-modal') closeSpecimenModal();
      };
      document.getElementById('order-invoice-modal').onclick = (e) => {
        if (e.target.id === 'order-invoice-modal') document.getElementById('order-invoice-modal').classList.add('hidden');
      };
      document.getElementById('close-invoice-modal').onclick = () => {
        document.getElementById('order-invoice-modal').classList.add('hidden');
      };

      // Filter category pills
      const filterBtns = document.querySelectorAll('#category-filters button');
      filterBtns.forEach(btn => {
        btn.onclick = () => {
          filterBtns.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          currentFilter = btn.dataset.cat;
          renderShoppe();
        };
      });

      // Shipping & Heat Pack recalculation
      document.getElementById('shipping-method-select').onchange = calculateCartTotals;
      document.getElementById('heat-pack-checkbox').onchange = calculateCartTotals;

      // Arcade Cabinet Tab Switching
      const tabPull = document.getElementById('tab-game-pull');
      const tabBox = document.getElementById('tab-game-box');
      const tabDarts = document.getElementById('tab-game-darts');
      const iframe = document.getElementById('arcade-iframe');
      const gameTitle = document.getElementById('current-game-title');
      const fullLink = document.getElementById('arcade-fullscreen-link');

      tabPull.onclick = () => {
        iframe.src = 'google-sites-embeds/mystery-pull-embed.html';
        gameTitle.textContent = 'active game: the magic walnut plant mystery pull';
        fullLink.href = 'google-sites-embeds/mystery-pull-embed.html';
        tabPull.classList.add('active');
        tabBox.classList.remove('active');
        tabDarts.classList.remove('active');
      };

      tabBox.onclick = () => {
        iframe.src = 'google-sites-embeds/plant-box-8bit-embed.html';
        gameTitle.textContent = 'active game: 8-bit plant mystery prize box';
        fullLink.href = 'google-sites-embeds/plant-box-8bit-embed.html';
        tabBox.classList.add('active');
        tabPull.classList.remove('active');
        tabDarts.classList.remove('active');
      };

      tabDarts.onclick = () => {
        iframe.src = 'google-sites-embeds/pixel-carnival-darts-embed.html';
        gameTitle.textContent = 'active game: pixel carnival balloon darts';
        fullLink.href = 'google-sites-embeds/pixel-carnival-darts-embed.html';
        tabDarts.classList.add('active');
        tabPull.classList.remove('active');
        tabBox.classList.remove('active');
      };

      // Complete Direct Checkout
      document.getElementById('generate-order-btn').onclick = () => {
        if (cart.length === 0) {
          alert('your crate is empty. please select a plant first.');
          return;
        }

        const name = document.getElementById('cust-name').value.trim();
        const email = document.getElementById('cust-email').value.trim();
        const phone = document.getElementById('cust-phone').value.trim();
        const address = document.getElementById('cust-address').value.trim() || 'local pickup';
        const notes = document.getElementById('cust-notes').value.trim();

        if (!name || !email || !phone) {
          alert('please enter your name, email, and phone number so i can contact you about shipping and weather updates.');
          return;
        }

        const orderId = 'MW-' + Math.floor(100000 + Math.random() * 900000);
        const total = document.getElementById('cart-total-val').textContent;

        document.getElementById('invoice-order-id').textContent = orderId;
        document.getElementById('invoice-total-amount').textContent = total;
        document.getElementById('invoice-cust-name').textContent = name + ' (' + email + ')';
        document.getElementById('invoice-cust-phone').textContent = phone;
        document.getElementById('invoice-cust-address').textContent = address;

        closeCartDrawer();
        document.getElementById('order-invoice-modal').classList.remove('hidden');

        // Store order details for Pirate Ship CSV
        window.lastOrder = { orderId, name, email, phone, address, notes, total, items: [...cart] };
      };

      // Pirate Ship CSV Export
      document.getElementById('download-pirate-ship-btn').onclick = () => {
        if (!window.lastOrder) return;
        const o = window.lastOrder;
        const csv = `Order Number,Recipient Name,Address,Email,Phone,Note\\n"${o.orderId}","${o.name}","${o.address}","${o.email}","${o.phone}","${o.items.map(i=>i.name).join('; ')} - ${o.notes}"`;
        const blob = new Blob([csv], { type: 'text/csv' });
        const a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = `pirateship_${o.orderId}.csv`;
        a.click();
      };

      // Plant Listing Assistant Modal
      const studioModal = document.getElementById('admin-studio-modal');
      document.getElementById('open-admin-btn').onclick = () => {
        studioModal.classList.remove('hidden');
        renderAdminList();
      };
      document.getElementById('close-admin-studio').onclick = () => {
        studioModal.classList.add('hidden');
      };

      // Easy Plant Posting (Like Facebook Post)
      document.getElementById('add-plant-submit-btn').onclick = async () => {
        const name = document.getElementById('new-plant-name').value.trim();
        const price = Number(document.getElementById('new-plant-price').value || 50);
        const category = document.getElementById('new-plant-cat').value;
        const potSize = document.getElementById('new-plant-pot').value.trim() || '4" chunky mix';
        const description = document.getElementById('new-plant-desc').value.trim() || 'exact plant pictured.';
        const files = document.getElementById('new-plant-files').files;

        if (!name) {
          alert('please enter a plant name.');
          return;
        }

        const images = [];
        for (const file of files) {
          const dataUrl = await new Promise(res => {
            const r = new FileReader();
            r.onload = (e) => res(e.target.result);
            r.readAsDataURL(file);
          });
          images.push(dataUrl);
        }
        if (images.length === 0) images.push('assets/logos/2.jpg');

        catalog.plants.unshift({
          id: 'mw-' + Date.now(),
          name,
          botanical: category + ' cultivar',
          price,
          type: 'WYSIWYG',
          category,
          status: 'available',
          stock: 1,
          potSize,
          rootStatus: 'established in chunky mix',
          light: 'bright indirect',
          badge: '1-of-1 plant',
          description,
          images
        });

        document.getElementById('new-plant-name').value = '';
        document.getElementById('new-plant-price').value = '';
        document.getElementById('new-plant-desc').value = '';
        document.getElementById('new-plant-files').value = '';
        saveCatalog();
        alert(`posted "${name}" to the live shoppe!`);
      };

      document.getElementById('wipe-drop-btn').onclick = () => {
        if (confirm('clear all plants from the active list?')) {
          catalog.plants = [];
          saveCatalog();
        }
      };

      document.getElementById('restore-sample-drop-btn').onclick = () => {
        catalog = JSON.parse(JSON.stringify(defaultCatalog));
        saveCatalog();
      };

      document.getElementById('export-catalog-json-btn').onclick = () => {
        const blob = new Blob([JSON.stringify(catalog, null, 2)], { type: 'application/json' });
        const a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = 'catalog.json';
        a.click();
      };
    }

    initApp();
  </script>
</body>
</html>
'''

target_path = r'H:\The Magic Walnut Plants Sales\website\index.html'
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Successfully written index.html with refined human, approachable typewriter aesthetic.")
