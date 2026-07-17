#!/usr/bin/env python3
"""
Tax Playbook Screenplay Generator
Generates 12 standalone HTML screenplays teaching US Tax Code strategies
through dramatic storytelling (audits, heists, courtroom scenes).
Requires: Python 3.10+, Pillow (pip install Pillow)
"""

import os
import math
import random
import base64
from io import BytesIO

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Pillow not installed. Installing...")
    os.system("pip install Pillow")
    from PIL import Image, ImageDraw, ImageFont

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = SCRIPT_DIR

# ─── Color Palettes (light, warm tones) ──────────────────────────────────────

PALETTES = [
    {"accent": "#2E86AB", "accent_rgb": "46,134,171", "name": "Ocean Blue"},
    {"accent": "#A23B72", "accent_rgb": "162,59,114", "name": "Berry"},
    {"accent": "#F18F01", "accent_rgb": "241,143,1", "name": "Amber"},
    {"accent": "#C73E1D", "accent_rgb": "199,62,29", "name": "Terracotta"},
    {"accent": "#3B8132", "accent_rgb": "59,129,50", "name": "Forest"},
    {"accent": "#6B4C9A", "accent_rgb": "107,76,154", "name": "Plum"},
    {"accent": "#D4A03C", "accent_rgb": "212,160,60", "name": "Gold"},
    {"accent": "#1B998B", "accent_rgb": "27,153,139", "name": "Teal"},
    {"accent": "#E84855", "accent_rgb": "232,72,85", "name": "Coral"},
    {"accent": "#5B7DB1", "accent_rgb": "91,125,177", "name": "Slate Blue"},
    {"accent": "#8B5E3C", "accent_rgb": "139,94,60", "name": "Warm Brown"},
    {"accent": "#7B2D8B", "accent_rgb": "123,45,139", "name": "Violet"},
]

# ─── Screenplay Data ─────────────────────────────────────────────────────────

SCREENPLAYS = {}

# ═══════════════════════════════════════════════════════════════════════════════
# SCREENPLAY 1: Section 1031 Like-Kind Exchange
# ═══════════════════════════════════════════════════════════════════════════════

SCREENPLAYS["1031 Like-Kind Exchange"] = {
    "title": "The 1031 Exchange: The Real Estate Shuffle",
    "tax_section": "IRC Section 1031",
    "subtitle": "A Tax Playbook Screenplay",
    "genre": "The Loophole (Heist/Caper)",
    "filename": "screenplay_1031_exchange.html",
    "summary": "A slick CPA explains how to defer capital gains taxes indefinitely by swapping investment properties — turning one duplex into a portfolio without ever writing the IRS a check.",
    "diagram": """
  PROPERTY A              QUALIFIED              PROPERTY B
  (Sell)                INTERMEDIARY              (Buy)
 ─────────────         ═══════════════         ─────────────
 Duplex worth    ──╲                      ╱──  Fourplex worth
 $400K (basis     ───╲  ┌─────────────┐ ╱───  $500K+
 $200K = $200K    ────╳──│ 1031 EXCHANGE │──╳──  (boot = taxable)
 gain deferred)   ───╱  └─────────────┘ ╲───
                 ╱                        ╲
  REQUIREMENTS:        45-DAY / 180-DAY        RESULT:
 ─────────────         DEADLINES              ─────────────
 • Like-kind                                  • $0 tax now
 • Investment/biz      Must identify in       • Basis carries
 • Equal or greater    45 days, close in      • Defer forever
   value               180 days               • Step-up at death

 ────────────────────────────────────────────────
 THE MATH:
 $200K gain × 23.8% (cap gains + NIIT) = $47,600 saved
 Reinvest that $47,600 → compounds tax-free
 Die with property → heirs get stepped-up basis → tax = $0
""",
    "pages": [
        {
            "heading": "PAGE 1 — INT. UPSCALE CPA OFFICE — DAY",
            "content": """FADE IN:

A modern CPA office. Floor-to-ceiling windows. VICTOR CHEN (40s, fitted vest, pocket square, speaks like he's letting you in on a secret) sits across from MARIA DELGADO (50s, successful landlord, skeptical arms crossed).

VICTOR
Maria, you've owned that duplex for twelve years. Bought it at 200K, it's worth 400K now. You want to sell and upgrade to a fourplex. Correct?

MARIA
Correct. My accountant says I'll owe about 47 thousand in capital gains tax on the sale.

VICTOR
(leaning forward)
What if I told you the number is zero?

MARIA
I'd say you're about to pitch me something illegal.

VICTOR
(grinning)
IRC Section 1031. It's been in the tax code since 1921. The IRS wrote it. Congress renewed it. It's as legal as the mortgage interest deduction. And it's how real estate investors build empires without ever writing the government a check on their gains."""
        },
        {
            "heading": "PAGE 2 — THE CONCEPT",
            "content": """Victor stands, walks to a whiteboard.

VICTOR
The principle is simple: if you sell an investment property and buy a similar one, you haven't really "cashed out." You've just... shuffled. The IRS agrees. They call it a Like-Kind Exchange.

MARIA
Like-kind meaning what? Same type of building?

VICTOR
Broader than that. Any real property held for investment or business can be exchanged for any other real property held for investment or business. A duplex for a strip mall. A parking lot for an apartment complex. Raw land for a warehouse. It's all "like-kind" under 1031.

He writes on the board:

VICTOR (CONT'D)
The only things that DON'T qualify: your personal residence, inventory you're flipping, and since 2018, personal property like equipment or art. But real estate? Wide open."""
        },
        {
            "heading": "PAGE 3 — THE MECHANICS",
            "content": """VICTOR
Here's how it works mechanically. You can't just sell your duplex, pocket the cash, and then go buy something. The moment you touch that money, it's a taxable event.

MARIA
So how do I not touch it?

VICTOR
You use a Qualified Intermediary — a third party who holds the proceeds. Think of them as an escrow agent for tax purposes.

He draws a diagram:

VICTOR (CONT'D)
Step one: You sell the duplex. The buyer's money goes directly to the Qualified Intermediary. NOT to you. Step two: The QI holds those funds. Step three: When you find your replacement property, the QI sends the money directly to close. You never touch a dime.

MARIA
And that's it? No tax?

VICTOR
No tax. The gain is "deferred" — it rolls into the new property's basis. Your $200K basis carries forward. The IRS doesn't forget. They just... wait."""
        },
        {
            "heading": "PAGE 4 — THE DEADLINES",
            "content": """VICTOR
Now here's where people blow it. There are two absolutely rigid deadlines. Miss either one by even a day and the entire exchange fails. Full tax.

He writes two numbers on the board: 45 and 180.

VICTOR (CONT'D)
Deadline one: The 45-Day Identification Period. From the day your duplex closes, you have exactly 45 calendar days to identify — in writing — up to three potential replacement properties.

MARIA
What if I can't find anything in 45 days?

VICTOR
Then you pay the tax. No extensions. No excuses. Holidays, weekends, pandemics — doesn't matter. Day 46 and you're cooked.

He taps the second number.

VICTOR (CONT'D)
Deadline two: The 180-Day Exchange Period. You must close on the replacement property within 180 days of selling the original. Again, no flexibility.

MARIA
So I need to have my replacement property lined up fast.

VICTOR
Smart investors start shopping BEFORE they list the original. You want to hit day one of the 45 already knowing your top picks."""
        },
        {
            "heading": "PAGE 5 — THE MATH",
            "content": """MARIA
Walk me through the actual dollars.

VICTOR
Gladly. Your duplex: purchase price $200K. Current value $400K. Capital gain: $200K. Federal capital gains rate for your bracket: 20%. Plus the 3.8% Net Investment Income Tax. That's 23.8% total.

He calculates on the whiteboard:

VICTOR (CONT'D)
$200,000 times 23.8% equals $47,600 in federal tax alone. Add state tax if applicable — in some states that's another 5-10%. You could be looking at $57,000 or more.

MARIA
(wincing)

VICTOR
With the 1031: tax is zero. You take that $47,600 you didn't send to the IRS and put it into equity in the fourplex. That extra equity generates rental income, appreciates, and compounds — all tax-deferred.

MARIA
What's the long-term impact?

VICTOR
If you exchange every 7-10 years, reinvesting the deferred tax each time, after three exchanges you could have $150,000+ in equity that only exists because you never paid the tax. That's the power of tax-deferred compounding."""
        },
        {
            "heading": "PAGE 6 — BOOT: THE TAX TRAP",
            "content": """VICTOR
Now, there's a trap called "boot." Boot is anything you receive in the exchange that isn't like-kind property. And boot IS taxable.

MARIA
Like what?

VICTOR
Three types. Cash boot: if the QI sends you any leftover cash from the sale, that's taxable. Mortgage boot: if your new property has less debt than the old one, the difference is boot. And personal property boot: if the deal includes a car or furniture, that portion is taxable.

He draws a scale on the board.

VICTOR (CONT'D)
The golden rule: trade UP or EQUAL. Your replacement property must be equal to or greater in value than what you sold. And your new mortgage must be equal to or greater than the old mortgage.

MARIA
What if the fourplex is 500K and I'm putting down more cash?

VICTOR
Perfect. You're trading up. Zero boot. Full deferral. But if you bought a 350K property and pocketed the difference — that $50K difference is boot, and it's taxable immediately.

MARIA
So always go bigger.

VICTOR
Always go bigger. Or at minimum, equal."""
        },
        {
            "heading": "PAGE 7 — THE INFINITE DEFERRAL",
            "content": """MARIA
You said the tax is "deferred." Does that mean I eventually pay?

VICTOR
(smiling like he's been waiting for this question)
In theory, yes. When you finally sell without doing another exchange, the accumulated gain becomes taxable. But here's the beautiful part — you never have to stop exchanging.

MARIA
Ever?

VICTOR
Section 1031 has no limit on the number of exchanges. You can go from a duplex to a fourplex to a small apartment building to a commercial property — each time deferring the entire cumulative gain. Twenty exchanges over forty years? All deferred.

He writes on the board: "DEFER → DEFER → DEFER → DIE"

VICTOR (CONT'D)
And here's the endgame. IRC Section 1014. When you die, your heirs receive the property at a stepped-up basis — the fair market value at your date of death. All that deferred gain? Eliminated. Permanently. The tax that was deferred becomes the tax that was never paid.

MARIA
(sitting back)
So the strategy is: exchange until I die?

VICTOR
The strategy is: build wealth tax-free during your lifetime, and pass it to your heirs with a clean slate. The IRS wrote both sections. They work together. Legally, elegantly, and permanently."""
        },
        {
            "heading": "PAGE 8 — COMMON MISTAKES",
            "content": """VICTOR
Let me give you the top three ways people blow a 1031.

He holds up one finger.

VICTOR (CONT'D)
One: touching the money. I had a client who had his sale proceeds wired to his personal account "just for one night" before the QI set up. Taxable event. Forty-two thousand dollars in tax because of one banking error.

Two fingers.

VICTOR (CONT'D)
Two: missing the 45-day identification. Client went on vacation, came back on day 47, had her perfect property picked out. Too late. Full tax.

Three fingers.

VICTOR (CONT'D)
Three: using a related party as the QI. Your brother, your business partner, your LLC's attorney — none of them qualify. The QI must be independent. I've seen exchanges disqualified retroactively because the intermediary had a business relationship with the seller.

MARIA
How do I avoid all of that?

VICTOR
You hire someone who does this every week. Not your general accountant. A 1031 specialist and a dedicated QI firm. The cost is usually $800-1,200. To save you $47,000."""
        },
        {
            "heading": "PAGE 9 — THE REAL-WORLD APPLICATION",
            "content": """Victor pulls up his laptop and shows Maria a timeline.

VICTOR
Here's what your next 90 days look like. Week one: we list the duplex and simultaneously start shopping for replacement properties. I want three strong candidates identified before the duplex even sells.

MARIA
Why three?

VICTOR
Because you're allowed to identify up to three properties in the 45-day window regardless of value. It's called the Three Property Rule. If one falls through, you pivot to number two or three without breaking the exchange.

He scrolls through listings.

VICTOR (CONT'D)
Week four to six: duplex closes. Money goes to QI. Clock starts. But you've already done your homework. Day one you submit your written identification of the three properties.

MARIA
And then?

VICTOR
Weeks six through twenty: you negotiate, inspect, and close on the best option. QI funds the purchase directly. You walk away with a bigger property, more rental income, zero tax paid, and your basis carries forward for the next exchange in 7-10 years.

MARIA
(nodding slowly)
This is how people build real estate empires.

VICTOR
This is how SMART people build them. The ones who don't know this? They pay $47K every time they upgrade. You do the math on that over a lifetime."""
        },
        {
            "heading": "PAGE 10 — THE LESSON",
            "content": """Maria stands, shaking Victor's hand.

MARIA
I've been a landlord for twenty years and nobody told me this.

VICTOR
Most accountants know about it. Few push it. It requires planning, discipline, and a team. But the math is undeniable.

He walks her to the door.

VICTOR (CONT'D)
IRC Section 1031 — Like-Kind Exchange. Written in 1921. Survived every tax reform since. Congress keeps it because real estate investment drives the economy. It's not a loophole — it's an incentive. The code is telling you: keep investing, keep building, and we won't take our cut until you stop. And if you never stop? Section 1014 says we never will.

MARIA
(smiling)
I'm never stopping.

VICTOR
That's the right answer. I'll have the QI paperwork ready by Thursday.

Maria exits. Victor turns back to his whiteboard and starts sketching the next client's exchange — this one involving a strip mall and a multi-family in another state.

FADE OUT.

— END —"""
        }
    ]
}

# ═══════════════════════════════════════════════════════════════════════════════
# SCREENPLAY 2: Donor-Advised Funds (Section 170)
# ═══════════════════════════════════════════════════════════════════════════════

SCREENPLAYS["Donor-Advised Funds"] = {
    "title": "The Donor-Advised Fund: The Philanthropist's Vault",
    "tax_section": "IRC Section 170",
    "subtitle": "A Tax Playbook Screenplay",
    "genre": "The Loophole (Heist/Caper)",
    "filename": "screenplay_donor_advised_fund.html",
    "summary": "A financial advisor reveals how to donate appreciated stock to a DAF — getting a full deduction at market value while avoiding capital gains, then granting to charities over decades on your own timeline.",
    "diagram": """
  APPRECIATED ASSET        DONOR-ADVISED           CHARITABLE
  (Stock, Crypto)            FUND                   GRANTS
 ─────────────────     ═══════════════════     ─────────────────
 • Apple stock at     ──╲                 ╱──  • Grant to any
   $10K basis, now     ───╲ ┌───────────┐╱───    501(c)(3)
   worth $100K         ────╳─│  DAF ACCOUNT │─╳── • On YOUR timeline
 • Donate directly     ───╱ └───────────┘╲───  • Invested & growing
   to the DAF         ╱                   ╲    • Anonymous option

  TAX BENEFITS:           INSIDE THE DAF:        FLEXIBILITY:
 ─────────────────     ═══════════════════     ─────────────────
 • Deduction = FMV     • Tax-free growth       • No minimum grant
   ($100K)             • No cap gains on       • No time pressure
 • No cap gains tax      the donation          • Advise forever
   on the $90K gain    • Compounds like IRA    • Name successors
 • AGI limit: 30%                              • Legacy giving

 ────────────────────────────────────────────────
 THE MATH:
 Sell stock & donate cash: pay $13,440 cap gains, deduct $86,560
 Donate stock directly to DAF: pay $0 cap gains, deduct $100,000
 Tax savings difference: ~$17,000 more in your pocket
""",
    "pages": [
        {
            "heading": "PAGE 1 — INT. WEALTH MANAGEMENT OFFICE — DAY",
            "content": """FADE IN:

A tastefully decorated wealth management office. JANET OKAFOR (45, sharp, a fiduciary advisor who actually earns her fees) sits across from DAVID WEINSTEIN (55, tech executive, philanthropically-minded but tax-allergic).

DAVID
I want to give a hundred grand to charity this year. My accountant says I should just write checks. But my stomach says there's a smarter way.

JANET
Your stomach is correct. How'd you make that hundred grand?

DAVID
Apple stock. Bought it fifteen years ago at ten thousand. It's worth a hundred now.

JANET
(leaning forward)
David, if you sell that stock and donate the cash, you're going to pay capital gains tax on ninety thousand dollars of gain before you give a penny away. At 23.8%, that's $21,420 gone. You'd only have $78,580 to donate.

DAVID
That's... annoying.

JANET
What if you donated the stock directly — never sold it — and got a deduction for the full hundred thousand? Zero capital gains. Full deduction. Every dollar works for charity instead of the IRS.

DAVID
That sounds too good to be true.

JANET
It's a Donor-Advised Fund. And it's been blessed by the IRS since 2006."""
        },
        {
            "heading": "PAGE 2 — HOW A DAF WORKS",
            "content": """Janet opens her laptop and pulls up a diagram.

JANET
A DAF is like a charitable investment account. You make an irrevocable donation into the fund — you get your tax deduction immediately. But you don't have to give the money to a specific charity right away. It sits in the fund, invested, growing tax-free, until YOU advise where it should go.

DAVID
I advise? So I still have control?

JANET
Advisory control. You recommend grants to qualified 501(c)(3) charities. The sponsoring organization technically approves them, but in practice, if it's a legit charity, they rubber-stamp it. You can grant ten thousand this year, fifty thousand next year, and forty thousand the year after. Or all at once. Or over twenty years.

DAVID
And the deduction happens...

JANET
The year you fund the DAF. All of it. You put a hundred thousand of appreciated stock in this year, you deduct a hundred thousand this year. The actual charitable grants happen on your timeline.

DAVID
That's... incredible flexibility.

JANET
It gets better. The money inside the DAF is invested — mutual funds, index funds, whatever you choose. It grows tax-free. Your hundred thousand could be a hundred forty thousand in five years. All of it going to charity eventually, but growing untaxed in the meantime."""
        },
        {
            "heading": "PAGE 3 — THE APPRECIATED STOCK ADVANTAGE",
            "content": """JANET
Let me show you why donating the stock directly — instead of selling and donating cash — is so powerful.

She draws two columns on a legal pad.

JANET (CONT'D)
Path A — Sell and donate: You sell 100K of Apple stock. You owe 23.8% on the $90K gain. That's $21,420 in tax. You have $78,580 left to donate. Your charitable deduction: $78,580.

Path B — Donate stock to DAF: You transfer the stock directly to the DAF. No sale occurs. Zero capital gains tax. The DAF receives stock worth $100,000. Your charitable deduction: $100,000.

She circles the comparison.

JANET (CONT'D)
Path B gives you $21,420 more in deduction, and the charity gets $21,420 more in assets. Everyone wins except the IRS. And Congress specifically wrote Section 170 to allow this.

DAVID
Why would they do that?

JANET
Because they want to incentivize charitable giving. The more generous the tax benefit, the more people give. It's deliberate policy. You're doing exactly what the code was designed to encourage."""
        },
        {
            "heading": "PAGE 4 — BUNCHING: THE STANDARD DEDUCTION HACK",
            "content": """JANET
Now here's where strategy meets timing. In 2024, the standard deduction for a married couple is $29,200. If your total itemized deductions — mortgage interest, state taxes, charity — don't exceed that, you get zero tax benefit from charitable giving.

DAVID
Right, that's been my issue some years.

JANET
Enter "bunching." Instead of giving $20,000 a year for five years — and never exceeding the standard deduction — you put $100,000 into the DAF in ONE year. That year, you itemize and get the full $100,000 deduction. The other four years? You take the standard deduction.

She sketches it out:

JANET (CONT'D)
Without bunching: 5 years × $20K = $100K donated. Tax benefit: $0 (never exceeds standard deduction).

With bunching via DAF: Year 1: $100K to DAF, itemize, save ~$37,000 in taxes. Years 2-5: standard deduction ($29,200/year saved). Same total giving. Massive difference in tax benefit.

DAVID
And I still grant $20K per year from the DAF to my charities?

JANET
Exactly. The charities receive the same money on the same schedule. Nothing changes for them. But your tax picture is transformed."""
        },
        {
            "heading": "PAGE 5 — AGI LIMITATIONS AND CARRYFORWARD",
            "content": """DAVID
Is there a limit on how much I can deduct?

JANET
Yes, but it's generous. For cash donations to a DAF: up to 60% of your Adjusted Gross Income. For appreciated property like stock: up to 30% of AGI.

DAVID
My AGI is about $400K. So 30% is $120K. I'm under that with my $100K donation.

JANET
Perfect. Full deduction in year one. But say you wanted to donate $200K of stock in a single year. You'd deduct $120K this year, and the remaining $80K carries forward — you can deduct it over the next five years.

She writes:

JANET (CONT'D)
Year 1: Deduct $120K (30% of $400K AGI)
Year 2: Deduct $80K (carryforward)
Total: $200K deducted over 2 years.

DAVID
So even a massive donation gets fully deducted eventually?

JANET
Within six years, yes. The five-year carryforward ensures nothing is wasted. And if you're planning a big liquidity event — selling a company, exercising options, a large bonus year — you time the DAF contribution to that high-income year for maximum impact."""
        },
        {
            "heading": "PAGE 6 — WHAT YOU CAN DONATE",
            "content": """JANET
Stock isn't the only thing you can put into a DAF. Any appreciated asset held longer than one year qualifies for the FMV deduction.

DAVID
Like what?

JANET
Publicly traded stock — that's the easiest. Mutual fund shares. ETFs. But also: privately held business interests, real estate, cryptocurrency, and even complex assets like limited partnership interests. Each requires an appraisal for non-publicly-traded assets, but the principle is the same.

DAVID
I have some Bitcoin I bought at $5K that's now at $60K...

JANET
(lighting up)
Fifty-five thousand dollars of unrealized gain. If you sold it: $13,090 in tax. If you donate it directly to the DAF: zero tax, $60K deduction. Some DAF sponsors — Fidelity Charitable, Schwab Charitable, Vanguard Charitable — now accept crypto directly.

DAVID
I had no idea.

JANET
Most people don't. They sell the crypto, pay the tax, then donate the after-tax proceeds. That's leaving thirteen thousand dollars on the table. The code says you can donate the asset directly and everyone benefits more."""
        },
        {
            "heading": "PAGE 7 — INVESTMENT GROWTH INSIDE THE DAF",
            "content": """JANET
Here's the part that surprises people. The money inside your DAF isn't sitting in a savings account. It's invested. And it grows tax-free.

DAVID
Like a Roth IRA for charity?

JANET
Exactly that analogy. You choose from investment pools — typically index funds. Say you put $100K in and grant $20K per year. The remaining $80K is invested. At a 7% average return...

She runs the numbers:

JANET (CONT'D)
End of year 1: $80K invested, grows to $85,600. You grant $20K. Balance: $65,600.
End of year 2: $65,600 grows to $70,192. Grant $20K. Balance: $50,192.
But here's the key — that growth never gets taxed. In a regular brokerage account, those gains would be taxed annually. Inside the DAF: tax-free.

DAVID
So the charities ultimately receive MORE than I put in?

JANET
If you're patient, yes. A $100K DAF contribution that you grant over 10 years, with growth, might distribute $130K or more to charities. The tax-free compounding is working for the charitable mission.

DAVID
The IRS just lets that happen?

JANET
It's working exactly as designed. The incentive structure rewards patience in giving."""
        },
        {
            "heading": "PAGE 8 — LEGACY AND SUCCESSION",
            "content": """JANET
One more thing. When you open a DAF, you name successor advisors. These are the people who continue recommending grants after you pass away.

DAVID
My kids?

JANET
Your kids, your spouse, a trusted friend, even a charitable organization. The DAF continues beyond your lifetime as a giving vehicle. Some families use it as a mini private foundation — but without the reporting requirements, excise taxes, or mandatory 5% distribution rules that foundations carry.

DAVID
Wait — foundations have to distribute 5% per year?

JANET
Yes. IRC Section 4942 requires private foundations to distribute at least 5% of assets annually or face penalties. DAFs have NO minimum distribution requirement. You can let it grow for decades if you want.

She leans back.

JANET (CONT'D)
You also get anonymity if you want it. Grants from your DAF can be made anonymously — the charity sees the sponsoring organization's name, not yours. Foundations file public Form 990-PFs that list every grant. DAFs? Private.

DAVID
(laughing)
So it's cheaper to run, more flexible, more private, and has no forced distributions. Why would anyone start a foundation?

JANET
Control and prestige. A foundation gives you total governance — hiring, investing, programming. A DAF is simpler but more constrained. For most people under $5 million in charitable assets, the DAF wins on every practical metric."""
        },
        {
            "heading": "PAGE 9 — THE STRATEGIC CALENDAR",
            "content": """Janet pulls up a timeline on her screen.

JANET
Here's your playbook for this year. October: we identify your most appreciated lots of Apple stock — the ones with the lowest basis. We want maximum gain avoided.

DAVID
The shares from 2009.

JANET
Perfect. We transfer those specific shares — not sell, TRANSFER — directly to your DAF account at Fidelity Charitable. The transfer typically takes 3-5 business days for publicly traded stock.

She scrolls forward.

JANET (CONT'D)
November: your year-end tax projection shows the $100K deduction. We verify you're under the 30% AGI limit. December 31: the deduction locks into this tax year.

DAVID
And then?

JANET
January onward: you start advising grants. Your alma mater, the food bank, that education nonprofit you love — you send grants whenever you want, in whatever amounts you want. No rush. No pressure. The money is permanently dedicated to charity; you're just directing the flow.

DAVID
What's the minimum to open one?

JANET
Most sponsors: $5,000 initial contribution. Some are as low as $0 with recurring contributions. Annual fees are typically 0.60% of assets. On $100K, that's $600 a year. You saved $21,000 in capital gains tax. The math is... not subtle."""
        },
        {
            "heading": "PAGE 10 — THE LESSON",
            "content": """David stands, energized.

DAVID
I've been donating wrong for fifteen years.

JANET
You've been donating GENEROUSLY for fifteen years. You just weren't capturing the full tax efficiency. The charity got helped either way. Now you'll help them more while keeping more too.

She walks him to the door.

JANET (CONT'D)
IRC Section 170 — Charitable Deductions. Donor-Advised Funds are the fastest-growing vehicle in philanthropy for a reason. You get an immediate deduction, avoid capital gains on appreciated assets, invest the funds tax-free, grant on your own timeline, and create a giving legacy that outlives you. All within code the IRS explicitly blesses.

DAVID
My accountant is going to be annoyed he didn't suggest this.

JANET
(smiling)
Lots of accountants know the tax code. Fewer know the strategy. Send him my way — I'll make him look good.

David shakes her hand and exits. Janet turns back to her screen, opens the next client's portfolio — a founder with $2M in pre-IPO stock about to vest.

FADE OUT.

— END —"""
        }
    ]
}

