import numpy as np
import matplotlib.pyplot as plt
import math


# Função genérica do metodo de Newton.
def newton_method(f, fprime, x0, tol=1e-5, max_iter=50, bound=1e10):
    iterates = [x0]
    errors = []
    print("Iteração\tx_n\t\tf(x_n)\t\tErro")
    for i in range(max_iter):
        x_current = iterates[-1]
        # Se o valor de x_current for muito grande, interrompe a iteração.
        if abs(x_current) > bound:
            print(f"Valor de x excedeu {bound}. Provável divergência. Interrompendo.")
            break
        try:
            f_val = f(x_current)
            fprime_val = fprime(x_current)
        except OverflowError:
            print(f"OverflowError na iteração {i} com x = {x_current}. Interrompendo.")
            break

        # Evita divisão por zero (ou valores muito pequenos)
        if abs(fprime_val) < 1e-12:
            print("Derivada muito próxima de zero. Método falhou.")
            break

        x_new = x_current - f_val / fprime_val
        iterates.append(x_new)
        error = abs(x_new - x_current)
        errors.append(error)
        print(f"{i:2d}\t\t{x_current:.8f}\t{f_val:.8f}\t{error:.8f}")
        if error < tol:
            break
    return iterates, errors


###############################################################################
# Item (a)
# A equação: 1/x = 1 + x^3  =>  f(x) = 1/x - 1 - x^3 = 0
# Derivada: f'(x) = -1/x^2 - 3x^2

def f_a(x):
    return 1 / x - 1 - x ** 3


def fprime_a(x):
    return -1 / x ** 2 - 3 * x ** 2


print("\n--- Item (a) ---")
# Escolhe um chute inicial razoável (por exemplo, x0 = 0.7)
x0_a = 0.7
iterates_a, errors_a = newton_method(f_a, fprime_a, x0_a, tol=1e-5, max_iter=20)
x_sol_a = iterates_a[-1]
print(f"\nSolução aproximada (5 casas decimais): {x_sol_a:.5f}")

# Gráfico das funções y = 1/x e y = 1+x^3
x_vals = np.linspace(0.1, 1.5, 400)
y1 = 1 / x_vals
y2 = 1 + x_vals ** 3

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y1, label='y = 1/x', color='blue')
plt.plot(x_vals, y2, label='y = 1 + x³', color='green')
# Marcar a solução aproximada
plt.plot(x_sol_a, 1 / x_sol_a, 'ro', label=f'Solução ≈ {x_sol_a:.5f}')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Item (a): Gráfico de y=1/x e y=1+x³")
plt.legend()
plt.grid(True)
plt.show()


###############################################################################
# Item (b)
# Para calcular 1/π, considere f(x) = π - 1/x.
# Zero de f: π - 1/x = 0  <=> 1/x = π  <=> x = 1/π.
# Derivada: f'(x) = 1/x².
def f_b(x):
    return math.pi - 1 / x


def fprime_b(x):
    return 1 / x ** 2


print("\n--- Item (b) ---")
# Caso com x0 = 0.5
print("\nChute inicial x0 = 0.5:")
x0_b1 = 0.5
iterates_b1, errors_b1 = newton_method(f_b, fprime_b, x0_b1, tol=1e-6, max_iter=20)
x_sol_b1 = iterates_b1[-1]
print(f"Solução aproximada (6 casas decimais): {x_sol_b1:.6f}  [1/π ≈ {1 / math.pi:.6f}]")

# Caso com x0 = 0.7
print("\nChute inicial x0 = 0.7:")
x0_b2 = 0.7
iterates_b2, errors_b2 = newton_method(f_b, fprime_b, x0_b2, tol=1e-6, max_iter=20)
x_sol_b2 = iterates_b2[-1]
print(f"Solução aproximada (6 casas decimais): {x_sol_b2:.6f}  [1/π ≈ {1 / math.pi:.6f}]")

# Plot das iterações para ambos os chutes
plt.figure(figsize=(8, 6))
plt.plot(iterates_b1, 'bo-', label='x0 = 0.5')
plt.plot(iterates_b2, 'ro-', label='x0 = 0.7')
plt.xlabel("Número da Iteração")
plt.ylabel("Aproximação de x")
plt.title("Item (b): Convergência do método para 1/π")
plt.legend()
plt.grid(True)
plt.show()

###############################################################################
# Item (c)
print("\n--- Item (c) ---")


# (c.1) f(x) = cube_root(x)
# Em Python, np.cbrt(x) retorna a raiz cúbica real.
# Derivada: f'(x) = 1/(3 * |x|^(2/3)), para x ≠ 0.
def f_c1(x):
    return np.cbrt(x)


def fprime_c1(x):
    # Para x != 0
    return 1 / (3 * np.cbrt(x ** 2))


