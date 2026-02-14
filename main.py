import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import time

def fibonacci_sequence_verbose(n):
    """
    Gera os primeiros n números da sequência de Fibonacci COM PRINTS.
    """
    print(f"\n{'='*80}")
    print(f"🔢 GERANDO OS PRIMEIROS {n} NÚMEROS DE FIBONACCI")
    print(f"{'='*80}\n")
    
    if n <= 0:
        return np.array([])
    elif n == 1:
        print("F(0) = 0")
        return np.array([0])
    elif n == 2:
        print("F(0) = 0")
        print("F(1) = 1")
        return np.array([0, 1])
    
    fib = np.zeros(n, dtype=np.int64)
    fib[0] = 0
    fib[1] = 1
    
    print("Inicializando sequência:")
    print(f"  F(0) = {fib[0]}")
    print(f"  F(1) = {fib[1]}")
    print()
    
    # Calcula e mostra progresso
    milestones = [5, 10, 15, 20, 25, 30, 35, 40, 45, n-1]
    
    for i in range(2, n):
        fib[i] = fib[i-1] + fib[i-2]
        
        # Mostra alguns passos intermediários
        if i in milestones or i < 10:
            print(f"  F({i}) = F({i-1}) + F({i-2}) = {fib[i-1]:,} + {fib[i-2]:,} = {fib[i]:,}")
        elif i == milestones[0] + 1:
            print("  ...")
    
    print(f"\n✅ Sequência gerada com sucesso! ({n} números)")
    print(f"   Menor: F(0) = {fib[0]:,}")
    print(f"   Maior: F({n-1}) = {fib[-1]:,} ({len(str(fib[-1]))} dígitos)")
    print(f"{'='*80}\n")
    
    return fib

def print_fibonacci_table_verbose(n=50):
    """
    Imprime tabela formatada COM INDICAÇÃO DE PROGRESSO.
    """
    print(f"\n{'='*100}")
    print(f"📊 CONSTRUINDO TABELA DETALHADA")
    print(f"{'='*100}\n")
    
    fib = fibonacci_sequence_verbose(n)
    phi = (1 + np.sqrt(5)) / 2
    
    print("Calculando razões e convergências...\n")
    
    print("="*100)
    print(f"{'TABELA DOS PRIMEIROS ' + str(n) + ' NÚMEROS DE FIBONACCI':^100}")
    print("="*100)
    print(f"{'n':<5} {'F(n)':<25} {'Dígitos':<10} {'F(n)/F(n-1)':<18} {'Diferença de φ':<20}")
    print("-"*100)
    
    for i in range(n):
        fn = fib[i]
        digits = len(str(fn))
        
        if i > 0:
            ratio = fn / fib[i-1] if fib[i-1] != 0 else 0
            phi_diff = abs(ratio - phi)
        else:
            ratio = 0
            phi_diff = 0
        
        ratio_str = f"{ratio:.10f}" if ratio > 0 else "N/A"
        phi_diff_str = f"{phi_diff:.12f}" if phi_diff > 0 else "N/A"
        
        print(f"{i:<5} {fn:<25,} {digits:<10} {ratio_str:<18} {phi_diff_str:<20}")
        
        # Pausa visual em marcos importantes
        if i in [0, 1, 10, 20, 30, 40, n-1]:
            time.sleep(0.01)  # Pequena pausa para visualizar
    
    print("="*100)
    print(f"Razão Áurea (φ) = {phi:.15f}")
    print(f"√5 = {np.sqrt(5):.15f}")
    print("="*100)
    
    return fib, phi

