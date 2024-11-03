# Anthropic OpenAPI spec

Repository created while waiting for the official OpenAPI spec from the Anthropic.

## F.A.Q.

## How was this created?

The spec is semi-automatically created by pointing Perplexity to each page on https://docs.anthropic.com/en/api/ and asking to generate the spec. Then, all were stitched manually together and eye-balled verified.

## Why not write an automatic script to generate all of this?

That's an option considered. To list all pages necessary, and use Antrhopic's officially supported SDK to generate OpenAPI spec for each, then 'just' merge them. This took me less than 10 min and if there's a needed update, we'll add the better option.

## Are there any other resources?

Yes, here are other:

* https://github.com/davidmigloz/langchain_dart/blob/main/packages/anthropic_sdk_dart/oas/anthropic_openapi_curated.yaml
