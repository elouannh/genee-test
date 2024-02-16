
<img src="./assets/genee.png" alt="Image 1" width="150px">

# Test Technique pour Développeur Fullstack

## Contexte

Ce test est conçu pour évaluer non seulement vos compétences techniques en développement d'applications web mais aussi votre capacité à structurer votre code, à aborder des problématiques complexes et à travailler en équipe. L'objectif n'est pas simplement de réussir le test mais de démontrer votre processus de réflexion, votre méthodologie de travail et votre collaboration au sein d'une équipe.

## Technologies

- **Backend** : Python Flask.
- **Frontend** : Libre.
- **Base de données** : Libre.
- **Environnement de développement** : Libre.

## Mission

Votre tâche consiste à développer une page web intégrant un formulaire dynamique lié à une base de données. Cette base doit inclure une entité "Affaire" au minimum, et le formulaire doit permettre de créer ou modifier une "Affaire" avec les éléments suivants :

1. **Nom de l'Affaire** : Champ pour saisir le nom.
2. **Lieu** : Champ de sélection dynamique comprenant :
   - Département
   - Commune
   - Précision (champ texte libre)

### Spécificités du Formulaire :

- **Relation Département/Commune** : Le choix des communes doit être filtré en fonction du département sélectionné, en vous basant sur le fichier de référence fourni (fr-esr-referentiel-geographique.csv).
- **Sélection du Lieu** :
  - **Mode Unique** : Permet l'ajout d'un seul lieu.
  - **Mode Multiple** : Permet d'ajouter ou de retirer des lieux dynamiquement.

### Objectifs Pédagogiques :

- **Structuration du Code** : Votre code doit être bien organisé, commenté et facile à comprendre.
- **Approche de la Problématique** : Nous sommes intéressés par la manière dont vous abordez et résolvez les défis proposés.
- **Travail d'Équipe** : Votre capacité à collaborer et à contribuer au sein d'une équipe est essentielle.

### Contraintes Techniques :

Le formulaire doit être intuitif et ergonomique, avec des transitions fluides entre les modes de sélection de lieu. Le bouton "Valider" enregistre les données, qui doivent être préchargées au rechargement de la page.

## Livrables

Nous attendons un code source clair et documenté, reflétant votre capacité à aborder des problèmes complexes et à travailler de manière collaborative. Montrez-nous votre processus de pensée et votre méthodologie de travail à travers votre code.

Votre approche pour relever ce défi nous intéresse autant que le résultat final. Bonne chance !