---
id: "DLV-26"
type: "requirement"
group: "DLV"
verification: "none"
---
# DLV-26

BEACON shall link a chat account to a Reader only when that chat account starts the bot through a link that BEACON issued to that Reader, that no chat account has used before and that has not expired.

**Rationale.** The link is issued only to the signed-in Reader, so no one can link a chat account by typing an identifier, mistyped or not. The link works once and only for a short time, so a copy that is forwarded, leaked or found later cannot link another chat account; a Reader who hands over an unused link while it is valid still gives that chat account their Deliveries.

**Verification.** none yet