# ═══════════════════════════════════════════════════════════════════════════════
# SCREENPLAY 3: Backdoor Roth IRA (Section 408A)
# ═══════════════════════════════════════════════════════════════════════════════

SCREENPLAYS["Backdoor Roth IRA"] = {
    "title": "The Backdoor Roth: The Income Ceiling Bypass",
    "tax_section": "IRC Section 408A",
    "subtitle": "A Tax Playbook Screenplay",
    "genre": "The Loophole (Heist/Caper)",
    "filename": "screenplay_backdoor_roth.html",
    "summary": "A savvy financial planner shows a high-earning couple how to contribute to a Roth IRA despite being over the income limit — using a perfectly legal two-step conversion that Congress has known about for decades.",
    "diagram": """
  HIGH EARNER              TWO-STEP                  ROTH IRA
  (Over $240K AGI)        CONVERSION               (Tax-Free Growth)
 ─────────────────     ═══════════════════     ─────────────────
 • Can't contribute   ──╲                 ╱──  • Tax-free growth
   directly to Roth    ───╲ ┌───────────┐╱───  • Tax-free withdrawals
 • No income limit     ────╳─│  BACKDOOR  │─╳── • No RMDs ever
   on Traditional      ───╱ └───────────┘╲───  • Estate planning tool
 • No income limit    ╱                   ╲
   on CONVERSION

  STEP 1:                  STEP 2:              RESULT:
 ─────────────────     ═══════════════════     ─────────────────
 • Contribute $7K      • Convert Traditional   • $7K/year in Roth
   to Traditional        to Roth immediately   • Tax-free at 59½
   IRA (non-deduct.)   • Minimal/zero tax      • Compounds for decades
 • After-tax money       (no gains yet)        • Mega backdoor: $69K

 ────────────────────────────────────────────────
 THE MATH (couple, 30 years at 8%):
 $14K/year × 30 years = $420K contributed
 At 8% growth = $1.76M in Roth
 Tax on $1.76M at withdrawal: $0
 Tax saved vs. taxable account: ~$400K+
""",
    "pages": [
        {
            "heading": "PAGE 1 — INT. KITCHEN TABLE — EVENING",
            "content": """FADE IN:

A well-appointed kitchen in a suburban home. PRIYA SHARMA (38, software engineer, analytical mind) and her husband JAMES (40, marketing director) sit at the kitchen table with their financial planner, ELENA RUIZ (50s, CFP, zero tolerance for jargon).

PRIYA
Our combined AGI is $290,000. My coworker says we can't contribute to a Roth IRA because we make too much. Is that true?

ELENA
Technically, yes. The direct contribution limit for Roth IRAs phases out at $240,000 for married filing jointly in 2024. You're well over.

JAMES
So we're locked out of the best retirement account?

ELENA
(smiling)
Of the front door, yes. But the back door is wide open. And the IRS has known about it since 2010. They've never closed it. At this point, it's effectively endorsed."""
        },
        {
            "heading": "PAGE 2 — THE TWO STEPS",
            "content": """Elena pulls out a napkin and draws two arrows.

ELENA
The Backdoor Roth is a two-step process. Step one: you each contribute $7,000 to a Traditional IRA. There's no income limit on Traditional IRA contributions — only on the DEDUCTION. Since you have workplace 401(k)s, you can't deduct these contributions. But you can still make them.

PRIYA
So we put in after-tax money that we can't deduct?

ELENA
Exactly. Step two: the next day — or the next week, it doesn't matter — you CONVERT that Traditional IRA to a Roth IRA. There's no income limit on Roth conversions. Congress removed that limit in 2010.

JAMES
That's it? Contribute and convert?

ELENA
That's it. You contributed after-tax dollars, so the conversion is tax-free — you already paid tax on that money. Now it's in a Roth, growing tax-free forever.

PRIYA
And this is... legal?

ELENA
The IRS issued guidance in 2018 explicitly acknowledging this strategy. It's not a loophole they overlooked. It's a feature of how the code interacts. Two rules, each perfectly legal, that combine to produce a result Congress could close if they wanted to — and hasn't."""
        },
        {
            "heading": "PAGE 3 — THE PRO-RATA TRAP",
            "content": """ELENA
Now, there's ONE thing that can mess this up. It's called the Pro-Rata Rule. And it trips up a lot of people.

JAMES
What is it?

ELENA
When you convert a Traditional IRA to a Roth, the IRS looks at ALL your Traditional IRA balances — not just the one you're converting. If you have pre-tax money in ANY Traditional IRA, the conversion is partially taxable.

She draws an example:

ELENA (CONT'D)
Say James has a $7,000 non-deductible Traditional IRA he wants to convert, but he ALSO has a $63,000 rollover IRA from an old 401(k). Total Traditional IRA balance: $70,000. Of that, $7,000 is after-tax and $63,000 is pre-tax. That's 10% after-tax.

JAMES
So I can only convert 10% tax-free?

ELENA
Exactly. You'd convert $7,000 but only $700 is tax-free. The other $6,300 is taxable. The IRS forces you to pro-rate.

PRIYA
How do we avoid that?

ELENA
Simple: make sure you have ZERO pre-tax money in Traditional IRAs on December 31 of the conversion year. If you have old rollovers, move them INTO your current 401(k) plan — most plans accept incoming rollovers. Once your Traditional IRA balance is zero, the conversion is 100% tax-free."""
        },
        {
            "heading": "PAGE 4 — THE MEGA BACKDOOR ROTH",
            "content": """ELENA
Now let me blow your mind. The regular backdoor gets you $7,000 per person per year. But if your 401(k) plan allows it, there's a MEGA Backdoor Roth that can get you up to $69,000 per year.

PRIYA
(eyes wide)
How?

ELENA
The total 401(k) contribution limit for 2024 is $69,000 — that includes your employee deferrals ($23,000), your employer match, and... after-tax contributions. Most people don't know about that third bucket.

She writes the breakdown:

ELENA (CONT'D)
Employee pre-tax/Roth deferral: $23,000
Employer match: let's say $10,000
After-tax contributions: up to $36,000 (the remainder to reach $69,000)

If your plan allows after-tax contributions AND in-service Roth conversions, you contribute $36,000 after-tax to the 401(k) and immediately convert it to Roth — either within the plan or to an outside Roth IRA.

JAMES
Does our plan allow that?

ELENA
That's what we check. Not all plans do. But increasingly, large tech employers are adding this feature specifically because employees are asking for it. Priya — check your plan documents for "after-tax contributions" and "in-service withdrawals or conversions."

PRIYA
If it does... we could put $69,000 EACH into Roth space every year?

ELENA
Between the regular backdoor and the mega backdoor, potentially yes. Tax-free growth on six figures annually. The math over 20-30 years is... staggering."""
        },
        {
            "heading": "PAGE 5 — THE LONG-TERM MATH",
            "content": """Elena opens her financial planning software.

ELENA
Let's run the numbers. Both of you contribute $7,000 each via the regular backdoor. That's $14,000 per year into Roth accounts. At 8% average annual growth over 30 years...

She shows the screen:

ELENA (CONT'D)
$14,000 per year × 30 years × 8% growth = approximately $1.76 million. Tax on that $1.76 million when you withdraw it in retirement? Zero. Zero federal. Zero state in most states. Zero on the growth, zero on the contributions.

JAMES
And if we did the mega backdoor too?

ELENA
If Priya can add $36K through mega backdoor: $43,000 per year going into Roth space. Over 30 years at 8%: approximately $5.4 million. Tax-free.

PRIYA
(quiet)
Five point four million dollars... with no tax ever.

ELENA
Compare that to a taxable brokerage account with the same contributions and growth. At a blended 20% tax rate on gains: you'd net about $4.3 million. The Roth saves you over a million dollars in taxes.

She pauses for effect.

ELENA (CONT'D)
And unlike Traditional IRAs and 401(k)s, Roths have NO Required Minimum Distributions. You never have to take money out. It can grow for your entire life and pass to your heirs — who then get tax-free withdrawals over 10 years."""
        },
        {
            "heading": "PAGE 6 — THE FIVE-YEAR RULES",
            "content": """JAMES
Are there any catches on when we can access the money?

ELENA
Two five-year rules you should know. First: Roth contributions can always be withdrawn tax-free and penalty-free. You already paid tax on them. That $7,000 you put in? You can pull it out tomorrow if you want.

PRIYA
And the growth?

ELENA
Rule one: the Roth account itself must be open for at least five years before you can withdraw earnings tax-free. This starts from January 1 of the year you first funded ANY Roth IRA. So if you open one today, the clock started January 1, 2024. By 2029, you're clear.

She holds up a second finger.

ELENA (CONT'D)
Rule two: conversion amounts have their own five-year clock for the 10% early withdrawal penalty. Each annual conversion starts its own five-year timer. After 59½, all these rules are irrelevant — everything comes out tax-free and penalty-free.

JAMES
We're 38 and 40. So by the time we retire...

ELENA
Everything will have been seasoning for 20+ years. Both five-year rules are satisfied many times over. For you, this is pure long-term wealth building with no practical restrictions."""
        },
        {
            "heading": "PAGE 7 — ANNUAL EXECUTION",
            "content": """ELENA
Let me walk you through the annual mechanics. It's simple once you set it up.

She pulls out a checklist:

ELENA (CONT'D)
January: Each of you contributes $7,000 to your respective Traditional IRAs. Make sure these accounts have zero prior balance — we cleared those old rollovers last year.

February: Convert each Traditional IRA fully to Roth. Fill out one form with your brokerage. Some — Vanguard, Fidelity, Schwab — let you do it online in three clicks.

PRIYA
Should we wait between the contribution and conversion?

ELENA
The IRS has never specified a required waiting period. Some advisors recommend a few days to a week, just for clean paperwork. Others convert the next business day. There's no formal "step transaction doctrine" risk here — the IRS has had years to challenge it and hasn't.

JAMES
What about tax forms?

ELENA
You'll get a Form 8606 with your tax return — it tracks your non-deductible contributions and shows the conversion was non-taxable. Your CPA or tax software handles it. It adds maybe five minutes to your annual filing.

ELENA (CONT'D)
April: File your taxes with Form 8606. Done. Repeat every January for the rest of your working lives."""
        },
        {
            "heading": "PAGE 8 — WHY CONGRESS HASN'T CLOSED IT",
            "content": """PRIYA
I keep waiting for the catch. If this is so good, why hasn't Congress eliminated it?

ELENA
They've tried. The Build Back Better Act in 2021 included a provision to ban backdoor Roth conversions for high earners. It passed the House. It died in the Senate.

JAMES
Could they try again?

ELENA
Always possible. But here's why it's unlikely to go away: tens of millions of Americans use Roth conversions. Financial services firms lobby heavily to keep them. And any change would likely be prospective — meaning money already in Roth stays in Roth.

She leans forward.

ELENA (CONT'D)
That's actually an argument for doing it NOW rather than later. Every dollar you get into Roth space today is protected even if the rules change tomorrow. It's like filling sandbags before the flood — the ones already in place still work.

PRIYA
So the worst case is they close the door going forward and we keep everything we've already converted?

ELENA
Exactly. There's no scenario where doing the backdoor Roth this year is the wrong move. The downside risk is essentially zero. The upside is decades of tax-free compounding."""
        },
        {
            "heading": "PAGE 9 — ROTH VS. TRADITIONAL: THE DECISION",
            "content": """JAMES
Quick question — should we also be doing pre-tax contributions to our 401(k)s? Or convert everything to Roth?

ELENA
Great question. It depends on whether you think your tax rate will be higher or lower in retirement.

She draws a simple comparison:

ELENA (CONT'D)
Pre-tax 401(k): Deduction now at your current rate (32%). Pay tax at withdrawal at your future rate. If your future rate is lower — say 22% — pre-tax wins.

Roth: No deduction now. Tax-free at withdrawal. If your future rate is higher — or if tax rates rise nationally — Roth wins.

PRIYA
We don't know future tax rates.

ELENA
Nobody does. That's why the smartest play is tax diversification. Max your pre-tax 401(k) for the $23K deduction at 32%. THEN do the backdoor Roth for additional savings. You end up with both pre-tax and Roth buckets. In retirement, you draw from whichever is most tax-efficient that year.

JAMES
So it's not either/or.

ELENA
Never either/or. It's both. The backdoor Roth is ADDITIONAL savings beyond your 401(k). It's not replacing it — it's complementing it. Two engines pulling the same train."""
        },
        {
            "heading": "PAGE 10 — THE LESSON",
            "content": """Priya and James exchange a look — the kind couples give each other when they realize they've been leaving money on the table.

PRIYA
We should have started this ten years ago.

ELENA
The best time to start was when you first crossed the income limit. The second best time is today. Ten years of $14K per year at 8% that you missed? That's about $217,000 in a Roth you don't have. But you've got 25+ years ahead. The math still works overwhelmingly in your favor.

She gathers her papers.

ELENA (CONT'D)
IRC Section 408A — Roth Individual Retirement Accounts. The income limits exist. The backdoor exists around them. The IRS knows. Congress knows. Your coworker who told you it was impossible? They're wrong. And they're probably sitting on the same opportunity you are.

JAMES
We're sending them your card.

ELENA
(laughing)
Please do. I'll have accounts open for both of you by Friday. First contributions in January. Conversions the same week. And we do it every year until you tell me to stop.

She shakes both their hands and lets herself out. Priya opens her laptop and starts searching "mega backdoor Roth" — already planning the next move.

FADE OUT.

— END —"""
        }
    ]
}

# ═══════════════════════════════════════════════════════════════════════════════
# SCREENPLAY 4: S-Corporation Election (Sections 1361-1379)
# ═══════════════════════════════════════════════════════════════════════════════

SCREENPLAYS["S-Corp Election"] = {
    "title": "The S-Corp Election: The Self-Employment Tax Escape",
    "tax_section": "IRC Sections 1361–1379",
    "subtitle": "A Tax Playbook Screenplay",
    "genre": "The Audit (Interrogation Room)",
    "filename": "screenplay_s_corp_election.html",
    "summary": "A freelancer making $200K learns how electing S-Corp status splits her income into salary and distributions — saving $15,000+ per year in self-employment taxes while staying perfectly legal.",
    "diagram": """
  SOLE PROPRIETOR         S-CORP ELECTION          SPLIT INCOME
  (Schedule C)           ═══════════════════      ─────────────────
 ─────────────────    ──╲                   ╱──  SALARY: $90K
 • $200K net income    ───╲ ┌─────────────┐╱───  (subject to FICA)
 • ALL subject to      ────╳─│  S-CORP 1120S │─╳──
   15.3% SE tax        ───╱ └─────────────┘╲───  DISTRIBUTIONS: $110K
 • Tax: $24,500+      ╱                     ╲    (NO FICA tax)

  WITHOUT S-CORP:          THE SPLIT:             WITH S-CORP:
 ─────────────────     ═══════════════════     ─────────────────
 • $200K × 15.3%       • Salary must be        • Salary: $90K
   = $24,500 SE tax      "reasonable"           • FICA on $90K only
 • No splitting         • Rest = distribution   • SE tax: ~$13,770
 • Full FICA burden     • 2553 election form    • Savings: ~$10,730/yr

 ────────────────────────────────────────────────
 THE MATH:
 Sole Prop SE tax: $200K × 92.35% × 15.3% = $28,260
 S-Corp FICA tax: $90K × 15.3% = $13,770
 Annual savings: $14,490
 10-year savings (invested at 7%): $200,000+
""",
    "pages": [
        {
            "heading": "PAGE 1 — INT. IRS AUDIT ROOM — DAY",
            "content": """FADE IN:

A fluorescent-lit IRS audit room. AGENT PATRICIA DELMORE (50s, reading glasses, has audited 3,000 returns and seen every trick) sits across from TANYA RIVERS (35, freelance UX designer, terrified) and her CPA, GLEN NAKAMURA (40s, calm, folder of documentation at the ready).

AGENT DELMORE
Ms. Rivers, you filed an S-Corporation return last year. Your corporation paid you a salary of $90,000 and distributed $110,000 in profits. Your total net income was $200,000.

TANYA
(nervously)
Correct.

AGENT DELMORE
My question is simple: why isn't all $200,000 subject to employment taxes?

GLEN
(opening his folder)
Because the tax code specifically allows it, Agent Delmore. And we can demonstrate exactly why $90,000 is a reasonable salary for Ms. Rivers's services."""
        },
        {
            "heading": "PAGE 2 — THE SELF-EMPLOYMENT TAX PROBLEM",
            "content": """GLEN
Let me back up. Before Tanya elected S-Corp status, she was a sole proprietor filing Schedule C. Every dollar of her $200,000 net income was subject to self-employment tax — that's 15.3% combining Social Security (12.4%) and Medicare (2.9%).

He shows the calculation:

GLEN (CONT'D)
$200,000 times 92.35% — that's the self-employment tax base — times 15.3% equals $28,260 in SE tax. On top of regular income tax. That's before she buys groceries or pays rent.

AGENT DELMORE
Self-employment tax funds Social Security and Medicare. Everyone pays it.

GLEN
Employees pay 7.65% and their employer pays 7.65%. That's fair — the employer is matching. But a sole proprietor pays BOTH halves. And for someone earning over $160,000, the Social Security portion phases out but Medicare continues. The structure creates an enormous burden on successful freelancers.

He pulls out a document.

GLEN (CONT'D)
Section 1361 allows a single-member LLC to elect to be treated as an S-Corporation. When it does, the owner pays herself a reasonable salary — which IS subject to employment taxes — and takes the remaining profit as a distribution, which is NOT subject to employment taxes. This is how Congress structured it."""
        },
        {
            "heading": "PAGE 3 — THE REASONABLE SALARY STANDARD",
            "content": """AGENT DELMORE
And who decides what's "reasonable"?

GLEN
Case law, industry data, and IRS guidance. The standard comes from Revenue Ruling 59-221 and multiple Tax Court cases. A reasonable salary is what you'd have to pay an unrelated employee to do the same work.

He pulls out salary data.

GLEN (CONT'D)
Tanya is a senior UX designer in the Phoenix metro area with eight years of experience. Bureau of Labor Statistics data shows the median salary for this role is $85,000 to $105,000. We chose $90,000 — right in the median range.

AGENT DELMORE
Why not $70,000?

GLEN
Because that would be below market and invite exactly this audit. We WANT to be defensible. A reasonable salary isn't the minimum you can get away with — it's the amount that makes an auditor nod and move on.

TANYA
(to Glen, whispering)
Is this going okay?

GLEN
(whispering back)
We're doing great. This is exactly what we prepared for."""
        },
        {
            "heading": "PAGE 4 — THE DOCUMENTATION",
            "content": """Glen lays out a series of documents.

GLEN
Agent Delmore, here's our supporting documentation. First: three comparable salary surveys from Glassdoor, BLS, and Robert Half's 2023 salary guide. All show senior UX designers in this market earning $85K-$110K.

He turns the page.

GLEN (CONT'D)
Second: Tanya's corporate minutes establishing her compensation. The S-Corp held a board meeting — her as sole director — and documented the salary determination with these market comparisons attached.

AGENT DELMORE
(taking notes)

GLEN
Third: her W-2 showing $90,000 in wages. All payroll taxes were paid — employer and employee portions. FICA, FUTA, state unemployment. Everything withheld and remitted on time.

He pulls one more document.

GLEN (CONT'D)
Fourth: the Form 1120-S showing net corporate income of $200,000, officer compensation of $90,000, and the remainder distributed as an ordinary distribution reported on her K-1.

AGENT DELMORE
(reviewing the documents)
You came prepared.

GLEN
Ms. Rivers pays me to be prepared. That's why she won't have a problem today."""
        },
        {
            "heading": "PAGE 5 — THE MATH COMPARISON",
            "content": """AGENT DELMORE
Walk me through the tax difference.

GLEN
Gladly. Under sole proprietorship — Schedule C:
Net income: $200,000
SE tax: $200K × 92.35% × 15.3% = $28,260
Deductible half of SE tax: $14,130

Under S-Corp election:
Salary: $90,000
FICA on salary (both halves): $90K × 15.3% = $13,770
Distributions: $110,000
FICA on distributions: $0

He circles the comparison.

GLEN (CONT'D)
Annual employment tax savings: $28,260 minus $13,770 equals $14,490. That's $14,490 per year that stays in Tanya's pocket — or more precisely, that she can invest in her retirement accounts or her business.

AGENT DELMORE
Over ten years?

GLEN
$14,490 per year, invested at 7% annual return, compounds to approximately $200,000 over ten years. That's a retirement fund built entirely from tax savings the code explicitly permits.

AGENT DELMORE
(leaning back)
The math isn't the issue, Mr. Nakamura. The issue is whether the salary is reasonable. And based on your documentation... it appears to be."""
        },
        {
            "heading": "PAGE 6 — THE RED FLAGS",
            "content": """AGENT DELMORE
For my records — what red flags does the IRS look for with S-Corps?

GLEN
I'll be transparent. There are five things that trigger audits:

He counts on his fingers.

GLEN (CONT'D)
One: zero salary. Some S-Corp owners pay themselves nothing and take everything as distributions. That's indefensible — if you're performing services, you must pay yourself.

Two: salary dramatically below market. Paying yourself $30K as a surgeon is going to get flagged.

Three: inconsistent year-to-year. If your S-Corp makes $150K one year and you pay yourself $80K, then it makes $400K the next year and you still pay $80K — that raises questions.

Four: salary that's a suspiciously round percentage. Exactly 50/50 split or exactly $50K every year regardless of revenue suggests the salary isn't based on market analysis.

Five: no documentation. If you can't show HOW you determined the salary, the IRS assumes you picked the lowest number you thought you could get away with.

AGENT DELMORE
And Ms. Rivers avoids all five?

GLEN
All five. $90K on $200K revenue, supported by market data, documented in corporate minutes, consistent with her role and experience."""
        },
        {
            "heading": "PAGE 7 — THE SETUP COSTS",
            "content": """AGENT DELMORE
One more question — what does this structure cost to maintain?

GLEN
Fair question. There are real costs that offset some of the savings.

He lists them:

GLEN (CONT'D)
Formation: LLC filing fee ($150-$300 depending on state) plus S-Corp election on Form 2553 (free to file).

Annual costs:
— Payroll service: $50-150/month ($600-1,800/year)
— S-Corp tax return (Form 1120-S): $800-1,500/year for a CPA
— Registered agent: $100-300/year
— State franchise tax or annual report: varies ($0-800/year)
— Quarterly payroll tax filings: included in payroll service

Total annual overhead: approximately $2,000-4,000.

He compares:

GLEN (CONT'D)
Annual overhead: $3,000 (approximately)
Annual FICA savings: $14,490
Net benefit: $11,490 per year.

The breakeven point is roughly $60,000 in net self-employment income. Below that, the savings don't justify the costs. Above that — and especially above $100K — it's a no-brainer.

AGENT DELMORE
(nodding)
And Ms. Rivers is well above that threshold.

GLEN
Significantly. This structure makes mathematical sense for her and has since her first year earning over $80K."""
        },
        {
            "heading": "PAGE 8 — THE ADDITIONAL BENEFITS",
            "content": """Glen leans forward.

GLEN
Beyond the FICA savings, the S-Corp structure unlocks additional benefits.

AGENT DELMORE
Such as?

GLEN
One: an Accountable Plan. The S-Corp can reimburse Tanya for business expenses — home office, internet, phone, travel — tax-free to her and deductible by the corp. No more arguing about Schedule C deductions.

Two: retirement contributions. The corp can establish a Solo 401(k) and contribute up to $69,000 per year between employee deferrals and employer profit sharing. The employer match comes from the corp's profits — it's deductible to the corp and not subject to FICA.

Three: health insurance. The S-Corp pays Tanya's health insurance premiums. They're deductible by the corp and reported on her W-2 — but not subject to FICA taxes. It's a better arrangement than the self-employed health insurance deduction on Schedule C.

AGENT DELMORE
These all sound like standard business benefits.

GLEN
They are. But sole proprietors often miss them because the structure doesn't make them obvious. The S-Corp makes the corp-to-owner relationship clear, and every legitimate business deduction flows naturally from that relationship."""
        },
        {
            "heading": "PAGE 9 — THE ELECTION MECHANICS",
            "content": """AGENT DELMORE
Let's wrap up. How did Ms. Rivers actually make this election?

GLEN
Form 2553 — Election by a Small Business Corporation. Filed with the IRS. The LLC remains the legal entity, but it's now TAXED as an S-Corporation. For the IRS, it's a tax classification — not a change in legal structure.

He shows the form.

GLEN (CONT'D)
Requirements: one class of stock, no more than 100 shareholders, all shareholders must be US citizens or residents, and it can't be an ineligible corporation type like a bank or insurance company. For a solo freelancer, all of these are automatically satisfied.

AGENT DELMORE
Filing deadline?

GLEN
March 15 for an existing entity wanting S-Corp treatment for the current tax year. Or within 75 days of formation for a new entity. Late elections are sometimes accepted under Revenue Procedure 2013-30 if you can show reasonable cause.

TANYA
(speaking up)
We filed ours on time. Glen made sure of that.

AGENT DELMORE
(closing her folder)
I can see that. Ms. Rivers, Mr. Nakamura — your documentation is thorough, your salary is within reasonable range, and your election is properly filed. I don't have further questions on this issue.

TANYA
(exhaling)
Thank you."""
        },
        {
            "heading": "PAGE 10 — THE LESSON",
            "content": """EXT. IRS BUILDING — CONTINUOUS

Tanya and Glen walk out into the sunlight. Tanya's hands are still shaking slightly.

TANYA
I thought I was going to owe thousands in back taxes.

GLEN
You did everything right. The S-Corp election is one of the most well-established tax strategies for self-employed professionals. The IRS doesn't audit them because they're illegal — they audit them to make sure the salary is reasonable. Yours is.

He puts on sunglasses.

GLEN (CONT'D)
IRC Sections 1361 through 1379 — Subchapter S Corporations. Congress created this structure specifically so small business owners could access corporate tax benefits without double taxation. The employment tax savings are a feature, not a bug. The code rewards business owners who structure properly.

TANYA
Every freelancer I know just files Schedule C and complains about taxes.

GLEN
And every one of them earning over $80K is leaving $10,000 or more per year on the table. The information is public. The forms are free. The only cost is doing it right.

He hands her his card.

GLEN (CONT'D)
Same time next January for your annual compensation review. We'll adjust the salary based on your revenue and fresh market data. That's how you stay audit-proof.

Tanya nods, tucks the card in her bag, and walks toward her car — $14,490 richer every year because she structured properly.

FADE OUT.

— END —"""
        }
    ]
}

