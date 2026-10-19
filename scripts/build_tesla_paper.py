from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import simpleSplit
from pathlib import Path
from math import sin
P=Path("pdf/achive-002.pdf");P.parent.mkdir(parents=True,exist_ok=True)
c=canvas.Canvas(str(P),pagesize=letter)
c.setTitle("Elon Musk and the Valuation of Tesla Stock")
c.setAuthor("Achive Research Notes")
pages=[
[("Abstract","Tesla stock is shaped by current automotive and energy operations, future expectations for autonomy and artificial intelligence, and the unusually visible leadership of Elon Musk. This research note separates operating data from conditional valuation assumptions. It examines executive influence, investor narratives, option value and risks, with minimalist explanatory figures."),("1. Introduction","Tesla is an operating manufacturer and energy company but its equity also expresses investor expectations for future businesses. To understand TSLA valuation, analysts must separate cash flows already earned from technology outcomes whose probability and commercial timing remain uncertain."),("Research framework","A disciplined valuation considers observable results, company investment, the potential value of new services, competitive pressures and discount rates. The paper does not offer a buy or sell recommendation.")],
[("2. The operating business","Tesla's automotive franchise depends on production, deliveries, average selling prices, manufacturing efficiency and margins. Energy storage introduces different deployment economics. Software and future autonomous services require separate assumptions about commercialization."),("3. Selected indicators","Tesla reported 480,126 vehicle deliveries, production of 451,758 vehicles and 13.5 GWh of energy storage deployments for Q2 2026. Volumes matter but are not a substitute for revenue quality, profitability or free cash flow."),("Interpretation","Reported activity anchors the valuation to a real operating enterprise. Investors should examine automotive cost structure and energy returns independently rather than treating a single company-wide growth story as sufficient.")],
[("4. Leadership as a valuation variable","Elon Musk influences Tesla's strategy and the way investors form expectations about autonomy, robotics and AI. His visibility may strengthen confidence in bold commercial goals, but concentration around one executive also creates reputational and execution risks."),("The Stock Father","As an informal phrase in market commentary, Musk may be described as 'the Stock Father' because of his prominent role in shaping retail-investor narratives about Tesla. This is not an established financial title."),("5. A layered valuation model","An analytical approach can divide enterprise value into current businesses, adjacent opportunities, probability-weighted autonomy or AI opportunities and a risk adjustment. Each layer has different evidence requirements.")],
[("6. Automotive, energy and platform possibilities","Tesla already operates at considerable industrial scale. Its vehicles, charging ecosystem and energy-storage activities provide business lines investors can examine directly. Autonomy and robotics, by comparison, are option-like prospective businesses whose margins and adoption paths remain uncertain."),("7. Optionality and sensitivity","A valuation that assigns substantial value to future technology platforms is sensitive to probability, launch timing and the discount rate. A relatively small change in assumptions can materially change present value."),("The key issue","It is possible to find Tesla expensive on current earnings and still construct an optimistic long-term thesis. Such a thesis must show exactly which future cash flows justify the extra valuation.")],
[("8. Investor sentiment and causal inference","Public statements and product events can influence expectations, yet TSLA prices also move with interest rates, market-wide risk appetite, competitor announcements and financial results. A before-and-after chart cannot establish the isolated effect of one Musk statement without a careful event-study design."),("9. Competitive and regulatory risks","Pricing pressure, tariff exposure, battery input costs, regulatory approvals, product safety and technology reliability can all change operating economics or weaken expectations. Long-dated projects carry execution risk as well as potential upside."),("Research discipline","Analysts should distinguish confirmed information from targets, demonstrations, marketing claims and scenario assumptions. A transparent valuation makes that distinction visible.")],
[("10. Scenario framing","A conservative scenario assumes Tesla is largely valued as an automotive and energy operator. An intermediate scenario adds meaningful software monetization. A high-upside scenario includes large-scale autonomy or robotics economics. These are hypothetical cases, not forecasts."),("11. Risks and leadership concentration","Tesla's risk disclosures include competition, market conditions, manufacturing and executive dependence. Investors should consider how company execution and public perceptions jointly affect the stock's valuation premium."),("Sensitivity","The further into the future a valuation's profits occur, the more sensitive the result tends to be to financing assumptions and the discount rate.")],
[("12. Conclusion","Tesla combines observable industrial performance with an unusually influential technology narrative. Elon Musk shapes the market's perception of ambitious new businesses, but an investment assessment must evaluate each opportunity according to cash flow, execution and risk."),("References","Tesla 2025 Form 10-K; Tesla Q2 2026 Vehicle Production and Deliveries release; Tesla Q2 2026 Form 10-Q; Tesla Investor Relations. This is an independent educational research note, not investment advice."),("Final analytical principle","Separate current operations from speculative option value, report scenario assumptions openly, and avoid turning a public personality's impact on market attention into an unsupported causal assertion about daily stock returns.")]
]
def para(text,y):
 c.setFont("Times-Roman",10.6)
 for line in simpleSplit(text,"Times-Roman",10.6,490):
  c.drawString(61,y,line);y-=16
 return y-25
def diagram(kind,y):
 c.setStrokeColorRGB(.2,.2,.2);c.setLineWidth(1)
 if kind==0:
  labels=["Automotive","Energy","Autonomy","AI/Robotics"]
  for j,label in enumerate(labels):
   x=75+j*112;c.rect(x,y-65,100,46)
   c.setFont("Helvetica",9);c.drawCentredString(x+50,y-43,label)
 elif kind in [1,3,5]:
  c.line(80,y-115,80,y-8);c.line(80,y-115,535,y-115)
  last=None
  for i in range(150):
   x=88+i*2.85;t=i/149
   v=(t*t if kind==1 else (t**0.55 if kind==3 else (1-t)**1.4))
   yy=y-111+94*v
   if last:c.line(last[0],last[1],x,yy)
   last=(x,yy)
  c.setFont("Helvetica",9);c.drawString(90,y-6,["","Option value sensitivity","","Competing factors and price response","","Discount-rate sensitivity"][kind])
 else:
  labels=["Operations","Narrative","Risks"]
  for j,label in enumerate(labels):
   x=75+j*150;c.rect(x,y-75,125,55);c.setFont("Helvetica",9);c.drawCentredString(x+62,y-47,label)
   if j<2:c.line(x+126,y-48,x+149,y-48)
 c.setFont("Times-Italic",8);c.drawCentredString(310,y-137,"Minimal schematic for illustrative valuation analysis; not plotted empirical data.")
 return y-165
for i,page in enumerate(pages):
 c.setFont("Times-Roman",8);c.drawString(61,754,"Elon Musk and the Valuation of Tesla Stock");c.line(59,747,554,747)
 y=708
 if i==0:
  c.setFont("Times-Bold",18);c.drawCentredString(306,y,"Elon Musk and the Valuation of Tesla Stock");y-=25
  c.setFont("Times-Roman",10);c.drawCentredString(306,y,"Leadership, fundamentals, narrative premia, and uncertainty in TSLA");y-=20
  c.drawCentredString(306,y,"Achive Research Notes | 19 October 2026");y-=42
 for j,(title,body) in enumerate(page):
  c.setFont("Times-Bold",12);c.drawString(61,y,title);y-=20
  y=para(body,y)
  if j==1 and i>0 and y>255:y=diagram(i-1,y)
 c.line(59,40,554,40);c.setFont("Times-Italic",8);c.drawString(61,26,"Independent educational research note. Not investment advice.");c.drawRightString(550,26,str(i+1));c.showPage()
c.save()
