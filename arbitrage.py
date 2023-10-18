class ArbitrageBot:
    def __init__(self, bookmaker1_odds, bookmaker2_odds, stake):
        self.bookmaker1_odds = bookmaker1_odds
        self.bookmaker2_odds = bookmaker2_odds
        self.stake = stake

    def find_arbitrage_opportunity(self):
        # Calculate implied probabilities
        implied_prob1 = 1 / self.bookmaker1_odds
        implied_prob2 = 1 / self.bookmaker2_odds

        # Calculate the total implied probability
        total_implied_prob = implied_prob1 + implied_prob2

        # Calculate the overround (vig or margin)
        overround = 1 / total_implied_prob - 1

        # Check for arbitrage opportunity
        if overround < 0:
            # Calculate the arb stake for each bookmaker
            arb_stake1 = (1 / (self.bookmaker1_odds * total_implied_prob)) * self.stake
            arb_stake2 = (1 / (self.bookmaker2_odds * total_implied_prob)) * self.stake

            # Calculate profit or loss
            profit = arb_stake1 * self.bookmaker1_odds - self.stake
            # Ensure profit is positive to confirm arbitrage opportunity
            if profit > 0:
                print("Arbitrage Opportunity Found:")
                print(f"Bookmaker 1 Stake: {arb_stake1:.2f}, Odds: {self.bookmaker1_odds:.2f}")
                print(f"Bookmaker 2 Stake: {arb_stake2:.2f}, Odds: {self.bookmaker2_odds:.2f}")
                print(f"Profit: {profit:.2f}")
            else:
                print("No Arbitrage Opportunity Found.")
        else:
            print("No Arbitrage Opportunity Found.")

if __name__ == "__main__":
    # Example usage
    bookmaker1_odds = 2.0  # Replace with actual odds from Bookmaker 1
    bookmaker2_odds = 2.5  # Replace with actual odds from Bookmaker 2
    stake = 100  # Replace with your desired stake amount

    bot = ArbitrageBot(bookmaker1_odds, bookmaker2_odds, stake)
    bot.find_arbitrage_opportunity()
