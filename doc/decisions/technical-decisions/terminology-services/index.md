# Terminology services

!!! note
    Work in Progress

**Status**: first sketch, work in progress, request for collaboration

**Date**: Updated 2025-06-27

**Governance**: To Be Discovered; potentially a combo of this repo participants,
DHCW CISO, NHS Wales UCB peers, etc.

## Context

Broadly, many of our medical applications provide many kinds search
capabilities, such as terminology search for procedure names and codes,
prescription  names and codes, location names and codes, etc.

A typical example is a clinician using a medical application who wants to search
for the medication "paracetamol", and find the medication code, or synonyms such
as "acetaminophen", or specific SKUs such as for a specific brands or specific
dose.

Many of our NHS Wales clinicians will be using the SNOMED CT ontology and/or the
NHS Wale OntoServer. However, it turns out there are many areas that SNOMED CT
and OntoServer don't seem to cover as well as some of the clinicians want. This
is especially turning up in the emergency department, where speed of lookup is a
key need, and where handling of unexpected patient presentations is a key need
as well.

Broadly, this is the use case: As a clinician, I want to search for a patient
presentation information quickly and with high success even with imprecise inputs.

The first priority is to make existing kinds of searches work better and faster.
As a clinician, medication "paracetamol" and I want the search to work well ,
using typical good search practices, and see results that include the best
matches for medical use.

* Autocorrect search such as "porocitimel" because spell check helps, especially
  for harder-to-spell works, and for English-as-an-successive-language speakers.

* Synonym search "acetaminophen" because this is a synonym and a more-common
  name in some countries.

* Brand name search "Tylenol" because this is a worldwide popular brand.

* Code search such as "41833511000001106" because this is SCTID code for a
  specific kind and dose.

* Scan code such as a barcode or QR code because these can be printed on paper,
  or bottles, or boxes, etc. Notably, QR code printing is now a security
  requirement for some medicine packaging.

* Results that include more-general answers, such as the more-general category
  of painkillers.

* Results that include more-specific answers, such as the more-specific category
  of pediatric paracetamol.

* Results with sibling answers with differences, such as returning the sibling
  painkiller "aspirin", pluse with differences noted such as "not recommended
  for people older than X or younger than Y or who are pregnant". We anticipate
  that this is a large research area that is beyond this ADR scope.

The secondary priority is how we can collect-store-share more unusual
information, that is especially relevant for fast response:

* Patient explains medications or prescriptions or treatments, such as verbally,
  or by showing packaging or a pill, or by showing a photo or email from another
  clinician.

* Clinicians are confused about life-critical terminology e.g. "anaphylaxis" cf.
  "anaphylactic" cf. "anaphylactoid", and the levels/stages that determine
  life-saving protocols.

The tertiary priority is how we can better align with long-term goals for our
organization goal of collect-store-share, including in multiple ways:

* Multilocation information e.g. people who are immigrating.

* Multilingual information e.g. Hindi, Spanish, Mandarin, Polish, Cymraeg, etc.

* Multimodal information e.g. TCM, supplements, herbalism, nutrition practices,
  sports optimization, etc.

## Drivers

Specifically right now, the emergency department module authentication needs
some kind of plan for authentication using "multi-party authentication" (MPA)
which is historically known as the "two-person rule" (2PR).

* Our current understanding is that there's a medical must-have requirement to
have two clinicians do simultaneous authentication in real-time during high-risk
treatments, procedures, prescriptions, etc.

* I'm seeking a terminology service that provides lookup via FHIR and/or RESTful
  API and/or GraphQL that returns an indicator of whether a specific medication
  needs multi-party authentication.

We currently believe the fastest/simplest/best path to the emergency department
module (EDM) proof of capability (PoC) for multi-party authentication (MPA) is
to skip building it into the app, and instead making an API call to external
terminology services, such as a SNOMED service, or MPA-compliance service, etc.

* We want to align with industry standards (not reinvent the wheel).

* We want to get good-enough quality work in place now, so we can try it out, ask
for feedback, and get help.

* We have recently seen working terminology services, including two written by
NHS clinicians, that have these kinds of capabilities. These solo-built servers
seem to demonstrate that there's not yet any DHCW solution or NHS Wales solution
that covers these physicians' use cases well enough.

We believe that terminology services do not, and must not, contain any
personally-identifying information, user-specific information,
medically-sensitive information, etc. This means terminology services are
excellent candidates for external services, such as DCHW building a free open
source tool, or DHCW buying Software as a Service APIs from a vendor, or some
kind of hybrid.

The makers of OntoServer distinguish between a "terminology server" (which is
the software they are building) and a "terminology service" which in their
country is a national organization that handles change management of clinical
terminology. The OntoServer terminology server is able to update itself with
changes provided by the national terminology service.

As far as I can tell, thus far, there's currently no worldwide sync by default
with OntoServer, and there's can be a gap of a few months where the terminology
server lags the terminology service.

## Assessment

We intend to assess at least three kinds of options, and timebox our assessment
of these kinds to just a few hours per kind:

1. Build. This means building our our terminology services at DHCW, using our
   new ways of working in the cloud, with modern practices, automatic testing,
   etc.

2. Buy. This means paying a vendor for terminology services, including the
   search API, using either a medical-specific vendor such as for SNOMED codes,
   or a global generic vendor such as for faceted search.

3. Brief. This means we'd code a "brief", which is a quick placeholder that
   demonstrates the use case, and drives discussion forward. The purpose of
   doing a brief is a short-duration summary of the facts, to help instruct and
   inform the chain-of-command. The goal of this brief would be to justify more
   work, funding, testing, etc.

## Tests

These are examples of the kinds of tests we could create:

* Provide a photo of a patient prescription pill bottle, and receive as much of
  this data as possible: medicine name, dose, prescription date, expiration
  date, prescribing clinic public contact information, etc. Do this in the
  various NHS languages for nhsinform.

* As above for more modalities, if possible, such as digital text (e.g. patient
  sends the clinician an email), handwritten text (e.g. patient has a doctor's
  prescription handwritten on paper), speech of a patient stating their
  prescription information (e.g. patient is calling the GP or in person).

If specific search terms may be helpful, here are some that can be for test cases:

* Distinguish between "anaphylaxis", "anaphylactic", "anaphylactoid", and
  whatever stages the emergency department wants-- which may vary by location.

* Cymraeg terms, such as "danadl poethion" in Welsh means "stinging nettles" and
is a common plant that treats allergies.

* Research medications, such as "AD109" is a drug for sleep apnea that works on
  hypoglossal motor nucleus (HMN).

* Multicultural medicine, such as "Qi" in traditional Chinese medicine can be loosely interpreted as a concept for energy.

* Brand marks, such as "Tylenol" refers to a brand name of paracetemol plus many
  variations such as Tylenol PM, containing many other medications such as
  co-codamol, dextromethorphan, methocarbamol, guaifenesin, pseudoephedrine,
  caffeine, diphenhydramine, chlorpheniramine and phenylephrine.

* Brand abbreviations, such as "DNRS" for Dynamic Neural Retraining System, a
  treatment to improve limbic system health.

## Recommendation - Decision Outcome

TODO
