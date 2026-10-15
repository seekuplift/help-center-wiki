# Buy and sell

--8<-- "includes/test-banner.md"

Open any token and use **Buy** or **Sell** under the header. Not a
recommendation to trade.

## Pay in SKR

On-curve buys pay in **SKR**, not SOL. The Buy balance line is your SKR;
**Max** uses the full SKR balance (buy) or full token holding (sell).
With only SOL, the sheet offers **Get SKR & Buy**: approve the SOL → SKR
swap, then the buy, separately. On fee-bearing tokens **Est. receive** is
already net of the transfer fee — what you see is what lands.

On-curve trades route via **Meteora DBC**; graduated tokens via
**Jupiter**. If a coin graduates while the sheet is open, it switches to
Jupiter and asks you to review the new price. More: [Graduation](graduation.md).

Every trade also pays a small SOL gas fee plus the trading fee in
[Fees](fees.md).

## When a trade is unavailable

Some coins can't be bought or sold where you are (see
[Privacy and safety](privacy.md)):
the buttons stay visible but disabled, with the reason underneath (for
cause-backed coins only **Buy** is disabled — holders can still sell). A
**Not available** panel means the market is switched off for now (for
example stock-quoted or transfer-fee coins) — **Sell still works** if you
hold. Right after graduation, **No route found** just means Jupiter hasn't
listed it yet — wait a moment, then close and reopen the sheet.

## Review before you sign

Confirm mint, side, and amount in the wallet prompt. **Cancel = no funds
move.** Invalid amounts are refused before any prompt. Sell is red on
purpose.

After a trade, give indexing a moment if a number looks stale. Charts
move on executed trades; headline prices are **display-grade**, never an
input to fees or payouts.

**Report** on the token page files a policy, trademark, or DMCA report
(wallet-attributed — no private data in the comment).
