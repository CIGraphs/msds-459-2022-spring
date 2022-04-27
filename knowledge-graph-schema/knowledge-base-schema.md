# Knowledge Graph Schema for Competitive Intelligence

## Basic Nodes

-   **company**: includes subsidiaries and divisions, could be a competitor, could be customer in B2B, could be for-profit, nonprofit, or governmental organization, likely to have an extensive attribute list, brand name
-   **industry**: generic group or subgroup of companies
-   **person**: could be a customer in B2C, reviewer or employee of company or product
-   **group**: generic group of people
-   **product**: includes product category/group

## Reference Nodes (point to relational tables)

-   **article**: general information in a relational table with article name, keywords for search, and JSON text [original data in a JSON lines (jl) file]
-   **review**: evaluation in a relational table with person name, product or company name, keywords for search, and JSON text [original data in a JSON lines (jl) file]
-   **data**: relational table with text strings and/or numbers in rows and columns, can be a menu of items or bill of materials [original data in a comma-delimited text (csv) file]

## Edges/Relations

-   **competes_with**: company-to-company or product-to-product relation
-   **has_potential_entrant**: company-to-company relation across industries
-   **makes**: has product in company-to-product relation, reviews company or product
-   **supplies**: has customer, company-to-company relation for B2B, company-to-person relation for B2C; company-to-data, or product-to-data relation, where a data table represents a menu of items or bill of materials, use **hires** for person or group
-   **has_substitute**: cross-industry product-to-product competitive relation
-   **has_article**: text associated with a basic node
-   **has_data**: table of text and/or data relating to a basic node
-   **has_review**: company-to-review or product-to-review relation
-   **is_in**: product-to-product category relation, company-to-industry relation
-   **is_like**: similarity relation between nodes of the same basic type
-   **hires**: known or advertised company or industry needs for labor (person or group)

## Linked properties

-   **attributes** arrays of key-value pairs for basic node
