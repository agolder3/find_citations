#!/bin/bash
export DOI=$1 # put your input DOI here (not as a URL, just the DOI itself)
export FILENAME=$2
curl -X GET "https://opencitations.net/index/api/v2/citations/doi:$DOI" | jq --raw-output ".[]|.citing" | doi2bib -i - -o "${FILENAME}-citations.bib"