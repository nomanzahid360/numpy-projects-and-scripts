# Broadcasting without numpy
import numpy as np

prices = [100, 200, 300, 400, 500]

discount = 0.1

discounted_prices = [price * (1 - discount) for price in prices]
print(discounted_prices)

# Broadcasting with Numpy

prices_np = np.array([100, 200, 300, 400, 500])
discount_np = 10
final_prices = prices_np - (prices_np * discount_np / 100)
print(final_prices)