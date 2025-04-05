def calcular_puntaje(actions):
    """Calcula el puntaje de un jugador basado en sus acciones."""
    # Cada kill suma 3 puntos, cada asistencia suma 1 punto, y cada muerte resta 1 punto.
    score=actions["kills"]*3+actions["assists"]
    if actions["deaths"]:
        score-=1
    return score

def determinar_mvp(round):
    """Devuelve el jugador con el puntaje más alto en la ronda."""
    max_puntaje = -1
    mvp_jugador = ""
    for player, actions in round.items():
        puntaje=calcular_puntaje(actions)
        if puntaje > max_puntaje:
            max_puntaje = puntaje
            mvp_jugador = player
    return mvp_jugador

def actualizar_estadisticas(round, ranking, mvp):
    """Actualiza las estadísticas de los jugadores."""
    for player, actions in round.items():
        if player not in ranking:
            ranking[player] = {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'score': 0}
        ranking[player]['kills'] += actions['kills']
        ranking[player]['assists'] += actions['assists']
        ranking[player]['deaths'] += actions['deaths']
        if player == mvp:
            ranking[player]['mvps'] += 1
        ranking[player]['score'] += calcular_puntaje(actions)
    return ranking

def imprimir_ranking(ranking):
    """Impimie el ranking de los jugadores según su puntaje en forma de tabla"""
    # Ordena el ranking por puntaje de mayor a menor
    ranking = dict(sorted(ranking.items(), key=lambda item: item[1]['score'], reverse=True))
    # Imprime el encabezado de la tabla
    print(f"{'Jugador':<10} {'Kills':<6} {'Asistencias':<12} {'Muertes':<6} {'MVPs':<4} {'Puntos':<7}")
    print("-" * 60)
    # Imprime cada jugador y sus estadísticas
    for player, stats in ranking.items():
        print(f"{player:<10} {stats['kills']:<6} {stats['assists']:<12} {stats['deaths']:<6} {stats['mvps']:<4} {stats['score']:<7}")

def simulacion_de_partidas(rounds):
    """Simula las partidas y devuelve el ranking final."""
    ranking = {}
    for i, round in enumerate(rounds, start=1):
        mvp = determinar_mvp(round)
        actualizar_estadisticas(round, ranking, mvp)
        print(f"Ranking ronda {i}:")
        imprimir_ranking(ranking)
        print("\n")
    return ranking