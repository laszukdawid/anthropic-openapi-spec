# Anthropic OpenAPI spec

Repository created while waiting for the official OpenAPI spec from the Anthropic.

## Versions

There are a few versions of the specifications.

### `hosted_spec.json`

(Recommended) Specification taken from Antrhopic's official TypeScript SDK - https://github.com/anthropics/anthropic-sdk-typescript/blob/main/.stats.yml. Unfortunately, it isn't "officially" exposed, nor easy to find, so this repo aims to help point at it.

Actually, this file is slightly modified. How exactly, check the `fix_spec.py`. The modification is adding missing "X-API-Key" param to header which is required according to Anthropic's doc but it's missing in the file.

### `hosted_spec_v3.0.0.json`

In case you can't use OpenApi spec in version 3.1.0, then this is your next step. The spec is created via `downgrade_spec.py`. Specifically, all `"type": "null"` were removed (in favour of `"nullable": true`) and prop `const` from enums was removed.

### `stiched_spec.yaml` 

The spec is semi-automatically created by pointing Perplexity to each page on https://docs.anthropic.com/en/api/ and asking to generate the spec. Then, all were stitched together and eye-balled verified.

## F.A.Q.

## Are there any other resources?

Yes, here are other:

* https://github.com/davidmigloz/langchain_dart/blob/main/packages/anthropic_sdk_dart/oas/anthropic_openapi_curated.yaml
