# CUBE Gateway & EPA Guidance Hub — GitHub Pages edition v0.5.2

This is a **self-contained static GitHub Pages adaptation** of the Floot v0.5.2 **public guidance experience**. It includes all seven audited baseline standards, their detailed Gateway and EPA requirements, CIOB/RICS dates guidance, the approved dual-audience visual design, **three ST0331 occupational pathways** with optional RICS APC reference material, FAQs, a preparation tracker, a printable one-page summary and a comparison matrix.

**Important:** This is not a byte-for-byte export of Floot's React application. The public user experience has been reimplemented in a dependency-free static site for GitHub Pages. Floot's private authentication, request approvals and staff source-review database are **not available** on GitHub Pages and are deliberately not included. Retain Floot or an authorised Microsoft 365 solution for those workflows.

## Deploy on GitHub Pages

1. Create an empty GitHub repository, e.g. `cube-gateway-epa`.
2. Upload **all** contents of this package to the root of the repository (including `.github/workflows/deploy-pages.yml` and the `site` folder). Commit to `main`.
3. In **Settings → Pages → Build and deployment**, select **GitHub Actions** as the source.
4. Open the **Actions** tab and verify that `Deploy CUBE Gateway & EPA Hub to GitHub Pages` succeeds.
5. Open the site URL reported by the deployment. It will usually resemble `https://YOUR-ACCOUNT.github.io/cube-gateway-epa/`.
6. For Teams/SharePoint embedding, use the published site URL and verify iframe policy and institutional approval. The query `?embed=1` is preserved for future embed-specific enhancements, but the layout is already responsive.

There is **no npm build** and no backend. All resource paths are relative, so repository-subpath hosting works without rewriting routes. Deep links use search parameters and the browser history API rather than server-only `/summary/*` paths.

## Local test

From this package's root:

```bash
python -m http.server 8000 --directory site
```

Open `http://localhost:8000`. Do not open `site/index.html` directly via `file://` because browsers generally block loading `data/guidance.json` in that context.

## What the GitHub site includes

- Audience landing: Apprentices; Staff & Workplace Learning Advisors.
- Staff (Coventry blue) and apprentice (burnt orange) interfaces using a shared content dataset.
- Seven standards and correct EPAO mapping: RICS for ST0331; CIOB for the remaining six.
- ST0331 three primary apprenticeship pathways: Quantity Surveying & Project Management (default), Building Surveying, Property.
- Optional reference panel for four previously developed RICS APC routes, including Project Management, independently selected from the apprenticeship pathway.
- Detailed Gateway requirements, assessment method specifications, indicative timelines, date windows, outcomes and reassessment information, source library.
- Optional browser-local preparation tracker and CSV export, without learner identity.
- 2027 RICS session selection and calendar `.ics` export.
- Searchable FAQ and detailed guidance entries, including staff practice prompts.
- One-page-style summary and seven-standard comparison, with browser Print / Save as PDF controls. Print pagination depends on browser settings, font metrics and print scale.

## Public/secure boundary

GitHub Pages is a public static host, **not** a protected institutional application merely because a SharePoint page embeds it. No confidential staff register, student records, login credentials, PINs or backend URLs have been packaged. The `Source review` section explains the unavailable authenticated function and redirects users toward the separately managed institutionally approved service. **Do not place personal data, restricted evidence or private administrative records into the `site/` directory.**

`site/data/guidance.json` is publicly downloadable. It has been created from `Gateway_EPA_Floot_Content_v0.4.2.json` with private audit/issue-register metadata removed. The source material remains labelled institutional approval pending.

## Update governance

When official apprenticeship standards, RICS/CIOB advice or dates change, update `site/data/guidance.json` only after the clause-level review and appropriate course approval. Changing code or guidance in Floot **does not automatically update** this GitHub edition. Changes must be deliberately reconciled and deployed.

**Current baseline date:** 15 November 2026. **Packaging date:** 23 November 2026. 2027 RICS dates require live verification before publication.

## Pre-publication checklist

- [ ] Official seven-standard assessment-plan version applicability reviewed and approved.
- [ ] 2027 RICS dates and link endpoints rechecked.
- [ ] Validate print layouts for all seven standards on institution-managed browsers.
- [ ] Test desktop, mobile and SharePoint/Teams iframe embedding.
- [ ] Confirm institutional copyright/brand use, public distribution, accessibility (WCAG 2.2 AA) and approval notices.
- [ ] Check ordinary users can access guidance without needing Floot sign-in.

Official GitHub Pages instructions: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