def plot_fibonacci_verbose(n=50):
    """
    Cria visualizações COM PRINTS DE PROGRESSO.
    """
    print(f"\n{'='*80}")
    print(f"📈 GERANDO VISUALIZAÇÕES GRÁFICAS")
    print(f"{'='*80}\n")
    
    fib = fibonacci_sequence(n)  # Versão silenciosa para os gráficos
    indices = np.arange(n)
    phi = (1 + np.sqrt(5)) / 2
    
    print("⏳ Preparando canvas (2x2 subplots)...")
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    def format_large(x, pos):
        if x >= 1e9:
            return f'{x/1e9:.1f}B'
        elif x >= 1e6:
            return f'{x/1e6:.1f}M'
        elif x >= 1e3:
            return f'{x/1e3:.1f}K'
        else:
            return f'{int(x)}'
    
    formatter = FuncFormatter(format_large)
    
    # ============ GRÁFICO 1 ============
    print("\n📊 Gráfico 1/4: Escala Linear")
    print("   → Plotando primeiros 30 termos...")
    
    ax1 = axes[0, 0]
    n_display = 30
    ax1.plot(indices[:n_display], fib[:n_display], 
            linewidth=2.5, color='#2E86AB', marker='o', 
            markersize=5, alpha=0.8)
    
    print("   → Adicionando anotações...")
    highlights = [0, 10, 20, n_display-1]
    for h in highlights:
        if h < n_display:
            ax1.plot(h, fib[h], 'ro', markersize=8, zorder=5)
            ax1.annotate(f'F({h})={fib[h]:,}', 
                        xy=(h, fib[h]), 
                        xytext=(5, 10), 
                        textcoords='offset points',
                        fontsize=9,
                        bbox=dict(boxstyle='round,pad=0.4', 
                                facecolor='yellow', alpha=0.8))
    
    ax1.set_xlabel('Índice (n)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('F(n)', fontsize=12, fontweight='bold')
    ax1.set_title(f'Sequência de Fibonacci - Escala Linear\n(Primeiros {n_display} termos para visualização)', 
                  fontsize=13, fontweight='bold', pad=15)
    ax1.grid(True, alpha=0.3, linestyle='--')
    ax1.yaxis.set_major_formatter(formatter)
    
    ax1.text(0.98, 0.98, f'Nota: F(50)={fib[-1]:,}\n(muito grande para esta escala)',
            transform=ax1.transAxes,
            fontsize=9, 
            verticalalignment='top',
            horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))
    
    print("   ✅ Gráfico 1 concluído!")
    
    # ============ GRÁFICO 2 ============
    print("\n📊 Gráfico 2/4: Escala Logarítmica")
    print(f"   → Plotando todos os {n} termos em escala log...")
    
    ax2 = axes[0, 1]
    
    fib_log = fib[1:]
    indices_log = indices[1:]
    
    ax2.semilogy(indices_log, fib_log, linewidth=2.5, color='#A23B72', 
                marker='s', markersize=4, alpha=0.8, label='F(n)')
    
    print("   → Calculando fórmula de Binet (φⁿ/√5)...")
    reference = phi**indices_log / np.sqrt(5)
    ax2.semilogy(indices_log, reference, '--', linewidth=2, 
                color='red', alpha=0.6, label='φⁿ/√5 (fórmula de Binet)')
    
    ax2.set_xlabel('Índice (n)', fontsize=12, fontweight='bold')
    ax2.set_ylabel('F(n) - Escala Log', fontsize=12, fontweight='bold')
    ax2.set_title('Sequência de Fibonacci - Escala Logarítmica\n(Lineariza o crescimento exponencial)', 
                  fontsize=13, fontweight='bold', pad=15)
    ax2.grid(True, alpha=0.3, linestyle='--', which='both')
    ax2.legend(fontsize=10, loc='upper left')
    
    print("   ✅ Gráfico 2 concluído!")
    
    # ============ GRÁFICO 3 ============
    print("\n📊 Gráfico 3/4: Convergência para φ")
    print("   → Calculando razões F(n)/F(n-1)...")
    
    ax3 = axes[1, 0]
    
    if n > 2:
        ratios = fib[2:] / fib[1:-1]
        ratio_indices = indices[2:]
        
        print(f"   → Primeiras razões: {ratios[:5]}")
        print(f"   → Últimas razões: {ratios[-5:]}")
        print(f"   → Convergindo para φ = {phi:.10f}")
        
        ax3.plot(ratio_indices, ratios, linewidth=2.5, color='#F18F01', 
                marker='o', markersize=4, alpha=0.8, label='F(n)/F(n-1)')
        
        ax3.axhline(y=phi, color='red', linestyle='--', linewidth=2.5, 
                   alpha=0.7, label=f'φ = {phi:.6f}')
        
        ax3.set_xlabel('Índice (n)', fontsize=12, fontweight='bold')
        ax3.set_ylabel('Razão F(n)/F(n-1)', fontsize=12, fontweight='bold')
        ax3.set_title('Convergência para a Razão Áurea (φ)\n(Oscila e estabiliza em φ)', 
                     fontsize=13, fontweight='bold', pad=15)
        ax3.grid(True, alpha=0.3, linestyle='--')
        ax3.legend(fontsize=11, loc='upper right')
        ax3.set_ylim([0.9, 2.1])
    
    print("   ✅ Gráfico 3 concluído!")
    
    # ============ GRÁFICO 4 ============
    print("\n📊 Gráfico 4/4: Crescimento Absoluto")
    print("   → Calculando diferenças F(n) - F(n-1)...")
    
    ax4 = axes[1, 1]
    
    if n > 1:
        growth = np.diff(fib)
        growth_indices = indices[1:]
        
        print(f"   → Primeiro crescimento: F(1) - F(0) = {growth[0]:,}")
        print(f"   → Último crescimento: F(49) - F(48) = {growth[-1]:,}")
        print(f"   → Padrão: F(n) - F(n-1) = F(n-2) ✓")
        
        ax4.bar(growth_indices, growth, color='#6A4C93', alpha=0.75, 
               edgecolor='black', linewidth=0.8)
        
        ax4.set_xlabel('Índice (n)', fontsize=12, fontweight='bold')
        ax4.set_ylabel('Crescimento: F(n) - F(n-1)', fontsize=12, fontweight='bold')
        ax4.set_title('Crescimento Absoluto entre Termos\n(F(n) - F(n-1) = F(n-2))', 
                     fontsize=13, fontweight='bold', pad=15)
        ax4.grid(True, alpha=0.3, linestyle='--', axis='y')
        ax4.yaxis.set_major_formatter(formatter)
        
        ax4.text(0.98, 0.98, 'Padrão: Crescimento\nsegue Fibonacci!',
                transform=ax4.transAxes,
                fontsize=10, 
                verticalalignment='top',
                horizontalalignment='right',
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
    
    print("   ✅ Gráfico 4 concluído!")
    
    plt.suptitle(f'Análise dos Primeiros {n} Números de Fibonacci', 
                fontsize=16, fontweight='bold', y=0.998)
    plt.tight_layout()
    
    print(f"\n{'='*80}")
    print("🎨 Renderizando visualização...")
    print(f"{'='*80}\n")
    
    plt.show()

def fibonacci_sequence(n):
    """Versão silenciosa para uso nos gráficos."""
    if n <= 0:
        return np.array([])
    elif n == 1:
        return np.array([0])
    elif n == 2:
        return np.array([0, 1])
    
    fib = np.zeros(n, dtype=np.int64)
    fib[0] = 0
    fib[1] = 1
    
    for i in range(2, n):
        fib[i] = fib[i-1] + fib[i-2]
    
    return fib

# ==================== EXECUÇÃO ====================

print("\n" + "🌀"*40)
print("ANÁLISE COMPLETA DA SEQUÊNCIA DE FIBONACCI")
print("🌀"*40 + "\n")

N = 50

print(f"Parâmetros:")
print(f"  • Quantidade de números: {N}")
print(f"  • Modo verbose: ATIVADO")
print()

input("Pressione ENTER para começar...")

# PARTE 1: TABELA NUMÉRICA
print("\n" + "📋"*40)
print("PARTE 1: GERANDO TABELA NUMÉRICA")
print("📋"*40)

fib, phi = print_fibonacci_table_verbose(N)

# PARTE 2: GRÁFICOS VISUAIS
print("\n" + "📊"*40)
print("PARTE 2: GERANDO VISUALIZAÇÕES GRÁFICAS")
print("📊"*40)

plot_fibonacci_verbose(N)

# RESUMO FINAL
print("\n" + "="*80)
print("✅ ANÁLISE COMPLETA CONCLUÍDA!")
print("="*80)
print(f"\n📊 RESUMO DOS RESULTADOS:")
print(f"   • Total de números calculados: {N}")
print(f"   • Menor número: F(0) = {fib[0]:,}")
print(f"   • Maior número: F({N-1}) = {fib[-1]:,}")
print(f"   • Dígitos do maior: {len(str(fib[-1]))}")
print(f"   • Razão áurea (φ): {phi:.15f}")
print(f"   • Convergência: F({N-1})/F({N-2}) = {fib[-1]/fib[-2]:.15f}")
print(f"   • Diferença de φ: {abs(fib[-1]/fib[-2] - phi):.2e}")
print()
print("📈 GRÁFICOS GERADOS:")
print("   1. Escala Linear (primeiros 30 termos)")
print("   2. Escala Logarítmica (todos os 50 termos)")
print("   3. Convergência para φ")
print("   4. Padrão de crescimento")
print("="*80 + "\n")
