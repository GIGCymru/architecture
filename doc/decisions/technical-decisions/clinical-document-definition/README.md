# What is a clinical document

Ensuring clarity, compliance, and consistency in clinical document management.

**Status**: { TDAG 03/11/25 (Approved), Architecture CoP 15/01/2026}
**Level**: { 4 }
**Updated**: { 2025-10-23 }

## Summary

There are significant inconsistencies and confusion across teams and systems regarding the definition of a "clinical document" within Digital Health Services. This lack of a shared understanding leads to misalignment in communication, integration challenges between systems, system misuse and inconsistencies in data governance practices.

To ensure clarity and interoperability, it is essential to establish a consistent, organisation-wide definition of a "clinical document" that distinguishes it from other artefacts such as, but not limited to, clinical data (form-based data), medical images, and diagnostic results.

A clear and standardised definition, supported by robust governance, will strengthen data integrity, improve cross-system integration, and enhance the safe and effective delivery of digital health services across NHS Wales.

## Drivers

The establishment of a consistent and standardised definition of a "clinical document" is driven by key stakeholder feedback obtained through cross-programme workshops, which identified significant variation in interpretation and implementation across systems. Addressing this inconsistency is essential to improve alignment and interoperability within the national digital ecosystem.

This work directly supports National Target Architecture, ensuring coherence and integration across digital health services in Wales. Furthermore, the transition towards adopting FHIR for interoperability and FHIR DocumentReference as the standard mechanism for document metadata provides a strategic opportunity to formalise governance, prevent misuse, and embed internationally recognised best practices.

Collectively, these drivers underpin the need for a unified definition to enhance data integrity, operational efficiency, and safe information exchange across NHS Wales.

A document should be defined not just by its file format (e.g., PDF), or by its type (clinic letter, discharge letter, clinic note) but by its function, intent, and context within clinical workflows. A true document represents a discrete, authored unit of information that:

Has clear authorship and creation metadata

- Is version-controlled and auditable
- Is bound to a specific clinical or administrative event
- Is intended for long-term storage and retrieval
- Is readable, shareable, and legally defensible as a snapshot of care or decision-making
- Can be indexed and discovered via metadata and search

Documents serve a critical role in continuity of care, legal accountability, information governance, and clinical safety. They offer a formal, persistent record designed to be understood by others (clinicians, patients, auditors), often across organisational boundaries.

However, it is equally important to define what a document is **NOT**:

- It is not a discrete data point: individual measurements like heart rate, lab results, or blood pressure readings which are data and not a document.
- It is not a real-time stream: telemetry feeds or continuously updated dashboards are transient, not persistent.
- It is not diagnostic images (e.g., X-rays, CT scans, echocardiograms, ultrasound) or media files that may be referenced by documents but are not themselves documents.
- It is not raw, unstructured notes without context or authorship (e.g., free-text comments in forms or internal system logs).
- It is not UI output or screen printouts unless preserved in an authored, versioned, and clinically contextual format.
- It is not temporary or incomplete drafts: unless formally authored, signed off, and stored as part of the health record.
- It is not an active form, as structured clinical data, should be stored in a clinical data repository; once finalised, a copy or summary can be converted into a formally authored, versioned document for the health record.

Without this functional definition and boundary-setting, we risk:

- Storing unnecessary or incomplete information
- Storage Misuse
- Search and classification issues
- Legal and governance gaps (e.g., storing unapproved or draft content as part of the official record)
- Inconsistent clinician experience and trust in the system

A shared understanding of what a clinical document is, and is not, will help inform system architecture, clinical workflows, information governance, and retention strategies across NHS Wales.

## Options
N/A

## Recommendation

Adopt and operationalise a definition of a clinical document across systems, teams, and governance processes to ensure consistency, safety, and interoperability. This definition should guide system design, information governance, user training, and record-keeping practices.

They should be defined as the following:

A discrete, authored, version-controlled unit of clinical or administrative information that is contextually bound to a care event or activity, intended for long-term storage and reference. It should be retrievable, legally defensible, and include sufficient metadata (e.g., author, creation time, document type, subject, version control and encounter context).

