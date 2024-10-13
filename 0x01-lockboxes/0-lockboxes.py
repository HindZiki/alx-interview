def canUnlockAll(boxes):
    n = len(boxes)  # Nombre total de boîtes
    opened = [False] * n  # Suivi des boîtes ouvertes
    opened[0] = True  # La première boîte est déverrouillée par défaut.
    stack = [0]  # Commencez à explorer à partir de la boîte 0.

    while stack:
        current_box = stack.pop()  # Prendre la boîte actuelle.
        for key in boxes[current_box]:  # Explorer les clés dans cette boîte.
            if key < n and not opened[key]:  # Si la cle ouvre une nouvelle boîte.
                opened[key] = True  # marquer cette boîte comme ouverte.
                stack.append(key)  # ajouter la boîte à la pile pour exploration.

    return all(opened)  # Verifier Si toutes les boîtes sont ouvertes.
