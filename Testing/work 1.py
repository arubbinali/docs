import random

# ANSI colors
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

# Initial settings
starting_cash = 10_000_000_000
ticket_cost = 10_000
your_investment = 50_000_000
your_tickets = your_investment // ticket_cost
rounds = 1000

# Column headers
headers = [
    "Round",
    "Your Investment",
    "Total Lottery Cash",
    "After-Tax Pool",
    "Win Probability",
    "Did You Win",
    "Net Profit/Loss",
    "Your Remaining Cash"
]

# Print header with spacing
print(f"{headers[0]:<8} {headers[1]:<20} {headers[2]:<22} {headers[3]:<20} "
      f"{headers[4]:<18} {headers[5]:<13} {headers[6]:<20} {headers[7]}")

cash = starting_cash

for i in range(1, rounds + 1):
    total_cash = random.uniform(800_000_000, 5_000_000_000)
    prize_pool = total_cash * 0.75
    total_tickets = total_cash / ticket_cost
    prob_win = your_tickets / total_tickets

    win = random.random() < prob_win
    winnings = prize_pool if win else 0
    net_gain = winnings - your_investment
    cash += net_gain

    # Format winnings with color
    if net_gain > 0:
        winnings_display = f"{GREEN}+{net_gain:,.0f}{RESET}"
    else:
        winnings_display = f"{RED}{net_gain:,.0f}{RESET}"

    # Format remaining cash with color
    if cash > starting_cash:
        cash_display = f"{GREEN}{cash:,.0f}{RESET}"
    else:
        cash_display = f"{RED}{cash:,.0f}{RESET}"

    # Print row with proper spacing and format
    print(f"{i:<8}"
          f"{your_investment:<20,.0f}"
          f"{total_cash:<22,.0f}"
          f"{prize_pool:<20,.0f}"
          f"{prob_win*100:<17.4f}% "
          f"{'YES' if win else 'NO':<13}"
          f"{winnings_display:<20}"
          f"{cash_display}")
