"""
Lottery Simulator Web App (single-file Flask app)

How to run:
1. Install Flask if you don't have it:
   pip install flask
2. Run this file:
   python lottery_sim_webapp.py
3. Open your browser at http://127.0.0.1:5000

Everything (HTML + CSS) is embedded in this single Python file, so no other language files are needed.
"""
from flask import Flask, request, render_template_string
import random
import math

app = Flask(__name__)

TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Lottery Simulator</title>
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
    <h1>Lottery Simulator (Local)</h1>
    <p class="small">Single-file Python Flask app — all HTML/CSS in this file. No external JS/HTML files required.</p>

    <form method="post" class="row">
      <label>Starting Cash:
        <input type="number" name="starting_cash" value="{{starting_cash}}" step="1" required>
      </label>

      <label>Your Investment per Round:
        <input type="number" name="your_investment" value="{{your_investment}}" step="1" required>
      </label>

      <label>Rounds:
        <input type="number" name="rounds" value="{{rounds}}" min="1" required>
      </label>

      <label>Min Total Pot:
        <input type="number" name="min_pot" value="{{min_pot}}" step="1" required>
      </label>

      <label>Max Total Pot:
        <input type="number" name="max_pot" value="{{max_pot}}" step="1" required>
      </label>

      <div class="controls">
        <button type="submit">Run Simulation</button>
      </div>
    </form>

    {% if rows %}
      <div class="summary">
        <strong>Summary:</strong>
        &nbsp;Rounds run: {{ rounds }} &nbsp;•&nbsp; Rounds won: {{ wins }} &nbsp;•&nbsp; Final balance: <span class="{{ 'green' if final_cash>starting_cash else 'red' }}">{{ final_cash | int | comma }}</span>
        &nbsp;•&nbsp; Net P/L: <span class="{{ 'green' if final_cash-starting_cash>0 else 'red' }}">{{ (final_cash-starting_cash) | int | comma_signed }}</span>
      </div>

      <table>
        <thead>
          <tr>
            <th>Round</th>
            <th>Your Investment</th>
            <th>Total Lottery Cash</th>
            <th>After-Tax Pool (75%)</th>
            <th>Win Probability</th>
            <th>Did You Win</th>
            <th>Net Profit/Loss</th>
            <th>Your Remaining Cash</th>
          </tr>
        </thead>
        <tbody>
          {% for r in rows %}
            <tr>
              <td style="text-align:left">{{ r.round }}</td>
              <td class="mono">{{ r.your_investment | comma }}</td>
              <td class="mono">{{ r.total_cash | comma }}</td>
              <td class="mono">{{ r.prize_pool | comma }}</td>
              <td>{{ "{:.4f}%".format(r.prob*100) }}</td>
              <td>{{ 'YES' if r.win else 'NO' }}</td>
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

# helpers for Jinja filters
from markupsafe import Markup

def comma(x):
    try:
        return f"{int(x):,}"
    except Exception:
        return x


def comma_signed(x):
    try:
        v = int(x)
        sign = '+' if v>0 else ''
        return f"{sign}{v:,}"
    except Exception:
        return x

app.jinja_env.filters['comma'] = comma
app.jinja_env.filters['comma_signed'] = comma_signed

# Simulation function

def run_simulation(starting_cash=10_000_000_000,
                   your_investment=100_000_000,
                   ticket_cost=10_000,
                   rounds=1000,
                   min_pot=800_000_000,
                   max_pot=5_000_000_000):
    cash = starting_cash
    your_tickets = your_investment // ticket_cost
    rows = []
    wins = 0

    for i in range(1, rounds+1):
        total_cash = random.uniform(min_pot, max_pot)
        prize_pool = total_cash * 0.75
        total_tickets = total_cash / ticket_cost
        prob = your_tickets / total_tickets if total_tickets>0 else 0

        win = random.random() < prob
        winnings = prize_pool if win else 0
        net_gain = int(round(winnings - your_investment))
        cash += net_gain

        if win:
            wins += 1

        rows.append({
            'round': i,
            'your_investment': int(your_investment),
            'total_cash': int(round(total_cash)),
            'prize_pool': int(round(prize_pool)),
            'prob': prob,
            'win': win,
            'net_gain': net_gain,
            'remaining_cash': int(cash)
        })

    return rows, cash, wins

@app.route('/', methods=['GET', 'POST'])
def index():
    # defaults
    starting_cash = int(request.form.get('starting_cash', 10_000_000_000))
    your_investment = int(request.form.get('your_investment', 100_000_000))
    ticket_cost = int(request.form.get('ticket_cost', 10_000))
    rounds = int(request.form.get('rounds', 1000))
    min_pot = int(request.form.get('min_pot', 800_000_000))
    max_pot = int(request.form.get('max_pot', 5_000_000_000))

    rows = None
    final_cash = None
    wins = 0

    if request.method == 'POST':
        rows, final_cash, wins = run_simulation(
            starting_cash=starting_cash,
            your_investment=your_investment,
            ticket_cost=ticket_cost,
            rounds=rounds,
            min_pot=min_pot,
            max_pot=max_pot
        )

    return render_template_string(TEMPLATE,
                                  rows=rows,
                                  starting_cash=starting_cash,
                                  your_investment=your_investment,
                                  ticket_cost=ticket_cost,
                                  rounds=rounds,
                                  min_pot=min_pot,
                                  max_pot=max_pot,
                                  final_cash=final_cash or starting_cash,
                                  wins=wins)

if __name__ == '__main__':
    app.run(debug=True)