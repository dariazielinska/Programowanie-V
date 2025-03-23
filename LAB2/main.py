import matplotlib.pyplot as plt
import numpy as np

poczatkowa_populacja = 100
lata = 50
r_best = 0.0194
r_average = -0.0324
r_worst = -0.0382

def model_populacji(zuraw, r, years, year=0, history=None):
    if history is None:
        history = [zuraw]
    
    if year >= years:
        return history
    
    next_population = zuraw + r * zuraw
    history.append(next_population)

    return model_populacji(next_population, r, years, year + 1, history)

history_best = model_populacji(poczatkowa_populacja, r_best, lata)
history_average = model_populacji(poczatkowa_populacja, r_average, lata)
history_worst = model_populacji(poczatkowa_populacja, r_worst, lata)

years_range = np.arange(0, lata + 1)

plt.figure(figsize=(10, 6))
plt.plot(years_range, history_best, label="Best Case (r = 0.0194)", color='g')
plt.plot(years_range, history_average, label="Average Case (r = -0.0324)", color='b')
plt.plot(years_range, history_worst, label="Worst Case (r = -0.0382)", color='r')

plt.title('Model Populacji Żurawia')
plt.xlabel('Rok')
plt.ylabel('Populacja')
plt.legend()
plt.grid(True)

plt.savefig("populacja_zurawia.png")
