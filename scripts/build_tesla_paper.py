from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import simpleSplit
from pathlib import Path
P=Path("pdf/achive-002.pdf");P.parent.mkdir(parents=True,exist_ok=True)
c=canvas.Canvas(str(P),pagesize=letter);c.setTitle("Elon Musk and the Valuation of Tesla Stock");c.setAuthor("Achive Research Notes")
pages=[
[
("Abstract","Tesla, Inc. combines an operating electric-vehicle and energy-storage business with ambitious plans in autonomous driving, robotics and artificial intelligence. Elon Musk is an unusually visible leader whose actions and public statements can alter investor expectations. This note separates measurable operating results from assumptions investors embed in the share price. It presents a qualitative valuation model and recognizes that no single Musk statement provides an isolated causal explanation of TSLA price moves."),
("1. Introduction: Two Ways to Read Tesla","One can evaluate Tesla as a manufacturer with factories, production costs, customers and margins, or as a platform pursuing new businesses with potentially different economics. Both interpretations matter. The first rests on company results. The second depends on confidence in future technical, commercial and regulatory execution."),
("Research scope","The analysis draws on company disclosures available through 19 October 2026, including Tesla's 2025 Form 10-K and Q2 2026 materials. It does not treat unpublished Q3 earnings as known. The purpose is explanation, not a price forecast.")
],
[
("2. Company Economics: What Shareholders Own","Tesla stock conveys an ownership interest in Tesla, Inc., not in Elon Musk personally or any other company he leads. Automotive revenue depends on vehicle sales, price realization, costs, incentives and competition. Energy storage has separate deployment and project economics. Software and autonomy could change the business model, but revenue and margin assumptions must reflect genuine commercialization."),
("3. Reported Operating Indicators","Tesla reported 480,126 vehicle deliveries and 13.5 GWh of energy-storage deployments in Q2 2026, alongside production of 451,758 vehicles. Deliveries and deployment volumes are important but do not independently establish operating profit: product mix, prices, warranty costs, incentives, exchange rates and investment also matter."),
("4. Elon Musk as an Economic Variable","Musk's leadership affects strategic priorities, recruiting, investor attention and beliefs about Tesla's future. Such influence can be positive or negative depending on execution and public reception. Key-person concentration introduces specific risks that must enter any investment assessment.")
],
[
("5. Leadership and Narrative Premium","Investor expectations are not purely retrospective. They assign probability to future businesses such as autonomous transport and AI-enabled services. A market may price these future possibilities before cash flows exist, creating a gap between current reported results and expectations."),
("The Stock Father","In the language of market commentary, Musk may be informally called 'the Stock Father' because of his unusually visible role in retail investor narratives. The phrase is a descriptive nickname in this paper, not an established financial title or an assertion that he controls the stock market."),
("6. Valuation as a Set of Conditional Scenarios","A useful decomposition expresses enterprise value as the discounted economic value of current operations plus probability-weighted future opportunities. Automotive growth, energy capacity, autonomous driving adoption, software margins and financing costs all affect the result. Alternative scenarios should be explicitly conditional, not treated as known outcomes.")
],
[
("7. Cash Flow, Discount Rates, and Uncertainty","Equity valuation requires assumptions about future free cash flow, reinvestment, dilution, interest rates and the risk premium. Optimistic technology scenarios often depend on long-dated cash flows and therefore are highly sensitive to the discount rate. Small changes in assumptions can produce large changes in present value."),
("8. Autonomy and Robotics as Options","Autonomous driving, robotaxis and robotics may broaden Tesla's economic opportunity. But a technological demonstration differs from repeatable commercial deployment. Analysts must consider safety, regulation, unit costs, operational reliability and competition before assigning durable operating earnings."),
("9. Sentiment and Event-Study Limitations","Tesla's share price can respond to earnings releases, macroeconomic developments, competitive news and executive communication at the same time. A simple before-and-after price chart does not demonstrate that any specific Musk statement caused the movement. A rigorous event study would require an explicit identification strategy and suitable controls.")
],
[
("10. Competitive and Execution Risks","Tesla competes in a rapidly changing automotive and energy ecosystem. Pricing competition, tariffs, incentives, supplier constraints, manufacturing transitions and policy shifts affect both volume and margins. Capital expenditure on new technologies increases the importance of disciplined project evaluation."),
("11. Leadership Concentration","Dependence on a prominent executive can amplify brand identity and strategic decisiveness while also increasing succession, reputation and attention risks. Tesla's own risk disclosures discuss executive-related and share-pledging risks. Investors should interpret those disclosures as uncertainty factors rather than predictions."),
("12. An Analytical Checklist","Separate verified results from management targets. Distinguish deliveries from profitability. Explain how a future business could produce free cash flow. Vary discount rates and commercialization assumptions. Identify which risks investors can observe and which remain uncertain.")
],
[
("13. Discussion","Tesla offers a particularly clear example of how investors combine tangible operating assets with intangible expectations. The company has measurable production, delivery and storage activity. It also pursues projects whose long-term cash flows remain contingent. Musk influences how those projects are communicated and perceived, but valuation still requires explicit economic assumptions."),
("14. Conclusion","Neither present operations alone nor a dramatic vision alone provides a complete account of TSLA valuation. The defensible analytical approach separates current evidence, leadership-driven expectations, prospective cash flow, and the risks that could interrupt execution. This research note offers no recommendation to buy or sell shares."),
("References and disclosure","Primary sources: Tesla 2025 Form 10-K; Tesla Q2 2026 Vehicle Production & Deliveries report; Tesla Q2 2026 Form 10-Q; Tesla Investor Relations executive biography. Independent educational note, not investment advice.")
]
]
def block(title,body,y):
    c.setFont("Times-Bold",12);c.drawString(55,y,title);y-=21;c.setFont("Times-Roman",10.5)
    for line in simpleSplit(body,"Times-Roman",10.5,500):
        c.drawString(55,y,line);y-=15
    return y-26
for i,blocks in enumerate(pages):
    c.setFont("Times-Roman",8);c.drawString(55,752,"Elon Musk and the Valuation of Tesla Stock")
    c.line(55,746,557,746)
    y=707
    if i==0:
        c.setFont("Times-Bold",19);c.drawCentredString(306,y,"Elon Musk and the Valuation of Tesla Stock");y-=25
        c.setFont("Times-Roman",10);c.drawCentredString(306,y,"Leadership, fundamentals, narrative premia, and uncertainty in TSLA");y-=26
        c.drawCentredString(306,y,"Achive Research Notes  |  19 October 2026");y-=42
    for title,body in blocks:y=block(title,body,y)
    c.line(55,40,557,40);c.setFont("Times-Italic",8);c.drawString(55,27,"Independent educational research note. Not investment advice.");c.drawRightString(555,27,str(i+1));c.showPage()
c.save()
print(f"Created {P} ({P.stat().st_size} bytes)")
