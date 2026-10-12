# Nelson blind labeling packet

For each case, read the evidence and record in your copy of `label_sheet_TEMPLATE.csv`
what a customer success lead should do next:

- **Monitor**: keep watching; no specific recent issue needs action now.
- **Stabilize**: a specific recent issue needs a concrete fix or outreach.
- **Escalate**: executive attention is needed (compounding critical issues, a failed
  recovery, an explicit request, or large revenue at risk that is getting worse).

Add a confidence of 1 (unsure) to 3 (sure). Label on your own, without discussing cases,
and do not open `data/` or `cases.json`; they can reveal the synthetic labels. Dates are as
of each case's review date. Generator tags in notes and emails are shown as [redacted].

## H001 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Home Office
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: LATAM
- primary_region: Central America
- total_orders: 5
- total_sales: 4419.43
- total_profit: 148.25
- late_delivery_count: 10
- late_delivery_rate: 0.5
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-07-18

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O063666 | 2026-01-23 | 2026-01-25 | COMPLETE | Shipping on time | 0 | Second Class | 149.94 | 51.46 | 131.95 | 2 | 2 |  |
| O061514 | 2025-12-22 | 2025-12-27 | PROCESSING | Late delivery | 1 | Standard Class | 879.91 | 122.75 | 768.52 | 4 | 5 | Late |
| O061236 | 2025-12-18 | 2025-12-20 | PENDING | Advance shipping | 0 | Standard Class | 1199.83 | -681.74 | 1092.34 | 4 | 2 |  |
| O038226 | 2025-01-16 | 2025-01-18 | COMPLETE | Advance shipping | 0 | Standard Class | 829.85 | 217.47 | 777.16 | 4 | 2 |  |
| O008920 | 2023-11-16 | 2023-11-22 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 1359.9 | 438.31 | 1246.71 | 4 | 6 | Late |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N15704 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band Medium and support history. |
| N15706 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |
| N15705 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.5000 with category concentration in Fishing. |
| N15703 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E22805 | TH-C001704-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E22803 | TH-C001704-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E22802 | TH-C001704-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL007568 | O061514 | 2025-12-22 | carrier_delay | High | Carrier route delay | Open |
| FUL008941 | O008920 | 2023-11-16 | carrier_delay | High | Carrier route delay | Open |

## H002 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Home Office
- customer_country: EE. UU.
- customer_state: WI
- customer_city: Milwaukee
- primary_market: Europe
- primary_region: Southern Europe
- total_orders: 7
- total_sales: 4461.52
- total_profit: -6.33
- late_delivery_count: 12
- late_delivery_rate: 0.5
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-08-08
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O065082 | 2026-02-13 | 2026-02-16 | PENDING_PAYMENT | Advance shipping | 0 | Standard Class | 749.95 | 198.31 | 694.45 | 4 | 3 |  |
| O043308 | 2025-04-01 | 2025-04-03 | COMPLETE | Late delivery | 1 | First Class | 539.94 | 143.57 | 445.75 | 1 | 2 | Late |
| O029083 | 2024-09-05 | 2024-09-09 | PENDING | Late delivery | 1 | Second Class | 769.92 | -43.45 | 655.63 | 2 | 4 | Late |
| O028149 | 2024-08-22 | 2024-08-27 | CANCELED | Shipping canceled | 0 | Second Class | 739.92 | -71.86 | 674.32 | 2 | 5 | Canceled |
| O018450 | 2024-04-03 | 2024-04-09 | CLOSED | Late delivery | 1 | Standard Class | 619.92 | 125.83 | 568.92 | 4 | 6 | Late |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N15240 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Escalation summary for the customer: protect revenue, close open issues, and document human review. |
| N15234 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N15239 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Monitor whether the next interaction with the customer resolves the current [redacted] thread. |
| N15238 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer-success owner should align response tone with [redacted] scenario. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E22014 | TH-C001615-[redacted] | 14 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E22012 | TH-C001615-[redacted] | 12 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E22011 | TH-C001615-[redacted] | 11 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E22010 | TH-C001615-[redacted] | 10 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E22008 | TH-C001615-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL004951 | O043308 | 2025-04-01 | carrier_delay | High | Carrier route delay | Open |
| FUL002906 | O029083 | 2024-09-05 | carrier_delay | High | Carrier route delay | Open |
| FUL002767 | O028149 | 2024-08-22 | cancellation_review | Medium | Customer or fulfillment cancellation | Closed |
| FUL001288 | O018450 | 2024-04-03 | carrier_delay | High | Carrier route delay | Open |
| FUL000997 | O016578 | 2024-03-06 | carrier_delay | High | Carrier route delay | Open |

## H003 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Home Office
- customer_country: EE. UU.
- customer_state: NY
- customer_city: Rochester
- primary_market: Europe
- primary_region: South America
- total_orders: 7
- total_sales: 4249.52
- total_profit: 910.11
- late_delivery_count: 20
- late_delivery_rate: 0.8333
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-05-01

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O058306 | 2025-11-06 | 2025-11-08 | COMPLETE | Late delivery | 1 | First Class | 759.85 | 127.43 | 681.86 | 1 | 2 | Late |
| O038788 | 2025-01-25 | 2025-01-29 | COMPLETE | Late delivery | 1 | Second Class | 739.95 | 239.36 | 647.55 | 2 | 4 | Late |
| O035579 | 2024-12-09 | 2024-12-14 | COMPLETE | Late delivery | 1 | Standard Class | 619.94 | 207.57 | 590.94 | 4 | 5 | Late |
| O019300 | 2024-04-15 | 2024-04-21 | PENDING_PAYMENT | Late delivery | 1 | Second Class | 319.95 | 145.49 | 309.15 | 2 | 6 | Late |
| O012664 | 2024-01-09 | 2024-01-14 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 829.94 | 210.06 | 727.14 | 4 | 5 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T6213 | 2026-01-15 | Billing inquiry | Installation support | I've recently set up my {product_purchased}, but it fails to connect to any available networks. What steps should I take to troubleshoot this issue?  Update:… | Closed | High | Chat | Right site wall stage particularly government long common. | 4.8 | 4.0 | Positive |
| T6215 | 2025-06-18 | Product inquiry | Peripheral compatibility | I'm having an issue with the {product_purchased}. Please assist. I won't need this because I don't sell anything else, but can get on the phone and get it back… | Open | High | Social media |  |  |  | Neutral |
| T6185 | 2025-02-18 | Technical issue | Battery life | I'm having an issue with the {product_purchased}. Please assist.  We can't find your name. Contact Us  Please let us know if you know the address below  … | Pending | High | Chat |  |  |  | Neutral |
| T6212 | 2024-09-05 | Cancellation request | Product recommendation | I'm having an issue with the {product_purchased}. Please assist.  Please contact me.   Your payment confirmation will allow us to continue your transactio… | Open | High | Phone |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N16962 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Men's Footwear. |
| N16963 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N16964 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band High and support history. |
| N16965 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.8333 with category concentration in Men's Footwear. |
| N16966 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E24952 | TH-C001959-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E24951 | TH-C001959-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E24950 | TH-C001959-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E24949 | TH-C001959-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E24948 | TH-C001959-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL007122 | O058306 | 2025-11-06 | carrier_delay | High | Carrier route delay | Open |
| FUL004285 | O038788 | 2025-01-25 | carrier_delay | High | Carrier route delay | Open |
| FUL003832 | O035579 | 2024-12-09 | carrier_delay | High | Carrier route delay | Open |
| FUL001416 | O019300 | 2024-04-15 | carrier_delay | High | Carrier route delay | Open |
| FUL000422 | O012664 | 2024-01-09 | carrier_delay | High | Carrier route delay | Open |

## H004 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Home Office
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: Pacific Asia
- primary_region: East of USA
- total_orders: 7
- total_sales: 4940.7
- total_profit: 863.53
- late_delivery_count: 16
- late_delivery_rate: 0.64
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-09-27
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O068546 | 2026-04-04 | 2026-04-06 | PENDING_PAYMENT | Advance shipping | 0 | Standard Class | 129.99 | 33.8 | 129.99 | 4 | 2 |  |
| O044949 | 2025-04-25 | 2025-04-30 | CLOSED | Late delivery | 1 | Standard Class | 599.95 | 247.98 | 519.95 | 4 | 5 | Late |
| O039047 | 2025-01-28 | 2025-01-29 | COMPLETE | Late delivery | 1 | Same Day | 375.0 | 84.33 | 357.0 | 0 | 1 | Late |
| O037669 | 2025-01-08 | 2025-01-13 | PENDING_PAYMENT | Late delivery | 1 | Second Class | 1319.89 | 421.7 | 1248.29 | 2 | 5 | Late |
| O025897 | 2024-07-21 | 2024-07-21 | COMPLETE | Shipping on time | 0 | Same Day | 615.98 | 140.24 | 601.32 | 0 | 0 |  |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N12260 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E16950 | TH-C001031-[redacted] | 12 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E16949 | TH-C001031-[redacted] | 11 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E16948 | TH-C001031-[redacted] | 10 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E16947 | TH-C001031-[redacted] | 9 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E16944 | TH-C001031-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL005167 | O044949 | 2025-04-25 | carrier_delay | High | Carrier route delay | Open |
| FUL004320 | O039047 | 2025-01-28 | carrier_delay | High | Carrier route delay | Open |
| FUL004134 | O037669 | 2025-01-08 | carrier_delay | High | Carrier route delay | Open |
| FUL005957 | O005019 | 2023-09-20 | carrier_delay | High | Carrier route delay | Open |

## H005 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: EE. UU.
- customer_state: OR
- customer_city: Portland
- primary_market: Europe
- primary_region: Western Europe
- total_orders: 10
- total_sales: 6464.99
- total_profit: 1150.57
- late_delivery_count: 23
- late_delivery_rate: 0.697
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-07-01

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O062528 | 2026-01-06 | 2026-01-10 | ON_HOLD | Shipping on time | 0 | Standard Class | 609.91 | 205.25 | 518.03 | 4 | 4 |  |
| O054990 | 2025-09-18 | 2025-09-24 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 299.98 | 72.54 | 278.98 | 4 | 6 | Late |
| O048962 | 2025-06-22 | 2025-06-25 | PENDING_PAYMENT | Late delivery | 1 | Second Class | 649.84 | 208.54 | 587.86 | 2 | 3 | Late |
| O041119 | 2025-02-28 | 2025-03-05 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 947.87 | 133.14 | 838.48 | 4 | 5 | Late |
| O039181 | 2025-01-30 | 2025-02-01 | PROCESSING | Advance shipping | 0 | Standard Class | 249.97 | 110.05 | 229.27 | 4 | 2 |  |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N8068 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |
| N8065 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E9812 | TH-C000210-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E9811 | TH-C000210-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E9810 | TH-C000210-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E9809 | TH-C000210-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E9808 | TH-C000210-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL006632 | O054990 | 2025-09-18 | carrier_delay | High | Carrier route delay | Open |
| FUL005774 | O048962 | 2025-06-22 | carrier_delay | High | Carrier route delay | Open |
| FUL004625 | O041119 | 2025-02-28 | carrier_delay | High | Carrier route delay | Open |
| FUL002180 | O024355 | 2024-06-28 | carrier_delay | High | Carrier route delay | Open |
| FUL001162 | O017709 | 2024-03-23 | carrier_delay | High | Carrier route delay | Open |

