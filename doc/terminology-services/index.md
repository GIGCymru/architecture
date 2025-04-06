# Terminology services

!!! note
    Work in Progress

**Status**: first sketch, work in progress, request for collaboration

**Date**: Updated 2025-04-06

**Governance**: To Be Discovered; potentially a combo of this repo partipants, DHCW CISO, NHS Wales UCB peers, etc.

## Context

Broadly, many of our medical applications provide many kinds search capabilities, such as medical terminology search for procedure names and codes, prescription  names and codes, location names and codes, etc. A typical example is a clinician using a medical application who wants to search for the medication "paracetamol", and find the medication code, or synonyms such as "acetaminophen", or specific SKUs such as for a specific brands or specific dose.

Broadly, this is the use case: As a clinician, I want to search for the medication "paracetamol", and I want the search to work well, using typical good search practices, and see results that include the best matches for medical use.

* Autocorrect search such as "porocitimel" because spell check helps, especially for harder-to-spell works, and for English-as-an-successive-language speakers.

* Synonym search "acetaminophen" because this is a synonym and a more-common name some countries.

* Code search such as "41833511000001106" because this is SCTID code for a specific kind and dose.

* Scan code such as a barcode or QR code because these can be printed on paper, or bottles, or boxes, etc.

* Results that include more-general answers, such as the more-general category of painkillers.

* Results that include more-specific answers, such as the more-specific category of pediatric paracetamol.
  
* Results with sibling answers with differences, such as returning the sibling painkiller "aspirin", pluse with differences noted such as "not recommended for people older than X or younger than Y or who are pregnant". We anticipate that this is a large research area that is beyond this ADR scope.

Specifically right now, the emergency department module authentication needs some kind of plan for authentication using "multi-party authentication" (MPA) which is historically known as the "two-person rule" (2PR). Our current understanding is that there's a medical must-have requirement to have two clinicians do simultaneous authentication in real-time during high-risk treatments, procedures, prescriptions, etc.

## Drivers

We currently believe the fastest/simplest/best path to the emergency department module (EDM) proof of capability (PoC) for multi-party authentication (MPA) is to skip building it into the app, and instead making an API call to external terminology services, such as a SNOMED service, or MPA-compliance service, etc.

We want to align with industry standards (not reinvent the wheel).

We want to get good-enough quality work in place now, so we can try it out, ask for feedback, and get help.

We have recently seen mostly-working prototypes of terminology services, including two written by NHS clinicians, that are very close to having this capability. These prototypes also seem to demonstrate that there's not yet any DHCW solution or NHS Wales solution that covers this use case well.

We believe that terminology services do not, and must not, contain any personally-identifying information, user-specific information, medically-senstive information, etc. This means terminology services are excellent candidates for external services, such as DCHW building a free open source tool, or DHCW buying Software as a Service APIs from a vendor, or some kind of hybrid.

We need to validate our understanding of all the above.

## Assessment

We intend to assess at least three kinds of options, and timebox our assessment of these kinds to just a few hours per kind:

1. Build. This means building our our terminology services at DHCW, using our new ways of working in the cloud, with modern practices, automatic testing, etc.

2. Buy. This means paying a vendor for terminology services, including the search API, using either a medical-specific vendor such as for SNOMED codes, or a global generic vendor such as for faceted search.

3. Brief. This means we'd code a "brief", which is a quick placeholder that demonstrates the use case, and drives discussion forward. The purpose of doing a brief is a short-duration summary of the facts, to help instruct and inform the chain-of-command. The goal of this brief would be to justify more work, funding, testing, etc.

## Recommendation - Decision Outcome

TODO