Core Attributes:
- Persistent: Remains unchanged over time; intended for long-term storage and retrieval.
- Complete: Represents a whole, self-contained snapshot of care or decision-making.
- Authentic: Has clear authorship, provenance, and is auditable.
- Contextual: Bound to a specific clinical or administrative event or activity.
- Legally Defensible: Meets standards for legal admissibility and governance (e.g., BS 10008).
- Machine-Processable: Structured for indexing, search, and interoperability across systems.
- Discoverable: Includes sufficient metadata (e.g., author, creation time, document type, subject, version, and encounter context) and alignment to [FHIR Document Reference](https://simplifier.net/guide/fhir-standards-wales-implementation-guide/Home/FHIR-Assets/Profiles-and-Extensions/Profiles/DataStandardsWales-DocumentReference?version=2.4.0)

Examples include:
- Discharge summaries
- Clinic letters
- Consent forms
- Care plans

To prevent misclassification and ensure alignment with the business capabilities defined in the National Target Architecture, the following items should not be considered documents for storage in the clinical document service.

- Results: Single data points (e.g., lab value, blood pressure reading)
- Real-time streams (e.g., telemetry feeds, dashboards)
- Diagnostic images or media files (e.g., X-ray, CT scan, ultrasound)
- Raw or unstructured notes without authorship or clinical context
- Screen printouts unless versioned and contextualised
- Temporary drafts or internal UI output not formally authored or signed off
- Clinical Data: active forms data, as this is clinical data and requires to be structured and stored in a clinical data repository, unless finalised, presented as a PDF, versioned, and stored with appropriate metadata

This definition provides standards alignment and is supported by:
- [SNOMED CT](https://termbrowser.nhs.uk/?): coded clinical content for semantic interoperability
- FHIR (UK Core / NHS Wales guidance): structured, machine-readable format for interoperability [FHIR Document Reference](https://simplifier.net/guide/fhir-standards-wales-implementation-guide/Home/FHIR-Assets/Profiles-and-Extensions/Profiles/DataStandardsWales-DocumentReference?version=2.4.0)
- Welsh Health Circulars (WHC): [WHC/2015/053](https://www.gov.wales/introduction-snomed-ct-nhs-information-standard-whc201553) & [WHC/2023/018](https://www.gov.wales/introduction-hl7-fhir-foundational-standard-all-nhs-wales-bodies-whc2023018)
- [BS 10008](https://knowledge.bsigroup.com/products/evidential-weight-and-legal-admissibility-of-electronically-stored-information-esi-code-of-practice-for-implementation-of-bs-10008-1): legal admissibility of electronic records
- [IHE XDS](https://profiles.ihe.net/ITI/TF/Volume1/ch-10.html): cross-organisation indexing and sharing
- [FAIR Principles](https://www.go-fair.org/fair-principles/): provide guidelines to improve the Findability, Accessibility, Interoperability, and Reuse of digital assets

Action Steps:
- Embed this definition into technical specifications, governance frameworks, and clinical safety cases
- Align with national and international standards (e.g., Document metadata standard, IHE XDS, FHIR DocumentReference)
- Train system designers, product teams, and clinical staff on appropriate classification and usage
- Ensure search, lifecycle management, and metadata tagging are aligned with the above definition

Exclude non-document artefacts from document repositories (e.g., data points, logs, raw media, Dicom images, active forms, etc)

## Consequences

**Clinical & Technical Practice**:
- Establishes a clear, standard definition of a clinical document across all systems.
- Enhances patient safety and trust by ensuring only complete, authorised documents are stored and shared.
- Streamlines workflows and improves discoverability through consistent metadata.
- Requires user education and cultural adoption to embed new documentation practices.

Teams will need to adjust to clear boundaries between documents, clinical data, forms, and DICOM images, moving away from the historic practice of treating all artefacts as “documents”.

**Legacy Data Organisations**:
- Existing repositories will need audit, reclassification, and cleansing to align with the new definition.
- Investment will be required to transition legacy data into the new architecture, ensuring compliance and interoperability.
- Metadata enrichment and migration planning will be essential to support discoverability and governance.

**Future Compliance and Strategy**:
- Once new document microservices are in place, all new systems and integrations must comply with the agreed definition and metadata standards.
- Strengthens governance and interoperability across NHS Wales through consistent adoption of FHIR DocumentReference.
- Provides a clear migration pathway toward a modern, scalable, cloud-native document ecosystem aligned with the National Target Architecture.