## H006 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Corporate
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: Europe
- primary_region: Western Europe
- total_orders: 7
- total_sales: 5016.4
- total_profit: 997.77
- late_delivery_count: 10
- late_delivery_rate: 0.4
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-08-07
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O065058 | 2026-02-12 | 2026-02-16 | ON_HOLD | Shipping on time | 0 | Standard Class | 817.93 | 303.99 | 774.23 | 4 | 4 |  |
| O063669 | 2026-01-23 | 2026-01-28 | PENDING | Late delivery | 1 | Standard Class | 825.98 | 263.83 | 709.96 | 4 | 5 | Late |
| O054916 | 2025-09-17 | 2025-09-19 | COMPLETE | Shipping on time | 0 | Second Class | 737.88 | 223.1 | 630.59 | 2 | 2 |  |
| O017883 | 2024-03-26 | 2024-03-30 | CLOSED | Late delivery | 1 | Second Class | 639.94 | 58.83 | 579.94 | 2 | 4 | Late |
| O011327 | 2023-12-21 | 2023-12-23 | COMPLETE | Late delivery | 1 | First Class | 824.91 | -79.34 | 680.67 | 1 | 2 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T5100 | 2024-09-15 | Technical issue | Hardware issue | I'm having an issue with the {product_purchased}. Please assist.  Thank you for your visit. I've noticed a peculiar error message popping up on my {product_p… | Pending | Low | Chat |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N11927 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Escalation summary for the customer: protect revenue, close open issues, and document human review. |
| N11924 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |
| N11921 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E16374 | TH-C000965-[redacted] | 14 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E16372 | TH-C000965-[redacted] | 12 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E16370 | TH-C000965-[redacted] | 10 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E16368 | TH-C000965-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E16365 | TH-C000965-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL007864 | O063669 | 2026-01-23 | carrier_delay | High | Carrier route delay | Open |
| FUL001191 | O017883 | 2024-03-26 | carrier_delay | High | Carrier route delay | Open |
| FUL000208 | O011327 | 2023-12-21 | carrier_delay | High | Carrier route delay | Open |

## H007 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Corporate
- customer_country: EE. UU.
- customer_state: CA
- customer_city: Alhambra
- primary_market: LATAM
- primary_region: Western Europe
- total_orders: 7
- total_sales: 5113.57
- total_profit: 1326.01
- late_delivery_count: 20
- late_delivery_rate: 0.7692
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-09-09

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O067302 | 2026-03-17 | 2026-03-20 | COMPLETE | Advance shipping | 0 | Standard Class | 599.98 | 110.7 | 526.98 | 4 | 3 |  |
| O055720 | 2025-09-29 | 2025-10-05 | COMPLETE | Late delivery | 1 | Standard Class | 884.95 | -79.54 | 781.35 | 4 | 6 | Late |
| O053255 | 2025-08-24 | 2025-08-26 | COMPLETE | Late delivery | 1 | First Class | 573.97 | 233.07 | 504.55 | 1 | 2 | Late |
| O036295 | 2024-12-19 | 2024-12-25 | COMPLETE | Late delivery | 1 | Standard Class | 1529.78 | 560.69 | 1281.62 | 4 | 6 | Late |
| O030742 | 2024-09-29 | 2024-10-01 | COMPLETE | Late delivery | 1 | First Class | 824.93 | 251.91 | 731.69 | 1 | 2 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T6754 | 2025-08-02 | Product inquiry | Refund request | I'm having an issue with the {product_purchased}. Please assist.  This is very frustrating for me. I'm a girl and I make my own food, as well as have a girlf… | Open | Medium | Social media |  |  |  | Neutral |
| T6745 | 2024-11-21 | Billing inquiry | Software bug | I'm having an issue with the {product_purchased}. Please assist. I've tried using different cables, adapters, or peripherals with my {product_purchased}, but t… | Pending | Medium | Chat |  |  |  | Neutral |
| T5248 | 2024-05-24 | Billing inquiry | Hardware issue | I've accidentally deleted important data from my {product_purchased}. Is there any way to recover the deleted files? I need them urgently. — Donald J. Trump (@… | Open | Medium | Chat |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N11566 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Women's Apparel. |
| N11567 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N11568 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band High and support history. |
| N11569 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.7692 with category concentration in Women's Apparel. |
| N11570 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E15762 | TH-C000893-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E15761 | TH-C000893-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E15760 | TH-C000893-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E15759 | TH-C000893-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E15758 | TH-C000893-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL006739 | O055720 | 2025-09-29 | carrier_delay | High | Carrier route delay | Open |
| FUL006394 | O053255 | 2025-08-24 | carrier_delay | High | Carrier route delay | Open |
| FUL003932 | O036295 | 2024-12-19 | carrier_delay | High | Carrier route delay | Open |
| FUL003150 | O030742 | 2024-09-29 | carrier_delay | High | Carrier route delay | Open |
| FUL000196 | O011259 | 2023-12-20 | carrier_delay | High | Carrier route delay | Open |

## H008 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: EE. UU.
- customer_state: CT
- customer_city: Milford
- primary_market: Europe
- primary_region: Western Europe
- total_orders: 9
- total_sales: 5379.28
- total_profit: 1081.42
- late_delivery_count: 17
- late_delivery_rate: 0.6071
- support_ticket_count: 1
- open_support_ticket_count: 1
- last_meaningful_touch_date: 2017-08-28

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O066502 | 2026-03-05 | 2026-03-08 | PENDING | Late delivery | 1 | Second Class | 319.93 | -57.67 | 316.93 | 2 | 3 | Late |
| O046289 | 2025-05-14 | 2025-05-19 | COMPLETE | Late delivery | 1 | Standard Class | 599.95 | 117.51 | 577.95 | 4 | 5 | Late |
| O043932 | 2025-04-10 | 2025-04-13 | PROCESSING | Advance shipping | 0 | Standard Class | 199.98 | 54.31 | 193.98 | 4 | 3 |  |
| O037478 | 2025-01-06 | 2025-01-10 | PROCESSING | Shipping on time | 0 | Standard Class | 479.92 | -38.52 | 412.73 | 4 | 4 |  |
| O029211 | 2024-09-07 | 2024-09-09 | PROCESSING | Advance shipping | 0 | Standard Class | 829.92 | 78.82 | 740.33 | 4 | 2 |  |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N10498 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E13948 | TH-C000684-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E13947 | TH-C000684-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E13946 | TH-C000684-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E13941 | TH-C000684-[redacted] | 1 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL008279 | O066502 | 2026-03-05 | carrier_delay | High | Carrier route delay | Open |
| FUL005368 | O046289 | 2025-05-14 | carrier_delay | High | Carrier route delay | Open |
| FUL001684 | O021034 | 2024-05-11 | carrier_delay | High | Carrier route delay | Open |
| FUL001175 | O017778 | 2024-03-24 | carrier_delay | High | Carrier route delay | Open |
| FUL009092 | O009959 | 2023-12-01 | carrier_delay | High | Carrier route delay | Open |

## H009 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Corporate
- customer_country: EE. UU.
- customer_state: MI
- customer_city: Detroit
- primary_market: Pacific Asia
- primary_region: West Asia
- total_orders: 7
- total_sales: 4559.4
- total_profit: 681.94
- late_delivery_count: 13
- late_delivery_rate: 0.5652
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2016-10-22

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O045242 | 2025-04-29 | 2025-05-02 | COMPLETE | Advance shipping | 0 | Standard Class | 609.94 | 222.95 | 567.94 | 4 | 3 |  |
| O041456 | 2025-03-05 | 2025-03-07 | PENDING_PAYMENT | Shipping on time | 0 | Second Class | 1089.91 | 322.46 | 990.41 | 2 | 2 |  |
| O021778 | 2024-05-21 | 2024-05-23 | PROCESSING | Late delivery | 1 | First Class | 149.94 | 42.4 | 130.45 | 1 | 2 | Late |
| O020130 | 2024-04-27 | 2024-05-03 | ON_HOLD | Late delivery | 1 | Second Class | 739.95 | -256.45 | 717.15 | 2 | 6 | Late |
| O006145 | 2023-10-06 | 2023-10-12 | CLOSED | Late delivery | 1 | Second Class | 609.94 | 90.99 | 558.85 | 2 | 6 | Late |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N14538 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |
| N14537 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.5652 with category concentration in Men's Footwear. |
| N14536 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band Medium and support history. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E20820 | TH-C001474-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E20819 | TH-C001474-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E20818 | TH-C001474-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL001789 | O021778 | 2024-05-21 | carrier_delay | High | Carrier route delay | Open |
| FUL001530 | O020130 | 2024-04-27 | carrier_delay | High | Carrier route delay | Open |
| FUL007559 | O006145 | 2023-10-06 | carrier_delay | High | Carrier route delay | Open |
| FUL003956 | O003648 | 2023-08-31 | carrier_delay | High | Carrier route delay | Open |

## H010 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Corporate
- customer_country: EE. UU.
- customer_state: GA
- customer_city: Lawrenceville
- primary_market: Europe
- primary_region: Western Europe
- total_orders: 9
- total_sales: 4239.64
- total_profit: -552.37
- late_delivery_count: 12
- late_delivery_rate: 0.5714
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2016-11-30

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O047909 | 2025-06-07 | 2025-06-12 | COMPLETE | Late delivery | 1 | Standard Class | 54.97 | -43.98 | 54.97 | 4 | 5 | Late |
| O042849 | 2025-03-25 | 2025-03-30 | COMPLETE | Late delivery | 1 | Second Class | 250.0 | -12.25 | 245.0 | 2 | 5 | Late |
| O039243 | 2025-01-31 | 2025-02-04 | CLOSED | Shipping on time | 0 | Standard Class | 449.99 | 65.42 | 428.24 | 4 | 4 |  |
| O031513 | 2024-10-11 | 2024-10-15 | CLOSED | Shipping on time | 0 | Standard Class | 24.99 | -5.42 | 23.24 | 4 | 4 |  |
| O028234 | 2024-08-24 | 2024-08-26 | PENDING | Late delivery | 1 | First Class | 1099.94 | -53.37 | 1040.44 | 1 | 2 | Late |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N17033 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band Medium and support history. |
| N17035 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |
| N17032 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E25065 | TH-C001974-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E25064 | TH-C001974-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E25063 | TH-C001974-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL005603 | O047909 | 2025-06-07 | carrier_delay | High | Carrier route delay | Open |
| FUL004884 | O042849 | 2025-03-25 | carrier_delay | High | Carrier route delay | Open |
| FUL002780 | O028234 | 2024-08-24 | carrier_delay | High | Carrier route delay | Open |
| FUL000811 | O015299 | 2024-02-17 | carrier_delay | High | Carrier route delay | Open |
| FUL000251 | O011605 | 2023-12-25 | carrier_delay | High | Carrier route delay | Open |

## H011 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: Europe
- primary_region: Central America
- total_orders: 11
- total_sales: 4804.4
- total_profit: 699.77
- late_delivery_count: 14
- late_delivery_rate: 0.6087
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-08-22
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O066082 | 2026-02-27 | 2026-03-02 | COMPLETE | Advance shipping | 0 | Standard Class | 249.99 | 89.4 | 213.49 | 4 | 3 |  |
| O065245 | 2026-02-15 | 2026-02-17 | PROCESSING | Late delivery | 1 | First Class | 359.96 | 79.67 | 329.36 | 1 | 2 | Late |
| O054780 | 2025-09-15 | 2025-09-21 | PROCESSING | Late delivery | 1 | Standard Class | 399.98 | 172.79 | 383.98 | 4 | 6 | Late |
| O052551 | 2025-08-14 | 2025-08-16 | CLOSED | Advance shipping | 0 | Standard Class | 99.95 | 35.23 | 74.96 | 4 | 2 |  |
| O048015 | 2025-06-08 | 2025-06-14 | COMPLETE | Late delivery | 1 | Standard Class | 604.94 | 61.32 | 514.64 | 4 | 6 | Late |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N13012 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Escalation summary for the customer: protect revenue, close open issues, and document human review. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E18214 | TH-C001182-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E18211 | TH-C001182-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E18210 | TH-C001182-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E18208 | TH-C001182-[redacted] | 2 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL008092 | O065245 | 2026-02-15 | carrier_delay | High | Carrier route delay | Open |
| FUL006597 | O054780 | 2025-09-15 | carrier_delay | High | Carrier route delay | Open |
| FUL005622 | O048015 | 2025-06-08 | carrier_delay | High | Carrier route delay | Open |
| FUL005349 | O046148 | 2025-05-12 | carrier_delay | High | Carrier route delay | Open |
| FUL000365 | O012260 | 2024-01-03 | carrier_delay | High | Carrier route delay | Open |

## H012 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: EE. UU.
- customer_state: OH
- customer_city: Marion
- primary_market: Pacific Asia
- primary_region: Oceania
- total_orders: 5
- total_sales: 4859.36
- total_profit: 844.42
- late_delivery_count: 18
- late_delivery_rate: 0.7826
- support_ticket_count: 1
- open_support_ticket_count: 1
- last_meaningful_touch_date: 2017-04-17
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O057368 | 2025-10-23 | 2025-10-27 | COMPLETE | Shipping on time | 0 | Standard Class | 1199.88 | -133.7 | 1117.89 | 4 | 4 |  |
| O043775 | 2025-04-07 | 2025-04-13 | PENDING_PAYMENT | Late delivery | 1 | Second Class | 1019.81 | 316.46 | 931.22 | 2 | 6 | Late |
| O039573 | 2025-02-05 | 2025-02-09 | PENDING_PAYMENT | Late delivery | 1 | Second Class | 1039.88 | 347.51 | 920.59 | 2 | 4 | Late |
| O030109 | 2024-09-20 | 2024-09-25 | PENDING | Late delivery | 1 | Standard Class | 709.88 | 68.15 | 657.59 | 4 | 5 | Late |
| O030029 | 2024-09-19 | 2024-09-24 | PENDING | Late delivery | 1 | Standard Class | 889.91 | 246.0 | 843.62 | 4 | 5 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T5112 | 2026-04-01 | Refund request | Display issue | I'm having an issue with the {product_purchased}. Please assist.  Sorry, there is an issue with retrieving posts.  Add a comment  Post a new comment. I n… | Open | High | Phone |  |  |  | Neutral |
| T5117 | 2026-03-30 | Cancellation request | Software bug | I'm having an issue with the {product_purchased}. Please assist.  Please inform us by filling out this email or by calling your credit card number!  I unde… | Closed | High | Email | Chance already mind son hand gun home call. | 0.0 | 5.0 | Positive |
| T5114 | 2026-03-15 | Cancellation request | Payment issue | I'm having an issue with the {product_purchased}. Please assist. I'm unable to find any results I've tried using different cables, adapters, or peripherals wit… | Closed | High | Email | Station rich evidence eight probably painting at. | 0.0 | 1.0 | Negative |
| T5115 | 2025-01-21 | Cancellation request | Battery life | My {product_purchased} is making strange noises and not functioning properly. I suspect there might be a hardware issue. Can you please help me with this? Than… | Closed | High | Email | List oil tax effort themselves will. | 0.0 | 1.0 | Negative |
| T5119 | 2024-12-18 | Refund request | Data loss | I'm having an issue with the {product_purchased}. Please assist. 1) Remove the {product_purchased_id}. Please assist. 2) Add the {product_purchased}.Please ass… | Open | High | Email |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N12713 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Cleats. |
| N12714 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N12715 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band High and support history. |
| N12716 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.7826 with category concentration in Cleats. |
| N12717 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E17722 | TH-C001120-[redacted] | 14 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E17721 | TH-C001120-[redacted] | 13 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E17720 | TH-C001120-[redacted] | 12 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E17719 | TH-C001120-[redacted] | 11 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E17718 | TH-C001120-[redacted] | 10 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL005012 | O043775 | 2025-04-07 | carrier_delay | High | Carrier route delay | Open |
| FUL004398 | O039573 | 2025-02-05 | carrier_delay | High | Carrier route delay | Open |
| FUL003071 | O030109 | 2024-09-20 | carrier_delay | High | Carrier route delay | Open |
| FUL003059 | O030029 | 2024-09-19 | carrier_delay | High | Carrier route delay | Open |

## H013 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: LATAM
- primary_region: Central America
- total_orders: 7
- total_sales: 6604.49
- total_profit: 1700.64
- late_delivery_count: 10
- late_delivery_rate: 0.3571
- support_ticket_count: 1
- open_support_ticket_count: 1
- last_meaningful_touch_date: 2017-08-18
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O065787 | 2026-02-23 | 2026-02-26 | PENDING_PAYMENT | Advance shipping | 0 | Standard Class | 299.98 | 30.75 | 245.98 | 4 | 3 |  |
| O056961 | 2025-10-17 | 2025-10-19 | CLOSED | Advance shipping | 0 | Standard Class | 1029.94 | 165.2 | 909.44 | 4 | 2 |  |
| O039081 | 2025-01-29 | 2025-01-31 | PROCESSING | Advance shipping | 0 | Standard Class | 1309.87 | 492.94 | 1241.08 | 4 | 2 |  |
| O031286 | 2024-10-07 | 2024-10-09 | COMPLETE | Shipping on time | 0 | Second Class | 994.94 | 303.34 | 898.29 | 2 | 2 |  |
| O023123 | 2024-06-10 | 2024-06-14 | PENDING_PAYMENT | Shipping on time | 0 | Standard Class | 929.84 | 284.15 | 848.96 | 4 | 4 |  |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N7900 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N7901 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band Low and support history. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E9538 | TH-C000174-[redacted] | 12 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E9537 | TH-C000174-[redacted] | 11 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E9530 | TH-C000174-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E9528 | TH-C000174-[redacted] | 2 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL008810 | O008088 | 2023-11-04 | carrier_delay | High | Carrier route delay | Open |
| FUL004035 | O003694 | 2023-08-31 | carrier_delay | High | Carrier route delay | Open |

## H014 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Corporate
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: LATAM
- primary_region: South America
- total_orders: 7
- total_sales: 4971.21
- total_profit: 568.18
- late_delivery_count: 14
- late_delivery_rate: 0.6087
- support_ticket_count: 1
- open_support_ticket_count: 1
- last_meaningful_touch_date: 2016-11-24
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O047479 | 2025-06-01 | 2025-06-06 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 979.82 | 384.72 | 899.18 | 4 | 5 | Late |
| O042278 | 2025-03-17 | 2025-03-21 | PENDING_PAYMENT | Late delivery | 1 | Second Class | 129.99 | 33.24 | 120.89 | 2 | 4 | Late |
| O039877 | 2025-02-10 | 2025-02-13 | COMPLETE | Advance shipping | 0 | Standard Class | 1529.92 | -22.45 | 1392.52 | 4 | 3 |  |
| O024136 | 2024-06-25 | 2024-06-25 | COMPLETE | Shipping on time | 0 | Same Day | 281.91 | 75.65 | 263.31 | 0 | 0 |  |
| O008106 | 2023-11-04 | 2023-11-06 | PENDING_PAYMENT | Late delivery | 1 | First Class | 849.88 | 12.72 | 815.88 | 1 | 2 | Late |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N12130 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Escalation summary for the customer: protect revenue, close open issues, and document human review. |
| N12125 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band Medium and support history. |
| N12127 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E16714 | TH-C001005-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E16712 | TH-C001005-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E16709 | TH-C001005-[redacted] | 3 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E16708 | TH-C001005-[redacted] | 2 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL005546 | O047479 | 2025-06-01 | carrier_delay | High | Carrier route delay | Open |
| FUL004802 | O042278 | 2025-03-17 | carrier_delay | High | Carrier route delay | Open |
| FUL008815 | O008106 | 2023-11-04 | carrier_delay | High | Carrier route delay | Open |
| FUL003581 | O003374 | 2023-08-27 | carrier_delay | High | Carrier route delay | Open |
| FUL001146 | O001755 | 2023-08-03 | carrier_delay | High | Carrier route delay | Open |

## H015 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: LATAM
- primary_region: West of USA
- total_orders: 6
- total_sales: 4729.36
- total_profit: 442.39
- late_delivery_count: 12
- late_delivery_rate: 0.5714
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-07-06
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O062861 | 2026-01-11 | 2026-01-13 | COMPLETE | Advance shipping | 0 | Standard Class | 200.0 | 87.42 | 186.0 | 4 | 2 |  |
| O052222 | 2025-08-09 | 2025-08-12 | PENDING_PAYMENT | Advance shipping | 0 | Standard Class | 319.94 | 81.09 | 289.74 | 4 | 3 |  |
| O038737 | 2025-01-24 | 2025-01-27 | COMPLETE | Late delivery | 1 | Second Class | 829.86 | 253.06 | 772.78 | 2 | 3 | Late |
| O029018 | 2024-09-04 | 2024-09-08 | PENDING_PAYMENT | Shipping on time | 0 | Standard Class | 1429.87 | -396.22 | 1344.27 | 4 | 4 |  |
| O011764 | 2023-12-27 | 2024-01-01 | COMPLETE | Late delivery | 1 | Standard Class | 1149.81 | 328.83 | 1041.82 | 4 | 5 | Late |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N13420 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer-success owner should align response tone with [redacted] scenario. |
| N13415 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Cardio Equipment. |
| N13417 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band Medium and support history. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E18920 | TH-C001267-[redacted] | 12 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E18917 | TH-C001267-[redacted] | 9 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E18915 | TH-C001267-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E18914 | TH-C001267-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL004278 | O038737 | 2025-01-24 | carrier_delay | High | Carrier route delay | Open |
| FUL000276 | O011764 | 2023-12-27 | carrier_delay | High | Carrier route delay | Open |
| FUL006316 | O005265 | 2023-09-23 | carrier_delay | High | Carrier route delay | Open |

## H016 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Corporate
- customer_country: EE. UU.
- customer_state: IL
- customer_city: Chicago
- primary_market: Europe
- primary_region: Western Europe
- total_orders: 7
- total_sales: 4369.46
- total_profit: 63.56
- late_delivery_count: 18
- late_delivery_rate: 0.8571
- support_ticket_count: 1
- open_support_ticket_count: 1
- last_meaningful_touch_date: 2017-09-14

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O067660 | 2026-03-22 | 2026-03-23 | COMPLETE | Late delivery | 1 | Same Day | 1029.81 | -25.18 | 969.91 | 0 | 1 | Late |
| O066330 | 2026-03-03 | 2026-03-09 | PROCESSING | Late delivery | 1 | Standard Class | 779.8 | 161.52 | 706.17 | 4 | 6 | Late |
| O057688 | 2025-10-28 | 2025-10-30 | PROCESSING | Late delivery | 1 | First Class | 19.99 | 6.52 | 17.39 | 1 | 2 | Late |
| O044923 | 2025-04-24 | 2025-04-28 | COMPLETE | Late delivery | 1 | Second Class | 329.98 | 45.35 | 285.88 | 2 | 4 | Late |
| O042788 | 2025-03-24 | 2025-03-28 | PENDING | Late delivery | 1 | Second Class | 1129.95 | 6.53 | 969.86 | 2 | 4 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T5518 | 2026-01-25 | Billing inquiry | Network problem | I'm having an issue with the {product_purchased}. Please assist.  I'd appreciate it if you could help me! Thanks!  R.B. Cajal.  I like the size of the lo… | Open | High | Social media |  |  |  | Neutral |
| T5523 | 2025-12-03 | Product inquiry | Network problem | The {product_purchased} is unable to establish a stable internet connection. It keeps disconnecting intermittently. How can I troubleshoot this network problem… | Open | High | Chat |  |  |  | Neutral |
| T5524 | 2025-08-11 | Cancellation request | Installation support | My {product_purchased} crashed, and I lost all the data stored on it. Is there any way to recover the lost data?  $ curl -X POST http://post.pinterest.com/?h… | Open | High | Email |  |  |  | Neutral |
| T6480 | 2025-02-01 | Technical issue | Product recommendation | I've accidentally deleted important data from my {product_purchased}. Is there any way to recover the deleted files? I need them urgently. The reason I'm using… | Pending | High | Chat |  |  |  | Neutral |
| T6487 | 2024-07-28 | Cancellation request | Peripheral compatibility | I'm having an issue with the {product_purchased}. Please assist.  When looking for a retailer, please consider these items: I've followed the troubleshooting… | Closed | High | Phone | Third just a behavior anyone artist enough. | 0.0 | 3.0 | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N16066 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Indoor/Outdoor Games. |
| N16067 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N16068 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band High and support history. |
| N16069 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.8571 with category concentration in Indoor/Outdoor Games. |
| N16070 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E23424 | TH-C001775-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E23423 | TH-C001775-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E23422 | TH-C001775-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E23421 | TH-C001775-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E23420 | TH-C001775-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL008447 | O067660 | 2026-03-22 | carrier_delay | High | Carrier route delay | Open |
| FUL008253 | O066330 | 2026-03-03 | carrier_delay | High | Carrier route delay | Open |
| FUL007030 | O057688 | 2025-10-28 | carrier_delay | High | Carrier route delay | Open |
| FUL005163 | O044923 | 2025-04-24 | carrier_delay | High | Carrier route delay | Open |
| FUL004869 | O042788 | 2025-03-24 | carrier_delay | High | Carrier route delay | Open |

## H017 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Home Office
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: LATAM
- primary_region: Western Europe
- total_orders: 8
- total_sales: 4964.46
- total_profit: 331.22
- late_delivery_count: 12
- late_delivery_rate: 0.5217
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-06-14
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O061331 | 2025-12-20 | 2025-12-22 | COMPLETE | Advance shipping | 0 | Standard Class | 429.84 | 117.22 | 369.26 | 4 | 2 |  |
| O058828 | 2025-11-13 | 2025-11-17 | CLOSED | Shipping on time | 0 | Standard Class | 769.91 | 112.13 | 669.41 | 4 | 4 |  |
| O046332 | 2025-05-15 | 2025-05-18 | PENDING_PAYMENT | Advance shipping | 0 | Standard Class | 749.97 | 201.26 | 639.48 | 4 | 3 |  |
| O044759 | 2025-04-22 | 2025-04-27 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 399.98 | -581.97 | 387.98 | 4 | 5 | Late |
| O018645 | 2024-04-06 | 2024-04-12 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 39.99 | -10.39 | 37.79 | 4 | 6 | Late |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N12167 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer-success owner should align response tone with [redacted] scenario. |
| N12168 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Monitor whether the next interaction with the customer resolves the current [redacted] thread. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E16789 | TH-C001014-[redacted] | 13 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E16782 | TH-C001014-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E16780 | TH-C001014-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E16778 | TH-C001014-[redacted] | 2 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL005140 | O044759 | 2025-04-22 | carrier_delay | High | Carrier route delay | Open |
| FUL001319 | O018645 | 2024-04-06 | carrier_delay | High | Carrier route delay | Open |
| FUL001066 | O017016 | 2024-03-13 | carrier_delay | High | Carrier route delay | Open |
| FUL000559 | O013685 | 2024-01-24 | carrier_delay | High | Carrier route delay | Open |
| FUL000117 | O001079 | 2023-07-24 | carrier_delay | High | Carrier route delay | Open |

## H018 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Corporate
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: Europe
- primary_region: Western Europe
- total_orders: 9
- total_sales: 4649.47
- total_profit: -289.86
- late_delivery_count: 17
- late_delivery_rate: 0.6538
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-09-15

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O067683 | 2026-03-23 | 2026-03-27 | PENDING_PAYMENT | Late delivery | 1 | Second Class | 929.87 | -452.24 | 845.88 | 2 | 4 | Late |
| O064526 | 2026-02-04 | 2026-02-06 | PENDING_PAYMENT | Advance shipping | 0 | Standard Class | 129.99 | 61.42 | 122.84 | 4 | 2 |  |
| O050645 | 2025-07-17 | 2025-07-23 | CLOSED | Late delivery | 1 | Standard Class | 249.9 | 22.49 | 224.91 | 4 | 6 | Late |
| O044345 | 2025-04-16 | 2025-04-22 | PENDING | Late delivery | 1 | Standard Class | 599.96 | -17.52 | 585.96 | 4 | 6 | Late |
| O031836 | 2024-10-15 | 2024-10-17 | PENDING | Advance shipping | 0 | Standard Class | 629.96 | -136.85 | 542.47 | 4 | 2 |  |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N13973 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N13974 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band Medium and support history. |
| N13972 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Men's Footwear. |
| N13975 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.6538 with category concentration in Men's Footwear. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E19868 | TH-C001367-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E19866 | TH-C001367-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E19862 | TH-C001367-[redacted] | 2 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL008450 | O067683 | 2026-03-23 | carrier_delay | High | Carrier route delay | Open |
| FUL006019 | O050645 | 2025-07-17 | carrier_delay | High | Carrier route delay | Open |
| FUL005086 | O044345 | 2025-04-16 | carrier_delay | High | Carrier route delay | Open |
| FUL000660 | O014319 | 2024-02-03 | carrier_delay | High | Carrier route delay | Open |
| FUL008601 | O006864 | 2023-10-17 | carrier_delay | High | Carrier route delay | Open |

## H019 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Corporate
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: Pacific Asia
- primary_region: Eastern Asia
- total_orders: 7
- total_sales: 4316.61
- total_profit: 855.34
- late_delivery_count: 11
- late_delivery_rate: 0.4583
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-06-04

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O060648 | 2025-12-10 | 2025-12-10 | PENDING_PAYMENT | Shipping on time | 0 | Same Day | 529.97 | 142.98 | 466.57 | 0 | 0 |  |
| O044024 | 2025-04-11 | 2025-04-16 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 129.99 | 37.31 | 106.59 | 4 | 5 | Late |
| O029003 | 2024-09-04 | 2024-09-08 | PENDING | Shipping on time | 0 | Standard Class | 631.9 | 62.23 | 563.69 | 4 | 4 |  |
| O027816 | 2024-08-18 | 2024-08-18 | COMPLETE | Shipping on time | 0 | Same Day | 49.98 | 8.0 | 39.98 | 0 | 0 |  |
| O020668 | 2024-05-05 | 2024-05-07 | PENDING | Late delivery | 1 | First Class | 979.9 | 97.43 | 901.4 | 1 | 2 | Late |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N16415 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Men's Footwear. |
| N16419 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E24020 | TH-C001852-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E24019 | TH-C001852-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E24018 | TH-C001852-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E24017 | TH-C001852-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E24016 | TH-C001852-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL005045 | O044024 | 2025-04-11 | carrier_delay | High | Carrier route delay | Open |
| FUL001618 | O020668 | 2024-05-05 | carrier_delay | High | Carrier route delay | Open |
| FUL001002 | O016610 | 2024-03-07 | carrier_delay | High | Carrier route delay | Open |

## H020 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Home Office
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: Europe
- primary_region: Western Europe
- total_orders: 7
- total_sales: 8339.26
- total_profit: 696.62
- late_delivery_count: 23
- late_delivery_rate: 0.8214
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-10-01
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O068806 | 2026-04-08 | 2026-04-10 | COMPLETE | Advance shipping | 0 | Standard Class | 2629.92 | 141.59 | 2341.02 | 4 | 2 |  |
| O064031 | 2026-01-28 | 2026-01-30 | CLOSED | Late delivery | 1 | First Class | 909.8 | 222.81 | 766.74 | 1 | 2 | Late |
| O063014 | 2026-01-13 | 2026-01-15 | PENDING | Late delivery | 1 | First Class | 1069.91 | -75.24 | 974.01 | 1 | 2 | Late |
| O049580 | 2025-07-01 | 2025-07-03 | CLOSED | Late delivery | 1 | First Class | 1199.9 | 257.51 | 1031.11 | 1 | 2 | Late |
| O047249 | 2025-05-28 | 2025-06-02 | PENDING | Late delivery | 1 | Standard Class | 1279.85 | 118.68 | 1139.37 | 4 | 5 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T6819 | 2025-12-18 | Technical issue | Product recommendation | I'm having an issue with the {product_purchased}. Please assist.   Thanks.  -R   Thanks:  -J   Click again  Thank you.  -B   Thank you I've… | Pending | Medium | Email |  |  |  | Neutral |
| T6821 | 2025-12-14 | Billing inquiry | Network problem | I'm having an issue with the {product_purchased}. Please assist.  Product Purchased  Product Purchased  Product Purchased  Product Purchased  Product… | Open | Medium | Phone |  |  |  | Neutral |
| T6809 | 2025-03-25 | Refund request | Delivery problem | I'm having an issue with the {product_purchased}. Please assist. A refund is not required to complete the purchase.  * The following may occur once you have … | Pending | Medium | Phone |  |  |  | Neutral |
| T6816 | 2024-08-20 | Billing inquiry | Data loss | I've forgotten my password for my {product_purchased} account, and the password reset option is not working. How can I recover my account?  If an action was … | Pending | Medium | Social media |  |  |  | Neutral |
| T6815 | 2024-06-24 | Technical issue | Battery life | My {product_purchased} is making strange noises and not functioning properly. I suspect there might be a hardware issue. Can you please help me with this? Can … | Open | Medium | Social media |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N7089 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Cleats. |
| N7090 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N7091 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band High and support history. |
| N7092 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.8214 with category concentration in Cleats. |
| N7093 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E8162 | TH-C000015-[redacted] | 14 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E8161 | TH-C000015-[redacted] | 13 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E8160 | TH-C000015-[redacted] | 12 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E8159 | TH-C000015-[redacted] | 11 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E8158 | TH-C000015-[redacted] | 10 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL007919 | O064031 | 2026-01-28 | carrier_delay | High | Carrier route delay | Open |
| FUL007775 | O063014 | 2026-01-13 | carrier_delay | High | Carrier route delay | Open |
| FUL005857 | O049580 | 2025-07-01 | carrier_delay | High | Carrier route delay | Open |
| FUL005515 | O047249 | 2025-05-28 | carrier_delay | High | Carrier route delay | Open |
| FUL003866 | O035790 | 2024-12-12 | carrier_delay | High | Carrier route delay | Open |

## H021 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Home Office
- customer_country: EE. UU.
- customer_state: NJ
- customer_city: North Bergen
- primary_market: LATAM
- primary_region: West of USA
- total_orders: 8
- total_sales: 5341.42
- total_profit: -483.37
- late_delivery_count: 18
- late_delivery_rate: 0.72
- support_ticket_count: 1
- open_support_ticket_count: 1
- last_meaningful_touch_date: 2017-08-12

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O065356 | 2026-02-17 | 2026-02-19 | CLOSED | Late delivery | 1 | First Class | 599.94 | 151.61 | 573.94 | 1 | 2 | Late |
| O060904 | 2025-12-14 | 2025-12-19 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 888.9 | -682.36 | 847.53 | 4 | 5 | Late |
| O040136 | 2025-02-13 | 2025-02-15 | PENDING | Advance shipping | 0 | Standard Class | 1139.89 | -56.51 | 1064.89 | 4 | 2 |  |
| O033313 | 2024-11-06 | 2024-11-08 | COMPLETE | Late delivery | 1 | First Class | 712.86 | -220.89 | 665.72 | 1 | 2 | Late |
| O027666 | 2024-08-15 | 2024-08-17 | PENDING | Shipping on time | 0 | Second Class | 399.98 | -48.5 | 387.98 | 2 | 2 |  |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N10610 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Camping & Hiking. |
| N10613 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.7200 with category concentration in Camping & Hiking. |
| N10612 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band Medium and support history. |
| N10614 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E14146 | TH-C000706-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E14145 | TH-C000706-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E14144 | TH-C000706-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E14143 | TH-C000706-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E14142 | TH-C000706-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL008105 | O065356 | 2026-02-17 | carrier_delay | High | Carrier route delay | Open |
| FUL007479 | O060904 | 2025-12-14 | carrier_delay | High | Carrier route delay | Open |
| FUL003514 | O033313 | 2024-11-06 | carrier_delay | High | Carrier route delay | Open |
| FUL001558 | O020340 | 2024-04-30 | carrier_delay | High | Carrier route delay | Open |
| FUL008946 | O008944 | 2023-11-16 | carrier_delay | High | Carrier route delay | Open |

## H022 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: LATAM
- primary_region: Western Europe
- total_orders: 6
- total_sales: 4735.55
- total_profit: -27.72
- late_delivery_count: 10
- late_delivery_rate: 0.4545
- support_ticket_count: 1
- open_support_ticket_count: 1
- last_meaningful_touch_date: 2017-05-08
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O058800 | 2025-11-13 | 2025-11-19 | COMPLETE | Late delivery | 1 | Second Class | 1309.87 | -243.92 | 1254.57 | 2 | 6 | Late |
| O029490 | 2024-09-11 | 2024-09-17 | PROCESSING | Late delivery | 1 | Standard Class | 609.91 | 22.93 | 540.42 | 4 | 6 | Late |
| O019953 | 2024-04-25 | 2024-04-29 | PENDING_PAYMENT | Shipping on time | 0 | Standard Class | 1149.94 | 50.98 | 1050.69 | 4 | 4 |  |
| O018701 | 2024-04-06 | 2024-04-08 | PENDING | Shipping on time | 0 | Second Class | 879.93 | -21.04 | 842.93 | 2 | 2 |  |
| O005512 | 2023-09-27 | 2023-09-30 | COMPLETE | Advance shipping | 0 | Standard Class | 629.94 | 161.49 | 559.34 | 4 | 3 |  |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N13351 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band Medium and support history. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E18806 | TH-C001255-[redacted] | 14 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E18803 | TH-C001255-[redacted] | 11 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E18800 | TH-C001255-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E18797 | TH-C001255-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E18795 | TH-C001255-[redacted] | 3 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL007182 | O058800 | 2025-11-13 | carrier_delay | High | Carrier route delay | Open |
| FUL002966 | O029490 | 2024-09-11 | carrier_delay | High | Carrier route delay | Open |
| FUL008938 | O000889 | 2023-07-21 | carrier_delay | High | Carrier route delay | Open |

## H023 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: LATAM
- primary_region: South America
- total_orders: 7
- total_sales: 7659.12
- total_profit: 1663.41
- late_delivery_count: 24
- late_delivery_rate: 0.8276
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-09-02

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O066818 | 2026-03-10 | 2026-03-14 | SUSPECTED_FRAUD | Shipping canceled | 0 | Standard Class | 1519.84 | 106.72 | 1351.84 | 4 | 4 | Canceled |
| O053859 | 2025-09-02 | 2025-09-07 | COMPLETE | Late delivery | 1 | Standard Class | 849.85 | 32.59 | 766.38 | 4 | 5 | Late |
| O050863 | 2025-07-20 | 2025-07-22 | PENDING | Late delivery | 1 | First Class | 1429.9 | 280.77 | 1415.7 | 1 | 2 | Late |
| O041449 | 2025-03-05 | 2025-03-10 | PROCESSING | Late delivery | 1 | Standard Class | 1309.83 | 336.03 | 1220.85 | 4 | 5 | Late |
| O020981 | 2024-05-10 | 2024-05-12 | PROCESSING | Late delivery | 1 | First Class | 319.92 | 117.9 | 278.62 | 1 | 2 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T5929 | 2026-01-07 | Cancellation request | Product compatibility | I'm having an issue with the {product_purchased}. Please assist. If this is a new or confusing product item, please let us know. I need assistance as soon as p… | Pending | High | Chat |  |  |  | Neutral |
| T5105 | 2025-10-28 | Refund request | Product recommendation | I'm encountering a software bug in the {product_purchased}. Whenever I try to perform a specific action, the application crashes. Are there any updates or fixe… | Open | High | Phone |  |  |  | Neutral |
| T5101 | 2024-10-01 | Cancellation request | Delivery problem | I'm having an issue with the {product_purchased}. Please assist. I'm using what is on my phone right now. I also have an issue with a product that was sold out… | Pending | High | Email |  |  |  | Neutral |
| T5104 | 2024-06-26 | Refund request | Battery life | I'm having an issue with the {product_purchased}. Please assist.  You are the author of this site and you understand that you are providing my services for i… | Open | High | Chat |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N7216 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Fishing. |
| N7217 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N7218 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band High and support history. |
| N7219 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.8276 with category concentration in Fishing. |
| N7220 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E8378 | TH-C000041-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E8377 | TH-C000041-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E8376 | TH-C000041-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E8375 | TH-C000041-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E8374 | TH-C000041-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL008327 | O066818 | 2026-03-10 | cancellation_review | Medium | Customer or fulfillment cancellation | Closed |
| FUL006480 | O053859 | 2025-09-02 | carrier_delay | High | Carrier route delay | Open |
| FUL006049 | O050863 | 2025-07-20 | carrier_delay | High | Carrier route delay | Open |
| FUL004665 | O041449 | 2025-03-05 | carrier_delay | High | Carrier route delay | Open |
| FUL001674 | O020981 | 2024-05-10 | carrier_delay | High | Carrier route delay | Open |

## H024 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: Europe
- primary_region: Northern Europe
- total_orders: 7
- total_sales: 4589.3
- total_profit: 816.04
- late_delivery_count: 18
- late_delivery_rate: 0.6667
- support_ticket_count: 1
- open_support_ticket_count: 1
- last_meaningful_touch_date: 2017-08-31
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O066690 | 2026-03-08 | 2026-03-14 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 789.92 | 150.97 | 672.84 | 4 | 6 | Late |
| O064020 | 2026-01-28 | 2026-02-03 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 639.93 | 232.76 | 622.33 | 4 | 6 | Late |
| O036097 | 2024-12-16 | 2024-12-19 | CLOSED | Advance shipping | 0 | Standard Class | 639.9 | 173.63 | 581.11 | 4 | 3 |  |
| O031920 | 2024-10-16 | 2024-10-22 | SUSPECTED_FRAUD | Shipping canceled | 0 | Standard Class | 429.97 | 162.96 | 385.47 | 4 | 6 | Canceled |
| O019019 | 2024-04-11 | 2024-04-12 | COMPLETE | Late delivery | 1 | Same Day | 1039.74 | 33.61 | 932.66 | 0 | 1 | Late |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N14372 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Escalation summary for the customer: protect revenue, close open issues, and document human review. |
| N14365 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Indoor/Outdoor Games. |
| N14368 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.6667 with category concentration in Indoor/Outdoor Games. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E20535 | TH-C001442-[redacted] | 9 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E20532 | TH-C001442-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL008304 | O066690 | 2026-03-08 | carrier_delay | High | Carrier route delay | Open |
| FUL007916 | O064020 | 2026-01-28 | carrier_delay | High | Carrier route delay | Open |
| FUL003322 | O031920 | 2024-10-16 | cancellation_review | Medium | Customer or fulfillment cancellation | Closed |
| FUL001373 | O019019 | 2024-04-11 | carrier_delay | High | Carrier route delay | Open |
| FUL000357 | O012241 | 2024-01-03 | carrier_delay | High | Carrier route delay | Open |

## H025 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Home Office
- customer_country: EE. UU.
- customer_state: CA
- customer_city: Chino
- primary_market: Europe
- primary_region: Western Europe
- total_orders: 8
- total_sales: 6591.23
- total_profit: 757.04
- late_delivery_count: 17
- late_delivery_rate: 0.5312
- support_ticket_count: 1
- open_support_ticket_count: 1
- last_meaningful_touch_date: 2017-07-17

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O063633 | 2026-01-22 | 2026-01-24 | PENDING_PAYMENT | Late delivery | 1 | First Class | 1269.85 | 241.67 | 1087.47 | 1 | 2 | Late |
| O047679 | 2025-06-03 | 2025-06-08 | CANCELED | Shipping canceled | 0 | Standard Class | 269.98 | -9.86 | 227.18 | 4 | 5 | Canceled |
| O036430 | 2024-12-21 | 2024-12-27 | COMPLETE | Late delivery | 1 | Standard Class | 1249.91 | -17.63 | 1165.92 | 4 | 6 | Late |
| O014554 | 2024-02-06 | 2024-02-11 | CANCELED | Shipping canceled | 0 | Standard Class | 511.9 | 44.85 | 446.51 | 4 | 5 | Canceled |
| O010975 | 2023-12-16 | 2023-12-22 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 829.86 | -93.51 | 765.87 | 4 | 6 | Late |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N7920 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N7921 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band Medium and support history. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E9568 | TH-C000178-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E9563 | TH-C000178-[redacted] | 3 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E9562 | TH-C000178-[redacted] | 2 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E9561 | TH-C000178-[redacted] | 1 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL007856 | O063633 | 2026-01-22 | carrier_delay | High | Carrier route delay | Open |
| FUL005570 | O047679 | 2025-06-03 | cancellation_review | Medium | Customer or fulfillment cancellation | Closed |
| FUL003946 | O036430 | 2024-12-21 | carrier_delay | High | Carrier route delay | Open |
| FUL000698 | O014554 | 2024-02-06 | cancellation_review | Medium | Customer or fulfillment cancellation | Closed |
| FUL000149 | O010975 | 2023-12-16 | carrier_delay | High | Carrier route delay | Open |

## H026 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Corporate
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: Europe
- primary_region: South America
- total_orders: 8
- total_sales: 6143.44
- total_profit: 382.35
- late_delivery_count: 25
- late_delivery_rate: 0.8333
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-09-10
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O067404 | 2026-03-18 | 2026-03-23 | PENDING | Late delivery | 1 | Standard Class | 549.98 | 202.72 | 430.49 | 4 | 5 | Late |
| O064644 | 2026-02-06 | 2026-02-11 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 909.93 | 136.38 | 784.84 | 4 | 5 | Late |
| O054239 | 2025-09-07 | 2025-09-12 | SUSPECTED_FRAUD | Shipping canceled | 0 | Standard Class | 949.86 | 283.93 | 796.68 | 4 | 5 | Canceled |
| O033898 | 2024-11-14 | 2024-11-18 | COMPLETE | Late delivery | 1 | Second Class | 464.95 | -171.48 | 438.75 | 2 | 4 | Late |
| O021855 | 2024-05-23 | 2024-05-29 | PROCESSING | Late delivery | 1 | Standard Class | 178.94 | 4.87 | 168.53 | 4 | 6 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T6331 | 2025-10-09 | Technical issue | Installation support | I've forgotten my password for my {product_purchased} account, and the password reset option is not working. How can I recover my account?  You must have sig… | Open | High | Email |  |  |  | Neutral |
| T6334 | 2025-01-04 | Billing inquiry | Cancellation request | I've encountered a data loss issue with my {product_purchased}. All the files and documents seem to have disappeared. Can you guide me on how to retrieve them?… | Closed | High | Chat | Same determine thing page represent that system. | 0.0 | 5.0 | Positive |
| T6625 | 2024-07-07 | Product inquiry | Hardware issue | I'm having an issue with the {product_purchased}. Please assist.   If this doesn't work for you  1) Try the default version. It works fine.  2) Please r… | Pending | High | Chat |  |  |  | Neutral |
| T5640 | 2024-07-04 | Refund request | Data loss | I've encountered a data loss issue with my {product_purchased}. All the files and documents seem to have disappeared. Can you guide me on how to retrieve them?… | Open | High | Phone |  |  |  | Neutral |
| T6624 | 2024-06-24 | Cancellation request | Product recommendation | I'm having an issue with the {product_purchased}. Please assist.  You have requested the file:  Name: Vapour_Wet_Apes_Villa_00_Lavender_Diva I've noticed a… | Closed | High | Phone | Star past car. | 2.4 | 4.0 | Positive |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N8516 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Men's Footwear. |
| N8517 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N8518 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band High and support history. |
| N8519 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.8333 with category concentration in Men's Footwear. |
| N8520 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E10580 | TH-C000292-[redacted] | 14 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E10579 | TH-C000292-[redacted] | 13 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E10578 | TH-C000292-[redacted] | 12 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E10577 | TH-C000292-[redacted] | 11 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E10576 | TH-C000292-[redacted] | 10 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL008403 | O067404 | 2026-03-18 | carrier_delay | High | Carrier route delay | Open |
| FUL008006 | O064644 | 2026-02-06 | carrier_delay | High | Carrier route delay | Open |
| FUL006527 | O054239 | 2025-09-07 | cancellation_review | Medium | Customer or fulfillment cancellation | Closed |
| FUL003603 | O033898 | 2024-11-14 | carrier_delay | High | Carrier route delay | Open |
| FUL001803 | O021855 | 2024-05-23 | carrier_delay | High | Carrier route delay | Open |

