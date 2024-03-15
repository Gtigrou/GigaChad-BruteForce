"""
La puissance de calcul de l'algodurant les tests était d'environ 250 433.21 combinaisons par seconde.
Gardez à l'esprit que ce chiffre peut varier en fonction de la machine utilisée.

1sec =>               250 433,21 combinaisons
1min =>            15 025 992,6 combinaisons
1heure =>         901 559 956 combinaisons
1jour =>       21 640 588 576 combinaisons

mdp 3 =>              778 688 combinaisons
mdp 4 =>          715 588 096 combinaisons
mdp 5 =>       62 523 949 144 combinaisons
mdp 6 =>5 748 647 907 983 680 combinaisons

!!! LA PUISSANCE DEPENDRA DE LA MACHINE UTILISER !!!
"""
import itertools
import timeit
import datetime
import matplotlib.pyplot as plt

num = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:\'",<.>/?'
password = input("Mot de passe à tester => ")
mode = input("Seulement des chiffres ? O/N => ").lower()
max_char = int(input("Nombre maximum de caractères ? 1-16 => "))
try_count = 0

if mode == "o":
    num = '0123456789'

def generate_combinations(length):
    return itertools.product(num, repeat=length)

def format_time(seconds):
    delta = datetime.timedelta(seconds=seconds)
    return str(delta)

def check_password():
    global try_count
    for length in range(1, max_char + 1):
        combinations = generate_combinations(length)
        for combo in combinations:
            brut_try = "".join(combo)
            try_count += 1
            if brut_try == password:
                return True
    return False

# Stocker le temps écoulé et le taux de test pour chaque itération
elapsed_times = []
test_rates = []

start_time = timeit.default_timer()
if check_password():
    end_time = timeit.default_timer()
    timer = round(end_time - start_time, 6)

    # Calculer le taux de test pour chaque seconde
    for second in range(int(timer)):
        elapsed_time = datetime.timedelta(seconds=second + 1).total_seconds()
        test_rate = try_count / elapsed_time
        elapsed_times.append(elapsed_time)
        test_rates.append(test_rate)

    # Afficher d'autres résultats
    formatted_time = format_time(timer)
    print("Temps écoulé => {}".format(formatted_time))
    print("Mot de passe trouvé en {} tentatives.".format(try_count))
    print("Mot de passe trouvé : {}".format(password))
    # Tracer le graphique
    plt.plot(elapsed_times, test_rates)
    plt.xlabel('Temps écoulé (secondes)')
    plt.ylabel('Taux de test (combinaisons par seconde)')
    plt.title('temps écoulé({})'.format(formatted_time)+' taux de test ({})'.format(try_count))

    plt.show()
else:
    end_time = timeit.default_timer()
    timer = round(end_time - start_time, 6)
    formatted_time = format_time(timer)
    print("Temps écoulé => {}".format(formatted_time))
    print("Mot de passe non trouvé en {} tentatives.".format(try_count))
