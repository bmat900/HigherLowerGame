import art
import random
import data


def print_data(dic1, dic2):
    """Ordena e imprime a informação da pessoa"""
    print(f"Compare A: {dic1['name']}, a {dic1['description']}, from {dic1['country']}.")
    print(art.vs)
    print(f"Compare B: {dic2['name']}, a {dic2['description']}, from {dic2['country']}.")


def get_followers(dic1):
    """Obtem o valor da quantidade dos followers e armazena em um Integer"""
    return dic1['follower_count']


def compare():
    global score
    A = data.data[random.randint(0, len(data.data))]
    B = data.data[random.randint(0, len(data.data))]
    print_data(A, B)
    choose = input("Who has more followers? Type 'A' or 'B': ")
    if choose == 'A':
        if get_followers(A) > get_followers(B):
            score += 1
            print(f'You are right! Current score: {score}')
            return True
        else:
            return False
    if choose == 'B':
        if get_followers(A) < get_followers(B):
            score += 1
            print(f'You are right! Current score: {score}')
            return True
        else:
            return False


score = 0
print(art.logo)

while compare():
    compare()
print(f"Sorry, that's wrong. Final Score: {score}")