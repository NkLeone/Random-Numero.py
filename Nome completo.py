fun main() { # type: ignore

    val nomes = listOf("João", "Maria", "Pedro") # type: ignore
    val sobrenomes = listOf("Silva", "Santos", "Oliveira") # type: ignore

    val nome = nomes.random() # type: ignore
    val sobrenome = sobrenomes.random() # type: ignore

    val nomeCompleto = "$nome $sobrenome" # type: ignore

    println("Nome completo: $nomeCompleto") # type: ignore
} # type: ignore