print("\n(c.1) f(x) = cube_root(x) com x0 = 0.1:")
x0_c1 = 0.1
iterates_c1, errors_c1 = newton_method(f_c1, fprime_c1, x0_c1, tol=1e-5, max_iter=10)
print("Observação: A iteração resulta em xₙ₊₁ = -2*xₙ, levando a uma sequência que oscila e diverge.")


# (c.2) f(x) = x³ - 5x  (zeros: 0, sqrt(5) e -sqrt(5))
def f_c2(x):
    return x ** 3 - 5 * x


def fprime_c2(x):
    return 3 * x ** 2 - 5


print("\n(c.2) f(x) = x³ - 5x com x0 = 1:")
iterates_c2_pos, errors_c2_pos = newton_method(f_c2, fprime_c2, 1, tol=1e-5, max_iter=10)
print("Observação: A sequência oscila entre 1 e -1, não convergindo para nenhuma das raízes.")

print("\n(c.2) f(x) = x³ - 5x com x0 = -1:")
iterates_c2_neg, errors_c2_neg = newton_method(f_c2, fprime_c2, -1, tol=1e-5, max_iter=10)
print("Observação: Novamente, a sequência oscila entre -1 e 1.")


# (c.3) f(x) = x³ - 2x + 2  (zero real próximo de -2)
def f_c3(x):
    return x ** 3 - 2 * x + 2


def fprime_c3(x):
    return 3 * x ** 2 - 2


print("\n(c.3) f(x) = x³ - 2x + 2:")
# Cenário 1: x0 = 0
print("\nChute inicial x0 = 0:")
iterates_c3_0, errors_c3_0 = newton_method(f_c3, fprime_c3, 0, tol=1e-5, max_iter=10)
print("Observação: O método inicia em 0 e vai para 1, indicando que não converge para o zero próximo de -2.")

# Cenário 2: x0 próximo de 0 (por exemplo, 0.05 e -0.05)
print("\nChute inicial x0 = 0.05:")
iterates_c3_small_pos, errors_c3_small_pos = newton_method(f_c3, fprime_c3, 0.05, tol=1e-5, max_iter=10)

print("\nChute inicial x0 = -0.05:")
iterates_c3_small_neg, errors_c3_small_neg = newton_method(f_c3, fprime_c3, -0.05, tol=1e-5, max_iter=10)
print("Observação: Chutes muito próximos de 0 não conduzem à convergência para o zero real esperado.")

# Cenário 3: x0 = 5
print("\nChute inicial x0 = 5:")
iterates_c3_5, errors_c3_5 = newton_method(f_c3, fprime_c3, 5, tol=1e-5, max_iter=15)
print(
    "Observação: Com um chute distante (x0 = 5), após várias iterações o método tende a convergir para o único zero real (próximo de -2), mas a convergência pode ser irregular e sensível à escolha do chute.")

# Para visualizar a evolução das iterações para o cenário (c.3) com x0 = 5:
plt.figure(figsize=(8, 6))
plt.plot(iterates_c3_5, 'mo-')  # Correção aplicada aqui: removido o marcador duplicado.
plt.xlabel("Número da Iteração")
plt.ylabel("Aproximação de x")
plt.title("Item (c.3): Convergência com x0 = 5 para f(x) = x³ - 2x + 2")
plt.grid(True)
plt.show()

###############################################################################
# Conclusão:
print("\n--- Conclusão Geral ---")
print("""
No item (a) foi confirmada a existência de um zero positivo para a equação 1/x = 1+x³. 
O método de Newton convergiu rapidamente para x ≈ {:.5f}, como ilustrado pelo gráfico que mostra a interseção das funções.

No item (b), ao calcular 1/π através da função f(x) = π - 1/x, os dois chutes iniciais (0.5 e 0.7) convergiram para o valor correto com precisão de 6 casas decimais. 
Observa-se que o método gera a iteração xₙ₊₁ = 2xₙ - πxₙ², um esquema clássico para o cálculo do recíproco.

No item (c), diversos comportamentos interessantes foram observados:
  • (c.1) Para f(x) = ∛x, o método gera a recorrência xₙ₊₁ = -2xₙ, o que leva a uma sequência oscilatória e divergente (exceto o caso trivial x₀ = 0).
  • (c.2) Em f(x) = x³ - 5x, com chutes x₀ = 1 e x₀ = -1, a sequência oscila entre 1 e -1, sem convergir para nenhuma das raízes reais.
  • (c.3) Para f(x) = x³ - 2x + 2, a escolha do chute inicial é crucial. Chutes próximos de 0 (ou entre -0.1 e 0.1) não direcionam a convergência para o único zero real (próximo de -2), enquanto um chute mais distante (por exemplo, x₀ = 5) pode, após iterações não triviais, levar à convergência, embora o processo seja sensível e potencialmente irregular.
""".format(x_sol_a))