# ═══════════════════════════════════════════════════════════════════════════════
# SCREENPLAY 5: Qualified Business Income Deduction (Section 199A)
# ═══════════════════════════════════════════════════════════════════════════════

SCREENPLAYS["Section 199A QBI"] = {
    "title": "The QBI Deduction: The Pass-Through Bonus",
    "tax_section": "IRC Section 199A",
    "subtitle": "A Tax Playbook Screenplay",
    "genre": "The Loophole (Heist/Caper)",
    "filename": "screenplay_qbi_deduction.html",
    "summary": "A tax strategist explains how pass-through business owners get a free 20% deduction on qualified business income — effectively reducing their top rate from 37% to 29.6% — and the tricks to stay under the income thresholds.",
    "diagram": """
  PASS-THROUGH INCOME       SECTION 199A            NET EFFECT
  (S-Corp, LLC, Sole)      DEDUCTION              ─────────────────
 ─────────────────────   ═══════════════════     • 20% OFF the top
 • Schedule C income    ──╲                ╱──   • Max rate: 29.6%
 • S-Corp K-1 income     ───╲┌──────────┐╱───     instead of 37%
 • Partnership K-1        ────╳│  199A QBI │╳──── • Up to $364K (MFJ)
 • Rental income (?)     ───╱└──────────┘╲───     no limitations
 • NOT W-2 wages        ╱                  ╲    • Above: W-2/UBIA test

  QUALIFIES:               LIMITS:                DOESN'T QUALIFY:
 ─────────────────────   ═══════════════════     ─────────────────
 • Most businesses       • SSTB phase-out       • Specified Service:
 • Below threshold:        above $364K (MFJ)      Law, Medicine,
   full 20%, no limits   • W-2 wages test         Consulting, Finance
 • Rental income          above threshold        • (But OK if under
   (safe harbor)        • UBIA (property) test     $364K!)

 ────────────────────────────────────────────────
 THE MATH:
 QBI = $300K pass-through income
 199A deduction = $300K × 20% = $60,000 FREE deduction
 Tax savings at 32% bracket: $60K × 32% = $19,200/year
""",
    "pages": [
        {
            "heading": "PAGE 1 — INT. COWORKING SPACE LOUNGE — DAY",
            "content": """FADE IN:

A modern coworking space. RASHID HASSAN (40s, owns three businesses, always in a hurry) drops into a chair across from his tax strategist CHARLOTTE PRICE (50s, former IRS agent turned advisor, knows where the bodies are buried).

RASHID
Charlotte, I made $300K from my businesses last year. My tax bill was brutal. Tell me there's something I'm missing.

CHARLOTTE
When you say $300K from your businesses — is that W-2 wages or pass-through income?

RASHID
Pass-through. I own an S-Corp marketing agency, a partnership in a real estate venture, and a sole proprietorship doing consulting on the side.

CHARLOTTE
(grinning)
Then you're missing a $60,000 deduction. And it's literally free.

RASHID
Sixty thousand? How?

CHARLOTTE
Section 199A. The Qualified Business Income deduction. Congress gave it to pass-through owners in 2017. It's a 20% deduction on your qualified business income. You don't have to do ANYTHING extra to claim it — you just have to know it exists."""
        },
        {
            "heading": "PAGE 2 — WHAT QUALIFIES",
            "content": """CHARLOTTE
Here's how it works. If you earn income through a pass-through entity — that's a sole proprietorship, partnership, LLC, or S-Corp — you get to deduct 20% of that income. It comes off the top, before you calculate your tax.

RASHID
All of my businesses count?

CHARLOTTE
Your marketing agency S-Corp: yes. Your real estate partnership: yes. Your consulting sole proprietorship... maybe. And that "maybe" is where the strategy lives.

She pulls out a highlighter.

CHARLOTTE (CONT'D)
There are two categories. "Qualified trades or businesses" — basically anything that makes money — and "Specified Service Trades or Businesses" — or SSTBs. SSTBs include law, accounting, medicine, consulting, financial services, and performing arts.

RASHID
Consulting is specified? That's my sole proprietorship.

CHARLOTTE
Right. BUT — and this is critical — if your total taxable income is under $364,200 for married filing jointly ($182,100 single), the SSTB limitation doesn't apply. You get the full 20% on everything, including consulting.

RASHID
I'm filing jointly. Our total taxable income is about $340K.

CHARLOTTE
(leaning back)
Then all three businesses qualify. Full 20%. No limitations. $60,000 deduction."""
        },
        {
            "heading": "PAGE 3 — THE MATH",
            "content": """Charlotte scribbles on a napkin.

CHARLOTTE
Let's break it down by business.

Marketing agency (S-Corp K-1): $180,000 QBI
Real estate partnership (K-1): $70,000 QBI
Consulting sole prop (Schedule C): $50,000 QBI
Total QBI: $300,000

Section 199A deduction: $300,000 × 20% = $60,000

RASHID
And that just... disappears from my taxable income?

CHARLOTTE
It's a deduction from your taxable income, not from your AGI. Think of it like a second standard deduction — but one that only pass-through business owners get. W-2 employees don't get this. Only business owners.

She calculates the tax savings:

CHARLOTTE (CONT'D)
Your marginal rate without the deduction: 32%. With the $60,000 QBI deduction: $60,000 × 32% = $19,200 in tax savings. Every year. For doing nothing extra.

RASHID
And I haven't been claiming this?

CHARLOTTE
Your tax software might be calculating it automatically — check Line 13 of your 1040 from last year. If your prior preparer was competent, it's there. If not... we might need to amend."""
        },
        {
            "heading": "PAGE 4 — ABOVE THE THRESHOLD",
            "content": """RASHID
What if my income goes up next year? What happens above $364K?

CHARLOTTE
Above $364,200 (MFJ), two things change. First, if any of your businesses are SSTBs — like your consulting — the deduction for that business phases out between $364K and $464K. Above $464K, SSTBs get zero deduction.

RASHID
So if I earn more, my consulting loses the deduction?

CHARLOTTE
Exactly. But your non-SSTB businesses — the marketing agency and real estate — still qualify. They just face a different limitation: the W-2 wages and UBIA test.

She writes the formula:

CHARLOTTE (CONT'D)
Above threshold, the deduction for non-SSTB businesses is the LESSER of:
A) 20% of QBI, OR
B) The GREATER of:
   — 50% of W-2 wages paid by the business, OR
   — 25% of W-2 wages PLUS 2.5% of UBIA (Unadjusted Basis of Qualified Property)

RASHID
That's... complicated.

CHARLOTTE
It is. But it means: if your business pays significant wages or owns significant property, you're fine. Your marketing agency pays employees $400K in total wages. Fifty percent of that is $200K — way more than 20% of your $180K income. You'd still get the full deduction even above the threshold.

RASHID
So the employees I'm already paying protect my deduction?

CHARLOTTE
The W-2 wages serve double duty: running your business AND securing your 199A deduction. Beautiful, isn't it?"""
        },
        {
            "heading": "PAGE 5 — RENTAL REAL ESTATE",
            "content": """RASHID
What about the rental income from the partnership? You said real estate qualifies.

CHARLOTTE
It does, with a caveat. The IRS issued a safe harbor — Revenue Procedure 2019-38 — that says rental real estate activities qualify for 199A if you spend at least 250 hours per year on rental activities AND keep contemporaneous records.

RASHID
We have a property manager.

CHARLOTTE
The hours can include time spent by your employees, agents, or contractors. So the property manager's time counts toward your 250 hours. As long as the total — you plus your team — exceeds 250 hours per year and you maintain a log, your rental income qualifies.

She pauses.

CHARLOTTE (CONT'D)
Even without the safe harbor, many tax practitioners take the position that rental income qualifies as QBI under general 199A rules — it's income from a trade or business. The safe harbor just gives you extra protection in an audit.

RASHID
And triple-net lease income?

CHARLOTTE
Riskier. If you're truly passive — just collecting rent with zero management involvement — it's harder to call it a "trade or business." But active rental operations with maintenance, tenant screening, and improvement projects? Solidly qualifies."""
        },
        {
            "heading": "PAGE 6 — STRATEGIC INCOME MANAGEMENT",
            "content": """CHARLOTTE
Now here's where the real strategy lives. Your taxable income is $340K this year — under the $364K threshold. That means everything qualifies with no limitations. But what if next year your income jumps to $400K?

RASHID
My consulting loses its deduction.

CHARLOTTE
Right. So what do you do? You manage your taxable income to stay below the threshold. Legally.

She lists options:

CHARLOTTE (CONT'D)
Option one: maximize retirement contributions. Your S-Corp Solo 401(k) employer contribution can be up to 25% of your salary. If you increase your salary or contributions, you reduce taxable income.

Option two: time deductions. If you're close to the threshold, accelerate business expenses into this year — buy equipment, prepay insurance, front-load marketing spend.

Option three: the charitable bunching strategy we discussed last week. A large Donor-Advised Fund contribution in a high-income year drops your taxable income below the threshold.

RASHID
So the $60K DAF contribution we talked about...

CHARLOTTE
Would drop your taxable income from $400K to $340K. Below the threshold. Full 199A deduction restored. The DAF contribution saves you tax directly AND unlocks additional savings through 199A. It's a multiplier effect.

RASHID
(laughing)
These strategies all work together.

CHARLOTTE
That's the game. No single strategy exists in isolation. They're an ecosystem."""
        },
        {
            "heading": "PAGE 7 — AGGREGATION AND SEPARATION",
            "content": """CHARLOTTE
One more tactical move. Section 199A allows you to aggregate multiple businesses for the W-2 wages and UBIA tests. If one business has lots of wages and another doesn't, combining them can help.

RASHID
Show me.

CHARLOTTE
Say your marketing agency has $400K in W-2 wages but your real estate partnership has zero. Individually, the real estate partnership would fail the W-2 wages test above the threshold. But if you aggregate them — and they share centralized management, which yours do — the combined W-2 wages cover both businesses.

She draws a bracket combining the two.

CHARLOTTE (CONT'D)
Conversely, sometimes SEPARATING businesses helps. If a non-SSTB business has a consulting arm inside it, splitting the consulting into its own entity might let the main business retain full 199A qualification.

RASHID
So the structure of your entities can change your deduction?

CHARLOTTE
Dramatically. This is why entity structure review should happen EVERY year, not just at formation. A decision you made five years ago might be costing you $10,000+ annually in lost 199A benefits.

RASHID
Let's review all of mine.

CHARLOTTE
Already on the calendar for November. Before year-end so we can restructure if needed."""
        },
        {
            "heading": "PAGE 8 — THE SUNSET",
            "content": """RASHID
How long does this deduction last?

CHARLOTTE
Here's the urgent part. Section 199A was enacted as part of the Tax Cuts and Jobs Act of 2017. It's scheduled to SUNSET on December 31, 2025. After that, it disappears unless Congress extends it.

RASHID
(alarmed)
That's next year!

CHARLOTTE
It's been a political football. Both parties have proposed extensions or modifications. It's likely to be extended in some form because it affects 25+ million small business owners — and those are voters. But "likely" isn't "certain."

She leans forward.

CHARLOTTE (CONT'D)
This means two things. One: claim every dollar of 199A deduction you're entitled to between now and the sunset. Don't leave money on the table while the law exists. Two: if you have the ability to accelerate income into the pre-sunset years — say, getting a client to pay early — it might be worth doing.

RASHID
And if it doesn't get extended?

CHARLOTTE
Your effective rate on pass-through income goes from 29.6% back to 37%. That's a 7.4 percentage point increase. On $300K of income: $22,200 more in tax per year. The deduction is worth fighting for — and worth planning around either outcome."""
        },
        {
            "heading": "PAGE 9 — COMMON MISTAKES",
            "content": """CHARLOTTE
Let me give you the top mistakes I see with 199A.

One: not claiming it at all. I've reviewed returns from other preparers where the taxpayer clearly qualified and it wasn't on the return. Tens of thousands in lost deductions.

Two: not tracking W-2 wages by business. When you're above the threshold, you need precise W-2 wage data for each separate qualified business. If your bookkeeping lumps everything together, you can't compute the limitation properly.

Three: not considering the SSTB rules before starting a new business. If you're above the income threshold and start a consulting company — that's an SSTB with zero 199A benefit. But if you structure the same services as a staffing company that provides contractors... it might not be specified service.

RASHID
Wait — the same work can qualify or not depending on how you structure it?

CHARLOTTE
The regulations are specific. "Consulting" is defined narrowly as providing advice and counsel. If your business provides services beyond advice — implementation, staffing, deliverables — it may not meet the SSTB definition. The facts and circumstances matter enormously.

RASHID
So how you describe your business in your formation documents...

CHARLOTTE
...can affect whether you get a 20% deduction. Words matter in tax law. We want your businesses described accurately — but also precisely enough that they don't accidentally fall into an SSTB category."""
        },
        {
            "heading": "PAGE 10 — THE LESSON",
            "content": """Rashid drains his coffee and shakes his head.

RASHID
I've been running businesses for fifteen years. Nobody explained 199A to me like this.

CHARLOTTE
It's new — only since 2018. And it's complex enough that most generalist CPAs apply it mechanically without optimizing. They calculate what the software spits out and move on. The strategy — managing income thresholds, aggregating businesses, structuring around SSTB rules — that's where the real value lives.

She packs up her laptop.

CHARLOTTE (CONT'D)
IRC Section 199A — Qualified Business Income Deduction. Twenty percent off the top for pass-through business owners. It's the single biggest tax incentive for small business since the S-Corp election. And it's sitting there, in the code, for anyone structured to claim it.

RASHID
The consulting entity — should we restructure before year-end?

CHARLOTTE
If your income's going above $364K, yes. We reclassify the entity description, separate the advisory services from the implementation services, and ensure the non-SSTB portion retains its full 199A benefit.

She stands.

CHARLOTTE (CONT'D)
November. That's our window. Before the calendar flips and the deduction for this year is locked in.

Rashid nods, already texting his business partner about the restructuring. Charlotte walks out, phone already ringing with the next client — another business owner who doesn't know they're missing $60,000.

FADE OUT.

— END —"""
        }
    ]
}

# ═══════════════════════════════════════════════════════════════════════════════
# SCREENPLAY 6: Tax-Loss Harvesting (Section 1091 Wash Sale Rule)
# ═══════════════════════════════════════════════════════════════════════════════

SCREENPLAYS["Tax-Loss Harvesting"] = {
    "title": "Tax-Loss Harvesting: The Portfolio Prune",
    "tax_section": "IRC Section 1091",
    "subtitle": "A Tax Playbook Screenplay",
    "genre": "The Loophole (Heist/Caper)",
    "filename": "screenplay_tax_loss_harvesting.html",
    "summary": "A wealth manager teaches a panicking client how to turn market losses into tax savings by strategically selling, booking the loss, and immediately buying a similar (but not identical) investment — all while navigating the wash sale rule.",
    "diagram": """
  PORTFOLIO LOSS           HARVEST THE             OFFSET GAINS
  (Paper → Realized)        LOSS                  & INCOME
 ─────────────────     ═══════════════════     ─────────────────
 • Stock A down 30%   ──╲                ╱──   • Offset cap gains
 • Loss is "paper"     ───╲┌──────────┐╱───   • $3K vs. ordinary
   until you sell       ────╳│ SELL + BUY │╳────   income/year
 • Sell to realize     ───╱└──────────┘╲───   • Carry forward
 • Buy similar (NOT   ╱                  ╲      unlimited losses
   substantially                               • Maintain exposure
   identical)

  WASH SALE RULE:          ALLOWED:               RESULT:
 ─────────────────     ═══════════════════     ─────────────────
 • Can't buy same      • Sell Vanguard S&P    • Tax loss: $30K
   security within       Buy Fidelity S&P     • Offset $30K gains
   30 days before/     • Sell AAPL             • Net tax saved:
   after the sale        Buy tech sector ETF     ~$7,140 at 23.8%
 • "Substantially      • Sell bond fund       • Portfolio stays
   identical" = NO       Buy diff duration       fully invested

 ────────────────────────────────────────────────
 THE MATH:
 $100K invested → drops to $70K → sell → realize $30K loss
 Buy similar fund same day → stay invested
 $30K loss offsets $30K in gains elsewhere
 Tax saved: $30K × 23.8% = $7,140 — and portfolio unchanged
""",
    "pages": [
        {
            "heading": "PAGE 1 — INT. FINANCIAL ADVISOR'S OFFICE — DAY",
            "content": """FADE IN:

A calm financial planning office. MARGARET KWAN (55, Certified Financial Planner, unflappable) faces her client DEREK CHEN (40s, tech worker, sweating through a market downturn).

DEREK
I'm down $80,000 this year. My portfolio is getting destroyed. Should I just sell everything and go to cash?

MARGARET
(steady)
No. But I want you to sell some things. Not because you're panicking — because those losses are VALUABLE. They're a tax asset sitting in your portfolio, and every day you don't harvest them is a day you're leaving money on the table.

DEREK
My losses are... valuable?

MARGARET
They're worth about $19,000 in tax savings right now. And I'm going to show you how to capture that money WITHOUT changing your investment strategy at all."""
        },
        {
            "heading": "PAGE 2 — PAPER LOSS VS. REALIZED LOSS",
            "content": """MARGARET
Right now your losses are "paper" losses. They exist on your screen but not on your tax return. The IRS doesn't care about paper losses. They only recognize REALIZED losses — which means you have to sell.

DEREK
But if I sell, I lock in the loss permanently.

MARGARET
Common misconception. You sell the losing position, realize the loss for tax purposes, and immediately buy a SIMILAR investment. Your portfolio exposure stays virtually identical. You stay fully invested. The only thing that changes is: you now have a tax deduction.

She draws a timeline:

MARGARET (CONT'D)
Monday 9:30 AM: Sell $100K position in Vanguard Total Stock Market Index Fund (VTSAX). Down 30%. Realized loss: $30,000.
Monday 9:31 AM: Buy $70,000 of Fidelity Total Market Index Fund (FSKAX). Same broad market exposure. Different fund company.

DEREK
Same day? That works?

MARGARET
Same minute if you want. The key is: you sold VTSAX and bought FSKAX. They track the same market. But they're not the same security. And that distinction matters enormously."""
        },
        {
            "heading": "PAGE 3 — THE WASH SALE RULE",
            "content": """MARGARET
Section 1091 — the Wash Sale Rule — says you cannot deduct a loss if you buy a "substantially identical" security within 30 days before or after the sale. That's a 61-day window: 30 days before, the sale day, and 30 days after.

DEREK
What counts as "substantially identical"?

MARGARET
Same security. If you sell Apple stock on Monday and buy Apple stock on Tuesday — wash sale. Loss is disallowed. If you sell Vanguard's S&P 500 fund and buy Vanguard's S&P 500 ETF (same underlying holdings, same manager) — the IRS will likely consider that substantially identical.

She lists what's safe:

MARGARET (CONT'D)
But if you sell Vanguard's S&P 500 fund and buy Fidelity's S&P 500 fund? Different fund, different manager, different CUSIP number. NOT substantially identical. Loss is valid.

Sell an individual stock and buy a sector ETF that contains it? Valid. You sold Apple and bought the Technology Select Sector SPDR. Different security.

DEREK
So I can maintain almost identical market exposure?

MARGARET
Almost identical, yes. The IRS allows you to stay invested in the same MARKET — just not the same SECURITY. That's the game."""
        },
        {
            "heading": "PAGE 4 — THE TAX MATH",
            "content": """MARGARET
Let's look at your actual portfolio losses.

She pulls up his account:

MARGARET (CONT'D)
International fund: bought at $50K, now worth $35K. Loss: $15,000.
Tech individual stocks: bought at $80K, now worth $52K. Loss: $28,000.
Bond fund: bought at $30K, now worth $27K. Loss: $3,000.
Small cap fund: bought at $40K, now worth $31K. Loss: $9,000.

Total harvestable losses: $55,000.

DEREK
And what does that save me?

MARGARET
First, those losses offset your capital gains. You sold some winners earlier this year — $35,000 in long-term gains. The first $35,000 of losses offset those gains dollar for dollar. At 23.8% (20% cap gains + 3.8% NIIT): that's $8,330 in tax savings.

Remaining losses: $20,000. Of that, $3,000 offsets ordinary income this year — at your 35% marginal rate, that's another $1,050.

The remaining $17,000 carries forward to next year and beyond — forever, until used.

DEREK
So I save about $9,380 THIS year, with $17K banked for future years?

MARGARET
And your portfolio is in the same investments, tracking the same markets. You just got a tax refund for free."""
        },
        {
            "heading": "PAGE 5 — THE 30-DAY WINDOW",
            "content": """DEREK
What about the 30-day rule going backward? You said 30 days BEFORE the sale too.

MARGARET
Right. If you bought additional shares of the same security within 30 days before your sale, that triggers a partial wash sale. The most common trap: automatic dividend reinvestment.

DEREK
(groaning)
My funds auto-reinvest dividends.

MARGARET
Exactly. If your Vanguard fund distributed and reinvested a dividend on December 1, and you try to harvest the loss on December 15, those reinvested shares within 30 days create a partial wash sale for that portion.

She shows the fix:

MARGARET (CONT'D)
Solution: turn off automatic reinvestment in any fund you plan to harvest BEFORE you sell. Let dividends accumulate as cash. Then sell the full position. No wash sale complication.

DEREK
Do I turn reinvestment back on after?

MARGARET
In the NEW fund — yes. FSKAX replaces VTSAX, and FSKAX can auto-reinvest from day one. You only need to pause reinvestment in the fund you're about to sell."""
        },
        {
            "heading": "PAGE 6 — AUTOMATED HARVESTING",
            "content": """MARGARET
Here's the modern evolution. Companies like Betterment, Wealthfront, and even Fidelity now offer automated tax-loss harvesting. The algorithm monitors your portfolio daily and harvests losses automatically whenever positions dip below their cost basis.

DEREK
Every single day?

MARGARET
Every day the market is down is a potential harvesting opportunity. And small frequent harvests add up to more than one big annual harvest. Research from Betterment suggests automated daily harvesting can add 1-2% to after-tax returns annually.

She explains:

MARGARET (CONT'D)
The algorithm sells the losing lot, buys the substitute, holds the substitute for 31 days, then swaps back to the original fund if it's still preferred. Continuous rotation. Continuous tax alpha.

DEREK
Should I use one of those robo-advisors?

MARGARET
If your portfolio is relatively simple — index funds and ETFs — an automated harvester is worth considering. For complex portfolios with individual stocks, restricted shares, or concentrated positions, you still want a human making those decisions. The wash sale rules get tricky with options, RSUs, and ESPP shares.

DEREK
I have RSUs from work.

MARGARET
Then we're doing this manually. Your RSU vesting dates interact with the 30-day windows in ways that algorithms often don't handle correctly."""
        },
        {
            "heading": "PAGE 7 — THE UNLIMITED CARRYFORWARD",
            "content": """MARGARET
One of the most underappreciated features of tax-loss harvesting: unused losses carry forward FOREVER. There's no expiration.

DEREK
Seriously? No time limit?

MARGARET
None. If you harvest $100,000 in losses during a major crash, you can use $3,000 per year against ordinary income plus unlimited amounts against capital gains — for the next thirty years if needed.

She draws a timeline:

MARGARET (CONT'D)
Say the market crashes and you harvest $100K in losses this year. Over the next decade, as you sell winners or rebalance, those carried-forward losses keep offsetting gains. It's like having a tax savings account that you built during the downturn and withdraw from during the recovery.

DEREK
So a bad year for my portfolio can be a good year for my taxes?

MARGARET
Some of my wealthiest clients have carryforward loss balances of $500K or more from 2008-2009. They've been harvesting those losses against gains for fifteen years. Every time they rebalance or take profits, the loss carryforward absorbs the tax. It's an enormous structural advantage.

DEREK
I wish I'd done this during COVID...

MARGARET
March 2020 was one of the greatest harvesting opportunities in history. A 30% drop and recovery within months. Anyone who harvested in March and bought back similar funds immediately captured losses that will save them taxes for a decade — while their portfolio recovered fully."""
        },
        {
            "heading": "PAGE 8 — WHAT NOT TO DO",
            "content": """MARGARET
Let me give you the mistakes to avoid.

One: harvesting in a retirement account. IRAs and 401(k)s don't generate taxable gains or deductible losses. Harvesting inside them does nothing. Only taxable brokerage accounts benefit.

Two: forgetting about spousal accounts. If you sell a stock and your spouse buys the same stock within 30 days — wash sale. The rule applies across ALL accounts you or your spouse control, including IRAs.

DEREK
Even my IRA?

MARGARET
If you sell Apple in your taxable account to harvest a loss, and your IRA buys Apple within 30 days — even through automatic rebalancing — the loss is permanently disallowed. Not deferred. Permanently gone. It's one of the harshest interpretations of the wash sale rule.

She holds up three fingers.

MARGARET (CONT'D)
Three: triggering short-term gains on the replacement. If you buy the substitute fund and sell it within a year, any gain is taxed at short-term rates (up to 37%) instead of long-term rates (20%). Make sure you hold the replacement for at least a year before swapping back.

Four: over-harvesting and resetting your basis too low. Every time you harvest and buy at the lower price, your cost basis resets lower. If markets recover, you'll eventually have larger gains when you sell. You're not eliminating tax — you're deferring it. But deferral IS valuable because of time value of money."""
        },
        {
            "heading": "PAGE 9 — THE ANNUAL CALENDAR",
            "content": """MARGARET
Here's your harvesting calendar going forward.

She pulls up a year view:

MARGARET (CONT'D)
Quarterly: I review your portfolio for harvestable positions. Any lot down 10% or more gets flagged for potential harvest.

October-November: the big push. We look at your year-to-date gains and estimate your tax liability. Then we harvest enough losses to offset those gains plus the $3,000 ordinary income deduction.

December: final sweep. Last chance to realize losses before the tax year closes. But watch the settlement date — trades must SETTLE by December 31, which means executing by approximately December 27-28.

DEREK
And the rest of the year?

MARGARET
Opportunistic harvesting during market drops. COVID crash in 2020, rate scare in 2022, any 10%+ correction — those are harvesting events. I'll reach out proactively when they happen.

She makes a note.

MARGARET (CONT'D)
One more thing: I'm turning off dividend reinvestment in your three largest taxable positions today. We'll harvest those this week while the losses are available. Markets can recover fast — we don't want to miss the window."""
        },
        {
            "heading": "PAGE 10 — THE LESSON",
            "content": """Derek looks at his portfolio with new eyes. The red numbers that were making him sick now look like opportunities.

DEREK
So my $80K loss isn't just pain — it's a $19,000 tax asset?

MARGARET
Think of it this way: the market gave you lemons. Tax-loss harvesting turns them into lemonade. You stay fully invested for the recovery, and you get a tax benefit that partially compensates you for the downturn. It doesn't eliminate the loss — but it softens the blow by 20-25%.

She shakes his hand.

MARGARET (CONT'D)
IRC Section 1091 — the Wash Sale Rule — is the boundary. Everything inside that boundary is fair game. Sell losing positions, buy similar but not identical replacements, stay invested, and capture the tax benefit. The code explicitly permits it. The IRS explicitly accepts it. And every year you don't do it is money you're donating to the Treasury for no reason.

DEREK
(calmer now)
I actually feel better about this downturn.

MARGARET
Good. That's the right frame. A disciplined investor sees opportunity in every market condition — up markets grow your wealth, down markets grow your tax assets. Both have value.

She turns to her computer and starts executing the trades. Derek watches the red numbers on his screen — not with dread anymore, but with purpose.

FADE OUT.

— END —"""
        }
    ]
}

