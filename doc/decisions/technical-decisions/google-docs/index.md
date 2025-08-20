# Google Docs

!!! note
    Work in Progress

**Status**: first sketch, work in progress, request for collaboration

**Date**: 2025-08-20

**Governance**: To Be Discovered; potentially a combo of this repo participants, DHCW CISO, NHS Wales UCB peers, etc.

## Situation - Context and Problem Statement

Google Docs is worldwide way to write documents, with valuable capabilities for collaboration such as shared writing, commenting, and viewing. This ARD is to add Google Docs to our capabilities.

Currently, our organization trusts Google for many services such as:

* Google Cloud for storing documentation of high-security protected health information (PHI) such as patient health records

* Google Sign In for federated authentication, Google Android for our mobile phones, etc.

* Google Mail for mission-critical emergency-grade disaster-recovery needs, etc.

Our most-recently-known documentation shows thousands of staff using Google for a wide range of purposes. However, our organization currently does not have a policy for Google Docs.

Therefore this ADR is to start with a simple small first step:

* Officially permit staff to use Google Sign In with official email addresses, then use Google Docs as usual, and collaborate with staff and similar trusted people e.g. trusted partners, vendors, peers.

## Drivers

* Joel wants to use Google Docs because it's a quick easy way to collaborate during our upskilling of staff, because it's easy to edit a document with a bunch of staff simultaneously.
  
* Joel's done this at many companies, ranging from tiny startups to very large enterprises, ranging from the private sector to public sector, and including in regulated industries such as fintech and healthcare. Joel's opinion is Google Docs security is fine for BAUI.

## Considerations

* Our organization has auditing requirements. Therefor this ADR includes a pragmatic path forward: we say that we'll use Google Docs for temporary work only i.e. anything in Google Docs that we want to keep permanently must also have a copy in our organization's systems of record, such as iPassport or Sharepoint. This aligns with our corporate strategy for PHI as well, where we're aiming for each product team to store data however they wish so long as the product also writes to our FHIR store.

* Presuming this ADR is approved, then it opens up viable next steps for an ADR for Google Sheets,  Google Slides, etc.

* The great news is our organisation already has Google Docs running. If you're on staff, then you can sign in to Google, and add Google Docs, and start using it. This is on our officially-approved Google enterprise account. In other words, this ADR is solely seeking the official blessing-- it's not seeking to change any fundamental tech or any fundamental vendor.

## Considered options and related tooling

* Alternatives that are officially approved: iPassport and Sharepoint. Joel's talked with many users of iPassport and it doesn't seem fit for quick scratch work. Joel's talked with many Sharepoint users and it's generally thought to be more-problematic than Google Docs.

* We might have a similar kind of issue with other documentation services that our organization uses, such as Jira, Trello, Confluence, Roadmunk, Basecamp, GitHub, Apple Notes, Google Keep, etc. This ADR deliberately is solely about Google Docs because it's urgent for Joel to get Google Docs blessed ASAP to help upskill our testers starting on September 10.