## H027 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: Pacific Asia
- primary_region: Southeast Asia
- total_orders: 6
- total_sales: 4935.61
- total_profit: 8.98
- late_delivery_count: 13
- late_delivery_rate: 0.5652
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-03-22
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O055616 | 2025-09-27 | 2025-09-29 | PENDING_PAYMENT | Shipping on time | 0 | Second Class | 545.92 | 143.31 | 448.37 | 2 | 2 |  |
| O049869 | 2025-07-05 | 2025-07-10 | PROCESSING | Late delivery | 1 | Standard Class | 829.92 | -791.35 | 733.42 | 4 | 5 | Late |
| O043320 | 2025-04-01 | 2025-04-07 | PROCESSING | Late delivery | 1 | Second Class | 1149.95 | 163.98 | 992.95 | 2 | 6 | Late |
| O033172 | 2024-11-04 | 2024-11-07 | PENDING_PAYMENT | Advance shipping | 0 | Standard Class | 499.97 | 91.67 | 454.97 | 4 | 3 |  |
| O026086 | 2024-07-23 | 2024-07-25 | PENDING_PAYMENT | Advance shipping | 0 | Standard Class | 739.94 | 89.11 | 655.34 | 4 | 2 |  |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T6152 | 2024-09-16 | Cancellation request | Network problem | I'm having an issue with the {product_purchased}. Please assist.  "  " }  // (1) Please refer to the instructions on the top left corner of this package … | Pending | Low | Phone |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N12317 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Escalation summary for the customer: protect revenue, close open issues, and document human review. |
| N12311 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N12312 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band Medium and support history. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E17042 | TH-C001040-[redacted] | 14 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E17039 | TH-C001040-[redacted] | 11 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E17032 | TH-C001040-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E17029 | TH-C001040-[redacted] | 1 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL005904 | O049869 | 2025-07-05 | carrier_delay | High | Carrier route delay | Open |
| FUL004956 | O043320 | 2025-04-01 | carrier_delay | High | Carrier route delay | Open |
| FUL001819 | O021983 | 2024-05-24 | carrier_delay | High | Carrier route delay | Open |

## H028 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Corporate
- customer_country: EE. UU.
- customer_state: MN
- customer_city: Burnsville
- primary_market: Pacific Asia
- primary_region: Oceania
- total_orders: 7
- total_sales: 4629.67
- total_profit: 369.13
- late_delivery_count: 11
- late_delivery_rate: 0.5238
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-03-23

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O055658 | 2025-09-28 | 2025-09-30 | ON_HOLD | Late delivery | 1 | First Class | 399.98 | 134.39 | 383.98 | 1 | 2 | Late |
| O053985 | 2025-09-04 | 2025-09-04 | COMPLETE | Shipping on time | 0 | Same Day | 699.95 | 162.17 | 641.96 | 0 | 0 |  |
| O046232 | 2025-05-13 | 2025-05-16 | CLOSED | Late delivery | 1 | Second Class | 419.97 | 39.63 | 385.07 | 2 | 3 | Late |
| O044245 | 2025-04-14 | 2025-04-20 | COMPLETE | Late delivery | 1 | Standard Class | 1079.97 | -308.52 | 1040.47 | 4 | 6 | Late |
| O042687 | 2025-03-23 | 2025-03-25 | COMPLETE | Late delivery | 1 | First Class | 270.0 | 21.75 | 238.5 | 1 | 2 | Late |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N14085 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N14088 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |
| N14086 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band Medium and support history. |
| N14087 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.5238 with category concentration in Women's Apparel. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E20055 | TH-C001387-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E20054 | TH-C001387-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E20053 | TH-C001387-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E20050 | TH-C001387-[redacted] | 2 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL006727 | O055658 | 2025-09-28 | carrier_delay | High | Carrier route delay | Open |
| FUL005361 | O046232 | 2025-05-13 | carrier_delay | High | Carrier route delay | Open |
| FUL005076 | O044245 | 2025-04-14 | carrier_delay | High | Carrier route delay | Open |
| FUL004856 | O042687 | 2025-03-23 | carrier_delay | High | Carrier route delay | Open |

## H029 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: Pacific Asia
- primary_region: West Africa
- total_orders: 10
- total_sales: 5779.39
- total_profit: 1093.38
- late_delivery_count: 13
- late_delivery_rate: 0.4194
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-09-05
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O067040 | 2026-03-13 | 2026-03-15 | PENDING | Late delivery | 1 | First Class | 729.84 | 215.15 | 684.95 | 1 | 2 | Late |
| O055481 | 2025-09-25 | 2025-09-27 | PROCESSING | Advance shipping | 0 | Standard Class | 379.97 | -229.37 | 321.97 | 4 | 2 |  |
| O051242 | 2025-07-26 | 2025-07-29 | COMPLETE | Advance shipping | 0 | Standard Class | 999.93 | 327.24 | 953.43 | 4 | 3 |  |
| O046555 | 2025-05-18 | 2025-05-19 | COMPLETE | Late delivery | 1 | Same Day | 199.99 | 18.98 | 167.99 | 0 | 1 | Late |
| O045505 | 2025-05-03 | 2025-05-09 | PENDING | Late delivery | 1 | Standard Class | 809.88 | 215.88 | 768.28 | 4 | 6 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T6895 | 2025-04-02 | Refund request | Refund request | I'm having an issue with the {product_purchased}. Please assist. [20:21:45.] The [code] is '{}': $x = 0x20000000. [20:21:45.] We are I've already contacted cus… | Open | Low | Email |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N9262 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Escalation summary for the customer: protect revenue, close open issues, and document human review. |
| N9258 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.4194 with category concentration in Water Sports. |
| N9259 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |
| N9256 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E11842 | TH-C000441-[redacted] | 12 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E11841 | TH-C000441-[redacted] | 11 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E11840 | TH-C000441-[redacted] | 10 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E11836 | TH-C000441-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E11831 | TH-C000441-[redacted] | 1 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL008371 | O067040 | 2026-03-13 | carrier_delay | High | Carrier route delay | Open |
| FUL005408 | O046555 | 2025-05-18 | carrier_delay | High | Carrier route delay | Open |
| FUL005263 | O045505 | 2025-05-03 | carrier_delay | High | Carrier route delay | Open |
| FUL004243 | O038454 | 2025-01-20 | carrier_delay | High | Carrier route delay | Open |
| FUL001777 | O021699 | 2024-05-20 | carrier_delay | High | Carrier route delay | Open |

## H030 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: EE. UU.
- customer_state: NY
- customer_city: Rochester
- primary_market: LATAM
- primary_region: Central America
- total_orders: 8
- total_sales: 4721.55
- total_profit: 951.19
- late_delivery_count: 18
- late_delivery_rate: 0.9
- support_ticket_count: 1
- open_support_ticket_count: 1
- last_meaningful_touch_date: 2017-06-14

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O061368 | 2025-12-20 | 2025-12-24 | PENDING | Late delivery | 1 | Second Class | 659.91 | 5.71 | 586.12 | 2 | 4 | Late |
| O059254 | 2025-11-19 | 2025-11-24 | PENDING | Late delivery | 1 | Standard Class | 969.95 | 248.23 | 842.6 | 4 | 5 | Late |
| O057005 | 2025-10-18 | 2025-10-24 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 399.98 | 101.39 | 299.99 | 4 | 6 | Late |
| O048244 | 2025-06-12 | 2025-06-17 | PROCESSING | Late delivery | 1 | Second Class | 459.91 | 113.58 | 407.12 | 2 | 5 | Late |
| O041700 | 2025-03-08 | 2025-03-14 | COMPLETE | Late delivery | 1 | Second Class | 579.95 | 114.95 | 515.96 | 2 | 6 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T5609 | 2026-04-02 | Technical issue | Refund request | My {product_purchased} crashed, and I lost all the data stored on it. Is there any way to recover the lost data? The issue I'm facing is intermittent. Sometime… | Open | Critical | Social media |  |  |  | Neutral |
| T6371 | 2025-10-27 | Technical issue | Data loss | I'm having an issue with the {product_purchased}. Please assist.  Q: Can I buy more than one copy of the item?  A: All sales are limited to 1 (1) copy. (Ex… | Closed | Critical | Social media | Sport forget even effect practice kitchen. | 0.0 | 5.0 | Positive |
| T6375 | 2024-11-05 | Billing inquiry | Refund request | I'm having an issue with the {product_purchased}. Please assist. <li>Sorry about the error. I was trying to open the app by name, but this is not a valid produ… | Pending | Critical | Social media |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N13438 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Fishing. |
| N13439 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N13440 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band High and support history. |
| N13441 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.9000 with category concentration in Fishing. |
| N13442 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E18954 | TH-C001271-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E18953 | TH-C001271-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E18952 | TH-C001271-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E18951 | TH-C001271-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E18950 | TH-C001271-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL007546 | O061368 | 2025-12-20 | carrier_delay | High | Carrier route delay | Open |
| FUL007246 | O059254 | 2025-11-19 | carrier_delay | High | Carrier route delay | Open |
| FUL006925 | O057005 | 2025-10-18 | carrier_delay | High | Carrier route delay | Open |
| FUL005658 | O048244 | 2025-06-12 | carrier_delay | High | Carrier route delay | Open |
| FUL004712 | O041700 | 2025-03-08 | carrier_delay | High | Carrier route delay | Open |

## H031 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Home Office
- customer_country: EE. UU.
- customer_state: MA
- customer_city: Brockton
- primary_market: Africa
- primary_region: West Africa
- total_orders: 6
- total_sales: 4969.37
- total_profit: 953.87
- late_delivery_count: 23
- late_delivery_rate: 1.0
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-01-22
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O051558 | 2025-07-30 | 2025-08-01 | PENDING | Late delivery | 1 | First Class | 949.91 | 136.53 | 848.41 | 1 | 2 | Late |
| O050438 | 2025-07-14 | 2025-07-18 | PENDING_PAYMENT | Late delivery | 1 | Second Class | 789.95 | 58.59 | 731.55 | 2 | 4 | Late |
| O049234 | 2025-06-26 | 2025-07-01 | CLOSED | Late delivery | 1 | Standard Class | 639.92 | 101.29 | 563.12 | 4 | 5 | Late |
| O046262 | 2025-05-14 | 2025-05-17 | PENDING | Late delivery | 1 | Second Class | 989.83 | 238.17 | 872.14 | 2 | 3 | Late |
| O034881 | 2024-11-29 | 2024-12-01 | PROCESSING | Late delivery | 1 | First Class | 909.85 | 133.3 | 836.57 | 1 | 2 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T6181 | 2026-02-25 | Technical issue | Product setup | I'm having an issue with the {product_purchased}. Please assist. {{product_purchased}}  {"user":{"product_name": "Savage Stave","name":"Savage Stave - Red Ve… | Open | Critical | Phone |  |  |  | Neutral |
| T5216 | 2026-01-14 | Billing inquiry | Peripheral compatibility | I've accidentally deleted important data from my {product_purchased}. Is there any way to recover the deleted files? I need them urgently.  There is no way t… | Open | Critical | Chat |  |  |  | Neutral |
| T6791 | 2025-11-24 | Technical issue | Product compatibility | I'm having an issue with the {product_purchased}. Please assist. As an artist, I'm trying to build a collection, I'd like to know what's out there. Thanks!  … | Open | Critical | Chat |  |  |  | Neutral |
| T5219 | 2025-06-15 | Billing inquiry | Battery life | I'm having an issue with the {product_purchased}. Please assist. # # If the product will sell for only $0 and then sold again after 3 minutes. The customer sho… | Pending | Critical | Email |  |  |  | Neutral |
| T6173 | 2024-09-01 | Refund request | Installation support | I'm facing issues logging into my {product_purchased} account. It says my account is locked. What should I do to unlock it? 1) Please contact me as soon as pos… | Pending | Critical | Phone |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N12152 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Water Sports. |
| N12153 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N12154 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band Critical and support history. |
| N12155 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 1.0000 with category concentration in Water Sports. |
| N12156 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E16772 | TH-C001012-[redacted] | 14 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E16771 | TH-C001012-[redacted] | 13 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E16770 | TH-C001012-[redacted] | 12 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E16769 | TH-C001012-[redacted] | 11 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E16768 | TH-C001012-[redacted] | 10 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL006148 | O051558 | 2025-07-30 | carrier_delay | High | Carrier route delay | Open |
| FUL005989 | O050438 | 2025-07-14 | carrier_delay | High | Carrier route delay | Open |
| FUL005807 | O049234 | 2025-06-26 | carrier_delay | High | Carrier route delay | Open |
| FUL005364 | O046262 | 2025-05-14 | carrier_delay | High | Carrier route delay | Open |
| FUL003736 | O034881 | 2024-11-29 | carrier_delay | High | Carrier route delay | Open |