# ═══════════════════════════════════════════════════════════════════════════════
# SCREENPLAY 7: Depreciation & Cost Segregation (Section 168/167)
# ═══════════════════════════════════════════════════════════════════════════════

SCREENPLAYS["Cost Segregation"] = {
    "title": "Cost Segregation: The Building Breakdown",
    "tax_section": "IRC Section 168 (MACRS)",
    "subtitle": "A Tax Playbook Screenplay",
    "genre": "The Loophole (Heist/Caper)",
    "filename": "screenplay_cost_segregation.html",
    "summary": "A real estate investor learns how a cost segregation study reclassifies parts of a building into faster depreciation categories — turning a 27.5-year deduction into massive Year 1 write-offs through bonus depreciation.",
    "diagram": """
  BUILDING PURCHASE         COST SEG                ACCELERATED
  ($1M Commercial)          STUDY                  DEPRECIATION
 ─────────────────     ═══════════════════     ─────────────────
 • Without study:     ──╲                ╱──   • 5-year: carpets,
   39-year straight    ───╲┌──────────┐╱───     appliances, fixtures
   line = $25,641/yr   ────╳│ RECLASSIFY │╳──── • 7-year: furniture,
 • With study:         ───╱└──────────┘╲───     certain equipment
   30-40% reclassed   ╱                  ╲    • 15-year: land
   to 5/7/15 year                              improvements, parking

  BEFORE STUDY:            AFTER STUDY:           YEAR 1 RESULT:
 ─────────────────     ═══════════════════     ─────────────────
 • Yr 1 deduction:     • $350K → 5-year        • $350K × 100% bonus
   $25,641               (bonus deprec.)          = $350K deduction
 • Linear & slow       • $100K → 15-year       • + $100K × 100%
 • 39 years to         • $550K → 39-year         = $100K deduction
   fully deduct        • Total Yr 1: $466K     • Year 1 total: $466K

 ────────────────────────────────────────────────
 THE MATH:
 Without cost seg: Year 1 deduction = $25,641
 With cost seg + bonus depreciation: Year 1 = $466,000+
 Tax savings at 37% rate: $172,000 in Year 1 alone
 Cost of study: $8,000-15,000 → ROI: 10x-20x
""",
    "pages": [
        {
            "heading": "PAGE 1 — INT. REAL ESTATE INVESTOR'S HOME OFFICE — DAY",
            "content": """FADE IN:

A home office cluttered with property listings. FRANK MORRISON (50s, owns seven commercial properties, self-taught investor) is on a video call with his new tax advisor, SAMIRA AZIZ (40s, specialty: real estate taxation, knows depreciation schedules like poetry).

FRANK
Samira, I bought a million-dollar commercial building last year. My old accountant set it up as 39-year straight-line depreciation. That gives me $25,641 per year in deductions. Fine. But a guy at my REIA meeting said I should get a cost segregation study. What is that?

SAMIRA
Frank, that cost seg study is going to turn your $25,000 deduction into a $450,000 deduction. In Year One.

FRANK
(long pause)
I'm sorry, did you say four hundred and fifty thousand?

SAMIRA
Give or take. And it's completely legal, well-established, and the IRS has blessed it in multiple revenue rulings. The real question is: why didn't your old accountant tell you about this?"""
        },
        {
            "heading": "PAGE 2 — WHAT IS COST SEGREGATION",
            "content": """SAMIRA
Here's the concept. When you buy a building, your accountant puts the entire purchase price — minus land — into one depreciation bucket: 39 years for commercial, 27.5 for residential. But a building isn't just one thing. It's made up of hundreds of components with different useful lives.

FRANK
Like what?

SAMIRA
The carpet has a 5-year useful life. The parking lot has a 15-year life. The specialized electrical for the HVAC: 7 years. The landscaping: 15 years. The cabinets, fixtures, appliances: 5-7 years. The concrete structure? That's 39 years.

She shares her screen showing a breakdown.

SAMIRA (CONT'D)
A cost segregation study sends an engineer and a tax professional to your property. They identify every component and reclassify it into the correct depreciation category. Instead of one bucket at 39 years, you get multiple buckets — many of which depreciate in 5, 7, or 15 years.

FRANK
And that's allowed?

SAMIRA
The IRS issued an Audit Techniques Guide specifically FOR cost segregation in 2004. They acknowledge it's legitimate. They just want the study done properly — by qualified engineers with documented methodology."""
        },
        {
            "heading": "PAGE 3 — THE RECLASSIFICATION",
            "content": """SAMIRA
For a typical $1 million commercial property, here's what a cost seg study often finds:

She shows a pie chart:

SAMIRA (CONT'D)
5-year property (personal property): 20-35% of building cost
— Carpet, vinyl flooring
— Decorative lighting
— Appliances
— Window treatments
— Specialized electrical outlets
— Cabinet work and millwork

7-year property: 5-10%
— Furniture and fixtures
— Certain equipment

15-year property (land improvements): 10-20%
— Parking lots and curbing
— Sidewalks
— Landscaping
— Fencing
— Outdoor lighting
— Signage

Remaining (39-year property): 40-60%
— Structural shell
— Roof
— HVAC core systems
— Plumbing infrastructure
— Electrical service entry

FRANK
So maybe 40-50% of my building can be depreciated faster?

SAMIRA
Typically 30-45% gets reclassified out of the 39-year category. And with current bonus depreciation rules, that reclassified portion can be written off ENTIRELY in Year One."""
        },
        {
            "heading": "PAGE 4 — BONUS DEPRECIATION",
            "content": """FRANK
Wait — 100% in Year One? How?

SAMIRA
Section 168(k) — Bonus Depreciation. For assets with a recovery period of 20 years or less, you can deduct 100% of the cost in the year the asset is placed in service. That means all your 5-year, 7-year, and 15-year property gets a FULL deduction in Year One.

She does the math:

SAMIRA (CONT'D)
Your $1M building, minus $100K for land = $900K depreciable basis.

Cost seg reclassification:
— 5-year property: $315K (35%)
— 15-year property: $135K (15%)
— 39-year property: $450K (50%)

Year 1 deduction with bonus depreciation:
— $315K × 100% = $315,000
— $135K × 100% = $135,000
— $450K ÷ 39 years = $11,538

Total Year 1 deduction: $461,538

FRANK
Compared to $25,641 without the study.

SAMIRA
That's an additional $435,897 in deductions moved into Year One. At your 37% marginal rate: that's $161,282 in tax savings this year.

FRANK
(stunned silence)

SAMIRA
Now you understand why every serious real estate investor does cost seg studies."""
        },
        {
            "heading": "PAGE 5 — THE BONUS DEPRECIATION PHASE-DOWN",
            "content": """SAMIRA
Important timing note. Bonus depreciation is phasing down. Here's the schedule:

She shows a chart:

SAMIRA (CONT'D)
2022: 100% bonus depreciation
2023: 80%
2024: 60%
2025: 40%
2026: 20%
2027: 0% (unless Congress extends)

So for a property placed in service in 2024, your 5-year and 15-year property gets 60% bonus depreciation in Year One, with the rest depreciated normally over the remaining life.

FRANK
That's still huge though.

SAMIRA
Absolutely. Even at 60%, your Year 1 deduction on the reclassified $450K portion would be $270K in bonus plus normal first-year depreciation on the remaining 40%. Still dramatically better than straight-line 39 years.

She leans forward.

SAMIRA (CONT'D)
But this is why timing matters. Every year the bonus percentage drops, the strategy becomes less powerful. If you're acquiring properties, front-loading purchases into higher bonus years increases the lifetime tax benefit. A property bought in 2024 at 60% bonus is more valuable from a tax standpoint than the same property bought in 2026 at 20%.

FRANK
My next acquisition was planned for 2025.

SAMIRA
At 40% bonus, still worth doing a cost seg. But if you can accelerate to 2024 — even by a month — that extra 20% bonus on $450K of reclassified property is $90K more deducted in Year One. Worth exploring."""
        },
        {
            "heading": "PAGE 6 — PASSIVE ACTIVITY RULES",
            "content": """FRANK
Can I actually USE all this depreciation? I've heard about passive loss rules.

SAMIRA
Great question. Section 469 — Passive Activity Limitations. If you're a passive investor in real estate — meaning you don't materially participate — your losses (including depreciation) can only offset passive income. You can't use them against your W-2 or active business income.

FRANK
I manage my own properties.

SAMIRA
Then you may qualify as a Real Estate Professional under Section 469(c)(7). Requirements: you spend more than 750 hours per year in real estate activities, AND more than half your working hours are in real estate. If you qualify, your rental losses are no longer passive — they can offset ANY income.

FRANK
I easily spend 1,500 hours a year on my properties.

SAMIRA
Document it. Keep a time log. Hours managing, maintaining, acquiring, analyzing — it all counts. With Real Estate Professional status and a cost seg study, you can generate $400K+ in paper losses that offset your other income. Your tax bill goes to zero — or close to it.

She pauses.

SAMIRA (CONT'D)
Even if you DON'T qualify as a Real Estate Professional, there's a $25,000 allowance for active participants with AGI under $100K, phasing out by $150K. And suspended passive losses carry forward until you sell the property — at which point they're fully released against the gain."""
        },
        {
            "heading": "PAGE 7 — THE STUDY PROCESS",
            "content": """FRANK
How does the actual cost seg study work? What do I need to do?

SAMIRA
Minimal effort on your part. Here's the process:

She lists the steps:

SAMIRA (CONT'D)
Step 1: You engage a cost segregation firm — typically a CPA firm with engineering staff, or an engineering firm with tax specialists. Cost: $8,000-15,000 for a $1M property. Scales with property value.

Step 2: They review your purchase documents — closing statement, appraisal, blueprints if available, and photos. For existing properties, they'll do a site visit.

Step 3: Their engineers break down the building component by component, assigning each to the correct asset class and recovery period. They produce a detailed report.

Step 4: Your CPA files Form 3115 — Change in Accounting Method — if you're doing this on a property you already own. This lets you catch up on all the depreciation you missed in prior years in ONE tax return. No need to amend old returns.

FRANK
Wait — I can catch up on properties I've owned for years?

SAMIRA
Section 481(a) adjustment. If you've owned a building for five years and never did a cost seg, we file Form 3115 and take the ENTIRE cumulative missed depreciation as a deduction in the current year. It's called a "catch-up" or "look-back" cost seg. You don't lose anything by having waited."""
        },
        {
            "heading": "PAGE 8 — DEPRECIATION RECAPTURE",
            "content": """FRANK
What happens when I sell the building? Do I pay back the depreciation?

SAMIRA
Yes — partially. That's depreciation recapture under Section 1250. When you sell, the IRS "recaptures" the depreciation you took and taxes it at 25% (for real property) or ordinary rates (for personal property).

FRANK
So I'm just deferring?

SAMIRA
Partially, yes. But deferral IS valuable. Three reasons:

She counts:

SAMIRA (CONT'D)
One: time value of money. A dollar saved today and invested for ten years at 7% becomes $1.97. Paying that dollar ten years from now — even at 25% — is much cheaper in present value terms.

Two: rate arbitrage. You took the deduction at 37% (your current marginal rate) and pay recapture at 25%. That's a permanent 12% rate difference.

Three: Section 1031 exchange. If you sell via a 1031 exchange — trading into a like-kind property — you defer BOTH the capital gain AND the depreciation recapture. Indefinitely. Combine cost seg with 1031 exchanges and you can cycle through properties for decades without ever triggering recapture.

FRANK
(connecting the dots)
So I do a cost seg on building one, take the big deduction, then 1031 into building two...

SAMIRA
And do another cost seg on building two. Reset the depreciation clock. Take another massive Year One deduction. Repeat every 5-10 years. It's the single most powerful legal tax reduction strategy in real estate investing."""
        },
        {
            "heading": "PAGE 9 — WHICH PROPERTIES QUALIFY",
            "content": """FRANK
Which of my seven properties should get a cost seg study?

SAMIRA
General rule of thumb: any property worth $500K or more where you plan to hold for at least a few years is a candidate. Below $500K, the study cost ($8-15K) eats too much of the benefit. Above $500K, the ROI is typically 10x to 20x the study cost.

She reviews his portfolio:

SAMIRA (CONT'D)
Your $1M commercial building: absolutely. Expected benefit: $160K+ in tax savings.
Your $750K apartment complex: yes. Expected benefit: $80-100K.
Your $400K strip mall: borderline. Let's run the numbers — it might still make sense if the personal property component is high (lots of tenant improvements).
Your three residential rentals at $200-300K each: probably not worth individual studies. But if you acquired them recently, standard cost seg shortcuts exist for residential properties under IRS guidance.

FRANK
What about the cost seg on the buildings I've owned for years?

SAMIRA
The catch-up study on your apartment complex — owned eight years — will capture all the missed accelerated depreciation from years one through eight. That could be a $200K+ deduction this year, applied through Form 3115. We should absolutely do that one.

FRANK
This is... a lot of money I've been missing.

SAMIRA
You're not alone. Most real estate investors — even sophisticated ones — leave cost segregation on the table for years. The old accountant's default of 27.5 or 39-year straight line is technically correct but strategically lazy."""
        },
        {
            "heading": "PAGE 10 — THE LESSON",
            "content": """Frank leans back, calculator in hand, running numbers.

FRANK
So across my portfolio, we're looking at potentially half a million dollars in accelerated deductions this year alone?

SAMIRA
Between the new acquisition cost seg, the catch-up studies on existing properties, and the bonus depreciation — yes. Your 2024 tax bill could be near zero. Possibly even generate a loss carryforward for next year.

She gathers her notes.

SAMIRA (CONT'D)
IRC Section 168 — Modified Accelerated Cost Recovery System. It's the depreciation framework for all tangible property. Cost segregation is just the art of applying it precisely rather than lazily. The tax code WANTS you to depreciate components over their actual useful lives. Most accountants just don't bother identifying them.

FRANK
What do I do next?

SAMIRA
I'm sending you three cost segregation firms I've vetted. Get proposals from each. The study on your $1M commercial building will take 4-6 weeks. We want it completed before your 2024 tax return is filed.

She smiles.

SAMIRA (CONT'D)
And Frank? That guy at your REIA meeting who told you about cost seg? Buy him dinner. He just saved you more money than most people earn in three years.

Frank laughs, already dialing the first firm on the list. The red numbers on his tax projection are turning green.

FADE OUT.

— END —"""
        }
    ]
}

# ═══════════════════════════════════════════════════════════════════════════════
# SCREENPLAY 8: Health Savings Account (Section 223)
# ═══════════════════════════════════════════════════════════════════════════════

