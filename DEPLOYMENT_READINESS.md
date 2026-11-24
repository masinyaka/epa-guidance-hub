# Deployment readiness — CUBE Gateway & EPA v0.5.2 GitHub static edition

**Built:** 23 November 2026

## What was verified

- JavaScript syntax (Node 22): clean.
- JSON data: seven standards, 2027 RICS calendar sessions, CIOB/RICS EPAO allocation.
- Headless Chromium interaction checks: nine successful task journeys in the browser-mocked sandbox.
- Screenshots generated at 1440px and 393px screen widths.
- GitHub Pages workflow uses `site/` artifact, `actions/configure-pages`, `actions/upload-pages-artifact`, and `actions/deploy-pages`.
- Internal links use query parameters to work below repository prefixes; static redirect pages preserve earlier `/compare` and `/summary/{standard}` routes.

## Environment limitations

The available container does not permit Chromium to navigate to localhost or file:// addresses. Browser tests were therefore performed by injecting the actual production CSS/JS plus JSON into an in-memory Chromium page, with mocked history and storage. Deployment on actual GitHub Pages was **not tested**. This is not an assertion that all browsers, accessibility tools or embedded SharePoint environments have passed.

## Differences from Floot

The GitHub version is a separate, dependency-free front-end adaptation of v0.5.2; it is not an export of Floot's entire React component tree. The protected Microsoft sign-in, access request database, review approvals, and confidential audit records are deliberately excluded because GitHub Pages is a static public host. See RELEASE_SCOPE.md.

## Remaining acceptance tests

1. Deploy to a test GitHub Pages repository and verify resource loading and GitHub Actions status.
2. Exercise all summary pages and comparison print in Edge and Chrome, using paper and Save as PDF.
3. Confirm Teams/SharePoint iframe behaviour and cross-origin clipboard limitations.
4. Run WCAG 2.2 AA review (contrast, focus, keyboard use, labels, zoom and screen reader).
5. Obtain formal approval for source-reviewed, version-dependent EPA and Gateway guidance and RICS dates.

The latest Floot application remains unchanged. Do not imply that a GitHub deploy is an authorised institutional production release.
