# GitColdChainWatch Explainability Specification

This document provides a transparent, verifiable architectural breakdown of how **GitColdChainWatch** operates, processes input, makes decisions, and enforces security boundaries.

---

## 1. Input Data and Data Sources Used

GitColdChainWatch consumes IoT temperature datalogger time-series logs, GPS shipment tracking telemetry, pharmaceutical consignment manifests, and USP/WHO cold chain guidelines. These data sources include continuous temperature readings in Celsius, relative humidity percentages, geofence coordinates, and transit timestamp arrays. The agent ingests these inputs in raw JSON, CSV, and sensor stream format and parses them into standardized cold chain validation objects for downstream regulatory analysis. Carrier cold-chain SLA contracts and GDP compliance archives are also monitored as sensitive data sources to ensure product efficacy is strictly maintained.

---

## 2. How It Decides and Reasoning Process

The decision making process follows a deterministic, five-stage analytical pipeline designed to eliminate ambiguity and hallucination. When shipment datalogger telemetry is received, the agent first evaluates temperature compliance using the temp-excursion-evaluator tool to verify that thermal limits (2°C-8°C) were maintained throughout transit. Next, the reasoning engine invokes the mkt-kinetic-temp-calculator tool to compute Mean Kinetic Temperature according to USP standards. Furthermore, transit duration is audited using the transit-sla-auditor tool. Finally, the agent correlates all thermal findings against predefined pharmaceutical quality standards to issue a conclusive verdict of APPROVED, BLOCKED, or NEEDS_REVIEW alongside an automated release certificate.

---

## 3. Constraints, Limitations, and Known Issues

GitColdChainWatch operates under strict operational constraints to prevent false positives and non-deterministic behavior across different agent frameworks. GitColdChainWatch operates under strict operational constraints to prevent degraded or ineffective pharmaceuticals from entering the healthcare supply chain. The agent is deliberately limited to time-series temperature parsing and kinetic equation evaluation and cannot physically perform biochemical assays on spoiled medications. Another known issue and limitation is that uncalibrated third-party analog sensors with drifting clock crystals may require secondary human review rather than autonomous blocking. Furthermore, the agent enforces a low temperature constraint of 0.1 to maintain strict predictability across all supported export frameworks.