## H032 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Home Office
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: Pacific Asia
- primary_region: Central America
- total_orders: 8
- total_sales: 4851.39
- total_profit: 991.42
- late_delivery_count: 16
- late_delivery_rate: 0.6667
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-06-04

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O060664 | 2025-12-10 | 2025-12-15 | COMPLETE | Late delivery | 1 | Standard Class | 129.99 | 13.22 | 116.99 | 4 | 5 | Late |
| O042507 | 2025-03-20 | 2025-03-23 | COMPLETE | Late delivery | 1 | Second Class | 229.95 | 50.41 | 222.05 | 2 | 3 | Late |
| O041459 | 2025-03-05 | 2025-03-10 | COMPLETE | Late delivery | 1 | Second Class | 589.96 | 208.53 | 520.16 | 2 | 5 | Late |
| O035915 | 2024-12-14 | 2024-12-20 | COMPLETE | Late delivery | 1 | Standard Class | 129.99 | 48.63 | 113.09 | 4 | 6 | Late |
| O029690 | 2024-09-14 | 2024-09-16 | PROCESSING | Late delivery | 1 | First Class | 959.95 | 220.68 | 868.35 | 1 | 2 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T6195 | 2026-02-21 | Technical issue | Software bug | The {product_purchased} is unable to establish a stable internet connection. It keeps disconnecting intermittently. How can I troubleshoot this network problem… | Open | Low | Phone |  |  |  | Neutral |
| T6193 | 2024-10-30 | Product inquiry | Delivery problem | There seems to be a hardware problem with my {product_purchased}. The screen is flickering, and I'm unable to use it. What should I do?  Can't do anything ab… | Open | Low | Chat |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N12749 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.6667 with category concentration in Men's Footwear. |
| N12750 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E17774 | TH-C001126-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E17772 | TH-C001126-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E17771 | TH-C001126-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E17767 | TH-C001126-[redacted] | 1 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL007450 | O060664 | 2025-12-10 | carrier_delay | High | Carrier route delay | Open |
| FUL004835 | O042507 | 2025-03-20 | carrier_delay | High | Carrier route delay | Open |
| FUL004669 | O041459 | 2025-03-05 | carrier_delay | High | Carrier route delay | Open |
| FUL003887 | O035915 | 2024-12-14 | carrier_delay | High | Carrier route delay | Open |
| FUL002994 | O029690 | 2024-09-14 | carrier_delay | High | Carrier route delay | Open |

## H033 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Corporate
- customer_country: EE. UU.
- customer_state: TX
- customer_city: Richardson
- primary_market: Pacific Asia
- primary_region: West Asia
- total_orders: 5
- total_sales: 4694.64
- total_profit: 810.28
- late_delivery_count: 9
- late_delivery_rate: 0.4286
- support_ticket_count: 1
- open_support_ticket_count: 1
- last_meaningful_touch_date: 2017-04-02
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O056341 | 2025-10-08 | 2025-10-10 | PENDING_PAYMENT | Advance shipping | 0 | Standard Class | 749.94 | 161.75 | 712.94 | 4 | 2 |  |
| O051220 | 2025-07-25 | 2025-07-31 | COMPLETE | Late delivery | 1 | Standard Class | 1319.88 | 159.6 | 1203.28 | 4 | 6 | Late |
| O042418 | 2025-03-19 | 2025-03-23 | PENDING_PAYMENT | Shipping on time | 0 | Standard Class | 999.95 | 342.81 | 891.95 | 4 | 4 |  |
| O040336 | 2025-02-16 | 2025-02-18 | COMPLETE | Shipping on time | 0 | Second Class | 854.96 | -34.75 | 741.41 | 2 | 2 |  |
| O010780 | 2023-12-13 | 2023-12-19 | COMPLETE | Late delivery | 1 | Standard Class | 769.91 | 180.87 | 692.04 | 4 | 6 | Late |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N13579 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer-success owner should align response tone with [redacted] scenario. |
| N13575 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N13577 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.4286 with category concentration in Women's Apparel. |
| N13578 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E19194 | TH-C001297-[redacted] | 14 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E19192 | TH-C001297-[redacted] | 12 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E19190 | TH-C001297-[redacted] | 10 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E19186 | TH-C001297-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E19184 | TH-C001297-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL006102 | O051220 | 2025-07-25 | carrier_delay | High | Carrier route delay | Open |
| FUL000115 | O010780 | 2023-12-13 | carrier_delay | High | Carrier route delay | Open |

## H034 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: EE. UU.
- customer_state: MD
- customer_city: Glen Burnie
- primary_market: USCA
- primary_region: East of USA
- total_orders: 8
- total_sales: 4827.36
- total_profit: -128.0
- late_delivery_count: 13
- late_delivery_rate: 0.5
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-04-07
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O056688 | 2025-10-13 | 2025-10-17 | COMPLETE | Shipping on time | 0 | Standard Class | 629.86 | 70.03 | 535.37 | 4 | 4 |  |
| O039257 | 2025-02-01 | 2025-02-03 | COMPLETE | Late delivery | 1 | First Class | 679.91 | -56.38 | 588.67 | 1 | 2 | Late |
| O036524 | 2024-12-23 | 2024-12-28 | CANCELED | Shipping canceled | 0 | Second Class | 637.88 | 186.92 | 531.5 | 2 | 5 | Canceled |
| O033443 | 2024-11-08 | 2024-11-12 | COMPLETE | Shipping on time | 0 | Standard Class | 989.88 | 0.96 | 926.68 | 4 | 4 |  |
| O028664 | 2024-08-30 | 2024-09-04 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 439.97 | -210.58 | 366.77 | 4 | 5 | Late |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N12875 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer-success owner should align response tone with [redacted] scenario. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E17991 | TH-C001155-[redacted] | 13 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E17990 | TH-C001155-[redacted] | 12 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL004352 | O039257 | 2025-02-01 | carrier_delay | High | Carrier route delay | Open |
| FUL003967 | O036524 | 2024-12-23 | cancellation_review | Medium | Customer or fulfillment cancellation | Closed |
| FUL002853 | O028664 | 2024-08-30 | carrier_delay | High | Carrier route delay | Open |
| FUL001031 | O016814 | 2024-03-10 | cancellation_review | Medium | Customer or fulfillment cancellation | Closed |
| FUL000243 | O011546 | 2023-12-24 | carrier_delay | High | Carrier route delay | Open |

## H035 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Corporate
- customer_country: EE. UU.
- customer_state: CA
- customer_city: Davis
- primary_market: USCA
- primary_region: North Africa
- total_orders: 5
- total_sales: 4289.63
- total_profit: 549.03
- late_delivery_count: 11
- late_delivery_rate: 0.55
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-04-24
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O057850 | 2025-10-30 | 2025-11-05 | PENDING_PAYMENT | Late delivery | 1 | Second Class | 1259.94 | 494.86 | 1170.14 | 2 | 6 | Late |
| O041352 | 2025-03-03 | 2025-03-05 | COMPLETE | Late delivery | 1 | First Class | 593.91 | 213.57 | 519.22 | 1 | 2 | Late |
| O040623 | 2025-02-20 | 2025-02-24 | PENDING_PAYMENT | Shipping on time | 0 | Standard Class | 1149.9 | -567.86 | 1009.41 | 4 | 4 |  |
| O035740 | 2024-12-11 | 2024-12-17 | PENDING | Late delivery | 1 | Second Class | 299.95 | 101.23 | 269.96 | 2 | 6 | Late |
| O022758 | 2024-06-05 | 2024-06-09 | COMPLETE | Shipping on time | 0 | Standard Class | 985.93 | 307.23 | 938.93 | 4 | 4 |  |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N16554 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N16557 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |
| N16559 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Monitor whether the next interaction with the customer resolves the current [redacted] thread. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E24261 | TH-C001879-[redacted] | 13 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E24258 | TH-C001879-[redacted] | 10 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E24257 | TH-C001879-[redacted] | 9 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E24256 | TH-C001879-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E24250 | TH-C001879-[redacted] | 2 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL007052 | O057850 | 2025-10-30 | carrier_delay | High | Carrier route delay | Open |
| FUL004650 | O041352 | 2025-03-03 | carrier_delay | High | Carrier route delay | Open |
| FUL003855 | O035740 | 2024-12-11 | carrier_delay | High | Carrier route delay | Open |

## H036 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: LATAM
- primary_region: Western Europe
- total_orders: 5
- total_sales: 4406.5
- total_profit: -527.18
- late_delivery_count: 18
- late_delivery_rate: 0.8182
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-06-25

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O062074 | 2025-12-31 | 2026-01-05 | PENDING_PAYMENT | Late delivery | 1 | Second Class | 1699.87 | -337.88 | 1467.39 | 2 | 5 | Late |
| O031614 | 2024-10-12 | 2024-10-17 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 609.91 | 127.02 | 540.32 | 4 | 5 | Late |
| O025089 | 2024-07-09 | 2024-07-14 | PROCESSING | Late delivery | 1 | Standard Class | 599.86 | -297.23 | 543.92 | 4 | 5 | Late |
| O008600 | 2023-11-11 | 2023-11-17 | CLOSED | Late delivery | 1 | Second Class | 694.95 | -232.66 | 654.85 | 2 | 6 | Late |
| O006718 | 2023-10-15 | 2023-10-19 | PROCESSING | Shipping on time | 0 | Standard Class | 801.91 | 213.57 | 747.31 | 4 | 4 |  |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T6555 | 2026-03-16 | Cancellation request | Product compatibility | I'm having an issue with the {product_purchased}. Please assist.  Here is an example:  {product_purchased} My cart is: 【Suit】  The product is: I'm unable… | Open | High | Email |  |  |  | Neutral |
| T5427 | 2025-09-30 | Billing inquiry | Installation support | I've accidentally deleted important data from my {product_purchased}. Is there any way to recover the deleted files? I need them urgently. A large amount of ti… | Pending | High | Email |  |  |  | Neutral |
| T6554 | 2025-03-26 | Billing inquiry | Installation support | I've noticed a software bug in the {product_purchased} app. It's causing data loss and unexpected errors. How can I resolve this issue? Write the following com… | Closed | High | Email | Likely instead government article throughout term bring. | 0.0 | 2.0 | Negative |
| T5425 | 2024-09-28 | Product inquiry | Hardware issue | I'm having an issue with the {product_purchased}. Please assist. It does my job and I have no need or desire to pay you.  You need to be willing to pay for a… | Pending | High | Chat |  |  |  | Neutral |
| T5429 | 2024-08-22 | Refund request | Hardware issue | I'm having an issue with the {product_purchased}. Please assist.  "I do not believe I can get any further information on the {product_purchased}. Thank you f… | Closed | High | Phone | Heart since laugh phone southern trade white. | 0.0 | 3.0 | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N15824 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Men's Footwear. |
| N15825 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N15826 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band High and support history. |
| N15827 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.8182 with category concentration in Men's Footwear. |
| N15828 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E23012 | TH-C001726-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E23011 | TH-C001726-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E23010 | TH-C001726-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E23009 | TH-C001726-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E23008 | TH-C001726-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL007648 | O062074 | 2025-12-31 | carrier_delay | High | Carrier route delay | Open |
| FUL003276 | O031614 | 2024-10-12 | carrier_delay | High | Carrier route delay | Open |
| FUL002312 | O025089 | 2024-07-09 | carrier_delay | High | Carrier route delay | Open |
| FUL008891 | O008600 | 2023-11-11 | carrier_delay | High | Carrier route delay | Open |

## H037 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: Europe
- primary_region: Western Europe
- total_orders: 7
- total_sales: 5851.28
- total_profit: 1086.99
- late_delivery_count: 15
- late_delivery_rate: 0.5769
- support_ticket_count: 1
- open_support_ticket_count: 1
- last_meaningful_touch_date: 2017-08-27
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O066382 | 2026-03-04 | 2026-03-07 | PENDING_PAYMENT | Advance shipping | 0 | Standard Class | 1029.93 | 84.84 | 912.64 | 4 | 3 |  |
| O065967 | 2026-02-25 | 2026-02-28 | COMPLETE | Advance shipping | 0 | Standard Class | 319.94 | 48.68 | 266.55 | 4 | 3 |  |
| O054455 | 2025-09-10 | 2025-09-16 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 1499.89 | 256.18 | 1253.9 | 4 | 6 | Late |
| O043120 | 2025-03-29 | 2025-04-04 | PENDING_PAYMENT | Late delivery | 1 | Second Class | 749.86 | 192.71 | 675.68 | 2 | 6 | Late |
| O025313 | 2024-07-12 | 2024-07-16 | CLOSED | Shipping on time | 0 | Standard Class | 531.89 | 116.74 | 485.5 | 4 | 4 |  |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N9071 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.5769 with category concentration in Cleats. |
| N9075 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Escalation summary for the customer: protect revenue, close open issues, and document human review. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E11523 | TH-C000403-[redacted] | 13 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E11522 | TH-C000403-[redacted] | 12 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL006555 | O054455 | 2025-09-10 | carrier_delay | High | Carrier route delay | Open |
| FUL004929 | O043120 | 2025-03-29 | carrier_delay | High | Carrier route delay | Open |
| FUL003172 | O003089 | 2023-08-23 | carrier_delay | High | Carrier route delay | Open |

## H038 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: Africa
- primary_region: North Africa
- total_orders: 9
- total_sales: 6444.22
- total_profit: 1138.51
- late_delivery_count: 14
- late_delivery_rate: 0.4828
- support_ticket_count: 1
- open_support_ticket_count: 1
- last_meaningful_touch_date: 2017-05-13
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O059164 | 2025-11-18 | 2025-11-23 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 449.92 | -84.1 | 401.42 | 4 | 5 | Late |
| O049056 | 2025-06-24 | 2025-06-26 | COMPLETE | Shipping on time | 0 | Second Class | 799.94 | 266.98 | 659.95 | 2 | 2 |  |
| O045553 | 2025-05-03 | 2025-05-07 | CLOSED | Shipping on time | 0 | Standard Class | 1099.83 | 212.9 | 978.34 | 4 | 4 |  |
| O043115 | 2025-03-29 | 2025-04-04 | COMPLETE | Late delivery | 1 | Standard Class | 344.94 | 99.83 | 312.39 | 4 | 6 | Late |
| O042379 | 2025-03-18 | 2025-03-20 | CLOSED | Late delivery | 1 | First Class | 499.95 | 134.39 | 479.95 | 1 | 2 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T6112 | 2025-10-13 | Refund request | Cancellation request | I've forgotten my password for my {product_purchased} account, and the password reset option is not working. How can I recover my account?  Note that althoug… | Pending | Low | Social media |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N8106 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Monitor whether the next interaction with the customer resolves the current [redacted] thread. |
| N8107 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Escalation summary for the customer: protect revenue, close open issues, and document human review. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E9878 | TH-C000216-[redacted] | 14 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E9877 | TH-C000216-[redacted] | 13 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E9873 | TH-C000216-[redacted] | 9 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E9869 | TH-C000216-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E9868 | TH-C000216-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL007232 | O059164 | 2025-11-18 | carrier_delay | High | Carrier route delay | Open |
| FUL004927 | O043115 | 2025-03-29 | carrier_delay | High | Carrier route delay | Open |
| FUL004815 | O042379 | 2025-03-18 | carrier_delay | High | Carrier route delay | Open |
| FUL003358 | O032204 | 2024-10-21 | carrier_delay | High | Carrier route delay | Open |
| FUL004294 | O003884 | 2023-09-03 | carrier_delay | High | Carrier route delay | Open |

## H039 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: Pacific Asia
- primary_region: Central America
- total_orders: 9
- total_sales: 6054.27
- total_profit: 1114.25
- late_delivery_count: 14
- late_delivery_rate: 0.4828
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-05-07

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O058748 | 2025-11-12 | 2025-11-16 | PENDING | Shipping on time | 0 | Standard Class | 1199.74 | 316.76 | 1132.25 | 4 | 4 |  |
| O053684 | 2025-08-30 | 2025-09-04 | COMPLETE | Late delivery | 1 | Standard Class | 199.99 | 95.0 | 189.99 | 4 | 5 | Late |
| O050866 | 2025-07-20 | 2025-07-22 | CLOSED | Late delivery | 1 | First Class | 699.92 | 150.22 | 642.22 | 1 | 2 | Late |
| O041898 | 2025-03-11 | 2025-03-15 | PROCESSING | Late delivery | 1 | Second Class | 439.97 | 145.64 | 387.17 | 2 | 4 | Late |
| O041398 | 2025-03-04 | 2025-03-06 | COMPLETE | Late delivery | 1 | First Class | 949.91 | 69.75 | 922.91 | 1 | 2 | Late |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N8653 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N8652 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Indoor/Outdoor Games. |
| N8656 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |
| N8654 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band Medium and support history. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E10804 | TH-C000318-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E10802 | TH-C000318-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E10801 | TH-C000318-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E10798 | TH-C000318-[redacted] | 2 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E10797 | TH-C000318-[redacted] | 1 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL006454 | O053684 | 2025-08-30 | carrier_delay | High | Carrier route delay | Open |
| FUL006051 | O050866 | 2025-07-20 | carrier_delay | High | Carrier route delay | Open |
| FUL004739 | O041898 | 2025-03-11 | carrier_delay | High | Carrier route delay | Open |
| FUL004657 | O041398 | 2025-03-04 | carrier_delay | High | Carrier route delay | Open |
| FUL001849 | O022155 | 2024-05-27 | carrier_delay | High | Carrier route delay | Open |