SCREENPLAYS["HSA Triple Tax Benefit"] = {
    "title": "The HSA: The Triple Tax-Free Account",
    "tax_section": "IRC Section 223",
    "subtitle": "A Tax Playbook Screenplay",
    "genre": "The Loophole (Heist/Caper)",
    "filename": "screenplay_hsa.html",
    "summary": "A benefits coordinator reveals the HSA as the only account in the tax code with triple tax advantages — tax-deductible contributions, tax-free growth, AND tax-free withdrawals — making it more powerful than a Roth IRA for healthcare expenses.",
    "diagram": """
  HIGH-DEDUCTIBLE          HEALTH SAVINGS          TRIPLE TAX
  HEALTH PLAN              ACCOUNT                 ADVANTAGE
 ─────────────────     ═══════════════════     ─────────────────
 • HDHP required:     ──╲                ╱──   TAX BREAK #1:
   $1,600+ deductible   ───╲┌──────────┐╱───   • Contributions are
   (individual)          ────╳│    HSA    │╳────   tax-deductible
 • Lower premiums      ───╱└──────────┘╲───   TAX BREAK #2:
 • Catastrophic        ╱                  ╲    • Growth is tax-free
   coverage model                              TAX BREAK #3:
                                               • Withdrawals for
  2024 LIMITS:            INVESTMENT:             medical = tax-free
 ─────────────────     ═══════════════════
 • Individual: $4,150  • Invest in index       NO OTHER ACCOUNT
 • Family: $8,300        funds                  HAS ALL THREE.
 • 55+ catch-up:       • Grows like IRA         Not 401(k). Not Roth.
   + $1,000            • No RMDs ever           Only the HSA.

 ────────────────────────────────────────────────
 THE MATH (family, 25 years, never withdraw):
 $8,300/year × 25 years × 8% growth = $632,000
 Tax saved on contributions (32% rate): $66,400
 Tax on growth & withdrawals for medical: $0
 Total tax benefit: $250,000+
""",
    "pages": [
        {
            "heading": "PAGE 1 — INT. HR BENEFITS MEETING ROOM — DAY",
            "content": """FADE IN:

A corporate meeting room during open enrollment. NANCY PARK (40s, HR benefits coordinator, secretly a tax optimization nerd) is doing a small-group session. Three employees sit across from her: ALEX (30, single, healthy), JESSICA (38, married, two kids), and TOM (55, nearing retirement).

NANCY
Okay, you three opted into this session because you checked "I want to understand HSAs" on the enrollment form. So let me start with a question: what's the best retirement account in the tax code?

ALEX
401(k)?

TOM
Roth IRA?

NANCY
Wrong and wrong. It's the Health Savings Account. And I'm going to spend the next twenty minutes showing you why it's the single most tax-advantaged account Congress has ever created."""
        },
        {
            "heading": "PAGE 2 — THE TRIPLE TAX ADVANTAGE",
            "content": """NANCY
Every tax-advantaged account gets ONE or TWO tax benefits. The HSA gets THREE. No other account in the entire tax code does this.

She writes on the whiteboard:

NANCY (CONT'D)
Traditional 401(k): Tax-deductible contributions. Taxable withdrawals. TWO tax features (deduction + tax-deferred growth).

Roth IRA: Non-deductible contributions. Tax-free growth. Tax-free withdrawals. TWO tax features (tax-free growth + tax-free withdrawals).

HSA: Tax-deductible contributions. Tax-free growth. Tax-free withdrawals for medical expenses. THREE tax features. All three.

She circles "HSA" three times.

NANCY (CONT'D)
Contributions reduce your taxable income — like a 401(k). Growth is never taxed — like a Roth. And withdrawals for qualified medical expenses are completely tax-free. It's the only account where money goes in tax-free, grows tax-free, and comes out tax-free.

JESSICA
That sounds too good.

NANCY
It's Section 223 of the Internal Revenue Code. Congress created it in 2003 specifically to incentivize high-deductible health plans. The triple benefit is the carrot."""
        },
        {
            "heading": "PAGE 3 — CONTRIBUTION LIMITS AND ELIGIBILITY",
            "content": """NANCY
To be eligible, you need a High-Deductible Health Plan — HDHP. For 2024, that means a deductible of at least $1,600 for individual coverage or $3,200 for family.

ALEX
Our HDHP option has a $3,000 deductible for individual. That qualifies?

NANCY
Yes. And the contribution limits for 2024 are $4,150 for individual coverage and $8,300 for family coverage. If you're 55 or older — that's you, Tom — you get an extra $1,000 catch-up contribution.

TOM
So I could put in $9,300 this year?

NANCY
If you have family coverage, yes. And here's a bonus: if your employer contributes to your HSA, that counts toward the limit — but it ALSO avoids FICA taxes. Our company contributes $1,000 for individual and $2,000 for family coverage. That money isn't subject to Social Security or Medicare tax on either side.

JESSICA
So it's even better than a 401(k) contribution from a tax perspective?

NANCY
Yes! A 401(k) contribution avoids income tax but still incurs FICA (Social Security and Medicare). An HSA contribution through payroll deduction avoids BOTH income tax AND FICA tax. At a combined FICA rate of 7.65%, that's an additional savings of $635 for a family contributing $8,300 through payroll."""
        },
        {
            "heading": "PAGE 4 — THE STEALTH RETIREMENT ACCOUNT",
            "content": """NANCY
Now here's the strategy nobody tells you. You don't have to spend your HSA money on medical expenses this year. Or next year. Or ever — until you choose to.

ALEX
What do you mean? I thought it was for medical bills.

NANCY
It IS for medical bills. But there's no deadline on when you reimburse yourself. You can pay a medical bill out of pocket today, save the receipt, and reimburse yourself from the HSA thirty YEARS from now. Tax-free.

She lets that sink in.

NANCY (CONT'D)
The strategy: pay all medical expenses out of pocket. Let your HSA grow and compound, invested in index funds, for decades. Keep every receipt. In retirement, when you need the money, withdraw and reimburse yourself for all those accumulated medical expenses. Completely tax-free.

TOM
So it's basically a Roth IRA with even better tax treatment?

NANCY
Better. Because the contribution was tax-deductible too. A Roth gives you two of three. The HSA gives you all three — IF you use it for medical expenses. And after 65, you can use it for ANYTHING (non-medical withdrawals after 65 are just taxed as ordinary income, like a Traditional IRA — no penalty).

JESSICA
So worst case after 65, it's equivalent to a Traditional IRA. Best case, it's better than a Roth.

NANCY
Exactly right. There is no scenario where funding an HSA is the wrong move if you're eligible."""
        },
        {
            "heading": "PAGE 5 — INVESTING THE HSA",
            "content": """NANCY
Most people make the mistake of leaving their HSA in cash — a savings account earning 0.5%. Don't do that. The HSA can be invested in mutual funds, index funds, and ETFs just like a 401(k) or IRA.

She shows the math:

NANCY (CONT'D)
Family contributing $8,300 per year, invested at 8% annual return, for 25 years: approximately $632,000. If left in a cash savings account at 1%: approximately $237,000. The difference — $395,000 — is purely from investing rather than saving.

ALEX
I'm 30. If I max it for 35 years...

NANCY
$4,150 per year at 8% for 35 years: approximately $730,000. All of it tax-free when used for medical expenses. And Alex — you WILL have medical expenses in retirement. The average retired couple spends $315,000+ on healthcare costs. Your HSA could cover all of it, tax-free.

TOM
I'm 55. I've only got 10 years until Medicare.

NANCY
$9,300 per year for 10 years at 8%: approximately $145,000. Plus whatever's already in there. And don't forget — Medicare premiums, dental, vision, long-term care insurance, and most medical expenses in retirement are ALL qualified HSA expenses. You'll have no trouble spending it tax-free.

JESSICA
What about my kids' medical expenses?

NANCY
Qualified medical expenses for your spouse and dependents count too. Braces, glasses, therapy, prescriptions — all tax-free from the HSA. But remember the strategy: pay out of pocket if you can afford to, keep receipts, let the HSA grow, reimburse later."""
        },
        {
            "heading": "PAGE 6 — THE RECEIPT SHOEBOX",
            "content": """ALEX
How do I keep track of receipts for thirty years?

NANCY
Digital folders. Create a folder called "HSA Receipts" in your cloud storage. Every time you pay a medical expense out of pocket, snap a photo of the receipt or save the EOB (Explanation of Benefits) from your insurer. Include the date, amount, and type of expense.

She shows her phone.

NANCY (CONT'D)
I've been doing this for twelve years. My folder has $47,000 in accumulated medical expenses I've never reimbursed from my HSA. That's $47,000 I can withdraw tax-free ANY time I want — today, next year, or in twenty years. The HSA balance keeps growing in the meantime.

JESSICA
Is there an audit risk?

NANCY
Keep records for seven years past the withdrawal date — that's the statute of limitations. If the IRS ever asks, you show the receipt dated 2024 and the withdrawal dated 2045. The law doesn't restrict the time gap. It just requires the expense to have occurred while you were HSA-eligible.

TOM
What if I lose the receipts?

NANCY
For insurance companies and medical providers, you can typically request EOB copies going back years. For pharmacy and doctor visit copays, most health plan portals have claims history going back 5-10 years. Download those annually as backup.

NANCY (CONT'D)
The key insight: your HSA balance and your receipt folder are two separate assets. The balance is your investment. The receipts are your tax-free withdrawal tickets. Both grow over time."""
        },
        {
            "heading": "PAGE 7 — HSA VS. FSA",
            "content": """JESSICA
What's the difference between this and the FSA I've been using?

NANCY
Night and day. An FSA — Flexible Spending Account — has a "use it or lose it" provision. You must spend the money by year-end (or a small grace period). Whatever you don't spend, you forfeit to your employer. It's a terrible design.

She compares:

NANCY (CONT'D)
FSA: Use it or lose it. Limited to $3,200 (2024). Can't invest. Can't carry forward. Employer owns the unspent balance.

HSA: Rolls over forever. No expiration. Fully investable. You own it permanently — even if you change jobs. Portable, heritable, and permanent.

JESSICA
I've been using the FSA...

NANCY
Switch. During this open enrollment, drop the FSA and elect the HDHP with HSA. The HDHP premiums are typically $100-200/month less than the PPO — that savings alone covers most of your routine medical costs, and you're building a tax-free wealth account simultaneously.

ALEX
What if you have both? Can you have an HSA and FSA?

NANCY
Not a general-purpose FSA. But you CAN pair an HSA with a "Limited Purpose FSA" that covers only dental and vision. That lets you use pre-tax FSA dollars for teeth and eyes while keeping the HSA invested for everything else. Best of both worlds."""
        },
        {
            "heading": "PAGE 8 — THE NUMBERS AT RETIREMENT",
            "content": """NANCY
Let me paint the retirement picture. Jessica — you're 38, contributing $8,300/year to family HSA, for 27 years until you're 65.

She calculates:

NANCY (CONT'D)
$8,300/year × 27 years at 8% = approximately $680,000 in the HSA.

Now. Your medical expenses in retirement: Medicare Part B premiums ($175/month in today's dollars, rising with inflation), supplemental insurance, dental, vision, prescriptions, long-term care...

Conservative estimate: $400,000 in medical expenses over a 25-year retirement.

You withdraw $400,000 from the HSA to cover medical expenses: tax-free. The remaining $280,000? After age 65, you can withdraw for any purpose — it's just taxed as ordinary income, like an IRA. Or you let it keep growing and pass it to your spouse tax-free.

JESSICA
So it covers all my retirement healthcare AND leaves money over?

NANCY
If you start now, invest aggressively, and don't tap it early — yes. The HSA becomes your dedicated healthcare retirement fund. Most people fund their 401(k) and Roth but forget that healthcare is their single largest retirement expense. The HSA is purpose-built for it.

TOM
What happens to the HSA when I die?

NANCY
If you name your spouse as beneficiary: they inherit it as their own HSA. Full tax benefits continue. If a non-spouse inherits: it's distributed as taxable income. So for estate planning, name your spouse first, and consider spending it down on qualified medical expenses late in life."""
        },
        {
            "heading": "PAGE 9 — THE PAYROLL TAX BONUS",
            "content": """NANCY
One more advantage that's easy to miss. When you contribute to the HSA through payroll deduction — which our company offers — the contribution avoids FICA taxes entirely. Both the employee portion AND the employer portion.

She breaks it down:

NANCY (CONT'D)
A 401(k) contribution of $8,300 saves you income tax but NOT FICA. You still pay 7.65% on that $8,300 in Social Security and Medicare taxes. Cost: $635.

An HSA contribution of $8,300 through payroll saves you income tax AND FICA. Additional savings: $635 per year to you, plus $635 to your employer.

ALEX
That's an extra $635 per year just from HOW I contribute?

NANCY
Over 35 years at 8% growth, that $635/year difference compounds to approximately $113,000. Just from the FICA savings being reinvested. If you have the option to contribute through payroll rather than writing a personal check — always choose payroll.

TOM
What if I contribute outside of payroll?

NANCY
You can still deduct it on your tax return — Line 17 of Schedule 1. You get the income tax deduction either way. But you miss the FICA exclusion. For most employees, payroll deduction is strictly superior.

JESSICA
I'm switching to payroll contribution right now.

NANCY
(smiling)
I'll have the form for you before you leave this room."""
        },
        {
            "heading": "PAGE 10 — THE LESSON",
            "content": """Nancy caps her whiteboard marker and faces the three employees.

NANCY
Here's the priority order for your benefits enrollment:

She writes:

NANCY (CONT'D)
1. Contribute enough to your 401(k) to get the full employer match. (Free money.)
2. Max your HSA. ($4,150 individual / $8,300 family through payroll.)
3. Max your 401(k) to the $23,000 limit.
4. Backdoor Roth IRA.
5. Mega Backdoor Roth if available.

The HSA comes BEFORE maxing the 401(k). Why? Because it has three tax benefits instead of two, it avoids FICA, and it's perfectly suited for your largest retirement expense — healthcare.

TOM
I feel stupid for leaving mine in cash for ten years.

NANCY
You're not stupid — you were uninformed. The HSA is marketed as a "health spending account" when it's actually one of the most powerful investment vehicles in the tax code. It's a branding failure, not an intelligence failure.

She hands each of them a one-page summary.

NANCY (CONT'D)
IRC Section 223 — Health Savings Accounts. Triple tax-free. No RMDs. Portable. Heritable. And available to anyone with a high-deductible plan. The only catch is you have to actually invest it rather than leave it in cash. Go set up your investment elections today.

All three nod and stand, forms in hand, already mentally calculating decades of tax-free compounding.

FADE OUT.

— END —"""
        }
    ]
}

# ═══════════════════════════════════════════════════════════════════════════════
# SCREENPLAY 9: Qualified Opportunity Zones (Section 1400Z-2)
# ═══════════════════════════════════════════════════════════════════════════════

SCREENPLAYS["Opportunity Zones"] = {
    "title": "Opportunity Zones: The Capital Gains Vanishing Act",
    "tax_section": "IRC Section 1400Z-2",
    "subtitle": "A Tax Playbook Screenplay",
    "genre": "The Loophole (Heist/Caper)",
    "filename": "screenplay_opportunity_zones.html",
    "summary": "An investor with a massive capital gain discovers how Qualified Opportunity Zones let her defer the gain, and potentially eliminate taxes on ALL future appreciation — by investing in designated economically distressed communities.",
    "diagram": """
  CAPITAL GAIN EVENT       QUALIFIED OZ            TAX BENEFITS
  (Stock sale, etc.)       FUND INVESTMENT        ─────────────────
 ─────────────────     ═══════════════════     • DEFER original gain
 • Sold stock/biz     ──╲                ╱──     until 2026 (or sale)
   $500K gain           ───╲┌──────────┐╱───   • ELIMINATE tax on
 • 180 days to          ────╳│  QOZ FUND  │╳────   NEW appreciation
   invest in QOF       ───╱└──────────┘╲───     if held 10+ years
 • Invest the GAIN    ╱                  ╲    • Invest in distressed
   (not proceeds)                                communities

  INVESTMENT:              REQUIREMENTS:           ENDGAME:
 ─────────────────     ═══════════════════     ─────────────────
 • Real estate dev     • Fund must invest      • Hold 10 years
 • Business startup      90%+ in OZ property   • Sell OZ investment
 • Operating biz       • Must be "new"         • ALL appreciation
   in the zone           investment/improve      = $0 tax
                       • 180-day deadline       • Only pay on
                                                  original deferred gain

 ────────────────────────────────────────────────
 THE MATH:
 $500K gain invested in OZ fund → grows to $1.5M in 12 years
 Tax on $1M appreciation: $0 (held 10+ years)
 Tax on original $500K gain: deferred, paid 2026 (~$119K)
 Without OZ: $500K × 23.8% = $119K now + $238K on growth later
 Total tax saved: ~$238,000
""",
    "pages": [
        {
            "heading": "PAGE 1 — INT. PRIVATE INVESTMENT OFFICE — DAY",
            "content": """FADE IN:

A sleek private investment office. KATHRYN REEVES (45, sold her tech startup, sitting on $2M in capital gains) faces her advisor MARCUS HAMILTON (50s, tax attorney, specializes in alternative investments).

KATHRYN
Marcus, I sold my company six weeks ago. My gain is $2 million. My CPA says I owe $476,000 in taxes by April. Is there anything I can do?

MARCUS
You have 180 days from the date of sale to invest that gain — or a portion of it — into a Qualified Opportunity Zone Fund. If you do, you defer the tax on the original gain AND potentially eliminate all tax on the new investment's appreciation forever.

KATHRYN
Forever?

MARCUS
If you hold the Opportunity Zone investment for at least ten years, any appreciation on that investment — no matter how large — is tax-free. The basis steps up to fair market value. The gain simply vanishes from the tax system.

KATHRYN
(leaning forward)
Tell me everything."""
        },
        {
            "heading": "PAGE 2 — HOW OPPORTUNITY ZONES WORK",
            "content": """MARCUS
Congress created Opportunity Zones in the Tax Cuts and Jobs Act of 2017. The idea: incentivize investment in economically distressed communities by offering extraordinary tax benefits to investors.

He pulls up a map showing designated census tracts.

MARCUS (CONT'D)
There are approximately 8,764 designated Opportunity Zones across all 50 states. They're census tracts nominated by governors and certified by Treasury. Many are in urban areas, but some are suburban or rural.

KATHRYN
What can I invest in?

MARCUS
You invest through a Qualified Opportunity Fund — a QOF. That's a corporation or partnership organized for the purpose of investing in Opportunity Zone property. The fund must hold at least 90% of its assets in qualified OZ property.

He lists options:

MARCUS (CONT'D)
The fund can invest in:
— Real estate: new construction or substantial improvement of existing property
— Operating businesses: startups or expansions in the zone
— Both through direct ownership or through partnership/LLC interests

The most common: ground-up real estate development. Apartment buildings, mixed-use commercial, hotels, industrial facilities — all in designated zones.

KATHRYN
Can I start my own fund?

MARCUS
Absolutely. A QOF can have a single investor — you. You form an LLC, elect QOF status by filing Form 8996 with your tax return, and invest the capital gains into qualifying zone property. You don't have to join someone else's fund."""
        },
        {
            "heading": "PAGE 3 — THE DEFERRAL",
            "content": """MARCUS
Benefit number one: deferral. When you invest a capital gain into a QOF, you defer recognition of that gain. The tax isn't due until the EARLIER of: December 31, 2026, or the date you sell the QOF investment.

KATHRYN
December 31, 2026? That's coming up.

MARCUS
Yes — and this is important. The original deferral deadline was pushed back over time. For investments made now, the deferred gain will be recognized on your 2026 tax return regardless. But you'll have had the use of that tax money for the deferral period — essentially an interest-free loan from the Treasury.

She calculates:

KATHRYN
So I invest $2M now instead of paying $476K in tax. I keep $476K invested for two more years earning returns. Even at 8%, that's $38,000 in additional returns on money I'd otherwise have sent to the IRS.

MARCUS
Correct. And that's just the deferral benefit. The real power is benefit number two.

KATHRYN
Which is?

MARCUS
Elimination of tax on the appreciation."""
        },
        {
            "heading": "PAGE 4 — THE APPRECIATION EXCLUSION",
            "content": """MARCUS
Benefit number two — and this is the big one: if you hold the QOF investment for at least ten years, your basis in the QOF interest steps up to fair market value at the time you sell. That means ALL appreciation — everything the investment gained above your original invested amount — is tax-free.

He writes the scenario:

MARCUS (CONT'D)
You invest $2M into a QOF that develops apartment buildings in an Opportunity Zone. Over 12 years, the properties appreciate and generate value. The investment is now worth $5M.

Without OZ: You'd owe 23.8% on $3M of appreciation = $714,000.
With OZ (10+ year hold): Tax on $3M appreciation = $0. Basis steps up to $5M.

KATHRYN
Zero tax on three million dollars of gain.

MARCUS
Zero. Section 1400Z-2(c) says "the basis of such investment shall be equal to the fair market value of the investment" at the time of sale, if held at least 10 years. The gain simply doesn't exist for tax purposes.

KATHRYN
That's... extraordinary.

MARCUS
It's the single most generous tax incentive Congress has created for capital gains since the Roth IRA. And unlike the Roth, there's no contribution limit on how much you can invest."""
        },
        {
            "heading": "PAGE 5 — THE 180-DAY RULE",
            "content": """MARCUS
The clock is ticking. You have 180 days from the date of your gain to invest in a QOF. When exactly did you close the sale?

KATHRYN
Six weeks ago. So I have about 138 days left.

MARCUS
Plenty of time if we move now. A few clarifications on the 180-day rule: it starts from the date the gain would be recognized. For a stock sale, that's the settlement date. For a business sale, it's typically the closing date.

He pauses.

MARCUS (CONT'D)
Also important: you only need to invest the GAIN amount, not the entire proceeds. You sold your company for $3.5M with a basis of $1.5M. Your gain is $2M. You only need to invest $2M in the QOF. The other $1.5M is your basis return — no tax on that anyway.

KATHRYN
Can I invest part of the gain?

MARCUS
Yes. There's no requirement to invest 100% of the gain. If you invest $1M of the $2M gain, you defer tax on $1M and pay tax currently on the other $1M. Partial investment is perfectly acceptable.

KATHRYN
What if I can't find a qualifying investment in 180 days?

MARCUS
Then the uninvested gain is recognized normally and you pay the tax. This is why many investors use third-party QOF funds that are already capitalized and deploying — you write a check, they invest it. No need to source and develop your own deals from scratch."""
        },
        {
            "heading": "PAGE 6 — SUBSTANTIAL IMPROVEMENT",
            "content": """MARCUS
One rule that trips people up: if the QOF purchases an existing building in the zone, it must "substantially improve" it within 30 months. That means spending at least as much on improvements as the original purchase price of the building — not the land.

KATHRYN
So you can't just buy an existing building and sit on it?

MARCUS
Correct. The law requires new investment activity. You can either:
A) Build new construction on purchased or leased land, or
B) Buy an existing building and invest at least the building's purchase price in improvements within 30 months.

He gives an example:

MARCUS (CONT'D)
Say you buy a property for $1M — $400K land, $600K building. You must invest at least $600K in improvements within 30 months. If you're doing a gut renovation or major expansion, you'll hit that naturally. If you're doing light cosmetic work, you won't qualify.

KATHRYN
What about ground-up development on vacant land?

MARCUS
That automatically satisfies the requirement — you're building new, not improving existing. Ground-up is the cleanest path. And in most Opportunity Zones, there's plenty of available land or teardown properties waiting for development.

KATHRYN
The zones near my old startup have a lot of new apartment construction happening.

MARCUS
That's not a coincidence. Developers have been flocking to OZ-designated tracts since 2018. The tax benefits make projects economically viable that wouldn't otherwise pencil out."""
        },
        {
            "heading": "PAGE 7 — COMBINING WITH OTHER STRATEGIES",
            "content": """MARCUS
Here's where it gets elegant. The Opportunity Zone benefit stacks with other strategies.

He draws a flowchart:

MARCUS (CONT'D)
Strategy one: 1031 into OZ. You can't directly 1031 into an OZ fund (they're different mechanisms). But you CAN sell a property, recognize the gain, invest that gain into a QOF, and defer. If the 1031 deadline would be impossible to meet but the OZ 180-day window works — use the OZ path instead.

Strategy two: Cost segregation on OZ property. If your QOF builds a $5M apartment complex in the zone, you can still do a cost seg study and take accelerated depreciation. The OZ benefit applies to the eventual sale; cost seg gives you benefits during the hold period.

KATHRYN
Both at the same time?

MARCUS
Both at the same time. You're deferring the original gain via OZ, taking depreciation deductions on the new property during the hold, and then eliminating tax on all appreciation after 10 years. It's layered tax planning.

Strategy three: installment sales into OZ. If you sold your business with an installment note, the 180-day clock starts when each installment payment creates gain recognition. You can invest each payment's gain into the QOF as it comes in.

KATHRYN
My sale had a $500K earn-out payment due next year.

MARCUS
When that earn-out creates gain, you'll have 180 days from that recognition date to invest it in the QOF. Each gain event gets its own clock."""
        },
        {
            "heading": "PAGE 8 — RISKS AND DUE DILIGENCE",
            "content": """KATHRYN
What are the risks?

MARCUS
Let me be transparent. OZ investing has real risks beyond typical real estate or business risk.

He counts:

MARCUS (CONT'D)
One: illiquidity. You need to hold for 10 years to get the appreciation exclusion. If you need to sell at year 7, you lose the biggest benefit. Make sure this is money you truly don't need for a decade.

Two: fund quality. Many QOF funds were launched by developers with little track record, riding the OZ hype. Due diligence on the fund operator is critical. Ask for audited financials, prior development experience, and references.

Three: zone quality. Not all Opportunity Zones are equal. Some are gentrifying rapidly — great for returns. Others are stagnant — designated as distressed because they ARE distressed, and investment alone won't change that.

Four: legislative risk. Congress could modify or repeal the OZ benefits. Existing investments are likely grandfathered, but no guarantee.

Five: compliance complexity. The QOF must maintain 90% of assets in qualified OZ property. The 30-month improvement window. The annual Form 8996 testing. Miss any requirement and the tax benefits disappear.

KATHRYN
So this isn't passive investing.

MARCUS
It can be passive if you invest in a well-managed third-party fund. But you need to vet that fund thoroughly. This isn't "set it and forget it" like an index fund."""
        },
        {
            "heading": "PAGE 9 — THE EXECUTION PLAN",
            "content": """MARCUS
Here's what I recommend for your $2M gain:

He draws a pie chart:

MARCUS (CONT'D)
$1.2M → Third-party QOF specializing in multifamily development. I have three vetted operators with strong track records in OZ developments. Diversifies your risk across multiple properties and zones.

$500K → Self-directed QOF. You form your own fund and invest in a specific project you identify. More control, more work, more concentrated risk.

$300K → Reserve. Don't invest in the QOF. Pay tax on this portion now. Keep it liquid for the tax bill in 2026 on the deferred gains and for personal use.

KATHRYN
Why not invest all $2M?

MARCUS
Because in 2026, you'll owe tax on the deferred gains — roughly $338K (at 23.8% on $1.7M invested). You need liquid assets to pay that bill. Don't put yourself in a position where you own illiquid OZ investments and owe a large tax bill with no cash to pay it.

KATHRYN
Smart. And the timeline?

MARCUS
We form your self-directed QOF this week. You subscribe to the third-party fund within 30 days. Both well within your 180-day window. By year-end, you'll have Form 8997 filed reporting the deferral election, and the money will be deployed into qualifying OZ property."""
        },
        {
            "heading": "PAGE 10 — THE LESSON",
            "content": """Kathryn stands, energized rather than stressed.

KATHRYN
Six weeks ago, I was dreading a $476K tax bill. Now I'm investing that money into communities that need it and potentially eliminating tax on millions in future appreciation.

MARCUS
(nodding)
That's the genius of the OZ program. Congress aligned incentives: investors get extraordinary tax benefits, distressed communities get capital investment, and the economy gets development activity. Everyone benefits.

He walks her to the door.

MARCUS (CONT'D)
IRC Section 1400Z-2 — Qualified Opportunity Zones. Defer capital gains by investing in designated communities. Hold for ten years and all appreciation is tax-free. No dollar limit. No income restriction. Available to anyone with a realized capital gain and the discipline to invest for the long term.

KATHRYN
What's the total tax savings if everything goes right?

MARCUS
You invest $1.7M. It grows to $5M over 12 years. Tax on $3.3M of appreciation: zero. That's $785K in tax you never pay. Minus the $405K you pay on the deferred gain in 2026, your NET tax savings is approximately $380K compared to just paying capital gains tax today and investing in a taxable account.

KATHRYN
(smiling)
Three hundred eighty thousand dollars. For investing in apartment buildings.

MARCUS
For investing in apartment buildings in communities that need them. The tax code rewards building things. It punishes hoarding. You're choosing the path the code is designed to encourage.

She shakes his hand and exits, already googling Opportunity Zones near her old startup's office.

FADE OUT.

— END —"""
        }
    ]
}

# ═══════════════════════════════════════════════════════════════════════════════
# SCREENPLAY 10: Augusta Rule (Section 280A(g))
# ═══════════════════════════════════════════════════════════════════════════════

