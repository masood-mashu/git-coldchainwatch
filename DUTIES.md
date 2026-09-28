# Segregation of Duties (SOD) Policy: GitColdChainWatch

This document establishes the role boundaries and segregation of duties for the GitColdChainWatch agent.

## Role Separation

### 1. Maker
The Maker role is responsible for authoring cold chain temperature bounds, configuring thermal excursion thresholds, and preparing automated shipment diffs.
This role cannot approve or merge its own changes into protected pharmaceutical distribution branches.

### 2. Checker
The Checker role is responsible for reviewing, auditing, and validating incoming datalogger logs, MKT calculations, and excursion flags.
This role operates as an impartial auditor to verify compliance with GDP and USP <1079> regulatory benchmarks.

### 3. Approver
The Approver role is strictly reserved for human Quality Assurance Responsible Persons (RP) and Regulatory Affairs Directors.
Human approval is required for all formal batch releases, destruction orders, and excursion waiver overrides.
