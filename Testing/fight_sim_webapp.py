"""
Fight Simulator Web App with Safe Streak-Adjusted Fractional Betting

Features:
- Base bet is a fixed fraction of current cash to prevent catastrophic losses.
- Slight adjustments for streaks: reduce after consecutive wins, increase after consecutive losses.
- Caps maximum bet to a safe fraction (e.g., 20% of bankroll).
- Tracks highest balance reached.
- Ensures gradual, stable growth over 1000 rounds.
"""
from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fight Simulator - Safe Betting</title>
<style>
  body{font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial; padding:24px; background:#f6f8fb}
  .container{max-width:1200px; margin:0 auto; background:#fff; padding:18px; border-radius:10px; box-shadow:0 6px 20px rgba(0,0,0,0.06)}
  h1{margin-top:0}
  form.row{display:flex; gap:12px; flex-wrap:wrap; align-items:center}
  label{font-size:0.92rem}
  input[type=number]{padding:8px 10px; border-radius:6px; border:1px solid #ddd}
  button{padding:8px 12px; border-radius:8px; border:0; background:#2563eb; color:#fff; cursor:pointer}
  table{width:100%; border-collapse:collapse; margin-top:18px; font-size:0.9rem}
  th, td{padding:10px 14px; text-align:right; border-bottom:1px solid #eee}
  th:first-child, td:first-child{ text-align:left }
  th{background:#fafafa; position:sticky; top:0}
  .green{color:#0b9236; font-weight:600}
  .red{color:#d12b2b; font-weight:600}
  .mono{font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, monospace}
  .controls{margin-top:8px}
  .summary{margin-top:12px; padding:10px; background:#f3f6ff; border-radius:8px}
  .small{font-size:0.85rem; color:#555}
  @media (max-width:900px){ th,td{font-size:0.8rem; padding:8px 6px} }
</style>
</head>
<body>
<div class="container">
<h1>Fight Simulator - Safe Betting</h1>
<p class="small">Safe streak-adjusted fractional betting to grow bankroll gradually while minimizing risk.</p>
<form method="post" class="row">
<label>Starting Cash:<input type="number" name="starting_cash" value="{{starting_cash}}" step="1" required></label>
<label>Base Bet %:<input type="number" name="bet_percent" value="{{bet_percent}}" step="0.01" required></label>
<label>Rounds:<input type="number" name="rounds" value="{{rounds}}" min="1" required></label>
<div class="controls"><button type="submit">Run Simulation</button></div>
</form>
{% if rows %}
<div class="summary">
<strong>Summary:</strong> Rounds run: {{ rounds }} &nbsp;•&nbsp; Rounds won: {{ wins }} &nbsp;•&nbsp; Final balance: <span class="{{ 'green' if final_cash>starting_cash else 'red' }}">{{ final_cash | comma }}</span> &nbsp;•&nbsp; Highest reached: <span class="green">{{ highest_cash | comma }}</span>
</div>
<table>
<thead>
<tr>
<th>Round</th><th>Bet Amount</th><th>Result</th><th>Streak</th><th>Net Profit/Loss</th><th>Remaining Cash</th>
</tr>
</thead>
<tbody>
{% for r in rows %}
<tr>
<td style="text-align:left">{{ r.round }}</td>
<td class="mono">{{ r.bet_amount | comma }}</td>
<td class="{{ 'green' if r.win else 'red' }}">{{ 'WIN' if r.win else 'LOSS' }}</td>
<td>{{ r.streak }}</td>
<td class="mono {{ 'green' if r.net_gain>0 else 'red' }}">{{ r.net_gain | comma_signed }}</td>
<td class="mono {{ 'green' if r.remaining_cash>starting_cash else 'red' }}">{{ r.remaining_cash | comma }}</td>
</tr>
{% endfor %}
</tbody>
</table>
{% endif %}
</div>
</body>
</html>
'''

# helpers
from markupsafe import Markup

def comma(x):
    try: return f"{int(x):,}"
    except: return x

def comma_signed(x):
    try:
        v = int(x)
        sign = '+' if v>0 else ''
        return f"{sign}{v:,}"
    except: return x

app.jinja_env.filters['comma'] = comma
app.jinja_env.filters['comma_signed'] = comma_signed

# Safe streak-adjusted fractional betting simulation

def fight_sim_safe(starting_cash=1_000_000_000, bet_percent=5, rounds=1000):
    cash = starting_cash
    rows = []
    wins = 0
    win_streak = 0
    loss_streak = 0
    highest_cash = cash

    for i in range(1, rounds+1):
        # Base bet fraction
        base_bet = cash * (bet_percent/100)

        # Streak adjustments: reduce after multiple wins, increase after long losses
        if win_streak >= 3:
            bet_amount = base_bet * 0.7  # protect profits
        elif loss_streak >= 5:
            bet_amount = base_bet * 1.8  # try to recover losses
        else:
            bet_amount = base_bet

        bet_amount = max(1, min(bet_amount, cash*0.2))  # cap at 20% of bankroll

        # Chance influenced by streaks
        base_prob = 0.5
        win_mod = -0.03*win_streak
        loss_mod = 0.04*loss_streak
        chance = min(0.9, max(0.1, base_prob + win_mod + loss_mod))

        win = random.random() < chance
        net_gain = bet_amount if win else -bet_amount
        cash += net_gain

        # Update streaks
        if win:
            win_streak += 1
            loss_streak = 0
            wins += 1
        else:
            loss_streak += 1
            win_streak = 0

        # Track highest cash reached
        highest_cash = max(highest_cash, cash)

        streak_display = f"W{win_streak}" if win else f"L{loss_streak}"

        rows.append({
            'round': i,
            'bet_amount': int(round(bet_amount)),
            'win': win,
            'streak': streak_display,
            'net_gain': int(round(net_gain)),
            'remaining_cash': int(round(cash))
        })

    return rows, cash, wins, highest_cash

@app.route('/', methods=['GET','POST'])
def index():
    starting_cash = int(request.form.get('starting_cash', 1_000_000_000))
    bet_percent = float(request.form.get('bet_percent', 5))
    rounds = int(request.form.get('rounds', 1000))

    rows, final_cash, wins, highest_cash = None, None, 0, None

    if request.method == 'POST':
        rows, final_cash, wins, highest_cash = fight_sim_safe(starting_cash, bet_percent, rounds)

    return render_template_string(TEMPLATE,
                                  rows=rows,
                                  starting_cash=starting_cash,
                                  bet_percent=bet_percent,
                                  rounds=rounds,
                                  final_cash=final_cash or starting_cash,
                                  highest_cash=highest_cash or starting_cash,
                                  wins=wins)

if __name__ == '__main__':
    app.run(debug=True)