SCREENPLAYS["Augusta Rule"] = {
    "title": "The Augusta Rule: The Home Rental Loophole",
    "tax_section": "IRC Section 280A(g)",
    "subtitle": "A Tax Playbook Screenplay",
    "genre": "Tax Court True Crime",
    "filename": "screenplay_augusta_rule.html",
    "summary": "A business owner discovers she can rent her own home to her own business for meetings — tax-free income to her, deductible expense to the business — using a provision originally written for homeowners near the Masters Tournament.",
    "diagram": """
  YOUR HOME               SECTION 280A(g)         TAX RESULT
  (Personal Residence)    ═══════════════════     ─────────────────
 ─────────────────     ──╲                ╱──   FOR YOU:
 • Rent your home       ───╲┌──────────┐╱───   • Rental income is
   to YOUR business      ────╳│ 14-DAY    │╳────   TAX-FREE
 • Up to 14 days/yr    ───╱│  RULE     │╲───   • Not reported on
 • At fair market      ╱   └──────────┘  ╲      tax return at all
   rental rate                                  FOR YOUR BUSINESS:
                                               • Rental expense is
  REQUIREMENTS:            DOCUMENTATION:          DEDUCTIBLE
 ─────────────────     ═══════════════════     ─────────────────
 • Legit business use  • Board resolution      • $600/day × 14 days
 • Fair market rate    • Rental agreement        = $8,400/year
 • 14 days or fewer    • Meeting minutes       • Business deducts
 • Document purpose    • Comparable rates        $8,400
                       • Photos of setup       • You receive $8,400
                                                 tax-free

 ────────────────────────────────────────────────
 THE MATH:
 Business pays you $8,400 for 14 meeting days
 Business deduction: $8,400 (reduces taxable income)
 Your income: $8,400 (tax-free, not reported)
 Net tax savings at 32%+15.3% combined: ~$3,975/year
""",
    "pages": [
        {
            "heading": "PAGE 1 — INT. TAX COURT OBSERVATION GALLERY — DAY",
            "content": """FADE IN:

A Tax Court observation gallery. DIANA ROSS-CHEN (45, small business owner, curious) is watching a case being argued. Her tax advisor PAUL FITZGERALD (60s, retired IRS agent, now teaches small business owners) leans over and whispers.

PAUL
(whispering)
See that case? Taxpayer rented their home to their business for fourteen days. IRS challenged it. Taxpayer won. The code is crystal clear on this one.

DIANA
You told me about this — the Augusta Rule?

PAUL
Section 280A(g). Named because homeowners in Augusta, Georgia would rent their homes during the Masters Golf Tournament for thousands of dollars and not report the income. Congress specifically wrote the law to say: if you rent your personal residence for 14 days or fewer per year, the income is TAX-FREE. Not deferred. Not reduced. Excluded from income entirely.

DIANA
And I can rent my home to my OWN business?

PAUL
With proper documentation, yes. Let's step outside and I'll walk you through it."""
        },
        {
            "heading": "PAGE 2 — THE MECHANICS",
            "content": """EXT. TAX COURT STEPS — CONTINUOUS

Paul and Diana sit on a bench outside the courthouse.

PAUL
Here's how it works for business owners. Your S-Corp needs to hold a board meeting, strategic planning session, or client event. Instead of renting a hotel conference room, your S-Corp rents YOUR home for the day. At fair market rates.

DIANA
What's a fair market rate for my home?

PAUL
What would an event space of similar size and quality charge? In most markets: $500-1,000 per day for a home suitable for business meetings. Maybe more if you have a dedicated office space, large dining area, or outdoor area for events.

He pulls out a card:

PAUL (CONT'D)
Step 1: Your S-Corp board (that's you, as sole director) passes a resolution authorizing the rental of your home for up to 14 days per year at a rate of $600/day (for example).

Step 2: You and the S-Corp sign a simple rental agreement — landlord (you personally) and tenant (the S-Corp).

Step 3: The S-Corp pays you $600 per event day. It writes a check or transfers funds.

Step 4: The S-Corp deducts the $8,400 ($600 × 14 days) as a business expense — rent or facility expense.

Step 5: You do NOT report the $8,400 on your personal tax return. Section 280A(g) excludes it entirely.

DIANA
And that's... it?

PAUL
That's it. Tax-free income to you, deductible expense to the business. The net effect is a $8,400 deduction for the business and $8,400 in untaxed income for you."""
        },
        {
            "heading": "PAGE 3 — THE TAX SAVINGS",
            "content": """PAUL
Let me show you the actual tax benefit.

He writes on a notepad:

PAUL (CONT'D)
The S-Corp deducts $8,400 as a business expense. This reduces the corporation's taxable income by $8,400. At your combined federal + state marginal rate of approximately 35%, that saves about $2,940 in tax at the corporate/pass-through level.

DIANA
And the income I receive?

PAUL
Zero tax. Section 280A(g) says rental income from 14 days or fewer is not included in gross income. You don't even have to report it. It doesn't appear on your Form 1040 at all.

DIANA
So the business gets a deduction and I get tax-free money. Isn't that double-dipping?

PAUL
It's not double-dipping — it's how the code works. The business legitimately rents space and deducts it, just like renting any other venue. The tax exemption on your end is a separate provision about short-term home rentals. Two different sections of the code, each applied correctly.

He smiles.

PAUL (CONT'D)
Now, will this make you rich? No. At $8,400 per year, it's a modest benefit. But it's essentially free money — you're conducting business meetings you'd hold anyway, just holding them at home instead of a restaurant or co-working space. The incremental cost to you is zero. The tax benefit is $3,000-4,000 per year. Over 20 years? That's $60,000-80,000."""
        },
        {
            "heading": "PAGE 4 — DOCUMENTATION IS EVERYTHING",
            "content": """PAUL
Now here's where people screw it up and attract audits. DOCUMENTATION. The IRS will accept this strategy gladly — if you can prove the meetings were real.

He lists requirements:

PAUL (CONT'D)
Requirement 1: REAL business purpose. Board meetings, strategic planning, employee training, client appreciation events, partner retreats. It must be a legitimate business activity.

Requirement 2: Meeting minutes. Every event gets documented. Date, time, attendees, agenda, decisions made. This proves the meeting actually happened.

Requirement 3: Fair market rental rate. Get comparable rates from local event spaces, Airbnb for similar properties, or Peerspace. Keep the research in your files.

Requirement 4: Rental agreement. Written lease between you (personally) and the business. Specifies the dates, rate, and property address.

Requirement 5: Separate payment. The business must actually PAY you — check or bank transfer. Don't just book an accounting entry. Show the money moving.

DIANA
And if I don't have all five?

PAUL
Then you're relying on the IRS's goodwill. Which is not a strategy. The beauty of the Augusta Rule is that it's unambiguously legal WHEN DOCUMENTED PROPERLY. The risk is entirely in sloppy execution, not in the law itself."""
        },
        {
            "heading": "PAGE 5 — THE ACTUAL TAX COURT CASES",
            "content": """PAUL
Let me tell you about actual Tax Court cases that define the boundaries.

He counts on his fingers:

PAUL (CONT'D)
Case one: The taxpayer who rented their home for 14 days at $10,000 per day. The IRS challenged the rate — not the concept. The court said the rate must be reasonable. If your home isn't a $10,000/day property, don't charge $10,000/day.

Case two: The taxpayer who "rented" their home for events that never happened. No minutes, no agenda, no attendees other than themselves watching TV. The IRS reclassified it as a disguised dividend. Court agreed.

DIANA
So the meetings have to actually happen.

PAUL
Actual meetings with actual business content. You can't have 14 "board meetings" where you sit alone in your living room for ten minutes. But a quarterly strategic planning session? A holiday client appreciation dinner? A team training day? A partner retreat? Four to six legitimate events per year is completely normal for any business.

He pauses.

PAUL (CONT'D)
Case three: The taxpayer who held an annual company holiday party at their home. Court ruled: legitimate business event. Rental deductible, income tax-free. That's one event — one day — that's been blessed.

DIANA
I already host a holiday party for my clients at my home every December.

PAUL
Then you're already doing it for free. Let your S-Corp rent the home for that day — document it — and now that party generates a tax benefit. You changed nothing about the event. You just documented it properly."""
        },
        {
            "heading": "PAGE 6 — COMBINING WITH MEAL DEDUCTIONS",
            "content": """PAUL
Here's a bonus layer. When your S-Corp holds a business meeting at your home, any food and beverages served are a separate deductible business expense — 50% deductible under Section 274.

DIANA
So the rental is one deduction and the food is another?

PAUL
Correct. Rental of your home: $600 (fully deductible to the S-Corp, tax-free to you). Catering for the meeting: $300 (50% deductible = $150 deduction). Total deduction for a one-day strategy session at your home: $750.

He grins.

PAUL (CONT'D)
Compare that to renting a hotel meeting room ($500) and ordering hotel catering ($400). You'd get deductions too — but the $500 goes to Marriott, not to you tax-free. With the Augusta Rule, YOU are the venue. YOU collect the rent. The tax benefit stays in your family.

DIANA
And I can do this fourteen times a year?

PAUL
Fourteen days. Some people do bi-monthly full-day sessions. Others do one event per month. Some do fewer events at a higher daily rate. As long as the total doesn't exceed 14 days and the rate is defensible, you have flexibility.

DIANA
What counts as a "day"?

PAUL
Any portion of a day counts as a full day. A three-hour board meeting on Tuesday morning = one of your fourteen days. So don't waste days on short meetings unless necessary. Consolidate business activities into fewer full days for maximum efficiency."""
        },
        {
            "heading": "PAGE 7 — WHO THIS WORKS FOR",
            "content": """PAUL
This strategy works best for S-Corp owners, C-Corp owners, and partners in partnerships who have a home suitable for business events. It does NOT work for sole proprietors renting to themselves — you can't have a deductible expense and excludable income on the same Schedule C.

DIANA
Because there's no separate entity?

PAUL
Right. You need two distinct taxpayers: you (the homeowner) and the business (the tenant). An S-Corp, C-Corp, or partnership is a separate entity. A sole proprietorship is you. You can't rent your home to yourself.

He also notes:

PAUL (CONT'D)
This works for:
— S-Corp owners renting to their S-Corp
— LLC members renting to their multi-member LLC
— Officers of a C-Corp renting to the corporation
— Partners renting to their partnership

Doesn't work for:
— Sole proprietors (same taxpayer)
— Employees renting to their employer (different issues, imputed income)

DIANA
Good thing I elected S-Corp last year.

PAUL
This is one more reason the S-Corp structure is advantageous for business owners earning above $80K. Employment tax savings, Augusta Rule, retirement plan options — the benefits compound."""
        },
        {
            "heading": "PAGE 8 — THE 14-DAY BRIGHT LINE",
            "content": """PAUL
The magic number is 14. Not 15. Not "about two weeks." Exactly 14 days or fewer.

DIANA
What happens on day 15?

PAUL
The entire rental activity becomes taxable. Not just day 15 — ALL of it. Once you exceed 14 days, you must report all rental income on Schedule E, you can take rental deductions, and the Section 280A(g) exclusion disappears entirely.

He emphasizes:

PAUL (CONT'D)
This is a bright-line rule. There's no "reasonable" standard, no gray area, no judgment call. Fourteen days: completely tax-free. Fifteen days: fully taxable. Treat the limit as sacred.

DIANA
What if I genuinely need 16 days for business events?

PAUL
Then stop at 14 for the tax-free treatment and hold the other events at a different venue. Or reconsider whether some of those days are truly full rental days. A two-hour meeting doesn't have to consume an entire "day" if you structure it differently.

PAUL (CONT'D)
Some advisors recommend staying at 12 days to build in a safety margin. If you accidentally add an event you forgot to count, you're still under 14.

DIANA
I'll stick with monthly board meetings — twelve per year. Clean and under the limit."""
        },
        {
            "heading": "PAGE 9 — SETTING THE RATE",
            "content": """PAUL
Let's set your rate. Your home is 3,200 square feet with a dedicated home office, dining room that seats 10, and a covered patio. In your area, what do comparable event spaces charge?

DIANA
I checked Peerspace last week. Similar homes list for $150-200/hour for events.

PAUL
Good research. For a full-day meeting (8 hours), that supports $1,200-1,600/day. I'd recommend being conservative — $800/day. Defensible, documented with comparables, and it doesn't invite scrutiny.

He calculates:

PAUL (CONT'D)
$800/day × 12 days = $9,600/year tax-free income.
S-Corp deduction: $9,600.
Tax saved (S-Corp level at 35%): $3,360.
Total benefit: $9,600 in your pocket + $3,360 tax reduction = effectively $12,960 in value.

DIANA
Almost $13,000 a year for hosting meetings I'd hold anyway.

PAUL
Now multiply by 20 years — that's $260,000 in cumulative tax benefit. From a strategy that costs nothing to implement and takes 30 minutes of documentation per event.

DIANA
What comparables do I keep on file?

PAUL
Save Peerspace listings, Airbnb daily rates for homes in your zip code, and quotes from local event venues. Screenshot them annually. If audited in year five, you want to show what rates were in year five — not just current rates."""
        },
        {
            "heading": "PAGE 10 — THE LESSON",
            "content": """They stand from the bench as the Tax Court lets out for lunch.

DIANA
So the Augusta Rule is really just: if you rent your home for 14 days or fewer, the income doesn't exist for tax purposes. And if your business is the renter, it gets a deduction too.

PAUL
(nodding)
That's the whole thing. Section 280A(g) — one paragraph in the code. Written in 1976 to help homeowners near sporting events and resort areas rent their homes short-term without tax complications. Applied by savvy business owners to create a beautiful tax asymmetry: deductible on one side, excluded on the other.

He hands her a folder.

PAUL (CONT'D)
In there: a template rental agreement, a sample board resolution, a meeting minutes template, and a comparable rates worksheet. Everything you need to implement this starting next month.

DIANA
(holding the folder)
This is the kind of thing that makes me feel like the tax code was written for people who read it.

PAUL
(laughing)
It was! That's the entire point of what we do. The code is 6,000 pages long. About 1,000 of those pages are ways to REDUCE your tax. The other 5,000 are ways to COMPUTE it. Most people only ever see the computation pages. We read the reduction pages.

Diana laughs, tucks the folder under her arm, and heads toward the parking lot — already mentally scheduling her first documented board meeting at home.

FADE OUT.

— END —"""
        }
    ]
}

# ═══════════════════════════════════════════════════════════════════════════════
# SCREENPLAY 11: Charitable Remainder Trust (Section 664)
# ═══════════════════════════════════════════════════════════════════════════════

SCREENPLAYS["Charitable Remainder Trust"] = {
    "title": "The Charitable Remainder Trust: The Annuity Factory",
    "tax_section": "IRC Section 664",
    "subtitle": "A Tax Playbook Screenplay",
    "genre": "The Loophole (Heist/Caper)",
    "filename": "screenplay_charitable_remainder_trust.html",
    "summary": "A couple with a $3M concentrated stock position learns how a CRT lets them diversify without paying capital gains, receive a lifetime income stream, get an immediate charitable deduction, and benefit their favorite nonprofit at death.",
    "diagram": """
  APPRECIATED ASSET        CHARITABLE              BENEFITS TO YOU
  ($3M stock, $200K       REMAINDER TRUST          ─────────────────
   basis)                ═══════════════════       • Immediate charitable
 ─────────────────    ──╲                  ╱──     deduction (~$800K)
 • Donate stock to     ───╲ ┌────────────┐╱───   • Lifetime income
   CRT (irrevocable)   ────╳─│     CRT     │─╳──   stream (5-8%/year)
 • CRT sells stock     ───╱ └────────────┘╲───   • No capital gains
   = NO cap gains tax  ╱                    ╲      on the sale
 • Reinvests full $3M                            • Tax-free
                                                   diversification
  DURING YOUR LIFE:        AT YOUR DEATH:
 ─────────────────     ═══════════════════     TOTAL BENEFIT:
 • CRT pays you 6%    • Remainder goes to     ─────────────────
   = $180K/year          charity (tax-free)    • Avoided $667K in
 • Taxable as          • Estate tax excluded     cap gains tax
   ordinary/cap gain   • Charity gets $2M+     • $800K deduction now
 • CRT grows tax-free  • You got $4M+ in       • $4M+ lifetime income
   inside trust          lifetime income        • Charity gets rest

 ────────────────────────────────────────────────
 THE MATH:
 Sell stock directly: $2.8M gain × 23.8% = $666,400 tax
 CRT sells stock: $0 tax. Reinvests full $3M.
 CRT pays 6%/year for 25 years: $4.5M total income
 Charitable deduction (present value of remainder): ~$800K
""",
    "pages": [
        {
            "heading": "PAGE 1 — INT. ESTATE PLANNING ATTORNEY'S OFFICE — DAY",
            "content": """FADE IN:

An estate planning attorney's office lined with leather-bound books. HELEN WHITFIELD (65, retired CEO, philanthropic) and her husband RAYMOND (67, former engineer, numbers-driven) sit across from their attorney STUART COLE (55, bow tie, trust and estate specialist).

HELEN
Stuart, we have $3 million in company stock. My cost basis is $200K from when I joined as employee number twelve. We want to diversify, but our accountant says we'll owe over $660,000 in capital gains tax if we sell.

RAYMOND
That's a quarter of our stock. Gone.

STUART
What if I told you there's a way to sell that stock, pay zero capital gains tax, receive a guaranteed income stream for life, get a charitable deduction of approximately $800,000 THIS year, and leave the remainder to a charity you love?

HELEN
(exchanging a glance with Raymond)
All of those things. Simultaneously.

STUART
Section 664. The Charitable Remainder Trust. And for your situation — highly appreciated concentrated stock — it's precisely what the code was designed for."""
        },
        {
            "heading": "PAGE 2 — THE STRUCTURE",
            "content": """Stuart draws a flow diagram on his legal pad.

STUART
Here's the structure. You create an irrevocable trust — the CRT. You donate your $3M of stock to the trust. That donation gives you an immediate charitable deduction.

He continues:

STUART (CONT'D)
The trust then sells the stock. Because the CRT is a tax-exempt entity — like a charity — it pays ZERO capital gains tax on the sale. The full $3 million stays invested.

RAYMOND
Instead of $2.34 million after tax.

STUART
Exactly. The CRT reinvests the full $3M into a diversified portfolio. Then it pays you — the income beneficiaries — a fixed percentage each year for life. Let's say 6%. That's $180,000 per year.

HELEN
For how long?

STUART
For both of your lifetimes. When the surviving spouse passes, whatever remains in the trust goes to the charity you designated. The "charitable remainder" — hence the name.

RAYMOND
And we can't get the principal back?

STUART
Correct. The donation to the CRT is irrevocable. You give up ownership of the stock permanently. In exchange, you get: no capital gains tax, a charitable deduction, lifetime income, and the satisfaction of eventually funding your charity. It's a trade — and for most people with appreciated assets, the math overwhelmingly favors the trade."""
        },
        {
            "heading": "PAGE 3 — TWO TYPES: CRAT AND CRUT",
            "content": """STUART
There are two flavors. A CRAT — Charitable Remainder Annuity Trust — pays a fixed dollar amount each year. If you fund it with $3M and choose 6%, you get $180,000 per year regardless of how the investments perform.

HELEN
Fixed forever?

STUART
Fixed forever. Good in a bad market — you still get $180K. But it doesn't grow with inflation.

He draws option two:

STUART (CONT'D)
A CRUT — Charitable Remainder Unitrust — pays a fixed PERCENTAGE of the trust's value each year, revalued annually. Six percent of $3M in year one = $180K. If the trust grows to $3.5M by year three, you get 6% of $3.5M = $210K. If it drops to $2.8M, you get $168K.

RAYMOND
So the CRUT adjusts with market performance?

STUART
Right. For inflation protection and upside participation, most clients choose the CRUT. Your income grows as the portfolio grows. The trade-off: it can decrease in bad years.

HELEN
Can we set the percentage at anything?

STUART
The IRS requires: minimum 5%, maximum 50%. And there's a separate test: the present value of the charitable remainder must be at least 10% of the initial contribution. At your ages (65 and 67), a 6% payout rate easily satisfies the 10% remainder test. Higher rates — 7%, 8% — might still work but we'd need to run the calculation."""
        },
        {
            "heading": "PAGE 4 — THE TAX DEDUCTION",
            "content": """STUART
In the year you fund the CRT, you receive an immediate income tax deduction equal to the present value of the charitable remainder. That's the amount the IRS projects will eventually go to charity, discounted to present value.

RAYMOND
How do they calculate that?

STUART
Using IRS actuarial tables, the Section 7520 rate (a published interest rate), and your life expectancies. At your ages with a 6% payout rate and current 7520 rates, the charitable deduction is approximately $800,000.

He shows the impact:

STUART (CONT'D)
$800,000 deduction at your 37% marginal rate = $296,000 in federal tax savings in the year you fund the trust. If your income isn't high enough to use the full deduction this year, you carry it forward for up to five additional years.

HELEN
So we save $296K in income tax PLUS we avoided $666K in capital gains?

STUART
The capital gains avoidance is inside the trust — you don't personally avoid it; the trust (as a tax-exempt entity) doesn't owe it. But the net effect: $296K in direct tax savings via the deduction, plus the entire $660K in gains avoiding taxation because the CRT sold it. Your economic benefit is substantial.

RAYMOND
And we get income for life on top of that.

STUART
For life. Both lives. The income stream is the centerpiece — the tax benefits are the sweeteners."""
        },
        {
            "heading": "PAGE 5 — TAXATION OF THE INCOME STREAM",
            "content": """RAYMOND
How is the $180K per year taxed when we receive it?

STUART
The CRT distributions follow a "tiering" system. Four tiers, paid in order:

He lists them:

STUART (CONT'D)
Tier 1: Ordinary income first. Any dividends, interest, or ordinary income earned inside the trust comes out taxed at ordinary rates (up to 37%).

Tier 2: Capital gains next. After ordinary income is exhausted, distributions come from accumulated capital gains (taxed at 20% + 3.8% NIIT).

Tier 3: Other income. Tax-exempt income if any.

Tier 4: Return of corpus (principal). Tax-free — it's return of your contribution.

HELEN
So it's not all taxed the same?

STUART
No. In your case, the CRT will first recognize $2.8M in capital gains from selling the stock. Over time, your annual distributions will carry out those gains to you — but spread over many years at the lower capital gains rate. Eventually, once the gains are exhausted, distributions shift to ordinary income from dividends and interest.

RAYMOND
So we're spreading that $2.8M gain over 20+ years instead of paying it all at once?

STUART
Exactly. The timing of tax recognition is dramatically different. You never pay $666K in one year. Instead, a portion of each annual distribution carries some capital gain — maybe $60-80K per year over 15+ years. And meanwhile, the full $3M is working for you, growing and compounding."""
        },
        {
            "heading": "PAGE 6 — THE WEALTH REPLACEMENT TRUST",
            "content": """STUART
Now, I know what Raymond is thinking. "If the remainder goes to charity, my kids get nothing."

RAYMOND
(nodding)
That's exactly what I'm thinking.

STUART
Standard solution: a Wealth Replacement Trust. You take some of the tax savings and income from the CRT and use it to fund an Irrevocable Life Insurance Trust — an ILIT — that owns a life insurance policy on both of you.

He draws the complete picture:

STUART (CONT'D)
Year one: You fund the CRT with $3M of stock. You receive $180K/year income and $296K in tax savings. You use $30K/year of that income to pay premiums on a $3M survivorship life insurance policy inside an ILIT.

Result at death: Charity receives the CRT remainder (~$2M-3M). Your children receive $3M from the life insurance policy — estate-tax-free and income-tax-free (inside the ILIT, it's excluded from your estate).

HELEN
So our kids get the same amount they would have inherited anyway?

STUART
The same or MORE. The stock was worth $3M. Your kids would have received $3M minus estate taxes (40% above exemption) and income taxes if they sold. With the ILIT: they get $3M completely tax-free. Plus the charity gets $2-3M. Everyone wins.

RAYMOND
Including the IRS?

STUART
The IRS gets less. That's why Congress created it — to incentivize charitable giving so thoroughly that even self-interested people choose it."""
        },
        {
            "heading": "PAGE 7 — NIMCRUT: THE FLEXIBLE VERSION",
            "content": """STUART
One more variation worth knowing: the NIMCRUT — Net Income with Makeup Charitable Remainder Unitrust. It's the most flexible CRT structure.

HELEN
What's different?

STUART
A standard CRUT pays you 6% every year regardless. A NIMCRUT pays you the lesser of the stated percentage OR the trust's actual net income. If the trust earns less than 6% in a year — because you invested in growth stocks that don't pay dividends — you get less. BUT the shortfall accumulates in a "makeup account."

He shows the benefit:

STUART (CONT'D)
In years you don't need income (you're still working, collecting Social Security, etc.), the NIMCRUT invests for growth and distributes little. The makeup account grows. When you DO need income — say, at age 72 — the trust shifts to income-producing investments and pays you the current year's percentage PLUS all the accumulated makeup.

RAYMOND
So we can defer our income from the CRT to years when our tax rate is lower?

STUART
Precisely. If you fund the CRT at 65 but don't need income until 72, the trust grows tax-free for seven years with no mandatory distributions. Then at 72, when you're in a lower bracket, you turn on the income and even get the makeup amounts. Tax rate arbitrage built into the trust design.

HELEN
That's brilliant for someone retiring early but not needing the money immediately.

STUART
Exactly the use case. And the makeup provision means you never lose the right to that income — it's just deferred to when you want it."""
        },
        {
            "heading": "PAGE 8 — WHAT ASSETS TO CONTRIBUTE",
            "content": """STUART
The CRT works best with highly appreciated assets — assets where the gain is a large percentage of the value. Your stock has $2.8M in gain on $3M value — that's 93% gain. Ideal.

He lists other good candidates:

STUART (CONT'D)
Best assets for a CRT:
— Concentrated stock positions (your case)
— Appreciated real estate (avoid the capital gains and 25% depreciation recapture)
— Closely held business interests before a sale
— Cryptocurrency with massive gains
— Appreciated collectibles (normally taxed at 28%)

Less ideal:
— Cash (no capital gains benefit — just use a DAF instead)
— Assets with losses (you WANT to realize losses, not avoid them)
— Assets you might need back (CRT is irrevocable)

RAYMOND
What about our rental property?

STUART
If it's appreciated significantly and you're tired of managing it — excellent candidate. The CRT sells it, avoids both capital gains AND depreciation recapture tax (which would be 25%), and converts your illiquid real estate into a diversified income stream. No 1031 exchange timeline pressure, no new property to manage.

HELEN
We've been thinking about selling the beach house...

STUART
Let's model that as a second CRT. Different properties, different trusts, different income streams. You can have multiple CRTs, each with its own schedule and payout structure."""
        },
        {
            "heading": "PAGE 9 — COSTS AND CONSIDERATIONS",
            "content": """STUART
Let me be transparent about the costs and limitations.

He lists:

STUART (CONT'D)
Setup costs: Attorney fees for drafting the trust ($5,000-15,000). Annual administration: trustee fees (often 1% of assets), tax return preparation (Form 5227: $1,000-2,000/year).

Limitations:
— Irrevocable. You cannot get the principal back. Period.
— Must pay at least 5% annually (standard CRT, not NIMCRUT).
— The remainder value must be at least 10% at funding.
— You cannot be the sole trustee (conflict of interest). Use a corporate trustee or co-trustee.

RAYMOND
So we lose access to $3M of principal forever?

STUART
Yes. But you GAIN $180K per year for life (likely $4-5M total over your lifetimes), $296K in immediate tax savings, and avoidance of $666K in capital gains tax. The principal you "lost" generates more value than the principal you would have kept — because the compounding starts on 100% of the assets rather than 78% after tax.

HELEN
And if we need emergency access to a large sum?

STUART
That's what the other $2M in your portfolio is for. Never put ALL your assets in a CRT. Keep liquid reserves outside. The CRT is for the concentrated, appreciated portion you're ready to convert into income.

STUART (CONT'D)
The general rule: fund the CRT with assets you'd sell anyway but hesitate because of the tax hit. If you'd never sell the stock regardless of tax consequences, the CRT may not be the right vehicle."""
        },
        {
            "heading": "PAGE 10 — THE LESSON",
            "content": """Helen and Raymond look at each other — the kind of look couples have when they've been married forty years and can communicate in glances.

HELEN
(to Stuart)
Set it up. The CRUT. Six percent. Beneficiary: the medical school scholarship fund we started twenty years ago.

STUART
(smiling)
I'll have the draft trust document to you next week. We'll fund it with the stock transfer by month-end, which gives you the deduction for this tax year.

He walks them to the door.

STUART (CONT'D)
IRC Section 664 — Charitable Remainder Trusts. You eliminate capital gains on the sale. You get a massive charitable deduction. You receive income for life. And your favorite charity receives the remainder when you're done. Four benefits. One structure. And the IRS blesses every piece of it because the code was specifically written to make this work.

RAYMOND
This feels like the tax code actually working FOR us for once.

STUART
(laughing)
That's because it IS working for you. The charitable sections of the code are the most generous provisions Congress has ever written. They WANT you to give. They just reward you spectacularly for doing it through the right structure.

Helen and Raymond walk out arm in arm — lighter by $3M in stock, heavier by a lifetime of income and the knowledge that their scholarship fund will receive millions more than they ever could have given directly.

FADE OUT.

— END —"""
        }
    ]
}