## H040 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Home Office
- customer_country: EE. UU.
- customer_state: TX
- customer_city: San Antonio
- primary_market: Pacific Asia
- primary_region: South America
- total_orders: 6
- total_sales: 5919.28
- total_profit: 127.48
- late_delivery_count: 18
- late_delivery_rate: 0.7826
- support_ticket_count: 1
- open_support_ticket_count: 1
- last_meaningful_touch_date: 2017-07-08
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O063017 | 2026-01-13 | 2026-01-14 | PENDING_PAYMENT | Late delivery | 1 | Same Day | 899.91 | 174.79 | 858.01 | 0 | 1 | Late |
| O045233 | 2025-04-29 | 2025-05-01 | COMPLETE | Late delivery | 1 | First Class | 879.86 | 225.02 | 792.17 | 1 | 2 | Late |
| O033130 | 2024-11-03 | 2024-11-09 | ON_HOLD | Late delivery | 1 | Standard Class | 999.91 | -64.99 | 863.92 | 4 | 6 | Late |
| O029830 | 2024-09-16 | 2024-09-22 | COMPLETE | Late delivery | 1 | Standard Class | 979.86 | 315.28 | 909.97 | 4 | 6 | Late |
| O021712 | 2024-05-20 | 2024-05-23 | ON_HOLD | Late delivery | 1 | Second Class | 719.93 | -136.45 | 682.13 | 2 | 3 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T5679 | 2026-04-27 | Cancellation request | Refund request | I'm having an issue with the {product_purchased}. Please assist. https://help.fitnesscouch.com/support/help This problem started occurring after the recent sof… | Closed | Medium | Social media | Himself challenge Congress source behavior success economy. | 0.0 | 3.0 | Neutral |
| T5321 | 2025-12-10 | Cancellation request | Software bug | I'm having an issue with the {product_purchased}. Please assist. Please send an email to us with suggestions. A product purchased has the ability to allow us t… | Closed | Medium | Email | Argue national white peace. | 0.0 | 4.0 | Positive |
| T6696 | 2025-03-13 | Billing inquiry | Payment issue | I'm having an issue with the {product_purchased}. Please assist.   Thank you for your prompt and helpful service.   I'm having an issue with the {product… | Open | Medium | Phone |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N8980 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Cleats. |
| N8981 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N8982 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band High and support history. |
| N8983 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.7826 with category concentration in Cleats. |
| N8984 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E11370 | TH-C000383-[redacted] | 14 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E11369 | TH-C000383-[redacted] | 13 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E11368 | TH-C000383-[redacted] | 12 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E11367 | TH-C000383-[redacted] | 11 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E11366 | TH-C000383-[redacted] | 10 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL007776 | O063017 | 2026-01-13 | carrier_delay | High | Carrier route delay | Open |
| FUL005216 | O045233 | 2025-04-29 | carrier_delay | High | Carrier route delay | Open |
| FUL003491 | O033130 | 2024-11-03 | carrier_delay | High | Carrier route delay | Open |
| FUL003025 | O029830 | 2024-09-16 | carrier_delay | High | Carrier route delay | Open |
| FUL001781 | O021712 | 2024-05-20 | carrier_delay | High | Carrier route delay | Open |

## H041 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: EE. UU.
- customer_state: NV
- customer_city: Las Vegas
- primary_market: USCA
- primary_region: Eastern Asia
- total_orders: 7
- total_sales: 5839.46
- total_profit: -89.85
- late_delivery_count: 18
- late_delivery_rate: 0.72
- support_ticket_count: 1
- open_support_ticket_count: 1
- last_meaningful_touch_date: 2017-01-01

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O050092 | 2025-07-09 | 2025-07-12 | PENDING_PAYMENT | Advance shipping | 0 | Standard Class | 59.99 | 2.55 | 50.99 | 4 | 3 |  |
| O049924 | 2025-07-06 | 2025-07-08 | COMPLETE | Late delivery | 1 | First Class | 529.95 | 97.89 | 453.76 | 1 | 2 | Late |
| O041206 | 2025-03-01 | 2025-03-03 | PENDING | Advance shipping | 0 | Standard Class | 1299.92 | 259.3 | 1155.93 | 4 | 2 |  |
| O024709 | 2024-07-03 | 2024-07-08 | COMPLETE | Late delivery | 1 | Standard Class | 1129.84 | -19.67 | 1053.06 | 4 | 5 | Late |
| O024491 | 2024-06-30 | 2024-07-02 | PENDING | Advance shipping | 0 | Standard Class | 299.95 | -470.17 | 284.95 | 4 | 2 |  |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N9114 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |
| N9113 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.7200 with category concentration in Cardio Equipment. |
| N9111 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N9110 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Cardio Equipment. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E11592 | TH-C000412-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E11591 | TH-C000412-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E11588 | TH-C000412-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E11586 | TH-C000412-[redacted] | 2 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E11585 | TH-C000412-[redacted] | 1 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL005911 | O049924 | 2025-07-06 | carrier_delay | High | Carrier route delay | Open |
| FUL002243 | O024709 | 2024-07-03 | carrier_delay | High | Carrier route delay | Open |
| FUL001428 | O019396 | 2024-04-17 | carrier_delay | High | Carrier route delay | Open |
| FUL006364 | O005299 | 2023-09-24 | carrier_delay | High | Carrier route delay | Open |

## H042 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Corporate
- customer_country: EE. UU.
- customer_state: FL
- customer_city: Miami
- primary_market: LATAM
- primary_region: Central America
- total_orders: 6
- total_sales: 4449.5
- total_profit: 565.77
- late_delivery_count: 9
- late_delivery_rate: 0.45
- support_ticket_count: 1
- open_support_ticket_count: 1
- last_meaningful_touch_date: 2017-09-08

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O067207 | 2026-03-16 | 2026-03-19 | PENDING_PAYMENT | Advance shipping | 0 | Standard Class | 929.84 | 49.16 | 849.94 | 4 | 3 |  |
| O063976 | 2026-01-27 | 2026-01-29 | CLOSED | Shipping on time | 0 | Second Class | 919.93 | 179.18 | 839.94 | 2 | 2 |  |
| O059770 | 2025-11-27 | 2025-11-29 | PENDING_PAYMENT | Late delivery | 1 | First Class | 769.96 | 271.97 | 709.46 | 1 | 2 | Late |
| O020877 | 2024-05-08 | 2024-05-11 | PENDING_PAYMENT | Advance shipping | 0 | Standard Class | 499.94 | -50.37 | 415.04 | 4 | 3 |  |
| O015133 | 2024-02-14 | 2024-02-18 | COMPLETE | Late delivery | 1 | Second Class | 59.99 | 13.65 | 54.59 | 2 | 4 | Late |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N15343 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band Low and support history. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E22192 | TH-C001636-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E22191 | TH-C001636-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E22190 | TH-C001636-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E22188 | TH-C001636-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E22187 | TH-C001636-[redacted] | 3 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL007313 | O059770 | 2025-11-27 | carrier_delay | High | Carrier route delay | Open |
| FUL000779 | O015133 | 2024-02-14 | carrier_delay | High | Carrier route delay | Open |
| FUL001499 | O001992 | 2023-08-07 | carrier_delay | High | Carrier route delay | Open |

## H043 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: EE. UU.
- customer_state: CA
- customer_city: Winnetka
- primary_market: Europe
- primary_region: Western Europe
- total_orders: 5
- total_sales: 4534.45
- total_profit: 970.36
- late_delivery_count: 12
- late_delivery_rate: 0.5714
- support_ticket_count: 1
- open_support_ticket_count: 1
- last_meaningful_touch_date: 2016-02-27

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O028922 | 2024-09-03 | 2024-09-06 | COMPLETE | Advance shipping | 0 | Standard Class | 879.94 | 42.23 | 815.64 | 4 | 3 |  |
| O019775 | 2024-04-22 | 2024-04-28 | PROCESSING | Late delivery | 1 | Standard Class | 1079.92 | 189.62 | 984.72 | 4 | 6 | Late |
| O017974 | 2024-03-27 | 2024-04-01 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 679.84 | 166.42 | 606.04 | 4 | 5 | Late |
| O011895 | 2023-12-29 | 2024-01-04 | COMPLETE | Late delivery | 1 | Second Class | 509.95 | 167.96 | 449.65 | 2 | 6 | Late |
| O006356 | 2023-10-09 | 2023-10-11 | ON_HOLD | Advance shipping | 0 | Standard Class | 1384.8 | 404.13 | 1340.6 | 4 | 2 |  |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N14720 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Cleats. |
| N14723 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.5714 with category concentration in Cleats. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E21131 | TH-C001513-[redacted] | 3 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E21130 | TH-C001513-[redacted] | 2 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL001477 | O019775 | 2024-04-22 | carrier_delay | High | Carrier route delay | Open |
| FUL001205 | O017974 | 2024-03-27 | carrier_delay | High | Carrier route delay | Open |
| FUL000292 | O011895 | 2023-12-29 | carrier_delay | High | Carrier route delay | Open |

## H044 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: Pacific Asia
- primary_region: Southeast Asia
- total_orders: 7
- total_sales: 4904.27
- total_profit: -81.6
- late_delivery_count: 16
- late_delivery_rate: 0.6667
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2016-08-11

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O040327 | 2025-02-16 | 2025-02-19 | COMPLETE | Advance shipping | 0 | Standard Class | 499.93 | 100.38 | 469.94 | 4 | 3 |  |
| O033497 | 2024-11-08 | 2024-11-10 | CLOSED | Late delivery | 1 | First Class | 939.92 | -1043.99 | 880.52 | 1 | 2 | Late |
| O030926 | 2024-10-02 | 2024-10-04 | PENDING_PAYMENT | Advance shipping | 0 | Standard Class | 709.91 | 237.68 | 695.12 | 4 | 2 |  |
| O029324 | 2024-09-09 | 2024-09-14 | PENDING | Late delivery | 1 | Standard Class | 1124.83 | 265.97 | 953.97 | 4 | 5 | Late |
| O022047 | 2024-05-25 | 2024-05-28 | CLOSED | Late delivery | 1 | Second Class | 989.87 | 244.32 | 866.19 | 2 | 3 | Late |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N12463 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Fishing. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E17292 | TH-C001067-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E17291 | TH-C001067-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E17290 | TH-C001067-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E17289 | TH-C001067-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E17288 | TH-C001067-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL003543 | O033497 | 2024-11-08 | carrier_delay | High | Carrier route delay | Open |
| FUL002938 | O029324 | 2024-09-09 | carrier_delay | High | Carrier route delay | Open |
| FUL001829 | O022047 | 2024-05-25 | carrier_delay | High | Carrier route delay | Open |
| FUL008834 | O008244 | 2023-11-06 | carrier_delay | High | Carrier route delay | Open |

## H045 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Corporate
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: Europe
- primary_region: South America
- total_orders: 8
- total_sales: 5047.13
- total_profit: 365.94
- late_delivery_count: 23
- late_delivery_rate: 0.9583
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-09-29
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O068688 | 2026-04-06 | 2026-04-08 | COMPLETE | Late delivery | 1 | First Class | 399.97 | 64.49 | 338.98 | 1 | 2 | Late |
| O065869 | 2026-02-24 | 2026-03-01 | COMPLETE | Late delivery | 1 | Standard Class | 959.68 | 186.5 | 838.13 | 4 | 5 | Late |
| O063481 | 2026-01-20 | 2026-01-21 | PENDING_PAYMENT | Late delivery | 1 | Same Day | 396.0 | 58.74 | 360.36 | 0 | 1 | Late |
| O050411 | 2025-07-13 | 2025-07-15 | PENDING | Advance shipping | 0 | Standard Class | 129.99 | -4.94 | 129.99 | 4 | 2 |  |
| O036521 | 2024-12-23 | 2024-12-25 | PENDING_PAYMENT | Late delivery | 1 | First Class | 599.93 | 130.21 | 532.44 | 1 | 2 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T6712 | 2025-05-05 | Refund request | Display issue | I'm having an issue with the {product_purchased}. Please assist.  If you've seen it before, this is probably your number one choice for the item.  You prob… | Pending | Critical | Email |  |  |  | Neutral |
| T6697 | 2025-04-19 | Refund request | Data loss | I'm having an issue with the {product_purchased}. Please assist.  [23/12/2014, 5:19:19 AM - Thread: 1 -> Loading my cart]  [23/12/2014, I've reviewed the t… | Open | Critical | Email |  |  |  | Neutral |
| T5306 | 2024-12-18 | Cancellation request | Refund request | I'm having an issue with the {product_purchased}. Please assist.  {product_purchased} is no longer listed on the  {product_purchased} table. This problem s… | Open | Critical | Chat |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N11842 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Cleats. |
| N11843 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N11844 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band High and support history. |
| N11845 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.9583 with category concentration in Cleats. |
| N11846 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E16240 | TH-C000947-[redacted] | 14 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E16239 | TH-C000947-[redacted] | 13 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E16238 | TH-C000947-[redacted] | 12 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E16237 | TH-C000947-[redacted] | 11 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E16236 | TH-C000947-[redacted] | 10 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL008608 | O068688 | 2026-04-06 | carrier_delay | High | Carrier route delay | Open |
| FUL008193 | O065869 | 2026-02-24 | carrier_delay | High | Carrier route delay | Open |
| FUL007846 | O063481 | 2026-01-20 | carrier_delay | High | Carrier route delay | Open |
| FUL003966 | O036521 | 2024-12-23 | carrier_delay | High | Carrier route delay | Open |
| FUL002910 | O029100 | 2024-09-05 | carrier_delay | High | Carrier route delay | Open |

## H046 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: EE. UU.
- customer_state: MO
- customer_city: Saint Charles
- primary_market: USCA
- primary_region: US Center
- total_orders: 7
- total_sales: 4429.59
- total_profit: 1158.78
- late_delivery_count: 8
- late_delivery_rate: 0.4706
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2016-11-02
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O046007 | 2025-05-10 | 2025-05-13 | PENDING_PAYMENT | Advance shipping | 0 | Standard Class | 1029.92 | 263.9 | 905.03 | 4 | 3 |  |
| O036899 | 2024-12-28 | 2025-01-02 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 289.95 | 97.75 | 275.35 | 4 | 5 | Late |
| O035943 | 2024-12-14 | 2024-12-18 | COMPLETE | Shipping on time | 0 | Standard Class | 919.9 | 147.39 | 830.3 | 4 | 4 |  |
| O035375 | 2024-12-06 | 2024-12-08 | PENDING_PAYMENT | Late delivery | 1 | First Class | 879.93 | 264.42 | 786.53 | 1 | 2 | Late |
| O033030 | 2024-11-02 | 2024-11-02 | PENDING_PAYMENT | Shipping on time | 0 | Same Day | 199.99 | 75.0 | 199.99 | 0 | 0 |  |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T6902 | 2025-08-10 | Cancellation request | Peripheral compatibility | I'm having an issue with the {product_purchased}. Please assist.   [08:01:29] [Client thread/INFO]: [CHAT] [Server: I want the package ID to be 'C:\Program … | Closed | Low | Phone | Law stop cut past generation. | 6.6 | 3.0 | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N15580 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Escalation summary for the customer: protect revenue, close open issues, and document human review. |
| N15578 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer-success owner should align response tone with [redacted] scenario. |
| N15575 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band Medium and support history. |
| N15576 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.4706 with category concentration in Cleats. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E22587 | TH-C001680-[redacted] | 11 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E22581 | TH-C001680-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL004028 | O036899 | 2024-12-28 | carrier_delay | High | Carrier route delay | Open |
| FUL003807 | O035375 | 2024-12-06 | carrier_delay | High | Carrier route delay | Open |
| FUL001067 | O017025 | 2024-03-13 | carrier_delay | High | Carrier route delay | Open |

## H047 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Corporate
- customer_country: EE. UU.
- customer_state: CA
- customer_city: Panorama City
- primary_market: USCA
- primary_region: Caribbean
- total_orders: 6
- total_sales: 4427.57
- total_profit: 905.07
- late_delivery_count: 10
- late_delivery_rate: 0.5
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-09-14

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O067653 | 2026-03-22 | 2026-03-26 | COMPLETE | Shipping on time | 0 | Standard Class | 329.98 | 106.84 | 277.18 | 4 | 4 |  |
| O053772 | 2025-08-31 | 2025-09-01 | PENDING_PAYMENT | Late delivery | 1 | Same Day | 1007.85 | 229.04 | 889.23 | 0 | 1 | Late |
| O038531 | 2025-01-21 | 2025-01-23 | PENDING | Advance shipping | 0 | Standard Class | 879.93 | 201.87 | 821.03 | 4 | 2 |  |
| O033329 | 2024-11-06 | 2024-11-08 | PENDING_PAYMENT | Late delivery | 1 | First Class | 679.94 | 54.18 | 562.34 | 1 | 2 | Late |
| O029020 | 2024-09-04 | 2024-09-10 | COMPLETE | Late delivery | 1 | Second Class | 179.94 | 36.6 | 164.34 | 2 | 6 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T6881 | 2024-11-15 | Product inquiry | Battery life | I'm having an issue with the {product_purchased}. Please assist.  (6) If the customer's name or ID is not on the Product Status Form, there may be an error r… | Open | Low | Chat |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N15613 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |
| N15612 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.5000 with category concentration in Camping & Hiking. |
| N15610 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N15611 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band Medium and support history. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E22645 | TH-C001689-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E22643 | TH-C001689-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E22642 | TH-C001689-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E22640 | TH-C001689-[redacted] | 2 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL006463 | O053772 | 2025-08-31 | carrier_delay | High | Carrier route delay | Open |
| FUL003517 | O033329 | 2024-11-06 | carrier_delay | High | Carrier route delay | Open |
| FUL002902 | O029020 | 2024-09-04 | carrier_delay | High | Carrier route delay | Open |

## H048 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Home Office
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: Europe
- primary_region: Western Europe
- total_orders: 7
- total_sales: 4359.47
- total_profit: 52.25
- late_delivery_count: 13
- late_delivery_rate: 0.65
- support_ticket_count: 1
- open_support_ticket_count: 1
- last_meaningful_touch_date: 2017-09-27

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O068519 | 2026-04-04 | 2026-04-09 | COMPLETE | Late delivery | 1 | Standard Class | 679.95 | 125.69 | 631.8 | 4 | 5 | Late |
| O065264 | 2026-02-15 | 2026-02-20 | PENDING_PAYMENT | Late delivery | 1 | Second Class | 379.99 | 115.95 | 325.59 | 2 | 5 | Late |
| O063641 | 2026-01-22 | 2026-01-24 | ON_HOLD | Advance shipping | 0 | Standard Class | 1199.84 | 139.23 | 1046.85 | 4 | 2 |  |
| O061956 | 2025-12-29 | 2025-12-31 | PENDING | Late delivery | 1 | First Class | 299.95 | 70.86 | 283.45 | 1 | 2 | Late |
| O046022 | 2025-05-10 | 2025-05-13 | COMPLETE | Advance shipping | 0 | Standard Class | 309.96 | 35.13 | 246.26 | 4 | 3 |  |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N16110 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band Medium and support history. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E23495 | TH-C001787-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E23491 | TH-C001787-[redacted] | 3 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E23490 | TH-C001787-[redacted] | 2 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E23489 | TH-C001787-[redacted] | 1 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL008580 | O068519 | 2026-04-04 | carrier_delay | High | Carrier route delay | Open |
| FUL008094 | O065264 | 2026-02-15 | carrier_delay | High | Carrier route delay | Open |
| FUL007628 | O061956 | 2025-12-29 | carrier_delay | High | Carrier route delay | Open |
| FUL003205 | O031114 | 2024-10-05 | carrier_delay | High | Carrier route delay | Open |
| FUL006943 | O005709 | 2023-09-30 | carrier_delay | High | Carrier route delay | Open |

## H049 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Corporate
- customer_country: EE. UU.
- customer_state: CO
- customer_city: Longmont
- primary_market: Pacific Asia
- primary_region: Southeast Asia
- total_orders: 9
- total_sales: 5920.21
- total_profit: 855.76
- late_delivery_count: 16
- late_delivery_rate: 0.5517
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-09-30
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O068760 | 2026-04-07 | 2026-04-08 | COMPLETE | Late delivery | 1 | Same Day | 399.94 | 107.33 | 380.94 | 0 | 1 | Late |
| O044858 | 2025-04-23 | 2025-04-27 | CLOSED | Shipping on time | 0 | Standard Class | 349.98 | 64.49 | 337.48 | 4 | 4 |  |
| O043310 | 2025-04-01 | 2025-04-07 | SUSPECTED_FRAUD | Shipping canceled | 0 | Second Class | 349.93 | -278.69 | 309.94 | 2 | 6 | Canceled |
| O028629 | 2024-08-29 | 2024-09-03 | PENDING_PAYMENT | Late delivery | 1 | Second Class | 779.94 | 239.22 | 666.24 | 2 | 5 | Late |
| O025907 | 2024-07-21 | 2024-07-24 | COMPLETE | Advance shipping | 0 | Standard Class | 804.82 | 225.57 | 763.27 | 4 | 3 |  |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N8967 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N8973 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Escalation summary for the customer: protect revenue, close open issues, and document human review. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E11340 | TH-C000379-[redacted] | 10 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E11339 | TH-C000379-[redacted] | 9 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E11332 | TH-C000379-[redacted] | 2 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL008619 | O068760 | 2026-04-07 | carrier_delay | High | Carrier route delay | Open |
| FUL004952 | O043310 | 2025-04-01 | cancellation_review | Medium | Customer or fulfillment cancellation | Closed |
| FUL002846 | O028629 | 2024-08-29 | carrier_delay | High | Carrier route delay | Open |
| FUL002033 | O023354 | 2024-06-13 | carrier_delay | High | Carrier route delay | Open |
| FUL002451 | O002596 | 2023-08-15 | carrier_delay | High | Carrier route delay | Open |

## H050 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Home Office
- customer_country: EE. UU.
- customer_state: CA
- customer_city: Cerritos
- primary_market: Pacific Asia
- primary_region: Western Europe
- total_orders: 8
- total_sales: 5029.24
- total_profit: 1333.38
- late_delivery_count: 14
- late_delivery_rate: 0.7
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-07-04
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O062697 | 2026-01-09 | 2026-01-12 | PROCESSING | Late delivery | 1 | Second Class | 1229.8 | 446.98 | 1006.34 | 2 | 3 | Late |
| O051957 | 2025-08-05 | 2025-08-08 | COMPLETE | Advance shipping | 0 | Standard Class | 349.93 | 115.15 | 317.68 | 4 | 3 |  |
| O032639 | 2024-10-27 | 2024-11-01 | PROCESSING | Late delivery | 1 | Standard Class | 159.96 | 46.23 | 135.97 | 4 | 5 | Late |
| O030884 | 2024-10-01 | 2024-10-06 | PROCESSING | Late delivery | 1 | Standard Class | 179.97 | 3.42 | 170.97 | 4 | 5 | Late |
| O024695 | 2024-07-03 | 2024-07-09 | PENDING_PAYMENT | Late delivery | 1 | Second Class | 1399.75 | 294.93 | 1238.78 | 2 | 6 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T6775 | 2025-05-08 | Cancellation request | Refund request | I'm having an issue with the {product_purchased}. Please assist. I'm using the original charger that came with my {product_purchased}, but it's not charging pr… | Pending | Low | Phone |  |  |  | Neutral |
| T6773 | 2024-12-14 | Product inquiry | Peripheral compatibility | I'm having an issue with the {product_purchased}. Please assist.   Please enter a valid Steam account.   The name you entered does not match the product … | Closed | Low | Phone | We but grow fill of media. | 3.6 | 3.0 | Neutral |
| T5228 | 2024-07-09 | Cancellation request | Product recommendation | There seems to be a hardware problem with my {product_purchased}. The screen is flickering, and I'm unable to use it. What should I do? This is mostly because … | Pending | Low | Phone |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N11893 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Indoor/Outdoor Games. |
| N11894 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N11895 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band High and support history. |
| N11896 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.7000 with category concentration in Indoor/Outdoor Games. |
| N11897 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E16328 | TH-C000959-[redacted] | 14 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E16327 | TH-C000959-[redacted] | 13 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E16326 | TH-C000959-[redacted] | 12 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E16325 | TH-C000959-[redacted] | 11 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E16324 | TH-C000959-[redacted] | 10 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL007731 | O062697 | 2026-01-09 | carrier_delay | High | Carrier route delay | Open |
| FUL003424 | O032639 | 2024-10-27 | carrier_delay | High | Carrier route delay | Open |
| FUL003171 | O030884 | 2024-10-01 | carrier_delay | High | Carrier route delay | Open |
| FUL002240 | O024695 | 2024-07-03 | carrier_delay | High | Carrier route delay | Open |
| FUL000080 | O010515 | 2023-12-09 | carrier_delay | High | Carrier route delay | Open |

## H051 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Corporate
- customer_country: EE. UU.
- customer_state: LA
- customer_city: New Orleans
- primary_market: LATAM
- primary_region: Central America
- total_orders: 6
- total_sales: 4254.27
- total_profit: 242.35
- late_delivery_count: 16
- late_delivery_rate: 0.7619
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-01-30
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O052095 | 2025-08-07 | 2025-08-13 | COMPLETE | Late delivery | 1 | Standard Class | 1399.84 | 237.2 | 1211.84 | 4 | 6 | Late |
| O024897 | 2024-07-06 | 2024-07-09 | CLOSED | Late delivery | 1 | Second Class | 589.86 | -477.46 | 495.38 | 2 | 3 | Late |
| O008022 | 2023-11-03 | 2023-11-06 | COMPLETE | Advance shipping | 0 | Standard Class | 74.97 | 29.6 | 62.97 | 4 | 3 |  |
| O007984 | 2023-11-02 | 2023-11-07 | PAYMENT_REVIEW | Late delivery | 1 | Second Class | 399.92 | 140.7 | 359.92 | 2 | 5 | Late |
| O007741 | 2023-10-29 | 2023-10-31 | COMPLETE | Advance shipping | 0 | Standard Class | 1019.86 | 243.42 | 900.28 | 4 | 2 |  |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T6763 | 2025-08-16 | Refund request | Hardware issue | I'm facing issues logging into my {product_purchased} account. It says my account is locked. What should I do to unlock it? I've had issues logging into my {pr… | Pending | Medium | Social media |  |  |  | Neutral |
| T5206 | 2025-03-27 | Refund request | Delivery problem | I'm having an issue with the {product_purchased}. Please assist. If you can find the right, you may be able to fix it.  Please let me know and I'll use them … | Closed | Medium | Phone | Employee support economy themselves should remember. | 0.0 | 1.0 | Negative |
| T5225 | 2025-03-19 | Refund request | Network problem | I'm having an issue with the {product_purchased}. Please assist. I'm experiencing this issue on multiple devices of the same model, so it seems to be a widespr… | Open | Medium | Chat |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N16913 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Indoor/Outdoor Games. |
| N16914 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N16915 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band High and support history. |
| N16916 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.7619 with category concentration in Indoor/Outdoor Games. |
| N16917 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E24872 | TH-C001948-[redacted] | 14 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E24871 | TH-C001948-[redacted] | 13 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E24870 | TH-C001948-[redacted] | 12 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E24869 | TH-C001948-[redacted] | 11 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E24868 | TH-C001948-[redacted] | 10 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL006230 | O052095 | 2025-08-07 | carrier_delay | High | Carrier route delay | Open |
| FUL002276 | O024897 | 2024-07-06 | carrier_delay | High | Carrier route delay | Open |
| FUL008794 | O007984 | 2023-11-02 | carrier_delay | High | Carrier route delay | Open |
| FUL001458 | O001965 | 2023-08-06 | carrier_delay | High | Carrier route delay | Open |

## H052 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: EE. UU.
- customer_state: TN
- customer_city: Memphis
- primary_market: LATAM
- primary_region: Central America
- total_orders: 9
- total_sales: 6257.14
- total_profit: -586.11
- late_delivery_count: 17
- late_delivery_rate: 0.5484
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-05-19

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O059574 | 2025-11-24 | 2025-11-26 | PENDING | Late delivery | 1 | First Class | 989.92 | 201.65 | 818.54 | 1 | 2 | Late |
| O054393 | 2025-09-09 | 2025-09-13 | ON_HOLD | Late delivery | 1 | Second Class | 399.91 | 100.78 | 329.93 | 2 | 4 | Late |
| O051895 | 2025-08-04 | 2025-08-10 | SUSPECTED_FRAUD | Shipping canceled | 0 | Standard Class | 919.88 | -79.4 | 877.28 | 4 | 6 | Canceled |
| O041826 | 2025-03-10 | 2025-03-12 | PENDING_PAYMENT | Advance shipping | 0 | Standard Class | 259.95 | 77.49 | 247.76 | 4 | 2 |  |
| O035115 | 2024-12-02 | 2024-12-04 | PROCESSING | Late delivery | 1 | First Class | 349.96 | -497.94 | 313.96 | 1 | 2 | Late |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N8341 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band Medium and support history. |
| N8342 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.5484 with category concentration in Cleats. |
| N8343 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |
| N8340 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E10272 | TH-C000259-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E10271 | TH-C000259-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E10270 | TH-C000259-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E10269 | TH-C000259-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E10268 | TH-C000259-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL007285 | O059574 | 2025-11-24 | carrier_delay | High | Carrier route delay | Open |
| FUL006549 | O054393 | 2025-09-09 | carrier_delay | High | Carrier route delay | Open |
| FUL006196 | O051895 | 2025-08-04 | cancellation_review | Medium | Customer or fulfillment cancellation | Closed |
| FUL003776 | O035115 | 2024-12-02 | carrier_delay | High | Carrier route delay | Open |
| FUL008999 | O009381 | 2023-11-22 | carrier_delay | High | Carrier route delay | Open |

## H053 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: Pacific Asia
- primary_region: South America
- total_orders: 8
- total_sales: 4554.54
- total_profit: 247.35
- late_delivery_count: 14
- late_delivery_rate: 0.6364
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-06-25

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O062103 | 2025-12-31 | 2026-01-04 | COMPLETE | Shipping on time | 0 | Standard Class | 299.98 | 122.84 | 272.98 | 4 | 4 |  |
| O048440 | 2025-06-15 | 2025-06-21 | SUSPECTED_FRAUD | Shipping canceled | 0 | Standard Class | 554.92 | 197.89 | 540.67 | 4 | 6 | Canceled |
| O048408 | 2025-06-14 | 2025-06-18 | PROCESSING | Shipping on time | 0 | Standard Class | 709.96 | 187.77 | 669.46 | 4 | 4 |  |
| O039845 | 2025-02-09 | 2025-02-15 | COMPLETE | Late delivery | 1 | Standard Class | 1329.89 | -427.4 | 1184.39 | 4 | 6 | Late |
| O029833 | 2024-09-16 | 2024-09-18 | PENDING_PAYMENT | Late delivery | 1 | First Class | 679.94 | 4.59 | 558.65 | 1 | 2 | Late |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N14543 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band Medium and support history. |
| N14542 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N14541 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Men's Footwear. |
| N14544 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.6364 with category concentration in Men's Footwear. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E20829 | TH-C001476-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E20828 | TH-C001476-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E20827 | TH-C001476-[redacted] | 3 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E20826 | TH-C001476-[redacted] | 2 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E20825 | TH-C001476-[redacted] | 1 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL005696 | O048440 | 2025-06-15 | cancellation_review | Medium | Customer or fulfillment cancellation | Closed |
| FUL004439 | O039845 | 2025-02-09 | carrier_delay | High | Carrier route delay | Open |
| FUL003027 | O029833 | 2024-09-16 | carrier_delay | High | Carrier route delay | Open |
| FUL000012 | O010050 | 2023-12-02 | carrier_delay | High | Carrier route delay | Open |
| FUL009028 | O009594 | 2023-11-26 | carrier_delay | High | Carrier route delay | Open |

## H054 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Home Office
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: Europe
- primary_region: Western Europe
- total_orders: 8
- total_sales: 5077.44
- total_profit: -362.03
- late_delivery_count: 18
- late_delivery_rate: 0.6923
- support_ticket_count: 1
- open_support_ticket_count: 1
- last_meaningful_touch_date: 2017-06-29
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O062374 | 2026-01-04 | 2026-01-09 | COMPLETE | Late delivery | 1 | Second Class | 509.95 | 148.06 | 499.05 | 2 | 5 | Late |
| O061373 | 2025-12-20 | 2025-12-22 | PENDING | Late delivery | 1 | First Class | 1629.89 | -854.5 | 1500.29 | 1 | 2 | Late |
| O048098 | 2025-06-10 | 2025-06-14 | PENDING_PAYMENT | Shipping on time | 0 | Standard Class | 989.85 | 197.35 | 855.96 | 4 | 4 |  |
| O045402 | 2025-05-01 | 2025-05-04 | CLOSED | Late delivery | 1 | Second Class | 499.96 | 180.05 | 438.16 | 2 | 3 | Late |
| O042579 | 2025-03-21 | 2025-03-22 | PROCESSING | Late delivery | 1 | Same Day | 249.97 | 52.07 | 207.37 | 0 | 1 | Late |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N11713 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.6923 with category concentration in Men's Footwear. |
| N11717 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Escalation summary for the customer: protect revenue, close open issues, and document human review. |
| N11710 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Men's Footwear. |
| N11714 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E16014 | TH-C000923-[redacted] | 14 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E16010 | TH-C000923-[redacted] | 10 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E16009 | TH-C000923-[redacted] | 9 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E16005 | TH-C000923-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E16003 | TH-C000923-[redacted] | 3 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL007690 | O062374 | 2026-01-04 | carrier_delay | High | Carrier route delay | Open |
| FUL007547 | O061373 | 2025-12-20 | carrier_delay | High | Carrier route delay | Open |
| FUL005245 | O045402 | 2025-05-01 | carrier_delay | High | Carrier route delay | Open |
| FUL004844 | O042579 | 2025-03-21 | carrier_delay | High | Carrier route delay | Open |
| FUL004566 | O040764 | 2025-02-23 | carrier_delay | High | Carrier route delay | Open |

## H055 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Corporate
- customer_country: EE. UU.
- customer_state: UT
- customer_city: Provo
- primary_market: Pacific Asia
- primary_region: Southern Europe
- total_orders: 7
- total_sales: 4449.67
- total_profit: 617.79
- late_delivery_count: 10
- late_delivery_rate: 0.4762
- support_ticket_count: 1
- open_support_ticket_count: 1
- last_meaningful_touch_date: 2016-12-15

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O048973 | 2025-06-22 | 2025-06-26 | PENDING | Shipping on time | 0 | Standard Class | 309.96 | 118.02 | 308.16 | 4 | 4 |  |
| O047330 | 2025-05-29 | 2025-06-04 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 110.0 | 44.98 | 95.7 | 4 | 6 | Late |
| O034291 | 2024-11-20 | 2024-11-22 | PENDING_PAYMENT | Advance shipping | 0 | Standard Class | 1239.92 | 231.9 | 1145.72 | 4 | 2 |  |
| O024040 | 2024-06-23 | 2024-06-29 | CLOSED | Late delivery | 1 | Standard Class | 629.9 | 119.24 | 573.8 | 4 | 6 | Late |
| O012579 | 2024-01-08 | 2024-01-13 | COMPLETE | Late delivery | 1 | Standard Class | 1279.93 | 265.05 | 1139.44 | 4 | 5 | Late |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N15325 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.4762 with category concentration in Cleats. |
| N15324 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band Medium and support history. |
| N15326 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E22160 | TH-C001631-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E22159 | TH-C001631-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E22158 | TH-C001631-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E22156 | TH-C001631-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E22155 | TH-C001631-[redacted] | 3 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL005529 | O047330 | 2025-05-29 | carrier_delay | High | Carrier route delay | Open |
| FUL002137 | O024040 | 2024-06-23 | carrier_delay | High | Carrier route delay | Open |
| FUL000412 | O012579 | 2024-01-08 | carrier_delay | High | Carrier route delay | Open |
| FUL004840 | O004255 | 2023-09-09 | cancellation_review | Medium | Customer or fulfillment cancellation | Closed |

## H056 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: EE. UU.
- customer_state: MI
- customer_city: Detroit
- primary_market: LATAM
- primary_region: Caribbean
- total_orders: 7
- total_sales: 4669.53
- total_profit: 306.89
- late_delivery_count: 15
- late_delivery_rate: 0.7143
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-09-24
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O068350 | 2026-04-01 | 2026-04-07 | PENDING_PAYMENT | Late delivery | 1 | Second Class | 369.97 | 85.55 | 318.77 | 2 | 6 | Late |
| O063977 | 2026-01-27 | 2026-01-28 | CLOSED | Late delivery | 1 | Same Day | 329.91 | 57.32 | 302.51 | 0 | 1 | Late |
| O058300 | 2025-11-06 | 2025-11-12 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 1099.94 | 165.45 | 991.94 | 4 | 6 | Late |
| O056766 | 2025-10-14 | 2025-10-16 | PENDING_PAYMENT | Advance shipping | 0 | Standard Class | 779.96 | 192.23 | 711.06 | 4 | 2 |  |
| O023895 | 2024-06-21 | 2024-06-27 | COMPLETE | Late delivery | 1 | Second Class | 399.98 | 3.94 | 327.98 | 2 | 6 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T6514 | 2025-11-02 | Cancellation request | Battery life | My {product_purchased} is making strange noises and not functioning properly. I suspect there might be a hardware issue. Can you please help me with this?  I… | Closed | Low | Email | Third she anyone low. | 0.0 | 3.0 | Neutral |
| T6513 | 2024-10-10 | Cancellation request | Product recommendation | My {product_purchased} crashed, and I lost all the data stored on it. Is there any way to recover the lost data?  Why should the original user lose the lost … | Pending | Low | Phone |  |  |  | Neutral |
| T6515 | 2024-08-17 | Refund request | Installation support | I'm having an issue with the {product_purchased}. Please assist. [23:20:06} [Client thread/INFO] [RecipeLoader/Forge]: Loading [recipe-loader] name from recipe… | Open | Low | Email |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N13752 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Men's Footwear. |
| N13753 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N13754 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band High and support history. |
| N13755 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.7143 with category concentration in Men's Footwear. |
| N13756 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E19496 | TH-C001329-[redacted] | 14 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E19495 | TH-C001329-[redacted] | 13 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E19494 | TH-C001329-[redacted] | 12 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E19493 | TH-C001329-[redacted] | 11 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E19492 | TH-C001329-[redacted] | 10 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL008551 | O068350 | 2026-04-01 | carrier_delay | High | Carrier route delay | Open |
| FUL007909 | O063977 | 2026-01-27 | carrier_delay | High | Carrier route delay | Open |
| FUL007121 | O058300 | 2025-11-06 | carrier_delay | High | Carrier route delay | Open |
| FUL002120 | O023895 | 2024-06-21 | carrier_delay | High | Carrier route delay | Open |
| FUL002058 | O002350 | 2023-08-12 | carrier_delay | High | Carrier route delay | Open |

## H057 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Home Office
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: Pacific Asia
- primary_region: South America
- total_orders: 8
- total_sales: 4664.44
- total_profit: 646.41
- late_delivery_count: 14
- late_delivery_rate: 0.5185
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-06-18
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O061630 | 2025-12-24 | 2025-12-30 | CLOSED | Late delivery | 1 | Standard Class | 989.87 | 260.6 | 913.47 | 4 | 6 | Late |
| O061317 | 2025-12-20 | 2025-12-23 | PROCESSING | Advance shipping | 0 | Standard Class | 350.0 | 151.16 | 310.5 | 4 | 3 |  |
| O055980 | 2025-10-03 | 2025-10-09 | COMPLETE | Late delivery | 1 | Standard Class | 1243.83 | 41.67 | 1077.43 | 4 | 6 | Late |
| O049486 | 2025-06-30 | 2025-07-02 | COMPLETE | Advance shipping | 0 | Standard Class | 149.98 | 54.38 | 146.98 | 4 | 2 |  |
| O048453 | 2025-06-15 | 2025-06-19 | PENDING_PAYMENT | Shipping on time | 0 | Standard Class | 595.9 | 18.53 | 526.84 | 4 | 4 |  |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N13840 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Monitor whether the next interaction with the customer resolves the current [redacted] thread. |
| N13837 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.5185 with category concentration in Women's Apparel. |
| N13839 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer-success owner should align response tone with [redacted] scenario. |
| N13834 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Women's Apparel. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E19634 | TH-C001343-[redacted] | 10 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E19625 | TH-C001343-[redacted] | 1 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL007580 | O061630 | 2025-12-24 | carrier_delay | High | Carrier route delay | Open |
| FUL006783 | O055980 | 2025-10-03 | carrier_delay | High | Carrier route delay | Open |
| FUL001295 | O018490 | 2024-04-03 | carrier_delay | High | Carrier route delay | Open |

## H058 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: EE. UU.
- customer_state: FL
- customer_city: Fort Lauderdale
- primary_market: LATAM
- primary_region: Central America
- total_orders: 8
- total_sales: 6134.27
- total_profit: 654.42
- late_delivery_count: 17
- late_delivery_rate: 0.68
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-06-18
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O061613 | 2025-12-24 | 2025-12-28 | CLOSED | Shipping on time | 0 | Standard Class | 599.93 | 81.73 | 537.94 | 4 | 4 |  |
| O050015 | 2025-07-08 | 2025-07-14 | COMPLETE | Late delivery | 1 | Standard Class | 679.93 | -28.43 | 571.94 | 4 | 6 | Late |
| O048841 | 2025-06-20 | 2025-06-22 | PENDING | Advance shipping | 0 | Standard Class | 149.94 | -99.56 | 124.45 | 4 | 2 |  |
| O033579 | 2024-11-10 | 2024-11-15 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 319.97 | 101.09 | 289.97 | 4 | 5 | Late |
| O032729 | 2024-10-28 | 2024-11-02 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 499.97 | 151.54 | 421.97 | 4 | 5 | Late |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N8535 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.6800 with category concentration in Cardio Equipment. |
| N8536 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |
| N8539 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Escalation summary for the customer: protect revenue, close open issues, and document human review. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E10606 | TH-C000294-[redacted] | 12 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E10599 | TH-C000294-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL005926 | O050015 | 2025-07-08 | carrier_delay | High | Carrier route delay | Open |
| FUL003555 | O033579 | 2024-11-10 | carrier_delay | High | Carrier route delay | Open |
| FUL003437 | O032729 | 2024-10-28 | carrier_delay | High | Carrier route delay | Open |
| FUL001824 | O022030 | 2024-05-25 | carrier_delay | High | Carrier route delay | Open |
| FUL009039 | O009631 | 2023-11-26 | carrier_delay | High | Carrier route delay | Open |

## H059 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: EE. UU.
- customer_state: NY
- customer_city: Buffalo
- primary_market: USCA
- primary_region: West of USA
- total_orders: 9
- total_sales: 4299.45
- total_profit: 753.85
- late_delivery_count: 19
- late_delivery_rate: 0.76
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-03-26

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O055898 | 2025-10-01 | 2025-10-05 | COMPLETE | Shipping on time | 0 | Standard Class | 679.98 | -102.58 | 610.48 | 4 | 4 |  |
| O045040 | 2025-04-26 | 2025-05-02 | PENDING | Late delivery | 1 | Standard Class | 729.96 | 176.01 | 689.86 | 4 | 6 | Late |
| O041794 | 2025-03-10 | 2025-03-15 | COMPLETE | Late delivery | 1 | Standard Class | 129.99 | 11.02 | 97.49 | 4 | 5 | Late |
| O036971 | 2024-12-29 | 2024-12-31 | PENDING_PAYMENT | Late delivery | 1 | First Class | 689.85 | 155.52 | 613.88 | 1 | 2 | Late |
| O036107 | 2024-12-17 | 2024-12-20 | COMPLETE | Late delivery | 1 | Second Class | 529.97 | 146.5 | 475.47 | 2 | 3 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T6166 | 2025-01-23 | Technical issue | Display issue | I'm having an issue with the {product_purchased}. Please assist. - "products":[17,18,20,19,23,24,25,26,27,28,29,30,31],"manufacturer_ I'm using the original ch… | Closed | Medium | Chat | Thousand policy door husband black. | 9.1 | 5.0 | Positive |
| T6161 | 2024-10-06 | Cancellation request | Software bug | The {product_purchased} is unable to establish a stable internet connection. It keeps disconnecting intermittently. How can I troubleshoot this network problem… | Pending | Medium | Chat |  |  |  | Neutral |
| T6156 | 2024-10-01 | Refund request | Payment issue | I'm having an issue with the {product_purchased}. Please assist.  The product is already in stock. Please try again later.  We take great pride in Electron… | Open | Medium | Email |  |  |  | Neutral |
| T6163 | 2024-06-17 | Product inquiry | Product recommendation | I'm having an issue with the {product_purchased}. Please assist. No sales will be made.  Please do not order this item unless it comes with a physical item t… | Pending | Medium | Chat |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N16490 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Men's Footwear. |
| N16491 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N16492 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band High and support history. |
| N16493 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.7600 with category concentration in Men's Footwear. |
| N16494 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E24148 | TH-C001867-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E24147 | TH-C001867-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E24146 | TH-C001867-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E24145 | TH-C001867-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E24144 | TH-C001867-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL005182 | O045040 | 2025-04-26 | carrier_delay | High | Carrier route delay | Open |
| FUL004723 | O041794 | 2025-03-10 | carrier_delay | High | Carrier route delay | Open |
| FUL004042 | O036971 | 2024-12-29 | carrier_delay | High | Carrier route delay | Open |
| FUL003912 | O036107 | 2024-12-17 | carrier_delay | High | Carrier route delay | Open |
| FUL003831 | O035574 | 2024-12-09 | carrier_delay | High | Carrier route delay | Open |

## H060 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Home Office
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: LATAM
- primary_region: Central America
- total_orders: 8
- total_sales: 5946.25
- total_profit: 538.08
- late_delivery_count: 23
- late_delivery_rate: 0.7667
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-04-15

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O057240 | 2025-10-21 | 2025-10-27 | COMPLETE | Late delivery | 1 | Standard Class | 529.93 | -220.31 | 467.93 | 4 | 6 | Late |
| O052636 | 2025-08-15 | 2025-08-17 | COMPLETE | Late delivery | 1 | First Class | 619.94 | 106.72 | 570.95 | 1 | 2 | Late |
| O052571 | 2025-08-14 | 2025-08-16 | CLOSED | Advance shipping | 0 | Standard Class | 1059.85 | -4.6 | 923.26 | 4 | 2 |  |
| O048869 | 2025-06-21 | 2025-06-26 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 1204.84 | 243.26 | 1082.65 | 4 | 5 | Late |
| O038472 | 2025-01-20 | 2025-01-23 | PROCESSING | Advance shipping | 0 | Standard Class | 699.93 | 171.8 | 524.95 | 4 | 3 |  |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T5607 | 2026-01-01 | Cancellation request | Product compatibility | The {product_purchased} is unable to establish a stable internet connection. It keeps disconnecting intermittently. How can I troubleshoot this network problem… | Open | Low | Phone |  |  |  | Neutral |
| T5397 | 2025-06-26 | Refund request | Refund request | I'm having an issue with the {product_purchased}. Please assist. I have no idea what's going on with the product.   I purchased this in February, 2014 and t… | Pending | Low | Chat |  |  |  | Neutral |
| T6601 | 2025-01-13 | Refund request | Battery life | I'm having an issue with the {product_purchased}. Please assist.  Thanks a lot!  If you want to help with this issue, please contact the support team on Di… | Pending | Low | Social media |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N8897 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Cleats. |
| N8898 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N8899 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band High and support history. |
| N8900 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.7667 with category concentration in Cleats. |
| N8901 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E11220 | TH-C000364-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E11219 | TH-C000364-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E11218 | TH-C000364-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E11217 | TH-C000364-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E11216 | TH-C000364-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL006965 | O057240 | 2025-10-21 | carrier_delay | High | Carrier route delay | Open |
| FUL006312 | O052636 | 2025-08-15 | carrier_delay | High | Carrier route delay | Open |
| FUL005757 | O048869 | 2025-06-21 | carrier_delay | High | Carrier route delay | Open |
| FUL004073 | O037179 | 2025-01-01 | carrier_delay | High | Carrier route delay | Open |
| FUL001910 | O022539 | 2024-06-02 | carrier_delay | High | Carrier route delay | Open |

## H061 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: EE. UU.
- customer_state: CA
- customer_city: Fullerton
- primary_market: USCA
- primary_region: US Center
- total_orders: 9
- total_sales: 4464.39
- total_profit: 1224.63
- late_delivery_count: 13
- late_delivery_rate: 0.5417
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-05-09
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O058911 | 2025-11-14 | 2025-11-16 | SUSPECTED_FRAUD | Shipping canceled | 0 | First Class | 329.99 | 17.69 | 314.99 | 1 | 2 | Canceled |
| O048595 | 2025-06-17 | 2025-06-23 | PROCESSING | Late delivery | 1 | Standard Class | 519.96 | 217.93 | 481.56 | 4 | 6 | Late |
| O041390 | 2025-03-04 | 2025-03-10 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 49.98 | 4.4 | 49.98 | 4 | 6 | Late |
| O036358 | 2024-12-20 | 2024-12-24 | PROCESSING | Shipping on time | 0 | Standard Class | 1369.81 | 280.26 | 1183.53 | 4 | 4 |  |
| O031297 | 2024-10-07 | 2024-10-10 | PENDING | Advance shipping | 0 | Standard Class | 619.91 | 159.68 | 525.71 | 4 | 3 |  |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N15218 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N15221 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |
| N15224 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Escalation summary for the customer: protect revenue, close open issues, and document human review. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E21985 | TH-C001613-[redacted] | 13 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E21982 | TH-C001613-[redacted] | 10 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E21980 | TH-C001613-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E21979 | TH-C001613-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E21978 | TH-C001613-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL007195 | O058911 | 2025-11-14 | cancellation_review | Medium | Customer or fulfillment cancellation | Closed |
| FUL005718 | O048595 | 2025-06-17 | carrier_delay | High | Carrier route delay | Open |
| FUL004655 | O041390 | 2025-03-04 | carrier_delay | High | Carrier route delay | Open |
| FUL003056 | O030003 | 2024-09-18 | carrier_delay | High | Carrier route delay | Open |
| FUL002406 | O025677 | 2024-07-17 | carrier_delay | High | Carrier route delay | Open |

## H062 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: Europe
- primary_region: Western Europe
- total_orders: 7
- total_sales: 4609.57
- total_profit: 995.54
- late_delivery_count: 17
- late_delivery_rate: 0.85
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-09-11

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O067445 | 2026-03-19 | 2026-03-25 | PENDING_PAYMENT | Late delivery | 1 | Second Class | 1699.91 | 470.79 | 1585.91 | 2 | 6 | Late |
| O064282 | 2026-02-01 | 2026-02-03 | PENDING | Late delivery | 1 | First Class | 859.92 | 175.04 | 742.14 | 1 | 2 | Late |
| O048483 | 2025-06-15 | 2025-06-19 | COMPLETE | Late delivery | 1 | Second Class | 499.94 | 191.51 | 489.54 | 2 | 4 | Late |
| O042775 | 2025-03-24 | 2025-03-30 | PROCESSING | Late delivery | 1 | Second Class | 579.95 | 153.02 | 550.75 | 2 | 6 | Late |
| O032751 | 2024-10-29 | 2024-10-31 | PROCESSING | Shipping on time | 0 | Second Class | 299.96 | -137.69 | 246.97 | 2 | 2 |  |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T5478 | 2026-02-14 | Cancellation request | Installation support | I'm having an issue with the {product_purchased}. Please assist. Please support this resource by signing up to our newsletter. Thank you.  Product Purchase /… | Open | Critical | Email |  |  |  | Neutral |
| T5458 | 2025-05-05 | Refund request | Software bug | I'm having an issue with the {product_purchased}. Please assist. <iid=2B6A7C1a9-A2CC-4F39-9FB7-D4B49D7DA I've noticed that the issue occurs consistently when I… | Pending | Critical | Chat |  |  |  | Neutral |
| T6423 | 2024-07-19 | Product inquiry | Product compatibility | My {product_purchased} crashed, and I lost all the data stored on it. Is there any way to recover the lost data?  Solution: To create a REST API, use the 'gr… | Pending | Critical | Social media |  |  |  | Neutral |
| T5480 | 2024-05-09 | Refund request | Product setup | I'm having an issue with the {product_purchased}. Please assist. (This means I'm in no way responsible as to which products you buy or what brand of product it… | Open | Critical | Phone |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N14229 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Cleats. |
| N14230 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N14231 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band High and support history. |
| N14232 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.8500 with category concentration in Cleats. |
| N14233 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E20300 | TH-C001413-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E20299 | TH-C001413-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E20298 | TH-C001413-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E20297 | TH-C001413-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E20296 | TH-C001413-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL008411 | O067445 | 2026-03-19 | carrier_delay | High | Carrier route delay | Open |
| FUL007951 | O064282 | 2026-02-01 | carrier_delay | High | Carrier route delay | Open |
| FUL005701 | O048483 | 2025-06-15 | carrier_delay | High | Carrier route delay | Open |
| FUL004867 | O042775 | 2025-03-24 | carrier_delay | High | Carrier route delay | Open |
| FUL009046 | O009714 | 2023-11-27 | carrier_delay | High | Carrier route delay | Open |

## H063 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Home Office
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: Pacific Asia
- primary_region: Southeast Asia
- total_orders: 8
- total_sales: 4979.46
- total_profit: 464.45
- late_delivery_count: 20
- late_delivery_rate: 0.8696
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-02-07
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O052633 | 2025-08-15 | 2025-08-19 | CLOSED | Late delivery | 1 | Second Class | 729.94 | 102.65 | 642.45 | 2 | 4 | Late |
| O032936 | 2024-10-31 | 2024-11-02 | COMPLETE | Late delivery | 1 | First Class | 1089.88 | 114.95 | 931.19 | 1 | 2 | Late |
| O029839 | 2024-09-16 | 2024-09-21 | PENDING | Late delivery | 1 | Standard Class | 489.93 | 10.97 | 402.74 | 4 | 5 | Late |
| O026452 | 2024-07-29 | 2024-08-01 | PENDING_PAYMENT | Advance shipping | 0 | Standard Class | 350.0 | 47.98 | 348.0 | 4 | 3 |  |
| O023890 | 2024-06-21 | 2024-06-27 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 1479.79 | 45.46 | 1291.91 | 4 | 6 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T6002 | 2025-06-23 | Billing inquiry | Product compatibility | I'm having an issue with the {product_purchased}. Please assist.  "If I click on [that product's] [Product]" button I have to pick up the latest version, tha… | Open | Critical | Social media |  |  |  | Neutral |
| T6001 | 2025-06-14 | Cancellation request | Installation support | I've forgotten my password for my {product_purchased} account, and the password reset option is not working. How can I recover my account?  You can recover y… | Open | Critical | Phone |  |  |  | Neutral |
| T5996 | 2025-03-10 | Cancellation request | Product compatibility | The {product_purchased} is unable to establish a stable internet connection. It keeps disconnecting intermittently. How can I troubleshoot this network problem… | Open | Critical | Chat |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N12098 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Men's Footwear. |
| N12099 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N12100 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band High and support history. |
| N12101 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.8696 with category concentration in Men's Footwear. |
| N12102 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E16678 | TH-C001000-[redacted] | 14 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E16677 | TH-C001000-[redacted] | 13 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E16676 | TH-C001000-[redacted] | 12 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E16675 | TH-C001000-[redacted] | 11 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E16674 | TH-C001000-[redacted] | 10 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL006311 | O052633 | 2025-08-15 | carrier_delay | High | Carrier route delay | Open |
| FUL003466 | O032936 | 2024-10-31 | carrier_delay | High | Carrier route delay | Open |
| FUL003029 | O029839 | 2024-09-16 | carrier_delay | High | Carrier route delay | Open |
| FUL002118 | O023890 | 2024-06-21 | carrier_delay | High | Carrier route delay | Open |
| FUL000232 | O011479 | 2023-12-23 | carrier_delay | High | Carrier route delay | Open |

## H064 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Corporate
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: Europe
- primary_region: Western Europe
- total_orders: 7
- total_sales: 4729.63
- total_profit: 83.53
- late_delivery_count: 9
- late_delivery_rate: 0.5294
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-09-29

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O068704 | 2026-04-06 | 2026-04-11 | PROCESSING | Late delivery | 1 | Standard Class | 529.97 | 171.47 | 485.82 | 4 | 5 | Late |
| O067992 | 2026-03-27 | 2026-03-30 | COMPLETE | Advance shipping | 0 | Standard Class | 649.95 | 137.67 | 565.96 | 4 | 3 |  |
| O063183 | 2026-01-16 | 2026-01-20 | COMPLETE | Shipping on time | 0 | Standard Class | 609.91 | -280.74 | 513.52 | 4 | 4 |  |
| O051704 | 2025-08-01 | 2025-08-06 | COMPLETE | Late delivery | 1 | Standard Class | 639.94 | 7.37 | 546.74 | 4 | 5 | Late |
| O043051 | 2025-03-28 | 2025-03-30 | PROCESSING | Advance shipping | 0 | Standard Class | 399.98 | 97.2 | 359.98 | 4 | 2 |  |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N13393 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Fishing. |
| N13395 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band Medium and support history. |
| N13397 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |
| N13394 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E18878 | TH-C001262-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E18877 | TH-C001262-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E18875 | TH-C001262-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E18874 | TH-C001262-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E18873 | TH-C001262-[redacted] | 3 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL008611 | O068704 | 2026-04-06 | carrier_delay | High | Carrier route delay | Open |
| FUL006168 | O051704 | 2025-08-01 | carrier_delay | High | Carrier route delay | Open |
| FUL003381 | O032370 | 2024-10-23 | cancellation_review | Medium | Customer or fulfillment cancellation | Closed |
| FUL002980 | O029592 | 2024-09-12 | carrier_delay | High | Carrier route delay | Open |

## H065 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: EE. UU.
- customer_state: TX
- customer_city: Richardson
- primary_market: Pacific Asia
- primary_region: South Asia
- total_orders: 7
- total_sales: 4504.55
- total_profit: -112.55
- late_delivery_count: 15
- late_delivery_rate: 0.75
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-01-19
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O051357 | 2025-07-27 | 2025-07-30 | PENDING_PAYMENT | Advance shipping | 0 | Standard Class | 299.95 | 133.75 | 272.95 | 4 | 3 |  |
| O044030 | 2025-04-11 | 2025-04-17 | COMPLETE | Late delivery | 1 | Standard Class | 759.96 | 167.14 | 651.46 | 4 | 6 | Late |
| O041927 | 2025-03-12 | 2025-03-15 | PENDING_PAYMENT | Late delivery | 1 | Second Class | 644.95 | 159.8 | 603.75 | 2 | 3 | Late |
| O041315 | 2025-03-03 | 2025-03-09 | PENDING | Late delivery | 1 | Standard Class | 119.98 | 26.19 | 99.58 | 4 | 6 | Late |
| O023838 | 2024-06-20 | 2024-06-24 | PENDING_PAYMENT | Late delivery | 1 | Second Class | 549.92 | -777.18 | 473.93 | 2 | 4 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T6735 | 2025-08-20 | Technical issue | Battery life | I'm having an issue with the {product_purchased}. Please assist.  Thank You  Your Service has been completely exceptional and will never be duplicated.  … | Closed | Medium | Chat | Establish establish song paper great sister rock. | 1.3 | 3.0 | Neutral |
| T6733 | 2025-06-05 | Technical issue | Installation support | I'm having an issue with the {product_purchased}. Please assist.  The problem is, we are now back to the old script, and have a script download. That script … | Closed | Medium | Social media | Head growth impact. | 0.0 | 2.0 | Negative |
| T6736 | 2024-11-07 | Technical issue | Battery life | I'm having an issue with the {product_purchased}. Please assist. The issue I'm facing is intermittent. Sometimes it works fine, but other times it acts up unex… | Pending | Medium | Social media |  |  |  | Neutral |
| T6734 | 2024-06-02 | Billing inquiry | Product setup | I'm having an issue with the {product_purchased}. Please assist. In the future, I will try and provide this error message. If I receive this error and I receiv… | Pending | Medium | Social media |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N14890 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Cardio Equipment. |
| N14891 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N14892 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band High and support history. |
| N14893 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.7500 with category concentration in Cardio Equipment. |
| N14894 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E21430 | TH-C001547-[redacted] | 14 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E21429 | TH-C001547-[redacted] | 13 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E21428 | TH-C001547-[redacted] | 12 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E21427 | TH-C001547-[redacted] | 11 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E21426 | TH-C001547-[redacted] | 10 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL005046 | O044030 | 2025-04-11 | carrier_delay | High | Carrier route delay | Open |
| FUL004748 | O041927 | 2025-03-12 | carrier_delay | High | Carrier route delay | Open |
| FUL004646 | O041315 | 2025-03-03 | carrier_delay | High | Carrier route delay | Open |
| FUL002107 | O023838 | 2024-06-20 | carrier_delay | High | Carrier route delay | Open |
| FUL001643 | O020802 | 2024-05-07 | carrier_delay | High | Carrier route delay | Open |

## H066 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Corporate
- customer_country: EE. UU.
- customer_state: TX
- customer_city: College Station
- primary_market: LATAM
- primary_region: Southeast Asia
- total_orders: 6
- total_sales: 4979.51
- total_profit: 376.07
- late_delivery_count: 18
- late_delivery_rate: 0.8571
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-05-26
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O060077 | 2025-12-01 | 2025-12-04 | PENDING_PAYMENT | Advance shipping | 0 | Standard Class | 849.9 | -575.67 | 723.92 | 4 | 3 |  |
| O057784 | 2025-10-29 | 2025-11-03 | COMPLETE | Late delivery | 1 | Second Class | 399.98 | 102.07 | 351.98 | 2 | 5 | Late |
| O023038 | 2024-06-09 | 2024-06-11 | PROCESSING | Late delivery | 1 | First Class | 949.9 | -136.91 | 877.0 | 1 | 2 | Late |
| O022915 | 2024-06-07 | 2024-06-09 | COMPLETE | Late delivery | 1 | First Class | 1369.82 | 517.07 | 1271.83 | 1 | 2 | Late |
| O009584 | 2023-11-25 | 2023-11-26 | PENDING_PAYMENT | Late delivery | 1 | Same Day | 449.96 | 177.47 | 372.96 | 0 | 1 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T5394 | 2025-12-28 | Billing inquiry | Delivery problem | I'm having an issue with the {product_purchased}. Please assist. I try to do my best to answer every question within my allotted time. In the meantime, you can… | Pending | High | Chat |  |  |  | Neutral |
| T5391 | 2025-11-09 | Technical issue | Display issue | I'm having an issue with the {product_purchased}. Please assist.  3. This product is not suitable for use by an adult.  4. You must be at least 18 years of… | Closed | High | Phone | Direction white dark computer cut product there. | 12.4 | 4.0 | Positive |
| T5392 | 2024-09-29 | Refund request | Display issue | I'm having an issue with the {product_purchased}. Please assist.  When you receive this notice, you will have one last chance to purchase both the product an… | Pending | High | Phone |  |  |  | Neutral |
| T5400 | 2024-08-19 | Product inquiry | Account access | I've accidentally deleted important data from my {product_purchased}. Is there any way to recover the deleted files? I need them urgently.  This problem aris… | Pending | High | Chat |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N12080 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Fishing. |
| N12081 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N12082 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band High and support history. |
| N12083 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.8571 with category concentration in Fishing. |
| N12084 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E16648 | TH-C000997-[redacted] | 14 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E16647 | TH-C000997-[redacted] | 13 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E16646 | TH-C000997-[redacted] | 12 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E16645 | TH-C000997-[redacted] | 11 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E16644 | TH-C000997-[redacted] | 10 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL007041 | O057784 | 2025-10-29 | carrier_delay | High | Carrier route delay | Open |
| FUL001984 | O023038 | 2024-06-09 | carrier_delay | High | Carrier route delay | Open |
| FUL001965 | O022915 | 2024-06-07 | carrier_delay | High | Carrier route delay | Open |
| FUL009026 | O009584 | 2023-11-25 | carrier_delay | High | Carrier route delay | Open |
| FUL007662 | O006220 | 2023-10-07 | carrier_delay | High | Carrier route delay | Open |

## H067 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: EE. UU.
- customer_state: NJ
- customer_city: Toms River
- primary_market: Pacific Asia
- primary_region: Oceania
- total_orders: 7
- total_sales: 4979.51
- total_profit: -572.86
- late_delivery_count: 17
- late_delivery_rate: 0.7391
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-02-19

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O053435 | 2025-08-27 | 2025-09-02 | CLOSED | Late delivery | 1 | Standard Class | 549.98 | -75.4 | 477.98 | 4 | 6 | Late |
| O050124 | 2025-07-09 | 2025-07-14 | COMPLETE | Late delivery | 1 | Second Class | 799.93 | -78.71 | 757.93 | 2 | 5 | Late |
| O049866 | 2025-07-05 | 2025-07-07 | COMPLETE | Advance shipping | 0 | Standard Class | 119.98 | 13.56 | 119.98 | 4 | 2 |  |
| O035944 | 2024-12-14 | 2024-12-15 | PENDING_PAYMENT | Late delivery | 1 | Same Day | 799.88 | 59.36 | 717.69 | 0 | 1 | Late |
| O030871 | 2024-10-01 | 2024-10-03 | COMPLETE | Advance shipping | 0 | Standard Class | 1329.88 | -216.93 | 1190.49 | 4 | 2 |  |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T5774 | 2025-02-03 | Technical issue | Product recommendation | I'm facing issues logging into my {product_purchased} account. It says my account is locked. What should I do to unlock it? (Yes, log in. No problem.) But if m… | Open | Low | Email |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N12092 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |
| N12088 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Cardio Equipment. |
| N12090 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band Medium and support history. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E16655 | TH-C000998-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E16654 | TH-C000998-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E16653 | TH-C000998-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E16652 | TH-C000998-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E16651 | TH-C000998-[redacted] | 3 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL006414 | O053435 | 2025-08-27 | carrier_delay | High | Carrier route delay | Open |
| FUL005942 | O050124 | 2025-07-09 | carrier_delay | High | Carrier route delay | Open |
| FUL003892 | O035944 | 2024-12-14 | carrier_delay | High | Carrier route delay | Open |
| FUL002947 | O029369 | 2024-09-09 | carrier_delay | High | Carrier route delay | Open |
| FUL001273 | O018347 | 2024-04-01 | carrier_delay | High | Carrier route delay | Open |

## H068 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: EE. UU.
- customer_state: NY
- customer_city: Brooklyn
- primary_market: LATAM
- primary_region: Central America
- total_orders: 7
- total_sales: 4629.62
- total_profit: 291.65
- late_delivery_count: 9
- late_delivery_rate: 0.45
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-09-27

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O068511 | 2026-04-04 | 2026-04-06 | PENDING_PAYMENT | Shipping on time | 0 | Second Class | 369.98 | -194.52 | 335.88 | 2 | 2 |  |
| O061262 | 2025-12-19 | 2025-12-19 | PROCESSING | Shipping on time | 0 | Same Day | 329.99 | 103.96 | 272.84 | 0 | 0 |  |
| O056929 | 2025-10-17 | 2025-10-22 | PENDING_PAYMENT | Late delivery | 1 | Second Class | 199.99 | 3.52 | 175.99 | 2 | 5 | Late |
| O050104 | 2025-07-09 | 2025-07-14 | CLOSED | Late delivery | 1 | Standard Class | 569.94 | 217.14 | 503.14 | 4 | 5 | Late |
| O018021 | 2024-03-28 | 2024-03-30 | PENDING_PAYMENT | Advance shipping | 0 | Standard Class | 859.95 | 261.09 | 792.95 | 4 | 2 |  |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N14089 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Cleats. |
| N14090 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E20064 | TH-C001388-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E20062 | TH-C001388-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E20061 | TH-C001388-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E20060 | TH-C001388-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL006912 | O056929 | 2025-10-17 | carrier_delay | High | Carrier route delay | Open |
| FUL005939 | O050104 | 2025-07-09 | carrier_delay | High | Carrier route delay | Open |
| FUL003605 | O003390 | 2023-08-27 | carrier_delay | High | Carrier route delay | Open |

## H069 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: EE. UU.
- customer_state: OK
- customer_city: Lawton
- primary_market: LATAM
- primary_region: Central America
- total_orders: 6
- total_sales: 4559.59
- total_profit: 477.95
- late_delivery_count: 20
- late_delivery_rate: 1.0
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-05-03
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O058455 | 2025-11-08 | 2025-11-14 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 50.0 | 13.64 | 44.0 | 4 | 6 | Late |
| O053655 | 2025-08-30 | 2025-09-05 | COMPLETE | Late delivery | 1 | Standard Class | 999.87 | 286.48 | 910.38 | 4 | 6 | Late |
| O044952 | 2025-04-25 | 2025-04-27 | PROCESSING | Late delivery | 1 | First Class | 899.84 | 250.27 | 801.26 | 1 | 2 | Late |
| O024976 | 2024-07-07 | 2024-07-09 | COMPLETE | Late delivery | 1 | First Class | 1599.93 | -171.35 | 1394.93 | 1 | 2 | Late |
| O019612 | 2024-04-20 | 2024-04-22 | PROCESSING | Late delivery | 1 | First Class | 459.97 | 11.42 | 410.32 | 1 | 2 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T5790 | 2026-01-07 | Billing inquiry | Payment issue | I'm encountering a software bug in the {product_purchased}. Whenever I try to perform a specific action, the application crashes. Are there any updates or fixe… | Open | Critical | Email |  |  |  | Neutral |
| T5796 | 2026-01-05 | Refund request | Product recommendation | I'm unable to access my {product_purchased} account. It keeps displaying an 'Invalid Credentials' error, even though I'm using the correct login information. H… | Closed | Critical | Chat | Heart across cold material feeling subject fact. | 0.8 | 1.0 | Negative |
| T5794 | 2025-10-11 | Product inquiry | Peripheral compatibility | I'm having an issue with the {product_purchased}. Please assist.  • Please ensure that the account is updated and the account is valid for a time.  • Pleas… | Pending | Critical | Social media |  |  |  | Neutral |
| T5793 | 2024-12-31 | Technical issue | Product compatibility | I'm having an issue with the {product_purchased}. Please assist.  This product has been purchased and used as a part of a project that includes building a ne… | Pending | Critical | Email |  |  |  | Neutral |
| T5792 | 2024-08-10 | Cancellation request | Software bug | I'm having an issue with the {product_purchased}. Please assist.  It's really important to me, as you've done a lot, for my family, as well as for my busines… | Closed | Critical | Email | Hotel take both wide. | 13.2 | 3.0 | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N14498 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Women's Apparel. |
| N14499 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N14500 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band Critical and support history. |
| N14501 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 1.0000 with category concentration in Women's Apparel. |
| N14502 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E20766 | TH-C001468-[redacted] | 14 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E20765 | TH-C001468-[redacted] | 13 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E20764 | TH-C001468-[redacted] | 12 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E20763 | TH-C001468-[redacted] | 11 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E20762 | TH-C001468-[redacted] | 10 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL007141 | O058455 | 2025-11-08 | carrier_delay | High | Carrier route delay | Open |
| FUL006450 | O053655 | 2025-08-30 | carrier_delay | High | Carrier route delay | Open |
| FUL005170 | O044952 | 2025-04-25 | carrier_delay | High | Carrier route delay | Open |
| FUL002291 | O024976 | 2024-07-07 | carrier_delay | High | Carrier route delay | Open |
| FUL001453 | O019612 | 2024-04-20 | carrier_delay | High | Carrier route delay | Open |

## H070 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Corporate
- customer_country: EE. UU.
- customer_state: CA
- customer_city: Tustin
- primary_market: Europe
- primary_region: Northern Europe
- total_orders: 9
- total_sales: 4874.44
- total_profit: 1075.41
- late_delivery_count: 16
- late_delivery_rate: 0.7273
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-03-14
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O055012 | 2025-09-19 | 2025-09-22 | CANCELED | Shipping canceled | 0 | Second Class | 249.9 | 63.67 | 227.41 | 2 | 3 | Canceled |
| O027276 | 2024-08-10 | 2024-08-12 | COMPLETE | Advance shipping | 0 | Standard Class | 449.98 | 179.42 | 392.98 | 4 | 2 |  |
| O027245 | 2024-08-09 | 2024-08-15 | PENDING | Late delivery | 1 | Standard Class | 559.96 | 54.13 | 510.96 | 4 | 6 | Late |
| O020083 | 2024-04-27 | 2024-04-29 | PENDING | Late delivery | 1 | First Class | 899.93 | 200.74 | 753.94 | 1 | 2 | Late |
| O018700 | 2024-04-06 | 2024-04-12 | CLOSED | Late delivery | 1 | Second Class | 674.84 | 104.67 | 616.7 | 2 | 6 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T6550 | 2025-11-02 | Product inquiry | Peripheral compatibility | I'm having an issue with the {product_purchased}. Please assist. {product_purchased} will not be updated. This is a product-based order processing order. Pleas… | Pending | Medium | Social media |  |  |  | Neutral |
| T6551 | 2025-10-25 | Cancellation request | Display issue | There seems to be a glitch in the {product_purchased} software. It freezes frequently, making it difficult to use. Can you please provide a solution?  -We ar… | Pending | Medium | Email |  |  |  | Neutral |
| T5558 | 2025-09-27 | Cancellation request | Product compatibility | I'm having an issue with the {product_purchased}. Please assist.  In the spirit of your trust, I would like to express my thanks and pleasure to everyone who… | Open | Medium | Social media |  |  |  | Neutral |
| T6429 | 2025-01-28 | Technical issue | Product recommendation | I'm having an issue with the {product_purchased}. Please assist. [23:35:33] <RxKendrick> but we are a little short on what we can expect from the bot on strea… | Open | Medium | Chat |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N12621 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Women's Apparel. |
| N12622 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N12623 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band High and support history. |
| N12624 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.7273 with category concentration in Women's Apparel. |
| N12625 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E17566 | TH-C001101-[redacted] | 14 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E17565 | TH-C001101-[redacted] | 13 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E17564 | TH-C001101-[redacted] | 12 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E17563 | TH-C001101-[redacted] | 11 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E17562 | TH-C001101-[redacted] | 10 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL006635 | O055012 | 2025-09-19 | cancellation_review | Medium | Customer or fulfillment cancellation | Closed |
| FUL002639 | O027245 | 2024-08-09 | carrier_delay | High | Carrier route delay | Open |
| FUL001521 | O020083 | 2024-04-27 | carrier_delay | High | Carrier route delay | Open |
| FUL001323 | O018700 | 2024-04-06 | carrier_delay | High | Carrier route delay | Open |
| FUL001202 | O017954 | 2024-03-27 | carrier_delay | High | Carrier route delay | Open |

## H071 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: EE. UU.
- customer_state: CA
- customer_city: Ontario
- primary_market: Europe
- primary_region: Western Europe
- total_orders: 7
- total_sales: 5339.35
- total_profit: 1552.78
- late_delivery_count: 15
- late_delivery_rate: 0.6
- support_ticket_count: 1
- open_support_ticket_count: 1
- last_meaningful_touch_date: 2017-08-14
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O065507 | 2026-02-19 | 2026-02-22 | PENDING_PAYMENT | Late delivery | 1 | Second Class | 1159.93 | 276.56 | 1040.13 | 2 | 3 | Late |
| O044180 | 2025-04-13 | 2025-04-19 | CLOSED | Late delivery | 1 | Standard Class | 129.99 | 63.06 | 128.69 | 4 | 6 | Late |
| O041863 | 2025-03-11 | 2025-03-15 | PROCESSING | Shipping on time | 0 | Standard Class | 949.81 | 222.23 | 832.44 | 4 | 4 |  |
| O032072 | 2024-10-19 | 2024-10-22 | CLOSED | Advance shipping | 0 | Standard Class | 1309.81 | 547.82 | 1213.32 | 4 | 3 |  |
| O012242 | 2024-01-03 | 2024-01-05 | COMPLETE | Late delivery | 1 | First Class | 729.88 | 121.17 | 695.59 | 1 | 2 | Late |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N10629 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E14182 | TH-C000709-[redacted] | 14 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E14177 | TH-C000709-[redacted] | 9 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E14172 | TH-C000709-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL008127 | O065507 | 2026-02-19 | carrier_delay | High | Carrier route delay | Open |
| FUL005069 | O044180 | 2025-04-13 | carrier_delay | High | Carrier route delay | Open |
| FUL000358 | O012242 | 2024-01-03 | carrier_delay | High | Carrier route delay | Open |
| FUL008884 | O008542 | 2023-11-10 | carrier_delay | High | Carrier route delay | Open |
| FUL004396 | O003955 | 2023-09-04 | carrier_delay | High | Carrier route delay | Open |

## H072 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Home Office
- customer_country: EE. UU.
- customer_state: PA
- customer_city: Philadelphia
- primary_market: Europe
- primary_region: Western Europe
- total_orders: 6
- total_sales: 5084.59
- total_profit: -365.53
- late_delivery_count: 14
- late_delivery_rate: 0.5833
- support_ticket_count: 1
- open_support_ticket_count: 1
- last_meaningful_touch_date: 2017-08-16

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O065628 | 2026-02-21 | 2026-02-25 | COMPLETE | Shipping on time | 0 | Standard Class | 599.95 | 144.12 | 537.96 | 4 | 4 |  |
| O063890 | 2026-01-26 | 2026-01-28 | PROCESSING | Late delivery | 1 | First Class | 909.94 | -1164.7 | 855.34 | 1 | 2 | Late |
| O042395 | 2025-03-18 | 2025-03-24 | PENDING_PAYMENT | Late delivery | 1 | Second Class | 1279.84 | 344.78 | 1174.04 | 2 | 6 | Late |
| O041400 | 2025-03-04 | 2025-03-06 | SUSPECTED_FRAUD | Shipping canceled | 0 | First Class | 359.98 | 68.77 | 292.48 | 1 | 2 | Canceled |
| O025746 | 2024-07-18 | 2024-07-20 | CLOSED | Shipping on time | 0 | Second Class | 834.94 | 282.18 | 739.14 | 2 | 2 |  |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N11668 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E15934 | TH-C000915-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E15933 | TH-C000915-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E15932 | TH-C000915-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL007890 | O063890 | 2026-01-26 | carrier_delay | High | Carrier route delay | Open |
| FUL004820 | O042395 | 2025-03-18 | carrier_delay | High | Carrier route delay | Open |
| FUL004658 | O041400 | 2025-03-04 | cancellation_review | Medium | Customer or fulfillment cancellation | Closed |
| FUL000708 | O014624 | 2024-02-07 | carrier_delay | High | Carrier route delay | Open |

## H073 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: LATAM
- primary_region: West Africa
- total_orders: 11
- total_sales: 5523.53
- total_profit: 1269.91
- late_delivery_count: 20
- late_delivery_rate: 0.7407
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-08-09

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O065185 | 2026-02-14 | 2026-02-20 | CLOSED | Late delivery | 1 | Standard Class | 329.98 | 113.16 | 325.38 | 4 | 6 | Late |
| O058102 | 2025-11-03 | 2025-11-06 | PROCESSING | Advance shipping | 0 | Standard Class | 599.96 | 25.62 | 557.96 | 4 | 3 |  |
| O047576 | 2025-06-02 | 2025-06-04 | COMPLETE | Advance shipping | 0 | Standard Class | 269.96 | 98.28 | 245.86 | 4 | 2 |  |
| O043054 | 2025-03-28 | 2025-04-02 | CLOSED | Late delivery | 1 | Second Class | 539.94 | 106.18 | 485.15 | 2 | 5 | Late |
| O039638 | 2025-02-06 | 2025-02-08 | COMPLETE | Late delivery | 1 | First Class | 739.93 | 276.97 | 692.93 | 1 | 2 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T6783 | 2026-04-13 | Technical issue | Account access | I've accidentally deleted important data from my {product_purchased}. Is there any way to recover the deleted files? I need them urgently. Thank you very much … | Closed | Low | Phone | Deal thing along east. | 1.7 | 2.0 | Negative |
| T6786 | 2025-12-11 | Refund request | Hardware issue | I'm encountering a software bug in the {product_purchased}. Whenever I try to perform a specific action, the application crashes. Are there any updates or fixe… | Closed | Low | Email | Around effect share order then bring live. | 10.6 | 4.0 | Positive |
| T6792 | 2024-08-31 | Cancellation request | Peripheral compatibility | I've noticed a software bug in the {product_purchased} app. It's causing data loss and unexpected errors. How can I resolve this issue?  I've noticed a softw… | Open | Low | Phone |  |  |  | Neutral |
| T5210 | 2024-06-06 | Technical issue | Delivery problem | I'm unable to access my {product_purchased} account. It keeps displaying an 'Invalid Credentials' error, even though I'm using the correct login information. H… | Closed | Low | Chat | Yet deal something travel. | 0.0 | 1.0 | Negative |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N10025 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Water Sports. |
| N10026 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N10027 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band High and support history. |
| N10028 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.7407 with category concentration in Water Sports. |
| N10029 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E13152 | TH-C000589-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E13151 | TH-C000589-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E13150 | TH-C000589-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E13149 | TH-C000589-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E13148 | TH-C000589-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL008082 | O065185 | 2026-02-14 | carrier_delay | High | Carrier route delay | Open |
| FUL004917 | O043054 | 2025-03-28 | carrier_delay | High | Carrier route delay | Open |
| FUL004412 | O039638 | 2025-02-06 | carrier_delay | High | Carrier route delay | Open |
| FUL002946 | O029364 | 2024-09-09 | carrier_delay | High | Carrier route delay | Open |
| FUL001450 | O019597 | 2024-04-20 | carrier_delay | High | Carrier route delay | Open |

## H074 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: LATAM
- primary_region: Central America
- total_orders: 8
- total_sales: 5957.35
- total_profit: 846.65
- late_delivery_count: 28
- late_delivery_rate: 0.875
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-07-26

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O064203 | 2026-01-31 | 2026-02-04 | CLOSED | Shipping on time | 0 | Standard Class | 829.89 | 223.46 | 715.61 | 4 | 4 |  |
| O060594 | 2025-12-09 | 2025-12-11 | PENDING_PAYMENT | Late delivery | 1 | First Class | 959.87 | 174.72 | 907.23 | 1 | 2 | Late |
| O055795 | 2025-09-30 | 2025-10-06 | COMPLETE | Late delivery | 1 | Standard Class | 247.95 | 59.54 | 219.11 | 4 | 6 | Late |
| O053505 | 2025-08-28 | 2025-09-03 | PROCESSING | Late delivery | 1 | Standard Class | 969.93 | 136.43 | 785.64 | 4 | 6 | Late |
| O037485 | 2025-01-06 | 2025-01-12 | COMPLETE | Late delivery | 1 | Standard Class | 609.87 | -242.55 | 515.99 | 4 | 6 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T5485 | 2025-11-25 | Technical issue | Data loss | I'm having an issue with the {product_purchased}. Please assist.  <script type="text/javascript"> var productID = document.getElementById('product_purchases'… | Closed | Critical | Chat | Ok appear ahead director have his consumer. | 0.0 | 5.0 | Positive |
| T5488 | 2025-08-06 | Technical issue | Data loss | I'm encountering a software bug in the {product_purchased}. Whenever I try to perform a specific action, the application crashes. Are there any updates or fixe… | Open | Critical | Chat |  |  |  | Neutral |
| T5494 | 2024-08-28 | Refund request | Payment issue | I'm facing issues logging into my {product_purchased} account. It says my account is locked. What should I do to unlock it?  If you have any questions or con… | Open | Critical | Phone |  |  |  | Neutral |
| T5493 | 2024-07-17 | Billing inquiry | Account access | I'm having an issue with the {product_purchased}. Please assist. I need it as soon as possible! Thank you.  7.3.1 The product number of the product is now di… | Closed | Critical | Chat | Event cell sign. | 0.0 | 4.0 | Positive |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N8862 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Men's Footwear. |
| N8863 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N8864 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band High and support history. |
| N8865 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.8750 with category concentration in Men's Footwear. |
| N8866 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E11160 | TH-C000357-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E11159 | TH-C000357-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E11158 | TH-C000357-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E11157 | TH-C000357-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E11156 | TH-C000357-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL007442 | O060594 | 2025-12-09 | carrier_delay | High | Carrier route delay | Open |
| FUL006753 | O055795 | 2025-09-30 | carrier_delay | High | Carrier route delay | Open |
| FUL006428 | O053505 | 2025-08-28 | carrier_delay | High | Carrier route delay | Open |
| FUL004112 | O037485 | 2025-01-06 | carrier_delay | High | Carrier route delay | Open |
| FUL002453 | O025974 | 2024-07-22 | carrier_delay | High | Carrier route delay | Open |

## H075 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: EE. UU.
- customer_state: CA
- customer_city: Moreno Valley
- primary_market: Pacific Asia
- primary_region: Oceania
- total_orders: 6
- total_sales: 4444.47
- total_profit: 913.62
- late_delivery_count: 19
- late_delivery_rate: 0.8261
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-08-26

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O066358 | 2026-03-03 | 2026-03-05 | COMPLETE | Late delivery | 1 | First Class | 499.98 | 228.9 | 474.98 | 1 | 2 | Late |
| O045542 | 2025-05-03 | 2025-05-06 | PROCESSING | Advance shipping | 0 | Standard Class | 999.86 | 36.94 | 919.37 | 4 | 3 |  |
| O034557 | 2024-11-24 | 2024-11-27 | PENDING_PAYMENT | Late delivery | 1 | Second Class | 969.95 | 139.14 | 901.45 | 2 | 3 | Late |
| O026558 | 2024-07-30 | 2024-08-01 | COMPLETE | Late delivery | 1 | First Class | 809.85 | 225.09 | 719.36 | 1 | 2 | Late |
| O025491 | 2024-07-15 | 2024-07-17 | PROCESSING | Late delivery | 1 | First Class | 389.93 | 127.25 | 372.63 | 1 | 2 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T6888 | 2026-01-12 | Cancellation request | Delivery problem | I'm having an issue with the {product_purchased}. Please assist.  How to determine what version of the service is supported by your company  Install an acc… | Closed | High | Chat | Two most born choice live choice. | 12.1 | 2.0 | Negative |
| T5875 | 2025-10-31 | Product inquiry | Refund request | I'm having an issue with the {product_purchased}. Please assist.  (3) Remove the {product_purchased} in a manner that prevents the merchant from withdrawing … | Open | High | Chat |  |  |  | Neutral |
| T5877 | 2025-05-17 | Technical issue | Payment issue | I'm having an issue with the {product_purchased}. Please assist.  "  // http://www.dota2.com/support/viewtopic.php?f=14&t=4639&msg I'm using the original c… | Closed | High | Phone | Window we effect daughter. | 0.0 | 5.0 | Positive |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N15423 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Women's Apparel. |
| N15424 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N15425 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band High and support history. |
| N15426 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.8261 with category concentration in Women's Apparel. |
| N15427 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E22332 | TH-C001650-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E22331 | TH-C001650-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E22330 | TH-C001650-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E22329 | TH-C001650-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E22328 | TH-C001650-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL008258 | O066358 | 2026-03-03 | carrier_delay | High | Carrier route delay | Open |
| FUL003694 | O034557 | 2024-11-24 | carrier_delay | High | Carrier route delay | Open |
| FUL002539 | O026558 | 2024-07-30 | carrier_delay | High | Carrier route delay | Open |
| FUL002373 | O025491 | 2024-07-15 | carrier_delay | High | Carrier route delay | Open |
| FUL000551 | O013595 | 2024-01-23 | carrier_delay | High | Carrier route delay | Open |

## H076 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: LATAM
- primary_region: South America
- total_orders: 8
- total_sales: 4359.28
- total_profit: 1146.6
- late_delivery_count: 21
- late_delivery_rate: 0.9545
- support_ticket_count: 1
- open_support_ticket_count: 1
- last_meaningful_touch_date: 2017-10-02

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O068865 | 2026-04-09 | 2026-04-15 | SUSPECTED_FRAUD | Shipping canceled | 0 | Standard Class | 399.98 | 101.91 | 363.98 | 4 | 6 | Canceled |
| O067654 | 2026-03-22 | 2026-03-27 | COMPLETE | Late delivery | 1 | Standard Class | 519.86 | 94.1 | 500.66 | 4 | 5 | Late |
| O034470 | 2024-11-23 | 2024-11-29 | CLOSED | Late delivery | 1 | Standard Class | 669.93 | 75.8 | 636.18 | 4 | 6 | Late |
| O025934 | 2024-07-21 | 2024-07-23 | COMPLETE | Late delivery | 1 | First Class | 859.95 | 321.11 | 765.25 | 1 | 2 | Late |
| O011400 | 2023-12-22 | 2023-12-24 | PENDING | Late delivery | 1 | First Class | 299.95 | 65.24 | 224.96 | 1 | 2 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T5742 | 2025-11-02 | Cancellation request | Account access | I'm having an issue with the {product_purchased}. Please assist. I have not been able to contact ux and ux will have no more comment by this post.  UPDATE: W… | Open | Critical | Chat |  |  |  | Neutral |
| T5749 | 2025-06-07 | Technical issue | Network problem | I'm having an issue with the {product_purchased}. Please assist.  I'm having an issue with the {product_purchased}. Please assist. The message is "I have pur… | Closed | Critical | Email | Produce score customer. | 17.9 | 2.0 | Negative |
| T5750 | 2025-04-21 | Cancellation request | Product compatibility | I'm having an issue with the {product_purchased}. Please assist.  I'm having an issue with the "The purchase will be cancelled if the product is not purchase… | Open | Critical | Social media |  |  |  | Neutral |
| T5744 | 2024-12-04 | Cancellation request | Refund request | I'm having an issue with the {product_purchased}. Please assist.  I have the new version of the code with a slightly smaller version.  Thanks.  TODO: The issu… | Closed | Critical | Email | Design first south collection offer point field. | 3.9 | 4.0 | Positive |
| T5743 | 2024-12-01 | Technical issue | Delivery problem | I'm having an issue with the {product_purchased}. Please assist. — Dr. Stephen  I received several different types of items from you and wanted to know what … | Open | Critical | Social media |  |  |  | Neutral |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N16120 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Indoor/Outdoor Games. |
| N16121 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N16122 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band High and support history. |
| N16123 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.9545 with category concentration in Indoor/Outdoor Games. |
| N16124 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E23516 | TH-C001790-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E23515 | TH-C001790-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E23514 | TH-C001790-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E23513 | TH-C001790-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E23512 | TH-C001790-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL008632 | O068865 | 2026-04-09 | cancellation_review | Medium | Customer or fulfillment cancellation | Closed |
| FUL008446 | O067654 | 2026-03-22 | carrier_delay | High | Carrier route delay | Open |
| FUL003680 | O034470 | 2024-11-23 | carrier_delay | High | Carrier route delay | Open |
| FUL002442 | O025934 | 2024-07-21 | carrier_delay | High | Carrier route delay | Open |
| FUL000221 | O011400 | 2023-12-22 | carrier_delay | High | Carrier route delay | Open |

## H077 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Corporate
- customer_country: Puerto Rico
- customer_state: PR
- customer_city: Caguas
- primary_market: LATAM
- primary_region: Central America
- total_orders: 7
- total_sales: 4884.42
- total_profit: 255.47
- late_delivery_count: 18
- late_delivery_rate: 0.72
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-08-30

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O066626 | 2026-03-07 | 2026-03-09 | COMPLETE | Advance shipping | 0 | Standard Class | 999.85 | 276.06 | 821.87 | 4 | 2 |  |
| O059445 | 2025-11-22 | 2025-11-24 | CLOSED | Late delivery | 1 | First Class | 599.91 | -150.65 | 508.82 | 1 | 2 | Late |
| O048469 | 2025-06-15 | 2025-06-17 | PENDING | Late delivery | 1 | First Class | 1019.91 | -386.61 | 891.62 | 1 | 2 | Late |
| O035640 | 2024-12-10 | 2024-12-12 | PROCESSING | Late delivery | 1 | First Class | 529.97 | 185.07 | 478.57 | 1 | 2 | Late |
| O024280 | 2024-06-27 | 2024-07-03 | PROCESSING | Late delivery | 1 | Second Class | 424.87 | 105.59 | 370.44 | 2 | 6 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T6246 | 2025-12-04 | Refund request | Installation support | I'm having an issue with the {product_purchased}. Please assist. I'd say to fix it then, we'd be here by now. Please give us an email if you're stuck with it. … | Open | Low | Chat |  |  |  | Neutral |
| T6244 | 2025-05-04 | Technical issue | Battery life | I'm having an issue with the {product_purchased}. Please assist. I'm unable to find the option to perform the desired action in the {product_purchased}. Could … | Open | Low | Email |  |  |  | Neutral |
| T6243 | 2024-11-17 | Billing inquiry | Battery life | I'm having an issue with the {product_purchased}. Please assist. I've already contacted customer support multiple times, but the issue remains unresolved. | Closed | Low | Phone | Within concern try whatever. | 0.0 | 5.0 | Positive |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N12568 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Men's Footwear. |
| N12569 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N12570 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band High and support history. |
| N12571 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.7200 with category concentration in Men's Footwear. |
| N12572 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E17470 | TH-C001091-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E17469 | TH-C001091-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E17468 | TH-C001091-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E17467 | TH-C001091-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E17466 | TH-C001091-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL007272 | O059445 | 2025-11-22 | carrier_delay | High | Carrier route delay | Open |
| FUL005700 | O048469 | 2025-06-15 | carrier_delay | High | Carrier route delay | Open |
| FUL003840 | O035640 | 2024-12-10 | carrier_delay | High | Carrier route delay | Open |
| FUL002168 | O024280 | 2024-06-27 | carrier_delay | High | Carrier route delay | Open |
| FUL008939 | O008905 | 2023-11-15 | carrier_delay | High | Carrier route delay | Open |

## H078 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: EE. UU.
- customer_state: SC
- customer_city: Summerville
- primary_market: USCA
- primary_region: West of USA
- total_orders: 7
- total_sales: 4334.48
- total_profit: 1022.92
- late_delivery_count: 15
- late_delivery_rate: 0.625
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-06-14

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O061379 | 2025-12-20 | 2025-12-25 | CLOSED | Late delivery | 1 | Standard Class | 609.91 | 144.26 | 549.52 | 4 | 5 | Late |
| O058773 | 2025-11-12 | 2025-11-16 | COMPLETE | Shipping on time | 0 | Standard Class | 639.94 | 188.98 | 602.34 | 4 | 4 |  |
| O038034 | 2025-01-14 | 2025-01-19 | ON_HOLD | Late delivery | 1 | Second Class | 869.89 | 259.7 | 831.49 | 2 | 5 | Late |
| O037828 | 2025-01-11 | 2025-01-15 | COMPLETE | Shipping on time | 0 | Standard Class | 274.91 | 77.16 | 255.67 | 4 | 4 |  |
| O031323 | 2024-10-08 | 2024-10-12 | PENDING_PAYMENT | Shipping on time | 0 | Standard Class | 629.97 | 191.58 | 541.47 | 4 | 4 |  |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N16302 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Cleats. |
| N16305 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 0.6250 with category concentration in Cleats. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E23828 | TH-C001827-[redacted] | 8 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E23827 | TH-C001827-[redacted] | 7 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E23826 | TH-C001827-[redacted] | 6 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E23825 | TH-C001827-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Late Delivery Recovery - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E23824 | TH-C001827-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Late Delivery Recovery - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL007549 | O061379 | 2025-12-20 | carrier_delay | High | Carrier route delay | Open |
| FUL004189 | O038034 | 2025-01-14 | carrier_delay | High | Carrier route delay | Open |
| FUL002001 | O023135 | 2024-06-10 | carrier_delay | High | Carrier route delay | Open |
| FUL001568 | O020390 | 2024-05-01 | carrier_delay | High | Carrier route delay | Open |

## H079 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Consumer
- customer_country: EE. UU.
- customer_state: CA
- customer_city: Fresno
- primary_market: Europe
- primary_region: Western Europe
- total_orders: 5
- total_sales: 4474.49
- total_profit: 1148.69
- late_delivery_count: 19
- late_delivery_rate: 1.0
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2016-12-06
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O048320 | 2025-06-13 | 2025-06-19 | COMPLETE | Late delivery | 1 | Standard Class | 349.93 | 32.66 | 330.93 | 4 | 6 | Late |
| O023030 | 2024-06-09 | 2024-06-15 | COMPLETE | Late delivery | 1 | Standard Class | 1124.89 | 129.9 | 1093.89 | 4 | 6 | Late |
| O017160 | 2024-03-15 | 2024-03-21 | PENDING_PAYMENT | Late delivery | 1 | Standard Class | 1379.85 | 522.78 | 1286.7 | 4 | 6 | Late |
| O015292 | 2024-02-17 | 2024-02-19 | CLOSED | Late delivery | 1 | First Class | 1119.83 | 339.77 | 1072.24 | 1 | 2 | Late |
| O011304 | 2023-12-20 | 2023-12-25 | COMPLETE | Late delivery | 1 | Standard Class | 499.99 | 123.58 | 443.99 | 4 | 5 | Late |

**Support tickets**

| ticket_id | date_of_purchase | ticket_type | ticket_subject | ticket_description | ticket_status | ticket_priority | ticket_channel | resolution | resolution_time_hours | customer_satisfaction_rating | customer_sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T6025 | 2026-03-24 | Billing inquiry | Peripheral compatibility | My {product_purchased} is making strange noises and not functioning properly. I suspect there might be a hardware issue. Can you please help me with this?  i… | Open | Critical | Phone |  |  |  | Neutral |
| T5102 | 2025-12-02 | Billing inquiry | Software bug | I'm having an issue with the {product_purchased}. Please assist.  As expected, an error message says: 'No product available.  '  In the case of this issu… | Pending | Critical | Phone |  |  |  | Neutral |
| T6032 | 2025-11-29 | Cancellation request | Product recommendation | I'm having an issue with the {product_purchased}. Please assist. Sorry, I get no support.  5 2/1/2017 7:58:03 The one I bought (or used) was quite the surpri… | Open | Critical | Social media |  |  |  | Neutral |
| T5106 | 2025-11-17 | Product inquiry | Battery life | I'm having an issue with the {product_purchased}. Please assist. I need assistance as soon as possible because it's affecting my work and productivity. | Pending | Critical | Chat |  |  |  | Neutral |
| T6030 | 2025-09-13 | Cancellation request | Display issue | I'm having an issue with the {product_purchased}. Please assist. Thank you.", "id":0}, "description": "  {product_purchased", "id":null}  {"id":16," I've r… | Closed | Critical | Phone | Vote hospital political indeed southern possible land. | 10.8 | 1.0 | Negative |

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N15128 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Fishing. |
| N15129 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N15130 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer needs follow-up based on risk band Critical and support history. |
| N15131 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Customer activity for the customer shows late-rate 1.0000 with category concentration in Fishing. |
| N15132 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Prepared next-step context for the customer; retain evidence links before outreach. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E21832 | TH-C001597-[redacted] | 14 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E21831 | TH-C001597-[redacted] | 13 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E21830 | TH-C001597-[redacted] | 12 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E21829 | TH-C001597-[redacted] | 11 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E21828 | TH-C001597-[redacted] | 10 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL005674 | O048320 | 2025-06-13 | carrier_delay | High | Carrier route delay | Open |
| FUL001983 | O023030 | 2024-06-09 | carrier_delay | High | Carrier route delay | Open |
| FUL001086 | O017160 | 2024-03-15 | carrier_delay | High | Carrier route delay | Open |
| FUL000808 | O015292 | 2024-02-17 | carrier_delay | High | Carrier route delay | Open |
| FUL000204 | O011304 | 2023-12-20 | carrier_delay | High | Carrier route delay | Open |

## H080 (review date 2026-05-06 00:00:00)

**Account**

- customer_segment: Home Office
- customer_country: EE. UU.
- customer_state: MO
- customer_city: Florissant
- primary_market: LATAM
- primary_region: Caribbean
- total_orders: 9
- total_sales: 4838.61
- total_profit: 258.64
- late_delivery_count: 13
- late_delivery_rate: 0.5
- support_ticket_count: 1
- open_support_ticket_count: 0
- last_meaningful_touch_date: 2017-08-15
- earlier reviews on: 2026-05-08 00:00:00, 2026-05-07 00:00:00

**Recent orders**

| order_id | order_date | shipping_date | order_status | delivery_status | late_delivery_risk | shipping_mode | order_sales | order_profit | order_total | days_scheduled | days_actual | issue_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O065589 | 2026-02-20 | 2026-02-25 | COMPLETE | Late delivery | 1 | Standard Class | 639.94 | 181.49 | 565.29 | 4 | 5 | Late |
| O059774 | 2025-11-27 | 2025-12-02 | PENDING | Late delivery | 1 | Standard Class | 659.96 | 181.15 | 569.66 | 4 | 5 | Late |
| O039801 | 2025-02-08 | 2025-02-10 | CLOSED | Advance shipping | 0 | Standard Class | 869.93 | -99.72 | 807.69 | 4 | 2 |  |
| O039266 | 2025-02-01 | 2025-02-03 | PENDING | Advance shipping | 0 | Standard Class | 489.94 | -183.43 | 434.75 | 4 | 2 |  |
| O027015 | 2024-08-06 | 2024-08-06 | CLOSED | Shipping on time | 0 | Same Day | 599.97 | -8.88 | 551.97 | 0 | 0 |  |

**Support tickets**

(none)

**Account notes**

| note_id | note_date | author | note_type | note_text |
|---|---|---|---|---|
| N12821 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | Reviewed recent order and support signals for the customer; topic is [redacted]. |
| N12820 | 2026-05-06 | Nelson DSS Synthetic CS | Customer Risk Review | the customer has a [redacted] pattern tied to Water Sports. |

**Emails**

| email_id | thread_id | message_sequence | direction | date | sender_type | recipient_type | subject | body | sentiment_hint |
|---|---|---|---|---|---|---|---|---|---|
| E17904 | TH-C001145-[redacted] | 12 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E17902 | TH-C001145-[redacted] | 10 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E17897 | TH-C001145-[redacted] | 5 | Customer | 2026-05-06 | Customer | Customer Success | Executive Escalation - the customer | the customer is following up on [redacted] and needs clarity on next steps. | Concerned |
| E17896 | TH-C001145-[redacted] | 4 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |
| E17894 | TH-C001145-[redacted] | 2 | Customer Success | 2026-05-06 | Customer Success | Customer | Executive Escalation - the customer | Customer Success responded to the customer with context, evidence, and a proposed next action for [redacted]. | Concerned |

**Fulfillment events**

| fulfillment_event_id | order_id | event_date | event_type | severity | root_cause | resolution_status |
|---|---|---|---|---|---|---|
| FUL008144 | O065589 | 2026-02-20 | carrier_delay | High | Carrier route delay | Open |
| FUL007316 | O059774 | 2025-11-27 | carrier_delay | High | Carrier route delay | Open |
| FUL004595 | O004095 | 2023-09-06 | carrier_delay | High | Carrier route delay | Open |
| FUL008657 | O000705 | 2023-07-19 | carrier_delay | High | Carrier route delay | Open |
