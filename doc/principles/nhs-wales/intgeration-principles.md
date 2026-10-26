# Integration Principles

> **⚠️ DRAFT – FOR REVIEW**
>
> These integration principles are being developed as part of
> the National Target Architecture and have not yet been formally endorsed.

  
## IP01. Open Standards-based Integration  
  Use approved open standards, information models and reusable integration patterns by default. Document exceptions for bespoke formats or pair-specific designs.  
  
## IP02. Contract-first integration  
  
Agree a versioned contract before implementation. It must cover structure and meaning, validation, security, responses, reliability and change.

## IP03. Govern API access and subscriptions  
  
Register and manage API access and feed subscriptions through approved systems and processes, with consistent controls proportionate to risk.

## IP04. Make integrations discoverable and manage them through their lifecycle  
  
Every integration must be registered, discoverable and actively managed from inception through change to retirement.

## IP05. Build portable, independently deployable integration components  

Build modular components that can be deployed independently and moved between suitable hosting environments. Use containers by default, while allowing justified platform-specific services.

## IP06. Make ownership explicit and keep platform responsibilities bounded  
  
Keep accountability with source, target and integration-component owners. Give every integration and product workload named business, technical and operational owners.

## IP07. Enable local autonomy within national guardrails  
  
Place decisions and capabilities at the most appropriate national, shared or local level. Apply national standards and guardrails while allowing conformant local solutions.

## IP08. Manage integration technical debt deliberately

Avoid unnecessary technical debt. Where delivery or platform-exit constraints require it, record, assess and own the debt through to remediation or retirement.

## IP09. Design for reliable delivery and safe reprocessing  
  
Define delivery, acknowledgement, retry and redelivery rules for each pattern. Anticipate duplicates, delays and out of-order delivery, and support safe reprocessing.  

## IP10. Provide end-to-end visibility and reconciliation  
  
Trace delivery from source to target, including relevant outcomes from the receiving system. Use correlation and reconciliation to direct failures to the responsible owner.  

## IP11. Automate exception handling, recovery and operational response  
  
Handle failures through defined, observable and automated mechanisms wherever possible. Provide actionable errors, controlled recovery and clear ownership when people must intervene..  

## IP12. Preserve meaning, provenance and clinical integrity end to end

Preserve information meaning, provenance and clinical integrity throughout the exchange, including its correct association with the people and other entities concerned.

Preserve information meaning, provenance and clinical integrity throughout the exchange, including its correct association with the people and other entities concerned.