# ═══════════════════════════════════════════════════════════════════════════════
# SCREENPLAY 12: Section 179 + Bonus Depreciation (The Equipment Write-Off)
# ═══════════════════════════════════════════════════════════════════════════════

SCREENPLAYS["Section 179 Deduction"] = {
    "title": "Section 179: The Equipment Write-Off",
    "tax_section": "IRC Section 179",
    "subtitle": "A Tax Playbook Screenplay",
    "genre": "The Audit (Interrogation Room)",
    "filename": "screenplay_section_179.html",
    "summary": "A small business owner facing a monster tax bill discovers she can deduct the FULL cost of business equipment and vehicles in Year One — including the infamous 'G-Wagon loophole' — turning a tax liability into a capital investment.",
    "diagram": """
  BUSINESS EQUIPMENT       SECTION 179             YEAR-ONE DEDUCTION
  PURCHASE                 ELECTION               ─────────────────
 ─────────────────     ═══════════════════     • Deduct FULL cost
 • Machinery           ──╲                ╱──    in year of purchase
 • Vehicles (6K+ GVW)  ───╲┌──────────┐╱───   • No multi-year
 • Computers/tech       ────╳│ IMMEDIATE  │╳────   depreciation needed
 • Office furniture    ───╱│ DEDUCTION │╲───   • 2024 limit: $1.22M
 • Software            ╱   └──────────┘  ╲    • Phase-out at $3.05M

  WITHOUT 179:             WITH 179:              THE VEHICLE RULE:
 ─────────────────     ═══════════════════     ─────────────────
 • $100K equipment      • $100K equipment       • Over 6,000 lbs GVW
   depreciated over      fully deducted          = full Section 179
   5-7 years             in Year 1             • Under 6,000 lbs
 • Yr 1 deduction:     • Yr 1 deduction:         = limited to $20,400
   ~$20K                 $100K                    (luxury auto limit)
 • Cash flow drag      • Immediate tax relief   • G-Wagon, Escalade,
                                                  pickup trucks OK

 ────────────────────────────────────────────────
 THE MATH:
 Buy $100K of equipment in December
 Section 179 deduction: $100K in Year 1
 Tax savings at 37% rate: $37,000
 Net cost of equipment: $63,000 (after tax benefit)
 Without 179: $37K savings spread over 5-7 years
""",
    "pages": [
        {
            "heading": "PAGE 1 — INT. ACCOUNTANT'S OFFICE — DECEMBER",
            "content": """FADE IN:

An accountant's office, December 15th. Holiday decorations on the desk. LINDA PARK (42, owns a growing construction company) sits across from her accountant, KEVIN MURPHY (50s, practical, saves his clients money).

LINDA
Kevin, you just told me I owe $87,000 in taxes this year. That's insane. My business is doing great but that bill could put me in a cash crunch.

KEVIN
Your business IS doing great. $400K in net income. That's why the bill is high. But here's my question: do you need any equipment?

LINDA
I was planning to buy a new excavator in January. And my office needs new computers. And I've been eyeing a truck.

KEVIN
Move all of that to December. Buy it this month. Before December 31st.

LINDA
Why? What difference does two weeks make?

KEVIN
About $50,000 in tax savings. Section 179 lets you deduct the FULL purchase price of business equipment in the year you buy it. If you buy $150K of equipment in December 2024, you deduct $150K from your 2024 income. Your $87K tax bill could drop to $32K.

LINDA
(standing up)
I'm going equipment shopping TODAY."""
        },
        {
            "heading": "PAGE 2 — WHAT SECTION 179 IS",
            "content": """KEVIN
Hold on — let me explain the rules so you don't accidentally buy something that doesn't qualify.

He pulls out a reference sheet:

KEVIN (CONT'D)
Section 179 allows a business to ELECT to expense — deduct immediately rather than depreciate over time — the cost of qualifying property in the year it's placed in service. Normally, equipment gets depreciated over 5, 7, or even 15 years. Section 179 accelerates that entire deduction into Year One.

LINDA
What qualifies?

KEVIN
Tangible personal property used more than 50% for business:
— Machinery and equipment
— Computers, printers, tech
— Office furniture
— Vehicles over 6,000 lbs GVWR
— Certain leasehold improvements
— Off-the-shelf software

What DOESN'T qualify:
— Real property (buildings, land) — with some exceptions for improvements
— Inventory
— Property used less than 50% for business
— Air conditioning and heating units (these are structural)

LINDA
The excavator?

KEVIN
One hundred percent qualifying. Business machinery. Full deduction in Year One."""
        },
        {
            "heading": "PAGE 3 — THE 2024 LIMITS",
            "content": """KEVIN
For 2024, the Section 179 deduction limit is $1,220,000. That's the maximum you can elect to expense in a single year.

LINDA
A million two? That's way more than I'd spend.

KEVIN
Right. For most small businesses, the limit is irrelevant — you'll never hit it. It phases out dollar-for-dollar once total equipment purchases exceed $3,050,000. So if you bought $3,150,000 in equipment, your 179 deduction would be reduced by $100K. But for typical small businesses: buy what you need, deduct it all.

He adds:

KEVIN (CONT'D)
One crucial limitation: the Section 179 deduction cannot exceed your taxable business income for the year. If your business earned $400K and you buy $500K in equipment, you can only 179 up to $400K. The remaining $100K? You can still use bonus depreciation on it — which has no income limitation.

LINDA
What's bonus depreciation?

KEVIN
Think of it as 179's bigger, less restrictive cousin. For 2024, bonus depreciation is 60% (declining from 100% in 2022). It applies to new AND used equipment, has no dollar cap, and no business income limitation. You'd typically use 179 first (full deduction if you have income), then bonus depreciation on the remainder.

LINDA
So between the two, I can write off basically anything I buy for business this year?

KEVIN
Between 179 and bonus depreciation, yes — virtually any business equipment purchased and placed in service before December 31st gets a massive first-year deduction."""
        },
        {
            "heading": "PAGE 4 — THE VEHICLE STRATEGY",
            "content": """LINDA
What about the truck? I want a heavy-duty pickup for job sites.

KEVIN
Vehicles have special rules. If the vehicle is under 6,000 pounds gross vehicle weight rating — like a sedan or small SUV — the deduction is limited by luxury auto rules: approximately $20,400 in Year One (2024), regardless of price.

LINDA
And over 6,000 pounds?

KEVIN
(smiling)
Full Section 179 deduction up to $28,900 (heavy SUVs) or UNLIMITED for vehicles over 6,000 GVW that aren't SUVs — like pickup trucks with a bed length over 6 feet. Your full-size pickup qualifies for the full purchase price.

LINDA
A $65,000 F-350?

KEVIN
$65,000 deduction in Year One. Full write-off. As long as business use is over 50%.

He pauses.

KEVIN (CONT'D)
This is the so-called "G-Wagon loophole" you hear about. A Mercedes G-Wagon weighs over 6,000 pounds GVW. An Escalade. A Range Rover. A loaded pickup. If business use exceeds 50%, the full purchase price is deductible under 179 (SUVs capped at $28,900) or bonus depreciation (60% of full price in 2024).

LINDA
My F-350 isn't an SUV — it's a truck. So full price?

KEVIN
Full price. $65,000 deduction. Your tax savings at 37%: $24,050. The government just subsidized your work truck by twenty-four thousand dollars."""
        },
        {
            "heading": "PAGE 5 — PLACED IN SERVICE",
            "content": """KEVIN
Critical concept: the equipment must be "placed in service" before December 31st. That means actually DELIVERED and READY FOR USE — not just ordered, not just paid for.

LINDA
If I order the excavator today and it's delivered January 3rd?

KEVIN
2025 deduction, not 2024. The delivery date — or more precisely, the date it's available and ready for its intended use — determines the tax year.

He emphasizes:

KEVIN (CONT'D)
For the truck: you need to take delivery before December 31st. Drive it off the lot, title it to the business, and start using it for work. If the dealer says "we'll prep it and have it ready January 2nd" — that's a 2025 deduction.

For computers and office equipment: same. Delivered, set up, and operational.

LINDA
What about financing? Do I have to pay cash?

KEVIN
No! Section 179 applies regardless of how you pay. Finance the equipment, lease-to-own, take a loan — you still deduct the full purchase price in Year One. This is one of the most powerful aspects: you can deduct $100K while only putting $10K down and financing the rest.

LINDA
So I could put $10K down on the excavator, finance $90K, and deduct the full $100K immediately?

KEVIN
Your Year One tax savings of $37K would MORE than cover the down payment. The government is effectively paying for the down payment on business equipment you need."""
        },
        {
            "heading": "PAGE 6 — THE CHRISTMAS RUSH",
            "content": """KEVIN
This is why December is the busiest month in equipment sales. Dealers know business owners are trying to get deductions into the current tax year.

LINDA
(laughing)
So there's a reason they run those "year-end clearance" ads.

KEVIN
Absolutely. And dealers are motivated to close deals before year-end too — their own quotas and bonuses depend on it. You may actually get better pricing in December than January.

He pulls up a checklist:

KEVIN (CONT'D)
Your December game plan:
1. Excavator ($100K) — order this week, confirm delivery before 12/31
2. Office computers and tech ($15K) — buy from a store with same-day availability
3. F-350 pickup ($65K) — call three dealers, take delivery this month
4. Office furniture for the expansion ($20K) — buy now, have delivered

Total Section 179 eligible: $200,000
Tax savings at 37%: $74,000
Your original tax bill: $87,000
New tax bill: approximately $13,000

LINDA
(staring)
From $87K to $13K?

KEVIN
By buying equipment you were going to buy ANYWAY — just two weeks earlier than planned. The only thing you changed was timing. The equipment need was real. The business use is real. You just made the purchase in the optimal tax year."""
        },
        {
            "heading": "PAGE 7 — THE BUSINESS USE REQUIREMENT",
            "content": """KEVIN
One rule that MUST be followed: the equipment must be used more than 50% for business. If you use that truck 60% for work and 40% personal, you deduct 60% of the cost.

LINDA
And if it drops below 50%?

KEVIN
Section 179 "recapture." The IRS takes back the deduction — you add it back to income in the year business use drops below 50%. This primarily affects vehicles that start as business but gradually become personal.

He advises:

KEVIN (CONT'D)
Documentation is key. For vehicles: keep a mileage log. Date, destination, business purpose, miles driven. There are apps — MileIQ, Everlance — that track it automatically.

For equipment: if it's at your job site or business premises, the business use is obvious. An excavator doesn't go to the grocery store. But a laptop? A phone? A truck? Those cross the personal/business line, so document the split.

LINDA
The excavator is 100% business. It lives on job sites.

KEVIN
Perfect. Full deduction, no questions. The truck — let's be realistic about business use. If you drive it to sites five days a week and personally on weekends, you might be 75-80% business. We deduct 75-80% of the price.

LINDA
I have a personal car for weekends. The truck is strictly work.

KEVIN
Even better. If you can show 100% business use — dedicated work vehicle, never personal — then 100% deduction. Keep a log to prove it."""
        },
        {
            "heading": "PAGE 8 — USED EQUIPMENT QUALIFIES TOO",
            "content": """KEVIN
Important update from 2017: Section 179 and bonus depreciation now apply to USED equipment — not just new. This is huge. Before 2017, bonus depreciation only worked for brand-new equipment. Now you can buy a used excavator at auction and still take the full first-year deduction.

LINDA
That changes things. I was looking at a used Cat 320 for $70K instead of a new one for $100K.

KEVIN
Buy the used one. Same deduction rules apply. $70K deduction in Year One. You save $30K on the purchase AND get the same tax benefit. The economics of used equipment just got dramatically better.

He adds:

KEVIN (CONT'D)
This also applies to used vehicles. Buy a two-year-old F-350 for $50K instead of a new one for $65K? Same Section 179 treatment. Full deduction.

LINDA
Is there any reason to buy new then?

KEVIN
Warranty, reliability, specific configurations — business reasons. From a pure tax standpoint, used equipment with the same deduction at a lower price is often the better mathematical choice. Unless there's a specific business reason for new, used can be financially superior.

LINDA
My estimator told me about a fleet auction next week. Three F-350s from a utility company with 40K miles.

KEVIN
If you can get one delivered and titled to your business by December 31st — do it. Lower purchase price, same Section 179 benefit, proven reliability from fleet maintenance. Win-win-win."""
        },
        {
            "heading": "PAGE 9 — LISTED PROPERTY AND RECAPTURE",
            "content": """KEVIN
Last technical point. Certain equipment is "listed property" under Section 280F — primarily vehicles and computers that could have personal use. Listed property has extra documentation requirements.

LINDA
What extra requirements?

KEVIN
You must maintain "adequate records" — contemporaneous logs showing business use. For vehicles: date, miles, business purpose. For computers: similar usage logs showing business percentage.

He warns:

KEVIN (CONT'D)
If you claim 100% business use on a vehicle and get audited, the IRS will ask for your log. No log? They'll deny the deduction and reclassify it as 50% personal at best. I've seen clients lose $30K+ in deductions because they couldn't produce a mileage log.

LINDA
(making a note)
I'm downloading that mileage app today.

KEVIN
Smart. The other recapture risk: if you sell the equipment within the first year, you may have to recapture (pay back) a portion of the deduction. The rule is complex, but the simple guidance: don't buy equipment in December for the deduction and sell it in January. Hold it for its useful life.

LINDA
I keep equipment for years. The excavator will run for a decade.

KEVIN
Then you'll never face recapture. The risk is really for people gaming the system with short-term purchases. Legitimate business equipment held for productive use? Zero issues."""
        },
        {
            "heading": "PAGE 10 — THE LESSON",
            "content": """Linda stands, already dialing her equipment dealer.

LINDA
So the bottom line: I was going to buy this equipment in January. By buying it in December instead, I save $74,000 in taxes THIS year. Same equipment. Same need. Same financing. Just different timing.

KEVIN
That's the entire lesson. Section 179 rewards action over procrastination. Every December, business owners who plan ahead save tens of thousands by making purchases they were going to make anyway — just in the right calendar year.

He packs up his files.

KEVIN (CONT'D)
IRC Section 179 — Election to Expense Certain Depreciable Business Assets. It's the most straightforward tax incentive in the code. Buy equipment for your business. Deduct it immediately. The government is essentially co-investing in your business by returning 37 cents of every dollar you spend in the form of tax savings.

LINDA
I should have been doing this every year.

KEVIN
We'll do it every year from now on. November — we project your income. December — we identify purchases that make business sense AND reduce your tax bill. It's not about buying things you don't need. It's about timing purchases you DO need to maximize the tax benefit.

He hands her a summary.

KEVIN (CONT'D)
Call me when the excavator is delivered. I'll need the invoice, delivery date, and VIN for the truck. Merry Christmas, Linda — your $87K tax bill just became a $13K tax bill.

Linda laughs, waves goodbye, and walks out into the December air, phone already ringing with the dealer's number.

FADE OUT.

— END —"""
        }
    ]
}

# ─── Ordered screenplay list ─────────────────────────────────────────────────

SCREENPLAY_ORDER = [
    "1031 Like-Kind Exchange",
    "Donor-Advised Funds",
    "Backdoor Roth IRA",
    "S-Corp Election",
    "Section 199A QBI",
    "Tax-Loss Harvesting",
    "Cost Segregation",
    "HSA Triple Tax Benefit",
    "Opportunity Zones",
    "Augusta Rule",
    "Charitable Remainder Trust",
    "Section 179 Deduction",
]


# ─── Image Generation ─────────────────────────────────────────────────────────

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def generate_header_image(index, palette, title):
    """Generate a unique header image for each screenplay."""
    width, height = 1200, 400
    accent = hex_to_rgb(palette["accent"])

    # Light background with subtle gradient
    img = Image.new('RGB', (width, height), (250, 248, 245))
    draw = ImageDraw.Draw(img)

    # Draw decorative geometric patterns based on index
    random.seed(index * 42)

    # Subtle grid lines
    for x in range(0, width, 60):
        draw.line([(x, 0), (x, height)], fill=(235, 232, 228), width=1)
    for y in range(0, height, 60):
        draw.line([(0, y), (width, y)], fill=(235, 232, 228), width=1)

    # Accent colored shapes
    shapes = ['circle', 'rect', 'diamond', 'line_burst']
    shape = shapes[index % 4]

    if shape == 'circle':
        for i in range(5, 0, -1):
            r = i * 40
            cx, cy = width // 2, height // 2
            color = (accent[0], accent[1], accent[2], int(255 * (0.1 + i * 0.05)))
            draw.ellipse([cx-r, cy-r, cx+r, cy+r], outline=accent, width=2)
    elif shape == 'rect':
        for i in range(8):
            x = random.randint(50, width - 200)
            y = random.randint(30, height - 100)
            w = random.randint(40, 150)
            h = random.randint(20, 80)
            opacity = random.randint(30, 80)
            color = (accent[0], accent[1], accent[2])
            draw.rectangle([x, y, x+w, y+h], outline=color, width=2)
    elif shape == 'diamond':
        cx, cy = width // 2, height // 2
        for i in range(6, 0, -1):
            s = i * 35
            points = [(cx, cy-s), (cx+s, cy), (cx, cy+s), (cx-s, cy)]
            draw.polygon(points, outline=accent, fill=None)
    else:  # line_burst
        cx, cy = width // 2, height // 2
        for angle in range(0, 360, 15):
            rad = math.radians(angle)
            x2 = cx + int(180 * math.cos(rad))
            y2 = cy + int(180 * math.sin(rad))
            draw.line([(cx, cy), (x2, y2)], fill=accent, width=1)

    # Add floating accent dots
    for _ in range(20):
        x = random.randint(0, width)
        y = random.randint(0, height)
        r = random.randint(3, 8)
        draw.ellipse([x-r, y-r, x+r, y+r], fill=accent)

    # Save to buffer
    buffer = BytesIO()
    img.save(buffer, format='JPEG', quality=85)
    buffer.seek(0)

    # Also save to img/ directory
    filename = SCREENPLAYS[SCREENPLAY_ORDER[index]]["filename"].replace(".html", ".jpg")
    img_path = os.path.join(OUTPUT_DIR, "img", filename)
    img.save(img_path, format='JPEG', quality=85)

    return base64.b64encode(buffer.read()).decode('utf-8')

# ─── HTML Template ────────────────────────────────────────────────────────────

def format_screenplay_content(text):
    """Format screenplay text with character names, directions, and scene directions."""
    lines = text.strip().split('\n')
    formatted = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('FADE IN:') or stripped.startswith('FADE OUT.') or stripped == '— END —':
            formatted.append(f'<span class="scene-dir">{stripped}</span>')
        elif stripped.startswith('(') and stripped.endswith(')'):
            formatted.append(f'<span class="direction">{stripped}</span>')
        elif stripped.isupper() and len(stripped) > 1 and not stripped.startswith('•') and not stripped.startswith('—') and not stripped.startswith('$') and 'CONT\'D' not in stripped and not any(c.isdigit() for c in stripped[:3]):
            # Check if it looks like a character name
            if len(stripped.split()) <= 4 and not stripped.startswith('IF') and not stripped.startswith('SO') and not stripped.startswith('BUT') and not stripped.startswith('AND') and not stripped.startswith('THE'):
                formatted.append(f'<span class="character">{stripped}</span>')
            else:
                formatted.append(stripped)
        elif '(CONT\'D)' in stripped.upper() or '(V.O.)' in stripped.upper():
            formatted.append(f'<span class="character">{stripped}</span>')
        else:
            formatted.append(stripped)
    return '\n'.join(formatted)


def generate_screenplay_html(index, key, data, palette, prev_info, next_info):
    """Generate a standalone HTML file for a screenplay."""
    accent = palette["accent"]
    accent_rgb = palette["accent_rgb"]
    num_pages = len(data["pages"])

    # Navigation
    prev_link = f'<a class="topnav-link" href="{prev_info["filename"]}" title="{prev_info["title"]}">&larr; Prev</a>' if prev_info else '<span class="topnav-link disabled"></span>'
    next_link = f'<a class="topnav-link" href="{next_info["filename"]}" title="{next_info["title"]}">Next &rarr;</a>' if next_info else '<span class="topnav-link disabled"></span>'

    # Bottom nav
    bottom_prev = f'<a class="bn-link bn-prev" href="{prev_info["filename"]}"><span class="bn-dir">&larr; Previous</span><span class="bn-title">{prev_info["title"]}</span></a>' if prev_info else '<span class="bn-link bn-prev disabled"></span>'
    bottom_next = f'<a class="bn-link bn-next" href="{next_info["filename"]}"><span class="bn-dir">Next &rarr;</span><span class="bn-title">{next_info["title"]}</span></a>' if next_info else '<span class="bn-link bn-next disabled"></span>'

    # Format pages
    pages_html = ""
    for i, page in enumerate(data["pages"]):
        content = format_screenplay_content(page["content"])
        page_break = ' style="page-break-before: always;"' if i > 0 else ''
        pages_html += f"""
        <div class="page"{page_break}>
            <div class="page-number">— {i+1} of {num_pages} —</div>
            <h2 class="page-heading">{page["heading"]}</h2>
            <div class="screenplay-content"><pre>{content}</pre></div>
        </div>
"""

    # Image filename
    img_filename = data["filename"].replace(".html", ".jpg")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
    <link rel="manifest" href="site.webmanifest">
    <meta name="theme-color" content="#faf8f5">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://tax.riskrunners.com/{data['filename']}">
    <meta property="og:title" content="{data['title']}">
    <meta property="og:description" content="A Tax Playbook screenplay — US Tax Code strategies through storytelling.">
    <meta property="og:image" content="https://tax.riskrunners.com/img/{img_filename}">
    <meta property="og:site_name" content="Tax Playbook">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{data['title']}">
    <meta name="twitter:description" content="A Tax Playbook screenplay — US Tax Code strategies through storytelling.">
    <meta name="twitter:image" content="https://tax.riskrunners.com/img/{img_filename}">
    <title>{data['title']}</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Courier+Prime:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;600;700&display=swap');
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            background: #faf8f5;
            color: #2a2a2a;
            font-family: 'Inter', sans-serif;
            line-height: 1.6;
        }}
        .topnav {{
            position: sticky;
            top: 0;
            z-index: 200;
            background: rgba(250, 248, 245, 0.95);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-bottom: 1px solid #e8e4e0;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 12px;
            gap: 8px;
        }}
        .topnav-link {{
            font-size: 0.85em;
            color: {accent};
            text-decoration: none;
            padding: 6px 14px;
            border-radius: 6px;
            transition: background 0.2s, color 0.2s;
            white-space: nowrap;
        }}
        .topnav-link:hover {{
            background: rgba({accent_rgb}, 0.1);
        }}
        .topnav-link.disabled {{
            visibility: hidden;
            pointer-events: none;
        }}
        .topnav-home {{
            font-family: 'Courier Prime', monospace;
            font-size: 0.8em;
            letter-spacing: 2px;
            text-transform: uppercase;
            color: #666;
            text-decoration: none;
            padding: 6px 14px;
            border-radius: 6px;
            transition: background 0.2s, color 0.2s;
        }}
        .topnav-home:hover {{
            background: rgba(0,0,0,0.04);
            color: #333;
        }}
        .header-image {{
            width: 100%;
            max-height: 400px;
            object-fit: cover;
            display: block;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 20px;
        }}
        .meta {{
            text-align: center;
            padding: 30px 0;
            border-bottom: 1px solid #e8e4e0;
            margin-bottom: 40px;
        }}
        .meta h1 {{
            font-size: 2.2em;
            font-weight: 700;
            color: {accent};
            margin-bottom: 10px;
            font-family: 'Inter', sans-serif;
        }}
        .meta .iso {{
            font-size: 0.95em;
            color: #888;
            letter-spacing: 2px;
            text-transform: uppercase;
        }}
        .meta .subtitle {{
            font-size: 1.1em;
            color: #999;
            margin-top: 8px;
            font-style: italic;
        }}
        .page {{
            margin-bottom: 60px;
            padding-bottom: 40px;
            border-bottom: 1px solid #ede9e5;
        }}
        .page-number {{
            text-align: center;
            color: {accent};
            font-size: 0.85em;
            letter-spacing: 3px;
            margin-bottom: 20px;
            opacity: 0.7;
        }}
        .page-heading {{
            font-family: 'Courier Prime', monospace;
            font-size: 1.1em;
            color: {accent};
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 25px;
            padding: 10px 0;
            border-left: 3px solid {accent};
            padding-left: 15px;
        }}
        .screenplay-content pre {{
            font-family: 'Courier Prime', monospace;
            font-size: 0.95em;
            line-height: 1.7;
            white-space: pre-wrap;
            word-wrap: break-word;
            color: #3a3a3a;
        }}
        .screenplay-content .character {{
            display: block;
            text-align: center;
            color: #1a1a1a;
            font-weight: 700;
            margin-top: 20px;
            margin-bottom: 2px;
            letter-spacing: 1px;
        }}
        .screenplay-content .direction {{
            display: block;
            text-align: center;
            color: #888;
            font-style: italic;
            margin-bottom: 5px;
        }}
        .screenplay-content .scene-dir {{
            display: block;
            color: {accent};
            font-weight: 700;
            margin: 15px 0;
        }}
        .toc {{
            background: #f4f1ed;
            border: 1px solid #e8e4e0;
            border-radius: 8px;
            padding: 25px 30px;
            margin-bottom: 50px;
        }}
        .toc h3 {{
            color: {accent};
            font-size: 0.9em;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 15px;
        }}
        .toc pre {{
            font-family: 'Courier Prime', monospace;
            font-size: 0.82em;
            line-height: 1.5;
            color: #555;
            white-space: pre;
            overflow-x: auto;
            margin: 0;
        }}
        .bottom-nav {{
            display: flex;
            justify-content: space-between;
            align-items: stretch;
            gap: 20px;
            margin: 60px 0 40px;
            padding-top: 40px;
            border-top: 1px solid #ede9e5;
        }}
        .bn-link {{
            display: flex;
            flex-direction: column;
            gap: 4px;
            padding: 16px 20px;
            background: #f4f1ed;
            border: 1px solid #e8e4e0;
            border-radius: 10px;
            text-decoration: none;
            color: inherit;
            flex: 1;
            transition: border-color 0.25s, background 0.25s;
        }}
        .bn-link:hover {{
            border-color: {accent};
            background: rgba({accent_rgb}, 0.05);
        }}
        .bn-link.disabled {{
            visibility: hidden;
            pointer-events: none;
        }}
        .bn-next {{ text-align: right; }}
        .bn-dir {{
            font-size: 0.8em;
            color: {accent};
            letter-spacing: 1px;
            text-transform: uppercase;
        }}
        .bn-title {{
            font-size: 0.95em;
            color: #555;
            font-weight: 600;
        }}
        .bn-home {{
            text-align: center;
            margin-bottom: 20px;
        }}
        .bn-home a {{
            font-family: 'Courier Prime', monospace;
            font-size: 0.85em;
            letter-spacing: 2px;
            text-transform: uppercase;
            color: #666;
            text-decoration: none;
            padding: 8px 20px;
            border: 1px solid #ddd;
            border-radius: 6px;
            transition: color 0.2s, border-color 0.2s;
        }}
        .bn-home a:hover {{
            color: {accent};
            border-color: {accent};
        }}
        .float-nav {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            display: flex;
            flex-direction: column;
            gap: 8px;
            z-index: 100;
        }}
        .float-nav a {{
            display: block;
            width: 40px;
            height: 40px;
            background: {accent};
            color: #fff;
            text-align: center;
            line-height: 40px;
            border-radius: 50%;
            text-decoration: none;
            font-size: 1.2em;
            opacity: 0.7;
            transition: opacity 0.2s;
        }}
        .float-nav a:hover {{ opacity: 1; }}
        .footer {{
            text-align: center;
            padding: 40px 0;
            color: #888;
            font-size: 0.85em;
            border-top: 1px solid #ede9e5;
        }}
        .footer .accent {{ color: {accent}; }}
        .footer-links {{
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 16px;
            flex-wrap: wrap;
        }}
        .footer-links a {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            color: #888;
            text-decoration: none;
            font-size: 0.85em;
            padding: 7px 14px;
            border: 1px solid #e8e4e0;
            border-radius: 8px;
            transition: color 0.2s, border-color 0.2s, background 0.2s;
        }}
        .footer-links a:hover {{
            color: {accent};
            border-color: rgba({accent_rgb},0.4);
            background: rgba({accent_rgb},0.05);
        }}
        .footer-links svg {{
            width: 15px;
            height: 15px;
            fill: currentColor;
            flex-shrink: 0;
        }}
        @media print {{
            body {{ background: #fff; color: #000; }}
            .topnav, .float-nav, .bottom-nav, .bn-home {{ display: none; }}
            .page {{ page-break-after: always; }}
        }}
        @media (max-width: 600px) {{
            .topnav {{ padding: 8px 10px; }}
            .topnav-link {{ font-size: 0.78em; padding: 6px 8px; }}
            .topnav-home {{ font-size: 0.7em; letter-spacing: 1px; }}
            .container {{ padding: 20px 14px; }}
            .meta h1 {{ font-size: 1.4em; }}
            .meta .iso {{ font-size: 0.8em; }}
            .screenplay-content pre {{ font-size: 0.82em; line-height: 1.6; }}
            .page-heading {{ font-size: 0.95em; }}
            .toc {{ padding: 18px 16px; }}
            .bottom-nav {{ flex-direction: column; }}
            .bn-next {{ text-align: left; }}
            .header-image {{ max-height: 250px; }}
        }}
    </style>
</head>
<body>
    <nav class="topnav">
        {prev_link}
        <a class="topnav-home" href="index.html">&#9670; Tax Playbook</a>
        {next_link}
    </nav>

    <img class="header-image" src="img/{img_filename}" alt="{data['title']} header image">

    <div class="container">
        <div class="meta">
            <h1>{data['title']}</h1>
            <div class="iso">{data['tax_section']}</div>
            <div class="subtitle">{data['subtitle']}</div>
        </div>

        <div class="toc">
            <h3>Tax Strategy Overview</h3>
            <pre>{data['diagram'].strip()}</pre>
        </div>

{pages_html}

        <div class="bn-home">
            <a href="index.html">&#9670; Back to Tax Playbook Home</a>
        </div>

        <div class="bottom-nav">
            {bottom_prev}
            {bottom_next}
        </div>

        <div class="footer">
            <p><span class="accent">TAX PLAYBOOK</span> — US Tax Code Strategies Through Storytelling</p>
            <p>A Risk Runners Project</p>
            <div class="footer-links">
                <a href="https://github.com/jeffy893/riskrunners/wiki" target="_blank" rel="noopener noreferrer">
                    <svg viewBox="0 0 16 16"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
                    Risk Runners Codebase
                </a>
                <a href="https://jeffersonrichards.com" target="_blank" rel="noopener noreferrer">
                    <svg viewBox="0 0 16 16"><path d="M13.6 0H2.4C1.07 0 0 1.07 0 2.4v11.2C0 14.93 1.07 16 2.4 16h11.2c1.33 0 2.4-1.07 2.4-2.4V2.4C16 1.07 14.93 0 13.6 0zM4.75 13.6H2.4V6h2.35v7.6zM3.58 5.03a1.36 1.36 0 110-2.72 1.36 1.36 0 010 2.72zM13.6 13.6h-2.35V9.92c0-.88-.02-2.01-1.23-2.01-1.23 0-1.42.96-1.42 1.95v3.74H6.25V6h2.26v1.04h.03c.31-.6 1.08-1.23 2.22-1.23 2.38 0 2.82 1.56 2.82 3.6v4.19z"/></svg>
                    Connect with the Founder
                </a>
                <a href="https://www.riskrunners.com" target="_blank" rel="noopener noreferrer">
                    <svg viewBox="0 0 16 16"><path d="M8 0a8 8 0 100 16A8 8 0 008 0zm5.3 4.7h-2.2c-.2-1-.6-1.9-1.1-2.6a6 6 0 013.3 2.6zM8 1.3c.7.8 1.2 1.9 1.5 3.4h-3C6.8 3.2 7.3 2.1 8 1.3zM1.5 9.3a6.4 6.4 0 010-2.6h2.6a13 13 0 000 2.6H1.5zm1.2 1.4h2.2c.2 1 .6 1.9 1.1 2.6a6 6 0 01-3.3-2.6zM4.9 4.7H2.7a6 6 0 013.3-2.6c-.5.7-.9 1.6-1.1 2.6zm3.1 10c-.7-.8-1.2-1.9-1.5-3.4h3c-.3 1.5-.8 2.6-1.5 3.4zm1.8-4.7H6.2a11.5 11.5 0 010-4h3.6a11.5 11.5 0 010 4zm.2 3.3c.5-.7.9-1.6 1.1-2.6h2.2a6 6 0 01-3.3 2.6zm1.4-4h2.6a6.4 6.4 0 000-2.6h-2.6a13 13 0 010 2.6z"/></svg>
                    Risk Runners Central Links
                </a>
            </div>
        </div>
    </div>

    <nav class="float-nav">
        <a href="#" title="Back to top" aria-label="Back to top">&uarr;</a>
    </nav>

    <script>
        document.querySelectorAll('.page').forEach((page, i) => {{
            page.id = 'page-' + (i + 1);
        }});
    </script>
</body>
</html>"""
    return html

# ─── Index Page Generation ────────────────────────────────────────────────────

def generate_index_html():
    """Generate the main index.html landing page."""
    cards_html = ""
    for i, key in enumerate(SCREENPLAY_ORDER):
        data = SCREENPLAYS[key]
        palette = PALETTES[i]
        accent = palette["accent"]
        accent_rgb = palette["accent_rgb"]

        cards_html += f"""
        <a class="card" href="{data['filename']}" style="border-color: rgba({accent_rgb}, 0.2);">
            <div class="card-accent" style="background: linear-gradient(90deg, {accent}, {accent}cc);"></div>
            <div class="card-body">
                <div class="card-iso" style="color: {accent};">{data['tax_section']}</div>
                <div class="card-title">{data['title'].split(': ')[1] if ': ' in data['title'] else data['title']}</div>
                <div class="card-scenario">{data['summary']}</div>
                <div class="card-footer">
                    <span class="card-pages">10 PAGES</span>
                    <span class="card-cta" style="color: {accent};">Read →</span>
                </div>
            </div>
        </a>
"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tax Playbook — US Tax Code Strategies Through Storytelling</title>
    <link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
    <link rel="manifest" href="site.webmanifest">
    <meta name="theme-color" content="#faf8f5">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://tax.riskrunners.com/">
    <meta property="og:title" content="Tax Playbook — US Tax Code Strategies Through Storytelling">
    <meta property="og:description" content="Twelve screenplays teaching real US Tax Code strategies — 1031 exchanges, Roth conversions, S-Corp elections, and more — through dramatic storytelling.">
    <meta property="og:image" content="https://tax.riskrunners.com/tax-logo.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Tax Playbook — US Tax Code Strategies Through Storytelling">
    <meta name="twitter:description" content="Twelve screenplays teaching real US Tax Code strategies through dramatic storytelling.">
    <meta name="twitter:image" content="https://tax.riskrunners.com/tax-logo.png">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Courier+Prime:wght@400;700&family=Inter:wght@300;400;600;700;900&display=swap');
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            background: #faf8f5;
            color: #3a3a3a;
            font-family: 'Inter', sans-serif;
            line-height: 1.6;
        }}
        .hero {{
            position: relative;
            min-height: 85vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 60px 20px;
            overflow: hidden;
        }}
        .hero::before {{
            content: '';
            position: absolute;
            inset: 0;
            background:
                radial-gradient(ellipse at 20% 50%, rgba(46,134,171,0.06) 0%, transparent 60%),
                radial-gradient(ellipse at 80% 50%, rgba(59,129,50,0.06) 0%, transparent 60%),
                radial-gradient(ellipse at 50% 80%, rgba(107,76,154,0.04) 0%, transparent 50%);
            pointer-events: none;
        }}
        .hero::after {{
            content: '';
            position: absolute;
            inset: 0;
            background-image:
                linear-gradient(rgba(0,0,0,0.02) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0,0,0,0.02) 1px, transparent 1px);
            background-size: 40px 40px;
            pointer-events: none;
        }}
        .hero-content {{ position: relative; z-index: 1; max-width: 800px; }}
        .hero-tag {{
            font-family: 'Courier Prime', monospace;
            font-size: 0.85em;
            letter-spacing: 4px;
            text-transform: uppercase;
            color: #2E86AB;
            margin-bottom: 20px;
        }}
        .hero h1 {{
            font-size: clamp(3em, 8vw, 5.5em);
            font-weight: 900;
            line-height: 1.05;
            letter-spacing: -2px;
            background: linear-gradient(135deg, #2a2a2a 0%, #666 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 25px;
        }}
        .hero-sub {{
            font-size: 1.25em;
            color: #777;
            max-width: 600px;
            margin: 0 auto 40px;
            font-weight: 300;
        }}
        .hero-iso {{
            font-family: 'Courier Prime', monospace;
            font-size: 0.8em;
            color: #999;
            letter-spacing: 2px;
        }}
        .scroll-hint {{
            position: absolute;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            color: #aaa;
            font-size: 0.8em;
            letter-spacing: 2px;
            text-transform: uppercase;
            animation: pulse 2s ease-in-out infinite;
        }}
        @keyframes pulse {{
            0%, 100% {{ opacity: 0.3; }}
            50% {{ opacity: 0.8; }}
        }}
        .intro {{
            max-width: 750px;
            margin: 0 auto;
            padding: 80px 20px;
            text-align: center;
        }}
        .intro h2 {{
            font-size: 1.8em;
            font-weight: 700;
            color: #2a2a2a;
            margin-bottom: 20px;
        }}
        .intro p {{
            color: #666;
            font-size: 1.05em;
            line-height: 1.8;
            margin-bottom: 15px;
        }}
        .intro .accent {{ color: #2E86AB; }}
        .grid-section {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px 100px;
        }}
        .grid-header {{
            text-align: center;
            margin-bottom: 50px;
        }}
        .grid-header h2 {{
            font-family: 'Courier Prime', monospace;
            font-size: 0.85em;
            letter-spacing: 4px;
            text-transform: uppercase;
            color: #2E86AB;
            margin-bottom: 10px;
        }}
        .grid-header p {{
            color: #888;
            font-size: 0.95em;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(min(340px, 100%), 1fr));
            gap: 24px;
        }}
        .card {{
            background: #fff;
            border: 1px solid #e8e4e0;
            border-radius: 12px;
            overflow: hidden;
            transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
            text-decoration: none;
            color: inherit;
            display: flex;
            flex-direction: column;
        }}
        .card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 12px 40px rgba(0,0,0,0.08);
        }}
        .card-accent {{
            height: 4px;
            width: 100%;
        }}
        .card-body {{
            padding: 28px 24px;
            flex: 1;
            display: flex;
            flex-direction: column;
        }}
        .card-iso {{
            font-family: 'Courier Prime', monospace;
            font-size: 0.75em;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 10px;
        }}
        .card-title {{
            font-size: 1.3em;
            font-weight: 700;
            color: #2a2a2a;
            margin-bottom: 12px;
            line-height: 1.3;
        }}
        .card-scenario {{
            font-size: 0.88em;
            color: #777;
            line-height: 1.7;
            flex: 1;
            margin-bottom: 20px;
        }}
        .card-footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 16px;
            border-top: 1px solid #ede9e5;
        }}
        .card-pages {{
            font-family: 'Courier Prime', monospace;
            font-size: 0.75em;
            color: #aaa;
            letter-spacing: 1px;
        }}
        .card-cta {{
            font-size: 0.85em;
            font-weight: 600;
            letter-spacing: 1px;
            transition: opacity 0.2s;
        }}
        .card:hover .card-cta {{ opacity: 1; }}
        .card .card-cta {{ opacity: 0.7; }}
        footer {{
            text-align: center;
            padding: 50px 20px;
            border-top: 1px solid #e8e4e0;
            color: #888;
            font-size: 0.85em;
        }}
        footer .brand {{
            font-family: 'Courier Prime', monospace;
            font-size: 1em;
            letter-spacing: 3px;
            color: #666;
            margin-bottom: 8px;
        }}
        .footer-links {{
            display: flex;
            justify-content: center;
            gap: 24px;
            margin-top: 18px;
            flex-wrap: wrap;
        }}
        .footer-links a {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            color: #888;
            text-decoration: none;
            font-size: 0.9em;
            padding: 8px 16px;
            border: 1px solid #e8e4e0;
            border-radius: 8px;
            transition: color 0.2s, border-color 0.2s, background 0.2s;
        }}
        .footer-links a:hover {{
            color: #2E86AB;
            border-color: rgba(46,134,171,0.4);
            background: rgba(46,134,171,0.05);
        }}
        .footer-links svg {{
            width: 16px;
            height: 16px;
            fill: currentColor;
            flex-shrink: 0;
        }}
        @media (max-width: 600px) {{
            .grid {{ grid-template-columns: 1fr; }}
            .hero {{ min-height: 70vh; padding: 40px 16px; }}
            .hero-sub {{ font-size: 1.05em; }}
            .intro {{ padding: 50px 16px; }}
            .intro h2 {{ font-size: 1.4em; }}
            .grid-section {{ padding: 30px 16px 60px; }}
            .card-body {{ padding: 20px 18px; }}
            .card-title {{ font-size: 1.15em; }}
            footer {{ padding: 40px 16px; }}
        }}
    </style>
</head>
<body>

<section class="hero">
    <div class="hero-content">
        <div class="hero-tag">Risk Runners Presents</div>
        <h1>Tax Playbook</h1>
        <p class="hero-sub">US Tax Code strategies — taught not in accounting offices but through audits, heists, courtrooms, and kitchen-table conversations.</p>
        <div class="hero-iso">Internal Revenue Code &bull; 12 Strategies &bull; Real Savings</div>
    </div>
    <div class="scroll-hint">&darr; Scroll to explore &darr;</div>
</section>

<section class="intro">
    <h2>The tax code is 6,000 pages. About 1,000 are ways to reduce your tax.</h2>
    <p>Most people only see the pages that compute their bill. <span class="accent">Tax Playbook</span> teaches the other pages — the ones Congress wrote specifically to incentivize saving, investing, building businesses, and giving to charity. Each screenplay drops a real IRC section into a dramatic scenario: an IRS audit, a CPA heist-planning session, or a Tax Court true crime.</p>
    <p>The strategies are real. The math is real. The characters just make it memorable.</p>
    <p>Twelve strategies. Twelve stories. All legal.</p>
</section>

<section class="grid-section" id="screenplays">
    <div class="grid-header">
        <h2>The Twelve Strategies</h2>
        <p>Click any card to read the full 10-page screenplay.</p>
    </div>
    <div class="grid">
{cards_html}
    </div>
</section>

<footer>
    <div class="brand">TAX PLAYBOOK</div>
    <p>US Tax Code Strategies — Through Storytelling</p>
    <p style="margin-top: 8px;">A Risk Runners Project</p>
    <div class="footer-links">
        <a href="https://github.com/jeffy893/riskrunners/wiki" target="_blank" rel="noopener noreferrer">
            <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
            Risk Runners Codebase
        </a>
        <a href="https://jeffersonrichards.com" target="_blank" rel="noopener noreferrer">
            <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M13.6 0H2.4C1.07 0 0 1.07 0 2.4v11.2C0 14.93 1.07 16 2.4 16h11.2c1.33 0 2.4-1.07 2.4-2.4V2.4C16 1.07 14.93 0 13.6 0zM4.75 13.6H2.4V6h2.35v7.6zM3.58 5.03a1.36 1.36 0 110-2.72 1.36 1.36 0 010 2.72zM13.6 13.6h-2.35V9.92c0-.88-.02-2.01-1.23-2.01-1.23 0-1.42.96-1.42 1.95v3.74H6.25V6h2.26v1.04h.03c.31-.6 1.08-1.23 2.22-1.23 2.38 0 2.82 1.56 2.82 3.6v4.19z"/></svg>
            Connect with the Founder
        </a>
        <a href="https://www.riskrunners.com" target="_blank" rel="noopener noreferrer">
            <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 0a8 8 0 100 16A8 8 0 008 0zm5.3 4.7h-2.2c-.2-1-.6-1.9-1.1-2.6a6 6 0 013.3 2.6zM8 1.3c.7.8 1.2 1.9 1.5 3.4h-3C6.8 3.2 7.3 2.1 8 1.3zM1.5 9.3a6.4 6.4 0 010-2.6h2.6a13 13 0 000 2.6H1.5zm1.2 1.4h2.2c.2 1 .6 1.9 1.1 2.6a6 6 0 01-3.3-2.6zM4.9 4.7H2.7a6 6 0 013.3-2.6c-.5.7-.9 1.6-1.1 2.6zm3.1 10c-.7-.8-1.2-1.9-1.5-3.4h3c-.3 1.5-.8 2.6-1.5 3.4zm1.8-4.7H6.2a11.5 11.5 0 010-4h3.6a11.5 11.5 0 010 4zm.2 3.3c.5-.7.9-1.6 1.1-2.6h2.2a6 6 0 01-3.3 2.6zm1.4-4h2.6a6.4 6.4 0 000-2.6h-2.6a13 13 0 010 2.6z"/></svg>
            Risk Runners Central Links
        </a>
    </div>
</footer>

</body>
</html>"""
    return html

# ─── Main Execution ───────────────────────────────────────────────────────────

def main():
    """Generate all screenplay HTML files and the index page."""
    print("=" * 60)
    print("TAX PLAYBOOK — Screenplay Generator")
    print("=" * 60)

    # Ensure img directory exists
    os.makedirs(os.path.join(OUTPUT_DIR, "img"), exist_ok=True)

    # Generate each screenplay
    for i, key in enumerate(SCREENPLAY_ORDER):
        data = SCREENPLAYS[key]
        palette = PALETTES[i]

        # Navigation info
        prev_info = None
        next_info = None
        if i > 0:
            prev_key = SCREENPLAY_ORDER[i - 1]
            prev_info = {"filename": SCREENPLAYS[prev_key]["filename"], "title": SCREENPLAYS[prev_key]["title"]}
        if i < len(SCREENPLAY_ORDER) - 1:
            next_key = SCREENPLAY_ORDER[i + 1]
            next_info = {"filename": SCREENPLAYS[next_key]["filename"], "title": SCREENPLAYS[next_key]["title"]}

        # Generate header image
        print(f"  [{i+1:02d}/12] Generating image for: {data['title']}")
        generate_header_image(i, palette, data["title"])

        # Generate HTML
        print(f"  [{i+1:02d}/12] Generating HTML for: {data['title']}")
        html = generate_screenplay_html(i, key, data, palette, prev_info, next_info)

        # Write file
        filepath = os.path.join(OUTPUT_DIR, data["filename"])
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"         → {data['filename']}")

    # Generate index page
    print(f"\n  Generating index.html...")
    index_html = generate_index_html()
    with open(os.path.join(OUTPUT_DIR, "index.html"), 'w', encoding='utf-8') as f:
        f.write(index_html)
    print(f"         → index.html")

    print("\n" + "=" * 60)
    print(f"  Generated 12 screenplays + index.html")
    print(f"  Output directory: {OUTPUT_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()
